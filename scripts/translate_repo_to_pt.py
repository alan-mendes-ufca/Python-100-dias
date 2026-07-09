#!/usr/bin/env python3
"""Translate repository text content to Portuguese without using API keys.

The script uses deep-translator's no-key GoogleTranslator client. It preserves
Markdown code fences, executable Python/SQL code, URLs, and inline code spans.
It is intentionally resumable because public translation endpoints can throttle
large repositories.
"""

from __future__ import annotations

import argparse
import ast
import io
import json
import re
import sys
import time
import tokenize
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import requests
from deep_translator import GoogleTranslator

_requests_get = requests.get


def requests_get_with_timeout(*args, **kwargs):
    kwargs.setdefault("timeout", 20)
    return _requests_get(*args, **kwargs)


requests.get = requests_get_with_timeout


SKIP_DIRS = {
    ".git",
    ".agents",
    ".codex",
    ".pytest_cache",
    ".venv",
    ".venv-translate",
    "__pycache__",
    "node_modules",
    "scripts",
}

TEXT_SUFFIXES = {".java", ".md", ".txt", ".html", ".ipynb", ".py", ".sql"}
MARKDOWN_SUFFIXES = {".md"}
PLAIN_TEXT_SUFFIXES = {".txt"}
SKIP_FILENAMES = {
    "dictionary.txt",
    "prime.txt",
    "requirements.txt",
}

TOKEN_RE = re.compile(r"ZXCVPH\d{5}ZXCV")
INLINE_PATTERNS = [
    re.compile(r"!\[[^\]\n]*\]\([^)]+\)"),
    re.compile(r"(?<!!)\[[^\]\n]+\]\([^)]+\)"),
    re.compile(r"`[^`\n]+`"),
    re.compile(r"https?://[^\s)>]+"),
    re.compile(r"<https?://[^>\n]+>"),
    re.compile(r"</?[A-Za-z][^>\n]*>"),
]


@dataclass
class Stats:
    files_seen: int = 0
    files_changed: int = 0
    requests: int = 0
    cache_hits: int = 0
    failures: int = 0


class CachedTranslator:
    def __init__(
        self,
        cache_path: Path,
        source: str,
        target: str,
        sleep: float,
        max_chars: int,
        dry_run: bool,
        stats: Stats,
    ) -> None:
        self.cache_path = cache_path
        self.sleep = sleep
        self.max_chars = max_chars
        self.dry_run = dry_run
        self.stats = stats
        self.translator = GoogleTranslator(source=source, target=target)
        self.cache: dict[str, str] = {}
        if cache_path.exists():
            self.cache = json.loads(cache_path.read_text(encoding="utf-8"))

    def save(self) -> None:
        if self.dry_run:
            return
        tmp = self.cache_path.with_suffix(self.cache_path.suffix + ".tmp")
        tmp.write_text(
            json.dumps(self.cache, ensure_ascii=False, indent=2, sort_keys=True),
            encoding="utf-8",
        )
        tmp.replace(self.cache_path)

    def translate(self, text: str) -> str:
        if not should_translate(text):
            return text
        protected, placeholders = protect_inline(text)
        if protected in self.cache:
            self.stats.cache_hits += 1
            return restore_inline(self.cache[protected], placeholders)
        chunks = split_chunks(protected, self.max_chars)
        translated_chunks: list[str] = []
        for chunk in chunks:
            if chunk in self.cache:
                self.stats.cache_hits += 1
                translated = self.cache[chunk]
            else:
                if self.dry_run:
                    translated = chunk
                else:
                    translated = self.translate_with_retry(chunk)
                self.cache[chunk] = translated
                self.stats.requests += 1
            translated_chunks.append(translated)
        translated = "\n".join(translated_chunks)
        self.cache[protected] = translated
        if self.stats.requests and self.stats.requests % 50 == 0:
            self.save()
            print(f"  progress: requests={self.stats.requests}", flush=True)
        return restore_inline(translated, placeholders)

    def translate_with_retry(self, chunk: str) -> str:
        last_exc: Exception | None = None
        for attempt in range(3):
            try:
                translated = self.translator.translate(chunk)
                time.sleep(self.sleep)
                return translated
            except Exception as exc:  # noqa: BLE001 - public endpoint can throttle.
                last_exc = exc
                time.sleep(self.sleep * (attempt + 2) + 1)
        assert last_exc is not None
        raise last_exc


def should_translate(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if not re.search(r"[A-Za-z]", stripped):
        return False
    if TOKEN_RE.fullmatch(stripped):
        return False
    return True


def protect_inline(text: str) -> tuple[str, dict[str, str]]:
    placeholders: dict[str, str] = {}

    def store(match: re.Match[str]) -> str:
        token = f"ZXCVPH{len(placeholders):05d}ZXCV"
        placeholders[token] = match.group(0)
        return token

    protected = text
    for pattern in INLINE_PATTERNS:
        protected = pattern.sub(store, protected)
    return protected, placeholders


def restore_inline(text: str, placeholders: dict[str, str]) -> str:
    restored = text
    for token, value in placeholders.items():
        restored = restored.replace(token, value)
        restored = restored.replace(token.lower(), value)
        restored = restored.replace(token.replace("ZXCV", "Z X C V"), value)
    return restored


def split_chunks(text: str, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text]
    parts = re.split(r"(?<=[.!?])\s+", text)
    chunks: list[str] = []
    current = ""
    for part in parts:
        candidate = f"{current} {part}".strip()
        if len(candidate) <= max_chars:
            current = candidate
            continue
        if current:
            chunks.append(current)
        if len(part) <= max_chars:
            current = part
        else:
            for i in range(0, len(part), max_chars):
                chunks.append(part[i : i + max_chars])
            current = ""
    if current:
        chunks.append(current)
    return chunks


def is_code_fence(line: str) -> bool:
    return bool(re.match(r"^\s*(```|~~~)", line))


def is_table_separator(line: str) -> bool:
    return bool(re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", line))


def translate_markdown(text: str, tr: CachedTranslator) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    paragraph: list[str] = []
    in_fence = False

    def flush_paragraph() -> None:
        if not paragraph:
            return
        raw = "".join(paragraph)
        trailing = "\n" if raw.endswith("\n") else ""
        joined = " ".join(line.strip() for line in paragraph if line.strip())
        out.append(tr.translate(joined) + trailing)
        paragraph.clear()

    for line in lines:
        if is_code_fence(line):
            flush_paragraph()
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if line.startswith(("    ", "\t")):
            flush_paragraph()
            out.append(line)
            continue
        if not line.strip():
            flush_paragraph()
            out.append(line)
            continue
        if is_structured_markdown_line(line):
            flush_paragraph()
            out.append(translate_markdown_line(line, tr))
            continue
        paragraph.append(line)
    flush_paragraph()
    return translate_markdown_links("".join(out), tr)


def translate_markdown_links(text: str, tr: CachedTranslator) -> str:
    def replace(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2)
        if label.startswith(("http://", "https://")) or not should_translate(label):
            return match.group(0)
        return f"[{tr.translate(label)}]({target})"

    return re.sub(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)", replace, text)


def is_structured_markdown_line(line: str) -> bool:
    stripped = line.strip()
    return (
        stripped.startswith("#")
        or stripped.startswith(">")
        or stripped.startswith("|")
        or stripped.startswith("<")
        or bool(re.match(r"^\s*(?:[-+*]|\d+[.)])\s+", line))
        or bool(re.match(r"^\s*\[[^\]]+\]:\s+", line))
        or bool(re.match(r"^\s*-{3,}\s*$", line))
    )


def translate_markdown_line(line: str, tr: CachedTranslator) -> str:
    newline = "\n" if line.endswith("\n") else ""
    body = line[:-1] if newline else line
    if is_table_separator(body) or re.match(r"^\s*-{3,}\s*$", body):
        return line
    if re.match(r"^\s*!\[[^\]\n]*\]\([^)]+\)\s*$", body):
        return line
    if re.match(r"^\s*<[^>]+>\s*$", body):
        return line
    if body.strip().startswith("|"):
        return translate_table_line(body, tr) + newline
    patterns = [
        r"^(\s{0,3}#{1,6}\s+)(.*?)(\s*#*\s*)$",
        r"^(\s*>+\s?)(.*)$",
        r"^(\s*(?:[-+*]|\d+[.)])\s+(?:\[[ xX]\]\s+)?)(.*)$",
    ]
    for pattern in patterns:
        match = re.match(pattern, body)
        if match:
            prefix = match.group(1)
            content = match.group(2)
            suffix = match.group(3) if match.lastindex and match.lastindex >= 3 else ""
            return f"{prefix}{tr.translate(content)}{suffix}{newline}"
    if re.match(r"^\s*\[[^\]]+\]:\s+", body):
        return line
    return tr.translate(body) + newline


def translate_table_line(line: str, tr: CachedTranslator) -> str:
    leading = line.startswith("|")
    trailing = line.endswith("|")
    cells = line.strip("|").split("|")
    translated = [tr.translate(cell.strip()) if cell.strip() else cell for cell in cells]
    result = " | ".join(translated)
    if leading:
        result = "| " + result
    if trailing:
        result += " |"
    return result


def translate_plain_text(text: str, tr: CachedTranslator) -> str:
    chunks = re.split(r"(\n\s*\n)", text)
    out = []
    for chunk in chunks:
        if re.fullmatch(r"\n\s*\n", chunk):
            out.append(chunk)
        else:
            out.append(tr.translate(" ".join(chunk.splitlines())))
    return "".join(out)


def translate_html(text: str, tr: CachedTranslator) -> str:
    from bs4 import BeautifulSoup, NavigableString

    soup = BeautifulSoup(text, "html.parser")
    skip = {"script", "style", "code", "pre", "kbd", "samp"}
    for node in soup.find_all(string=True):
        if not isinstance(node, NavigableString):
            continue
        if node.parent and node.parent.name in skip:
            continue
        original = str(node)
        if original.strip():
            node.replace_with(tr.translate(original))
    return str(soup)


def translate_notebook(text: str, tr: CachedTranslator) -> str:
    data = json.loads(text)
    changed = False
    for cell in data.get("cells", []):
        source = cell.get("source")
        if not isinstance(source, list):
            continue
        original = "".join(source)
        if cell.get("cell_type") == "markdown":
            translated = translate_markdown(original, tr)
        elif cell.get("cell_type") == "code":
            translated = translate_python_comments(original, tr)
        else:
            continue
        if translated != original:
            cell["source"] = translated.splitlines(keepends=True)
            changed = True
    if not changed:
        return text
    return json.dumps(data, ensure_ascii=False, indent=1) + "\n"


def translate_python_comments(text: str, tr: CachedTranslator) -> str:
    lines = text.splitlines(keepends=True)
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(text).readline))
    except tokenize.TokenError:
        return text
    replacements: list[tuple[int, int, str]] = []
    for token in tokens:
        if token.type != tokenize.COMMENT:
            continue
        row, col = token.start
        comment = token.string
        body = comment[1:].strip()
        if should_skip_code_comment(body):
            continue
        translated = "# " + tr.translate(body)
        replacements.append((row - 1, col, translated))
    for row, col, translated in reversed(replacements):
        line = lines[row]
        newline = "\n" if line.endswith("\n") else ""
        body = line[:-1] if newline else line
        lines[row] = body[:col] + translated + newline
    text = "".join(lines)
    return translate_python_docstrings(text, tr)


def translate_python_docstrings(text: str, tr: CachedTranslator) -> str:
    try:
        tree = ast.parse(text)
        tokens = list(tokenize.generate_tokens(io.StringIO(text).readline))
    except (SyntaxError, tokenize.TokenError):
        return text

    docstring_positions: set[tuple[int, int]] = set()
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if not isinstance(body, list) or not body:
            continue
        first = body[0]
        if (
            isinstance(first, ast.Expr)
            and isinstance(first.value, ast.Constant)
            and isinstance(first.value.value, str)
        ):
            docstring_positions.add((first.value.lineno, first.value.col_offset))

    if not docstring_positions:
        return text

    lines = text.splitlines(keepends=True)
    replacements: list[tuple[int, int, int, int, str]] = []
    for token in tokens:
        if token.type != tokenize.STRING:
            continue
        if token.start not in docstring_positions:
            continue
        try:
            value = ast.literal_eval(token.string)
        except (SyntaxError, ValueError):
            continue
        if not should_translate(value):
            continue
        translated_value = tr.translate(value)
        quote = choose_docstring_quote(token.string)
        escaped = translated_value.replace("\\", "\\\\").replace(quote, "\\" + quote)
        replacement = quote + escaped + quote
        replacements.append((*token.start, *token.end, replacement))

    for start_row, start_col, end_row, end_col, replacement in reversed(replacements):
        start_i = start_row - 1
        end_i = end_row - 1
        before = lines[start_i][:start_col]
        after = lines[end_i][end_col:]
        replacement_lines = replacement.splitlines(keepends=True)
        if len(replacement_lines) == 1:
            lines[start_i : end_i + 1] = [before + replacement_lines[0] + after]
        else:
            replacement_lines[0] = before + replacement_lines[0]
            replacement_lines[-1] = replacement_lines[-1] + after
            lines[start_i : end_i + 1] = replacement_lines
    return "".join(lines)


def choose_docstring_quote(token_string: str) -> str:
    lowered = token_string.lower()
    for prefix in ("r", "u", "f", "b"):
        lowered = lowered.removeprefix(prefix)
    stripped = lowered.lstrip()
    if stripped.startswith('"""'):
        return '"""'
    if stripped.startswith("'''"):
        return "'''"
    if stripped.startswith('"'):
        return '"'
    return "'"


def should_skip_code_comment(text: str) -> bool:
    lowered = text.lower()
    skip_prefixes = (
        "!",
        "/",
        "coding",
        "-*-",
        "type:",
        "noqa",
        "pragma:",
        "pylint:",
        "flake8:",
        "fmt:",
        "isort:",
    )
    return not should_translate(text) or lowered.startswith(skip_prefixes)


def translate_sql_comments(text: str, tr: CachedTranslator) -> str:
    def line_comment(match: re.Match[str]) -> str:
        prefix, body = match.group(1), match.group(2).strip()
        if should_skip_code_comment(body):
            return match.group(0)
        return f"{prefix} {tr.translate(body)}"

    text = re.sub(r"(^\s*--)(.*)$", line_comment, text, flags=re.MULTILINE)

    def block_comment(match: re.Match[str]) -> str:
        body = match.group(1).strip()
        if should_skip_code_comment(body):
            return match.group(0)
        return "/* " + tr.translate(body) + " */"

    return re.sub(r"/\*(.*?)\*/", block_comment, text, flags=re.DOTALL)


def translate_java_comments(text: str, tr: CachedTranslator) -> str:
    def line_comment(match: re.Match[str]) -> str:
        prefix, body = match.group(1), match.group(2).strip()
        if should_skip_code_comment(body):
            return match.group(0)
        return f"{prefix} {tr.translate(body)}"

    text = re.sub(r"(^\s*//)(.*)$", line_comment, text, flags=re.MULTILINE)

    def block_comment(match: re.Match[str]) -> str:
        block = match.group(0)
        if "\n" not in block:
            body = match.group(1).strip()
            if should_skip_code_comment(body):
                return block
            return "/* " + tr.translate(body) + " */"
        lines = block.splitlines()
        out: list[str] = []
        for line in lines:
            content = re.match(r"^(\s*\*\s?)(.+?)(\s*)$", line)
            if content and should_translate(content.group(2)):
                out.append(content.group(1) + tr.translate(content.group(2).strip()) + content.group(3))
            else:
                out.append(line)
        return "\n".join(out)

    return re.sub(r"/\*(.*?)\*/", block_comment, text, flags=re.DOTALL)


def translate_file(path: Path, tr: CachedTranslator, markdown_links_only: bool = False) -> bool:
    original = path.read_text(encoding="utf-8")
    suffix = path.suffix.lower()
    if markdown_links_only:
        if suffix not in MARKDOWN_SUFFIXES:
            return False
        translated = translate_markdown_links(original, tr)
    elif suffix in MARKDOWN_SUFFIXES:
        translated = translate_markdown(original, tr)
    elif suffix in PLAIN_TEXT_SUFFIXES:
        translated = translate_plain_text(original, tr)
    elif suffix == ".html":
        translated = translate_html(original, tr)
    elif suffix == ".ipynb":
        translated = translate_notebook(original, tr)
    elif suffix == ".py":
        translated = translate_python_comments(original, tr)
    elif suffix == ".sql":
        translated = translate_sql_comments(original, tr)
    elif suffix == ".java":
        translated = translate_java_comments(original, tr)
    else:
        return False
    if translated == original:
        return False
    if not tr.dry_run:
        path.write_text(translated, encoding="utf-8")
    return True


def iter_files(root: Path, paths: Iterable[str]) -> Iterable[Path]:
    if paths:
        for raw in paths:
            path = (root / raw).resolve()
            if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
                yield path
        return
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.name in SKIP_FILENAMES:
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        yield path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="Optional repo-relative files to translate")
    parser.add_argument("--paths-from", help="Read additional repo-relative paths from a text file")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--source", default="auto", help="Source language")
    parser.add_argument("--target", default="pt", help="Target language")
    parser.add_argument("--cache", default=".translation-cache-pt-v2.json")
    parser.add_argument("--sleep", type=float, default=0.25)
    parser.add_argument("--max-chars", type=int, default=4200)
    parser.add_argument("--limit", type=int, default=0, help="Stop after N candidate files")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--markdown-links-only", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if args.paths_from:
        paths_file = Path(args.paths_from)
        args.paths.extend(
            line.strip()
            for line in paths_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    stats = Stats()
    tr = CachedTranslator(
        root / args.cache,
        args.source,
        args.target,
        args.sleep,
        args.max_chars,
        args.dry_run,
        stats,
    )
    try:
        for path in iter_files(root, args.paths):
            stats.files_seen += 1
            rel = path.relative_to(root)
            print(f"[{stats.files_seen}] {rel}", flush=True)
            try:
                if translate_file(path, tr, args.markdown_links_only):
                    stats.files_changed += 1
                    print(f"  changed: {rel}", flush=True)
            except Exception as exc:  # noqa: BLE001 - keep batch resumable.
                stats.failures += 1
                print(f"  failed: {rel}: {exc}", file=sys.stderr, flush=True)
            if args.limit and stats.files_seen >= args.limit:
                break
    finally:
        tr.save()
    print(
        "done: "
        f"seen={stats.files_seen} changed={stats.files_changed} "
        f"requests={stats.requests} cache_hits={stats.cache_hits} "
        f"failures={stats.failures}",
        flush=True,
    )
    return 1 if stats.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Verifica destinos locais de links Markdown e imagens HTML."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)')
HTML_SOURCE = re.compile(r'<(?:img|source)\s+[^>]*\bsrc=["\']([^"\']+)["\']', re.I)
FENCED_CODE = re.compile(r'^```.*?^```', re.M | re.S)
EXTERNAL_PREFIXES = ('https://', 'http://', 'mailto:', 'tel:', 'data:')


def local_destination(target: str) -> str | None:
    target = target.strip('<>').split('#', maxsplit=1)[0].split('?', maxsplit=1)[0]
    if not target or target.startswith('/') or target.startswith(EXTERNAL_PREFIXES):
        return None
    return unquote(target)


def main() -> int:
    errors: list[str] = []
    checked = 0
    for document in sorted(ROOT.rglob('*.md')):
        text = FENCED_CODE.sub('', document.read_text(encoding='utf-8'))
        targets = MARKDOWN_LINK.findall(text) + HTML_SOURCE.findall(text)
        for target in targets:
            destination = local_destination(target)
            if destination is None:
                continue
            checked += 1
            resolved = (document.parent / destination).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f'{document.relative_to(ROOT)}: link leaves the repository: {target}'
                )
                continue
            if not resolved.exists():
                errors.append(
                    f'{document.relative_to(ROOT)}: missing local target: {target}'
                )

    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1

    print(f'Validated {checked} local Markdown targets.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

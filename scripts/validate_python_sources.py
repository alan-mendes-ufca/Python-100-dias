"""Valida a sintaxe dos exemplos Python sem importar suas dependências."""
from __future__ import annotations

import ast
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRECTORIES = {'.git', '.venv', 'venv', '__pycache__'}


def main() -> int:
    errors: list[str] = []
    sources = sorted(
        path
        for path in ROOT.rglob('*.py')
        if not any(part in IGNORED_DIRECTORIES for part in path.parts)
    )
    for path in sources:
        try:
            ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
        except SyntaxError as error:
            location = f'{path.relative_to(ROOT)}:{error.lineno}:{error.offset}'
            errors.append(f'{location}: {error.msg}')

    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1

    print(f'Validated Python syntax in {len(sources)} files.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Read the canonical Society in Silico TOC from repo-root _quarto.yml."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Iterator

import yaml


def get_repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_quarto_config() -> dict:
    quarto_path = get_repo_root() / "_quarto.yml"
    return yaml.safe_load(quarto_path.read_text())


def resolve_content_file(file_path: str) -> str:
    path = Path(file_path)
    if path.name == "index.md" and path.parent == Path("."):
        thesis_path = Path("manuscript/front-matter/00-thesis.md")
        if (get_repo_root() / thesis_path).exists():
            return thesis_path.as_posix()
    return file_path


def is_manuscript_chapter(file_path: str) -> bool:
    return file_path.startswith("manuscript/") and not file_path.endswith("00-outline.md")


def iter_manuscript_files(config: dict) -> Iterator[str]:
    chapters = config.get("book", {}).get("chapters", [])
    for entry in chapters:
        if isinstance(entry, str):
            if is_manuscript_chapter(entry):
                yield resolve_content_file(entry)
            continue

        for child in entry.get("chapters", []) or []:
            if is_manuscript_chapter(child):
                yield resolve_content_file(child)


def to_output_path(file_path: str, absolute: bool) -> str:
    resolved = (get_repo_root() / file_path).resolve()
    if absolute:
        return str(resolved)
    return os.path.relpath(resolved, start=Path.cwd())


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Emit manuscript chapter files in the order defined by _quarto.yml."
    )
    parser.add_argument(
        "--absolute",
        action="store_true",
        help="Print absolute paths instead of paths relative to the current directory.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero if _quarto.yml references any missing manuscript files.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the ordered manuscript files as JSON.",
    )
    args = parser.parse_args()

    files = list(iter_manuscript_files(load_quarto_config()))

    if args.check:
        missing = [file_path for file_path in files if not (get_repo_root() / file_path).exists()]
        if missing:
            for file_path in missing:
                print(f"MISSING {file_path}")
            raise SystemExit(1)

        print(f"OK {len(files)} manuscript files in _quarto.yml")
        return

    if args.json:
        print(json.dumps({"files": files}, indent=2))
        return

    print("\n".join(to_output_path(file_path, absolute=args.absolute) for file_path in files))


if __name__ == "__main__":
    main()

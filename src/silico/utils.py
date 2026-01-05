"""Shared utilities for Society in Silico tooling."""

import re
from pathlib import Path
from typing import Optional


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown file.

    Args:
        content: Markdown file content

    Returns:
        Dictionary of frontmatter fields, or empty dict if none found
    """
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return {}

    try:
        import yaml
        return yaml.safe_load(match.group(1)) or {}
    except (ImportError, Exception):
        # Fallback to simple parsing if yaml not available
        frontmatter = {}
        for line in match.group(1).split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip()

                # Parse lists [1, 2, 3]
                if value.startswith('[') and value.endswith(']'):
                    value = [int(x.strip()) for x in value[1:-1].split(',') if x.strip()]
                # Parse quoted strings
                elif value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                # Parse numbers
                elif value.isdigit():
                    value = int(value)

                frontmatter[key] = value
        return frontmatter


def extract_title(content: str) -> str:
    """Extract the first H1 title from markdown.

    Args:
        content: Markdown file content

    Returns:
        Title text, or "Untitled" if none found
    """
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1) if match else "Untitled"


def get_manuscript_chapters(manuscript_dir: Path) -> list[dict]:
    """Get all chapters from manuscript in reading order.

    Returns list of dicts with keys: path, title, number, part

    Order:
    1. front-matter
    2. part-1-origins
    3. part-2-building
    4. part-3-future

    Args:
        manuscript_dir: Path to manuscript directory

    Returns:
        List of chapter info dicts
    """
    chapters = []
    chapter_num = 0

    parts = [
        ("Front Matter", "front-matter"),
        ("Part I: Origins", "part-1-origins"),
        ("Part II: Building", "part-2-building"),
        ("Part III: Future", "part-3-future"),
    ]

    for part_name, part_dir in parts:
        part_path = manuscript_dir / part_dir
        if not part_path.exists():
            continue

        md_files = sorted(part_path.glob("*.md"))

        for md_file in md_files:
            # Skip outline files
            if "outline" in md_file.name.lower():
                continue

            content = md_file.read_text()
            title = extract_title(content)

            # Extract chapter number from filename (e.g., "01-intro.md" -> 1)
            number_match = re.match(r'(\d+)', md_file.name)
            file_number = int(number_match.group(1)) if number_match else 0

            chapter_num += 1
            chapters.append({
                'path': md_file,
                'title': title,
                'number': chapter_num,
                'file_number': file_number,
                'part': part_name,
                'part_dir': part_dir,
            })

    return chapters


def get_research_notes(research_dir: Path, with_frontmatter: bool = False) -> list[dict]:
    """Get all research notes, optionally filtered by those with frontmatter.

    Args:
        research_dir: Path to research directory
        with_frontmatter: If True, only return notes with tracking frontmatter

    Returns:
        List of note info dicts with keys: path, stem, title, frontmatter
    """
    notes = []

    for md_file in research_dir.rglob("*.md"):
        if md_file.name == 'chapter-mapping.md':
            continue

        content = md_file.read_text()
        frontmatter = parse_frontmatter(content)

        if with_frontmatter and not frontmatter:
            continue

        notes.append({
            'path': md_file,
            'stem': md_file.stem,
            'title': extract_title(content),
            'frontmatter': frontmatter,
        })

    return notes

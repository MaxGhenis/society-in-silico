"""Manuscript processing utilities for Society in Silico.

Handles chapter discovery, content extraction, and manuscript structure.
"""

import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Chapter:
    """Represents a book chapter with metadata."""

    path: Path
    title: str
    number: int  # Sequential chapter number (1, 2, 3...)
    file_number: int  # Number from filename (01, 02, 03...)
    part: str  # "Front Matter", "Part I: Origins", etc.
    part_dir: str  # Directory name: "front-matter", "part-1-origins"

    def read_content(self) -> str:
        """Read raw markdown content."""
        return self.path.read_text()

    def extract_clean_text(self) -> str:
        """Extract text with markdown stripped."""
        from .formatting import strip_markdown
        return strip_markdown(self.read_content())

    def character_count(self) -> int:
        """Count characters in clean text."""
        return len(self.extract_clean_text())

    def word_count(self) -> int:
        """Count words in clean text."""
        return len(self.extract_clean_text().split())


def extract_title(content: str) -> str:
    """Extract the first H1 title from markdown.

    Args:
        content: Markdown file content

    Returns:
        Title text, or "Untitled" if none found
    """
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    return match.group(1) if match else "Untitled"


def get_chapters(manuscript_dir: Path) -> List[Chapter]:
    """Get all chapters from manuscript in reading order.

    Order:
    1. front-matter (preface, thesis, introduction)
    2. part-1-origins
    3. part-2-building
    4. part-3-future

    Within each part, files are sorted by numeric prefix.
    Excludes outline files (00-outline.md).

    Args:
        manuscript_dir: Path to manuscript directory

    Returns:
        List of Chapter objects in reading order
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
            if "outline" in md_file.name.lower() or md_file.name.startswith("00-"):
                continue

            content = md_file.read_text()
            title = extract_title(content)

            # Extract chapter number from filename (e.g., "01-intro.md" -> 1)
            number_match = re.match(r'(\d+)', md_file.name)
            file_number = int(number_match.group(1)) if number_match else 0

            chapter_num += 1
            chapters.append(Chapter(
                path=md_file,
                title=title,
                number=chapter_num,
                file_number=file_number,
                part=part_name,
                part_dir=part_dir,
            ))

    return chapters


def get_chapter_by_number(manuscript_dir: Path, chapter_num: int) -> Optional[Chapter]:
    """Get a specific chapter by its file number.

    Args:
        manuscript_dir: Path to manuscript directory
        chapter_num: Chapter file number (from filename)

    Returns:
        Chapter object or None if not found
    """
    chapters = get_chapters(manuscript_dir)
    for ch in chapters:
        if ch.file_number == chapter_num:
            return ch
    return None


def calculate_manuscript_stats(manuscript_dir: Path) -> dict:
    """Calculate statistics for the entire manuscript.

    Args:
        manuscript_dir: Path to manuscript directory

    Returns:
        Dict with word counts, character counts, chapter counts
    """
    chapters = get_chapters(manuscript_dir)

    stats = {
        'total_chapters': len(chapters),
        'total_words': sum(ch.word_count() for ch in chapters),
        'total_characters': sum(ch.character_count() for ch in chapters),
        'by_part': {}
    }

    # Group by part
    for ch in chapters:
        if ch.part not in stats['by_part']:
            stats['by_part'][ch.part] = {
                'chapters': 0,
                'words': 0,
                'characters': 0
            }
        stats['by_part'][ch.part]['chapters'] += 1
        stats['by_part'][ch.part]['words'] += ch.word_count()
        stats['by_part'][ch.part]['characters'] += ch.character_count()

    return stats

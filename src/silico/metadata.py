"""Metadata extraction and management for Society in Silico.

Handles YAML frontmatter parsing and research note tracking.
"""

import re
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class ResearchNote:
    """Represents a research note with tracking metadata."""

    path: Path
    stem: str
    title: str
    frontmatter: Dict

    @property
    def chapters(self) -> List[int]:
        """Get list of chapters this concept appears in."""
        return self.frontmatter.get('chapters', [])

    @property
    def primary_chapter(self) -> Optional[int]:
        """Get the primary chapter for this concept."""
        return self.frontmatter.get('primary_chapter')

    @property
    def narrative_role(self) -> str:
        """Get the narrative role description."""
        return self.frontmatter.get('narrative_role', '')


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


def get_research_notes(
    research_dir: Path,
    with_tracking: bool = False
) -> List[ResearchNote]:
    """Get all research notes, optionally filtered by tracking frontmatter.

    Args:
        research_dir: Path to research directory
        with_tracking: If True, only return notes with tracking frontmatter

    Returns:
        List of ResearchNote objects
    """
    notes = []

    for md_file in research_dir.rglob("*.md"):
        # Skip chapter mapping file
        if md_file.name == 'chapter-mapping.md':
            continue

        content = md_file.read_text()
        frontmatter = parse_frontmatter(content)

        # Filter by tracking if requested
        if with_tracking and not frontmatter.get('chapters'):
            continue

        from .manuscript import extract_title
        notes.append(ResearchNote(
            path=md_file,
            stem=md_file.stem,
            title=extract_title(content),
            frontmatter=frontmatter,
        ))

    return notes


def load_tracked_concepts(research_dir: Path) -> Dict[str, ResearchNote]:
    """Load all concepts with tracking frontmatter.

    Args:
        research_dir: Path to research directory

    Returns:
        Dict mapping concept stem to ResearchNote
    """
    notes = get_research_notes(research_dir, with_tracking=True)
    return {note.stem: note for note in notes}

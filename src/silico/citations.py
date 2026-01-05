"""Citation management for Society in Silico.

Handles BibTeX parsing, citation validation, and reference tracking.
"""

import re
from pathlib import Path
from typing import Set, List, Dict


def get_bibtex_keys(bib_file: Path) -> Set[str]:
    """Extract all citation keys from a BibTeX file.

    Args:
        bib_file: Path to references.bib file

    Returns:
        Set of citation keys
    """
    if not bib_file.exists():
        return set()

    content = bib_file.read_text()
    # Match @type{key, ...}
    return set(re.findall(r'@\w+\{(\w+),', content))


def find_missing_citations(
    manuscript_dir: Path,
    bib_file: Path
) -> Dict[str, List[str]]:
    """Find citations used in manuscript but missing from BibTeX.

    Args:
        manuscript_dir: Path to manuscript directory
        bib_file: Path to references.bib file

    Returns:
        Dict mapping chapter paths to lists of missing citation keys
    """
    from .manuscript import get_chapters
    from .formatting import extract_citations

    bib_keys = get_bibtex_keys(bib_file)
    missing = {}

    chapters = get_chapters(manuscript_dir)
    for ch in chapters:
        content = ch.read_content()
        used_citations = set(extract_citations(content))
        missing_in_chapter = used_citations - bib_keys

        if missing_in_chapter:
            missing[str(ch.path)] = list(missing_in_chapter)

    return missing


def find_unused_citations(
    manuscript_dir: Path,
    bib_file: Path
) -> List[str]:
    """Find BibTeX entries not cited anywhere in manuscript.

    Args:
        manuscript_dir: Path to manuscript directory
        bib_file: Path to references.bib file

    Returns:
        List of unused citation keys
    """
    from .manuscript import get_chapters
    from .formatting import extract_citations

    bib_keys = get_bibtex_keys(bib_file)
    used_citations = set()

    chapters = get_chapters(manuscript_dir)
    for ch in chapters:
        content = ch.read_content()
        used_citations.update(extract_citations(content))

    return list(bib_keys - used_citations)

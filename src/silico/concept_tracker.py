"""Concept tracker - validates consistency of concept/people tracking across manuscript.

Enforces concept tracking discipline similar to Robert Caro's filing system or Obsidian Dataview.
Ensures no duplication without proper tracking frontmatter.
"""

import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set

from .utils import parse_frontmatter, extract_title, get_manuscript_chapters, get_research_notes


def extract_model_mentions(content: str) -> Set[str]:
    """Extract model/tool names mentioned in text.

    Looks for common model patterns in all caps or specific forms.
    """
    models = set()
    patterns = [
        r'\b(TAXSIM|EUROMOD|UKMOD|MINT|DYNASIM|CBOLT|CORSIM)\b',
        r'\b(Tax-Calculator|OpenFisca|PolicyEngine|OG-USA|FRB/US)\b',
        r'\b(TAXBEN|Tax-Data|TaxBrain|Cost-of-Capital-Calculator)\b',
    ]

    for pattern in patterns:
        models.update(re.findall(pattern, content))

    return models


def extract_wiki_links(content: str) -> Set[str]:
    """Extract [[wiki-links]] from text."""
    return set(re.findall(r'\[\[([^\]]+)\]\]', content))


def analyze_chapter_references(chapter: dict) -> Dict:
    """Analyze what concepts/models a chapter references.

    Args:
        chapter: Chapter dict from get_manuscript_chapters()

    Returns:
        Dict with chapter info and extracted references
    """
    content = chapter['path'].read_text()

    return {
        'path': chapter['path'],
        'chapter': chapter['file_number'],
        'title': chapter['title'],
        'models': extract_model_mentions(content),
        'wiki_links': extract_wiki_links(content),
    }


def find_concept_duplications(
    chapters: List[Dict],
    tracked: Dict[str, Dict]
) -> List[Dict]:
    """Find concepts appearing in multiple chapters without proper tracking.

    Args:
        chapters: List of chapter analysis dicts
        tracked: Dict of tracked entities from research notes

    Returns:
        List of issue dicts
    """
    issues = []

    # Build inverse map: concept -> [chapters where it appears]
    concept_appearances = defaultdict(list)

    for ch in chapters:
        chapter_id = ch['chapter']

        # Check models
        for model in ch['models']:
            concept_appearances[model].append(chapter_id)

        # Check wiki-linked concepts
        for link in ch['wiki_links']:
            concept_appearances[link].append(chapter_id)

    # Check each concept
    for concept, appearances in concept_appearances.items():
        if len(appearances) > 1:
            # Multiple appearances - is it tracked?
            concept_lower = concept.lower().replace(' ', '-')

            if concept_lower not in tracked and concept not in tracked:
                issues.append({
                    'type': 'untracked_duplication',
                    'concept': concept,
                    'chapters': appearances,
                    'message': f"'{concept}' appears in chapters {appearances} but has no tracking frontmatter"
                })
            else:
                # Found in tracked - check consistency
                tracked_data = tracked.get(concept_lower) or tracked.get(concept)

                if not tracked_data.get('primary_chapter'):
                    issues.append({
                        'type': 'missing_primary',
                        'concept': concept,
                        'chapters': appearances,
                        'message': f"'{concept}' appears in multiple chapters but no primary_chapter marked"
                    })
                else:
                    # Check if tracked chapters match actual appearances
                    declared = set(tracked_data['chapters'])
                    actual = set(appearances)
                    if declared != actual:
                        issues.append({
                            'type': 'tracking_mismatch',
                            'concept': concept,
                            'declared': list(declared),
                            'actual': list(actual),
                            'message': f"'{concept}' tracking mismatch: declared {declared}, actual {actual}"
                        })

    return issues


def generate_tracking_report(
    chapters: List[Dict],
    tracked: Dict[str, Dict],
    repo_root: Path
) -> str:
    """Generate comprehensive tracking report.

    Args:
        chapters: List of chapter analysis dicts
        tracked: Dict of tracked entities
        repo_root: Repository root path

    Returns:
        Formatted report string
    """
    lines = []
    lines.append("=" * 70)
    lines.append("CONCEPT TRACKING REPORT")
    lines.append("=" * 70)
    lines.append("")

    # Summary
    lines.append(f"📚 Chapters analyzed: {len(chapters)}")
    lines.append(f"✅ Tracked entities: {len(tracked)}")
    lines.append("")

    # Tracked entities by chapter
    lines.append("📖 Tracked Entities by Primary Chapter:")
    lines.append("-" * 70)

    by_chapter = defaultdict(list)
    for concept_key, data in tracked.items():
        primary = data.get('primary_chapter', '?')
        by_chapter[primary].append({
            'name': concept_key,
            'title': data.get('title', concept_key),
            'chapters': data.get('chapters', []),
            'role': data.get('narrative_role', '')
        })

    for ch_num in sorted(by_chapter.keys()):
        lines.append(f"\nChapter {ch_num}:")
        for entity in sorted(by_chapter[ch_num], key=lambda x: x['name']):
            appearances = f"(also in {entity['chapters']})" if len(entity['chapters']) > 1 else ""
            role = f" - {entity['role'][:60]}" if entity['role'] else ""
            lines.append(f"  • {entity['title'][:40]}{role} {appearances}")

    lines.append("")
    lines.append("=" * 70)

    return "\n".join(lines)


def load_tracked_entities(research_dir: Path) -> Dict[str, Dict]:
    """Load all research notes with tracking frontmatter.

    Args:
        research_dir: Path to research directory

    Returns:
        Dict mapping note stem to frontmatter data
    """
    tracked = {}

    notes = get_research_notes(research_dir, with_frontmatter=True)

    for note in notes:
        tracked[note['stem']] = {
            'path': note['path'],
            'title': note['title'],
            **note['frontmatter']
        }

    return tracked


def main():
    """CLI entry point for concept tracking validation."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Track concepts and people across manuscript"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate full tracking report"
    )
    parser.add_argument(
        "--manuscript",
        type=Path,
        default=Path.cwd() / "manuscript",
        help="Path to manuscript directory"
    )
    parser.add_argument(
        "--research",
        type=Path,
        default=Path.cwd() / "research",
        help="Path to research directory"
    )

    args = parser.parse_args()

    # Load data
    manuscript_chapters = get_manuscript_chapters(args.manuscript)
    chapters = [analyze_chapter_references(ch) for ch in manuscript_chapters]
    tracked = load_tracked_entities(args.research)

    if args.report:
        print(generate_tracking_report(chapters, tracked, Path.cwd()))
        return

    # Default: check for issues
    issues = find_concept_duplications(chapters, tracked)

    if not issues:
        print("\n✅ No tracking issues found!")
        print(f"   {len(tracked)} entities properly tracked across {len(chapters)} chapters")
    else:
        print(f"\n⚠️  Found {len(issues)} tracking issues:\n")

        for issue in issues:
            print(f"  {issue['type'].upper()}: {issue['message']}")

        print(f"\n💡 Run with --report for full tracking overview")


if __name__ == "__main__":
    main()

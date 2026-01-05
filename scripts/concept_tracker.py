#!/usr/bin/env python3
"""
Concept Tracker - Validates consistency of concept/people tracking across manuscript.

Extends book_dashboard.py to enforce concept tracking discipline similar to
Robert Caro's filing system or Obsidian Dataview.

Usage:
    python scripts/concept_tracker.py              # Check for issues
    python scripts/concept_tracker.py --report     # Full tracking report
    python scripts/concept_tracker.py --untrac ked  # List untracked entities
"""

import re
import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple

REPO_ROOT = Path(__file__).parent.parent
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
RESEARCH_DIR = REPO_ROOT / "research"


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown file."""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def extract_people_mentions(content: str) -> Set[str]:
    """Extract people mentioned in manuscript (heuristic)."""
    # Look for capitalized names (First Last pattern)
    # Filter out common false positives
    names = set()
    patterns = [
        r'\b([A-Z][a-z]+)\s+([A-Z][a-z]+)\b',  # First Last
        r'\*\*([A-Z][a-z]+\s+[A-Z][a-z]+)\*\*',  # **Name**
    ]

    false_positives = {
        'United States', 'United Kingdom', 'New Zealand', 'Universal Basic',
        'Child Tax', 'Basic Income', 'Open Source', 'Policy Simulation',
        'Tax Foundation', 'Urban Institute', 'Google Analytics', 'YouTube Go',
        'Democratic Party', 'Republican Party'
    }

    for pattern in patterns:
        for match in re.finditer(pattern, content):
            name = match.group(1) if pattern.startswith(r'\b') else match.group(1)
            if ' ' in name or len(match.groups()) > 1:
                full_name = ' '.join(match.groups()) if len(match.groups()) > 1 else name
                if full_name not in false_positives:
                    names.add(full_name)

    return names


def extract_model_mentions(content: str) -> Set[str]:
    """Extract model/tool names mentioned."""
    models = set()
    # Common model names in all caps or specific patterns
    patterns = [
        r'\b(TAXSIM|EUROMOD|UKMOD|MINT|DYNASIM|CBOLT|CORSIM)\b',
        r'\b(Tax-Calculator|OpenFisca|PolicyEngine|OG-USA|FRB/US)\b',
        r'\b(TAXBEN|Tax-Data|TaxBrain|Cost-of-Capital-Calculator)\b',
    ]

    for pattern in patterns:
        models.update(re.findall(pattern, content))

    return models


def analyze_chapter_references(md_file: Path) -> Dict:
    """Analyze what concepts/people a chapter references."""
    content = md_file.read_text()

    # Get chapter number from filename
    match = re.match(r'(\d+)', md_file.name)
    chapter_num = int(match.group(1)) if match else 0

    return {
        'path': str(md_file.relative_to(MANUSCRIPT_DIR)),
        'chapter': chapter_num,
        'title': extract_title(content),
        'people': extract_people_mentions(content),
        'models': extract_model_mentions(content),
        'wiki_links': set(re.findall(r'\[\[([^\]]+)\]\]', content)),
    }


def extract_title(content: str) -> str:
    """Extract H1 title from markdown."""
    match = re.search(r'^# (.+)$', content, re.MULTILINE)
    return match.group(1) if match else "Untitled"


def load_tracked_entities() -> Dict[str, Dict]:
    """Load all research notes with tracking frontmatter."""
    tracked = {}

    for md_file in RESEARCH_DIR.rglob("*.md"):
        if md_file.name == 'chapter-mapping.md':
            continue

        content = md_file.read_text()
        frontmatter = parse_frontmatter(content)

        if frontmatter.get('chapters'):
            key = md_file.stem
            tracked[key] = {
                'path': str(md_file.relative_to(RESEARCH_DIR)),
                'chapters': frontmatter.get('chapters', []),
                'primary_chapter': frontmatter.get('primary_chapter'),
                'narrative_role': frontmatter.get('narrative_role', ''),
                'title': extract_title(content),
            }

    return tracked


def find_concept_duplications(chapters: List[Dict], tracked: Dict[str, Dict]) -> List[Dict]:
    """Find concepts that appear in multiple chapters without proper tracking."""
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
            if concept not in tracked:
                issues.append({
                    'type': 'untracked_duplication',
                    'concept': concept,
                    'chapters': appearances,
                    'message': f"'{concept}' appears in chapters {appearances} but has no tracking frontmatter"
                })
            elif not tracked[concept].get('primary_chapter'):
                issues.append({
                    'type': 'missing_primary',
                    'concept': concept,
                    'chapters': appearances,
                    'message': f"'{concept}' appears in multiple chapters but no primary_chapter marked"
                })
            else:
                # Check if tracked chapters match actual appearances
                declared = set(tracked[concept]['chapters'])
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


def find_untracked_entities(chapters: List[Dict], tracked: Dict[str, Dict]) -> Dict[str, Set[str]]:
    """Find people and models mentioned but not tracked."""
    all_people = set()
    all_models = set()

    for ch in chapters:
        all_people.update(ch['people'])
        all_models.update(ch['models'])

    # Filter out what's already tracked
    tracked_keys_lower = {k.lower().replace('-', ' ') for k in tracked.keys()}

    untracked_people = {
        p for p in all_people
        if p.lower() not in tracked_keys_lower and p.replace(' ', '-').lower() not in tracked.keys()
    }

    untracked_models = {
        m for m in all_models
        if m.lower() not in tracked_keys_lower and m.replace(' ', '-').lower() not in tracked.keys()
    }

    return {
        'people': untracked_people,
        'models': untracked_models,
    }


def generate_tracking_report(chapters: List[Dict], tracked: Dict[str, Dict]) -> str:
    """Generate a comprehensive tracking report."""
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
    lines.append("📖 Tracked Entities by Chapter:")
    lines.append("-" * 70)

    by_chapter = defaultdict(list)
    for concept, data in tracked.items():
        primary = data.get('primary_chapter', '?')
        by_chapter[primary].append({
            'name': concept,
            'title': data.get('title', concept),
            'chapters': data['chapters']
        })

    for ch_num in sorted(by_chapter.keys()):
        lines.append(f"\nChapter {ch_num}:")
        for entity in sorted(by_chapter[ch_num], key=lambda x: x['name']):
            appearances = f"(also in {entity['chapters']})" if len(entity['chapters']) > 1 else ""
            lines.append(f"  • {entity['title'][:50]} {appearances}")

    lines.append("")
    lines.append("=" * 70)

    return "\n".join(lines)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Track concepts and people across manuscript")
    parser.add_argument("--report", action="store_true", help="Generate full tracking report")
    parser.add_argument("--untracked", action="store_true", help="Show untracked entities")
    args = parser.parse_args()

    # Load data
    chapters = []
    for part_dir in MANUSCRIPT_DIR.iterdir():
        if part_dir.is_dir():
            for md_file in sorted(part_dir.glob("*.md")):
                if not md_file.name.startswith("00-"):
                    chapters.append(analyze_chapter_references(md_file))

    tracked = load_tracked_entities()

    if args.report:
        print(generate_tracking_report(chapters, tracked))
        return

    if args.untracked:
        untracked = find_untracked_entities(chapters, tracked)
        print("\n🔍 UNTRACKED ENTITIES")
        print("=" * 70)
        print(f"\nPeople mentioned but not tracked ({len(untracked['people'])}):")
        for person in sorted(untracked['people']):
            print(f"  • {person}")
        print(f"\nModels mentioned but not tracked ({len(untracked['models'])}):")
        for model in sorted(untracked['models']):
            print(f"  • {model}")
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

        print(f"\n💡 Run with --untracked to see what needs tracking frontmatter")
        print(f"💡 Run with --report for full tracking overview")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Concept Tracker - Validates consistency of concept/people tracking across manuscript.

Extends book_dashboard.py to enforce concept tracking discipline similar to
Robert Caro's filing system or Obsidian Dataview.

Usage:
    python scripts/concept_tracker.py              # Check for issues
    python scripts/concept_tracker.py --report     # Full tracking report
    python scripts/concept_tracker.py --untracked  # List untracked entities
    python scripts/concept_tracker.py --semantic    # Detect semantic duplications
"""

import re
import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Tuple

REPO_ROOT = Path(__file__).parent.parent
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
RESEARCH_DIR = REPO_ROOT / "research"

# Patterns that indicate a concept is being introduced/defined (not just mentioned)
INTRODUCTION_PATTERNS = [
    r'{concept}\s+(?:is|was|are|were)\s+(?:a|an|the)\b',       # "X is a ..."
    r'{concept},\s+(?:a|an|the)\s+',                            # "X, a ..."
    r'(?:called|named|known as|dubbed)\s+{concept}',            # "called X"
    r'{concept}\s*[-—]\s*(?:a|an|the)\s+',                      # "X — a ..."
    r'(?:introduced|launched|created|founded|built|developed)\s+{concept}', # "launched X"
    r'{concept}\s+(?:launched|emerged|appeared|began)\b',        # "X launched ..."
    r'(?:What|who)\s+(?:is|was)\s+{concept}',                   # "What is X"
]

# Patterns that indicate explanation/description (extended context around a concept)
EXPLANATION_PATTERNS = [
    r'{concept}[^.]*?(?:model|tool|system|platform|framework|calculator|simulator)',
    r'{concept}[^.]*?(?:simulates?|calculates?|estimates?|projects?|analyzes?)',
    r'{concept}[^.]*?(?:enables?|allows?|provides?|supports?|covers?)',
]


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
    names = set()
    patterns = [
        r'\b([A-Z][a-z]+)\s+([A-Z][a-z]+)\b',  # First Last
        r'\*\*([A-Z][a-z]+\s+[A-Z][a-z]+)\*\*',  # **Name**
    ]

    false_positives = {
        'United States', 'United Kingdom', 'New Zealand', 'Universal Basic',
        'Child Tax', 'Basic Income', 'Open Source', 'Policy Simulation',
        'Tax Foundation', 'Urban Institute', 'Google Analytics', 'YouTube Go',
        'Democratic Party', 'Republican Party', 'Population Survey',
        'Tax Credit', 'Social Security', 'National Insurance', 'Autumn Budget',
        'Spring Budget', 'Current Population', 'Family Resources',
        'Consumer Expenditure', 'Public Use', 'Internal Revenue',
        'Joint Committee', 'Budget Office', 'Federal Reserve',
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
    patterns = [
        r'\b(TAXSIM|EUROMOD|UKMOD|MINT|DYNASIM|CBOLT|CORSIM)\b',
        r'\b(Tax-Calculator|OpenFisca|PolicyEngine|OG-USA|FRB/US)\b',
        r'\b(TAXBEN|Tax-Data|TaxBrain|Cost-of-Capital-Calculator)\b',
    ]

    for pattern in patterns:
        models.update(re.findall(pattern, content))

    return models


def normalize_concept_name(name: str) -> str:
    """Normalize concept name for case-insensitive matching.

    Maps regex-captured names (e.g., 'PolicyEngine', 'TAXSIM') to
    research file stems (e.g., 'policyengine', 'taxsim').
    """
    return name.lower().replace('-', '-')


def build_concept_to_tracked_map(tracked: Dict[str, Dict]) -> Dict[str, str]:
    """Build a mapping from normalized concept names to tracked keys.

    Handles the case mismatch between regex captures (PolicyEngine)
    and file stems (policyengine).
    """
    mapping = {}
    for key in tracked:
        # Map both the key itself and common variants
        normalized = normalize_concept_name(key)
        mapping[normalized] = key
        # Also map without hyphens for cases like ifs-taxben -> TAXBEN
        mapping[normalized.replace('-', '')] = key
    return mapping


def find_tracked_key(concept: str, tracked: Dict[str, Dict],
                     concept_map: Dict[str, str]) -> str | None:
    """Find the tracked key for a concept, handling case/format differences."""
    # Direct match
    if concept in tracked:
        return concept

    # Normalized match
    normalized = normalize_concept_name(concept)
    if normalized in concept_map:
        return concept_map[normalized]

    # Try with hyphens replaced by nothing
    no_hyphens = normalized.replace('-', '')
    if no_hyphens in concept_map:
        return concept_map[no_hyphens]

    # Special cases: TAXBEN -> ifs-taxben
    for key in tracked:
        if concept.lower() in key.lower() or key.lower() in concept.lower():
            return key

    return None


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
        'content': content,
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
    concept_map = build_concept_to_tracked_map(tracked)

    # Build inverse map: concept -> [chapters where it appears]
    concept_appearances = defaultdict(list)

    for ch in chapters:
        chapter_id = ch['chapter']

        for model in ch['models']:
            concept_appearances[model].append(chapter_id)

        for link in ch['wiki_links']:
            concept_appearances[link].append(chapter_id)

    # Check each concept
    for concept, appearances in concept_appearances.items():
        if len(appearances) > 1:
            tracked_key = find_tracked_key(concept, tracked, concept_map)

            if tracked_key is None:
                issues.append({
                    'type': 'untracked_duplication',
                    'concept': concept,
                    'chapters': appearances,
                    'message': f"'{concept}' appears in chapters {appearances} but has no tracking frontmatter"
                })
            elif not tracked[tracked_key].get('primary_chapter'):
                issues.append({
                    'type': 'missing_primary',
                    'concept': concept,
                    'chapters': appearances,
                    'message': f"'{concept}' appears in multiple chapters but no primary_chapter marked"
                })
            else:
                declared = set(tracked[tracked_key]['chapters'])
                actual = set(appearances)
                if declared != actual:
                    issues.append({
                        'type': 'tracking_mismatch',
                        'concept': concept,
                        'declared': sorted(declared),
                        'actual': sorted(actual),
                        'message': f"'{concept}' tracking mismatch: declared {sorted(declared)}, actual {sorted(actual)}"
                    })

    return issues


def extract_concept_contexts(content: str, concept: str, window: int = 200) -> List[Dict]:
    """Extract text contexts around concept mentions.

    Returns list of dicts with 'text' (surrounding context) and 'is_introduction'
    (whether this looks like a definitional/introductory usage).
    """
    contexts = []
    # Escape concept for regex
    escaped = re.escape(concept)

    for match in re.finditer(escaped, content):
        start = max(0, match.start() - window)
        end = min(len(content), match.end() + window)
        context_text = content[start:end]

        # Check if this is an introduction/definition
        is_intro = False
        for pattern_template in INTRODUCTION_PATTERNS:
            pattern = pattern_template.format(concept=escaped)
            if re.search(pattern, context_text, re.IGNORECASE):
                is_intro = True
                break

        # Check for explanation patterns
        is_explanation = False
        for pattern_template in EXPLANATION_PATTERNS:
            pattern = pattern_template.format(concept=escaped)
            if re.search(pattern, context_text, re.IGNORECASE):
                is_explanation = True
                break

        # Extract the sentence containing the concept
        sentence_match = re.search(
            r'[.!?\n][^.!?\n]*' + escaped + r'[^.!?\n]*[.!?\n]',
            content[max(0, match.start() - 500):min(len(content), match.end() + 500)]
        )
        sentence = sentence_match.group().strip() if sentence_match else context_text.strip()

        contexts.append({
            'text': context_text.strip(),
            'sentence': sentence[:300],
            'is_introduction': is_intro,
            'is_explanation': is_explanation,
            'position': match.start(),
        })

    return contexts


def extract_key_phrases(text: str) -> Set[str]:
    """Extract meaningful phrases from text for similarity comparison."""
    # Lowercase and split into words
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    # Filter stopwords
    stopwords = {
        'the', 'and', 'for', 'that', 'this', 'with', 'from', 'are', 'was',
        'were', 'been', 'being', 'have', 'has', 'had', 'does', 'did', 'will',
        'would', 'could', 'should', 'may', 'might', 'can', 'its', 'their',
        'they', 'them', 'which', 'what', 'when', 'where', 'who', 'how',
        'than', 'but', 'not', 'also', 'more', 'most', 'other', 'some',
        'such', 'only', 'same', 'into', 'over', 'about', 'between',
    }
    return {w for w in words if w not in stopwords}


def compute_phrase_overlap(phrases1: Set[str], phrases2: Set[str]) -> float:
    """Compute Jaccard-like overlap between phrase sets."""
    if not phrases1 or not phrases2:
        return 0.0
    intersection = phrases1 & phrases2
    union = phrases1 | phrases2
    return len(intersection) / len(union)


def find_semantic_duplications(chapters: List[Dict], tracked: Dict[str, Dict]) -> List[Dict]:
    """Detect concepts that are re-introduced/re-explained in multiple chapters.

    This goes beyond entity tracking to find cases where:
    1. A concept is introduced (definitional language) in multiple chapters
    2. Similar explanations of a concept appear in different chapters
    """
    issues = []
    concept_map = build_concept_to_tracked_map(tracked)

    # Collect all concepts mentioned across chapters
    all_concepts = set()
    for ch in chapters:
        all_concepts.update(ch['models'])

    # Also check key people who appear in multiple chapters
    people_appearances = defaultdict(list)
    for ch in chapters:
        for person in ch['people']:
            people_appearances[person].append(ch['chapter'])

    # For each concept, check for duplicate introductions
    for concept in sorted(all_concepts):
        introductions = []
        explanations = []

        for ch in chapters:
            if concept not in ch['models']:
                continue

            contexts = extract_concept_contexts(ch['content'], concept)

            for ctx in contexts:
                if ctx['is_introduction']:
                    introductions.append({
                        'chapter': ch['chapter'],
                        'title': ch['title'],
                        'sentence': ctx['sentence'],
                        'phrases': extract_key_phrases(ctx['sentence']),
                    })
                if ctx['is_explanation']:
                    explanations.append({
                        'chapter': ch['chapter'],
                        'title': ch['title'],
                        'sentence': ctx['sentence'],
                        'phrases': extract_key_phrases(ctx['sentence']),
                    })

        # Flag if concept is introduced (definitional language) in multiple chapters
        if len(introductions) > 1:
            intro_chapters = sorted(set(i['chapter'] for i in introductions))
            tracked_key = find_tracked_key(concept, tracked, concept_map)
            primary = tracked[tracked_key]['primary_chapter'] if tracked_key else None

            # Check if non-primary chapters have introductions
            non_primary_intros = [i for i in introductions if i['chapter'] != primary]
            if non_primary_intros and primary is not None:
                issues.append({
                    'type': 'duplicate_introduction',
                    'concept': concept,
                    'primary_chapter': primary,
                    'also_introduced_in': sorted(set(i['chapter'] for i in non_primary_intros)),
                    'examples': [
                        {'chapter': i['chapter'], 'sentence': i['sentence'][:200]}
                        for i in introductions[:4]
                    ],
                    'message': (
                        f"'{concept}' is introduced in ch {primary} (primary) "
                        f"but also re-introduced in ch {sorted(set(i['chapter'] for i in non_primary_intros))}"
                    ),
                })
            elif primary is None:
                issues.append({
                    'type': 'duplicate_introduction',
                    'concept': concept,
                    'primary_chapter': None,
                    'also_introduced_in': intro_chapters,
                    'examples': [
                        {'chapter': i['chapter'], 'sentence': i['sentence'][:200]}
                        for i in introductions[:4]
                    ],
                    'message': (
                        f"'{concept}' has introductory language in chapters {intro_chapters} "
                        f"but no primary chapter is designated"
                    ),
                })

        # Check for similar explanations across chapters
        if len(explanations) > 1:
            for i, exp1 in enumerate(explanations):
                for exp2 in explanations[i + 1:]:
                    if exp1['chapter'] == exp2['chapter']:
                        continue
                    overlap = compute_phrase_overlap(exp1['phrases'], exp2['phrases'])
                    if overlap > 0.35:  # Significant phrase overlap
                        issues.append({
                            'type': 'similar_explanation',
                            'concept': concept,
                            'chapters': sorted([exp1['chapter'], exp2['chapter']]),
                            'overlap': f"{overlap:.0%}",
                            'sentence1': exp1['sentence'][:150],
                            'sentence2': exp2['sentence'][:150],
                            'message': (
                                f"'{concept}' has similar explanations in ch {exp1['chapter']} "
                                f"and ch {exp2['chapter']} ({overlap:.0%} phrase overlap)"
                            ),
                        })

    # Check for people re-introduced in multiple chapters
    for person, appearances in people_appearances.items():
        if len(appearances) < 2:
            continue

        person_intros = []
        for ch in chapters:
            if ch['chapter'] not in appearances:
                continue
            contexts = extract_concept_contexts(ch['content'], person)
            for ctx in contexts:
                if ctx['is_introduction']:
                    person_intros.append({
                        'chapter': ch['chapter'],
                        'sentence': ctx['sentence'],
                    })

        if len(person_intros) > 1:
            intro_chapters = sorted(set(i['chapter'] for i in person_intros))
            issues.append({
                'type': 'person_reintroduction',
                'concept': person,
                'chapters': intro_chapters,
                'examples': [
                    {'chapter': i['chapter'], 'sentence': i['sentence'][:200]}
                    for i in person_intros[:4]
                ],
                'message': (
                    f"'{person}' is introduced with definitional language in "
                    f"chapters {intro_chapters}"
                ),
            })

    return issues


def find_untracked_entities(chapters: List[Dict], tracked: Dict[str, Dict]) -> Dict[str, Set[str]]:
    """Find people and models mentioned but not tracked."""
    all_people = set()
    all_models = set()

    for ch in chapters:
        all_people.update(ch['people'])
        all_models.update(ch['models'])

    # Filter out what's already tracked (case-insensitive)
    concept_map = build_concept_to_tracked_map(tracked)

    untracked_people = {
        p for p in all_people
        if find_tracked_key(p, tracked, concept_map) is None
    }

    untracked_models = {
        m for m in all_models
        if find_tracked_key(m, tracked, concept_map) is None
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
    lines.append(f"Chapters analyzed: {len(chapters)}")
    lines.append(f"Tracked entities: {len(tracked)}")
    lines.append("")

    # Tracked entities by chapter
    lines.append("Tracked Entities by Chapter:")
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
            lines.append(f"  - {entity['title'][:50]} {appearances}")

    lines.append("")
    lines.append("=" * 70)

    return "\n".join(lines)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Track concepts and people across manuscript")
    parser.add_argument("--report", action="store_true", help="Generate full tracking report")
    parser.add_argument("--untracked", action="store_true", help="Show untracked entities")
    parser.add_argument("--semantic", action="store_true", help="Detect semantic duplications")
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
        print("\nUNTRACKED ENTITIES")
        print("=" * 70)
        print(f"\nPeople mentioned but not tracked ({len(untracked['people'])}):")
        for person in sorted(untracked['people']):
            print(f"  - {person}")
        print(f"\nModels mentioned but not tracked ({len(untracked['models'])}):")
        for model in sorted(untracked['models']):
            print(f"  - {model}")
        return

    if args.semantic:
        issues = find_semantic_duplications(chapters, tracked)

        if not issues:
            print("\nNo semantic duplications found!")
            print(f"   Checked {len(chapters)} chapters for duplicate introductions and similar explanations")
        else:
            # Group by type
            by_type = defaultdict(list)
            for issue in issues:
                by_type[issue['type']].append(issue)

            print(f"\nFound {len(issues)} semantic duplication issues:\n")

            if by_type.get('duplicate_introduction'):
                print("DUPLICATE INTRODUCTIONS (concept defined in multiple chapters):")
                print("-" * 70)
                for issue in by_type['duplicate_introduction']:
                    print(f"\n  {issue['message']}")
                    for ex in issue.get('examples', []):
                        sentence = ex['sentence'].replace('\n', ' ')[:150]
                        print(f"    Ch {ex['chapter']}: \"{sentence}...\"")

            if by_type.get('similar_explanation'):
                print("\n\nSIMILAR EXPLANATIONS (same concept explained similarly in different chapters):")
                print("-" * 70)
                for issue in by_type['similar_explanation']:
                    print(f"\n  {issue['message']}")
                    s1 = issue['sentence1'].replace('\n', ' ')[:120]
                    s2 = issue['sentence2'].replace('\n', ' ')[:120]
                    print(f"    Ch {issue['chapters'][0]}: \"{s1}...\"")
                    print(f"    Ch {issue['chapters'][1]}: \"{s2}...\"")

            if by_type.get('person_reintroduction'):
                print("\n\nPERSON RE-INTRODUCTIONS (same person introduced in multiple chapters):")
                print("-" * 70)
                for issue in by_type['person_reintroduction']:
                    print(f"\n  {issue['message']}")
                    for ex in issue.get('examples', []):
                        sentence = ex['sentence'].replace('\n', ' ')[:150]
                        print(f"    Ch {ex['chapter']}: \"{sentence}...\"")

        return

    # Default: run both entity tracking and semantic checks
    entity_issues = find_concept_duplications(chapters, tracked)
    semantic_issues = find_semantic_duplications(chapters, tracked)
    all_issues = entity_issues + semantic_issues

    if not all_issues:
        print("\nAll clear! No issues found.")
        print(f"   {len(tracked)} entities tracked, {len(chapters)} chapters analyzed")
    else:
        if entity_issues:
            print(f"\nEntity tracking issues ({len(entity_issues)}):\n")
            for issue in entity_issues:
                msg = issue.get("message", str(issue))
                print(f"  {issue['type'].upper()}: {msg}")

        if semantic_issues:
            by_type = {}
            for issue in semantic_issues:
                by_type.setdefault(issue["type"], []).append(issue)
            print(f"\nSemantic issues ({len(semantic_issues)}):\n")
            for itype, items in by_type.items():
                label = itype.upper().replace("_", " ")
                print(f"  {label}:")
                for item in items:
                    print(f"    {item['message']}")

        print(f"\n  Run with --semantic for detailed output")
        print(f"  Run with --untracked for entity details")


if __name__ == "__main__":
    main()

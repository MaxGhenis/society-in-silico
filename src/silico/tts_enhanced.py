"""Enhanced TTS pipeline with concept tracking integration.

Extends basic TTS with:
- Optional chapter introductions from tracked concepts
- Metadata generation with concept mentions per chapter
- Validation warnings for untracked duplications
"""

from pathlib import Path
from typing import Optional, Dict, List
import json

from .tts_pipeline import Chapter, generate_chapter_audio, get_chapters_in_order
from .concept_tracker import (
    load_tracked_entities,
    analyze_chapter_references,
    find_concept_duplications
)
from .utils import get_manuscript_chapters


def generate_chapter_introduction(
    chapter: Chapter,
    tracked_concepts: Dict[str, Dict],
    chapter_file_number: int
) -> Optional[str]:
    """Generate an optional spoken introduction for a chapter based on tracked concepts.

    Args:
        chapter: Chapter object
        tracked_concepts: Dict of tracked entities from research notes
        chapter_file_number: The chapter's file number for matching

    Returns:
        Introduction text, or None if no tracked concepts found
    """
    # Find concepts that have this as their primary chapter
    primary_concepts = []

    for concept_key, data in tracked_concepts.items():
        if data.get('primary_chapter') == chapter_file_number:
            primary_concepts.append({
                'name': data.get('title', concept_key),
                'role': data.get('narrative_role', '')
            })

    if not primary_concepts:
        return None

    # Build introduction
    intro = f"{chapter.title}. "

    if len(primary_concepts) == 1:
        concept = primary_concepts[0]
        if concept['role']:
            intro += f"In this chapter, we discuss {concept['name']}: {concept['role']}."
    elif len(primary_concepts) == 2:
        intro += f"In this chapter, we cover {primary_concepts[0]['name']} and {primary_concepts[1]['name']}."
    else:
        names = [c['name'] for c in primary_concepts[:3]]
        intro += f"In this chapter, we explore {', '.join(names[:-1])}, and {names[-1]}."

    return intro


def generate_metadata_with_concepts(
    chapters: List[Chapter],
    research_dir: Path
) -> Dict:
    """Generate metadata JSON with concept tracking information.

    Args:
        chapters: List of Chapter objects
        research_dir: Path to research directory

    Returns:
        Dict with chapter metadata including tracked concepts
    """
    tracked = load_tracked_entities(research_dir)
    metadata = {
        'total_chapters': len(chapters),
        'chapters': []
    }

    for ch in chapters:
        # Get chapter file number from filename
        import re
        number_match = re.match(r'(\d+)', ch.path.name)
        file_number = int(number_match.group(1)) if number_match else 0

        # Find concepts mentioned in this chapter
        content = ch.path.read_text()
        from .concept_tracker import extract_model_mentions, extract_wiki_links

        models = extract_model_mentions(content)
        links = extract_wiki_links(content)
        all_mentions = models | links

        # Match with tracked concepts
        tracked_mentions = []
        for mention in all_mentions:
            mention_lower = mention.lower().replace(' ', '-')
            if mention_lower in tracked or mention in tracked:
                concept_data = tracked.get(mention_lower) or tracked.get(mention)
                tracked_mentions.append({
                    'name': concept_data.get('title', mention),
                    'role': concept_data.get('narrative_role', ''),
                    'is_primary': concept_data.get('primary_chapter') == file_number
                })

        metadata['chapters'].append({
            'track': ch.track_number,
            'title': ch.title,
            'part': ch.part,
            'file_number': file_number,
            'tracked_concepts': tracked_mentions
        })

    return metadata


def generate_book_audio_enhanced(
    manuscript_dir: Path,
    output_dir: Path,
    research_dir: Optional[Path] = None,
    voice: str = "nova",
    add_introductions: bool = False,
    validate_tracking: bool = True,
    dry_run: bool = False,
) -> dict:
    """Generate audiobook with concept tracking enhancements.

    Args:
        manuscript_dir: Path to manuscript directory
        output_dir: Where to save MP3 files
        research_dir: Path to research directory (for concept tracking)
        voice: OpenAI TTS voice
        add_introductions: If True, prepend chapter introductions based on concepts
        validate_tracking: If True, warn about untracked duplications
        dry_run: If True, just estimate costs without generating

    Returns:
        Dict with statistics and metadata
    """
    chapters = get_chapters_in_order(manuscript_dir)

    # Load tracked concepts if research_dir provided
    tracked_concepts = {}
    if research_dir and research_dir.exists():
        tracked_concepts = load_tracked_entities(research_dir)

        # Validate if requested
        if validate_tracking:
            manuscript_chapters = get_manuscript_chapters(manuscript_dir)
            chapter_refs = [analyze_chapter_references(ch) for ch in manuscript_chapters]
            issues = find_concept_duplications(chapter_refs, tracked_concepts)

            if issues:
                print(f"\n⚠️  Warning: {len(issues)} concept tracking issues found:")
                for issue in issues[:5]:  # Show first 5
                    print(f"  - {issue['message']}")
                if len(issues) > 5:
                    print(f"  ... and {len(issues) - 5} more")
                print("\n💡 Run 'silico-check' for full details\n")

    # Generate metadata
    metadata = generate_metadata_with_concepts(chapters, research_dir) if research_dir else None

    # Continue with standard TTS generation
    from .tts_pipeline import estimate_cost

    total_chars = sum(ch.character_count() for ch in chapters)
    estimated_cost = estimate_cost(total_chars)

    result = {
        "chapters": len(chapters),
        "total_characters": total_chars,
        "estimated_cost": estimated_cost,
        "files": [],
        "metadata": metadata,
    }

    if dry_run:
        for ch in chapters:
            result["files"].append({
                "track": ch.track_number,
                "title": ch.title,
                "part": ch.part,
                "characters": ch.character_count(),
                "path": None,
            })
        return result

    output_dir.mkdir(parents=True, exist_ok=True)

    # Save metadata if generated
    if metadata:
        metadata_path = output_dir / "chapters_metadata.json"
        metadata_path.write_text(json.dumps(metadata, indent=2))
        print(f"📝 Saved metadata to {metadata_path}")

    for ch in chapters:
        # Get file number
        import re
        number_match = re.match(r'(\d+)', ch.path.name)
        file_number = int(number_match.group(1)) if number_match else 0

        # Prepare text
        text = ch.get_clean_text()

        # Add introduction if requested
        if add_introductions and tracked_concepts:
            intro = generate_chapter_introduction(ch, tracked_concepts, file_number)
            if intro:
                text = f"{intro}\n\n{text}"

        # Create filename
        safe_title = re.sub(r"[^\w\s-]", "", ch.title.lower())
        safe_title = re.sub(r"\s+", "-", safe_title)
        filename = f"{ch.track_number:02d}-{safe_title}.mp3"
        output_path = output_dir / filename

        print(f"Generating {ch.track_number}/{len(chapters)}: {ch.title}")

        generate_chapter_audio(
            text=text,
            output_path=output_path,
            voice=voice,
        )

        result["files"].append({
            "track": ch.track_number,
            "title": ch.title,
            "part": ch.part,
            "characters": len(text),
            "path": str(output_path),
        })

    return result


def main():
    """CLI entry point for enhanced audiobook generation."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate audiobook from manuscript with concept tracking"
    )
    parser.add_argument(
        "--manuscript",
        type=Path,
        default=Path.cwd() / "manuscript",
        help="Path to manuscript directory",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path.cwd() / "audiobook",
        help="Output directory for MP3 files",
    )
    parser.add_argument(
        "--research",
        type=Path,
        default=Path.cwd() / "research",
        help="Path to research directory (for concept tracking)",
    )
    parser.add_argument(
        "--voice",
        choices=["alloy", "echo", "fable", "onyx", "nova", "shimmer"],
        default="nova",
        help="OpenAI TTS voice",
    )
    parser.add_argument(
        "--introductions",
        action="store_true",
        help="Add chapter introductions based on tracked concepts",
    )
    parser.add_argument(
        "--no-validate",
        action="store_true",
        help="Skip concept tracking validation",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Estimate costs without generating audio",
    )

    args = parser.parse_args()

    result = generate_book_audio_enhanced(
        manuscript_dir=args.manuscript,
        output_dir=args.output,
        research_dir=args.research if args.research.exists() else None,
        voice=args.voice,
        add_introductions=args.introductions,
        validate_tracking=not args.no_validate,
        dry_run=args.dry_run,
    )

    print(f"\nChapters: {result['chapters']}")
    print(f"Total characters: {result['total_characters']:,}")
    print(f"Estimated cost: ${result['estimated_cost']:.2f}")

    if args.dry_run:
        print("\nChapter breakdown:")
        for f in result["files"]:
            print(f"  {f['track']:2d}. {f['title'][:40]:<40} ({f['characters']:,} chars)")


if __name__ == "__main__":
    main()

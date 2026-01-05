"""TTS pipeline for converting Society in Silico to audiobook."""

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import io

from openai import OpenAI


# OpenAI TTS pricing: $15 per 1M characters
COST_PER_MILLION_CHARS = 15.0

# OpenAI TTS character limit per request
MAX_CHARS_PER_REQUEST = 4096


def strip_markdown(text: str) -> str:
    """Strip markdown formatting for clean TTS input.

    Removes:
    - Code blocks (```...```)
    - HTML comments (<!-- ... -->)
    - Citations ({cite}`...`)
    - Footnote references ([^...])
    - Wiki-style links ([[...]])
    - Horizontal rules (---)
    - Tables
    - Header markers (#)
    - Bibliography blocks

    Preserves:
    - Plain text content
    - Blockquotes (as plain text)
    """
    if not text:
        return ""

    result = text

    # Remove HTML comments (multiline)
    result = re.sub(r"<!--.*?-->", "", result, flags=re.DOTALL)

    # Remove code blocks (including bibliography blocks)
    result = re.sub(r"```.*?```", "", result, flags=re.DOTALL)

    # Remove citations (and trailing space before punctuation)
    result = re.sub(r"\s*\{cite\}`[^`]*`", "", result)
    result = re.sub(r"\s*\{cite:[a-z]+\}`[^`]*`", "", result)

    # Remove footnote references
    result = re.sub(r"\[\^[^\]]*\]", "", result)

    # Convert wiki links with aliases [[target|display]] -> display
    result = re.sub(r"\[\[([^\]|]*)\|([^\]]*)\]\]", r"\2", result)

    # Convert wiki links without aliases [[target]] -> target
    result = re.sub(r"\[\[([^\]]*)\]\]", r"\1", result)

    # Remove horizontal rules
    result = re.sub(r"^\s*---\s*$", "", result, flags=re.MULTILINE)

    # Remove table rows (lines that start and end with |)
    result = re.sub(r"^\s*\|.*\|\s*$", "", result, flags=re.MULTILINE)

    # Remove header markers but keep the text
    result = re.sub(r"^#+\s*", "", result, flags=re.MULTILINE)

    # Clean up blockquote markers but keep text
    result = re.sub(r"^>\s*", "", result, flags=re.MULTILINE)

    # Normalize multiple newlines (max 2)
    result = re.sub(r"\n{3,}", "\n\n", result)

    # Clean up extra spaces
    result = re.sub(r"  +", " ", result)

    return result.strip()


@dataclass
class Chapter:
    """Represents a book chapter."""

    path: Path
    title: str
    track_number: int
    part: str

    def get_clean_text(self) -> str:
        """Get markdown-stripped text content."""
        raw = self.path.read_text()
        return strip_markdown(raw)

    def character_count(self) -> int:
        """Get character count of clean text."""
        return len(self.get_clean_text())


def get_chapters_in_order(manuscript_dir: Path) -> list[Chapter]:
    """Get all chapters in reading order.

    Order:
    1. front-matter (preface, thesis, introduction)
    2. part-1-origins
    3. part-2-building
    4. part-3-future

    Within each part, files are sorted by their numeric prefix.
    Excludes outline files.
    """
    chapters = []
    track_num = 0

    # Define part order and their directory names
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

        # Get markdown files, sorted by name
        md_files = sorted(part_path.glob("*.md"))

        for md_file in md_files:
            # Skip outline files
            if "outline" in md_file.name.lower():
                continue

            # Extract title from first # header or filename
            content = md_file.read_text()
            title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            if title_match:
                title = title_match.group(1)
            else:
                # Use filename without extension and number prefix
                title = re.sub(r"^\d+-", "", md_file.stem).replace("-", " ").title()

            track_num += 1
            chapters.append(
                Chapter(
                    path=md_file,
                    title=title,
                    track_number=track_num,
                    part=part_name,
                )
            )

    return chapters


def estimate_cost(character_count: int) -> float:
    """Estimate OpenAI TTS cost for given character count."""
    return (character_count / 1_000_000) * COST_PER_MILLION_CHARS


def split_text_for_tts(text: str, max_chars: int = MAX_CHARS_PER_REQUEST) -> list[str]:
    """Split text into chunks suitable for TTS API.

    Tries to split on paragraph boundaries, falling back to sentence
    boundaries, then word boundaries.
    """
    if len(text) <= max_chars:
        return [text]

    chunks = []
    remaining = text

    while remaining:
        if len(remaining) <= max_chars:
            chunks.append(remaining)
            break

        # Find a good split point
        chunk = remaining[:max_chars]

        # Try to split on paragraph boundary
        para_break = chunk.rfind("\n\n")
        if para_break > max_chars // 2:
            split_point = para_break + 2
        else:
            # Try sentence boundary
            sentence_end = max(
                chunk.rfind(". "),
                chunk.rfind("? "),
                chunk.rfind("! "),
            )
            if sentence_end > max_chars // 2:
                split_point = sentence_end + 2
            else:
                # Fall back to word boundary
                space = chunk.rfind(" ")
                split_point = space + 1 if space > 0 else max_chars

        chunks.append(remaining[:split_point].strip())
        remaining = remaining[split_point:].strip()

    return chunks


def generate_chapter_audio(
    text: str,
    output_path: Path,
    voice: str = "nova",
    model: str = "tts-1",
) -> None:
    """Generate audio file from text using OpenAI TTS.

    Handles long text by chunking and concatenating.

    Args:
        text: The text to convert to speech
        output_path: Where to save the MP3 file
        voice: OpenAI TTS voice (alloy, echo, fable, onyx, nova, shimmer)
        model: TTS model (tts-1 or tts-1-hd)
    """
    client = OpenAI()
    chunks = split_text_for_tts(text)

    audio_segments = []

    for chunk in chunks:
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=chunk,
        )
        audio_segments.append(response.content)

    # Concatenate all audio segments
    combined_audio = b"".join(audio_segments)

    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(combined_audio)


def generate_book_audio(
    manuscript_dir: Path,
    output_dir: Path,
    voice: str = "nova",
    dry_run: bool = False,
) -> dict:
    """Generate audio for entire book.

    Args:
        manuscript_dir: Path to manuscript directory
        output_dir: Where to save MP3 files
        voice: OpenAI TTS voice
        dry_run: If True, just estimate costs without generating

    Returns:
        Dict with statistics (chapters, characters, cost, files)
    """
    chapters = get_chapters_in_order(manuscript_dir)

    total_chars = sum(ch.character_count() for ch in chapters)
    estimated_cost = estimate_cost(total_chars)

    result = {
        "chapters": len(chapters),
        "total_characters": total_chars,
        "estimated_cost": estimated_cost,
        "files": [],
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

    for ch in chapters:
        # Create filename: 01-preface.mp3
        safe_title = re.sub(r"[^\w\s-]", "", ch.title.lower())
        safe_title = re.sub(r"\s+", "-", safe_title)
        filename = f"{ch.track_number:02d}-{safe_title}.mp3"
        output_path = output_dir / filename

        print(f"Generating {ch.track_number}/{len(chapters)}: {ch.title}")

        generate_chapter_audio(
            text=ch.get_clean_text(),
            output_path=output_path,
            voice=voice,
        )

        result["files"].append({
            "track": ch.track_number,
            "title": ch.title,
            "part": ch.part,
            "characters": ch.character_count(),
            "path": str(output_path),
        })

    return result


def main():
    """CLI entry point for generating audiobook."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate audiobook from manuscript")
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
        "--voice",
        choices=["alloy", "echo", "fable", "onyx", "nova", "shimmer"],
        default="nova",
        help="OpenAI TTS voice",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Estimate costs without generating audio",
    )

    args = parser.parse_args()

    result = generate_book_audio(
        manuscript_dir=args.manuscript,
        output_dir=args.output,
        voice=args.voice,
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

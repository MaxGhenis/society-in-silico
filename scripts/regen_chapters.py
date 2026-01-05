#!/usr/bin/env python3
"""Regenerate specific chapters."""
import sys
sys.path.insert(0, '/Users/maxghenis/society-in-silico/src')

from pathlib import Path
from silico.tts_pipeline import Chapter, generate_chapter_audio, strip_markdown

chapters_to_regen = [
    ("manuscript/front-matter/01-introduction.md", "03-introduction-the-model-and-the-world.mp3", "Introduction: The Model and the World", 3),
    ("manuscript/part-1-origins/03-open-source-revolution.md", "06-chapter-3-the-open-source-revolution.mp3", "Chapter 3: The Open Source Revolution", 6),
    ("manuscript/part-2-building/04-policyengine-proof-of-concept.md", "08-chapter-4-policyengine---proof-of-concept.mp3", "Chapter 4: PolicyEngine - Proof of Concept", 8),
]

base = Path("/Users/maxghenis/society-in-silico")
output_dir = base / "audiobook"

for src, dest, title, track in chapters_to_regen:
    print(f"Regenerating {track}: {title}")
    ch = Chapter(
        path=base / src,
        title=title,
        track_number=track,
        part="",
    )
    output_path = output_dir / dest
    generate_chapter_audio(
        text=ch.get_clean_text(),
        output_path=output_path,
        voice="nova",
    )
    print(f"  Done: {output_path}")

print("\nAll chapters regenerated!")

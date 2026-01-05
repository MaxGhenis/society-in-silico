"""Tests for TTS pipeline - TDD approach."""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import tempfile
import os

from silico.tts_pipeline import (
    strip_markdown,
    get_chapters_in_order,
    Chapter,
    generate_chapter_audio,
    estimate_cost,
)


class TestStripMarkdown:
    """Test markdown stripping for clean TTS input."""

    def test_strips_code_blocks(self):
        text = "Before\n```python\ncode here\n```\nAfter"
        assert strip_markdown(text) == "Before\n\nAfter"

    def test_strips_html_comments(self):
        text = "Before\n<!-- comment\nmultiline -->\nAfter"
        assert strip_markdown(text) == "Before\n\nAfter"

    def test_strips_citations(self):
        text = "This is a claim {cite}`jones2024`."
        assert strip_markdown(text) == "This is a claim."

    def test_strips_footnote_refs(self):
        text = "Some text[^1] with footnotes[^gpt4-tax]."
        assert strip_markdown(text) == "Some text with footnotes."

    def test_strips_wiki_links(self):
        text = "See [[guy-orcutt|Guy Orcutt]] for details."
        assert strip_markdown(text) == "See Guy Orcutt for details."

    def test_strips_wiki_links_no_alias(self):
        text = "See [[policyengine]] for details."
        assert strip_markdown(text) == "See policyengine for details."

    def test_strips_horizontal_rules(self):
        text = "Section one\n\n---\n\nSection two"
        result = strip_markdown(text)
        assert "---" not in result
        assert "Section one" in result
        assert "Section two" in result

    def test_strips_table_rows(self):
        text = "Before\n| Col1 | Col2 |\n|------|------|\n| a | b |\nAfter"
        result = strip_markdown(text)
        assert "|" not in result
        assert "Before" in result
        assert "After" in result

    def test_converts_headers_to_plain_text(self):
        text = "# Chapter Title\n\nContent here\n\n## Section"
        result = strip_markdown(text)
        assert "Chapter Title" in result
        assert "#" not in result

    def test_strips_bibliography_block(self):
        text = "Content\n\n```{bibliography}\n:filter: docname\n```\n\nMore"
        assert "bibliography" not in strip_markdown(text)

    def test_preserves_blockquotes_as_text(self):
        text = '> "This is a quote from someone."'
        result = strip_markdown(text)
        assert "This is a quote from someone" in result

    def test_handles_empty_input(self):
        assert strip_markdown("") == ""

    def test_normalizes_whitespace(self):
        text = "Word1\n\n\n\n\nWord2"
        result = strip_markdown(text)
        # Should collapse multiple newlines but preserve paragraph breaks
        assert "\n\n\n\n\n" not in result


class TestChapterOrdering:
    """Test that chapters are discovered and ordered correctly."""

    def test_discovers_all_chapters(self):
        chapters = get_chapters_in_order(
            Path("/Users/maxghenis/society-in-silico/manuscript")
        )
        # Should have front matter, part 1, part 2, part 3
        assert len(chapters) >= 10

    def test_front_matter_comes_first(self):
        chapters = get_chapters_in_order(
            Path("/Users/maxghenis/society-in-silico/manuscript")
        )
        # First few should be from front-matter
        assert "front-matter" in str(chapters[0].path) or "preface" in chapters[0].title.lower()

    def test_chapters_have_required_attributes(self):
        chapters = get_chapters_in_order(
            Path("/Users/maxghenis/society-in-silico/manuscript")
        )
        for ch in chapters:
            assert hasattr(ch, "path")
            assert hasattr(ch, "title")
            assert hasattr(ch, "track_number")
            assert hasattr(ch, "part")

    def test_track_numbers_are_sequential(self):
        chapters = get_chapters_in_order(
            Path("/Users/maxghenis/society-in-silico/manuscript")
        )
        track_numbers = [ch.track_number for ch in chapters]
        assert track_numbers == list(range(1, len(chapters) + 1))

    def test_excludes_outline_file(self):
        chapters = get_chapters_in_order(
            Path("/Users/maxghenis/society-in-silico/manuscript")
        )
        paths = [str(ch.path) for ch in chapters]
        assert not any("00-outline.md" in p for p in paths)


class TestChapter:
    """Test Chapter dataclass."""

    def test_chapter_clean_text(self):
        # Create a temp file with markdown
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write("# Test Chapter\n\nSome content {cite}`ref`.")
            f.flush()
            path = Path(f.name)

        try:
            ch = Chapter(path=path, title="Test", track_number=1, part="Test Part")
            clean = ch.get_clean_text()
            assert "Test Chapter" in clean
            assert "Some content" in clean
            assert "{cite}" not in clean
        finally:
            os.unlink(path)

    def test_chapter_character_count(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write("# Title\n\nHello world.")
            f.flush()
            path = Path(f.name)

        try:
            ch = Chapter(path=path, title="Test", track_number=1, part="Test Part")
            count = ch.character_count()
            assert count > 0
            assert count < 100  # Reasonable for this small file
        finally:
            os.unlink(path)


class TestCostEstimate:
    """Test cost estimation."""

    def test_estimate_for_known_chars(self):
        # OpenAI TTS is $15 per 1M characters
        cost = estimate_cost(1_000_000)
        assert cost == pytest.approx(15.0, rel=0.01)

    def test_estimate_for_book(self):
        # ~222k characters
        cost = estimate_cost(222_000)
        assert cost == pytest.approx(3.33, rel=0.1)


class TestGenerateAudio:
    """Test audio generation (mocked)."""

    @patch("silico.tts_pipeline.OpenAI")
    def test_calls_openai_with_correct_params(self, mock_openai_class):
        mock_client = MagicMock()
        mock_openai_class.return_value = mock_client
        mock_response = MagicMock()
        mock_response.content = b"fake audio data"
        mock_client.audio.speech.create.return_value = mock_response

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "test.mp3"
            generate_chapter_audio(
                text="Hello world",
                output_path=output_path,
                voice="nova",
            )

            mock_client.audio.speech.create.assert_called_once()
            call_kwargs = mock_client.audio.speech.create.call_args[1]
            assert call_kwargs["model"] == "tts-1"
            assert call_kwargs["voice"] == "nova"
            assert call_kwargs["input"] == "Hello world"

    @patch("silico.tts_pipeline.OpenAI")
    def test_writes_mp3_file(self, mock_openai_class):
        mock_client = MagicMock()
        mock_openai_class.return_value = mock_client
        mock_response = MagicMock()
        mock_response.content = b"fake audio data"
        mock_client.audio.speech.create.return_value = mock_response

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "test.mp3"
            generate_chapter_audio(
                text="Hello world",
                output_path=output_path,
            )

            assert output_path.exists()
            assert output_path.read_bytes() == b"fake audio data"

    @patch("silico.tts_pipeline.OpenAI")
    def test_handles_long_text_chunking(self, mock_openai_class):
        """OpenAI TTS has a 4096 character limit per request."""
        mock_client = MagicMock()
        mock_openai_class.return_value = mock_client
        mock_response = MagicMock()
        mock_response.content = b"audio"
        mock_client.audio.speech.create.return_value = mock_response

        # Text longer than 4096 chars
        long_text = "Hello world. " * 500  # ~6500 chars

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "test.mp3"
            generate_chapter_audio(
                text=long_text,
                output_path=output_path,
            )

            # Should have made multiple API calls
            assert mock_client.audio.speech.create.call_count >= 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

"""Text formatting and markdown processing for Society in Silico.

Handles markdown stripping, text cleaning, and format conversions.
"""

import re


def strip_markdown(text: str) -> str:
    """Strip markdown formatting for clean text output (TTS, word count, etc.).

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

    Args:
        text: Raw markdown content

    Returns:
        Cleaned plain text
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


def extract_citations(text: str) -> list[str]:
    """Extract {cite}`key` citations from markdown text.

    Args:
        text: Markdown content

    Returns:
        List of citation keys
    """
    return re.findall(r"\{cite\}`([^`]+)`", text)


def extract_wiki_links(text: str) -> list[str]:
    """Extract [[wiki-links]] from markdown text.

    Args:
        text: Markdown content

    Returns:
        List of wiki-link targets
    """
    # Handle both [[target|display]] and [[target]] formats
    with_alias = re.findall(r"\[\[([^\]|]+)\|[^\]]+\]\]", text)
    without_alias = re.findall(r"\[\[([^\]|]+)\]\]", text)
    return list(set(with_alias + without_alias))


def count_words(text: str) -> int:
    """Count words in text, excluding code blocks and YAML frontmatter.

    Args:
        text: Markdown content

    Returns:
        Word count
    """
    # Remove YAML frontmatter
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    # Remove code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Remove inline code
    text = re.sub(r"`[^`]+`", "", text)
    # Remove citations
    text = re.sub(r"\{cite\}`[^`]+`", "", text)
    # Count words
    return len(text.split())

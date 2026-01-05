# Silico Package

Tools and infrastructure for "Society in Silico" book project.

## Overview

The `silico` package provides:
- **TTS audiobook generation** from manuscript markdown
- **Concept tracking validation** to prevent duplication errors
- **Shared utilities** for working with manuscript and research notes

## Installation

```bash
pip install -e .  # From repository root
```

## Tools

### 1. Audiobook Generation

Convert manuscript to audiobook using OpenAI TTS:

```bash
# Basic usage
silico-tts --dry-run  # Estimate cost first
silico-tts            # Generate audiobook

# Options
silico-tts --voice nova --output ./my-audiobook
```

**Enhanced version** with concept tracking integration:

```bash
# With concept-based chapter introductions and validation
silico-tts-enhanced --introductions --dry-run
silico-tts-enhanced --introductions

# Skip validation
silico-tts-enhanced --no-validate
```

**Features:**
- Strips markdown (citations, code blocks, tables) for clean narration
- Handles 4096-char API limit with smart chunking on paragraph/sentence boundaries
- Cost estimation: ~$3.33 for 222k characters ($15/1M chars)
- Optional chapter introductions from tracked concepts
- Generates `chapters_metadata.json` with concept mentions per chapter

### 2. Concept Tracking

Validate consistency of people/concepts across manuscript:

```bash
# Check for tracking issues
silico-check

# Full tracking report
silico-check --report
```

**What it checks:**
- Concepts appearing in multiple chapters need tracking frontmatter
- Tracked concepts need `primary_chapter` marked
- Declared chapters match actual appearances

**Example issue:**
```
UNTRACKED_DUPLICATION: 'TAXSIM' appears in chapters [2, 4, 8] but has no tracking frontmatter
```

**Fix:** Add frontmatter to `research/concepts/taxsim.md`:
```yaml
---
chapters: [2, 4, 8]
primary_chapter: 2
narrative_role: "NBER tax calculator for academic research"
---
```

## Integration

### Concept Tracking → TTS Pipeline

The enhanced TTS pipeline uses concept tracking to:

1. **Validate before generation:**
   ```
   ⚠️  Warning: 3 concept tracking issues found:
     - 'PolicyEngine' appears in chapters [1, 3, 4...] but has no tracking frontmatter
   ```

2. **Generate chapter introductions** (optional):
   ```
   "Chapter 3: The Open Source Revolution. In this chapter, we discuss OpenFisca:
   a government-backed open-source framework for encoding tax-benefit rules as
   executable code."
   ```

3. **Export metadata** for each chapter:
   ```json
   {
     "track": 3,
     "title": "The Open Source Revolution",
     "tracked_concepts": [
       {
         "name": "OpenFisca",
         "role": "government-backed open-source framework...",
         "is_primary": true
       }
     ]
   }
   ```

### Shared Utilities

Both tools use `silico.utils`:

```python
from silico.utils import (
    parse_frontmatter,      # Extract YAML from markdown
    extract_title,          # Get H1 title
    get_manuscript_chapters,# Chapter discovery in order
    get_research_notes,     # Load research notes
)
```

## Architecture

```
silico/
├── tts_pipeline.py      # Basic TTS (OpenAI speech API)
├── tts_enhanced.py      # TTS + concept tracking
├── concept_tracker.py   # Validation system
└── utils.py            # Shared utilities

Modeled on:
- Robert Caro's filing system (canonical sources, labeled tracking)
- Obsidian Dataview (frontmatter queries)
- Modern build validation (CI-ready consistency checks)
```

## Development

```bash
# Run tests
pytest

# Install dev dependencies
pip install -e ".[dev]"
```

## Tracking Discipline

**Why tracking matters:**

The book integrates personal narrative with technical history. Concepts like "Tax-Calculator" appear in multiple chapters:
- Ch2 (Tax Model Wars): Historical context - "open-source tools emerging"
- Ch3 (Open Source Revolution): Personal discovery - "I found a tool..."

Without tracking, it's easy to:
1. Duplicate detailed introductions
2. Provide inconsistent details
3. Miss primary vs secondary mentions

**Solution:**

Research notes serve as **canonical source**. Manuscript references them. Tracking frontmatter documents where each concept appears and which chapter is primary.

This caught the Jensen/Tax-Calculator duplication during development.

## Future Extensions

Potential additions:
- Pre-commit hooks running `silico-check`
- Generate Obsidian graph from tracking data
- TTS voice customization per character/narrator
- Chapter-specific pacing/pauses
- Integration with MyST build process

---
description: Verify factual claims in a manuscript section against primary sources
allowed_tools:
  - Read
  - Grep
  - Glob
  - WebSearch
  - WebFetch
---

# Check Facts

Verify factual claims in the specified file or section.

## Usage

```
/check-facts manuscript/part-1-origins/02-orcutt.md
```

## Process

1. **Extract claims** from the file:
   - Numbers (percentages, dollar amounts, years)
   - Quotes and attributions
   - Historical assertions
   - Institutional facts

2. **Check against research notes** in `research/` directory

3. **Search for primary sources** when research notes insufficient

4. **Categorize findings**:
   - ✓ Verified (primary source found)
   - ⚠ Needs source (no citation found)
   - ✗ Potential error (source contradicts claim)

## Output

```
## Fact Check: [filename]

### Summary
- X claims verified
- Y claims need sources
- Z potential issues

### Details
[Specific findings with line numbers and sources]

### Sources to Add
[New sources that should be added to research notes]
```

## Arguments

$ARGUMENTS - Path to file to check (required)

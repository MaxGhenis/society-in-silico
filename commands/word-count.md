---
description: Show word count progress for the manuscript
allowed_tools:
  - Bash
  - Glob
  - Read
---

# Word Count

Track manuscript progress by word count.

## Usage

```
/word-count
/word-count manuscript/part-1-origins/
```

## Process

1. **Find all manuscript files** in the specified path (or all of `manuscript/`)
2. **Count words** in each file (excluding YAML frontmatter and code blocks)
3. **Calculate totals** by part and overall
4. **Compare to targets** (if set)

## Output

```
## Word Count: Society in Silico

### By Part
| Part | Chapters | Words | Target | Progress |
|------|----------|-------|--------|----------|
| Front Matter | 2 | 3,500 | 5,000 | 70% |
| Part I: Origins | 4 | 15,200 | 20,000 | 76% |
| Part II: Building | 5 | 18,100 | 25,000 | 72% |
| Part III: Future | 3 | 8,400 | 15,000 | 56% |
| **Total** | **14** | **45,200** | **65,000** | **70%** |

### By Chapter
| Chapter | Words | Status |
|---------|-------|--------|
| 01-introduction.md | 2,100 | Draft |
| 02-orcutt.md | 4,500 | Review |
...

### Notes
- Typical nonfiction book: 50,000-80,000 words
- Current pace: [words per chapter average]
```

## Arguments

$ARGUMENTS - Optional path to specific part or chapter. If omitted, counts entire manuscript.

## Implementation

Use bash to count words:
```bash
# Count words in markdown, excluding frontmatter
find manuscript -name "*.md" -exec sh -c '
  for f; do
    words=$(sed "1,/^---$/d" "$f" | sed "/^---$/,/^---$/d" | wc -w)
    echo "$f: $words"
  done
' sh {} +
```

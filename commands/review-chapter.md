---
description: Run full review pipeline on a chapter - style, facts, consistency, and narrative
allowed_tools:
  - Read
  - Grep
  - Glob
  - Task
  - WebSearch
  - WebFetch
---

# Review Chapter

Run comprehensive review on the specified chapter file.

## Usage

```
/review-chapter manuscript/part-1-origins/01-chapter-name.md
```

## Process

1. **Read the chapter** to understand content and structure
2. **Launch parallel reviews**:
   - Style editor agent for prose quality
   - Factchecker agent for claim verification
   - Consistency checker for terminology/naming
   - Research linker for wiki-link suggestions
3. **Synthesize findings** into prioritized action list
4. **Assess narrative** for flow, hooks, and engagement

## Output

Provide a unified review report with:
- Executive summary (2-3 sentences)
- Top 5 priority fixes
- Detailed findings by category
- Checklist for "ready for external review"

## Arguments

$ARGUMENTS - Path to the chapter file (e.g., `manuscript/front-matter/01-introduction.md`)

If no path provided, prompt for which chapter to review.

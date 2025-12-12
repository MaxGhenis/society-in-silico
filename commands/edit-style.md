---
description: Apply style edits to a section - converts passive voice, removes weak words, quantifies claims
allowed_tools:
  - Read
  - Edit
  - Grep
---

# Edit Style

Apply style improvements directly to a manuscript file.

## Usage

```
/edit-style manuscript/front-matter/01-introduction.md
```

## What It Does

Unlike `/review-chapter` which reports issues, this command **makes edits**:

1. **Read the file**
2. **Identify style issues**:
   - Passive voice constructions
   - Weak hedging words ("perhaps", "might", "it seems")
   - Unnecessary adverbs
   - Vague quantifiers ("many", "significant", "various")
3. **Apply fixes** using Edit tool
4. **Report changes** made

## Style Rules Applied

### Passive → Active
- "was calculated by" → "[subject] calculated"
- "has been shown to" → "shows"

### Remove Hedging
- "It should be noted that X" → "X"
- "It is worth considering that" → [delete]
- "perhaps" → [delete or strengthen]

### Remove Weak Adverbs
- "very important" → "important" or [stronger word]
- "really significant" → [quantify instead]
- "quite impressive" → [what specifically?]

### Quantify
- "significant increase" → "[X%] increase"
- "many people" → "[N] people"
- Flag if number not available: `[TODO: quantify]`

## Output

```
## Style Edits Applied: [filename]

### Changes Made
1. Line X: "was estimated by CBO" → "CBO estimated"
2. Line Y: "It should be noted that..." → [removed]
3. Line Z: "significantly reduced" → "reduced by [TODO: quantify]"

### Summary
- X passive→active conversions
- Y hedging phrases removed
- Z adverbs removed
- W items flagged for quantification

### Manual Review Needed
- Line A: Complex sentence, multiple possible rewrites
- Line B: "significant" - author should provide number
```

## Arguments

$ARGUMENTS - Path to file to edit (required)

## Caution

This makes direct edits. The file should be committed before running so changes can be reviewed/reverted via git.

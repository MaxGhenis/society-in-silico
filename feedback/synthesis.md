# Introduction Review Synthesis

**Date**: 2025-12-12
**Chapter**: manuscript/front-matter/01-introduction.md

## Executive Summary

Four parallel reviews identified **38 total issues** across style, facts, consistency, and research linking. The introduction has a strong foundation but needs tightening.

| Review | Issues | Grade |
|--------|--------|-------|
| Style | 23 | 7/10 |
| Factcheck | 8 | A- |
| Consistency | 4 | Strong |
| Research Links | 15 gaps, 8 links to add | Good foundation |

---

## Priority Actions (Top 10)

### Immediate Fixes

1. **Delete adverbs**: "quietly", "already" (x2), "exactly", "technically", "really"
   - Lines: 37, 46, 49, 64, 91, 61

2. **Add "microsimulation" to body text**
   - Currently only in wiki-links section
   - Suggest Line 33: "building microsimulation systems that model society"

3. **Fix open-source hyphenation**
   - Line 57: "open-source movement" → "open source movement"
   - Line 89: "open-source turn" → "open source turn"

4. **Clarify Westworld Paris terminology**
   - Line 29: "nuclear fire" → "thermonuclear incident" (show's term)
   - Or add temporal context: "In the 2020 third season of Westworld..."

5. **Cite GPT-4 67% accuracy**
   - Add footnote: Blair-Stanek et al. (2023), arXiv:2309.09992

### Style Tightening

6. **Delete self-describing phrases**
   - Line 31: Remove "chilling in its logic" (let quote speak for itself)
   - Line 61: Remove "The thesis is simple:" (let reader judge)

7. **Quantify vague timeframes**
   - Line 33: "spent years" → "spent [N] years"
   - Line 58: "through decades" → "through six decades" or "from 1957 to 2020s"

8. **Strengthen passive constructions**
   - Line 29: "watched Paris destroyed by" → "watched nuclear fire destroy Paris"
   - Line 47: "GPT-4 achieves" → "GPT-4 answers only 67% of tax questions correctly"

### Research Linking

9. **Add wiki-links to existing notes** (7 additions):
   ```markdown
   Line 57: [[guy-orcutt|Guy Orcutt]]'s 1957 vision
   Line 59: [[policyengine|PolicyEngine]] and [[cosilico|Cosilico]]
   Line 87: [[dynasim|DYNASIM]], [[ifs-taxben|IFS]], [[taxsim|NBER]]
   Line 89: [[openfisca|OpenFisca]], [[rules-as-code|code]]
   ```

10. **Create high-priority research notes**:
    - `ai-tax-accuracy.md` - GPT-4 67% finding with full citation
    - `distributional-analysis.md` - Core microsimulation concept
    - `orcutt-1957-paper.md` - Timeline entry for foundational document

---

## All Issues by Category

### Style (23 issues)

**Adverbs to delete**: quietly, already (x2), exactly, technically, really
**Vague timeframes**: "years", "decades" without specifics
**Self-describing phrases**: "chilling in its logic", "The thesis is simple"
**Emotional qualifiers**: "complicated recognition", "messy reality"
**Passive voice**: 2 instances
**Weak verbs**: "tell", "confronts"

### Factcheck (8 items)

**Verified ✓**: GPT-4 67%, Orcutt 1957, PolicyEngine founding, Serac/Rehoboam details
**Needs source ⚠**: "napkin math", "AI hallucinates eligibility", IFS/NBER impact
**Correction ✗**: "nuclear fire" → "thermonuclear incident"

### Consistency (4 issues)

- 2 hyphenation errors (open-source as noun phrase)
- "microsimulation" missing from body text
- Guy Orcutt needs context in Part I section

### Research Gaps (15 notes to create)

**Tier 1**: ai-tax-accuracy, orcutt-1957-paper, distributional-analysis, static-vs-dynamic
**Tier 2**: digital-public-goods, algorithmic-governance, technocracy-vs-democracy
**Tier 3**: westworld-serac, piketty/saez, behavioral-responses

---

## Established Style Conventions

From consistency review - apply to all chapters:

| Element | Convention |
|---------|------------|
| microsimulation | One word, lowercase |
| PolicyEngine | CamelCase |
| open source | Two words (no hyphen as noun) |
| open-source | Hyphenated only before noun |
| Numbers | Spell 1-9, numerals 10+ |
| Percentages | Always numerals (67%) |
| Years | Always numerals (1957) |
| Em dashes | No spaces (word—word) |
| Contractions | Encouraged for accessible tone |

---

## Next Steps

1. Apply immediate fixes (items 1-5)
2. Style pass (items 6-8)
3. Add wiki-links (item 9)
4. Create Tier 1 research notes (item 10)
5. Second review after edits

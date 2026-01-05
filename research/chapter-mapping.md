# Chapter-Concept Mapping

This file tracks where each concept, person, and model appears in the manuscript to prevent duplication and ensure consistency.

## Automated Map (Dataview)

```dataview
TABLE chapters as "Chapters", primary_chapter as "Primary", narrative_role as "Role"
FROM "research/concepts" OR "research/people"
WHERE chapters
SORT primary_chapter ASC, file.name ASC
```

## Key Principles

1. **Primary Chapter**: Where the main, detailed coverage appears
2. **Secondary Mentions**: Brief references or contextual appearances
3. **Consistency**: All details about a concept should match across chapters
4. **Source of Truth**: The research note is the canonical source; manuscript draws from it

## Manual Tracking (for quick reference while writing)

### Chapter 2: Tax Model Wars

**People:**
- Karen Smith (American Machinery) - PRIMARY
- Daniel Feenberg (Asymmetry Problem) - PRIMARY
- Howard Reed (UK Alternative) - PRIMARY
- Malcolm Torry (UK Alternative) - PRIMARY

**Concepts:**
- TAXSIM - PRIMARY
- EUROMOD - PRIMARY
- UKMOD - PRIMARY
- OpenFisca - BRIEF mention in Open Source Emergence
- Tax-Calculator - BRIEF mention in Open Source Emergence

### Chapter 3: Open Source Revolution

**Concepts:**
- OpenFisca - PRIMARY (opening, Two Architectures section)
- Tax-Calculator - PRIMARY (opening, Two Architectures section)
- Policy Simulation Library - PRIMARY

**People:**
- Matt Jensen - PRIMARY
- Martin Holmer - PRIMARY
- Max Ghenis - PRIMARY (personal narrative)

**Models:**
- OG-USA - mentioned
- FRB/US - mentioned
- Cost-of-Capital-Calculator - mentioned

## Notes

The Tax-Calculator "duplication" between Ch2 and Ch3 is intentional:
- Ch2: Historical context (open-source tools emerging)
- Ch3: Personal discovery ("I found a tool...")

This is appropriate - historical overview vs personal narrative. Just track to ensure detailed introductions don't duplicate.

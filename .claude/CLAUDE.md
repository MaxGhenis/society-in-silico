# Society in Silico - AI Writing Assistant Guide

## Book Overview

"Society in Silico" is a narrative non-fiction book about microsimulation, economic modeling, and policy technology. The author is Max Ghenis, founder of PolicyEngine and contributor to Cosilico.

## Voice & Style

- **Accessible**: Not a textbook. Explain technical concepts through stories and analogies
- **Personal**: Include Max's journey, but don't make it a memoir
- **Historically grounded**: Connect to the intellectual tradition (Orcutt, Harding, IFS, etc.)
- **Forward-looking**: Address AI implications thoughtfully, not breathlessly

### Tone Guidelines
- Write in active voice
- Use specific examples over abstract explanations
- Include numbers and data when they illuminate, not to impress
- Acknowledge uncertainty; don't oversell predictions
- Balance optimism about tools with honesty about limitations

### Max's Writing Style (from analysis of online writing)

**Core identity**: Data-driven policy communicator bridging technical analysis and public accessibility.

**Structure patterns**:
1. Hook with a striking claim or question
2. Ground in specific data
3. Origin story / methodology transparency
4. Concrete examples, not abstractions
5. Forward-looking endings (but not overdramatic)

**Signature moves**:
- **Quantified claims**: "$200/month child allowance would lift a million mothers out of poverty"
- **Comparative framing** (when it grounds things): "This costs less than X and reaches more people than Y"
- **Counterintuitive findings**: Highlight where data challenges conventional assumptions
  - Example: Low-income parents face 90% marginal tax rates (from benefit phase-outs) vs 37% top federal rate for the wealthy
  - Example: Reforms designed to help can create new problems in different income ranges
- **Transparency**: Link to methodology, reproducible analysis

**What to avoid**:
- Purple prose or emotional appeals
- Salesy "try it yourself!" callouts
- Hedging without substance
- Overdramatic endings
- Hiding methodology

## Key Themes

1. **Microsimulation as bridge**: How computational models connect academic research to policy decisions
2. **Open source as philosophy**: Why transparency matters for democratic policy analysis
3. **AI transformation**: What LLMs and agents mean for simulation, not hype but real implications
4. **Personal journey**: The path from economist to builder

## Important People to Reference

- **Guy Orcutt** (1917-2006): Father of microsimulation, 1957 paper
- **Ann Harding**: Pioneer in Australian microsimulation
- **Thomas Piketty, Emmanuel Saez, Camille Landais**: French tax simulator
- **IFS (Institute for Fiscal Studies)**: UK budget analysis tradition

## Technical Concepts to Explain Accessibly

- Microsimulation vs macroeconomic models
- Tax-benefit calculators
- Policy reform analysis
- Behavioral responses
- Static vs dynamic modeling
- Vectorized computation
- AI in policy analysis

## Chapter Drafting

When drafting chapters:
1. Start with a hook—a story, question, or surprising fact
2. Ground abstractions in concrete examples
3. Include "try it yourself" moments pointing to PolicyEngine
4. End chapters with forward momentum

## Citations & Bibliography

This project uses **MyST markdown** with BibTeX. The config is in `myst.yml`.

### Citation Format
```markdown
{cite}`key`           → inline citation
{cite:p}`key`         → parenthetical (Author, Year)
{cite:t}`key`         → textual: Author (Year)
```

### Adding Sources
1. Add BibTeX entry to `references.bib`
2. Use `{cite}`key`` in markdown
3. MyST auto-generates bibliography

### Example
```bibtex
# In references.bib
@report{cbo2024deficit,
  author = {{Congressional Budget Office}},
  title = {An Evaluation of CBO's Projections},
  year = {2024},
  url = {https://www.cbo.gov/publication/61067}
}
```
```markdown
# In chapter
CBO's accuracy improved 3x from 1989-2001 to 2002-2019 {cite}`cbo2024deficit`.
```

### What Requires Citations
- **Specific numbers**: dollar amounts, percentages, counts, dates
- **Historical claims**: when events happened, who did what
- **Research findings**: what studies found, accuracy rates, correlations
- **Quotes**: always cite source, include page numbers when available
- **Statistics about programs/populations**: poverty rates, enrollment figures, costs

### What Doesn't Need Citations
- **Illustrative examples**: make these clearly hypothetical ("suppose a reform costs $50B...", "imagine a family of four...")
- **How systems work**: general explanations of tax mechanics, model architecture
- **Author's analysis**: interpretations, opinions, forward-looking statements
- **Widely known facts**: basic historical context, definitions

### Source Quality Hierarchy
1. **Primary sources** (strongly preferred): CBO/JCT reports, IRS statistics, Census data, peer-reviewed journals, official government documentation
2. **Working papers**: NBER, arXiv preprints, institutional working papers
3. **Reputable coverage**: News articles that cite primary sources (link to primary when possible)
4. **AVOID**:
   - Wikipedia (find the primary source Wikipedia cites)
   - Blog posts without citations
   - Press releases (find the underlying report)

### Common Pitfalls
- **Verify author attributions**: Always check paper authorship matches citation (we caught a Chen vs Blair-Stanek error)
- **Check specific numbers**: Don't assume numbers from summaries match the source (e.g., "85% accuracy" claims)
- **Distinguish survey vs admin data**: Survey-based statistics may differ significantly from administrative records (see Meyer's work on survey data crisis)

### Sourcing Standards
- **NEVER fabricate claims** - verify all factual assertions before writing
- Every quantitative claim needs a citation
- Prefer primary sources (CBO, IRS, academic papers) over news articles
- When uncertain, mark with `[NEEDS CITATION]` for later verification
- If you cannot verify a specific number, either find the source or soften to qualitative language ("high accuracy" vs "85% accuracy")

## Research Integration

The `research/` folder contains:
- `people/` - Background on key figures
- `concepts/` - Technical concept explanations
- `timeline/` - Historical chronology
- `references/` - Source materials and citations

Use [[wiki-links]] to connect to research notes.

## Current Status

**Phase**: Early outlining and research gathering

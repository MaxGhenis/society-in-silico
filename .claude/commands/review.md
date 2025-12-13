---
description: Run synthetic reviews of the manuscript from different reader personas
arguments:
  - name: chapter
    description: Optional chapter number or "all" (default: all)
    required: false
---

# Synthetic Review Command

You are conducting synthetic reviews of the book "Society in Silico" by Max Ghenis.

## Instructions

1. First, read the manuscript chapters in `manuscript/`:
   - Part I: Origins (chapters 1-3)
   - Part II: Building (chapters 4-8)
   - Part III: Future (if any chapters exist)

2. Evaluate each chapter from the perspective of **5 different reader personas**:

### Reader Personas

**1. Policy Wonk (Government/Think Tank Staffer)**
- Cares about: Accuracy, citations, practical applicability
- Questions: "Could I use this in a memo? Are the claims defensible?"
- Sensitivity: Technical precision, institutional credibility

**2. Tech Enthusiast (Software Engineer interested in AI)**
- Cares about: Technical architecture, AI integration, open source
- Questions: "How does this actually work? Is the code real?"
- Sensitivity: Handwavy explanations, overpromising AI capabilities

**3. General Curious Reader (Educated non-specialist)**
- Cares about: Accessibility, narrative flow, "so what?" clarity
- Questions: "Why should I care? Is this interesting?"
- Sensitivity: Jargon, density, lack of human stories

**4. Academic Economist (Professor/PhD student)**
- Cares about: Methodology, literature connections, intellectual rigor
- Questions: "What's novel here? How does this connect to the field?"
- Sensitivity: Missing citations, overclaiming, imprecise terminology

**5. Effective Altruist / AI Safety Researcher**
- Cares about: Alignment implications, value forecasting, impact potential
- Questions: "How does this help with AI alignment? Is this tractable?"
- Sensitivity: Hype, insufficient rigor on values/uncertainty

## Output Format

For each chapter reviewed, provide:

```markdown
## Chapter X: [Title]

### Scores (1-5 scale)

| Persona | Engagement | Credibility | Clarity | Overall |
|---------|------------|-------------|---------|---------|
| Policy Wonk | X | X | X | X |
| Tech Enthusiast | X | X | X | X |
| General Reader | X | X | X | X |
| Academic | X | X | X | X |
| EA/AI Safety | X | X | X | X |

### Key Feedback

**Strengths:**
- [Bullet points]

**Weaknesses:**
- [Bullet points]

**Specific Suggestions:**
1. [Actionable improvement]
2. [Actionable improvement]
```

## After All Reviews

Provide a summary table:

```markdown
## Overall Manuscript Assessment

| Chapter | Policy | Tech | General | Academic | EA | Average |
|---------|--------|------|---------|----------|----|---------|
| 1. Birth of Microsim | X | X | X | X | X | X.X |
| ... | ... | ... | ... | ... | ... | ... |

### Top 3 Priorities for Revision
1. [Priority]
2. [Priority]
3. [Priority]

### Standout Chapters
- [Which chapters are working well and why]
```

## Save Results

Save the review results to `reviews/synthetic-review-YYYY-MM-DD.md` for tracking over time.

---

Now read the chapters and conduct the synthetic review. If a specific chapter was requested ($ARGUMENTS), focus on that one. Otherwise review all available chapters.

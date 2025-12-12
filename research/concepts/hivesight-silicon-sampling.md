# HiveSight: Silicon Sampling for Survey Research

## Overview

HiveSight is a web application for AI-powered survey simulation. It uses "silicon sampling"—LLMs conditioned on demographic traits—to generate survey responses that correlate with human data.

**Tagline**: "Simulate Public Opinion At Scale"

Live: hivesight.ai
Repository: `/Users/maxghenis/hivesight/hivesight/`

## Core Mechanism

1. User enters a survey question
2. Selects demographic filters (age, income, state)
3. HiveSight generates personas from PolicyEngine/Cosilico microdata
4. GPT-4o/Mini answers as each persona
5. Results aggregated with statistics and visualizations

```
Question + Demographics → Representative Microdata Personas → LLM as Each Persona → Aggregated Results
```

## The Diversity Problem (Key Insight)

**The fundamental LLM limitation**: LLMs predict the "most likely" response based on training data + RLHF. They don't naturally produce the diversity of human opinion.

**Temperature is not the answer**: The temperature parameter adds random noise, but that's fundamentally different from structured human variation. Real people's opinions vary in ways that correlate with their demographics, experiences, and circumstances—not randomly.

**The microdata solution**: HiveSight uses PolicyEngine/Cosilico microdata to construct representative demographic profiles. This grounds diversity in actual population distributions rather than LLM temperature noise.

Compare:
| Approach | How variation is generated | Problem |
|----------|---------------------------|---------|
| Raw LLM | Predicts modal response | No diversity |
| Temperature | Adds random noise | Unstructured, unrealistic |
| **Microdata personas** | Sample from actual population | Reflects real demographic variation |

**Analogy to microimpute**: This mirrors how quantile regression forests in microimpute work—modeling not just the mean but the full conditional distribution. HiveSight does the same for opinions: instead of asking "what would the average person say?", it asks "what would person with characteristics X, Y, Z say?" across a representative sample of actual demographic profiles.

## The Science

Key validation research:

| Study | Finding |
|-------|---------|
| Argyle et al. (2023) | GPT-3 with demographics reproduces voting patterns at 85%+ accuracy |
| Mei et al. (2024) | ChatGPT/GPT-4 reproduce human behavior across 6 canonical psychology studies |
| Sarstedt et al. (2024) | Silicon sampling viable for pretesting and pilot studies |

Known limitations:
- **WEIRD bias**: Better for Western populations (training data distribution)
- **Sample size**: Unreliable below ~200 simulated respondents
- **Complementary use**: Best alongside, not replacing, traditional research

## Connection to the Simulation Stack

| Tool | Question | Method |
|------|----------|--------|
| **PolicyEngine** | "How does Policy X affect households?" | Deterministic microsimulation |
| **Democrasim** | "How does voter knowledge affect elections?" | Agent-based simulation |
| **HiveSight** | "How would people respond to Question X?" | LLM persona simulation |
| **Cosilico** | "Can AI agents encode policy rules reliably?" | Agentic rule encoding |

## Key Differentiators

From thesis competitive analysis:

| Feature | Qualtrics | SurveyMonkey | EDSL | HiveSight |
|---------|-----------|--------------|------|-----------|
| AI respondents | ✗ | ✗ | ✓ | ✓ |
| Web UI (no code) | ✓ | ✓ | ✗ | ✓ |
| Instant results | ✗ | ✗ | ✓ | ✓ |
| Low cost | ✗ | ✗ | ✓ | ✓ |

HiveSight is the first tool combining AI respondents + web UI + instant results + demographic targeting.

## Business Model

- **Credits**: $0.10 each, 4 respondents/credit (Likert) or 2/credit (open-ended)
- **Subscriptions**: $29/mo (1K credits) or $99/mo (10K credits)
- **Gross margin**: ~75% (API costs ~$0.025/credit)

Target: $140B market research industry, with 69% of professionals already using synthetic data.

## HiveSight-Calibration Research

Parallel research project: `/Users/maxghenis/hivesight/hivesight-calibration/`

Goal: Calibrate LLM response distributions against General Social Survey (GSS) data.

Method:
1. Extract GSS respondent demographics + actual responses
2. Run LLM with matched persona profiles
3. Learn conditional distribution P(actual | LLM, demographics)
4. Deploy calibrated confidence intervals in HiveSight

This would provide defensible methodology for synthetic survey research.

## Implications for "Society in Silico"

### 1. Another Layer of Simulation

The book's narrative can now span:
- **Microsimulation**: How policies affect people (Part II)
- **Opinion simulation**: How people respond to policies (extension)
- **Democratic simulation**: How opinions become elections (extension)

### 2. The Accuracy Problem (Again)

Like the GPT-4 67% accuracy stat in the intro, HiveSight faces the "can you trust AI?" question. But the answer is the same:

> LLMs conditioned on demographics achieve 85%+ accuracy for many question types. For rapid prototyping and hypothesis generation, that's valuable—especially when the alternative is no data at all.

### 3. Complementary, Not Replacement

The thesis is explicit: "Silicon sampling is best used alongside traditional research, not as a complete replacement."

This mirrors the book's argument: deterministic tools complement AI, not replace it.

### 4. Democratizing Research Access

HiveSight democratizes survey research the same way PolicyEngine democratizes policy analysis:
- Expensive panels ($5-50/response) → $0.025/response
- Weeks of fieldwork → Instant results
- Requires procurement → Self-serve

## Potential Book Angles

1. **The Simulation Landscape**: Different tools for different layers of society modeling
2. **Trust and Validation**: How do we trust AI outputs? Calibration, validation, transparency
3. **Democratization Pattern**: Same story playing out across domains
4. **Max's Portfolio**: PolicyEngine + Cosilico + Democrasim + HiveSight as coherent vision

## Quotes from Thesis

Industry adoption:
> "Within three years, more than half of market research may be done using AI-created synthetic personas instead of humans." — Qualtrics 2025 Report

On limitations:
> "We're transparent about methodology. Position as rapid prototyping and hypothesis generation, not replacement for high-stakes research."

## Sources

- HiveSight thesis page: `/src/app/(public)/thesis/page.tsx`
- HiveSight calibration README: `/hivesight-calibration/README.md`
- Argyle et al. 2023: "Out of One, Many: Using Language Models to Simulate Human Samples"

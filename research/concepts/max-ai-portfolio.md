# Max's AI & Simulation Portfolio

## Overview

A coherent vision emerges across multiple projects: using AI and simulation to make complex systems (policy, economics, decisions, retirement) tractable for individuals and researchers.

## The Projects

### 1. PolicyEngine
**What**: Open-source tax-benefit microsimulation
**AI Role**: Claude for explanations, GPT-4 for narratives, multi-agent workflows for research
**Key Insight**: Deterministic calculations as infrastructure that AI calls

### 2. Cosilico
**What**: Agentic rule encoding for policy
**AI Role**: LLMs encode statutes with deterministic oracles for verification
**Key Insight**: "Deterministic tools will always be faster, auditable, legally citable; LLMs will call tools"

### 3. HiveSight
**What**: AI-powered survey simulation ("silicon sampling")
**AI Role**: LLMs conditioned on demographics generate survey responses
**Key Insight**: Microdata provides structured human variation that temperature can't replicate

### 4. Democrasim
**What**: Voter behavior → election → policy outcome simulation
**AI Role**: None currently (deterministic agent-based model)
**Key Insight**: Voter "accuracy" parameter captures what informed tools provide

### 5. Farness
**What**: Decision-making framework that reframes advice-seeking as forecasting
**AI Role**: Forces LLMs to make numeric predictions instead of vague advice
**Key Insight**: "Making numeric predictions forces mechanism thinking, creates accountability, and reduces sycophancy"

Repository: `/Users/maxghenis/farness/`

Core framework:
- **KPIs**: Define what success looks like (measurable outcomes)
- **Options**: Expand beyond A vs B (what about C? waiting? hybrid?)
- **Forecasts**: Point estimates + confidence intervals + reasoning
- **Tracking**: Log decisions, review outcomes, calibrate over time

Why it works:
- Reduces sycophancy (harder to just agree when making numbers)
- Forces mechanism thinking (must reason about cause and effect)
- Creates accountability (predictions can be scored)
- Separates values from facts (you pick KPIs, forecasts are facts)

### 6. LLM-ETI
**What**: Research paper on LLMs simulating behavioral responses to tax policy
**AI Role**: LLMs as experimental subjects replicating human economics studies
**Key Insight**: LLMs can simulate Elasticity of Taxable Income (ETI) responses, replicating lab experiments

Repository: `/Users/maxghenis/llm-eti/`

Two-study approach:
1. Lab experiment replication (Pfeil et al. 2024) - 16-round tax decision game
2. Observational study replication (Gruber & Saez 2002) - simulated real-world responses

Co-authored with Jason DeBacker.

### 7. LLM Presidential Outcome Forecasts
**What**: Comparing LLM predictions for policy outcomes under different administrations
**AI Role**: LLMs as forecasters using narrative prompting
**Key Insight**: Systematic differences between models (GPT-4, Grok) in policy predictions

Repository: `/Users/maxghenis/llm-presidential-outcome-forecasts/`

Metrics: Air quality, GDP, poverty
Method: Narrative prompting from Cunningham et al. (2024)

### 8. OptiqAL
**What**: QALY impact estimator for lifestyle choices
**AI Role**: Claude synthesizes medical evidence to estimate quality-adjusted life impact
**Key Insight**: AI can translate research literature into personalized, quantified health guidance

Repository: `/Users/maxghenis/optiqal-ai/`

Flow: Lifestyle change → Evidence search → QALY estimate → Personalization → Uncertainty quantification

### 9. Fred Forecaster
**What**: Time series forecasting for Federal Reserve Economic Data
**AI Role**: None (classical statistics + Bayesian methods)
**Key Insight**: Calibration to external targets (e.g., CBO forecasts) improves predictions

Repository: `/Users/maxghenis/fred-forecaster/`

Methods:
- SARIMAX modeling
- Bayesian structural time series (PyMC)
- Simulation reweighting to match targets

### 10. EggNest
**What**: Monte Carlo retirement simulation with real tax calculations
**AI Role**: None (PolicyEngine for taxes, NumPy for Monte Carlo)
**Key Insight**: 10,000+ scenarios show probability distributions, not just expected values

Repository: `/Users/maxghenis/eggnest/`

Stack: React + FastAPI + PolicyEngine-US + NumPy

### 11. Manifold Stock Bot
**What**: Trading bot for prediction markets based on stock movements
**AI Role**: None (rule-based trading)
**Key Insight**: Prediction markets as a mechanism for aggregating information

Repository: `/Users/maxghenis/manifold-stock-bot/`

## Emerging Themes

### 1. The Diversity Problem
Multiple projects address the same challenge: how to get realistic variation from AI systems.

| Project | Solution |
|---------|----------|
| HiveSight | Microdata personas |
| LLM-ETI | Demographic conditioning |
| Farness | Force numeric predictions with CIs |
| EggNest | Monte Carlo simulation |

**The pattern**: Temperature/randomness isn't enough. You need structured variation grounded in real distributions.

### 2. AI + Deterministic Infrastructure
The consistent architecture:

```
User Query → LLM (interpretation/communication) → Deterministic Tool (calculation) → LLM (explanation) → User
```

Projects following this:
- PolicyEngine (Claude explains, engine calculates)
- Cosilico (LLMs encode, oracles verify)
- HiveSight (microdata structures, LLMs respond)
- EggNest (PolicyEngine calculates taxes)
- OptiqAL (Claude synthesizes, evidence grounds)

### 3. Forecasting as Epistemics
Multiple projects treat forecasting as a way to improve reasoning:

- **Farness**: Reframe advice as forecasts to reduce sycophancy
- **LLM-ETI**: Can LLMs predict behavioral responses?
- **LLM Presidential Forecasts**: Can LLMs predict policy outcomes?
- **Fred Forecaster**: Calibrated economic predictions
- **Manifold Stock Bot**: Prediction market arbitrage

**The thesis**: Making predictions forces clarity, creates accountability, and improves over time through calibration.

### 4. Democratization Pattern
Every project follows the same arc:

| Domain | Before | After |
|--------|--------|-------|
| Policy analysis | CBO/JCT monopoly | PolicyEngine for anyone |
| Survey research | $50K panels | HiveSight for $50 |
| Retirement planning | Fee-only advisors | EggNest for free |
| Medical research synthesis | Literature reviews | OptiqAL instant |
| Decision support | Expensive consultants | Farness framework |

### 5. Quantification Over Intuition
A consistent preference for numbers over vibes:

- Farness: Point estimates + CIs, not "I think you should..."
- OptiqAL: QALYs, not "this might be healthy"
- EggNest: Probability distributions, not "you'll probably be fine"
- HiveSight: Statistical aggregates, not "people would like this"

## For "Society in Silico"

### Chapter Possibilities

1. **The Forecasting Mindset**: Farness + LLM forecasting projects as a philosophy of epistemics
2. **Diversity in Simulation**: The microdata insight across HiveSight, Democrasim, PolicyEngine
3. **AI as Infrastructure User**: How LLMs become tool-callers, not tool-replacers
4. **Democratizing Expertise**: The common pattern across all projects

### Narrative Arc

Part I (History): Guy Orcutt → microsimulation tradition
Part II (Building): PolicyEngine + Cosilico + the AI integration philosophy
Part III (Future): The full stack (HiveSight + Democrasim + AI agents) + Farness epistemics

### Key Quotes to Surface

From Farness README:
> "Making numeric predictions forces mechanism thinking, creates accountability, and reduces sycophancy"

From Cosilico thesis:
> "Deterministic tools will always be faster, auditable, and legally citable; LLMs will call tools"

From HiveSight thesis:
> "Within three years, more than half of market research may be done using AI-created synthetic personas"

## Technical Connections

| Project A | Project B | Integration |
|-----------|-----------|-------------|
| PolicyEngine | HiveSight | Microdata for personas |
| PolicyEngine | EggNest | Tax calculations |
| PolicyEngine | Cosilico | Rule encoding validation |
| Democrasim | HiveSight | Voter opinion simulation |
| Farness | All | Decision framework for development |
| Fred Forecaster | EggNest | Economic assumptions |

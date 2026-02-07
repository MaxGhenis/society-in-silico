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

### Introduction
- Rehoboam/Westworld hook
- Blair-Stanek GPT-4 tax accuracy (67%)
- TaxCalcBench results (41.7% best general-purpose)
- Ohio parent marginal tax rate example

### Chapter 1: Birth of Microsimulation
- **Guy Orcutt** - PRIMARY (full biography and 1957 paper)
- DYNASIM - mentioned
- Alice Rivlin - mentioned (1961 coauthor)

### Chapter 2: Tax Model Wars
**People:**
- Alice Rivlin (CBO founding) - PRIMARY
- Karen Smith (Urban Institute) - PRIMARY
- Daniel Feenberg (TAXSIM) - PRIMARY
- Howard Reed (Landman Economics) - PRIMARY
- Malcolm Torry (Citizen's Basic Income Trust) - PRIMARY
- C. Eugene Steuerle & Leonard Burman (TPC founders)
- Kent Smetters (PWBM)

**Concepts:**
- TAXSIM - PRIMARY
- EUROMOD - PRIMARY (transition to JRC)
- UKMOD - PRIMARY
- IFS/TAXBEN - PRIMARY
- Tax Policy Center - PRIMARY
- Penn Wharton Budget Model - PRIMARY
- CBO/JCT institutional history - PRIMARY
- Dynamic scoring debate - PRIMARY
- OpenFisca - BRIEF (Open Source Emergence)
- Tax-Calculator - BRIEF (Open Source Emergence)

### Chapter 3: Open Source Revolution
**Concepts:**
- OpenFisca - PRIMARY (founding, architecture, LexImpact)
- Tax-Calculator - PRIMARY (opening, Two Architectures)
- Policy Simulation Library - PRIMARY
- Rules as Code movement - PRIMARY
- Piketty-Saez-Landais revolution-fiscale.fr - PRIMARY

**People:**
- Matt Jensen - PRIMARY
- Martin Holmer - PRIMARY
- Max Ghenis - PRIMARY (personal narrative: Berkeley, Google, Alex, UBI Center)
- Mahdi Ben Jelloul & Clément Schaff (OpenFisca creators)

**Models:**
- OG-USA - mentioned
- FRB/US - mentioned

### Chapter 4: The Accuracy Question
- CBO deficit projection accuracy - PRIMARY
- TAXSIM validation - back-reference to Ch 2
- PolicyEngine validation (HM Treasury ATRS) - back-reference to Ch 5
- Meyer survey data crisis - PRIMARY
- Box quote ("all models are wrong")

### Chapter 5: PolicyEngine Proof of Concept
- PolicyEngine - PRIMARY (origin, development, growth)
- UBI Center - mentioned (predecessor)
- Nikhil Woodruff - PRIMARY
- HM Treasury ATRS evaluation - PRIMARY
- Digital Public Good recognition

### Chapter 6: Three Ingredients of Microsimulation
- Rules encoding architectures (EUROMOD XML vs Python)
- Microdata construction (CPS, Enhanced CPS)
- Behavioral dynamics (elasticities, structural)
- HM Treasury - back-reference to Ch 5
- Tax-Data - mentioned

### Chapter 7: The Household View
- Benefit cliffs - PRIMARY
- Marginal tax rates - PRIMARY
- SSI phase-out example
- SNAP categorical cliff
- HM Treasury - back-reference to Ch 5
- UK Universal Credit taper

### Chapter 8: The Society View
- Distributional analysis - PRIMARY
- Budget scoring - PRIMARY
- Poverty measurement
- CTC expansion 2021 analysis

### Chapter 9: AI Enters the Picture
- LLM tool-use paradigm - PRIMARY
- PolicyEngine ChatGPT integration
- TaxCalcBench benchmark
- AI Economist (Zheng et al.)
- TaxAgent (Wang et al.)

### Chapter 10: Cosilico
- Rules Foundation / RAC - PRIMARY
- Cosilico commercial layer - PRIMARY
- Open-core model - PRIMARY
- Avalara market comparison
- HM Treasury - back-reference to Ch 5

### Chapter 11: The Uncertainty Gap
- Monte Carlo methods - PRIMARY
- Squigglepy - PRIMARY
- Prediction markets (Tetlock, Polymarket)
- CBO projection uncertainty

### Chapter 12: Simulating Opinion
- HiveSight - PRIMARY
- Silicon sampling - PRIMARY
- Argyle et al. 2023 - PRIMARY
- Santurkar et al. 2023 (WEIRD bias)
- Bisbee et al. 2024 (limitations)
- Park et al. 2023 (generative agents)

### Chapter 13: Simulating Democracy
- Democrasim - PRIMARY
- Achen & Bartels - PRIMARY
- Caplan - PRIMARY
- Arrow's impossibility theorem
- Futarchy (Hanson)
- Lupia & McCubbins (information shortcuts)

### Chapter 14: Simulating Values
- Value forecasting methodology - PRIMARY
- GSS empirical test - PRIMARY
- EMOS calibration - PRIMARY
- HOMOSEX reversal case study
- Constitutional AI (Anthropic) - mentioned
- Stuart Russell "Human Compatible" - mentioned
- Philosophical precedents (Rawls, Habermas, Sen/Nussbaum)

### Chapter 15: Society in Silico
- Guy Orcutt - bookend reference (intentional echo of Ch 1)
- Full simulation stack summary
- Open vs closed systems

## Notes

The Tax-Calculator "duplication" between Ch2 and Ch3 is intentional:
- Ch2: Historical context (open-source tools emerging)
- Ch3: Personal discovery ("I found a tool...")

PolicyEngine appears in nearly every chapter because it's the central subject. The concept tracker flags this but it's acceptable — each chapter uses PE differently.

Guy Orcutt bookends Ch1 and Ch15 intentionally (narrative arc).

## Duplication to fix

### MAJOR: Meyer survey data crisis (Ch 4 vs Ch 8)
Ch 4 has full treatment (lines 128-143): Bruce Meyer, 40-50% SNAP, 60% TANF, 33% housing, seniors 30% higher in admin, 9.1% vs 6.9% poverty, top-coding, declining response rates.
Ch 8 (lines 29-37) repeats nearly identical stats. **Fix: Ch 8 should back-reference Ch 4 and focus on how PolicyEngine addresses data problems (enhanced CPS), not re-explain the problem.**

### MODERATE: GPT-4 67% accuracy (Intro vs Ch 10)
Introduction (lines 21-23) establishes the stat as the book's hook.
Ch 10 (line 45) re-introduces the stat as if new: "Blair-Stanek et al. (2023) developed SARA..."
Ch 15 (line 139) uses it as a conclusion callback (acceptable bookend).
**Fix: Ch 10 should reference the intro ("As we saw in the introduction...") not re-introduce the finding.**

### MODERATE: "Hallucinated phase-outs" phrasing (Intro vs Ch 10)
Introduction: "It misread the statutes. It confused filing statuses. It hallucinated phase-out thresholds that didn't exist."
Ch 10: "The models confused marginal and effective rates. They misapplied filing status rules. They hallucinated phase-out thresholds that didn't exist."
**Fix: Vary Ch 10 language or cut the repeated phrasing entirely (reader already knows this).**

### MINOR: HM Treasury 60% stat (Ch 5 vs Ch 7)
Ch 5 has primary coverage. Ch 7 (line 132) repeats the specific "60% of National Insurance calculations within 0.5%". Other chapters (6, 10) correctly back-reference without repeating specific numbers.
**Fix: Ch 7 should reference Ch 5 without the specific stat.**

## Duplication that's acceptable

Run `python scripts/concept_tracker.py` regularly. Current acceptable issues:
- PolicyEngine re-introduced in multiple chapters (central subject; each chapter uses it differently)
- TAXSIM re-introduced in Ch 4 (back-reference to Ch 2)
- Tax-Calculator in Ch 2 and 3 (intentional: historical context vs personal discovery)
- Guy Orcutt in Ch 1 and 15 (intentional bookend)
- Orcutt brief mentions in Intro, Ch 3, Ch 11 (appropriate callbacks)
- HM Treasury mentioned in Ch 5, 6, 7, 10, 15 (Ch 5 is primary; others mostly back-reference correctly)
- CBO/JCT/Treasury listed in Intro and Ch 15 (just naming agencies, not re-explaining)

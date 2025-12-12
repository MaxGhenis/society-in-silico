# Simulation Accuracy: Successes and Failures

**Key insight**: Policy analysis is typically a comparison of two simulations—baseline vs. reform. Errors in either compound.

## The Two-Simulation Problem

Every policy score involves:
1. **Baseline projection**: What happens under current law
2. **Reform projection**: What happens with the change
3. **Policy effect**: The difference between them

Errors in baseline can swamp the policy effect estimate.

## CBO's Self-Assessment

CBO regularly evaluates its own accuracy ([Accuracy of Projections](https://www.cbo.gov/topics/budget/accuracy-projections)):

### Overall Performance
- Budget-year revenue projections: average error of 1.2%
- CBO forecasts tend to be more accurate than Administration and Blue Chip consensus
- About half of two-year forecasts more accurate than Survey of Professional Forecasters

### Known Weaknesses
> "Quickly identifying new trends—particularly in federal spending on health care—and incorporating them into the agency's baseline projections has proved difficult."

Financial sector disruptions particularly challenging to anticipate.

## Case Studies: When Simulation Got It Wrong

### IRA Clean Energy Tax Credits (2022-present)

**Original CBO/JCT estimate (August 2022):**
- Clean vehicle credits: **$14 billion** over 10 years
- Total energy provisions: ~$400 billion

**Revised estimates (2024):**
- Clean vehicle credits: **$173 billion** (12x original)
- Total energy provisions: ~$870 billion (2x original)

**What happened:**
- Treasury created leasing loophole, dramatically expanding eligibility
- Uptake exceeded all models' assumptions
- Behavioral response to incentives was stronger than anticipated

**Implications:**
- Original score showed IRA reducing deficit by ~$90B
- Revised estimates show IRA *increasing* deficit by ~$300B
- The policy effect flipped sign

**Source:** [CRFB analysis](https://www.crfb.org/blogs/ira-energy-provisions-could-cost-two-thirds-more-originally-estimated)

### Medicare Part D (2003-2013)

**Original CBO estimate (2003):**
- Projected enrollment 2006-2010: 38.4 million average
- Projected 2010 per-beneficiary cost: $1,824

**Actual:**
- Actual enrollment: 31.3 million (18% lower)
- Actual 2010 per-beneficiary cost: $1,532 (16% lower)
- Total spending **50% lower** than projected by 2013

**What happened:**
- Lower-than-expected enrollment (57% of error)
- Generic drug wave after patent expirations (40% drop in national drug spending vs projections)
- Competition among Part D plans kept margins low

**Source:** [CBO Part D retrospective](https://www.cbo.gov/sites/default/files/cbofiles/attachments/12-01-MedicarePartD.pdf)

### Medicare Part D 2026 (Current)

**January 2025 shock:**
- Private insurers bid 35% increase in 2026 per-enrollee costs
- CBO expected ~5% increase
- If sustained, **$500 billion more** over next decade than projected

**Possible causes:**
- Reduced competition (market instability)
- Tariff uncertainty on pharmaceutical imports
- New high-cost drugs entering market

**Source:** [CBO call for research](https://www.cbo.gov/publication/61824)

## Case Studies: When Simulation Informed Policy

### EITC and CTC Expansions

Microsimulation models (TRIM3, ITEP, Tax-Calculator, TPC) were used to:
- Estimate poverty reduction from 2021 expansions
- Target credits to maximize impact per dollar

**Results validated:**
> "Together, the child tax credit and the EITC (both expanded in 2021) and the Child and Dependent Care Tax Credit lifted 9.6 million people out of poverty in 2021."
> — Census Bureau

**The models were right** about directional impact and approximate magnitude.

**Source:** [National Academies report](https://www.nationalacademies.org/news/federal-tax-credits-in-2021-lifted-more-than-2-million-children-out-of-poverty-says-new-report)

### State CTC Analysis

ITEP microsimulation modeled state-level child tax credits to:
- Estimate poverty reduction by state
- Identify credit levels needed for 25% and 50% poverty reduction targets
- Compare cost-effectiveness vs. state EITC expansions

Conclusion: Refundable CTCs more progressive and targeted than state EITC expansions.

**Source:** [ITEP 50-state analysis](https://itep.org/state-child-tax-credits-and-child-poverty-50-state-analysis/)

## Why Simulations Fail

### 1. Baseline Uncertainty
- Economic conditions change
- Existing policy implementation evolves
- Trends reverse unexpectedly

### 2. Behavioral Response Uncertainty
- How will people/firms respond to new incentives?
- Models use historical elasticities, but novel policies may differ
- Leasing loophole in IRA: unmodeled behavior

### 3. Implementation Uncertainty
- Regulatory decisions affect who's eligible
- Administrative capacity affects take-up
- CBO/JCT can't predict Treasury interpretations

### 4. Structural Breaks
- Generic drug wave wasn't in Part D models
- Financial crises not in baseline
- Pandemics not in baseline

## Lessons for the Book

### Honesty About Limitations
Simulation isn't prophecy. It's structured reasoning about counterfactuals given assumptions.

### The Value Proposition
Even with errors, simulation provides:
- Explicit assumptions (auditable, debatable)
- Distributional information (who gains, who loses)
- Scenario comparison (this vs. that)
- Feedback mechanism (model vs. actual → model improvement)

### The Baseline Problem
CBO's errors often come from **baseline**, not policy effect estimation. This suggests:
- Better baselines matter more than fancier policy models
- Real-time data integration could help
- Uncertainty quantification should be standard

### Open Source Advantage
When models are open:
- Assumptions are transparent
- Others can challenge parameters
- Faster correction when reality diverges

## Key Quotes

From CBO:
> "Model results can generate important insights and, on many questions, reasonably accurate forecasts. At the end of the day, however, policies must also be based on values and therefore should be informed, but not determined, by scientific data."

## Sources

- [CBO Accuracy of Projections](https://www.cbo.gov/topics/budget/accuracy-projections)
- [CBO Economic Forecasting Record: 2025](https://www.cbo.gov/publication/61334)
- [CBO Part D retrospective](https://www.cbo.gov/sites/default/files/cbofiles/attachments/12-01-MedicarePartD.pdf)
- [CRFB on IRA costs](https://www.crfb.org/blogs/ira-energy-provisions-could-cost-two-thirds-more-originally-estimated)
- [National Academies on tax credits](https://www.nationalacademies.org/news/federal-tax-credits-in-2021-lifted-more-than-2-million-children-out-of-poverty-says-new-report)

## Links

- [[microsimulation-definition]]
- [[taxsim]]
- [[ifs-taxben]]
- [[policyengine]]
- [[cosilico]]

## Tags

#concept #accuracy #limitations #honesty

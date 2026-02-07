---
chapters: [11, 4]
primary_chapter: 11
narrative_role: "The gap between microsimulation point estimates and the uncertainty they carry"
---

# Uncertainty in Microsimulation

## The Problem

Every microsimulation estimate is a point estimate. CBO says a policy costs $50 billion. TPC says it costs $47 billion. PolicyEngine says $52 billion. None provides confidence intervals.

This is a structural omission, not a technical impossibility.

## Five Sources of Uncertainty

(Per the academic literature)

1. **Input data** — sampling errors from surveys
2. **Model structure** — methodological choices
3. **Model specification** — choice of covariates, functional forms
4. **Model parameters** — imprecision in estimated values (elasticities, take-up rates)
5. **Monte Carlo variation** — from stochastic processes in dynamic models

## Key Academic Work

### Pudney and Sutherland (1994)
"How reliable are microsimulation results?" Journal of Public Economics, 53(3), pp. 327-365.
First rigorous analysis. Found baseline simulations reasonably accurate, but some widely-used measures of policy change effects "may be very imprecise."

### National Research Council (1991)
*Improving Information for Social Policy Decisions*. Called for a "second revolution" to improve microsimulation quality. Recommended systematic studies of parameter uncertainty.

### McClelland, Khitatrakun, and Lu (2020)
"Estimating Confidence Intervals in a Tax Microsimulation Model," International Journal of Microsimulation, 13(2), pp. 2-20.
Applied bootstrap methods to the Tax Policy Center model. Key finding: most point estimates had tight confidence intervals, but proposals affecting few taxpayers had considerably wider intervals. Open-source code on GitHub.

### Goedeme et al. (2013)
"Testing the Statistical Significance of Microsimulation Results: A Plea," International Journal of Microsimulation, 6(3).
Argued that significance testing is feasible for static microsimulation. Standard routines can calculate sampling variance while accounting for complex survey design.

## Methods

- **Bootstrap resampling**: Most common. McClelland et al. showed it's computationally tractable even for large models.
- **Normal approximation**: Works for large-impact proposals, breaks down for small populations.
- **Parametric bootstrap**: Draw coefficients from estimated distributions.
- **Repeated stochastic simulation**: Different random seeds for Monte Carlo variation.

## Who Does It?

**Almost nobody routinely.**

- **Tax Policy Center**: Published bootstrap CIs (McClelland 2020) but not in routine output
- **EUROMOD**: Goedeme et al. provided tools, but standard errors not routinely published
- **CBO**: Publishes uncertainty fan charts on *baseline projections* (since 2004), but NOT on individual cost estimates for legislation
- **PolicyEngine**: No published uncertainty methodology
- **JCT**: No published uncertainty ranges

## CBO Fan Charts

CBO has published uncertainty ranges on baseline budget projections since January 2004:
- Methodology paper: April 2004, "The Uncertainty of Budget Projections"
- Uses RMSE of historical forecast errors (22 baselines, 1981-2003)
- ±1 RMSE ≈ two-thirds of likely variation
- 90% confidence range shown as fan chart
- Extended to long-term projections in 2014

**Critical distinction**: Fan charts apply to overall fiscal outlook, NOT to individual bill scores. When CBO says a bill costs $50B, there's no published confidence interval.

## SSA Stochastic Projections

The Social Security Administration is the most prominent user of Monte Carlo in government fiscal analysis:
- First appeared in 2003 Trustees Report
- 5,000 independent Monte Carlo simulations
- Varies demographic, economic, and programmatic parameters
- Produces probability distributions over 75-year horizon
- Documented in Actuarial Study No. 117 (September 2004)

## Why This Matters for the Book

Chapter 11 argues this is a major gap. The absence of uncertainty quantification:

1. **Creates false precision**: Point estimates suggest more confidence than warranted
2. **Hides disagreement sources**: When TPC says $47B and CBO says $50B, is the difference meaningful? Without CIs, we can't tell.
3. **Misguides policymakers**: A $50B estimate with a $10B CI means something different from $50B with a $40B CI
4. **Is technically solvable**: The methods exist (bootstrap, Monte Carlo). The barrier is institutional, not technical.

## Sources

- McClelland et al. (2020), IJM 13(2)
- Pudney and Sutherland (1994), JPubEc 53(3)
- Goedeme et al. (2013), IJM 6(3)
- National Research Council (1991)
- CBO (2004), "The Uncertainty of Budget Projections"
- SSA (2003), Trustees Report + Actuarial Study No. 117

## Links

- [[simulation-accuracy]]
- [[squigglepy]]
- [[policyengine]]

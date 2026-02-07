---
chapters: [11]
primary_chapter: 11
narrative_role: "Python library for probabilistic estimation; represents the uncertainty quantification toolchain"
---

# Squigglepy

**Creator**: Peter Wildeford, Co-CEO of Rethink Priorities
**First release**: September 2022
**Announced**: October 2022, EA Forum
**License**: MIT
**GitHub**: github.com/rethinkpriorities/squigglepy (80 stars, 11 forks)
**PyPI**: v0.29 (April 2025), alpha status

## What It Does

Python library for probabilistic estimation — building models with uncertainty. Distinct from Squiggle (QURI's JavaScript language for the same purpose). Built because Rethink Priorities wanted Squiggle-like functionality in the Python ecosystem.

## Key Features

- **Distributions**: Normal, lognormal, t, triangular, PERT, binomial, beta, Bernoulli, Poisson, chi-square, gamma, Pareto, exponential, geometric, discrete, mixtures
- **Bayesian inference**: Simple Bayes, Bayesian networks (rejection sampling)
- **Forecasting utilities**: Forecast pooling, Laplace's rule, Kelly betting
- **Arithmetic on distributions**: Add, multiply, clip, correlate distributions

## Notable Usage

Rethink Priorities' **Cross-Cause Cost-Effectiveness Model (CCM)** uses Squigglepy extensively — a tool for comparing interventions across global health, animal welfare, and existential risk domains.

## Why It Matters for the Book

Chapter 11 (The Uncertainty Gap) argues that microsimulation lacks uncertainty quantification. Squigglepy represents the kind of tooling that could address this:

1. **The gap**: CBO doesn't publish confidence intervals on individual cost estimates. Neither does JCT, TPC, or PolicyEngine. Every estimate is a point estimate.
2. **The tool**: Squigglepy wraps Monte Carlo simulation in a clean API. You express uncertainty as distributions, not point values.
3. **The connection**: If microsimulation parameters (elasticities, take-up rates, income distributions) were expressed as distributions rather than point estimates, the same calculation engine could produce confidence intervals.

## The Broader Uncertainty Ecosystem

Squigglepy sits in a family of tools:
- **Squiggle** (QURI): JavaScript language for probabilistic modeling
- **Metaculus/Manifold**: Prediction platforms that aggregate uncertainty
- **GJOpen/Superforecasters**: Tetlock's forecasting infrastructure
- **Stan/PyMC**: Bayesian modeling languages (heavier-weight)

The EA community has invested heavily in making uncertainty quantification accessible to non-statisticians. Microsimulation has not.

## Sources

- [GitHub](https://github.com/rethinkpriorities/squigglepy)
- [EA Forum announcement](https://forum.effectivealtruism.org/posts/nj9FLkifyb3s6Eijx/announcing-squigglepy-a-python-package-for-squiggle)
- [PyPI](https://pypi.org/project/squigglepy/)

## Links

- [[simulation-accuracy]]
- [[policyengine]]

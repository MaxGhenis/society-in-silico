# TAXSIM

**Institution**: National Bureau of Economic Research (NBER)
**Maintainer**: Daniel Feenberg
**Language**: ~20,000 lines of FORTRAN 77

## What It Is

TAXSIM calculates federal and state income tax liabilities from individual data. Users provide household data; TAXSIM returns tax calculations.

## Coverage

- **Federal law**: 1960-2023
- **State laws**: 1977-2018
- Includes TCJA provisions and temporary CARES Act provisions (2020-2021)

## Access

Available via:
- Stata
- SAS
- R
- Python
- Web interface (Internet TAXSIM v35)

## Key Documentation

Feenberg, Daniel and Elisabeth Coutts. "An Introduction to the TAXSIM Model." *Journal of Policy Analysis and Management* Vol. 12 no. 1 (Winter, 1993).

## Daniel Feenberg

- Research Associate and IT Director at NBER
- Based in Cambridge, MA
- Over 4,618 citations
- Primary expertise: income taxation
- Contact: feenberg@nber.org

## Government Usage

Used by:
- Bureau of Labor Statistics (Consumer Expenditure Survey preparation)
- Census Bureau (evaluated alongside other tax calculators)
- Academic researchers

## Research Applications

Example finding: Using TAXSIM 1962-95, researchers estimated federal taxes offset ~8% of initial GDP shocks, acting as an automatic stabilizer.

## Comparison to Other Models

| Model | Institution | Access | Scope |
|-------|-------------|--------|-------|
| TAXSIM | NBER | Open (via API) | US federal + state |
| TAXBEN | IFS | Proprietary | UK |
| PolicyEngine | PolicyEngine | Open source | US + UK |

TAXSIM is more open than TAXBEN (free API access) but less open than PolicyEngine (code not available for inspection/modification).

## Book Narrative Notes

TAXSIM represents a middle ground: institutionally maintained, freely accessible, but not fully open source. It's been the standard for US tax research for decades.

The FORTRAN 77 codebase is a reminder of how long these models have been around—and the technical debt that accumulates in policy infrastructure.

## Sources

- [NBER TAXSIM](https://www.nber.org/research/data/taxsim)
- [Feenberg profile](https://www.nber.org/people/daniel_feenberg)
- [Introduction paper PDF](https://taxsim.nber.org/feenberg-coutts.pdf)

## Links

- [[microsimulation-definition]]
- [[ifs-taxben]]
- [[policyengine]]

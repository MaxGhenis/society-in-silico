# PolicyEngine

**Founded**: 2021
**Type**: Tech nonprofit
**Mission**: Compute the impact of public policy for the world

## What It Does

Free, open-source software that:
1. Models tax and benefit systems (US, UK, Canada in progress)
2. Lets users design custom reforms
3. Shows impacts on:
   - Government budget
   - Poverty and inequality
   - Individual households (net income, marginal tax rates)

## Origin Story

Created at the [[ubi-center]] when [[max-ghenis]] and [[nikhil-woodruff]] wanted to analyze UBI policies across both US and UK. No open-source UK model existed, so they built one.

> "UBI is a simple policy, but its high cost generally requires reforms to the rest of the tax and benefit system."

This meant they needed tools to jointly analyze taxes and benefits—something no existing product supported well.

## Technical Stack

- **policyengine-core**: Fork of [[openfisca]]-Core
- **policyengine-us**: US tax-benefit microsimulation model
- **policyengine-uk**: UK tax-benefit microsimulation model
- **policyengine-canada**: In early development
- Built on representative survey microdata (CPS, FRS, etc.)

## Recognition

- Recognized as a **Digital Public Good** by the Digital Public Goods Alliance
- FFWD tech nonprofit portfolio
- Policy Simulation Library member

## Key Differentiators

1. **Open source**: Unlike IFS TAXBEN, anyone can inspect, use, contribute
2. **Web interface**: Accessible to non-programmers
3. **Household + society views**: See both personal and aggregate impacts
4. **API access**: For researchers and developers

## Book Narrative Notes

PolicyEngine represents the "democratization" thesis: tools once available only to government agencies and elite think tanks are now available to anyone. This shifts power in policy debates.

The nonprofit structure is deliberate—neutrality matters for policy analysis.

## Sources

- [GitHub](https://github.com/PolicyEngine)
- [PolicyEngine.org](https://policyengine.org)
- [Introducing PolicyEngine UK](https://www.ubicenter.org/introducing-policyengine)
- [Crunchbase](https://www.crunchbase.com/organization/policyengine)

## Links

- [[max-ghenis]]
- [[nikhil-woodruff]]
- [[openfisca]]
- [[microsimulation-definition]]

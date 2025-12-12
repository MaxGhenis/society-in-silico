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

## Future State (Post-Cosilico Launch)

PolicyEngine will transition from maintaining its own microsimulation models to becoming a **policy analysis organization built on Cosilico infrastructure**.

### The Shift

| Before | After |
|--------|-------|
| Maintains policyengine-us, policyengine-uk | Uses Cosilico as the rule engine |
| Develops microsimulation infrastructure | Develops analysis tools atop Cosilico |
| Software org that does policy | Policy org that uses software |

### The New Identity

**"Between a think tank and a dev shop"**

- More quantitative than traditional think tanks
- More neutral than advocacy organizations
- Builds tools, not just reports
- Leverages Cosilico for the heavy lifting

### What PolicyEngine Becomes

1. **Policy analysis shop** - Research and reports using Cosilico
2. **Tool builder** - Applications atop Cosilico (calculators, dashboards)
3. **Accessibility layer** - Making Cosilico usable for non-technical audiences
4. **Neutral arbiter** - Quantitative analysis without ideological agenda

### Strategic Rationale

- **Cosilico** handles rule encoding, validation, AI integration
- **PolicyEngine** handles policy questions, user experience, communication
- Separation of concerns: infrastructure vs. application
- PolicyEngine can focus on impact rather than maintenance

## Book Narrative Notes

PolicyEngine represents the "democratization" thesis: tools once available only to government agencies and elite think tanks are now available to anyone. This shifts power in policy debates.

The nonprofit structure is deliberate—neutrality matters for policy analysis.

**The evolution** (for Part III): From "build the models" to "build on the models." PolicyEngine's transition to using Cosilico demonstrates the maturation of open policy infrastructure—from proof-of-concept to platform.

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

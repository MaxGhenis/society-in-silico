# Rules as Code

**Also known as**: Legislation as Code, RaC

## Definition

Rules as Code (RaC) is the process of encoding legislation, regulations, and policies as machine-readable code. The encoded version exists alongside—not replacing—the natural language version.

## Core Principles

1. **Dual representation**: Every rule exists in both human and machine form
2. **Tight coupling**: Human and machine versions stay synchronized
3. **Parallel development**: Not translation after the fact, but co-creation

> "With RaC, a machine-consumable rule isn't a translation of a rule by separate people at a different point in time but is developed in parallel and at the same time."

## Why It Matters

### For Government
- Reduces ambiguity in legislation
- Identifies gaps and inconsistencies before passage
- Enables digital service delivery

### For Citizens
- Easier compliance (clear rules)
- Automated eligibility checking
- Greater transparency

### For Policy Analysis
- Enables [[microsimulation-definition]]
- Allows "what if" scenario testing
- Facilitates comparison across jurisdictions

## Global Adoption

### New Zealand
- Better Rules initiative began early 2018
- Collaboration: Inland Revenue, MBIE, Parliamentary Counsel Office
- First production service: Rates Rebate app

### France
- [[openfisca]] is flagship implementation
- Government-created, now international

### Australia
- GovCMS platform integrating RaC
- Trials offered 2024-2025

### Other Jurisdictions
- Tunisia
- Spain
- Barcelona
- Senegal

## AI and Rules as Code

Recent experiments (Digital Benefits Network, Beeck Center):
- LLMs can help translate policy to code
- Works better with detailed prompts and simple policy logic
- Expert knowledge retrieval improves accuracy

Key finding:
> "LLMs can extract programmable rules from policy by leveraging expert knowledge retrieved from policy documents and employing well-crafted templates."

## The Vision

> "A rules as code approach to rules and regulations could help close the gap between policy and service delivery for governments, delivery organizations, and—most importantly—people seeking services."

## Challenges

1. Legal validity: Is code authoritative?
2. Complexity: Some rules resist formalization
3. Maintenance: Keeping code current with amendments
4. Expertise: Requires both legal and technical knowledge

## Relationship to Cosilico

Cosilico's approach pushes RaC further: not just encoding rules, but parameterizing them such that the code itself becomes a source of truth that can be validated against multiple authoritative sources.

## Book Narrative Notes

Rules as Code is the intellectual foundation for modern policy simulation. It's the answer to "how can a computer understand tax law?"

The movement is global but fragmented—each country reinventing the wheel. OpenFisca showed this doesn't need to happen.

## Sources

- [Digital Government Hub](https://digitalgovernmenthub.org/topics/digitizing-policy-rules-as-code/)
- [McKinsey report](https://www.mckinsey.com/industries/public-sector/our-insights/unlocking-the-potential-of-public-service-digitization)
- [GovInsider explainer](https://govinsider.asia/intl-en/article/four-things-you-should-know-about-rules-as-code)
- [AI experiments summary](https://digitalgovernmenthub.org/publications/ai-powered-rules-as-code-experiments-with-public-benefits-policy-summary/)

## Links

- [[openfisca]]
- [[policyengine]]
- [[microsimulation-definition]]

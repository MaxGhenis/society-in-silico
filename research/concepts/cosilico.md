# Cosilico

**Tagline**: "Infrastructure for Simulating Society"
**Founded**: 2024
**Founder**: [[max-ghenis]]
**Type**: Open-core startup

## The Core Thesis

> "Large language models cannot reliably calculate taxes and benefits."

From the research prospectus (December 2024):

**The evidence:**
- GPT-4 achieves only **67% accuracy** on true/false tax questions (Chen et al. 2023, SARA benchmark)
- Only 78% of scenario-based calculations within 10% of correct liability
- Models confuse marginal/effective rates, misapply filing status, hallucinate phase-outs

> "Today's LLMs cannot 'do taxes' on their own because tax calculations require 100% correctness. Today's models hallucinate."
> — Column Tax engineering blog, 2024

**Why this can't be trained away:**
- Tax law changes annually
- 50+ state jurisdictions with different rules
- Benefit eligibility depends on dozens of interacting variables
- No amount of pretraining produces reliability

## The Solution: Deterministic + Auditable Code

Three integrated capabilities:

```
┌─────────────────────────────────────────────────────┐
│                 COSILICO PLATFORM                    │
├─────────────────┬─────────────────┬─────────────────┤
│     RULES       │      DATA       │   SCENARIOS     │
│                 │                 │                 │
│ Deterministic   │ Synthetic       │ Population-     │
│ tax & benefit   │ populations     │ scale policy    │
│ calculations    │ calibrated to   │ simulation      │
│                 │ reality         │                 │
├─────────────────┴─────────────────┴─────────────────┤
│                OPEN SOURCE CORE                      │
│            (Apache 2.0 / MIT licensed)               │
└─────────────────────────────────────────────────────┘
```

### Key Properties

1. **Deterministic**: Same inputs → same outputs (always)
2. **Auditable**: Every calculation includes legal citation and parameter values
3. **Versioned**: Git history tracks all rule changes
4. **Bi-temporal**: Parameters track both effective date and knowledge date

## Code Example (from thesis)

```python
def eitc(
    earned_income: float,
    filing_status: FilingStatus,
    qualifying_children: int,
    tax_year: int
) -> CalculationResult:
    """
    Calculate federal EITC.

    Citation: 26 USC § 32
    Parameters effective: 2024-01-01
    """
    params = get_parameters("eitc", tax_year)
    # ... calculation logic ...

    return CalculationResult(
        value=credit,
        citation="26 USC § 32",
        parameters_used=params,
        calculation_trace=trace
    )
```

## Market Context

The gap in infrastructure:

| Capability | Provider | Limitation |
|------------|----------|------------|
| Sales tax | Avalara ($8.4B) | Sales tax only |
| Payroll tax | Symmetry, ADP | Payroll only |
| Benefits screening | Benefit Kitchen | 7 states, no taxes |
| Tax filing | TurboTax, Column | No API |
| Policy simulation | Academic models | Not production-ready |

**The opportunity**: No one provides income tax + benefits + prediction + simulation in a single production API.

## Why Now

Four converging trends (December 2024):

1. **AI tool use is standard** - Function calling shipped in GPT-4, Claude 3. Every AI assistant needs reliable tools.

2. **AI financial regulation coming** - SEC, CFPB examining AI in financial services. Audit trails will be required.

3. **Fintech infrastructure consolidation** - Avalara ($8.4B), Credit Karma ($8.1B). Acquirers pay premium.

4. **Open source AI stack maturing** - Open infrastructure is the new standard.

## Business Model (Open Core)

| Tier | Pricing | What You Get |
|------|---------|--------------|
| Self-hosted | Free | Run engine yourself |
| API (usage) | $0.001-0.01/call | Hosted, managed, fast |
| Data enrichment | $0.10-1.00/record | 200+ attributes per household |
| Enterprise | $100K-1M+/year | SLA, support, custom jurisdictions |
| Simulation | $50K-500K/project | Population-scale analysis |

## The Vision

> "Society is hard to optimize because nobody has a shared model to reason against. Congress debates with napkin math. Banks model risk without knowing policy changes. AI agents hallucinate eligibility rules.
>
> Cosilico is the shared substrate—a simulation everyone can query, so decisions are grounded in the same reality.
>
> We're building it in the open, because understanding society requires transparency."

## Connection to PolicyEngine

Cosilico builds on [[policyengine]] foundation:
- PolicyEngine proved the rules can be encoded at scale
- 1M+ simulations run, UK Treasury and US Congress usage
- 50+ open source contributors
- Coverage: US federal + 50 states, UK, Canada

Cosilico is the commercial infrastructure layer.

## Book Narrative Notes

Cosilico represents the thesis of the book in action:
1. **AI needs tools**: LLMs can't do tax math reliably
2. **Determinism matters**: Some things must be exactly right
3. **Open source as strategy**: Transparency builds trust
4. **Society as computable**: The vision of shared models

The GPT-4 accuracy numbers (67%) make the problem concrete and non-obvious. Most people assume AI can do math.

The "shared substrate" framing connects to the book's broader theme about democratic infrastructure.

## Key References

- Chen et al. (2023). "SARA: A Simple AI-Resilient Assessor for Tax Calculation." arXiv:2309.09992
- Column Tax (2024). "Will AI Agents Help File Your Taxes?"

## Sources

- Cosilico thesis: `/Users/maxghenis/CosilicoAI/cosilico.ai/docs/THESIS.md`

## Links

- [[policyengine]]
- [[max-ghenis]]
- [[rules-as-code]]
- [[microsimulation-definition]]

## Tags

#concept #current #ai #startup

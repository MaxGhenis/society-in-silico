---
exports:
  - format: pdf
    template: plain_latex_book
    output: exports/society-in-silico.pdf
    toc: true
    articles:
      - file: 00-thesis.md
      - file: 00-preface.md
      - file: 01-introduction.md
      - file: ../part-1-origins/01-birth-of-microsimulation.md
      - file: ../part-1-origins/02-tax-model-wars.md
      - file: ../part-1-origins/03-open-source-revolution.md
      - file: ../part-1-origins/04-the-accuracy-question.md
      - file: ../part-2-building/04-policyengine-proof-of-concept.md
      - file: ../part-2-building/05-the-household-view.md
      - file: ../part-2-building/06-the-society-view.md
      - file: ../part-2-building/07-ai-enters-the-picture.md
      - file: ../part-2-building/08-cosilico-infrastructure-for-the-future.md
      - file: ../part-3-future/10-the-uncertainty-gap.md
      - file: ../part-3-future/11-simulating-opinion.md
      - file: ../part-3-future/12-simulating-democracy.md
      - file: ../part-3-future/13-simulating-values.md
      - file: ../part-3-future/14-society-in-silico.md
---

# The Thesis

## The Question

Can simulation help society realize its goals?

Not: "Can we build a perfect model of society?"
Not: "Have we solved policy analysis?"
Not: "Is AI the answer?"

But: Can computational models of social systems—taxes, benefits, elections, values—help humanity reason more clearly about what it wants and how to get there?

## The Aspiration

This book is inherently aspirational. We will never have a perfect model of society in silico. The systems are too complex, the values too contested, the future too uncertain.

But we can have:
- **More accessible models** — Tools once hoarded by governments, available to anyone
- **More transparent models** — Open source, auditable, citable
- **More honest models** — Uncertainty quantified, not hidden
- **More useful models** — Infrastructure that AI and humans can reason against

## The Arc

**Part I: History**
Microsimulation began as an aspiration. Guy Orcutt in 1957 imagined simulating the economy household by household. He didn't have the compute. The vision preceded the capability by decades.

**Part II: Building**
PolicyEngine, Cosilico, and related projects are proof that open simulation infrastructure is possible. Not complete—possible. They demonstrate that the tools of policy analysis can be democratized, that AI can call deterministic backends, that rules can be encoded with validation.

**Part III: Future**
The deepest question: Can we simulate not just how policies affect people, but how values evolve? Can we ground AI alignment in empirical forecasts of what an informed, reflective humanity would want? This is aspirational by definition—but it's aspirational in a direction we can work toward.

## The Claim

Society in silico is not a destination. It's a method.

The claim isn't "we've modeled society." The claim is:
1. Simulation helps us reason about complex systems
2. Open simulation shifts power toward citizens
3. Uncertainty quantification makes us honest about what we don't know
4. AI will use these tools—so we should build them well
5. The ultimate question—what do we want?—might itself be approachable through simulation

## Why This Matters

If society can't reason about itself, it can't govern itself.

The alternative to simulation isn't "human judgment uncorrupted by models." It's:
- Black-box decisions by agencies with proprietary tools
- Vibes-based policy debate
- AI systems aligned to current values without understanding how values evolve
- Power concentrated in those with access to compute and data

Open simulation is infrastructure for collective reasoning. It won't be perfect. But it can be *better than the alternative*.

## The Honest Caveat

This book is written while the work is ongoing. Cosilico isn't launched. PolicyEngine doesn't have full uncertainty quantification. The value forecasting thesis is untested.

The book sets a vision—then invites the reader to watch (and participate in) the attempt to realize it.

That's not a bug. That's the nature of aspiration.

# Chapter 8: Cosilico - Infrastructure for the Future

GPT-4 gets tax questions wrong 33% of the time.

This is not an urban legend or an exaggerated claim. Chen et al. (2023) developed SARA—a benchmark for evaluating large language models on US income tax calculations—and found that GPT-4 answered only 67% of true/false tax questions correctly. On scenario-based calculations, only 78% of results were within 10% of the correct liability {cite}`chen2023sara`.

The models confused marginal and effective rates. They misapplied filing status rules. They hallucinated phase-out thresholds that didn't exist.

> "Today's LLMs cannot 'do taxes' on their own because tax calculations require 100% correctness. Today's models hallucinate."

This finding, from Column Tax's engineering blog in 2024, captures a fundamental problem: AI systems will increasingly mediate financial decisions, but they cannot reliably calculate the regulatory details that govern those decisions {cite}`columntax2024`.

PolicyEngine had demonstrated that deterministic tax-benefit calculations could be encoded as open-source code. The question was whether that approach could become infrastructure—not just for policy analysis, but for every fintech application, government agency, and AI assistant that needed accurate calculations.

That question led to Cosilico.

---

## The Infrastructure Gap

Look at the landscape of tax and financial infrastructure in 2024:

**Sales tax** has Avalara—a company acquired for $8.4 billion in 2022. They provide APIs that calculate sales tax obligations for e-commerce transactions. But sales tax only.

**Payroll tax** has Symmetry, ADP, and others. They calculate employer and employee tax obligations. But payroll only.

**Benefits screening** has Benefit Kitchen and similar services. They estimate program eligibility. But coverage is limited—a handful of states, no tax integration.

**Tax filing** has TurboTax and emerging players like Column Tax. They help individuals file returns. But they're consumer-facing, not API-first infrastructure.

**Policy simulation** has academic models like PolicyEngine, EUROMOD, Tax-Calculator. They're rigorous but not production-ready for commercial applications.

No one provides the full stack: income tax + benefits eligibility + attribute prediction + population simulation in a single, production-ready API.

This gap matters because every application that involves money eventually runs into tax and benefit calculations. A lending app needs to estimate after-tax income. A benefits platform needs to determine eligibility across programs. A financial planning tool needs to project tax liability under different scenarios. An AI assistant asked about finances needs to call *something* to get accurate numbers.

Without unified infrastructure, each company builds fragmented, partial solutions—or gives wrong answers.

---

## Why This Can't Be Trained Away

A natural response to the AI accuracy problem is: "Just train better models."

This won't work for tax and benefit calculations, for structural reasons:

**Tax law changes annually.** Every January brings new brackets, new thresholds, new credits. Training data from last year encodes rules that no longer apply. Models can't extrapolate to provisions they've never seen.

**Fifty states have different rules.** Each state has its own income tax (or no income tax), its own credits, its own benefit programs. The combinatorial explosion of jurisdiction-specific rules exceeds what pretraining can memorize reliably.

**Eligibility depends on dozens of variables.** SNAP eligibility involves income, household size, expenses, categorical eligibility, state supplements. One wrong variable produces wrong results. LLMs compress this complexity into statistical patterns that don't preserve exact logic.

**Calculations must be 100% correct.** A model that's 95% accurate sounds impressive until you realize that 1 in 20 tax returns would be wrong. Real-world tolerance for error in financial calculations is effectively zero.

The Column Tax engineers put it bluntly: "Today's LLMs cannot 'do taxes' on their own because tax calculations require 100% correctness" {cite}`columntax2024`.

The solution isn't better training. It's tools.

---

## Deterministic + Auditable

Cosilico's thesis is that AI systems need deterministic, auditable tools for calculations—and that building those tools as open-source infrastructure creates value for everyone.

The architecture has three components:

**Rules Engine**: Every tax and benefit formula encoded as deterministic code, traceable to statute. The EITC calculation cites 26 USC § 32. The SNAP calculation cites 7 USC § 2014. Each computation includes a citation and the parameter values used.

**Synthetic Populations**: For aggregate analysis, you need representative data. Cosilico constructs synthetic populations by calibrating public microdata to known totals, imputing missing variables, and validating against administrative aggregates. The result is a privacy-preserving dataset of ~100 million synthetic households that produces correct aggregate tax revenue when run through the rules engine.

**Scenario Simulation**: With rules and population, you can answer counterfactual questions. What if the EITC expanded by 50%? Run the baseline, run the reform, take the difference. Cost: $147 billion over ten years. Households affected: 43 million. Poverty reduction: 2.1 percentage points.

The key properties:

- **Deterministic**: Same inputs → same outputs, always
- **Auditable**: Every calculation includes legal citation and parameter values
- **Versioned**: Git history tracks all rule changes
- **Bi-temporal**: Parameters track both effective date and knowledge date

When an AI agent calls Cosilico to answer a tax question, the calculation is provably correct, legally citable, and traceable. The AI explains; the infrastructure calculates.

---

## Building on PolicyEngine

Cosilico doesn't start from scratch. It builds on the foundation PolicyEngine established.

PolicyEngine proved the core thesis: tax and benefit rules *can* be encoded accurately at scale. Over a million simulations have run on the platform. The UK Treasury has used the UK model for policy costing. US Congressional offices have used the analysis. The codebase covers US federal plus 50 states, the UK, and Canada—with 50+ open-source contributors maintaining and extending it {cite}`policyengine2024about`.

This is the starting point. But PolicyEngine was designed as a policy analysis tool—a nonprofit providing free research infrastructure. Cosilico is designed as commercial infrastructure—an open-core business providing production APIs.

The relationship is complementary:

- **PolicyEngine** continues as a nonprofit doing policy research and public-facing tools
- **Cosilico** builds on the same rule-encoding approach but serves commercial customers
- The open-source core is shared; the commercial layers are separate

This structure mirrors patterns in other successful open-source infrastructure: Linux and Red Hat, Kubernetes and cloud providers, PostgreSQL and managed database services.

---

## The Open-Core Model

Cosilico is structured as open-core: the simulation engine is open source (Apache 2.0 licensed), while hosted services and enterprise features are commercial.

The tiers:

| Tier | Pricing | What You Get |
|------|---------|--------------|
| **Self-hosted** | Free | Run the engine yourself |
| **API (usage)** | $0.001-0.01/call | Hosted, managed, fast |
| **Data enrichment** | $0.10-1.00/record | Predict 200+ attributes per household |
| **Enterprise** | $100K-1M+/year | SLA, support, custom jurisdictions |
| **Simulation** | $50K-500K/project | Population-scale policy analysis |

The open-source foundation serves multiple purposes:

**Trust through transparency.** When a fintech company integrates tax calculations into their product, they can inspect exactly how those calculations work. No black boxes.

**Community contributions.** Tax law is vast and constantly changing. Open source enables distributed maintenance—state-level experts can contribute state-specific rules.

**Regulatory readiness.** As AI regulation increases, audit trails matter. Calculations based on open-source, citable code are inherently more defensible than LLM outputs.

**Competitive moat.** Paradoxically, open-sourcing the core makes it harder for competitors to catch up. The comprehensive rule coverage becomes a network effect—each additional program encoded increases the value of the whole.

---

## The Market Opportunity

The infrastructure layer Cosilico builds sits beneath multiple large markets:

Tax software: $90 billion in 2024, growing 11% annually. Benefits administration: $2.5 billion, growing 10% annually. AI infrastructure: $46 billion, growing 29% annually. Data enrichment: $2.4 billion, growing 10% annually {cite}`cosilico2024thesis`.

Comparable outcomes validate the opportunity. Avalara was acquired for $8.4 billion providing sales tax APIs alone. Plaid reached a $6.1 billion valuation providing financial data APIs. Gusto reached $9.3 billion building payroll and benefits platforms that need exactly the eligibility calculations Cosilico provides.

The timing is right:

**AI tool use is standard.** Function calling shipped in GPT-4 and Claude 3. Anthropic's Model Context Protocol is being adopted by Microsoft. Every AI assistant needs reliable tools to call.

**AI financial regulation is coming.** The SEC, CFPB, and state regulators are examining AI in financial services. Audit trails and explainability will be required. Citation-based approaches are regulation-ready.

**Fintech infrastructure is consolidating.** Large players are acquiring core infrastructure. Acquirers pay premiums for financial data capabilities.

---

## The Shared Substrate Vision

The deepest rationale for Cosilico connects to the book's larger thesis:

> "Society is hard to optimize because nobody has a shared model to reason against. Congress debates with napkin math. Banks model risk without knowing policy changes. AI agents hallucinate eligibility rules.
>
> Cosilico is the shared substrate—a simulation everyone can query, so decisions are grounded in the same reality."

When policymakers consider reforming the EITC, they should be able to query the same simulation that banks use to assess lending risk, that fintech apps use to estimate tax liability, that AI assistants use to answer questions. The calculations should be the same because the underlying reality is the same.

Today, fragmentation creates divergent answers. Official government estimates use proprietary models. Think tanks use different models. Companies build ad-hoc solutions. Individuals get inconsistent information. The policy debate suffers because participants aren't reasoning against the same facts.

Shared infrastructure could change this. A canonical, open-source, production-quality simulation that anyone can query—and anyone can verify—creates common ground. Disagreements can focus on values and priorities rather than on whose numbers are right.

This is infrastructure for democratic deliberation: transparent, accessible, shared.

---

## From PolicyEngine to Cosilico

The transition represents an evolution in thinking about what policy simulation infrastructure should be.

PolicyEngine asked: "Can we make policy analysis accessible to everyone?" The answer was yes—through open-source models, web interfaces, and free public tools.

Cosilico asks: "Can accurate policy calculations become infrastructure that everything else builds on?" The answer requires commercial sustainability, production-quality engineering, and integration with the broader ecosystem of AI tools and financial applications.

PolicyEngine demonstrated the proof of concept. Cosilico is the attempt to scale it.

The nonprofit continues, focused on research and public goods. The company builds the commercial infrastructure layer. The open-source foundation supports both. And the vision—understanding policy through transparent, accurate simulation—remains the same.

---

## What Success Looks Like

If Cosilico succeeds, the results would be visible throughout the financial ecosystem:

**AI assistants** that give accurate answers to tax and benefit questions—not because they've been trained better, but because they call reliable tools.

**Fintech applications** that correctly calculate after-tax income, benefit eligibility, and financial impacts—without each company reinventing the calculations.

**Government agencies** that use the same validated calculations as the private sector—reducing discrepancies and improving trust.

**Policy debates** grounded in shared numbers—where disagreements are about values, not whose model is right.

**Individual citizens** who can understand how policies affect them—accessing the same calculations that Congress uses.

This is the vision of "society in silico" applied practically: simulation as infrastructure for understanding and improving the systems that govern our lives.

---

## The Work Ahead

Cosilico launched in 2024, still in early development. The rules engine is being built. The API is being designed. The commercial model is being tested with design partners.

Success is not guaranteed. Building production infrastructure is hard. Commercializing open source is tricky. The market for policy calculation APIs is unproven. Many startups with compelling theses fail for execution reasons.

But the thesis is clear: AI systems need deterministic tools, tax and benefit calculations are essential, and no one else is building the comprehensive solution. The foundation from PolicyEngine provides a starting point that would take competitors years to replicate. The open-source approach builds trust and community.

Whether Cosilico specifically succeeds, the need for this infrastructure is real. Someone will build it—because AI systems will increasingly need accurate tools for financial calculations, and hallucinating 33% of tax answers is unacceptable.

The question is whether it will be built openly, accessibly, as shared infrastructure for society—or whether it will be another proprietary black box controlled by whoever wins the race.

Cosilico is a bet on openness.

---

## References

```{bibliography}
:filter: docname in docnames
```

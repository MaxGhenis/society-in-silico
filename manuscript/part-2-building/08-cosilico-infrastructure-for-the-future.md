# Chapter 8: Infrastructure for the Future

*A note to the reader: This chapter differs from the rest of the book. Earlier chapters described working systems—PolicyEngine, TAXSIM, existing models with validated track records. This chapter describes infrastructure that doesn't yet exist. I include it not as a product review, but as a technical exploration of what would be needed for AI systems to reliably perform tax and benefit calculations. The problems described are real; the solutions are speculative.*

---

GPT-4 gets tax questions wrong 33% of the time.

This is not an urban legend or an exaggerated claim. Blair-Stanek et al. (2023) developed SARA (StAtutory Reasoning Assessment)—a benchmark for evaluating large language models on US income tax calculations—and found that GPT-4 answered only 67% of true/false tax questions correctly. On scenario-based calculations, GPT-4 got tax liabilities exactly right only about a third of the time {cite}`blairstanek2023gpt4tax`.

The models confused marginal and effective rates. They misapplied filing status rules. They hallucinated phase-out thresholds that didn't exist.

> "Today's LLMs cannot 'do taxes' on their own because tax calculations require 100% correctness. Today's models hallucinate."

This finding, from Column Tax's engineering blog in 2024, captures a fundamental problem: AI systems will increasingly mediate financial decisions, but they cannot reliably calculate the regulatory details that govern those decisions {cite}`columntax2024`.

PolicyEngine had demonstrated that deterministic tax-benefit calculations could be encoded as open-source code. The question was whether that approach could become infrastructure—not just for policy analysis, but for every fintech application, government agency, and AI assistant that needed accurate calculations.

That question led me to explore what such infrastructure would require.

---

## The Infrastructure Gap

Look at the landscape of tax and financial infrastructure in 2024:

**Sales tax** has Avalara—a company acquired for $8.4 billion in 2022 {cite}`avalara2022acquisition`. They provide APIs that calculate sales tax obligations for e-commerce transactions. But sales tax only.

**Payroll tax** has Symmetry, ADP, and others. They calculate employer and employee tax obligations. But payroll only.

**Benefits screening** has Benefit Kitchen and similar services. They estimate program eligibility. But coverage is limited—a handful of states, no tax integration.

**Tax filing** has TurboTax and emerging players like Column Tax. They help individuals file returns. But they're consumer-facing, not API-first infrastructure.

**Policy simulation** has academic models like PolicyEngine, EUROMOD, Tax-Calculator. They're rigorous but not designed as production-ready commercial infrastructure.

No one provides the full stack: income tax + benefits eligibility + attribute prediction + population simulation in a single, production-ready API. This gap is both a problem and an opportunity.

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

## What Would Be Needed: Deterministic + Auditable

The thesis is that AI systems need deterministic, auditable tools for calculations—and that building those tools as open-source infrastructure would create value for everyone.

Such infrastructure would require three components:

**Rules Engine**: Every tax and benefit formula encoded as deterministic code, traceable to statute. The EITC calculation cites 26 USC § 32. The SNAP calculation cites 7 USC § 2014. Each computation includes a citation and the parameter values used.

**Synthetic Populations**: For aggregate analysis, you need representative data. This would involve constructing synthetic populations by calibrating public microdata to known totals, imputing missing variables, and validating against administrative aggregates. The result would be a privacy-preserving dataset of synthetic households that produces correct aggregate tax revenue when run through the rules engine.

**Scenario Simulation**: With rules and population, you could answer counterfactual questions. What if the EITC expanded by 50%? Run the baseline, run the reform, take the difference. The output might show: cost estimates over ten years, households affected, poverty reduction in percentage points—all calculated from the underlying rules and population data.

The key properties such a system would need:

- **Deterministic**: Same inputs produce same outputs, always
- **Auditable**: Every calculation includes legal citation and parameter values
- **Versioned**: Git history tracks all rule changes
- **Bi-temporal**: Parameters track both effective date and knowledge date

When an AI agent would call such infrastructure to answer a tax question, the calculation would be provably correct, legally citable, and traceable. The AI explains; the infrastructure calculates.

---

## The Foundation Exists

Such infrastructure wouldn't start from scratch. PolicyEngine has demonstrated the core thesis: tax and benefit rules *can* be encoded accurately at scale. Over a million simulations have run on the platform. The UK Treasury has used the UK model for policy costing. US Congressional offices have used the analysis. The codebase covers US federal plus 50 states, the UK, and Canada—with 50+ open-source contributors maintaining and extending it {cite}`policyengine2024about`.

But PolicyEngine was designed as a policy analysis tool—a nonprofit providing free research infrastructure. The gap is commercial infrastructure: production APIs, enterprise support, service-level guarantees.

One potential path would be an open-core model, mirroring patterns in other successful open-source infrastructure: Linux and Red Hat, Kubernetes and cloud providers, PostgreSQL and managed database services. The simulation engine could remain open source while hosted services and enterprise features would be commercial.

Whether this specific approach is the right one remains uncertain. What's clear is that the foundation exists—accurate, open-source policy rules that could be packaged differently to serve different use cases.

---

## Why Open Source Would Matter

If policy calculation infrastructure were built as open-core—with the simulation engine open source and hosted services commercial—the open-source foundation would serve multiple purposes:

**Trust through transparency.** When a fintech company integrates tax calculations into their product, they can inspect exactly how those calculations work. No black boxes.

**Community contributions.** Tax law is vast and constantly changing. Open source enables distributed maintenance—state-level experts can contribute state-specific rules.

**Regulatory readiness.** As AI regulation increases, audit trails matter. Calculations based on open-source, citable code are inherently more defensible than LLM outputs.

**Competitive moat.** Paradoxically, open-sourcing the core makes it harder for competitors to catch up. The comprehensive rule coverage becomes a network effect—each additional program encoded increases the value of the whole.

---

## Why This Would Matter

The thesis is that accurate tax and benefit calculations could become essential infrastructure—not a niche academic tool but something every fintech app, government service, and AI assistant needs.

Several trends suggest this need is growing:

**AI tool use is becoming standard.** Function calling shipped in GPT-4 and Claude 3. Anthropic's Model Context Protocol is being adopted broadly. AI assistants need reliable tools to call—hallucinating tax calculations is unacceptable.

**AI financial regulation is coming.** The SEC, CFPB, and state regulators are examining AI in financial services. Audit trails and explainability will likely be required. Citation-based approaches are regulation-ready.

**The precedent exists.** Avalara built a large business ($8.4 billion acquisition) providing sales tax APIs alone. Someone will likely build the equivalent for income taxes and benefits. The question is whether it will be open or proprietary.

The underlying need—accurate calculations that AI can call—appears real. Whether the market is large enough to sustain commercial infrastructure remains unproven.

---

## The Shared Substrate Vision

The deepest rationale for such infrastructure connects to the book's larger thesis:

Society is hard to optimize because nobody has a shared model to reason against. Congress debates with napkin math. Banks model risk without knowing policy changes. AI agents hallucinate eligibility rules.

What's needed is a shared substrate—a simulation everyone can query, so decisions are grounded in the same reality.

When policymakers consider reforming the EITC, they should be able to query the same simulation that banks use to assess lending risk, that fintech apps use to estimate tax liability, that AI assistants use to answer questions. The calculations should be the same because the underlying reality is the same.

Today, fragmentation creates divergent answers. Official government estimates use proprietary models. Think tanks use different models. Companies build ad-hoc solutions. Individuals get inconsistent information. The policy debate suffers because participants aren't reasoning against the same facts.

Shared infrastructure could change this. A canonical, open-source, production-quality simulation that anyone can query—and anyone can verify—creates common ground. Disagreements can focus on values and priorities rather than on whose numbers are right.

This is infrastructure for democratic deliberation: transparent, accessible, shared.

---

## From Analysis to Infrastructure

This vision represents an evolution in thinking about what policy simulation infrastructure could be.

PolicyEngine asked: "Can we make policy analysis accessible to everyone?" The answer was yes—through open-source models, web interfaces, and free public tools.

The next question is: "Can accurate policy calculations become infrastructure that everything else builds on?" The answer would require commercial sustainability, production-quality engineering, and integration with the broader ecosystem of AI tools and financial applications.

PolicyEngine demonstrated the proof of concept. Scaling it to production infrastructure is the open challenge.

---

## What Success Would Look Like

If such infrastructure were built successfully, the results would be visible throughout the financial ecosystem:

**AI assistants** that give accurate answers to tax and benefit questions—not because they've been trained better, but because they call reliable tools.

**Fintech applications** that correctly calculate after-tax income, benefit eligibility, and financial impacts—without each company reinventing the calculations.

**Government agencies** that use the same validated calculations as the private sector—reducing discrepancies and improving trust.

**Policy debates** grounded in shared numbers—where disagreements are about values, not whose model is right.

**Individual citizens** who can understand how policies affect them—accessing the same calculations that Congress uses.

This is the vision of "society in silico" applied practically: simulation as infrastructure for understanding and improving the systems that govern our lives.

---

## The Work Ahead

As I write this in late 2024, I'm exploring whether to build this infrastructure through a venture called Cosilico. The company is incorporated. Early design work has begun. But there's no production API, no paying customers, no proof that the market exists.

I include this chapter not because such infrastructure has been built, but because the problem is real regardless of whether this particular attempt succeeds. AI systems need deterministic tools for financial calculations. Someone will likely build this infrastructure. The question is whether it will be open or proprietary.

If this specific venture fails—and most startups do—the thesis remains: open-source policy simulation infrastructure, production-ready and commercially sustainable, would be valuable. Someone should build it. Maybe I will. Maybe someone else will do it better. Maybe PolicyEngine itself will evolve to fill this role without a separate commercial layer.

The honest framing is aspiration, not accomplishment. PolicyEngine demonstrated that open policy simulation is possible and valuable. Whether it can be packaged as production infrastructure that AI systems and fintech companies rely on remains unproven.

What I can say with confidence: the gap exists. GPT-4 gets tax questions wrong a third of the time. Every fintech company that needs accurate calculations today builds fragmented, partial solutions. The need for shared infrastructure appears real, even if the path to building it remains uncertain.

This chapter describes a problem and a potential solution. Whether that solution materializes—and whether it's commercially viable—is unknown. You're reading this partly to understand what infrastructure would be needed for AI to reliably handle policy calculations, and why it matters whether that infrastructure is open or proprietary.

---

## References

```{bibliography}
:filter: docname in docnames
```

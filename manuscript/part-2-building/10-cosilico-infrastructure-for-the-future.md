# Chapter 10: Infrastructure for the future

*A note to the reader: This chapter differs from the rest of the book. Earlier chapters described working systems—PolicyEngine, TAXSIM, existing models with validated track records. This chapter describes infrastructure that doesn't yet exist. I include it not as a product review, but as a technical exploration of what would be needed for AI systems to reliably perform tax and benefit calculations. The problems described are real; the solutions are speculative.*

---

In March 2025, a fintech startup called April raised $38 million to build what they called "embedded tax infrastructure"—AI-powered tools that would let any financial platform offer tax filing to its users. Their pitch deck probably mentioned that 150 million Americans file taxes every year and most hate the experience. What it likely didn't mention is the engineering nightmare underneath.

April's tax engine needed to handle federal income tax plus the tax codes of every state that levies one. It needed to track annual changes to brackets, credits, phase-outs, and deductions. It needed to integrate with payroll data, brokerage statements, and government forms in dozens of formats. And it needed to be exactly right—not 95% right, not 99% right, but right to the penny, because the IRS doesn't grade on a curve.

April is one company solving one slice of this problem. Column Tax is another: they've filed over a million returns through their embedded API and recently introduced an AI agent called Iris to help maintain their tax engine year over year {cite}`columntax2024`. Both companies are well-funded, well-engineered, and focused almost entirely on filing federal and state income tax returns.

Neither handles benefits eligibility. Neither models the interaction between taxes and transfer programs. Neither can answer the question a lending app actually needs to answer: "What is this borrower's true after-tax, after-benefits disposable income?"

That question—the full-stack question—is where the infrastructure gap begins.

---

## The landscape of partial solutions

Look at the landscape of tax and financial infrastructure in 2025:

**Sales tax** has Avalara—a company acquired for $8.4 billion in 2022 {cite}`avalara2022acquisition`. They provide APIs that calculate sales tax obligations for e-commerce transactions. The global tax tech market is projected to reach $60 billion by 2034 {cite}`taxtech2025market`. But Avalara handles sales tax only.

**Payroll tax** has ADP, Gusto, and others. They calculate employer and employee tax obligations. But payroll only.

**Tax filing** has TurboTax, Column Tax, April, and emerging players. They help individuals file returns or let platforms embed filing. But they're consumer-facing, not infrastructure for economic calculation.

**Benefits screening** has services like Benefit Kitchen and Benefits.gov. They estimate program eligibility. But coverage is limited—a handful of programs, no tax integration, no household-level modeling.

**Policy simulation** has academic models like PolicyEngine, EUROMOD, and Tax-Calculator. They're rigorous and comprehensive but designed for research, not production API calls at enterprise scale.

No one provides the full stack: income tax + benefits eligibility + household attribute prediction + population simulation in a single, production-ready API. Each piece exists somewhere. The integration exists nowhere.

This gap matters because every application that involves money eventually runs into tax and benefit calculations. A lending app needs to estimate after-tax income. A benefits platform needs to determine eligibility across programs that interact with each other—SNAP benefits phase out as earned income rises, but the Earned Income Tax Credit phases in, and the net effect depends on household composition, state of residence, and a dozen other variables. A financial planning tool needs to project tax liability under different scenarios. An AI assistant asked "how much would I get from the Child Tax Credit?" needs to call *something* to get an accurate answer.

Without unified infrastructure, each company builds fragmented, partial solutions—or gives wrong answers.

---

## Why this can't be trained away

As the introduction described, GPT-4 answered only 67% of true/false tax questions correctly on the SARA benchmark {cite}`blairstanek2023gpt4tax`. Two years and several model generations later, the problem hasn't been solved. In July 2025, Column Tax released TaxCalcBench—a benchmark requiring models to compute complete federal tax returns rather than just answer questions. The best-performing model, Gemini 2.5 Pro, got fewer than one in three returns right {cite}`bock2025taxcalcbench`.

A natural response: "Just train better models." This won't work, for structural reasons:

**Tax law changes annually.** Every January brings new brackets, thresholds, and credits. Training data from last year encodes rules that no longer apply. Models can't extrapolate to provisions they've never seen.

**Fifty states have different rules.** Each state has its own income tax (or none), its own credits, its own benefit programs. The combinatorial explosion of jurisdiction-specific rules exceeds what pretraining can memorize reliably.

**Eligibility depends on dozens of interacting variables.** SNAP eligibility involves income, household size, expenses, categorical eligibility, and state supplements. One wrong variable produces wrong results. Language models compress this complexity into statistical patterns that don't preserve exact logic.

**Financial calculations require 100% correctness.** A model that's 95% accurate sounds impressive until you realize that 1 in 20 tax returns would be wrong. Column Tax's engineers put it directly: "Today's LLMs cannot 'do taxes' on their own because tax calculations require 100% correctness" {cite}`columntax2024`.

The solution isn't better training. It's tools—deterministic, auditable tools that AI systems can call.

---

## Meet Priya

Let me make this concrete with a composite character drawn from real patterns I've seen.

Priya runs engineering at a mid-stage fintech company that provides cash advances to gig workers. Her users—DoorDash drivers, Instacart shoppers, freelance designers—need to know their actual take-home income to make borrowing decisions. The app's underwriting model needs the same information to assess risk.

The problem: a gig worker earning $45,000 in a year might owe $4,200 in federal income tax, $1,800 in self-employment tax, $900 in state tax—and qualify for $2,100 in Earned Income Tax Credit, reducing their effective burden to $4,800. But the same worker with two kids might qualify for $3,600 in Child Tax Credit, dropping their net tax to $1,200. Add SNAP eligibility—which depends on net income after a complex set of deductions—and the picture shifts again.

Priya's team tried four approaches:

First, they used a tax estimation library from GitHub. It handled federal brackets but nothing else—no credits, no state taxes, no benefits. Their estimates were off by 30-40% for low-income users.

Second, they called a tax API provider. The provider handled filing-related calculations but couldn't estimate benefits, couldn't model year-over-year changes, and charged per-call fees that made population-level analysis prohibitive.

Third, they tried prompting GPT-4 with tax scenarios. The hallucination rate was unacceptable for a financial product.

Fourth, they considered building it themselves. Their senior engineer estimated six months of work to cover federal tax alone. State taxes would be another six months. Benefits would be another year. And then they'd need to maintain it as laws change.

Priya's company is real, even if Priya herself is composite. The pattern repeats across fintech: every company that touches consumer finance eventually hits the tax-and-benefits wall, and every one builds a partial, fragile solution.

---

## What the infrastructure would require

The thesis is that AI systems need deterministic, auditable tools for calculations—and that building those tools as shared infrastructure would create value for everyone.

Such infrastructure would require three components:

**A rules engine** where every tax and benefit formula is encoded as deterministic code, traceable to statute. The EITC calculation cites 26 USC § 32. The SNAP calculation cites 7 USC § 2014. Each computation includes a citation and the parameter values used. When the IRS updates the EITC maximum credit for 2026, the parameter file changes; the formula doesn't.

**Synthetic populations** for aggregate analysis. This means constructing representative datasets by calibrating public microdata—the Current Population Survey, the American Community Survey—to known administrative totals. The result: a privacy-preserving dataset of synthetic households that, when run through the rules engine, produces aggregate tax revenue matching IRS statistics and benefit enrollment matching agency reports.

**A scenario simulation layer** that answers counterfactual questions. What if the EITC expanded by 50%? Run the baseline, run the reform, take the difference. The output: cost estimates, households affected, poverty impact—all computed from the underlying rules and population data, all auditable.

The key properties:

- **Deterministic**: Same inputs, same outputs, always
- **Auditable**: Every calculation includes legal citation and parameter values
- **Versioned**: Git history tracks all rule changes
- **Bi-temporal**: Parameters track both effective date (when a law takes effect) and knowledge date (when we learned about it)

When an AI agent calls such infrastructure to answer a tax question, the calculation is provably correct, legally citable, and traceable. The AI explains; the infrastructure calculates.

---

## The foundation exists

This infrastructure wouldn't start from scratch.

PolicyEngine has demonstrated the core thesis: tax and benefit rules *can* be encoded accurately at scale. Over a million simulations have run on the platform. HM Treasury formally evaluated the UK model (Chapter 5). US Congressional offices have used the analysis for budget scoring. The codebase covers US federal plus all 50 states, the UK, and Canada—maintained by 50+ open-source contributors {cite}`policyengine2024about`.

But PolicyEngine was designed as a policy analysis tool—a nonprofit providing free research infrastructure. The gap is commercial infrastructure: production APIs with millisecond response times, enterprise support with service-level agreements, documentation aimed at developers rather than policy analysts.

One potential path: an open-core model mirroring patterns in other successful open-source infrastructure. Linux powers the cloud but Red Hat sells enterprise support. Kubernetes orchestrates containers but cloud providers sell managed services. PostgreSQL stores data but managed database services add monitoring, backups, and guarantees.

Under this model, the simulation engine—the rules, the parameters, the formulas—would remain open source. Anyone could inspect, verify, or extend the calculations. Commercial value would come from hosted services, enterprise features, and integration support.

---

## The open-core tension

An open-core approach to policy infrastructure raises legitimate concerns that deserve honest engagement.

**Governance risk.** If a commercial entity controls the roadmap of open-source policy rules, commercial incentives could distort priorities. A paying customer might want Australian tax rules before a nonprofit wants updated SNAP calculations. The maintainer could deprioritize accuracy fixes that don't affect revenue.

This tension exists in every open-core project, but it's more acute for policy infrastructure. When Red Hat prioritizes enterprise Linux features, the stakes are server uptime. When a policy infrastructure company prioritizes one country's tax code over another, the stakes include whether vulnerable populations get accurate benefits estimates.

**Capture risk.** A well-funded commercial player could dominate the open-source project, effectively making "open source" a brand rather than a genuine commons. Contributors might drift away if they feel their work primarily benefits shareholders.

**Sustainability risk.** Most startups fail. If the commercial layer fails, the open-source foundation might lose its most active maintainers. The codebase could stagnate, and downstream users—nonprofits, government agencies, researchers—would be left maintaining infrastructure designed for a commercial context that no longer exists.

These aren't hypothetical objections. They're structural features of the open-core model that any attempt to build this infrastructure would need to address through governance structures, contributor agreements, and institutional redundancy.

---

## Why open source would matter anyway

Despite the tensions, open-source foundations serve purposes that closed infrastructure cannot.

**Trust through transparency.** When a fintech company integrates tax calculations, they can inspect exactly how those calculations work. When a government agency uses the infrastructure, they can verify it matches statute. No black boxes.

**Distributed maintenance.** Tax law is vast and constantly changing. Open source enables state-level experts to contribute state-specific rules, benefits specialists to maintain eligibility logic, and international contributors to add jurisdictions. No single company can hire enough domain experts to cover every rule.

**Regulatory readiness.** As AI regulation increases, audit trails matter. Calculations based on open-source, citable code are inherently more defensible than LLM outputs. The EU AI Act, US state-level AI regulations, and financial regulators are all moving toward requiring explainability for automated financial decisions.

---

## The market question

Is this a real business or a nice idea?

The market signals are mixed but suggestive.

Avalara built a large business—$8.4 billion acquisition—providing sales tax APIs alone {cite}`avalara2022acquisition`. Column Tax has filed over a million returns through its embedded API. April raised $38 million. The global tax tech market is projected to grow from $21 billion in 2025 to over $60 billion by 2034 {cite}`taxtech2025market`.

But these companies focus on narrow slices: sales tax compliance, income tax filing, payroll calculation. The full-stack vision—income tax plus benefits plus population simulation—has no direct precedent as a commercial product. It's possible the market wants narrow, specialized tools rather than unified infrastructure. It's possible that the integration challenge is too complex for a single API. It's possible that the potential customers—fintechs, government agencies, AI companies—would rather build their own partial solutions than depend on shared infrastructure.

The honest answer: the need for accurate, comprehensive tax-and-benefit calculations appears real. Whether that need translates into a viable market for infrastructure-as-a-service is unproven.

---

## The shared substrate vision

The deepest rationale for such infrastructure connects to the book's larger thesis.

Society is hard to optimize because nobody has a shared model to reason against. Congress debates with napkin math. Banks model risk without knowing policy changes. AI agents hallucinate eligibility rules.

What's needed is a shared substrate—a simulation everyone can query, so decisions are grounded in the same reality.

When policymakers consider reforming the EITC, they should be able to query the same simulation that banks use to assess lending risk, that fintech apps use to estimate tax liability, that AI assistants use to answer questions. The calculations should be the same because the underlying law is the same.

Today, fragmentation creates divergent answers. Official government estimates use proprietary models. Think tanks use different models. Companies build ad-hoc solutions. Individuals get inconsistent information from AI chatbots that hallucinate confidently. The policy debate suffers because participants aren't reasoning against the same facts.

Shared infrastructure could change this. A canonical, open-source, production-quality simulation that anyone can query—and anyone can verify—creates common ground. Disagreements can focus on values and priorities rather than on whose numbers are right.

---

## The work ahead

As I write this, I'm exploring whether to build this infrastructure through two complementary organizations.

The first is the **Rules Foundation**, a 501(c)(3) nonprofit developing open-source standards for encoding law as code. The foundation maintains Atlas—an archive of statutes, regulations, and IRS guidance—and RAC (Rules as Code), a domain-specific language for encoding tax and benefit formulas in a format that's both human-readable and machine-executable. RAC encodes each calculation with legal citations, parameter values, and deterministic logic. The encoding for the Earned Income Tax Credit, for example, traces each step to 26 USC § 32, with parameter values that update annually as the IRS publishes new thresholds. The foundation also builds AutoRAC, tooling that uses AI to accelerate the encoding of statutes into RAC format. Jurisdiction-specific encodings—US federal, California, New York, Canada—are maintained as separate open-source repositories.

The second is **Cosilico**, a commercial venture that would build production APIs on top of the Rules Foundation's open-source encoding. Cosilico's layer adds microdata (representative household datasets for population simulation), synthetic data generation, and hosted API endpoints with the performance and reliability guarantees that production applications require.

This structure directly addresses the open-core governance tension described earlier. The rules themselves—the encoding of law—live in a nonprofit foundation with an independent governance structure. No commercial entity controls which statutes get encoded or how. The commercial layer provides infrastructure services on top of the open-source foundation, the same way managed database services build on PostgreSQL without controlling PostgreSQL's development.

Both organizations are early. The Rules Foundation has encoded portions of US federal tax law and several state codes. Cosilico has no production API, no paying customers, no proof that the market exists at scale.

I include this chapter not because the infrastructure has been built, but because the problem is real regardless of whether this particular attempt succeeds. AI systems need deterministic tools for financial calculations. Column Tax, April, and others are building pieces of the answer for tax filing. No one is building the full stack that connects taxes, benefits, and population simulation.

If these specific ventures fail—and most do—the thesis remains: open-source policy simulation infrastructure, production-ready and commercially sustainable, would be valuable. Someone should build it. Maybe I will. Maybe Column Tax will expand beyond filing. Maybe a government agency will fund it as public infrastructure. Maybe the open-source community around PolicyEngine and OpenFisca will evolve to fill the gap without any commercial layer at all.

The honest framing is aspiration, not accomplishment. PolicyEngine demonstrated that open policy simulation is possible and valuable. Whether it can become the production infrastructure that AI systems and financial applications rely on—fast enough, reliable enough, comprehensive enough, and commercially sustainable enough—remains the open question.

What I can say with confidence: the gap exists. GPT-4 gets tax questions wrong a third of the time. Every Priya at every fintech company that needs accurate calculations builds fragmented, partial solutions. The $60 billion tax tech market is growing fast but remains balkanized into narrow verticals. The need for shared infrastructure appears real, even if the path to building it remains uncertain.

---

## References

```{bibliography}
:filter: docname in docnames
```

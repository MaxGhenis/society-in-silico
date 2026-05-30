# Chapter 10: Infrastructure for the future

*A note to the reader: This chapter differs from the rest of the book. Earlier chapters described working systems—PolicyEngine, TAXSIM, existing models with validated track records. This chapter describes infrastructure that doesn't yet exist. I include it not as a product review, but as a technical exploration of what would be needed for AI systems to reliably perform tax and benefit calculations. The problems described are real; the solutions are speculative.*

---

In July 2025, a fintech startup called April raised $38 million to build what they called "embedded tax infrastructure"—AI-powered tools that would let any financial platform offer tax filing to its users. Their pitch deck probably mentioned that 150 million Americans file taxes every year and most hate the experience. What it likely didn't mention is the engineering nightmare underneath.

April's tax engine needed to handle federal income tax plus the tax codes of every state that levies one. It needed to track annual changes to brackets, credits, phase-outs, and deductions. It needed to integrate with payroll data, brokerage statements, and government forms in dozens of formats. And it needed to be exactly right—not 95% right, not 99% right, but right to the penny, because the IRS doesn't grade on a curve.

April is one company solving one slice of this problem. Column Tax is another: they've filed over a million returns through their embedded API and recently introduced an AI agent called Iris to help maintain their tax engine year over year [@columntax2024]. Both companies are well-funded, well-engineered, and focused almost entirely on filing federal and state income tax returns.

Neither handles benefits eligibility. Neither models the interaction between taxes and transfer programs. Neither can answer the question a lending app actually needs to answer: "What is this borrower's true after-tax, after-benefits disposable income?"

That question—the full-stack question—is where the infrastructure gap begins.

---

## The landscape of partial solutions

Look at the landscape of tax and financial infrastructure in 2025:

**Sales tax** has Avalara—a company acquired for $8.4 billion in 2022 [@avalara2022acquisition]. They provide APIs that calculate sales tax obligations for e-commerce transactions. The global tax tech market is projected to reach $60 billion by 2034 [@taxtech2025market]. But Avalara handles sales tax only.

**Payroll tax** has ADP, Gusto, and others. They calculate employer and employee tax obligations. But payroll only.

**Tax filing** has TurboTax, Column Tax, April, and emerging players. They help individuals file returns or let platforms embed filing. But they're consumer-facing, not infrastructure for economic calculation.

**Benefits screening** has services like Benefit Kitchen, MyFriendBen, and Benefits.gov. They solve a real need and in some cases offer APIs, white-labeled workflows, and multi-state screening. But they're optimized for present-tense navigation, not unified tax-and-benefit calculation, legal provenance, or counterfactual household simulation [@benefitkitchen2026; @myfriendben2024grant].

**Policy simulation** has academic models like PolicyEngine, EUROMOD, and Tax-Calculator. They're rigorous and comprehensive but designed for research, not production API calls at enterprise scale.

No one provides the full stack: income tax + benefits eligibility + household attribute prediction + population simulation in a single, production-ready API. Each piece exists somewhere. The integration exists nowhere.

This gap matters because every application that involves money eventually runs into tax and benefit calculations. A lending app needs to estimate after-tax income. A benefits platform needs to determine eligibility across programs that interact with each other—SNAP benefits phase out as earned income rises, but the Earned Income Tax Credit phases in, and the net effect depends on household composition, state of residence, and a dozen other variables. A financial planning tool needs to project tax liability under different scenarios. An AI assistant asked "how much would I get from the Child Tax Credit?" needs to call *something* to get an accurate answer.

Without unified infrastructure, each company builds fragmented, partial solutions—or gives wrong answers.

---

## Why this can't be trained away

As the introduction described, frontier AI models still get fewer than one in three complete tax returns right [@bock2025taxcalcbench]. The problem hasn't improved despite two years of model advances.

A natural response: "Just train better models." This won't work, for structural reasons:

**Tax law changes annually.** Every January brings new brackets, thresholds, and credits. Training data from last year encodes rules that no longer apply. Models can't extrapolate to provisions they've never seen.

**Fifty states have different rules.** Each state has its own income tax (or none), its own credits, its own benefit programs. The combinatorial explosion of jurisdiction-specific rules exceeds what pretraining can memorize reliably.

**Eligibility depends on dozens of interacting variables.** SNAP eligibility involves income, household size, expenses, categorical eligibility, and state supplements. One wrong variable produces wrong results. Language models compress this complexity into statistical patterns that don't preserve exact logic.

**Financial calculations require 100% correctness.** A model that's 95% accurate sounds impressive until you realize that 1 in 20 tax returns would be wrong. Column Tax's engineers put it directly: "Today's LLMs cannot 'do taxes' on their own because tax calculations require 100% correctness" [@columntax2024].

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

Such infrastructure must be deterministic (same inputs, same outputs, always), auditable (every calculation includes legal citation and parameter values), versioned (git history tracks all rule changes), and bi-temporal (parameters track both when a law takes effect and when the system learned about it).

When an AI agent calls such infrastructure to answer a tax question, the calculation is provably correct, legally citable, and traceable. The AI explains; the infrastructure calculates.

---

## The foundation exists

This infrastructure wouldn't start from scratch.

PolicyEngine has demonstrated the core thesis: tax and benefit rules *can* be encoded accurately at scale. Over a million simulations have run on the platform. HM Treasury formally evaluated the UK model (Chapter 5). US Congressional offices have used the analysis for budget scoring. The codebase covers US federal plus all 50 states, the UK, and Canada—maintained by more than 100 open-source contributors [@policyengine2024about].

But PolicyEngine was designed as a policy analysis tool—a nonprofit providing free research infrastructure. The gap is production infrastructure: encodings packaged for software rather than for policy analysts, with the reliability, speed, and developer-facing documentation that applications need before they can depend on them. That gap can be filled as a public good rather than a product—but it still has to be filled.

That gap no longer feels purely hypothetical. The ecosystem is forming into recognizable layers.

At the household-facing application layer are benefits navigators and screeners like MyFriendBen and Benefit Kitchen. They show that households, nonprofits, healthcare systems, and local governments will adopt high-fidelity eligibility tooling when it is packaged accessibly, and that some of this tooling is already evolving into APIs and partner infrastructure rather than stand-alone questionnaires [@myfriendben2024grant; @benefitkitchen2026].

At the field-building layer, the Beeck Center and Digital Government Hub have turned U.S. rules as code from an isolated idea into a documented community of practice. Their reports and experiments describe the same pattern repeatedly: policy logic lives in PDFs, manuals, and vendor systems; organizations reinvent the same eligibility rules; and AI can assist policy-to-code workflows only when external knowledge and human review remain in the loop [@digitalgovernmenthub2024cop; @digitalgovernmenthub2024implementation; @digitalgovernmenthub2025ai].

At the canonical layer, the Axiom Foundation is attempting to build the missing substrate directly: source documents, machine-readable encodings, provenance, and validation through Atlas, RAC, and AutoRAC [@axiomfoundation2026].

Recent RAC prototypes make the abstraction more concrete, while also clarifying how hard the problem is. The current RAC work treats time, relations, legal judgments, and typed values as first-class concepts rather than forcing all law into scalar formulas. It supports separate "explain" and "fast" execution modes over the same semantics, and the examples now include SNAP, UK income tax, Universal Credit, and a non-tax-benefit Housing Act notice-validity demonstrator [@axiomrac2026]. That last example matters: much of law is not "calculate an amount." It is "does this legal conclusion hold, fail, or remain undetermined given a history of events?" A real rules engine needs to represent that shape of reasoning directly.

And adjacent to all of this, a company like Simile suggests that simulation itself is becoming a broader AI category rather than a niche policy-analysis method [@simile2026company].

How does infrastructure like this get sustained if it isn't a business? The same way other reference commons do. OpenStreetMap, Wikipedia, and the major open-source language ecosystems are public goods supported by some mix of foundations, institutional users, and public grants—not by metering access. The encoding of law fits that mold: governments, courts, benefits agencies, researchers, and AI developers all need the same canonical rules, and none of them is well served by a private gatekeeper sitting between the public and the statute.

Under this model, the engine—the rules, the parameters, the formulas—stays open and free to run. The work that actually costs money—maintaining encodings as law changes, validating against authoritative calculators, packaging for delivery—is funded as the public good it is. Hosted convenience services can exist for those who want them, but they are never the only way to reach the law.

---

## Administrative quality is part of the product

One thing I underappreciated when I first imagined this stack was that the hardest problems are not only mathematical. They are administrative.

For benefits software, "quality" is not exhausted by whether the formula is legally correct. It also includes how quickly a rule change becomes publishable, how many misunderstanding loops occur between policy experts and engineers, how much bespoke hand-holding a partner developer needs before making a correct API call, and how often a tool gives households a misleading answer because the interface cannot express the real-world edge case. In practice, these show up as operational metrics: time to publish, discrepancy rates against authoritative examples, onboarding time for integrators, and the frequency with which support questions expose unclear assumptions.

That frame clarified for me through ordinary work rather than theory. In internal discussions about state policy publication workflows, the useful questions were often not dramatic ones. They were questions about where errors entered, where misunderstandings accumulated, what created bottlenecks, and why one process shipped faster than another. Conversations about benefits screeners raised a parallel concern: if screeners operate on imperfect information, how do they stay up to date, how should they be benchmarked, and what value are they actually providing beyond a brittle eligibility guess? Those are software questions, but they are also policy questions.

The distinction matters because households experience policy through administration. A tax credit that exists in statute but takes six months to appear in a screener is not, from the user's perspective, fully real. A benefits calculator that silently misses an immigration rule or a state-specific exception is not merely an imperfect interface; it can reduce trust, waste caseworker time, and deter take-up. If Axiom-style infrastructure succeeds, one of its main contributions should be to shorten the path from law to working software, reduce the number of transcription errors between policy and engineering, and make the interface between rule maintainers and downstream applications more legible.

---

## A public case study in administrative failure

The stakes became unusually visible during the 2023 Medicaid unwinding. CMS told states to restore coverage for roughly half a million children and families after identifying an eligibility-systems issue in automatic renewals [@cms2023reinstated]. That is what administrative quality looks like from the outside: the legal entitlement exists, the renewal process exists, and yet a software or workflow defect is large enough that federal officials have to order a mass correction.

Zoom in and the failure mode gets more concrete. KFF Health News documented how fixes in Deloitte-run eligibility systems can take months or years to negotiate and implement. In Kentucky, one system limitation that caused a resident to lose Medicaid coverage took about ten months, more than 3,500 hours of work, and over $500,000 to address. In Georgia, officials were still resolving a defect that affected more than 25,000 SNAP and TANF cases nearly two years after the original report [@kffhealthnews2024deloitte].

Benefits screeners face a quieter version of the same risk. Eubanks and coauthors argue that screening tools can appear authoritative even when their internal logic is opaque, causing users to act on incorrect predictions without challenging them [@eubanks2020screening]. That is why administrative quality belongs in the product spec. Faster publication pipelines, benchmark households, visible provenance, and shorter loops between policy and code are not operational luxuries. They are part of whether the tool is safe to use.

---

## Governing a public good

Building this as a public good rather than a business removes the sharpest worries—no shareholders, no paywall on the law—but it doesn't remove the need for governance. Shared infrastructure raises real questions however it's funded.

**Whose rules get encoded first.** Funders and large institutional users always have priorities; a grantmaker may want one program covered before another. The risk is that the roadmap tracks whoever pays the bills rather than where accurate rules matter most. The mitigation is the same as for any commons: transparent governance, a published roadmap, and the fact that anyone can fork and encode what they need.

This matters more for policy infrastructure than for most software. When a database project deprioritizes a feature, the stakes are server uptime. When a rules project deprioritizes one jurisdiction's benefit code, the stakes include whether vulnerable households get accurate eligibility estimates.

**Capture.** Even a nonprofit can be captured—by a dominant funder, or by a maintainer monoculture—until "open" becomes a brand rather than a genuine commons. Independent governance and a real plurality of contributors are the guardrails.

**Sustainability.** Public goods are chronically underfunded; that is nearly their definition. Keeping a country's rules current is unglamorous, never-finished work, and the failure mode here isn't bankruptcy but quiet staleness—encodings that drift out of date as laws change. Durable funding and institutional redundancy matter more than any clever revenue model.

These aren't hypothetical objections. They're the structural challenges any shared rules layer has to address through governance, contributor diversity, and stable funding—whether it's run as a foundation, a consortium, or a government program.

---

## Why open source would matter anyway

Despite the tensions, open-source foundations serve purposes that closed infrastructure cannot.

**Trust through transparency.** When a fintech company integrates tax calculations, they can inspect exactly how those calculations work. When a government agency uses the infrastructure, they can verify it matches statute. No black boxes.

**Distributed maintenance.** Tax law is vast and constantly changing. Open source enables state-level experts to contribute state-specific rules, benefits specialists to maintain eligibility logic, and international contributors to add jurisdictions. No single company can hire enough domain experts to cover every rule.

**Regulatory readiness.** As AI regulation increases, audit trails matter. Calculations based on open-source, citable code are inherently more defensible than LLM outputs. The EU AI Act, US state-level AI regulations, and financial regulators are all moving toward requiring explainability for automated financial decisions.

---

## Is the need real?

Set aside whether this could be a business. Is the underlying need real—real enough to justify building and funding shared infrastructure?

The signals are suggestive.

Avalara built an $8.4 billion business providing sales-tax APIs alone [@avalara2022acquisition]. Column Tax has filed over a million returns through its embedded API. April raised $38 million. The global tax-tech market is projected to grow from $21 billion in 2025 to over $60 billion by 2034 [@taxtech2025market]. Whatever else those numbers show, they show that accurate, programmatic tax and benefit calculation is something the economy already pays for at scale.

But these companies cover narrow slices—sales-tax compliance, income-tax filing, payroll. The full-stack capability—income tax plus benefits plus population simulation—has no single home, and each company rebuilds the overlapping rules privately. That duplication is exactly the waste a shared public layer would remove. It's possible users would rather build their own partial solutions than depend on common infrastructure; it's possible the integration is too complex for one interface. Those are open questions.

Another signal comes from government modernization itself. States are re-procuring large eligibility systems in modular pieces rather than betting again on a single monolith; Colorado's CBMS reprocurement is a clear example [@colorado2024cbms]. If that pattern holds, an external, open rules layer looks less like a speculative thesis and more like overdue public infrastructure.

The honest answer: the need for accurate, comprehensive tax-and-benefit calculation appears real. Whether it gets met as a public good, a commercial service, or a government system is still unsettled—but the need itself is not in much doubt.

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

The work described here is taking shape through two open public-good institutions. The **Axiom Foundation** encodes the rules; the **Brier Institute**—the home, now, for PolicyEngine's microsimulation alongside calibration-native forecasting—models and predicts what those rules do. This chapter is mostly about the first: the rules layer that everything downstream runs on. Both are being built as public goods, not products.

The Axiom Foundation is the nonprofit home of **The Axiom Project**: open standards and canonical encodings for law as code. The foundation is building Atlas—an archive of statutes, regulations, and IRS guidance—and RAC (Rules as Code), a domain-specific language for encoding tax and benefit formulas in a format that's both human-readable and machine-executable. RAC encodes each calculation with legal citations, parameter values, and deterministic logic. An encoding for the Earned Income Tax Credit, for example, traces each step to 26 USC § 32, with parameter values that update annually as the IRS publishes new thresholds. The foundation is also developing AutoRAC, tooling that uses AI to accelerate the encoding of statutes into RAC format. Early jurisdiction-specific encodings—beginning with US federal and several states—live in separate open-source repositories.

The applied layer lives inside the foundation rather than in a separate company. It adds what production use requires—reliable, versioned delivery of the encodings—but ships them by default as open, self-hostable bundles, with lighter hosted endpoints only where they add real operational value. The aim is to let downstream products and agencies build on the rules instead of re-encoding them, not to meter access to the law. The population microdata and synthetic households that turn these rules into distributional estimates live on the modeling side, with PolicyEngine and the Brier Institute.

Keeping the whole stack inside a nonprofit is deliberate. The encoding of law is exactly the kind of thing that shouldn't sit behind a paywall or answer to shareholders—it is reference infrastructure, closer to a dictionary or a map projection than to a product. No commercial entity decides which statutes get encoded or how; the canonical rules stay open, auditable, and free to fork.

### What "encoding law" looks like in practice

The encoding process is more concrete than it might sound. Take the Earned Income Tax Credit's phase-in calculation. The statute (26 USC § 32) defines a credit rate that applies to earned income up to a threshold. RAC encodes this as a formula with explicit parameter references:

- The **credit rate** (7.65% for no children, 34% for one, 40% for two, 45% for three or more) comes from a parameter file that updates when the IRS publishes annual adjustments.
- The **earned income threshold** ($8,260 for no children in 2024) is a separate parameter.
- The **phase-out rate and threshold** are further parameters, split by filing status.

Each parameter includes a legal citation, an effective date, and a source URL. When the IRS publishes Revenue Procedure 2025-XX with new inflation-adjusted amounts, the encoding changes parameter values—not formulas. The formula only changes when Congress amends the statute itself.

The Axiom Foundation validates each encoding against established calculators—TAXSIM for federal taxes, state tax agencies' online calculators for state-level rules. The validation is automated: test cases run against both the RAC encoding and the reference calculator, and discrepancies flag either encoding errors or ambiguities in the statute that require human judgment.

This encoding-and-validation loop is where AI accelerates the work. AutoRAC uses large language models to draft initial encodings from statute text, which human reviewers then verify against authoritative sources. The AI doesn't replace the legal analysis—it produces a first draft that's faster to review than encoding from scratch. Early experience suggests this can meaningfully reduce encoding time for well-structured statutes, though complex provisions with cross-references and exceptions still require substantial human effort.

### The MCP connection

Chapter 9 described how the Model Context Protocol is becoming the standard way AI systems discover and invoke external tools. For tax and benefit infrastructure, MCP matters because it defines how an AI assistant would find and call a tax calculation service. A PolicyEngine or Axiom API endpoint, registered as an MCP-compatible tool server, would be discoverable by any MCP-compatible AI system—Claude, GPT, Gemini, or open-source alternatives. The AI would understand the API's parameters (household income, filing status, state of residence), invoke the correct endpoint, receive a deterministic result, and explain it in natural language.

Without standardized discovery protocols, each AI provider would need custom integration with each calculation service—the same fragmentation problem that plagues the fintech landscape today. MCP doesn't solve the infrastructure gap by itself, but it removes a significant barrier to adoption: the integration cost that prevents AI systems from using specialized tools even when those tools exist.

The work is early. The Axiom Foundation has encoded portions of US federal tax law and several state codes; there is no production-scale public deployment yet. The open question isn't whether there's a market—it's whether a public-good project can sustain the unglamorous, never-finished maintenance that keeping a country's rules current demands.

I include this chapter not because the infrastructure has been built, but because the problem is real regardless of whether this particular attempt succeeds. AI systems need deterministic tools for financial calculations. Column Tax, April, the Axiom Foundation, and others are building pieces of the answer in adjacent layers. No one has yet delivered the full stack that connects taxes, benefits, and population simulation in a single production system.

If this specific attempt stalls, the thesis remains: open, production-grade policy-simulation infrastructure would be valuable however it gets built. Maybe the Axiom Foundation builds it as a public good. Maybe a commercial filer like Column Tax expands beyond filing. Maybe a government agency funds it as public infrastructure. Maybe the open-source community around PolicyEngine and OpenFisca grows to fill the gap. The point of this chapter is the gap, not the claimant.

The honest framing is aspiration, not accomplishment. PolicyEngine demonstrated that open policy simulation is possible and valuable. Whether it can become the production infrastructure that AI systems and financial applications rely on—fast enough, reliable enough, comprehensive enough, and well-enough maintained—remains the open question.

What I can say with confidence: the gap exists. Frontier models still fail most complete tax-return benchmarks. Every Priya at every fintech company that needs accurate calculations builds fragmented, partial solutions. The $60 billion tax tech market is growing fast but remains balkanized into narrow verticals. The need for shared infrastructure appears real, even if the path to building it remains uncertain.

---

## References

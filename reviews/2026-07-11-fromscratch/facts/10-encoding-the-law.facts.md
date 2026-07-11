# Facts catalog — "Encoding the law"

Source: `manuscript/part-3-agent-turn/09-encoding-the-law.md` (headed "Chapter 9" in source; new-TOC position → ch 10).
Facts/Story beats/Arguments paraphrased; Quotes and Author-texture verbatim. Citation keys and `[NEEDS CITATION]`/`[VERIFY]` markers and the DECISION HTML comment preserved exactly.

## Facts

### The market sold only slices
- The core question: what is a household's real income after taxes, after benefits, after the two collide? Needed by a lending platform underwriting a gig worker, a benefits screener, and an AI assistant answering a Child Tax Credit question without inventing the number. Through the mid-2020s none could simply buy the whole answer.
- Income-tax filing specialists: April (embedding returns inside other companies' apps) and Column Tax, which had filed more than a million returns through its API and built an AI agent to help maintain the engine as the law shifts year to year [@columntax2024].
- Sales tax: Avalara, acquired for $8.4 billion in 2022 [@avalara2022acquisition].
- Payroll: ADP and Gusto.
- Benefits screening: MyFriendBen and Benefit Kitchen [@benefitkitchen2026; @myfriendben2024grant].
- Policy research: PolicyEngine, EUROMOD, and Tax-Calculator.
- The global tax-tech market was climbing toward $60 billion [@taxtech2025market], balkanized into verticals that each re-encoded the same overlapping rules behind their own walls.
- The full-stack question — income tax plus benefits eligibility plus the population-level simulation that turns one household into a national estimate — had no home. Benefits and taxes are not separable (SNAP falls as earnings rise while the EITC climbs; the net depends on household composition, state of residence, and interacting thresholds).
- Because no one sold the whole, every company that needed it rebuilt the overlapping rules privately (the same EITC phase-in, the same SNAP deductions), each copy a fresh chance to be wrong.
- Priya (a composite drawn from real fintech engineering teams): her company advanced cash to gig workers who needed their true take-home pay before borrowing. A GitHub tax library handled federal brackets and nothing else, missing low-income users by 30–40%. A commercial tax API charged per call and could not touch benefits. Prompting a frontier model produced a hallucination rate no financial product could ship. Building in-house penciled to eighteen months of engineering before the first law changed underneath it. Every path led to a partial, fragile solution rebuilt privately by every company that hit the wall.

### Why this can't be trained away
- The reasons are structural, not a matter of time: tax law changes every January, so last year's training data encodes rules that no longer apply and a model cannot extrapolate to a bracket it has never seen; fifty states each run their own income taxes, credits, and benefit programs (combinatorial sprawl beyond reliable pretraining memorization); eligibility turns on dozens of interacting variables where one wrong input silently yields a wrong result; and financial calculation tolerates neither 95% nor 99% (right nineteen times in twenty means one return in twenty filed wrong).
- Column Tax's own engineers stated it flatly (see Quotes) [@columntax2024].
- On PolicyBench the best 2026 models still get roughly one in six households wrong by more than a dollar; most miss a quarter or more; the misses are structural (a blown Medicaid determination, a wrong SNAP amount), not rounding [@policybench2026].
- The answer was never a better prompt but a tool: a deterministic, auditable engine the model can call, that computes the number while the model explains it.

### Administrative quality is part of the product
- Correction to what "quality" means: the hardest problems in benefits software are not mathematical. Whether a formula is legally correct is one question; how fast a rule change becomes publishable, how many misunderstanding loops open between policy experts and engineers, how much hand-holding a partner developer needs, and how often a tool hands a misleading answer because its interface cannot express a real-world exception — these decide whether the software is good, and none is a math problem. They surface as operational metrics: time to publish, discrepancy rates against authoritative examples, onboarding time, and the rate at which a support ticket exposes an unwritten assumption.
- Households experience policy through administration: a credit that exists in statute but takes six months to reach a screener is not fully real to the household; a calculator that silently misses an immigration rule or state exception erodes trust, burns caseworker time, and suppresses take-up.
- 2023 Medicaid unwinding: CMS ordered states to restore coverage for roughly half a million children and families after finding a defect in the automatic-renewal logic of their eligibility systems [@cms2023reinstated].
- KFF Health News documented that fixes in Deloitte-run eligibility systems can take months or years — in Kentucky, one limitation that cost a resident his Medicaid coverage took about ten months, more than 3,500 hours of work, and over $500,000 to resolve; in Georgia, officials were still untangling a defect affecting more than 25,000 SNAP and TANF cases nearly two years after it was first reported [@kffhealthnews2024deloitte].
- Deloitte-built eligibility systems span roughly twenty-five states and some $6 billion in contracts [NEEDS CITATION: Deloitte eligibility-system state count and contract value].
- Virginia Eubanks and colleagues showed a screening tool can look authoritative while its logic stays opaque, so people act on wrong predictions without thinking to challenge them [@eubanks2020screening].
- Shared trait of these failures: opacity — a defect buried in a vendor system no outside (often no inside) party could inspect, trace to a rule, or fix quickly; right in statute, wrong in software, invisible until it produced a headline.
- Policy began pricing administrative accuracy directly. Under the One Big Beautiful Bill Act, enacted July 4, 2025 [@obbba2025], states will for the first time — beginning in fiscal 2028 — pay a share of SNAP benefit costs pegged to their own payment error rate: nothing while the error rate stays under 6%, then 5%, 10%, or 15% of benefits as it crosses 6%, 8%, and 10%.
- The national payment error rate for fiscal 2025 was 10.6% [NEEDS CITATION: USDA FY2025 SNAP national payment error rate], an average that would put many states straight into the top penalty tier.
- The state share of SNAP administrative costs rises from 50% to 75% in fiscal 2027 [@obbba2025].
- Medicaid's new work requirements oblige states to stand up verification systems by the end of 2026 [NEEDS CITATION: CMS interim final rule, December 31 2026 verification deadline].
- Framing: a payment error rate used to be an audit statistic; it is now a line in the state budget — the cost that verified, provenance-carrying rules infrastructure exists to lower.
- Precedents (downside not hypothetical): Australia's Robodebt scheme raised automated debts against welfare recipients on faulty income-averaging, was unwound in the courts, and put ministers before a royal commission [NEEDS CITATION: Robodebt royal commission]. Michigan's MiDAS system issued tens of thousands of false fraud determinations against unemployment claimants [NEEDS CITATION: Michigan MiDAS false-fraud determinations]. Arkansas replaced a nurse's judgment with an algorithm for allocating Medicaid home-care hours, cut care for disabled residents, and drew litigation [NEEDS CITATION: Arkansas algorithmic home-care-hour cuts litigation]. In each, the arithmetic was automatable and the judgment was not.
- USDA's Food and Nutrition Service has held that AI may not replace state merit personnel in SNAP eligibility determinations [NEEDS CITATION: FNS guidance on AI and merit personnel in eligibility determinations] — a boundary matching the book's stance: decision support, not decision replacement; a human makes the determination and the tool makes it checkable.

### The Axiom Foundation (field-report facts)
- Axiom is a Delaware nonprofit, fiscally sponsored by the PSL Foundation, anchored by funding from Ballmer Group; Ariel Kennan became its president on July 1, 2026; it launches publicly on July 28 [@axiomfoundation2026].
- Charter (narrow and immodest at once): encode the law itself, exactly, as open infrastructure — in a form anyone can run and anyone can check. PolicyEngine had proved tax and benefit rules could be encoded accurately at all; Axiom is the attempt to encode all of them.
- The wager: agent-drafted encoding behind merge-blocking checks is what makes that scope tractable for a nonprofit.
- Its sibling institute, Thesis, takes the other half (forecasting what government will actually do) and belongs to later chapters.

### RuleSpec and the corpus
- An Axiom encoding is not an ordinary program. Its format, RuleSpec, is a set of YAML files that hold the law's logic and the law's numbers apart, each file versioned, each testable, each stamped with the dates over which it takes effect.
- The logic computing a credit lives in one place; the parameters it reads (a rate, a threshold, a phase-out amount) live in another, so an agency's inflation adjustment changes a parameter value and not the logic. An act of Congress changes the logic; an annual revenue procedure changes only the numbers; both are versioned files with effective dates, so an encoding answers not only "what does the law say" but "what did it say last March, and when did we learn it had changed."
- EITC example: the statute defines a credit that climbs with earned income at a set rate up to a ceiling, plateaus, then phases out above a higher income threshold shifting with filing status and number of children; in RuleSpec that becomes a formula referencing named parameters (phase-in rate, earned-income ceiling, phase-out rate and threshold), each carrying its own citation, effective date, and source link.
- Beneath the rules sits the corpus — the source text itself. Axiom ingests statutes, regulations, agency manuals, and sub-regulatory guidance as anchored provisions, each clause individually addressable, organized against a registry of roughly 41,000 legal concepts [VERIFY: corpus concept-registry count].
- The corpus makes provenance possible: an encoding earns trust by pointing back to the exact governing words, which live in a service anyone can open and read. Anchoring matters because the rule a caseworker applies is often buried in an agency manual or guidance letter; the corpus holds primary law and its sub-regulatory layers at clause resolution.

### The encoding pipeline (axiom-encode)
- Encoding law by hand is slow and does not scale; a team can keep one country current or attempt fifty, not both. The pipeline axiom-encode turns encoding from analyst-months into agent-runs.
- Stages: pull the relevant provisions from the corpus → scaffold a prompt around them (statute text, the concepts they touch, the shape of the encoding to produce) → hand to a language model that drafts the RuleSpec → then, before anything merges, run a gauntlet in which every gate can block the merge.
- The gates: the code must compile; its tests must pass; a proof step must validate the logic's internal consistency; the output must be compared against independent reference calculators; every monetary obligation must be grounded in the source.
- Only a draft that clears all gates yields a signed manifest — a cryptographic record of what was encoded, from which sources, having passed which checks — so a later reviewer, a skeptical agency, or a court can reconstruct provenance rather than take it on faith.
- Human review sits deliberately at the top of the stack, not the bottom: the machine drafts and the gates screen, while a person adjudicates the judgment calls the statute leaves open (cross-references and exceptions no gate can settle).
- Each gate defends a different failure: compilation catches an encoding that does not run; the tests catch a change that breaks a case that used to work; the proof step catches logic that contradicts itself; comparison against an independently built calculator catches an encoding that runs, passes its own tests, and is still wrong (the failure no self-check can see — the subject of the next chapter); the last gate catches a number with nothing behind it.
- None of the gates trusts the model that wrote the draft; the pipeline runs several language-model backends and stays indifferent to which produced a given encoding, because the guarantee lives in the gates, not the generator. A better model drafts faster and trips fewer checks but never earns the right to skip them.

### The money-atom gate
- The money-atom gate demands that every monetary obligation an encoding produces — every dollar figure the law commands — trace to a quoted excerpt of the governing source: the actual authorizing words pulled from the corpus, not a section number in a comment.
- It targets money rather than every clause because a wrong eligibility flag is a bug but a wrong dollar figure is a household underpaid or a program overexposed — the failure mode with a face on it; grounding every commanded amount in the words that command it puts the tightest check where the damage is largest.
- If a figure cannot be grounded that way, the build does not warn — it fails.
- Consequence: ordinary software cites its sources in documentation that drifts out of date the instant someone edits the code; a merge-blocking check cannot drift, because nothing merges until it passes. "Every number traces to the law" is a build condition, not a professed virtue.

### What counts as law (shipped scale)
- By July 2026 the US repository held on the order of 3,000 rule files with matching tests, covering federal law plus twenty-eight state codes, absorbed with their full git history [VERIFY: US rule-file and state counts].
- Absorbing a state code with its history (rather than retyping it) means the encodings inherit years of prior fixes and the reasoning behind them — a change of representation, not a fresh start with fresh bugs.
- Separate monorepos carried the United Kingdom, Canada, New Zealand, and Belgium, alongside a set of African lanes validated against established reference models (taken up in full in a later chapter). A single pipeline produced all of it, putting the marginal cost of the next jurisdiction in units of agent-time rather than institution-years.
- Scope is deliberately, almost provocatively, total: not "the parts of law that compute a number" but all public policy — statutes, regulations, agency manuals, statutory guidance, grant conditions, and the eligibility scheme of a single London borough.
- Among early UK encodings is the council-tax-reduction policy of the Royal Borough of Kingston upon Thames: a local scheme binding on a few tens of thousands of residents, encoded with the same machinery as federal income tax; a resident is governed by it as concretely as by any act of Parliament.
- Stated rule: bindingness is metadata, never a scope filter. Whether a provision is hard law or soft guidance is recorded as a property of the encoding, never used to decide whether it is worth encoding.
- Axiom models authority explicitly, representing the chain by which a statute delegates power to an agency and an agency binds itself through its own published policy. The doctrines are old — in US law an agency must follow its own regulations; in English law it must follow its own stated policy absent good reason [NEEDS CITATION: Accardi and Lumba authority doctrines] — and encoding them lets a model answer not only what a rule computes but whether the body applying it had authority to.
- Licensing: everything ships under permissive licenses, Apache 2.0 for the code and Creative Commons Attribution for the content, so no one need ask permission to run, fork, or build on the encoded law.
- Much of law is not "compute an amount" at all but "does this conclusion hold, fail, or remain undetermined given a history of events?" (whether a notice is valid, a deadline met, a procedure followed). Modeling authority, delegation, and legal judgment lets the encodings represent that second shape — the difference between encoding a calculator and encoding the law.

### Governing a commons
- Building this as a public good removes the sharpest objections (no shareholders, no paywall on the law) without removing the need for governance. Three failure modes:
  - Whose rules come first: funders and large institutional users have priorities; the risk is a roadmap tracking whoever pays rather than where accurate rules matter most (deprioritizing a jurisdiction's benefit code risks whether vulnerable households get accurate answers). Guardrails: transparent governance, a published roadmap, and the standing ability to fork.
  - Capture: even a nonprofit can be captured by a dominant funder or a maintainer monoculture until "open" is a brand rather than a fact; independent governance and a genuine plurality of contributors are the only durable defense.
  - Staleness: public goods are chronically underfunded; the characteristic failure is not bankruptcy but quiet drift as laws change while no one notices; the conformance ratchets of the next chapter turn "keep it current" into a gate under which coverage can only rise and unexplained gaps can only fall.
- Openness is the mechanism behind the defenses: a fintech can read exactly what the encodings compute, an agency can confirm they match statute, and a citable, inspectable rule is more defensible than a model's unexplained output when a regulator or court asks for an audit trail; the ability to fork is the ultimate check on capture.
- Deeper (structural) commitment: the encoding of law is reference infrastructure — closer to a dictionary or a map projection than to a product — and is not well served by a private gatekeeper sitting between the public and the statute. So the rules layer is a commons, and the commercial activity growing around it (managed runtimes, service-level guarantees, applied products) is built on the commons, never owner of it.
- One such operator already exists in formation, organized around graded simulation; it is not yet public.
- DECISION marker (reproduce verbatim; located in the "Governing a commons" / commons-and-operators section of this chapter): `<!-- [DECISION for author at publication: whether to name Cosilico PBC here] -->` — the commercial operator is left unnamed in prose pending the author's publication decision.
- The line the foundation commits to publicly: the commercial service tier will always be a separate entity, so the foundation never competes with builders on its own commons; the law stays free to run and only the convenience of not running it yourself has a price.

### An honest failure (the B1 probe)
- In July 2026 Axiom ran an experiment on the premise that encodings are essentially cache: if every rule is deterministically derived from source text, no encoding need be a durable artifact — you could discard any module and regenerate it from the corpus on demand, cheaply. Known internally as the B1 probe; put the premise to twenty-five modules.
- It failed. Regeneration was genuinely cheap — about eight cents of compute per module — but in twenty-three of the twenty-five cases the original encoding was the correct one and the freshly regenerated version introduced naming instability that would have broken every downstream consumer (same source, same pipeline, different output; silent damage).
- Conclusion adopted (against the elegant version of its own story): encodings are not disposable cache; they are durable artifacts with provenance, and regeneration, at the current configuration, is not yet trustworthy enough to lean on. The finding changed how encodings are treated — stored, versioned, migrated with care, not discarded and re-derived — and regeneration went back on the shelf as a research problem.
- Framed as the discipline working, not failing: a project convinced of its own story would have shipped regeneration and met the breakage in production.

### Closing (grounding is not correctness)
- Encoding all public policy at agent speed is worth nothing unless the encodings are right; "a language model wrote it and the tests passed" is not by itself a reason to trust a number that decides whether a family makes rent. Compilation proves the code runs; the money-atom gate proves each dollar traces to the law; neither proves the encoding matches the world.
- That proof is a separate discipline — comparison, case by case, against independent calculators built by other people with other tools, and explaining rather than waving away every place they disagree. How to trust law encoded by machines = the next chapter.

## Story beats

- Priya's dead ends: the composite fintech engineer runs the full-stack real-income problem to ground and hits a partial, fragile solution at every path (GitHub library missing low-income users by 30–40%, per-call commercial API that can't touch benefits, un-shippable model hallucination rate, 18-month in-house build obsolete before the first law change).
- Administrative failure at scale: the 2023 Medicaid unwinding (CMS commanding ~500k restorations); the Kentucky fix (about ten months, 3,500+ hours, $500k+); the Georgia defect (25,000+ SNAP/TANF cases untangled nearly two years later).
- Provenance becomes a merge condition: the money-atom gate fails the build (rather than warning) when a commanded dollar figure cannot be grounded in quoted source.
- The B1 probe turns red: the "encodings are cache" premise tested on 25 modules and failing 23/25 on naming instability — the discipline catching its own authors and forcing the durable-artifact conclusion.

## Quotes

- Column Tax's engineers, on why today's language models cannot file returns unaided: language models "cannot 'do taxes' on their own because tax calculations require 100% correctness" [@columntax2024].

## Arguments

1. The market sold slices of the tax-and-benefit answer but never the whole; the full-stack question (tax + benefits + population simulation) had no home, so everyone rebuilt overlapping rules privately — each private copy a fresh chance to be wrong.
2. This cannot be trained away for structural reasons: annual law changes, fifty-state combinatorial sprawl, dozens of interacting eligibility variables, and a 100%-correctness requirement that 95–99% cannot meet.
3. Administrative quality — speed to publish, discrepancy rates, onboarding, interface expressiveness — is part of the product, not an afterthought; households experience policy through administration, and opaque vendor defects cause real harm.
4. Policy now prices administrative accuracy directly (OBBBA's SNAP error-rate cost-share; the 50→75% admin share; the Medicaid verification deadline), turning an audit statistic into a budget line — the exact cost verified rules infrastructure can help lower.
5. The right boundary is decision support, not decision replacement (the FNS merit-personnel bright line): a human decides, the tool makes the decision checkable; automating judgment without a check causes the Robodebt/MiDAS/Arkansas class of harm.
6. Separating logic from parameters, both versioned with effective dates, lets an encoding answer not only what the law says but what it said on a past date and when the change was learned.
7. Provenance is enforced, not professed: the money-atom gate is merge-blocking, so "every number traces to the law" is a build condition that cannot drift, unlike documentation.
8. Trust lives in the gates, not the generator: the pipeline is indifferent to which model drafted an encoding because no draft merges until every gate passes.
9. Scope is total by principle — bindingness is metadata, never a scope filter — because a household is governed by the manual a caseworker follows as much as by the statute behind it; modeling authority and delegation is what makes it encoding the law rather than encoding a calculator.
10. A commons is the right structure for reference infrastructure (no gatekeeper between public and statute); its failure modes (roadmap capture, funder/maintainer capture, staleness) are answered by transparent governance, plurality, forkability, and — for staleness — the next chapter's ratchets.
11. The discipline is real because it fails its authors: the B1 probe disproved the seductive "encodings are cache" premise (23/25 regenerations worse), establishing encodings as durable provenance-bearing artifacts.
12. Compilation and money-atom grounding prove runnability and sourcing, not correctness; correctness requires independent oracle comparison — the boundary question the next chapter answers.

## Author-texture (verbatim, may be reused)

- Protected keeper (verbatim): "Provenance stopped being a promise and became a merge condition."
- Candidate distinctive line (verbatim, NOT on the protected keeper list — bolded standalone in source): "Bindingness is metadata, never a scope filter."

## Structural notes

- Chapter's job: introduce the Axiom Foundation and the RuleSpec / corpus / axiom-encode machinery; establish administrative quality (and OBBBA's pricing of accuracy) as the real product problem; make provenance a merge condition via the money-atom gate; state the total-scope, bindingness-is-metadata charter; name the commons governance risks and the (unnamed) commercial operator; log the B1 honest failure; end by conceding grounding ≠ correctness → verification.
- Handoff in (from ch 8): the demanding, accountable tool ch 8 defined is what this chapter builds.
- Handoff out (9→10, the trust question): closing line — "How to trust law encoded by machines is the subject of the next chapter."
- DECISION marker location: the commons-and-operators discussion ("Governing a commons") carries `<!-- [DECISION for author at publication: whether to name Cosilico PBC here] -->`.
- Markers to carry: `[VERIFY: corpus concept-registry count]` (~41k); `[VERIFY: US rule-file and state counts]` (~3,000 files / 28 states); `[NEEDS CITATION]` on Deloitte state count/contract value, USDA FY2025 SNAP national payment error rate (10.6%), CMS Dec 31 2026 verification deadline, Robodebt royal commission, Michigan MiDAS, Arkansas home-care litigation, FNS merit-personnel guidance, Accardi and Lumba doctrines.
- Naming discipline: the data layer is populace (no old name here); the commercial operator stays unnamed in prose; "Cosilico" appears only inside the author-facing DECISION comment, never as current prose.

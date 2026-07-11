# Fact catalog — 00-preface.md (+ index.md landing text)

Source files:
- `manuscript/front-matter/00-preface.md`
- `index.md` (landing-page thesis text; unique material folded in below, tagged [from index.md])

## Facts

- In 2019, the author was trying to understand how a universal basic income would affect poverty in the United States, and wanted the precise version of the answer, not the "vibes-level" version.
- The precise questions he wanted answered: how many families would cross the poverty line, which families, and what it would cost net of reduced spending on existing programs.
- A $1,000-a-month basic income runs to roughly $3 trillion a year. (uncited)
- The interesting questions about a UBI live in how you pay for it and in how it interacts with the Earned Income Tax Credit, SNAP, Medicaid, and housing assistance.
- The author couldn't find the answer — not because no one had modeled it, but because the models that could answer were locked inside government agencies and think tanks, built on confidential data, and inaccessible to outsiders.
- The Congressional Budget Office (CBO) had such models. The Tax Policy Center had such models. The Joint Committee on Taxation (JCT) had such models. None were available for the author to query with his specific question. (uncited)
- The author started building: first a scrappy research outfit called the UBI Center, running analyses on existing open-source tools.
- Then, with Nikhil Woodruff, the author built PolicyEngine — an attempt to make policy simulation available to anyone with a web browser.
- Disclosure (carried in a footnote): as of July 2026, Nikhil Woodruff serves in the UK government at 10 Downing Street. [VERIFY with Nikhil: role wording] — the footnote flags that where the book discusses UK institutions evaluating tools Nikhil helped build, this should be read with that in mind.
- PolicyEngine lets a user enter household details, change a policy parameter, and see what happens — no expertise required, no paywall, no waiting for an analyst to run the numbers.
- The book begins in 1957 with Guy Orcutt, described as an economist-engineer who imagined simulating society household by household, decades before the computers existed to do it.
- The book moves through six decades of institutional microsimulation: mainframes at the Urban Institute, proprietary models at the Congressional Budget Office, and the open-source policy tools that emerged in Europe and the United States. (uncited)
- Projects the author has built or helped build, named in the preface: PolicyEngine, HiveSight, Democrasim, the Axiom Foundation, and the Thesis Institute.
- A chapter drafted in 2025 as a sketch of infrastructure that didn't yet exist had to be rewritten in 2026 as a field report on infrastructure that does — described as law encoded by AI agents and checked, line by line, against the models governments already trust.
- The book labels claims by category throughout: "this works," "this is early," and "this might work someday."
- The Axiom Foundation launches publicly in summer 2026 ("this summer"); the Thesis Institute follows in fall 2026 ("the fall").
- As of the writing, not one of the forecasts published by the Thesis Institute's scoreboard has resolved; grading against reality will take years.
- The book is written for three readers: policy people, technologists, and curious readers — and any one lens is said to be enough.
- The book runs in five parts (Part I: The closed stack; Part II: The open engine; Part III: The agent turn; Part IV: The prediction pole; Part V: The horizon).
- Part I spans Orcutt's 1957 vision through the tax model wars, ending on the accuracy question ("how would you know whether any of these models is right?").
- Part II is the PolicyEngine story: rebuilding the closed stack in public, what the engine shows for one household and a whole country, and the three ingredients every such model must solve.
- Part III (called "the new heart of the book") covers why AI systems need deterministic policy tools, how AI agents came to write verified law-as-code at scale, how to trust machine-encoded law, and reaching countries that never had public models.
- Part IV crosses from calculation to forecasting: the uncertainty point estimates hide, the scoreboard being built to price it, and what large language models add to opinion research once benchmarked.
- Part V is the speculative edge: simulated democracy, simulated values, and a return to the fork in the road opened by the introduction.
- Signature/attribution: "Max Ghenis / Washington, DC, 2026."
- [from index.md] The book's title is "Society in Silico."
- [from index.md] The book's framing question: "Can simulation help society realize its goals?" — specifically whether open computational models of social systems (taxes, benefits, populations, forecasts, even opinions and values) can help humanity reason more clearly about what it wants and how to get there.
- [from index.md] The book's stated answer is a method, not a destination: build the analytic stack of government in the open, and hold every layer to one discipline — a simulation is admissible only where its verification chain terminates in ground truth.
- [from index.md] The verification discipline is spelled out in three instances: a rule checked against the statute and against the calculators governments already trust; a synthetic population checked against surveys and administrative totals; a forecast graded when the official number lands.

## Story beats

- 2019: author wants a precise answer on how a UBI would affect US poverty (how many/which families cross the poverty line; net cost after offsetting existing-program spending); can't get it because the capable models (CBO, Tax Policy Center, JCT) are locked inside institutions, built on confidential data, inaccessible to outsiders.
- Author responds by building: starts the UBI Center (a scrappy research outfit running analyses on existing open-source tools), then co-founds PolicyEngine with Nikhil Woodruff to put policy simulation in anyone's web browser.
- That work generates a chain of larger questions (encode tax law → what else can you encode; AI needs calculations it can't do → who builds the tools it calls; simulate wallets → can you simulate opinion; simulate policies/opinions/values → what does it mean for how society governs itself). The book is the author's attempt to trace those questions from origins to implications.
- Between the 2025 first draft and the 2026 revision, one chapter had to shift from speculative sketch to field report because the infrastructure it described (AI-agent-encoded, verified law-as-code) came to exist in the interval.

## Quotes

(No verbatim third-party quotations appear in the preface. All voice-carrying verbatim passages are the author's own — see Author-texture.)

## Arguments

1. Answering real policy questions precisely (e.g., a UBI's effect on poverty and its net cost) requires household-level models, not aggregate/"vibes-level" reasoning.
2. The models capable of answering existed but were locked inside government agencies and think tanks, built on confidential data — so the analytic capacity was inaccessible to the public.
3. The response to inaccessibility is to build open alternatives (UBI Center, then PolicyEngine) that put the same kind of simulation in anyone's browser, free and without gatekeeping.
4. Encoding tax-and-benefit law as code opens a widening set of questions — what else can be encoded, who builds the tools AI calls, whether opinion and values can be simulated, and what all of it means for self-governance.
5. The honest status of each claim ("works" / "early" / "might work someday") is the book's central currency, and the speed at which items moved between those categories is itself part of the story.
6. The book is deliberately not a textbook, not a memoir, and not a manifesto: technical detail serves ideas; personal experience is connective tissue only; views are presented alongside their strongest counterarguments.
7. Core thesis: the tools we use to understand society shape the decisions we make about it; when tools are locked inside institutions the understanding is locked too, and when they are open/transparent/accessible, more people can participate in deciding what policies to adopt and why.
8. [from index.md] The claim is a method, not a destination — the book does not claim a perfect model of society is possible; it claims open, ground-truth-verified models can help society reason about what it wants.

## Author-texture (verbatim, may be reused)

- Opening of the preface (the 2019 UBI origin): "In 2019, I was trying to understand how a universal basic income would affect poverty in the United States. Not the vibes-level version—'it would help a lot of people' or 'it would cost too much'—but the precise version. How many families would cross the poverty line? Which families? What would it cost, net of reduced spending on existing programs?"
- The question chain that pivots from building to the book's subject (sat after the PolicyEngine introduction): "If you can encode tax law as code, what else can you encode? If AI systems need accurate financial calculations and can't do them on their own, who builds the tools they call? If simulation can tell you what a policy does to people's wallets, can it also tell you what people think about it? And if you can simulate policies, opinions, and values—what does that mean for how society governs itself?"
- The honest-accounting / moving-target passage (from "What this book is"): "The honest accounting turned out to be a moving target. A chapter drafted in 2025 as a sketch of infrastructure that didn't yet exist had to be rewritten in 2026 as a field report on infrastructure that does—law encoded by AI agents and checked, line by line, against the models governments already trust."
- The "not finished" time-anchored disclosure (from "What this book is not"): "The Axiom Foundation launches publicly this summer; the Thesis Institute follows in the fall; the forecasts its scoreboard publishes will take years to grade themselves against reality, and as of this writing not one has resolved."
- The closing thesis-and-invitation (final section, before the signature): "I started this project because I believed—and still believe—that the tools we use to understand society shape the decisions we make about it. When those tools are locked inside institutions, the understanding is locked too. When they're open, transparent, and accessible, more people can participate in the conversation about what policies we should adopt and why. That's an optimistic view. Whether it survives contact with the evidence is something you can judge for yourself."
- [from index.md] The method-not-destination framing that closes the landing text: "Society in silico is not a destination. It's a method."
- [from index.md] The scope disclaimer that opens the landing text: "Not 'can we build a perfect model of society' — we can't, and this book doesn't claim to."

## Structural notes

- Job of the preface: establish the author's personal origin (2019 UBI question → inaccessible institutional models → building UBI Center then PolicyEngine), set the book's honest-accounting contract ("works / early / might work someday"), define what the book is and is not, name its three audiences, and lay out the five-part structure with a reading path.
- Required disclosure carried in the preface as a footnote: Nikhil Woodruff, PolicyEngine co-founder, serves in the UK government at 10 Downing Street as of July 2026 [VERIFY with Nikhil: role wording]; must be surfaced wherever the book discusses UK institutions evaluating tools he helped build. Preserve this disclosure in any rewrite.
- Preserve the [VERIFY with Nikhil: role wording] marker — do not delete on rewrite.
- Cross-references the preface sets up (each maps to later parts/chapters): Guy Orcutt / 1957 (Part I / Ch 1); institutional microsimulation history — Urban Institute, CBO, European + US open-source tools (Part I); PolicyEngine build (Part II); AI-agent-encoded verified law-as-code (Part III); scoreboard/forecast grading and LLMs in opinion research (Part IV); simulated democracy and simulated values (Part V); "the fork in the road" is opened by the introduction and returned to in Part V.
- Named projects that must be treated as the author's own (disclosure of interest applies): PolicyEngine, HiveSight, Democrasim, the Axiom Foundation, the Thesis Institute.
- Reading-path guidance the preface gives: impatient readers → introduction, then Part III, then dip into Part V; readers with time → start with the Part I history.
- The five-part scaffold (closed stack / open engine / agent turn / prediction pole / horizon) is the book's spine and is introduced here for the first time — the introduction restates it in more detail (see 01-introduction facts).
- index.md is the landing/thesis page; its unique contributions are the title, the one-line framing question ("Can simulation help society realize its goals?"), the explicit "admissible only where its verification chain terminates in ground truth" discipline, and the "method, not a destination" refrain — all of which the preface implies but index.md states outright.

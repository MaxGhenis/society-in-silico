# Fact catalog — Chapter 5: Proof of concept

Source: `manuscript/part-2-open-engine/05-proof-of-concept.md`
(Chapter 5 in the manuscript; Part II chapter 5 in the from-scratch outline. Output filename offset to `06-…` per the facts-folder convention.)

Extraction rules applied: every claim below is paraphrased except where marked as a quote or author-texture. Citation keys `[@key]` are preserved exactly and placed with their facts. `[NEEDS CITATION: …]` and `[VERIFY: …]` markers are carried verbatim. Specific claims (dates, counts, dollar figures, named attributes) that carry no citation key and no marker are flagged `(uncited)`.

---

## Facts

### The state of play, 2019–2021
- In October 2019, UKMOD became the first freely available tax-benefit microsimulation model of the United Kingdom [@ukmod2020].
- Before UKMOD, the UK already had proprietary tools: the Institute for Fiscal Studies had run TAXBEN since 1983 (uncited); HM Treasury had IGOTM, its internal tax and benefit model (uncited); the Department for Work and Pensions had its Policy Simulation Model (uncited).
- UKMOD was built on EUROMOD's UK component and funded by the Nuffield Foundation, and was open to anyone who asked (uncited).
- When COVID-19 arrived, demand for policy analysis spiked as pandemic rules changed weekly — the CARES Act, expanded unemployment insurance, and recovery rebates (uncited).
- NBER updated its TAXSIM calculator for the new pandemic provisions (uncited).
- Tax-Calculator shipped a pandemic release, version 3.2.1, in August 2021 [NEEDS CITATION: Tax-Calculator v3.2.1 release date].
- In December 2020, EUROMOD went fully open source; the European Commission's Joint Research Centre took it over the following month (January 2021) (dates uncited). EUROMOD had been the backbone of European tax-benefit modeling for two decades [@sutherland2013euromod].
- The International Microsimulation Association convened a conference in December 2020 devoted entirely to pandemic policy responses (uncited).
- The open-source Policy Simulation Library kept adding models over this period (uncited).
- Author's framing: the ecosystem was growing fast, and almost none of it was usable by anyone who could not write code.
- The author started the UBI Center in 2019 out of a specific frustration: no public tool could say with any specificity what various universal basic income proposals would cost or whom they would help [@ubicenter2019intro].
- The UBI Center published open-source analyses of basic income proposals using whatever existed — mostly Tax-Calculator and custom Python scripts running on Census survey data (uncited).
- Lesson one (fragmentation): Tax-Calculator handled federal income tax but ignored benefits; TAXSIM handled state taxes but ran in batches; nothing captured the full tax-benefit interaction that decides whether a basic income is progressive, regressive, or poverty-reducing (uncited). Illustration: funding a basic income by tapering an existing benefit can lift some families while stranding others at a cliff, and no available tool showed both effects at once.
- Lesson two (access gap): the audience for policy analysis was far larger than the audience that could run the tools; UBI Center analyses lived in Jupyter notebooks, so readers could not vary parameters, change the household, or model their own group's variant.

### Building the application
- By late 2020, Nikhil Woodruff and the author had a working microsimulation model of the UK tax-and-benefit system, built at the UBI Center (uncited).
- Nikhil Woodruff was an undergraduate at University College London reading mathematics and computer science, and the stronger engineer of the two (uncited).
- Their UK model was OpenFisca UK; it could calculate taxes, simulate benefits, and estimate the effect of a reform, but it ran only in Python scripts a programmer could use (uncited).
- The pattern they saw everywhere: powerful tools locked behind technical barriers — TAXSIM wanted batch files, Tax-Calculator wanted Python, UKMOD was built for academics, TAXBEN was proprietary.
- The goal they set: put the full power of microsimulation in a browser so anyone could design a reform, see its cost and distributional effect, and check its effect on their own household without writing code. They named it PolicyEngine.
- PolicyEngine was built in three layers: (1) a model layer running OpenFisca UK in Python on cloud servers, returning exact tax and benefit before and after a change; (2) an API layer wrapping the model in HTTP endpoints so interface and rules could evolve independently; (3) an application layer, a React web app that turned user answers (income sources, number of children, housing costs) and reform choices (sliders, toggles) into API calls and drew the results.
- Core architectural decision: the model had to be usable without the interface — the API was the product and the web app was merely its first consumer; any researcher, journalist, or program could call the same engine that ran the website.
- Division of labor: Nikhil handled most engineering (API design, React front end, state management); the author worked the policy logic (which parameters to expose, how to present results, what comparisons mattered).
- Interface-complexity compromise: expose every parameter and a user drowns (there are thousands); hide too many and the tool is gutted. They exposed a curated set of frequently debated parameters (income tax rates, benefit levels, credit amounts) plus the option to reach any parameter in the model. Output used progressive disclosure: headline numbers first (net cost, poverty change), then breakdowns by income decile, household type, and region.
- PolicyEngine UK launched in September 2021 [@policyengine2021review].
- On launch, users could enter a reform (raise income tax, increase child benefits, introduce a carbon dividend) and see cost to the Treasury, change in poverty, shift in inequality, and the effect on their own household.
- Within weeks of the UK launch, advocacy groups were using it to design proposals (uncited).
- When the Chancellor's Autumn Budget changed Universal Credit, PolicyEngine published distributional analysis within a day [@policyengine2021review].
- In October 2021, PolicyEngine spun out as a separate nonprofit; the mission statement shifted from "make everyone a policymaker" to "help people understand and change public policy" (dates/wording uncited beyond the org's own statements).
- Incorporating as a 501(c)(3) was a deliberate trust choice: keep the code open for inspection and have no shareholders whose interests could bend results, so groups across the political spectrum could trust the engine was not tilted.
- At this stage the operation was two people plus a rotating cast of volunteers and interns, with a website that repeatedly went viral faster than they could fix the bugs the traffic exposed (uncited).

### Crossing the Atlantic
- PolicyEngine US launched in March 2022 [@policyengine2022review].
- The US posed a different shape of complexity: the UK has one national tax system (though Scotland sets its own income tax rates) and Universal Credit had folded most means-tested support into one program; the US has fifty states with separate income tax codes over a complex federal system, and benefits scattered across agencies — SNAP at USDA, SSI at the Social Security Administration, Medicaid at HHS, housing vouchers at HUD, childcare subsidies at the states — each defining income, counting the household, and setting eligibility its own way.
- Author's framing: modeling the US was not harder than the UK by a constant factor; complexity grew multiplicatively rather than additively.
- They started with what they could model — federal income and payroll taxes, SNAP, the EITC — and shipped the household calculator first (uncited).
- In July 2022 they added population-level impacts using the Current Population Survey, the same microdata foundation behind official government estimates [@policyengine2022review].
- State coverage came one state at a time: some states piggyback on federal adjusted gross income and fall into place once the federal model exists; others (e.g., New York, with multiple income tax schedules, city taxes, and supplemental credits) were miniature ecosystems, and encoding one rarely transferred to the next.
- By the end of 2022 they had modeled six states, leaving forty-four remaining (uncited).
- Capacity gap: they wanted comprehensive, always-current coverage but relied on a small volunteer team encoding rules on weekends; e.g., a contributor might encode Oregon's working-family credit only to find the legislature had amended eligibility rules mid-session with no updated documentation (illustrative).
- Contributor model: anyone could submit a pull request encoding a state's rules, and the team reviewed for accuracy and code quality; this worked where a local expert volunteered and failed where none did, so coverage tracked contributor geography rather than policy importance.

### Who used it
- Congressional-staff use pattern: an aide could use PolicyEngine to check whether a proposed child tax credit expansion would reach the families a member cared about (e.g., finding that a credit phased in over the first few thousand dollars of earnings missed the poorest households), then reshape the legislative language before requesting a formal CBO score — changing the questions that arrived at CBO rather than replacing the formal process (illustrative vignette).
- Democratization pattern: advocacy groups and academic researchers who had relied on government estimates or expensive consultants could now run their own simulations [@policyengine2022review].
- Example of a volunteer-run user: UBI Lab Northern Ireland could model a recovery basic income on its own, without commissioning a think tank (uncited).
- Developer/API use: the Fund for Guaranteed Income wired PolicyEngine into a tool showing cash-pilot participants how their other benefits would change as income rose (uncited).

### The validation challenge
- Open source means anyone can inspect the code, but inspection is not correctness; the team invested heavily in validation against official calculators and published statistics.
- Each model carried a test suite checking outputs against official calculations across hundreds of household scenarios (uncited).
- Every discrepancy raised a three-way question: was the bug in PolicyEngine's code, in the official calculator, or in the team's reading of an ambiguous rule?
- Simple case: an outside contributor comparing results against IRS tables caught a transposed phase-out rate — 21.60 percent entered where the EITC's two-child schedule specifies 21.06 percent [VERIFY: real incident].
- Ambiguous case: when a regulation says income is figured "net of applicable deductions," different official sources sometimes gave different answers about which deductions apply; the team kept a running log of such cases. The log was itself a finding: the tax-benefit system is complex enough that the agencies administering it sometimes disagree about its own rules.
- For the UK model, HM Treasury eventually ran its own evaluation and found that 60 percent of National Insurance calculations fell within 0.5 percent of its internal model [@hmt2025policyengine].
- UK income tax proved harder to compare — the two systems had trouble even identifying which variables corresponded — with edge cases everywhere (housing benefit interacting with legacy benefits, Scotland-specific provisions, transition rules for households moving between programs) [@hmt2025policyengine].
- Lesson: validating against a government model is hard not because the arithmetic is difficult but because two systems can define "income," aggregate units, and handle household composition in quietly incompatible ways.
- Volunteered structural limitation: PolicyEngine runs on household survey data while governments run on administrative tax records; surveys under-sample the very rich (the CPS might hold a few hundred households above $500,000 where the IRS has vastly more), and because high earners generate a disproportionate share of revenue, that sampling gap cascades into totals.
- PolicyEngine's revenue estimates ran about a third below official ones (uncited — recurs in ch 6 with a [VERIFY] marker).
- This revenue gap was a structural constraint of survey-based microsimulation, not a code bug; the team learned to lead with relative impacts (change against current law), because the survey's sampling error moves baseline and reform alike and largely cancels.

### From tool to infrastructure
- In 2024 the National Science Foundation awarded PolicyEngine a Pathways to Enable Open-Source Ecosystems (POSE) grant [NEEDS CITATION: NSF POSE award].
- In April 2024, PolicyEngine launched income tax modeling for all fifty states and DC, the work of more than a hundred open-source contributors [NEEDS CITATION: contributor count].
- The 50-state push required finding a local-expertise contributor for each missing state or recruiting an engineer to parse an unfamiliar code, then validating each implementation against whatever official calculator or published table existed; flat-tax states with a handful of credits took days, while New York, California, and Hawaii took weeks of iterative debugging (uncited).
- In August 2025 PolicyEngine launched the Enhanced Current Population Survey, integrating five datasets and calibrating to 9,168 administrative totals; the pipeline paired Quantile Regression Forests for imputation with gradient-descent reweighting and cut deviations from official statistics by 97 percent [@policyengine2022enhanced].
  - Carried marker (HTML comment in source): `[VERIFY: citation key year mismatch policyengine2022enhanced]`.
- That data line was later rebuilt as populace, described as the open commons of calibrated microdata the book returns to.
- In September 2025 PolicyEngine signed a memorandum of understanding with the National Bureau of Economic Research to build an open-source emulator of TAXSIM, the tax calculator that had powered academic research since the 1970s; more than 1,200 papers had relied on it [NEEDS CITATION: TAXSIM paper count].
- Daniel Feenberg, TAXSIM's creator, joined PolicyEngine's advisory board and served as external mentor under the NSF grant (uncited).
- Purpose of the emulator: partly to guarantee researchers keep TAXSIM's capabilities, partly to build a framework in which several independently developed models could cross-check one another.
- A month later (October 2025), PolicyEngine signed a second MOU with the Federal Reserve Bank of Atlanta (Atlanta Fed naming is author-approved per `reviews/2026-07-10T1227/rewrite-facts.md`; keep partner and program names as facts).
- The Atlanta Fed's Policy Rules Database covered benefits — SNAP, Medicaid, housing vouchers, childcare subsidies — complementing TAXSIM's focus on taxes.
- The Policy Rules Database powered the Atlanta Fed's CLIFF tools, which Colorado's Workforce Development Council and New Mexico's Caregivers Coalition used to help families understand how earning more would affect their benefits.
  - Carried marker (HTML comment in source): `[VERIFY wording vs MOU at copyedit]`.
- Three-way validation rationale: with three independently developed models (PolicyEngine, TAXSIM, the Policy Rules Database), agreement builds trust and divergence isolates where a discrepancy originates and surfaces genuine questions of policy interpretation.
- Positioning: PolicyEngine as an integrator that could cross-validate across Python and R, across taxes and benefits, across academic and government implementations.
- In March 2025, HM Treasury published an Algorithmic Transparency Record disclosing that it had piloted PolicyEngine UK as a possible supplement to IGOTM, the closed model that had produced government policy estimates for decades [@hmt2025policyengine].
- The Treasury singled out PolicyEngine's machine-learning approach to survey error — combining multiple years of the Family Resources Survey, imputing missing income with random forests, reweighting households with gradient descent — the same techniques built for the Enhanced CPS, now under evaluation inside the government [@hmt2025policyengine].
- The Times reported that the tool could more accurately predict the outcomes of ministers' decisions and was expected to be used mainly in budget periods [@hmt2025policyengine]. (Reported/paraphrased in the source, not a verbatim Times quotation.)
- Nikhil Woodruff, PolicyEngine's co-founder, has since joined the UK government at 10 Downing Street [VERIFY with Nikhil: role wording]. (Narrative beat: the co-founder recruited off a subreddit now works inside the government machinery an outside tool helped open. Per the fact sheet, use with a disclosure at first mention.)
- Significance stated: government microsimulation had been closed by default (proprietary code, restricted data, non-reproducible results); an outside model good enough for the Treasury to pilot weakened the case for keeping the models closed.

### Rules, data, and prediction (the separability hinge)
- Status by late 2025: the tool was real but unfinished — household calculations sharp, unusual cases still exposing gaps, revenue still running below official totals.
- Central distinction the build produced: a policy question that looks like one question is really three, and they come apart the moment you try to compute them —
  1. What does the law say? (exact tax owed and benefit due for a specific household, place, and year)
  2. Who are the people? (how many households look like that one, and how they sum to a country)
  3. What will happen? (behavioral response, economic movement, how next year differs)
- Each of the three is answerable and checkable, but against a different kind of truth and on a different clock:
  - An encoded rule is right or wrong against the statute and against another calculator built from the same statute — provable to the dollar.
  - A population estimate is right or wrong against a survey and against administrative totals — calibrated, with residual measured.
  - A prediction is right or wrong only when the future arrives and the official number lands — committed, then graded.
- The team ran all three inside one engine and one organization because that is how the tool grew, but the seams were visible: the revenue gap was a data problem, not a rules problem; the rules stayed exact precisely where the data was uncertain; behavioral responses belonged to neither.
- Framing for what follows: what was built as one thing is underneath three things, each buildable, checkable, and trustworthy on its own terms; pulling them apart comes later, but first the engine must show what it can do for a single household and then for a country.

---

## Story beats

- **UBI Center → PolicyEngine origin arc.** The author's inability (from 2019) to answer a basic UBI question with any public tool drives the founding of the UBI Center (2019), the partnership with Nikhil Woodruff, the OpenFisca UK model (late 2020), and the decision to put microsimulation in a browser — which becomes PolicyEngine. This chapter owns the origin story.
- **Recruiting a co-founder off a subreddit.** Nikhil Woodruff, a UCL maths/CS undergraduate recruited via Reddit, is the stronger engineer; the arc closes with him joining the UK government at 10 Downing Street [VERIFY with Nikhil: role wording].
- **UK launch, September 2021 / US launch, March 2022.** Two dated launch milestones anchor Part II's chronology; the UK Autumn Budget same-day Universal Credit analysis is the first "we shipped analysis while the news was live" beat.
- **The overwhelmed two-person operation.** When the Autumn Budget analysis went viral, PolicyEngine was two people with a model — fielding interview requests with one hand and patching traffic-broken code with the other.
- **The legislative-staff-arriving-at-CBO-prepared vignette.** A congressional aide uses PolicyEngine to refine a child tax credit proposal for distributional impact before requesting a formal CBO score, walking in with a proposal already refined instead of leading with "what does this cost?"
- **Product becomes infrastructure.** The Fund for Guaranteed Income and other developers build on the API rather than the website; "we had set out to build a product and were turning into infrastructure."
- **"And then came the UK" — the HM Treasury pilot beat.** March 2025 Algorithmic Transparency Record; the outside tool the Treasury tested against its own closed IGOTM model; the arc's payoff that "in 2019 I couldn't find a tool… by 2025, HM Treasury was piloting one we had built."
- **The validation-discrepancy detective beat.** The 21.60-vs-21.06 EITC transposition catch and the running log of ambiguous-rule cases dramatize the three-way "whose bug is it?" question.

---

## Quotes

Verbatim quoted strings and attributed material in this chapter (note: most of the chapter's memorable lines are the author's own — those are in Author-texture, not here):

- PolicyEngine mission statements, quoted in text: **"make everyone a policymaker"** (original) shifting to **"help people understand and change public policy"** (after the October 2021 nonprofit spin-out). Attribution: PolicyEngine's own mission statement.
- Regulatory phrasing quoted as an example of ambiguity: income figured **"net of applicable deductions."** Attribution: unnamed regulation (illustrative).
- The framing question staff used to lead with at CBO: **"what does this cost?"** Attribution: author's characterization of congressional-staff practice.
- The Times, reported (not verbatim): that PolicyEngine UK "could more accurately predict the outcomes of ministers' decisions and was expected to be used mainly in budget periods." Attribution: The Times, via [@hmt2025policyengine]. Flag: paraphrased in the source; no verbatim Times wording is present to quote.

---

## Arguments

Numbered propositions this chapter advances:

1. **The API was the product; the web app was merely its first consumer.** Making the model usable without the interface — overengineering at the time — is what later let developers put PolicyEngine's numbers inside their own tools.
2. **Openness plus nonprofit structure is a trust mechanism, not just a license choice.** Open code anyone can inspect, plus no shareholders whose interests could bend results, is what lets ideologically opposed users trust the same engine.
3. **US complexity is multiplicative, not additive.** Fifty state codes layered on a complex federal system with agency-scattered benefits, each with its own income definition and household unit, compounds rather than adds.
4. **Open-source contribution scales with contributor geography, not policy importance.** The volunteer PR model covers where a local expert volunteers and leaves gaps where none does — a structural limit of enthusiasm-driven coverage.
5. **Inspection is not correctness.** Open code is necessary but not sufficient; validation against official calculators and test suites is what tests correctness, and every discrepancy is a three-way question (our bug / their bug / ambiguous rule).
6. **Validating against a government model is hard for definitional, not arithmetic, reasons.** Two systems can define "income," aggregate units, and treat household composition in quietly incompatible ways.
7. **The revenue gap is a data problem, not a rules problem.** Survey microdata under-samples the very rich, so absolute revenue totals run ~one-third low; relative impacts are more trustworthy because sampling error largely cancels across baseline and reform. (Only better data — not better code — can close it.)
8. **An outside model good enough for the government to pilot weakens the case for closed models.** Partial open reproduction of internal estimates puts pressure on closed-by-default government microsimulation.
9. **A policy question is really three separable concerns with three different verification loops and three different clocks** (rules vs. statute, now; data vs. administrative totals, now; prediction vs. the future, later). This is the chapter's central analytical payoff and the hinge into the book's decomposition.

---

## Author-texture (verbatim, may be reused)

Passages with the author's hand — first-person, time-anchored, or rhetorically load-bearing. Selective.

- Opening line: "For a few years around the turn of the decade, open-source policy modeling went through a quiet boom—and I spent most of it unable to answer a simple question."
- The naming beat: "We called it PolicyEngine."
- The multiplicative-vs-additive complexity line: "Modeling the US wasn't harder than modeling the UK by some constant factor; the complexity grew multiplicatively rather than additively."
- The product-to-infrastructure line: "We had set out to build a product and were turning into infrastructure."
- The pivot beat: "And then came the UK."
- The subreddit-to-government line: "…the co-founder I had recruited off a subreddit, now working inside the machinery an outside tool had helped pry open."
- The bookend on the founding frustration: "In 2019 I couldn't find a tool to answer a basic question about a universal basic income; by 2025, HM Treasury was piloting one we had built." (Paired earlier with: "What I couldn't find in 2019, we had built by 2024.")
- The "two people with a model" image: "…we weren't a media operation—we were two people with a model, fielding interview requests with one hand and patching the code the traffic had broken with the other."
- The closing distinction: "Three concerns, three verification loops, three different clocks."

---

## Structural notes

- **Chapter's job (from the from-scratch outline, ch 5).** Tell the UBI Center → PolicyEngine origin, the UK launch, the HM Treasury pilot, the US expansion, and what "open" bought and cost. Nikhil's arc threads through here. The chapter **owns the origin story only** — later chapters must not re-tell it.
- **New ending / cross-reference.** Replace the old ch-5 ending ("sustainability is the unsolved problem → ch 10") with the real hinge: building the tool proved that rules, data, and prediction are **separable concerns**, which is what makes the later recomposition possible. This separability hinge is **paid off in ch 12 (The decomposition)** — keep the seam explicit here and let ch 12 deliver it.
- **De-duplication ownership (Part II).** Prior review found the mini-budget beat told four times and MyFriendBen twice across Part II. Assignment: **ch 5 owns origin; ch 6 owns MyFriendBen and the case studies.** Do not import MyFriendBen or the household case studies into this chapter.
- **Cross-chapter repetitions to police (this chapter is a source of each; decide a single home):**
  - Enhanced CPS milestone (August 2025, five datasets, 9,168 administrative targets, ~97% deviation cut) also appears in ch 6 and ch 7. Here it is compressed to the 97% figure; ch 7 carries the fuller "8.3%→0.2%" and names all five datasets.
  - The ~one-third revenue gap also appears in ch 6 (there with a `[VERIFY: reconcile the revenue gap against the populace-calibrated stack]` marker).
  - The HM Treasury pilot / evaluation also appears in ch 6.
- **Naming guardrails carried into this chapter (per rewrite-facts.md).** The data layer is **populace** (never microplex). The **Federal Reserve Bank of Atlanta** naming is author-approved — keep it. Retired names must never appear as current.
- **Markers that must survive the rewrite (resolve, don't delete):** the Tax-Calculator v3.2.1 date [NEEDS CITATION]; the NSF POSE award [NEEDS CITATION]; the >100 contributor count [NEEDS CITATION]; the >1,200 TAXSIM papers [NEEDS CITATION]; the EITC transposition [VERIFY: real incident]; the `policyengine2022enhanced` key-year mismatch [VERIFY]; the Atlanta Fed MOU wording [VERIFY at copyedit]; Nikhil's role wording [VERIFY with Nikhil].

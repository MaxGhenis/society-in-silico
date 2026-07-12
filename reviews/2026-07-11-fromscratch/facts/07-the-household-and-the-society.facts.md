# Fact catalog — Chapter 6: The household and the society

Source: `manuscript/part-2-open-engine/06-the-household-and-the-society.md`
(Chapter 6 in the manuscript; Part II chapter 6 in the from-scratch outline. Output filename offset to `07-…` per the facts-folder convention.)

Extraction rules applied: every claim below is paraphrased except where marked as a quote, code block, or author-texture. Citation keys `[@key]` are preserved exactly and placed with their facts. `[NEEDS CITATION: …]` and `[VERIFY: …]` markers are carried verbatim. Specific claims (dates, counts, dollar figures, rates, named attributes) with no citation key and no marker are flagged `(uncited)`.

---

## Facts

### Opening scenario and the household calculator
- Framing case: a single parent in New York with one child who has a disability, earning $30,000 a year — how much do they owe in taxes, how much do they receive in benefits, and what happens if they take an extra shift? (illustrative scenario, uncited).
- The answer runs through federal income tax, state income tax, payroll taxes, the EITC, the Child Tax Credit, Supplemental Security Income, SNAP, and a dozen other programs, each with its own income definition, household unit, and phase-out schedule, none designed to fit together.
- This is the problem PolicyEngine's household calculator was built to solve [@policyengine2022ssi].

### What you owe, what you get
- A typical low-income family might simultaneously draw on the EITC, a partially refundable Child Tax Credit, SNAP, SSI for a disabled member, Medicaid, a housing voucher, a state child-care subsidy, and free school meals — eight programs, each written independently with its own idea of income and its own household unit (uncited).
- Consequence of fragmentation: caseworkers specialize in one program, tax preparers work one side of the ledger, benefits counselors know eligibility but not tax consequences; the fragmentation is why eligible families leave benefits unclaimed and why a raise can quietly cost more than it pays.
- The calculator's promise: enter your circumstances and it shows taxes and benefits together under current law — walking through household composition (adults, children, ages), then income (wages, self-employment, investment, retirement), then specifics (housing cost, child-care expense, disability), and computing dozens of outputs including a single net figure for what the family keeps [@policyengine2022review].
- Coverage: PolicyEngine's US model spans federal income and payroll taxes, the EITC and CTC, SNAP, SSI, WIC, TANF, and dozens of state programs; the UK model spans income tax, National Insurance, Universal Credit, Child Benefit, and the full run of means-tested support. Each program is a separate module drawn from statute, regulation, and agency guidance.
- Why comprehensiveness matters: programs interact (a family's SNAP benefit depends on net income after taxes and deductions; its tax depends on credits tied to the same children who might also generate SSI or a child-care subsidy), so changing one input ripples across the others — captured only by evaluating every program at once for the same household.

### Rates above a billionaire's (marginal-rate mechanics)
- Plotting a household's net income against its earnings reveals hidden structure: for many low-income families the line has flat stretches (more work barely raises take-home pay) and vertical drops — cliffs — where crossing a threshold loses a benefit worth more than the raise [@policyengine2023cliffs].
- A cliff is the point where earning more leaves a household worse off, because benefits withdrawn plus taxes owed on the next dollar exceed the dollar.
- As the New York parent's earnings climb from $20,000 toward $30,000, SNAP tapers, the EITC phases out, the child's SSI falls, and income and payroll taxes begin to bite (illustrative, uncited).
- Marginal-rate mechanics (uncited mechanism figures):
  - SNAP withdraws about thirty cents per additional dollar of net income.
  - The EITC phases out at roughly sixteen cents per dollar for a family with one child, and twenty-one cents for two or more.
  - SSI falls by about fifty cents per dollar of countable income.
  - Stacked, the combined marginal rate can approach eighty percent — more than double the ~37 percent top federal rate a high earner pays on his last dollar.
- The counterintuitive claim: a low-income worker often faces a higher marginal rate than any billionaire, because benefit phase-outs stack on top of taxes; this is the ordinary structure of a low-income budget, not an edge case, and it disappears into any average.
- At a true cliff the marginal-rate chart spikes past 100 percent (earning more, keeping less); the calculator shades the earnings "dead zone" where extra work barely moves net income.
- Dual use of that visibility: a family can plan around a cliff, and a policymaker can see work disincentives that programs create only in combination.

### Three worked household cases (surviving from an originally larger set — see Story beats)
- **The SNAP categorical cliff.** Receiving SSI confers categorical eligibility for SNAP (qualifying regardless of the usual income test); once earnings push SSI to zero, categorical eligibility vanishes and the household must suddenly satisfy SNAP's own income test — the cliff landing exactly where someone is trying to become self-sufficient (uncited mechanism).
- **The marriage penalty.** Two single parents, each earning $25,000 with one child, each qualify separately for substantial EITC and CTC; marrying them pushes their combined $50,000 into higher phase-out ranges, so the household can end up with less in total transfers than the two separate households received. The penalty is in no single line of the code; it emerges from programs' different treatment of household structure, and the calculator surfaces it by running the two adults separately and then as one (uncited).
- **The aging-out cliff.** A family receiving SSI for a disabled child hits a discontinuity when the child turns eighteen and SSI stops counting the parents' income and starts counting the child's own — often raising the SSI payment while stripping family-based benefits, as the same birthday moves the child out of pediatric Medicaid provisions, school meals, and child-care subsidies (uncited).

### The what-if machine
- The calculator also edits rules: the policy editor can raise the EITC, smooth a SNAP cliff, add a child allowance, make the CTC fully refundable, set a universal basic income, or flatten the income tax; baseline shows in gray, reform in blue, and the dead zones and marginal-rate spikes redraw (uncited feature description).
- Charts update live: two net-income lines, two sets of dead zones, and stacked marginal-rate curves showing where a reform flattens the benefit system and where it carves a new cliff.
- Under 2026 law the Child Tax Credit is $2,200 per child [@obbba2025]; any reform is measured against that.
- Worked 2021 CTC example (author's illustration, uncited): in 2021 Congress temporarily raised the credit to $3,600 for children under six and $3,000 for those six to seventeen, and made it fully refundable. For a single parent earning $15,000 with two young children, the engine computes roughly $1,800 under the old rules (held down by the phase-in on earnings above $2,500) against $7,200 under the expansion; when the expansion lapsed at the end of 2021, that family's income fell by more than $5,000.
- Policy-design use: rather than propose a reform and wait weeks for a score, a legislative aide can model dozens of variants in an afternoon (benefit at $3,000 vs $4,000 per child, phase-in from the first dollar or from $2,500, cap at $75,000 or $150,000), reading a different household chart for each (illustrative).

### Where the system is most complex (UK / Universal Credit)
- The household calculator originated in the UK, where PolicyEngine launched in 2021 before crossing to the US [@ubicenter2021policyengine]; the household view is most powerful where the system is most tangled.
- Universal Credit was meant to simplify welfare by folding six legacy benefits into one, but its taper (the rate at which the award is withdrawn as earnings rise) interacts with income tax, National Insurance, and council-tax support to push some working families' marginal rates above 70 percent (uncited).
- When Chancellor Rishi Sunak cut the UC taper from 63 to 55 percent in the Autumn 2021 Budget (with a £500/yr work-allowance increase), the tool could show household-by-household effects [@policyengine2021uctaper]: a single parent working 25 hours a week at minimum wage would keep about £1,000 more a year [NEEDS CITATION: the specific £1,000/single-parent-at-25hrs figure is NOT in PolicyEngine's UC-taper post; recompute and cite, or soften — the nearest official comparator is HMT/HoC Library "~£1,200/yr for a single parent of two on the NMW," a different household spec], while a two-earner couple would gain less. (Reform cited to @policyengine2021uctaper: taper 63→55%, cost £2.8bn/yr, poverty −3.1%; the £1,000 household figure marker stays open — see research/part2-verification.md.)
- HM Treasury later published a formal evaluation benchmarking PolicyEngine UK against its own internal models [@hmt2025policyengine] — a research prototype the government took seriously enough to test against its own machinery.

### From calculator to primitive
- Every household calculation carries a caveat shown plainly: PolicyEngine provides estimates, not benefit determinations [@policyengine2022ssi]. The model encodes rules as written; an actual determination turns on discretion, documentation, asset tests, and local variation.
- The team validates continuously against official calculators and published tables [@policyengine2024ukvalidation] and treats every discrepancy as a bug to investigate, while admitting perfect accuracy in a system this complex is unattainable and that claiming it would be worse than naming the gap.
- In 2025 MyFriendBen, a benefits-screening service, launched in North Carolina, Illinois, Colorado, and New York on PolicyEngine's API [@policyengine2025myfriendben]: plain-language questions in a dozen languages, with a household learning in about six minutes which programs it likely qualifies for.
- In Colorado, MyFriendBen users surfaced an average of $1,500 a month in benefits they appeared eligible for but had not claimed [@myfriendben2025pueblo].
- PolicyEngine's own note reported that the estimates matched expected amounts more than 90 percent of the time — flagged in the text as a self-reported figure, not an independent audit [@policyengine2025myfriendben].
- A prototype reframes the whole calculation around life events — a birth, a move, a marriage, a job loss, turning 65 — because that is how people meet policy [@policyengine2026crossroads].
- The household view is a "primitive" in two senses: (1) the basic computation that benefits screening, financial coaching, guaranteed-income design, and legislative analysis all separately need; and (2) the atomic unit of ground-truth verification — the level at which an encoded rule can be proven against a reference calculator or a real determination. A national estimate is a weighted sum of household calculations, so if the household calculation is wrong, everything above it is wrong in ways no aggregate reveals.
- Bridge to the society view (illustrative contrast, uncited): a macroeconomic model might say a tax cut costs $100 billion and lifts GDP by 0.3 percent; microsimulation can add that the same cut hands $12,000 to a high-income household in Connecticut and $200 to a low-income household in Mississippi — and that the Mississippi family now faces a higher marginal rate because the cut nudged it into a phase-out.

### From one household to many (lineage and weighting)
- Lineage: in 1974 Joseph Pechman and Benjamin Okner of Brookings published *Who Bears the Tax Burden?*, the first comprehensive attempt to allocate US tax burdens across the income distribution using household-level data [@pechman1974taxburden].
- Pechman and Okner merged records for 72,000 households and found the system roughly proportional across most of the distribution — a result that irritated partisans on both sides (challenging conservatives who called it too progressive and liberals who called it too regressive) [@pechman1974taxburden].
- Their method — running micro-data through incidence assumptions — became the template for distributional analysis at Treasury's Office of Tax Analysis, the Joint Committee on Taxation, and the CBO.
- You cannot survey everybody: the monthly Current Population Survey samples about 60,000 households [@census2024cps]; its Annual Social and Economic Supplement (the income workhorse) reaches roughly 75,000 to 90,000 households — either way a sliver of some 130 million American households. (ASEC figure corrected from "roughly 100,000" per primary source — the current ASEC sample is ~75,000–90,000; "100,000" reflected the pre-2014 expanded-sample era. See research/part2-verification.md correction C5.)
- Each surveyed household carries a weight saying how many others it stands in for (a rural Wyoming household might represent 5,000, a Manhattan one 500) — weights the Census computes to correct for sampling design and nonresponse (uncited example figures).
- To score a reform, the engine computes the change for each sampled household, multiplies by its weight, and sums across the sample.

### The data underneath
- The survey biases the answer rather than merely blurring it: high incomes are top-coded and under-reported; benefits are undercounted — Bruce Meyer and colleagues found that 40 to 50 percent of SNAP recipients do not report their benefits, with the problem running across programs [@meyer2015underreporting]; the sample is too thin for most state-level work; and asset questions are sparse.
- Direction of bias: survey-based scores tend to understate both the cost of reforming means-tested programs and the revenue from taxing top earners, because the data undercounts exactly the benefits and incomes in play.
- The fix is to calibrate the survey to administrative reality. PolicyEngine's earlier public milestone was the Enhanced CPS, released in August 2025: five datasets integrated, reported taxes and benefits replaced with computed amounts for internal consistency, income distributions corrected against IRS records, and survey weights re-solved to match 9,168 administrative totals — cutting deviations from those targets by about 97 percent. **[VERIFY: publish or soften]** — the 9,168-targets and 97% figures are author-internal, August-2025 populace-era numbers that are not publicly verifiable; the previously cited `[@policyengine2022enhanced]` (a Dec 2022 post) predates and does not contain them, so it was removed. See research/part2-verification.md correction C6.
- That work has since been folded into populace, a calibrated-microdata commons that treats data construction as shared infrastructure: synthesize records where the survey is thin, impute missing variables with quantile-regression forests [@microimpute2026], calibrate weights to administrative aggregates [@microcalibrate2026], and publish certified releases like versioned software builds.
- Local-area analysis becomes a matter of filtering one national calibrated dataset rather than building fifty bespoke ones.

### Cost, poverty, and who gains
- PolicyEngine scores a reform by running two simulations across the weighted sample — one under current law, one under the reform — and summing the difference in tax revenue and benefit spending [@policyengine2023scoring].
- Each of the roughly 100,000 records in PolicyEngine's enhanced microdataset (distinct from the raw ~75,000–90,000-household ASEC sample) triggers thousands of eligibility checks and bracket calculations, yet the whole run finishes in seconds. (Clarified per research/part2-verification.md C5: this "100,000" is the enhanced dataset's record count, not the survey sample.)
- Scores are static by default (behavior held fixed); layering in labor-supply elasticities can pull an estimate down (people assumed to work more) or push it up (work less) — one reason two honest analysts can publish different numbers for the same bill.
- A single cost figure hides its contingency on the scoring year, on whether behavior is allowed to respond, and — most subtly — on the baseline compared against, which can swing estimates by hundreds of billions.
- Before July 2025, scoring an extension of the 2017 tax cuts meant first deciding whether the baseline assumed the individual provisions would expire on schedule or continue — an assumption worth hundreds of billions before any policy changed; OBBBA settled that by making the provisions permanent [@obbba2025].
- **CTC full-refundability score (author's own calculation):** removing the refundable cap and the earnings phase-in so families who owe no federal income tax receive the whole credit, scored against 2026 law (credit $2,200 per child [@obbba2025]): the net cost is roughly $23 billion for 2026, and child poverty falls by about 2.6 percentage points — on the order of 1.9 million children.
  - Provenance (HTML comment carried in source, load-bearing): "Author's calculation: PolicyEngine US 1.768.3, dense Enhanced CPS, static score, fully_refundable=True from 2026; matches chapter 13's figure by construction; rerun at publication data vintage."
  - Note for the rewriter: the chapter text states the delta (−2.6pp, ~1.9M children); the from-scratch brief expresses the same result as an absolute child-poverty move of ~16.6% → 14.0%. Use the chapter's delta form unless the rescore run supplies fresh endpoints.
- Distributional shape of that reform: the families who gain are those whose credit currently exceeds the income tax they owe (low- and moderate-income working families with children, who forfeit part of the credit today); higher-income households already claiming the full credit see nothing change.
- Poverty measurement: PolicyEngine uses the Supplemental Poverty Measure, which (unlike the older official measure) counts taxes and in-kind benefits like SNAP, adjusts for geographic housing-cost differences, and nets out work and medical expenses; for two adults and two children renting, the 2024 SPM threshold is about $39,400 [@bls2024spm].
- In a 2023 analysis, PolicyEngine put roughly 9.6 percent of Americans below their threshold, with children poorer than working-age adults and seniors, and women poorer than men [@policyengine2023sex] [VERIFY: date this estimate's vintage and reconcile with the Census official SPM of ~12.4% for 2022 [@census2023spm]]. (The official SPM was 12.4% in 2022 (up from 7.8% in 2021) — the gap to PolicyEngine's ~9.6% is real; pin the estimate's data vintage. Marker stays open — see research/part2-verification.md.)
- WIC case (demographic unevenness): it lowers overall poverty by about 0.8 percent and deep poverty by 2.2 percent, but child poverty by 2.6 percent, and women's poverty by 0.9 percent against men's 0.7 — a program that looks gender-neutral on its face landing unevenly once the microdata is split [@policyengine2023sex].
- Distributional cuts available: share of each income decile that gains or loses; the same cut by wealth decile using imputed wealth, by age, by sex, by geography, and by race where the data supports it [@policyengine2023scoring].
- Inequality measures: the Gini coefficient is standard but most sensitive to the middle of the distribution, so a reform transforming the very bottom can barely move it; the Atkinson index, tuned by an inequality-aversion parameter, weights the bottom more heavily and responds more to anti-poverty reforms; the two can disagree instructively.

### Neutrality
- PolicyEngine reports outcomes (budget, poverty, inequality, distribution across several cuts) and lets users weigh what they value; it adds no editorial verdict, documents its behavioral assumptions and data limits, and keeps its methodology open to challenge.
- The neutrality is deliberate and imperfect: the choice of what to display is itself normative (showing a poverty rate implies poverty matters; framing by income decile frames the debate a particular way). The honest claim is not perfect neutrality but a deliberate separation of analytical infrastructure from advocacy.

### Where the numbers are solid, and where they're soft
- Society-level estimates carry more uncertainty than household ones (weighted sample, imputed variables, compounding interactions).
- Household calculations are the most reliable output, because they depend on the encoded rules rather than the data distribution: for a family with stated characteristics, the answer is only as good as the statute encoding, no better or worse for the survey behind it.
- Directional and comparative results are nearly as solid (whether a reform helps low-income families more than high-income ones; whether Reform A costs more than Reform B), because distribution shapes and reform ratios hold steadier than absolute levels and the same data limits press on both sides of a comparison.
- Absolute budget scores deserve the most caution: PolicyEngine's aggregate revenue estimates have historically run well below official totals — by roughly a third [VERIFY: reconcile the revenue gap against the populace-calibrated stack] — because survey microdata undercounts top incomes and underreports benefits, and a static model omits behavioral and macroeconomic feedback.
- For an order-of-magnitude figure or a cross-reform comparison that is good enough; for a precise revenue estimate, the Joint Committee on Taxation and the CBO remain the standard, because they work from confidential tax returns that capture the whole income distribution.
- Calibration is validated by holding out some administrative targets and checking the reweighted sample against them — the same procedure that cut deviations by about 97 percent — but even a 97 percent improvement from a large gap still leaves a meaningful gap. Open models expose their limits where closed ones hide behind institutional authority.

### Analysis as infrastructure
- The society view enables a response to a policy proposal while the proposal is still live; traditional analysis takes weeks or months (read the legislation, code it, run the model, write it up, clear review), by which time the legislative moment may have passed.
- The model's speed comes from pre-investment: building and maintaining the engine takes years, but once it exists, scoring a new reform takes hours because the fixed cost is already paid.
- When analysis is a one-time product (a think-tank report), the argument is whether to trust that report; when analysis is infrastructure anyone can run (web app, Python package, API), the argument shifts to whether the underlying model is sound — a more productive fight, because model quality is testable and improvable in ways a report's credibility is not.

### Two reforms, seen clearly
- **2021 Child Tax Credit expansion (US).** The American Rescue Plan raised the credit and, more consequentially, made it fully refundable, removing the earnings phase-in that had excluded the poorest families, and paid half of it out in monthly installments from July through December (uncited detail).
  - Before enactment, Columbia University's Center on Poverty and Social Policy projected the broader relief package could cut child poverty by more than half [@columbia2021ctc].
  - After enactment, SPM child poverty fell from 9.7 percent in 2020 to 5.2 percent in 2021, a record low [@census2022spm].
  - The credit as a whole kept 2.9 million children out of poverty that year; the expansion alone accounted for 2.1 million of them [@census2022childpoverty; @census2022ctcimpact] — two numbers the debate routinely conflates and the microdata keeps distinct. (Census SEHSD-WP-2022-24 added as a stronger primary source per research/part2-verification.md: CTC lifted 5.3M people incl. 2.9M children; the expansion alone lifted 2.1M children.)
  - The one-year cost ran to roughly $105 billion [NEEDS CITATION: annual cost of the 2021 ARP CTC expansion].
  - When the expansion expired in January 2022, Columbia tracked child poverty nearly doubling within months (uncited; attributed to Columbia).
  - Distributional subtlety: because the expansion also raised the maximum credit for every eligible family, distributional tables showed the largest percentage gains at the bottom but real dollar gains further up — whether that read as a broad coalition or as loose targeting depended on values the model could not adjudicate.
- **September 2022 UK "mini-budget."** Chancellor Kwasi Kwarteng's mini-budget (under PM Liz Truss) proposed abolishing the 45p additional rate of income tax, cutting the basic rate, and reversing a National Insurance rise, in the name of growth (uncited detail).
  - PolicyEngine UK published household-level distributional analysis on 23 September 2022, the day of the mini-budget — among the only independent estimates available in the critical first days — showing the package overwhelmingly favored high earners, the top decile gaining about £2,738 a year (2.5 percent) while the bottom gained about £45 (0.4 percent) [@policyengine2022growthplan]. (Figures corrected from "about £2,500 … almost nothing" and re-cited to the same-day Growth Plan post per primary source — see research/part2-verification.md correction C4; also: Gini +1.2%, top-1% share +2.2%.)
  - Media outlets cited it; within weeks the government reversed the 45p abolition, and within a month the prime minister had resigned (uncited).
- **UC taper cut, as contrast.** The same UC taper cut from 63 to 55 percent: the taper cut reached only working recipients, while the pandemic's £20-a-week uplift had reached everyone on Universal Credit, so per pound the uplift cut poverty roughly 40 percent more effectively [NEEDS CITATION], even as the taper cut improved work incentives, dropping the share of workers facing marginal rates above 70 percent from 26 to 9 percent [NEEDS CITATION]. Two policies, similar budgets, opposite distributional signatures.
- By 2026 the infrastructure began watching legislation as it moved, flagging which bills the model could already handle and routing the rest toward encoding [@policyengine2026statelegtracker] — the on-ramp to encoding the policy corpus at scale (subject of Part III).

### One engine, three ingredients
- Both the household view and the national estimate run on one engine — the same computation at two scales — and it works only because three things beneath it hold: the rules encoded correctly, the data representing the people, and the behavior (the seam where the model stops describing the law and starts predicting how people respond) handled honestly.
- Those are the three ingredients of any microsimulation; the next chapter takes them one at a time.

---

## Story beats

- **The New York single-parent opening scenario.** A single parent in New York with one disabled child earning $30,000 — owe how much, receive how much, what happens on an extra shift? — is the chapter's cold open and the recurring test case for marginal-rate mechanics and the aging-out cliff. This household is the chapter's spine.
- **The what-if machine.** The scene where a reader opens the policy editor, changes a rule (raise the EITC, add a child allowance, make the CTC fully refundable, set a UBI, flatten the tax), and watches the gray baseline and blue reform lines redraw for their own household — "it's your life, under different rules."
- **The six worked household cases (three survive in the current draft).** The chapter's benefit-trap gallery originally ran to six worked cases; the current draft keeps three: (1) the SNAP categorical cliff, (2) the marriage penalty, (3) the aging-out cliff. Rewriter note: this chapter **owns** these case studies (see Structural notes); the other three cases have been cut and should not be reintroduced without a source.
- **MyFriendBen — the $1,500/month beat, with its hedge.** The 2025 launch across NC/IL/CO/NY on PolicyEngine's API; the ~six-minute screening in a dozen languages; the Colorado finding that users surfaced an average of $1,500/month in unclaimed benefits; and, critically, the hedge — PolicyEngine's own note put the match rate above 90 percent, explicitly labeled self-reported, not an independent audit. This chapter **owns** MyFriendBen.
- **The Truss/Kwarteng mini-budget, same-day analysis beat.** September 2022: PolicyEngine UK publishes distributional analysis within hours, among the only independent estimates in the first days; media cite it; the 45p reversal and the prime minister's resignation follow. (Prior review flagged this beat as told four times across Part II — it is owned here.)
- **Pechman and Okner, 1974.** The origin scene for distributional analysis: *Who Bears the Tax Burden?*, 72,000 merged household records, the "roughly proportional" finding that annoyed both sides, and the method that Treasury/JCT/CBO still use.
- **The two-reforms diptych.** The 2021 CTC expansion (predictions landed because the policy worked through mechanical, low-behavioral-uncertainty channels) set against the UK mini-budget and the UC taper (same budgets, opposite distributional signatures) — the chapter's demonstration of what the society view catches and what goes dark without it.

---

## Quotes

This chapter's most memorable lines are the author's own (see Author-texture). Verbatim/attributed external material is thin:

- Book title, quoted and attributed: *Who Bears the Tax Burden?*, Joseph Pechman and Benjamin Okner, Brookings, 1974 [@pechman1974taxburden].
- Product caveat, quoted as the calculator's standing disclaimer: "PolicyEngine provides estimates, not benefit determinations" [@policyengine2022ssi]. (Rendered as a plain statement in the source, not in quotation marks; treat as the product's own caveat text.)
- The two framing questions that separate the views: the household view answers "what would this mean for me?"; the society view answers "what would this mean for everyone?"
- MyFriendBen match-rate figure, quoted with its hedge: estimates "matched expected amounts more than 90 percent of the time — a self-reported figure, not an independent audit" [@policyengine2025myfriendben]. (The hedge is part of the claim — carry it.)

---

## Arguments

Numbered propositions this chapter advances:

1. **The household calculation is the atomic unit of ground-truth verification.** A national estimate is nothing but a weighted sum of household calculations; if the single-family calculation is wrong, every aggregate built on it is wrong in ways no aggregate reveals. Getting one family right is what makes country-level numbers mean anything. (This is the chapter's new bridge sentence per the outline.)
2. **A low-income worker can face a higher marginal rate than any billionaire.** Stacked benefit phase-outs (SNAP ~30¢, EITC ~16¢/21¢, SSI ~50¢) plus taxes can approach ~80 percent, more than double the top federal rate — and this is the ordinary structure of a low-income budget, invisible in any average.
3. **Comprehensiveness is not a feature but a necessity, because programs interact.** No single-program calculator captures cross-program ripples; only evaluating every program at once for the same household does.
4. **The household view is a primitive in two senses** — the shared basic computation many applications need, and the level at which encoded rules are provable against an oracle or a real determination.
5. **Neutrality is deliberate but impossible to perfect.** The tool adds no verdict and documents its assumptions, but the choice of what to display is itself normative; the honest claim is separation of analytical infrastructure from advocacy, not perfect neutrality.
6. **Reliability is tiered.** Household calculations are most reliable (they depend on encoded rules, not the data distribution); directional/comparative results are nearly as reliable; absolute budget scores deserve the most caution — the aggregate revenue gap runs ~one-third low, and even a 97 percent calibration improvement from a large gap still leaves a meaningful gap.
7. **Open models expose their limits; closed models hide behind institutional authority.** The knowability of a model's limits, not exact match to reality, is the standard.
8. **Predictions land closest where policy works through mechanical channels.** The 2021 CTC forecasts held because direct cash on simple eligibility rules carries low behavioral uncertainty — microsimulation's best case — whereas high-end tax changes turn on behavioral assumptions the data cannot pin down.
9. **Analysis-as-infrastructure changes the debate from "trust this report" to "is the model sound?"** — a more productive and testable question, and one that lowers the marginal cost of each new analysis to hours because the fixed cost is pre-paid.
10. **A cost figure is meaningless without its distribution and its baseline.** The same $50 billion concentrated on families in poverty is a different policy from $50 billion spread evenly; and baseline choice alone can swing an estimate by hundreds of billions.

---

## Author-texture (verbatim, may be reused)

Passages with the author's hand — selective:

- The cold-open pressure: "No one can calculate this in their head. Most accountants would struggle. Yet the answer shapes every financial decision the family makes."
- The billionaire line: "…a low-income worker often faces a higher marginal rate than any billionaire, because benefit phase-outs stack on top of taxes."
- The hedge-fund comparison: "Stack them and the combined rate can approach eighty percent — more than double what a hedge-fund manager pays on his last dollar."
- The what-if payoff: "It's your life, under different rules."
- The primitive framing: "The household view, it turned out, was a primitive — and in two senses at once."
- The verification bridge: "A national estimate is nothing but a weighted sum of household calculations; if the household calculation is wrong, everything built on top of it is wrong in ways no aggregate will reveal."
- The neutrality couplet: "PolicyEngine does not tell you which of those to prefer. It tells you what the outcomes are."
- The macro-vs-micro contrast: "A macroeconomic model might say a tax cut costs $100 billion and lifts GDP by 0.3 percent. Microsimulation can say that and also tell you the same cut hands $12,000 to a high-income household in Connecticut and $200 to a low-income household in Mississippi…"

---

## Structural notes

- **Chapter's job (from the from-scratch outline, ch 6).** Merge the calculator view and the population view into one chapter: marginal rates, benefit cliffs, distributional analysis, budget scoring, and the neutrality challenge (a merge of the old ch 7 + ch 8). The prior review found the mini-budget beat told four times and MyFriendBen twice across Part II — evidence these chapters want to be one.
- **De-duplication ownership.** Per the outline's ownership split: **ch 5 owns the origin story; this chapter (household/society) owns MyFriendBen and the case studies.** Mini-budget ownership DECIDED 2026-07-12: the beat lives in ch 5 ("What open bought"); this chapter keeps only the back-reference plus the Gini/top-1% numbers. (Supersedes the earlier keep-it-here instruction.) Keep the three household case studies here.
- **The required new bridge sentence.** The outline mandates one addition: the household calculation is the **atomic unit of ground-truth verification** — the level at which an encoded rule is provable against an oracle or a real determination. It is present (see Arguments #1) and should survive any rewrite; it is what wires this chapter to Part III.
- **Forward cross-references.** The closing "One engine, three ingredients" hands directly to ch 7 (rules, data, dynamics). The 2026 legislation-tracker beat [@policyengine2026statelegtracker] is an explicit on-ramp to Part III (encoding the corpus at scale).
- **Cross-chapter repetitions to police (shared with ch 5 and ch 7 — pick one home each):**
  - Enhanced CPS milestone (August 2025, five datasets, 9,168 targets, ~97% deviation cut) appears here, in ch 5, and in ch 7. This chapter's version adds the internal-consistency and IRS-correction detail; ch 7 names the five datasets and gives 8.3%→0.2%.
  - The ~one-third revenue gap appears here (with the `[VERIFY: reconcile the revenue gap against the populace-calibrated stack]` marker) and in ch 5.
  - The HM Treasury evaluation appears here and in ch 5.
  - The 2021 CTC expansion appears twice within this chapter (the "what-if machine" worked example and the "two reforms" case) — consolidate or clearly differentiate on rewrite.
- **Naming guardrails (per rewrite-facts.md).** Data layer is **populace** (never microplex). CTC is **$2,200 per child from 2026** under **OBBBA** [@obbba2025]. Keep the CTC-score HTML provenance comment; the figure is the author's own calculation and is flagged to rerun at publication data vintage.
- **Markers that must survive the rewrite (resolve, don't delete):** the UC taper £1,000/year figure [NEEDS CITATION]; the SPM-vintage/Census reconciliation [VERIFY]; the revenue-gap reconciliation [VERIFY]; the 2021 ARP CTC annual cost [NEEDS CITATION]; the two UK-contrast figures (40% more effective; 26→9 percent) [NEEDS CITATION ×2]; and the CTC author's-calculation provenance comment.

# Fact catalog — Chapter 7: The three ingredients

Source: `manuscript/part-2-open-engine/07-three-ingredients.md`
(Chapter 7 in the manuscript; Part II chapter 7 in the from-scratch outline. Output filename offset to `08-…` per the facts-folder convention.)

Extraction rules applied: every claim below is paraphrased except where marked as a quote, code block, or author-texture. Citation keys `[@key]` are preserved exactly and placed with their facts. `[NEEDS CITATION: …]` and `[VERIFY: …]` markers are carried verbatim. Specific claims with no citation key and no marker are flagged `(uncited)`.

---

## Facts

### The framework
- Every microsimulation model rests on three foundations: rules encoding, microdata construction, and behavioral dynamics.
- This three-part framework does not appear explicitly in the microsimulation literature — textbooks organize around techniques, not architecture [@caldwell1996microsimulation] — but it captures what any team building such a model must solve.
- Failure modes: get the rules wrong and calculations are incorrect; get the data wrong and estimates are biased; ignore dynamics and projections miss how people respond.
- PolicyEngine, Tax-Calculator, EUROMOD, and TAXSIM each answer the same three questions differently, and the differences are the most revealing thing about them.
- The three are also separate construction projects that AI agents can increasingly take on: each ingredient is now a layer buildable at a fraction of its former cost, and each is trustworthy only to the degree its output can be checked against something real. (Through-line: a cheaply built layer is worth nothing if you cannot tell whether it is right.)

### Ingredient one: rules
- The first ingredient is encoding policy rules as executable logic — every tax rate, benefit threshold, eligibility condition, and phase-out schedule becoming something a computer can evaluate.
- EITC example of hidden complexity: its phase-in rate depends on the number of qualifying children; "qualifying child" carries its own age, relationship, residency, and joint-return tests; the credit depends on earned income (which excludes some income types and includes others); the phase-out threshold differs for single and married filers; and many states layer their own EITC on top, each with its own conformity rules [NEEDS CITATION: number of states with EITC variants].
- Encoding the EITC alone takes hundreds of parameters and dozens of functions, and a single misreading produces wrong answers for millions of households (uncited).
- A comprehensive US model must also encode federal income tax (brackets, dozens of credits), payroll taxes, fifty state income taxes (own brackets and conformity rules), SNAP, Medicaid, SSI, TANF, housing subsidies, WIC, school meals, and more — on the order of a few thousand parameters [NEEDS CITATION: PolicyEngine US parameter count], each traceable to a legislative or regulatory source and each changing on its own schedule.
- Programs interact (eligibility for one benefit often turns on income defined by another), so a change to a single rule ripples through the rest; it is the edge cases and interactions, far more than headline rates, where encodings go wrong.

### Three architectures
- **Architecture 1 — spreadsheet behind a graphical interface; EUROMOD is the most developed example** [@sutherland2013euromod].
  - Policy rules live in structured XML: parameters, a "spine" defining calculation order, and switches for which policies are active, edited through EUROMOD's own application, which presents each policy as an expandable tree with dialogue boxes for the values.
  - Advantages: a researcher with no programming background can change a rate or threshold; the interface enforces structure; the files are openly licensed.
  - Costs at scale: the country models are large [NEEDS CITATION: EUROMOD UK component file size]; navigation depends on knowing where in the tree to look; tracking changes across versions means comparing XML; and contributing means learning EUROMOD's tooling rather than a transferable skill.
- **Architecture 2 — code-native; the approach PolicyEngine and Tax-Calculator take.**
  - Policy rules are ordinary source code — readable in any editor, browsable on GitHub, changed through the same version-control workflow developers use for everything else; a calculation is literally a function you can step through in a debugger and cover with unit tests.
  - Logic lives in Python; values live separately in human-readable YAML (see the two verbatim code blocks in Quotes). Updating for a new tax year is usually just editing parameter files; the code changes only when the structure of the policy changes.
  - Both Architecture 1 and Architecture 2 are genuinely open source (EUROMOD publishes XML under open licenses; PolicyEngine and Tax-Calculator publish code on GitHub); what differs is the experience and the mental model ("use this application to view these configurations" vs. "read this code like any other software project").
  - This is a community difference, not a better/worse judgment: EUROMOD serves researchers who work inside its ecosystem for years (investment in its tooling pays off in depth); code-native tools serve people who might contribute once, work across many projects, or wire microsimulation into other software (investment in general programming skills pays off in breadth).
- **A fourth tool outside the axis — TAXSIM**, maintained by Daniel Feenberg at the National Bureau of Economic Research since the early 1980s [@feenberg1993taxsim].
  - TAXSIM is neither spreadsheet nor open repository — it is a compiled program behind a web interface — and its distinguishing feature is decades of validation against actual IRS return data, which makes it the benchmark other tax calculators are measured against.
  - You cannot step through its code, but you can trust its answers: opaque internals, validated outputs — the combination the third architecture needs.

### Agent-encoded and verified (the third architecture)
- The third architecture is the newest. Rules are still written as YAML — a format called RuleSpec, in which logic and parameters are versioned, testable files carrying their own effective dates — but the author is usually an AI agent rather than a person, and no encoding merges on the agent's say-so.
- The agent drafts against a corpus of the actual source law (statutes, regulations, and agency guidance ingested as anchored provisions) rather than from memory, and its output is treated as a proposal, not a result.
- Each proposal passes through merge-blocking gates before it lands: the code must compile and the tests must pass, and then two checks specific to law must clear:
  1. **Money-atom grounding:** every monetary amount in the encoding must trace to a quoted passage of the governing statute or regulation, or the build fails (no dollar figure may float free of a source).
  2. **Oracle comparison:** the encoding's outputs are compared case by case against a reference calculator — TAXSIM for US federal tax, EUROMOD and UKMOD abroad, official calculators where they exist — with mismatches blocking the merge until they are explained.
- Human review sits on top of the automated gates rather than in place of them.
- The Axiom Foundation is building this layer, and at the time of writing it spans US federal law plus dozens of state codes and several other countries [VERIFY counts at publication], each encoding carrying a signed manifest recording what was built and how it checked out.
- What makes machine-written law admissible is not the agent and not the YAML but the criterion the gates enforce: every unit's output is checkable against ground truth. A statute has a fact of the matter, and an encoding either reproduces it, per household, or it doesn't; the reference calculators say which.
- How the verification actually works — the oracles, the conformance gates that only ratchet toward correctness, the countries encoded in days rather than years — is the subject of Part III.

### Ingredient two: data
- Rules encoding determines what the model computes; microdata construction determines who it computes for. A microsimulation calculates for tens of thousands of records standing in for the whole population, each with realistic income, family structure, location, and program participation; the model sums the weighted results into an estimate for the country, so every downstream revenue score, poverty rate, and distributional table inherits whatever is right or wrong about the records.
- Most records come from household surveys: in the US usually the Current Population Survey (monthly basic sample ~60,000 households; larger annual supplement carries the detailed income and program data microsimulation needs) [@census2024cps]; in the UK the Family Resources Survey; across Europe EU-SILC.
- No survey has everything. The CPS captures wages well and capital income poorly (people underreport dividends and gains, and the very wealthy are undersampled); it top-codes very high earnings [NEEDS CITATION: CPS top-coding], compressing the top tail exactly where high-earner policies bite; and it omits tax-relevant detail like itemized deductions and retirement contributions entirely.
- The gaps run the other way too: Bruce Meyer and colleagues found that 40 to 50 percent of SNAP recipients don't report their benefits in surveys, with similar non-reporting for Medicaid, SSI, and TANF [@meyer2015underreporting], biasing survey-based safety-net estimates downward and making program expansions look cheaper than they are.
- Each survey has its own blind spots: the Family Resources Survey lacks the council-tax detail UK local-tax modeling needs; EU-SILC misses the within-year timing that drives benefit calculations; none holds everything a comprehensive model requires.

### The data pipeline (now shared, versioned infrastructure)
- **Statistical matching** combines surveys: take a CPS household ($80,000, two children, California) and find a similar record in the Survey of Consumer Finances (which carries the wealth and asset detail the CPS lacks), merging their characteristics into one richer record. The craft is in "similar" — match on too few variables and you get implausible combinations (a tech worker's income welded to a retiree's assets); match on too many and no two households pair.
  - Tax-Data, part of the Policy Simulation Library, pioneered this for US tax modeling by matching CPS records to IRS Public Use File data, recovering the capital gains realizations and itemized-deduction patterns the CPS alone would miss (uncited).
  - Matching recombines existing information rather than creating it; its validity rests entirely on whether the matching assumptions hold.
- **Imputation** predicts a missing value from observed ones. Traditional imputation fits a regression and applies its average relationship, so every $100,000 earner in California receives roughly the same predicted deduction; quantile regression forests instead estimate the whole distribution of plausible values and sample from it, so a high-income California household might draw a deduction anywhere from $15,000 to $50,000 (uncited example range). Preserving that spread is what lets a model see a reform's winners and losers (e.g., a cap on itemized deductions) instead of only its average.
- **Calibration** adjusts each record's weight (how many people it represents — a rural household might stand for 5,000, an urban one for 500) so that survey aggregates reproduce known totals (e.g., a survey showing $9 trillion in aggregate wages where IRS records show $10 trillion). The mathematics is optimization: define a loss measuring how far weighted aggregates sit from the targets, add a penalty for moving any weight too far from its survey value, and minimize the sum. Targets are specific and numerous (federal income tax by bracket, SNAP benefits by state, Social Security payments by age group, wages by industry), and the reweighting stays plausible only because the penalty holds new weights close to the survey's original design.
- **Aging** moves a snapshot forward: the 2023 CPS describes 2023, while policy questions are usually about future years. The simplest version scales everything by an index (wages by projected wage growth, investment income by projected returns, everyone's age advanced); a more sophisticated version models who retires, who enters the workforce, and how individual incomes evolve, gaining accuracy at much higher build-and-validate cost. PolicyEngine draws its projection factors from the Congressional Budget Office's forecasts so its estimates line up with the baselines Washington already argues over [@cbo2025forecasting].
- These pieces are now reusable libraries rather than one-off code: imputation methods behind a common interface [@microimpute2026], weight calibration with holdout checks and diagnostics [@microcalibrate2026], and synthesis and projection alongside them; consolidated, they form populace, a calibrated-microdata commons — population data built, tested, and versioned as infrastructure rather than a hidden appendix to a tax model.
- Milestone the approach is measured against: the Enhanced CPS that PolicyEngine released in August 2025, which fused five datasets — the CPS (income and employment backbone), the Survey of Consumer Finances (wealth), the Consumer Expenditure Survey (spending), the Residential Energy Consumption Survey (energy use), and the American Time Use Survey (hours) — then calibrated the result to 9,168 administrative targets, cutting the average deviation from those totals from 8.3 percent to 0.2 percent [@policyengine2022enhanced].
  - Carried marker (HTML comment in source): `[VERIFY: key year — @policyengine2022enhanced is a 2022 blog key cited for the August 2025 Enhanced CPS milestone]`.
- The residual risk calibration cannot remove: matching aggregates is matching margins — after calibration the totals are right by construction, but nothing guarantees the joint structure (that the right households hold the right combinations of income, assets, and benefits). A population can reproduce every published total and still assemble those totals out of people who don't quite exist. Joint structure is exactly what many reforms turn on (a benefit that phases out with income but only for households holding assets above a threshold depends on how income and wealth are paired, not on either total alone). Testing that joint structure — holding a synthesized population against held-out ground truth rather than against the totals it was fit to — is per-unit verification work, and Part III returns to it.

### Ingredient three: dynamics
- Rules handle the arithmetic and data handles the who; dynamics handle how people respond (raise a marginal rate and some work less; cut a phase-out and some work more; tax carbon and some drive less). These responses move revenue, distribution, and effectiveness, and are much harder to model than the static calculation.
- Most microsimulation is static: compute what each household owes and receives under current policy, compute it again under the reform holding behavior fixed, and report the difference as the day-one effect. Static analysis answers who gains and loses and by how much (which barely depends on behavioral assumptions) but misses responses that change the totals (a carbon tax raising $100 billion assuming no driving change raises less once people respond). The static-vs-dynamic gap is largest exactly where behavior is most sensitive.
- The most-studied response is labor supply [@odonoghue2001dynamic]: how much hours or reported income shift when the after-tax wage changes, summarized as an elasticity. The most comprehensive summary is the elasticity of taxable income (ETI), which folds in hours plus tax planning, income shifting, and avoidance.
- Carina Neisser's meta-regression — 1,720 estimates from 61 studies — finds a mean ETI around 0.30, meaning a 10 percent rise in the net-of-tax rate raises reported income by roughly 3 percent [@neisser2021eti]. The spread is enormous (some near zero, others above 1.0), varying with income, tax system, time horizon, and method.
- Consequence of that spread: raising the top rate from 37 to 39.6 percent brings in something like $50 billion more per year under a low elasticity than under a high one (uncited illustrative figure), a genuine and consequential disagreement among honest estimators.
- Robust patterns within the range: primary earners in married couples barely move; secondary earners and single parents respond more; the reported income of the very wealthy moves the most, though much of that reflects tax planning rather than any real change in work.
- PolicyEngine makes the choice explicit: users can run no response, CBO-style elasticities, or their own parameters, and watch the revenue estimate move — uncertainty surfaced rather than buried.
- Other behavioral margins the same machinery can carry: capital gains realizations respond in their timing (higher rates encourage holding, lower rates encourage selling), swinging revenue between years; taxpayers restructure around new rules, shifting income between years or reclassifying its type (as the speed of the response to the 2017 Tax Cuts and Jobs Act showed); and program take-up rises and falls with generosity and complexity (because take-up for programs like SNAP and the EITC already runs well below 100 percent, a reform can change costs as much by moving enrollment as by changing the benefit).
- Structural models: rather than take elasticities as given, specify what people maximize (utility from consumption and leisure under a budget constraint) and let behavior fall out of the optimization, so changing the tax schedule and re-solving produces the new behavior directly. Appeal: reach — a structural model can price a 90 percent marginal rate no one has ever observed, where an elasticity estimated at lower rates may not carry. Cost: assumption (that people truly maximize expected utility, that the chosen functional forms are right) and a steep climb in computational complexity. PolicyEngine does not yet implement structural responses; the architecture leaves room for them as modules over the same household data.

### The determinism/prediction seam
- Everything up to the behavioral response is deterministic: given the rules and a household's inputs, the tax it owes and the benefits it receives are not estimated — they are computed exactly and can be checked, household by household, against the statute, against a reference calculator, or against what a caseworker actually determined. There is a fact of the matter, verifiable now, per unit, before the policy takes effect.
- The behavioral response is different in kind: ask how people will change their hours, portfolios, or take-up, and you leave the domain where the answer is computable and enter the domain of prediction. Structural models do not escape this — their outputs still land on the prediction side of the seam, answerable only once the behavior has happened.
- The same model wears two epistemic hats: one output verified against the rules as written, the other against outcomes as they happen. Keeping those two straight — being exact where exactness is possible and honestly uncertain where it isn't — is most of what separates a trustworthy model from a merely confident one.

### The integration problem
- The three ingredients give the questions to ask of any microsimulation model, and building one means answering all three at once:
  - **Rules:** Are the calculations right, validated against authoritative sources, and legible enough to see why they produce a given answer?
  - **Data:** Does the microdata represent the population, with missing variables filled defensibly and weights calibrated to real totals?
  - **Dynamics:** What behavioral assumptions are in play, are they stated or hidden, and how much do results move when the assumptions change?
- Different models are strong in different columns: TAXSIM in rules, validated against decades of returns [@feenberg1993taxsim]; Tax-Data in microdata construction; OG-USA in dynamics, with a full overlapping-generations model of behavior. PolicyEngine's aim was to be strong across all three at once, which is exactly what made it hard.
- The three ingredients constrain each other: the rules you want to simulate dictate the data you need (model capital gains and you need asset data; model childcare subsidies and you need childcare expenses); the data you have bounds the rules you can implement (without itemized-deduction detail you cannot credibly score a deduction reform); and dynamics reach into both (a behavioral response changes effective rates, which change the distributional story).
- Why PolicyEngine took years rather than months: no single tax formula is hard, but making comprehensive rules work with realistic data while supporting flexible dynamics — all at once, across the whole system — takes sustained engineering.
- Each of the three ingredients is now becoming a layer an agent can build and a machine can check on its own terms — rules against statute, data against ground truth, dynamics against outcomes as they arrive — and that decomposition is the story Part III tells.

---

## Story beats

This chapter is expository anatomy rather than narrative; its "beats" are conceptual movements and set-piece examples:

- **"This sounds simple. It isn't."** The EITC unfolds from a single credit into hundreds of parameters and dozens of functions, dramatizing that the difficulty lives in edge cases and interactions, not headline rates.
- **The three-architectures reveal.** The field's three answers to how rules should be written and stored, staged as a progression: spreadsheet/XML (EUROMOD) → code-native (Tax-Calculator, classic PolicyEngine) → agent-encoded + oracle-verified (RuleSpec/Axiom). The National Insurance code example (Python + YAML) is the concrete artifact that makes "code-native" legible.
- **TAXSIM as the pivot.** The "opaque internals, validated outputs" characterization sets up why the third architecture leans on reference calculators — the fourth tool that "matters for what comes next."
- **The pipeline walk-through.** Matching → imputation → calibration → aging, each with its own small worked illustration (the $80k California household matched to SCF; the $15k–$50k deduction draw; the $9T-vs-$10T wage gap), culminating in the Enhanced CPS five-dataset fusion (8.3% → 0.2%).
- **The joint-structure warning.** "A population can reproduce every published total and still assemble those totals out of people who don't quite exist" — the residual-risk beat that hands verification work forward to Part III.
- **Naming the seam.** The chapter's closing move: the deterministic side (checkable now, per unit) vs. the prediction side (checkable only when reality arrives), "the same model wearing two epistemic hats."

---

## Quotes

The two example code blocks are quotable artifacts and are included verbatim below (a UK National Insurance contribution in PolicyEngine, code-native architecture):

**Python (logic):**
```python
def formula(person, period, parameters):
    earnings = person("employee_earnings", period)
    ni = parameters(period).gov.hmrc.national_insurance
    pt = ni.class_1.thresholds.primary_threshold
    uel = ni.class_1.thresholds.upper_earnings_limit
    main_rate = ni.class_1.rates.main

    liable_at_main = max_(0, min_(earnings, uel) - pt)
    return liable_at_main * main_rate
```

**YAML (values):**
```yaml
gov:
  hmrc:
    national_insurance:
      class_1:
        thresholds:
          primary_threshold:
            values:
              2024-04-06: 242  # weekly
        rates:
          main:
            values:
              2024-04-06: 0.08
```

Quoted terms and short attributed phrases used in the chapter:
- The EITC dependency term "qualifying child" (with its age, relationship, residency, and joint-return tests).
- The EUROMOD structural term "spine" (the XML element defining calculation order).
- The matching craft-word "similar" (the whole difficulty of statistical matching hangs on it).
- The rules-layer gate name "money-atom" (grounding check requiring every monetary amount to trace to a quoted source passage).
- The dynamics term "net-of-tax rate" (a 10 percent rise raising reported income ~3 percent at mean ETI ≈ 0.30).

(No external verbatim source quotations appear in this chapter; the load-bearing artifacts are the two code blocks.)

---

## Arguments

Numbered propositions this chapter advances:

1. **Every microsimulation decomposes into exactly three ingredients — rules, data, dynamics — and each is verifiable against a different kind of truth.** The framework is architecture, not technique, and it is the anatomy the rest of the book builds on.
2. **There are three architectures for rules encoding, not two.** Extend the usual spreadsheet-vs-code framing to a third: agent-encoded + oracle-verified (RuleSpec). TAXSIM's "opaque internals, validated outputs" is the model the third architecture generalizes.
3. **What makes machine-written law admissible is per-unit checkability against ground truth — not the agent and not the format.** A statute has a fact of the matter; an encoding reproduces it per household or it doesn't; reference calculators adjudicate. (Corollary, stated as texture: agent scale without this is "confident fiction at volume.")
4. **Money-atom grounding and oracle comparison are merge-blocking gates, not documentation.** Verification is built into the pipeline as a one-way valve, not appended after the fact.
5. **Preserving distributional spread (quantile methods) beats mean imputation whenever a reform bites unevenly.** Collapsing similar households onto one predicted value hides winners and losers.
6. **Calibration matches margins, not joint structure — and joint structure is where the residual risk and many reforms live.** Reproducing every published total does not guarantee the right households hold the right combinations; testing that requires per-unit verification against held-out ground truth.
7. **Most distributional conclusions are robust to behavioral assumptions; most high-end revenue conclusions are not.** Who-gains-and-loses barely depends on dynamics, but the static-vs-dynamic gap is largest where behavior is most sensitive, which is where honest estimators most disagree (ETI spread from ~0 to >1.0).
8. **Elasticities assume the response is known; structural models derive it — trading reach for assumption.** Structural reach (pricing an unobserved 90% rate) comes at the cost of maximization/functional-form assumptions and computational complexity, and its outputs still land on the prediction side of the seam.
9. **The determinism/prediction seam is the book's organizing distinction.** One model output is verifiable now, per unit, against the law; the other is verifiable only when reality arrives. Being exact where exactness is possible and honestly uncertain where it isn't is what separates a trustworthy model from a merely confident one.
10. **The three ingredients constrain each other, which is why comprehensive modeling took years, not months** — and why decomposing them into independently agent-buildable, machine-checkable layers is the payoff Part III delivers.

---

## Author-texture (verbatim, may be reused)

Passages with the author's hand — selective:

- The rules-complexity beat: "This sounds simple. It isn't."
- The verification criterion, stated bluntly: "Agent scale without it is just confident fiction at volume."
- The admissibility line: "What makes this admissible—what lets you trust law written by a machine—is not the agent and not the YAML. It's the criterion the gates enforce: every unit's output is checkable against ground truth."
- The joint-structure warning: "A population can reproduce every published total and still assemble those totals out of people who don't quite exist."
- The two-hats image: "It is the same model wearing two epistemic hats: one output verified against the rules as written, the other against outcomes as they happen."
- The seam's closing standard: "Keeping those two straight—being exact where exactness is possible and honestly uncertain where it isn't—is most of what separates a trustworthy model from a merely confident one."
- The integration payoff: "No single tax formula is hard; individual calculations are straightforward. What takes sustained engineering is making comprehensive rules work with realistic data while supporting flexible dynamics, all at once, across the whole system."

---

## Structural notes

- **Chapter's job (from the from-scratch outline, ch 7).** Present rules, data, and dynamics as the anatomy of microsimulation, with the review's best structural idea baked in: extend "two architectures" of rules encoding to **three** — spreadsheet/XML (EUROMOD), hand-written code-native (Tax-Calculator, classic PolicyEngine), and agent-encoded + oracle-verified (RuleSpec) — introducing the per-unit-verifiability criterion that Part III delivers in full. Reframe dynamics as the seam where determinism ends and prediction begins. This chapter is the hinge into Part III: each ingredient is an agent-buildable layer.
- **Scope discipline (do not over-build here).** The deep encoding / verification / SOUTHMOD material belongs in Part III where it has room, not stuffed into this chapter. This chapter introduces the money-atom gate, oracle comparison, RuleSpec, and the Axiom Foundation only enough to name the mechanism and the criterion; the full treatment (oracles, conformance ratchets, countries in days) is explicitly deferred to Part III (ch 9–11).
- **Ending cross-reference (the seam).** The chapter ends on the **determinism/prediction seam** — the property that everything before the behavioral response is checkable now, per unit, while the behavioral response is prediction, checkable only when reality arrives. This seam is the hinge the rest of the book is built on and is paid off across Part III and the prediction pole (Part IV).
- **Data-layer framing (per outline + rewrite-facts.md).** The updated data story runs Enhanced CPS → **populace** (calibrated-microdata commons), methods foregrounded and the populace brand kept low-key ("name it once, plainly, as infrastructure; lean on the methods elsewhere"). Never write **microplex**.
- **Cross-chapter repetitions to police (shared with ch 5 and ch 6 — pick one home each):**
  - Enhanced CPS milestone (August 2025, five datasets, 9,168 targets) appears here, in ch 5, and in ch 6. This chapter carries the fullest version: it names all five datasets and their contributions and gives the 8.3% → 0.2% deviation figure. If the milestone is told once, this is the natural home for the detailed version.
  - The Meyer 40–50% SNAP under-reporting finding [@meyer2015underreporting] appears here and in ch 6 — dedupe or differentiate.
  - The quantile-regression-forests imputation method and the calibration-to-administrative-totals method appear here and in ch 6 (there compressed, with [@microimpute2026] / [@microcalibrate2026]).
  - The weighting illustration (rural household ≈ 5,000 people, urban ≈ 500) appears here and in ch 6.
- **Markers that must survive the rewrite (resolve, don't delete):** number of states with EITC variants [NEEDS CITATION]; PolicyEngine US parameter count [NEEDS CITATION]; EUROMOD UK component file size [NEEDS CITATION]; Axiom coverage counts [VERIFY counts at publication]; CPS top-coding [NEEDS CITATION]; and the `policyengine2022enhanced` key-year mismatch [VERIFY].
- **Verbatim artifacts to preserve.** The two National Insurance code blocks (Python logic + YAML values) are the chapter's load-bearing illustration of the code-native architecture — carry them verbatim; the YAML values (£242 weekly primary threshold and 0.08 main rate, effective 2024-04-06) are illustrative parameter values, not sourced claims.

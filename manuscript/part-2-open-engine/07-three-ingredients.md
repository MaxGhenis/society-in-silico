# Chapter 7: The three ingredients

Every microsimulation model rests on three foundations: rules encoding, microdata construction, and behavioral dynamics. The framework doesn't appear explicitly in the microsimulation literature—textbooks organize around techniques, not architecture [@caldwell1996microsimulation]—but it captures what any team that builds one of these models has to solve. Get the rules wrong and the calculations are incorrect. Get the data wrong and the estimates are biased. Ignore dynamics and the projections miss how people respond. PolicyEngine, Tax-Calculator, EUROMOD, and TAXSIM each answer the same three questions differently, and the differences are the most revealing thing about them.

They are also three separate construction projects, and increasingly ones that AI agents can take on: each ingredient is now a layer that can be built at a fraction of its former cost, and each is trustworthy only to the degree its output can be checked against something real.

## Ingredient one: rules

The first ingredient is encoding policy rules as executable logic. Every tax rate, benefit threshold, eligibility condition, and phase-out schedule has to become something a computer can evaluate.

This sounds simple. It isn't.

Take the Earned Income Tax Credit. Its phase-in rate depends on the number of qualifying children, and "qualifying child" carries its own age, relationship, residency, and joint-return tests. The credit depends on earned income, which excludes some income types and includes others; the phase-out threshold differs for single and married filers; and many states layer their own EITC on top, each with its own rules about whether it conforms to the federal definition [NEEDS CITATION: number of states with EITC variants]. Encoding this one credit takes hundreds of parameters and dozens of functions, and a single misreading produces wrong answers for millions of households.

And the EITC is one program. A comprehensive US model also has to encode federal income tax with its brackets and dozens of credits, payroll taxes, fifty state income taxes with their own brackets and conformity rules, SNAP, Medicaid, SSI, TANF, housing subsidies, WIC, school meals, and more—on the order of a few thousand parameters [NEEDS CITATION: PolicyEngine US parameter count], each traceable to a legislative or regulatory source, each changing on its own schedule.

### Three architectures

The field has produced three distinct answers to how those rules should be written and stored.

The first is the spreadsheet behind a graphical interface, and EUROMOD is its most developed example [@sutherland2013euromod]. Policy rules live in structured XML—parameters, a "spine" defining calculation order, switches for which policies are active—edited through EUROMOD's own application, which presents each policy as an expandable tree with dialogue boxes for the values. The design has real advantages: a researcher with no programming background can change a rate or a threshold, the interface enforces structure, and the files are openly licensed. Its costs show up at scale. The country models are large [NEEDS CITATION: EUROMOD UK component file size], navigation depends on knowing where in the tree to look, tracking changes across versions means comparing XML, and contributing means learning EUROMOD's tooling rather than a skill that transfers elsewhere.

The second architecture is code-native, the approach PolicyEngine and Tax-Calculator take. Policy rules are ordinary source code—readable in any editor, browsable on GitHub, changed through the same version-control workflow developers use for everything else. A calculation is literally a function you can step through in a debugger and cover with unit tests. Here is a UK National Insurance contribution in PolicyEngine:

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

Anyone who reads Python can follow it: pull earnings, look up thresholds and a rate, apply the rate to earnings in the liable band. The values themselves live separately, in human-readable YAML:

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

Logic in Python, values in YAML. Updating for a new tax year is usually just editing parameter files; the code changes only when the structure of the policy changes.

Both architectures are genuinely open source, and both communities are right to call them so—EUROMOD publishes its XML under open licenses, PolicyEngine and Tax-Calculator publish their code on GitHub. What differs is the experience. Reading a EUROMOD policy means installing the software, opening the project, and navigating menus; reading a PolicyEngine policy means opening a file in a browser. This isn't about better or worse—it's about different communities. EUROMOD serves researchers who work inside its ecosystem for years, and the investment in its tooling pays off in depth. The code-native tools serve people who might contribute once, or who work across many projects, or who want to wire microsimulation into other software, and the investment in general programming skills pays off in breadth.

A fourth tool sits slightly outside this axis and matters for what comes next: TAXSIM, maintained by Daniel Feenberg at the National Bureau of Economic Research since the early 1980s [@feenberg1993taxsim]. TAXSIM is neither spreadsheet nor open repository—it's a compiled program behind a web interface—and its distinguishing feature is decades of validation against actual IRS return data, which makes it the benchmark other tax calculators are measured against. You can't step through its code, but you can trust its answers, and that combination—opaque internals, validated outputs—turns out to be exactly what the third architecture needs.

### Agent-encoded and verified

The third architecture is the newest. Rules are still written as YAML—a format called RuleSpec, in which logic and parameters are versioned, testable files carrying their own effective dates—but the author is usually an AI agent rather than a person, and no encoding merges on the agent's say-so. Each one passes through merge-blocking gates before it lands. The code has to compile and the tests have to pass, and then two checks specific to law have to clear. Every monetary amount in the encoding must trace to a quoted passage of the governing statute or regulation—a "money-atom" grounding check that fails the build if any dollar figure floats free of a source. And the encoding's outputs are compared, case by case, against a reference calculator—TAXSIM for US federal tax, EUROMOD and UKMOD abroad, official calculators where they exist—with mismatches blocking the merge until they are explained. The Axiom Foundation is building this layer, and at the time of writing it spans US federal law plus dozens of state codes and several other countries [VERIFY counts at publication], each encoding carrying a signed manifest of what was built and how it checked out.

What makes this admissible—what lets you trust law written by a machine—is not the agent and not the YAML. It's the criterion the gates enforce: every unit's output is checkable against ground truth. A statute has a fact of the matter, and an encoding either reproduces it, per household, or it doesn't; the reference calculators say which. That is the whole test, and it is what separates a verified encoding from a plausible-looking one. Agent scale without it is just confident fiction at volume. How that verification actually works—the oracles, the conformance gates that only ratchet toward correctness, the countries encoded in days rather than years—is the subject of Part III.

## Ingredient two: data

Rules encoding determines what the model computes. Microdata construction determines who it computes for. A microsimulation doesn't calculate taxes for one hypothetical family; it calculates them for tens of thousands of records standing in for the whole population, each with realistic income, family structure, location, and program participation, and then aggregates. The records have to come from somewhere.

Most of them come from household surveys. In the US that is usually the Current Population Survey, whose monthly basic sample covers about 60,000 households and whose larger annual supplement carries the detailed income and program data microsimulation needs [@census2024cps]; in the UK, the Family Resources Survey; across Europe, EU-SILC. These surveys exist because governments need population statistics, and they measure income, employment, and poverty—much of what a model needs. But no survey has everything. The CPS captures wages well and capital income poorly, because people underreport dividends and gains and the very wealthy are undersampled; it top-codes very high earnings [NEEDS CITATION: CPS top-coding], compressing the top tail exactly where high-earner policies bite; and it omits tax-relevant detail like itemized deductions and retirement contributions entirely. The gaps run the other way too. Bruce Meyer and colleagues found that 40 to 50 percent of SNAP recipients don't report their benefits in surveys, with similar non-reporting for Medicaid, SSI, and TANF [@meyer2015underreporting]—which biases survey-based safety-net estimates downward and makes program expansions look cheaper than they are.

Closing those gaps is a pipeline, and over the past few years it has turned from model-specific plumbing into shared, versioned infrastructure.

Statistical matching combines surveys. Take a CPS household—$80,000, two children, California—and find a similar record in the Survey of Consumer Finances, which carries the wealth and asset detail the CPS lacks; merge their characteristics into one richer record. The craft is in "similar": match on too few variables and you get implausible combinations, match on too many and no two households pair at all. Tax-Data, part of the Policy Simulation Library, pioneered this for US tax modeling by matching CPS records to IRS Public Use File data, recovering the capital gains realizations and itemized-deduction patterns the CPS alone would miss.

Some variables aren't in any survey, and for those the model imputes—predicts the missing value from the observed ones. Traditional imputation fits a regression and applies its average relationship, so every $100,000 earner in California receives roughly the same predicted deduction. Quantile regression forests instead estimate the whole distribution of plausible values and sample from it, so a high-income California household might draw a deduction anywhere from $15,000 to $50,000. That matters whenever a reform bites unevenly across the distribution: a cap on itemized deductions affects people differently depending where in the range they fall, and mean imputation would systematically misstate it.

Even perfect matching and imputation don't guarantee the microdata matches administrative totals; the survey might show $9 trillion in aggregate wages where IRS records show $10 trillion, and that gap propagates to every estimate. Calibration fixes it by adjusting each record's weight—how many people it represents—so that survey aggregates reproduce known totals, penalizing large departures from the original survey design so the reweighting stays plausible.

Microdata is also a snapshot: the 2023 CPS describes 2023, while policy questions are usually about future years. So the pipeline ages the data forward, growing incomes, shifting the age structure, and aligning to official projections. PolicyEngine draws its projection factors from the Congressional Budget Office's forecasts so its estimates line up with the baselines Washington already argues over [@cbo2025forecasting].

These pieces are now built as reusable libraries rather than one-off code: imputation methods behind a common interface [@microimpute2026], weight calibration with holdout checks and diagnostics [@microcalibrate2026], and synthesis and projection alongside them. Consolidated, they form populace, a calibrated-microdata commons—population data built, tested, and versioned as infrastructure in its own right rather than as a hidden appendix to a tax model. The milestone the approach is measured against is the Enhanced CPS that PolicyEngine released in August 2025, which fused five datasets—the CPS, the Survey of Consumer Finances, the Consumer Expenditure Survey, the Residential Energy Consumption Survey, and the American Time Use Survey—and calibrated the result to 9,168 administrative targets, cutting the average deviation from those totals from 8.3 percent to 0.2 percent [@policyengine2022enhanced]. <!-- [VERIFY: key year — @policyengine2022enhanced is a 2022 blog key cited for the August 2025 Enhanced CPS milestone] -->

One thing calibration cannot do is worth stating plainly, because it is where the residual risk lives. Matching aggregates is matching margins: after calibration the totals are right by construction, but nothing guarantees the joint structure—that the right households hold the right combinations of income, assets, and benefits. A population can reproduce every published total and still assemble those totals out of people who don't quite exist. Testing that joint structure—holding a synthesized population against held-out ground truth rather than against the totals it was fit to—is verification work, of the same per-unit kind the rules layer demands, and Part III returns to it.

## Ingredient three: dynamics

Rules handle the arithmetic and data handles the who; dynamics handle how people respond. Raise a marginal rate and some people work less; cut a phase-out and some work more; tax carbon and some drive less. These responses move revenue, distribution, and effectiveness, and they are much harder to model than the static calculation.

Most microsimulation is static: compute what each household owes and receives under current policy, compute it again under the reform holding behavior fixed, and report the difference as the day-one effect. Static analysis answers a great deal—who gains, who loses, and by how much barely depends on behavioral assumptions—but it misses responses that change the totals. A carbon tax that raises $100 billion assuming no one changes their driving raises less once people do.

The most-studied response is labor supply [@odonoghue2001dynamic]: how much do hours, or reported income, shift when the after-tax wage changes? Economists summarize it as an elasticity, and the most comprehensive summary is the elasticity of taxable income, which folds in not just hours but tax planning, income shifting, and avoidance. Carina Neisser's meta-regression—1,720 estimates from 61 studies—finds a mean ETI around 0.30, meaning a 10 percent rise in the net-of-tax rate raises reported income by roughly 3 percent [@neisser2021eti]. But the spread is enormous: some estimates sit near zero, others above 1.0, varying with income, tax system, time horizon, and method. That range is not a rounding concern. Raising the top rate from 37 to 39.6 percent brings in something like $50 billion more per year under a low elasticity than under a high one, and no amount of data has settled which is right—it is a genuine and consequential disagreement among honest estimators.

Some patterns within the range are robust. Primary earners in married couples barely move—they work about the same whatever the rate—while secondary earners and single parents respond more; the reported income of the very wealthy moves the most, though much of that reflects tax planning rather than any real change in work. A model that takes behavior seriously has to say which populations respond how much, and then be honest that the parameter carries its own uncertainty. PolicyEngine handles this by making the choice explicit: users can run no response, CBO-style elasticities, or their own parameters, and watch the revenue estimate move—uncertainty surfaced rather than buried. Labor supply is only the first margin. Capital gains realizations respond in their timing to rate changes, taxpayers restructure around new rules, and program take-up rises and falls with generosity and complexity—each a further response the same machinery can carry.

There is a seam running through this third ingredient, and it is worth naming because much of the rest of the book is built on it. Everything up to the behavioral response is deterministic. Given the rules and a household's inputs, the tax it owes and the benefits it receives are not estimated—they are computed, exactly, and can be checked, household by household, against the statute, against a reference calculator, or against what a caseworker actually determined. There is a fact of the matter, and you can verify it now, per unit, before the policy ever takes effect.

The behavioral response is different in kind. Ask how people will change their hours, their portfolios, or their take-up, and you have left the domain where the answer is computable and entered the domain of prediction. There is still a fact of the matter, but you don't get to check it today—you find out when reality arrives and the data comes in. It is the same model wearing two epistemic hats: one output verified against the rules as written, the other against outcomes as they happen. Keeping those two straight—being exact where exactness is possible and honestly uncertain where it isn't—is most of what separates a trustworthy model from a merely confident one.

## The integration problem

The three ingredients give you the questions to ask of any microsimulation model, and building one means answering all three at once:

**Rules.** Are the calculations right, validated against authoritative sources, and legible enough that you can see why they produce a given answer?

**Data.** Does the microdata represent the population, with missing variables filled defensibly and weights calibrated to real totals?

**Dynamics.** What behavioral assumptions are in play, are they stated or hidden, and how much do the results move when the assumptions change?

Different models are strong in different columns—TAXSIM in rules, validated against decades of returns [@feenberg1993taxsim]; Tax-Data in microdata construction; OG-USA in dynamics, with a full overlapping-generations model of behavior. PolicyEngine's aim was to be strong across all three at once, and that is exactly what made it hard.

The three ingredients don't sit side by side; they constrain each other. The rules you want to simulate dictate the data you need—model capital gains and you need asset data, model childcare subsidies and you need childcare expenses. The data you have bounds the rules you can implement—without itemized-deduction detail, you cannot credibly score a deduction reform. And dynamics reach into both, because a behavioral response changes effective rates, which change the distributional story. Building the model means making these fit: rules that handle whatever data exists, data that supports whatever rules matter, dynamics calibrated to make sense with both.

That is why PolicyEngine took years rather than months. No single tax formula is hard; individual calculations are straightforward. What takes sustained engineering is making comprehensive rules work with realistic data while supporting flexible dynamics, all at once, across the whole system. Each of the three ingredients is now becoming a layer an agent can build and a machine can check on its own terms—rules against statute, data against ground truth, dynamics against outcomes as they arrive—and that decomposition is the story Part III tells.

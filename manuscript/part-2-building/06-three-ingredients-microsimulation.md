# Chapter 6: The Three Ingredients of Microsimulation

Every microsimulation model rests on three foundations: rules encoding, microdata construction, and behavioral dynamics. This three-part framework doesn't appear explicitly in the microsimulation literature—textbooks focus on techniques, not architecture—but it captures what any team building these models must solve.

Get the rules wrong, and your calculations are incorrect. Get the data wrong, and your estimates are biased. Ignore dynamics, and your projections miss how people respond to policy changes.

PolicyEngine, Tax-Calculator, EUROMOD, TAXSIM—each approaches these three ingredients differently. Understanding those differences reveals why some models work better for certain purposes, and what tradeoffs every modeling team faces.

---

## Ingredient One: Rules Encoding

The first ingredient is encoding policy rules as executable code. Every tax rate, benefit threshold, eligibility condition, and phase-out schedule must be translated into logic that a computer can evaluate.

This sounds straightforward. It isn't.

Consider the Earned Income Tax Credit. The federal EITC has different phase-in rates based on the number of qualifying children. A "qualifying child" has specific age requirements, relationship requirements, residency requirements, and joint return requirements. The credit amount depends on earned income, which excludes certain types of income but includes others. The phase-out threshold differs for single and married filers. And thirty-one states have their own EITC variants, each with its own rules about conformity to federal definitions.

Encoding the EITC requires hundreds of parameters and dozens of functions. A single misread of the tax code produces incorrect results for millions of hypothetical households.

### Two Architectures

The microsimulation world has converged on two main approaches to rules encoding: spreadsheet-style configuration and code-native implementation.

**EUROMOD exemplifies the spreadsheet approach.** Policy rules live in XML files—structured text that looks more like configuration than code. A typical EUROMOD XML file contains policy parameters (rates, thresholds, amounts), policy spine definitions (which calculations run in what order), and switch settings (which policies are active). To view or modify these rules, you download the EUROMOD software and open the project files in its graphical interface. The interface presents policies as expandable trees of parameters, with dialogue boxes for editing values.

This architecture has real advantages. Researchers without programming backgrounds can modify parameters—change a tax rate, adjust a benefit threshold—without writing code. The interface enforces structure, preventing certain classes of errors. And the XML format is technically "open source"—anyone can read the files.

But limitations emerge at scale. EUROMOD's UK component contains over 67 megabytes of XML policy definitions. Navigating that through a graphical interface requires knowing where to look. Tracking changes across versions requires comparing XML files, which isn't how most researchers work. Contributing improvements means learning EUROMOD's tooling, not the general-purpose skills transferable to other projects.

**PolicyEngine and Tax-Calculator represent the code-native approach.** Policy rules are Python functions, readable in any text editor or IDE, browsable on GitHub, modifiable through standard version control workflows. A tax calculation is literally code: you can step through it with a debugger, test it with unit tests, trace exactly what happens for any input.

Here's what calculating UK National Insurance contributions looks like in PolicyEngine:

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

Anyone who reads Python can follow this. The function retrieves earnings, looks up thresholds and rates from a parameter tree, and calculates the contribution. The parameter values come from YAML files—human-readable configuration that can be updated annually without modifying code:

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

This separation—logic in Python, values in YAML—means updating for a new tax year is often just changing parameter files. The logic only changes when the structure of the policy changes.

### Openness vs. Accessibility

Both architectures call themselves "open source," and both legitimately are. EUROMOD publishes its XML files under open licenses. PolicyEngine and Tax-Calculator publish their Python code on GitHub. Anyone can inspect, copy, or modify either.

But the practical experience differs dramatically.

To understand a EUROMOD policy, you download the software, open the project, navigate through menus to find the relevant policy, expand trees to see parameters, and read values from dialogue boxes. The mental model is "use this application to view these configurations."

To understand a PolicyEngine policy, you browse GitHub, click on a file, and read code. No installation required. The mental model is "read this code like any other software project."

This isn't about better or worse—it's about different communities. EUROMOD serves researchers who work primarily in its ecosystem, often for years. The investment in learning its tooling pays off through deep capability. PolicyEngine and Tax-Calculator serve researchers who might contribute once, or who work across many projects, or who want to integrate microsimulation into other software. The investment in general Python skills pays off through breadth.

The difference matters for transparency. When HM Treasury published their Algorithmic Transparency Record about PolicyEngine UK, they could link directly to the GitHub repository. Anyone curious about how the model works can browse the code without installing anything. That immediate accessibility is impossible with tools requiring specialized software to inspect.

---

## Ingredient Two: Microdata Construction

Rules encoding determines what calculations the model performs. Microdata construction determines who those calculations are performed for.

A microsimulation model simulates real populations. You don't just compute taxes for one hypothetical household—you compute taxes for 100,000 households representing 330 million Americans. Each household has realistic characteristics: income distribution, family composition, geographic location, benefit receipt. The model calculates taxes and benefits for each record, then aggregates to estimate totals.

Where do these records come from?

### The Survey Foundation

Most microsimulation uses household survey data. In the US, that's typically the Current Population Survey (CPS)—an annual sample of about 100,000 households. In the UK, the Family Resources Survey (FRS). In Europe, the European Union Statistics on Income and Living Conditions (EU-SILC).

These surveys exist because governments need population statistics. They're designed for measuring income, employment, poverty—exactly what microsimulation models need. The data already exists. Just use it.

Except it's never that simple.

The CPS captures wages, salaries, and common benefit receipt well. It captures capital income poorly—people underreport dividends and capital gains, and the very wealthy are systematically undersampled. It doesn't capture certain tax-relevant information at all—itemized deductions, retirement contributions, business income details.

Every survey has these gaps. The FRS doesn't include council tax details needed for UK local tax modeling. EU-SILC doesn't capture within-year timing that affects benefit calculations. No single survey has everything a comprehensive microsimulation model needs.

### Statistical Matching

One solution: combine multiple surveys.

Statistical matching links records from different datasets that represent similar households. Take a CPS record for a household earning $80,000 with two children in California. Find a similar household in the Survey of Consumer Finances (SCF), which has detailed wealth and asset information. Combine their characteristics: the CPS provides income and employment details, the SCF provides investment holdings and debt.

The technique requires careful judgment about what "similar" means. Matching on too few variables produces implausible combinations—a tech worker's income matched to a retiree's wealth profile. Matching on too many variables finds no matches—no two households are identical across many dimensions.

Tax-Data, part of the Policy Simulation Library, pioneered this approach for US tax modeling. The package statistically matches CPS records to IRS Public Use Files (PUF), combining survey income data with tax return information. The result captures tax-relevant details—capital gains realizations, itemized deduction patterns—that the CPS alone would miss.

The Enhanced CPS that PolicyEngine launched in August 2025 extended this further. We integrated five datasets: the CPS, Survey of Consumer Finances, Consumer Expenditure Survey, Residential Energy Consumption Survey, and American Time Use Survey. Each contributed different information. The SCF filled in wealth. The CEX added spending patterns relevant for consumption taxes. The RECS added energy consumption for carbon tax modeling. The ATUS added time use for understanding childcare policy.

Statistical matching doesn't create new information—it combines existing information in ways that plausibly represent real households. The validity depends on whether the matching assumptions hold. When they do, you get more comprehensive records. When they don't, you get statistical artifacts that bias your estimates.

### Imputation

Some variables simply aren't in any available survey. For these, microsimulation models impute—predict missing values from observed characteristics.

Traditional imputation uses regression. Fit a model predicting itemized deductions from income, filing status, and state of residence. Apply that model to records lacking deduction information. The result fills the gap, but with the average relationship—every $100,000 earner in California gets similar predicted deductions, ignoring the real variation.

The Enhanced CPS used Quantile Regression Forests instead. Rather than predicting the mean, QRFs estimate the entire distribution of plausible values. A high-income California household might have predicted deductions anywhere from $15,000 to $50,000, with probabilities for each level. The imputation samples from this distribution, preserving realistic variation rather than collapsing to averages.

This matters for policy analysis. A reform that caps itemized deductions at $25,000 affects different people depending on where they fall in the distribution. Mean imputation would systematically misestimate this impact. Distributional imputation gets closer to reality.

### Calibration

Even perfect statistical matching and imputation don't guarantee the microdata matches administrative totals. The CPS might show aggregate wages of $9 trillion when IRS records show $10 trillion. That 10% gap propagates to every estimate—revenue projections, distributional tables, poverty rates.

Calibration adjusts survey weights to match external targets. Each survey record has a weight representing how many people it represents in the population. A rural household might have weight 5,000; an urban household weight 500. Adjusting these weights can make survey aggregates match known totals.

The mathematics involve optimization. Define a loss function measuring how far survey aggregates deviate from targets. Add a penalty for changing weights too dramatically from their original values. Minimize the combined objective. The result: new weights that reproduce administrative totals while staying reasonably close to the original survey design.

The Enhanced CPS calibrated to 9,168 administrative targets. Federal income tax by bracket. SNAP benefits by state. Social Security payments by age group. Wages by industry. The gradient descent optimizer found weights that matched these targets while maintaining plausible household characteristics.

The impact was dramatic. Before calibration, aggregate deviations from administrative totals averaged 8.3%. After calibration, 0.2%. The same survey records, reweighted to match reality.

### Projection

Microdata represents a point in time. The 2023 CPS describes America in 2023. But policy analysis often asks about future years—what would this reform cost in 2027?

Projection "ages" the microdata forward. Incomes grow with inflation and real wage growth. Population demographics shift toward older ages. New policies that took effect get incorporated. The goal: make 2023 data represent a plausible 2027.

Simple projection uses indexes. Multiply all wages by projected wage growth. Multiply all investment income by projected capital returns. Age everyone by four years. This preserves the basic structure while scaling to future levels.

Sophisticated projection involves modeling—who dies, who retires, who enters the workforce, how incomes evolve for individuals over time. These dynamic models are more accurate but more complex to build and validate.

PolicyEngine uses projection factors from the Congressional Budget Office and other official forecasts. The CBO already projects future tax revenues, benefit costs, and economic variables. Aligning microdata projection to CBO's assumptions ensures our estimates are comparable to official baselines.

---

## Ingredient Three: Behavioral Dynamics

Rules encoding handles the math. Microdata construction handles who. Behavioral dynamics handles how people respond.

Raise tax rates, and some people work less. Cut benefit phase-outs, and some people work more. Implement a carbon tax, and some people drive less. These behavioral responses affect revenue, distributional impacts, and policy effectiveness—but they're much harder to model than static calculations.

### Static vs. Dynamic

Most microsimulation is static. Calculate what households owe or receive under current behavior, then calculate what they'd owe or receive under reform, assuming identical behavior. The difference is the "static" or "day-one" effect.

Static analysis is useful for many purposes. If you want to know how a reform redistributes income—who gains, who loses, by how much—static calculation answers that question. The distributional tables don't depend much on behavioral assumptions.

But static analysis misses some effects entirely. A carbon tax might raise $100 billion statically—but if people drive less in response, actual revenue is lower. The gap between static and dynamic estimates can be substantial.

### Labor Supply Responses

The most studied behavioral response is labor supply. How much do people adjust their work when tax rates change?

Economists parameterize this as "elasticities"—the percentage change in hours worked for a 1% change in after-tax wages. Decades of research estimates these parameters from natural experiments, tax reforms, and survey data.

The consensus: elasticities vary dramatically by population. Primary earners in married couples have low elasticities—they work about the same regardless of tax rates. Secondary earners and single parents have higher elasticities—tax changes do affect their labor supply decisions. The very wealthy may have the highest elasticities of all, though estimates vary widely.

Integrating elasticities into microsimulation requires specifying which populations respond how much, then adjusting their simulated earnings accordingly. A reform raising marginal rates on high earners might show 10% less revenue dynamically than statically, as those earners reduce labor supply.

PolicyEngine implements several labor supply response models. Users can choose between no response (static), CBO-style elasticities, or custom parameters. The interface shows how different assumptions affect revenue estimates—making the uncertainty explicit rather than hidden.

### Beyond Labor Supply

Labor supply is just one dimension. Other behavioral responses matter too:

**Portfolio reallocation.** Capital gains taxes affect when people sell assets. Higher rates encourage holding assets longer; lower rates encourage realizing gains. This timing response can dramatically affect year-to-year revenue.

**Tax planning.** Changes to tax rules prompt restructuring—shifting income between years, reclassifying income types, using new deductions. The responses to the 2017 Tax Cuts and Jobs Act showed how quickly sophisticated taxpayers adapt.

**Program take-up.** Expanding benefit eligibility doesn't mean everyone eligible will enroll. Take-up rates for programs like SNAP and EITC run well below 100%. Reforms increasing benefits might increase take-up; reforms adding complexity might decrease it.

**Firm responses.** Corporate tax changes affect business decisions—investment, location, compensation structure. These responses take time to materialize but can dominate long-run effects.

### The Structural Alternative

Elasticity-based responses assume we know how people respond. An alternative: build models that derive responses from underlying preferences.

Structural models specify what people maximize—utility from consumption and leisure, subject to budget constraints. Solve the optimization problem, and behavior emerges. Change the tax schedule, re-solve the problem, and the behavioral response emerges too.

The advantage: structural models can extrapolate to policies outside historical experience. If we've never seen a 90% marginal tax rate, elasticities estimated from lower rates may not apply. A structural model can still compute optimal responses to novel policies.

The disadvantage: structural models require strong assumptions about preferences and optimization behavior. People may not actually maximize expected utility. The functional forms may be wrong. Computational complexity increases dramatically.

PolicyEngine doesn't currently implement structural behavioral responses—the models require specialized expertise and substantial computational resources. But the architecture supports adding them as modules that process the same household data.

---

## Why Three Ingredients?

This three-part framework organizes how to think about microsimulation models. When evaluating a model—or building one—ask three questions:

**Rules:** Are the policy calculations correct? Have they been validated against official sources? Are edge cases handled appropriately? Can you read and understand the logic?

**Data:** Does the microdata represent the population accurately? Have missing variables been filled appropriately? Have weights been calibrated to administrative totals? Are the statistical matching and imputation assumptions defensible?

**Dynamics:** What behavioral assumptions does the model make? Are they explicit or hidden? How sensitive are results to different assumptions? Are static and dynamic estimates clearly distinguished?

Different models emphasize different ingredients. TAXSIM's strength is rules accuracy—decades of validation against actual tax returns. Tax-Data's strength is microdata construction—careful statistical matching and calibration. OG-USA's strength is dynamics—a full overlapping-generations model with computed behavioral responses.

PolicyEngine aims to be strong across all three. We invested heavily in rules encoding (comprehensive UK and US tax-benefit systems), microdata construction (the Enhanced CPS with statistical matching and gradient descent calibration), and behavioral options (elasticity-based labor supply responses with transparent parameters).

But no model is complete. Rules lag legislative changes. Data has irreducible limitations. Behavioral parameters remain uncertain. The honest model acknowledges these limitations rather than hiding them.

---

## The Integration Challenge

The three ingredients don't just coexist—they interact.

Rules affect data requirements. A model encoding capital gains taxes needs microdata with asset information. A model encoding childcare subsidies needs microdata with childcare expenses and provider locations. The rules you want to simulate determine what data you must construct.

Data affects rule implementation. Limited data forces simplifying assumptions. If your microdata lacks itemized deduction detail, you can't simulate deduction-specific reforms accurately. The model's capabilities are bounded by available data.

Dynamics affect both. Behavioral responses change effective rates, which change distributional impacts, which change the policy story. A reform that looks progressive statically might look regressive dynamically if high earners respond more than low earners.

Building a microsimulation model means making these pieces work together. Rules must handle whatever data exists. Data must support whatever rules matter. Dynamics must be calibrated to make sense with both. The integration is harder than any individual piece.

This is why building PolicyEngine took years, not months. Not because any single calculation was complex—individual tax formulas are straightforward. But because making comprehensive rules work with realistic data while supporting flexible dynamics requires sustained engineering effort across all three dimensions simultaneously.

---

## References

```{bibliography}
:filter: docname in docnames
```

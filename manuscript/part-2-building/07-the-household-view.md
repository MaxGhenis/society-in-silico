# Chapter 7: The Household View

Consider a single parent in New York with one child who has a disability. They earn $30,000 per year.

How much do they owe in taxes? How much do they receive in benefits? What happens if they get a raise?

These are not abstract questions. They determine whether this parent can afford rent, whether they should take on extra shifts, whether a job offer across town is worth pursuing. The answers involve federal income tax, state income tax, payroll taxes, the Earned Income Tax Credit, the Child Tax Credit, Supplemental Security Income, SNAP benefits, and a dozen other programs—each with its own rules, phase-outs, and interactions.

No one can calculate this in their head. Most accountants would struggle. Yet these calculations affect every financial decision the parent makes.

This is the problem PolicyEngine's household calculator was designed to solve {cite}`policyengine2022ssi`.

---

## The Invisible Labyrinth

Americans interact with a tax-benefit system of staggering complexity. A typical low-income family might simultaneously receive the federal Earned Income Tax Credit (phased by income and number of children), the Child Tax Credit (partially refundable, phased by income), SNAP benefits (with categorical eligibility plus an income test that varies by state), Supplemental Security Income for a disabled family member, Medicaid, housing assistance through local voucher programs, state child care subsidies, and free school meals. That's eight programs, each with its own definition of income, its own household unit, and its own phase-out schedule.

Each was designed independently. Each has its own definition of "income," its own household unit, its own phase-out schedule. The interactions are not coherent—they are accretions of decades of legislation, regulation, and administrative convenience.

The result is a system that no participant fully understands. Caseworkers specialize in one program. Tax preparers specialize in one side of the ledger. Benefits counselors know eligibility rules but not tax implications. No one sees the whole picture.

Until now, no tool existed for ordinary people to see that picture either.

---

## What Do I Owe? What Do I Get?

PolicyEngine's household calculator begins with a simple promise: enter your circumstances, and we'll show you your taxes and benefits under current law.

The interface walks users through questions about their household: How many adults? How many children? What ages? Then income: wages, self-employment, investments, retirement. Then specifics: housing costs, childcare expenses, disability status.

From these inputs, the calculator computes dozens of outputs. Federal income tax. State income tax (in supported states). Payroll taxes. The alphabet soup of credits—EITC, CTC, CDCTC. Benefit programs—SNAP, SSI, Medicaid eligibility. Housing calculations where relevant.

The result appears as a detailed breakdown: here is what you pay, here is what you receive, here is your net income after all transfers {cite}`policyengine2022review`.

This isn't just convenience. It's a form of empowerment. When you can see the complete calculation, you can plan. You can understand why a raise might not increase your take-home pay as much as expected. You can identify programs you're eligible for but not receiving.

The scope is significant. PolicyEngine's US model covers federal income tax, payroll taxes, the Earned Income Tax Credit, the Child Tax Credit, SNAP, SSI, WIC, TANF, and dozens of other federal and state programs. The UK model covers income tax, National Insurance, Universal Credit, Child Benefit, and the full suite of means-tested benefits. Each program is coded as a separate module, following rules extracted from legislation, regulation, and agency guidance.

The comprehensiveness matters because programs interact. A family's SNAP benefits depend on their net income after taxes and other deductions. Their tax liability depends on credits that depend on whether they have qualifying children—the same children who might generate SSI payments or child care subsidies. Change one variable and the effects ripple through the system. No single-program calculator captures these interactions. PolicyEngine does, because the microsimulation engine evaluates all programs simultaneously for each household.

---

## The Cliff Problem

The most revealing feature of the household calculator is the earnings chart. Plot net income against earnings, and the hidden structure of the tax-benefit system becomes visible.

For many low-income households, this chart is not a smooth upward slope. It has flat regions where higher earnings don't increase net income. It has downward slopes where higher earnings actually *reduce* net income. It has vertical drops—cliffs—where crossing an income threshold means losing benefits worth more than the additional earnings {cite}`policyengine2023cliffs`.

Consider the New York parent from our opening. At $20,000 in earnings, they receive significant SNAP benefits and SSI for their disabled child. At $45,000 in earnings, they lose categorical SNAP eligibility—a cliff worth thousands of dollars. The parent who earns $45,000 may have less disposable income than the parent who earns $20,000.

This is the "benefit cliff" or "welfare cliff" that policy analysts have worried about for decades. But until tools like PolicyEngine made it visible, most people affected by cliffs never saw them coming.

> "The cliff is a phenomenon that occurs when an individual is worse off when their income rises, due to the government withdrawing benefits and/or levying taxes."

PolicyEngine quantifies this visibility. Users see an "earnings dead zone"—a shaded region showing where additional work would make them worse off. The marginal tax rate chart shows the same information differently: spikes in the rate that sometimes exceed 100%.

---

## Marginal Tax Rates: The Hidden Incentive

Economists care about marginal tax rates because they affect behavior. If you keep 90 cents of your next dollar earned, you might work more. If you keep only 20 cents, you might not.

For high earners, marginal tax rates are discussed extensively—the top federal rate of 37%, state rates, capital gains rates. But here's the counterintuitive reality: low-income workers often face marginal rates that exceed what any billionaire pays, because benefit phase-outs stack on top of taxes.

Consider a single parent earning $30,000 with a child receiving SSI. They face federal and state income taxes, payroll taxes, EITC phase-out, SSI phase-out (50 cents per dollar), and SNAP phase-out (30 cents per dollar). Stack these together and the marginal rate approaches 90%—more than double the top rate a hedge fund manager pays on their last dollar of income.

This isn't an edge case. The mechanics are structural: SNAP benefits phase out at roughly 30 cents per dollar of additional net income. The EITC phases out at 21 cents per dollar for families with children. SSI phases out at 50 cents. State programs add more. At certain income ranges, a worker faces combined marginal rates that would provoke outrage if imposed on the wealthy.

PolicyEngine makes these rates visible. The marginal tax rate chart shows users exactly what happens when they earn more: at $20,000, their marginal rate might be 40%. At $30,000, it might spike to 70%. At $45,000, it might briefly exceed 100% as they hit a cliff.

This visibility serves two purposes. For individuals, it helps with financial planning—knowing where the cliffs are before you fall off them. For policymakers, it reveals the unintended consequences of well-meaning programs that, in combination, create work disincentives.

---

## The What-If Machine

But PolicyEngine isn't just a calculator for current law. Its power comes from letting users change the rules.

Click into the policy editor, and you can adjust any parameter in the model. Raise the EITC maximum. Eliminate the benefit cliff in SNAP. Add a child allowance. Convert the Child Tax Credit to full refundability. Set a universal basic income. Flatten the income tax. The reform space is as broad as the model's coverage.

Then return to your household, and see what changes.

This is the "what if" that wasn't previously possible for ordinary people. What if Congress reformed the CTC? Here's what it would mean for your family. What if your state expanded its EITC? Here's the impact on your take-home pay. What if a candidate's tax plan were enacted? Here's the bottom line for your household.

The visualizations update in real time. The net income chart shows baseline in gray, reform in blue. Two sets of earnings dead zones appear, revealing whether the reform helps or hurts work incentives for your specific situation. The marginal tax rate chart shows both lines stacked, making it immediately visible where a reform smooths out the benefit system or creates new cliffs.

This isn't abstract policy analysis. It's your life, under different rules.

Consider a concrete example. In 2021, Congress temporarily expanded the Child Tax Credit from $2,000 to $3,600 per child under six and $3,000 per child ages 6-17. The credit was also made fully refundable—families who owed no federal income tax could still receive the full amount. For a single parent earning $15,000 with two young children, this wasn't a marginal change. Under the old CTC, they received roughly $1,800 (limited by the 15% phase-in rate on earnings above $2,500). Under the expansion, they received $7,200. PolicyEngine could show this difference instantly—not as a policy brief about national averages, but as a specific dollar amount for a specific family.

When the expansion expired at the end of 2021, PolicyEngine could show that same family's income dropping by over $5,000. The tool made visible what policy debates often obscure: the concrete financial impact of legislative choices on real households.

---

## Real Cases, Real Complexity

The household view reveals complexity that aggregate statistics hide.

**Case 1: The SSI phase-out.** Supplemental Security Income for disabled individuals phases out at 50 cents per dollar of earnings above certain thresholds. A reform increasing the earnings exclusion to 75% would reduce SSI's marginal rate to 25%. For individuals with disabilities, this could mean the difference between working being worthwhile or not.

**Case 2: The SNAP categorical cliff.** Receiving SSI provides categorical eligibility for SNAP—you qualify regardless of income. But once SSI phases out, you lose categorical eligibility and must meet SNAP's own income test. This creates a cliff at precisely the income level where you're trying to become self-sufficient.

**Case 3: State credit stacking.** Washington's Working Families Tax Credit begins phasing out $5,000 below where the federal EITC phases out, creating an additional marginal tax rate of 12-24% that stacks on top of federal rates {cite}`policyengine2023cliffs`.

Each case represents millions of real households making real decisions. The household view makes the specific impacts calculable for any individual's circumstances.

---

## The UK Household View

The household calculator originated in the UK, where PolicyEngine launched in 2021 before expanding to the US {cite}`ubicenter2021policyengine`. The UK model carries a different flavor because the tax-benefit system is different—more centralized, with Universal Credit replacing several legacy benefits, and a national health service that removes healthcare from the calculation.

But the UK version demonstrated something the US version later confirmed: the household view is most powerful when the system is most complex.

Universal Credit, the UK's flagship welfare reform, was designed to simplify the benefit system by combining six legacy benefits into one. In practice, it introduced its own complexities. The UC taper rate—the rate at which benefits are withdrawn as income rises—interacts with income tax, National Insurance, council tax support, and student loan repayment to create marginal rates that can exceed 70% for some working families.

PolicyEngine UK made these interactions visible. When Chancellor Rishi Sunak reduced the UC taper rate from 63% to 55% in the 2021 Autumn Budget, PolicyEngine could show exactly what this meant for specific household types: a single parent working 25 hours per week at minimum wage would keep an additional £1,000 per year. A couple with children where one partner worked full-time would see a smaller gain. The distributional effects varied enormously by household composition—details that aggregate statistics masked.

When Prime Minister Liz Truss announced sweeping tax cuts in September 2022, PolicyEngine produced household-level distributional analysis within hours—a rapid response enabled by the infrastructure described in Chapter 8.

As Chapter 5 described, HM Treasury eventually published a formal evaluation of PolicyEngine UK {cite}`hmt2025policyengine`. The household calculator that started as a research prototype had become something government took seriously enough to benchmark against their own internal models.

---

## Trust But Verify

PolicyEngine's household calculations come with a caveat displayed prominently: "PolicyEngine provides estimates only; they do not confer benefit eligibility" {cite}`policyengine2022ssi`.

This caveat reflects an important limitation. The model encodes rules as we understand them from legislation and regulation. But actual benefit determinations involve discretion, documentation, and administrative processes that no model fully captures. Asset tests may apply that users don't enter. Categorical requirements may not be met. Local variations may differ from our understanding of state rules.

The household calculator is not a replacement for official agency calculators or professional advice. It's a tool for understanding and exploration—one that's far more comprehensive than what existed before, but still an approximation.

The team invests heavily in validation, comparing results to official calculators and published tables {cite}`policyengine2024ukvalidation`. Where discrepancies appear, they trigger investigation and often improvement. But perfect accuracy is unattainable in a system this complex.

This honest uncertainty matters. The alternative—black-box calculations that claim false precision—would be worse. By showing the model's logic transparently, PolicyEngine allows users to judge whether the calculation matches their understanding of their own situation.

---

## From Households to Society

The household view is powerful for individuals. But policy doesn't affect just one household—it affects millions. The question of whether a reform helps "people like you" requires knowing how many people are like you, and how differently they're affected.

This is where the household view connects to the society view. The same microsimulation engine that calculates your personal impact can calculate the impact on a representative sample of the entire population. Your situation becomes one data point in a statistical picture.

That statistical picture—budget costs, poverty impacts, distributional effects—is the subject of the next chapter. But it rests on the foundation of the household view: the ability to correctly calculate how any specific policy affects any specific family.

Without that household-level accuracy, the society-level estimates would be meaningless. Microsimulation works precisely because it gets the individual calculations right, then aggregates them appropriately. This is what distinguishes microsimulation from macroeconomic modeling. A macro model might estimate that a tax cut costs $100 billion and increases GDP by 0.3%. A microsimulation model can also tell you that the same tax cut gives $12,000 to a high-income household in Connecticut and $200 to a low-income household in Mississippi—and that the Mississippi household faces a higher marginal rate afterward because the cut pushed them into a benefit phase-out zone. The aggregate numbers emerge from millions of individual calculations, each grounded in actual rules applied to actual circumstances.

The household view is not just a user-friendly interface. It's the verification that the underlying model works—visible to anyone who cares to check. Every user who runs their own scenario and recognizes the result as approximately correct provides an informal validation. Every user who finds an error and reports it improves the model. The household view makes microsimulation self-correcting in a way that aggregate models never are.

---

## References

```{bibliography}
:filter: docname in docnames
```

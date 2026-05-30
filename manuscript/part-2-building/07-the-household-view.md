# Chapter 7: The Household View

Consider a single parent in New York with one child who has a disability. They earn $30,000 per year.

How much do they owe in taxes? How much do they receive in benefits? What happens if they get a raise?

These are not abstract questions. They determine whether this parent can afford rent, whether they should take on extra shifts, whether a job offer across town is worth pursuing. The answers involve federal income tax, state income tax, payroll taxes, the Earned Income Tax Credit, the Child Tax Credit, Supplemental Security Income, SNAP benefits, and a dozen other programs—each with its own rules, phase-outs, and interactions.

No one can calculate this in their head. Most accountants would struggle. Yet these calculations affect every financial decision the parent makes.

This is the problem PolicyEngine's household calculator was designed to solve [@policyengine2022ssi].

---

## The Invisible Labyrinth

Americans interact with a tax-benefit system of staggering complexity. A typical low-income family might simultaneously receive the federal Earned Income Tax Credit (phased by income and number of children), the Child Tax Credit (partially refundable, phased by income), SNAP benefits (with categorical eligibility plus an income test that varies by state), Supplemental Security Income for a disabled family member, Medicaid, housing assistance through local voucher programs, state child care subsidies, and free school meals. That's eight programs, each designed independently, each with its own definition of "income," its own household unit, its own phase-out schedule. The interactions are not coherent—they are accretions of decades of legislation, regulation, and administrative convenience.

The result is a system that no participant fully understands. Caseworkers specialize in one program. Tax preparers specialize in one side of the ledger. Benefits counselors know eligibility rules but not tax implications. No one sees the whole picture.

Few tools let ordinary people see the whole picture—taxes and benefits together, with all the interactions.

---

## What Do I Owe? What Do I Get?

PolicyEngine's household calculator begins with a simple promise: enter your circumstances, and we'll show you your taxes and benefits under current law.

The interface walks users through questions about their household: How many adults? How many children? What ages? Then income: wages, self-employment, investments, retirement. Then specifics: housing costs, childcare expenses, disability status.

From these inputs, the calculator computes dozens of outputs. Federal income tax. State income tax (in supported states). Payroll taxes. The alphabet soup of credits—EITC, CTC, CDCTC. Benefit programs—SNAP, SSI, Medicaid eligibility. Housing calculations where relevant.

The result appears as a detailed breakdown: here is what you pay, here is what you receive, here is your net income after all transfers [@policyengine2022review].

This isn't just convenience. It's a form of empowerment. When you can see the complete calculation, you can plan. You can understand why a raise might not increase your take-home pay as much as expected. You can identify programs you're eligible for but not receiving.

The scope is significant. PolicyEngine's US model covers federal income tax, payroll taxes, the Earned Income Tax Credit, the Child Tax Credit, SNAP, SSI, WIC, TANF, and dozens of other federal and state programs. The UK model covers income tax, National Insurance, Universal Credit, Child Benefit, and the full suite of means-tested benefits. Each program is coded as a separate module, following rules extracted from legislation, regulation, and agency guidance.

The comprehensiveness matters because programs interact. A family's SNAP benefits depend on their net income after taxes and other deductions. Their tax liability depends on credits that depend on whether they have qualifying children—the same children who might generate SSI payments or child care subsidies. Change one variable and the effects ripple through the system. No single-program calculator captures these interactions. PolicyEngine does, because the microsimulation engine evaluates all programs simultaneously for each household.

---

## The Cliff Problem

The most revealing feature of the household calculator is the earnings chart. Plot net income against earnings, and the hidden structure of the tax-benefit system becomes visible.

For many low-income households, this chart is not a smooth upward slope. It has flat regions where higher earnings don't increase net income. It has downward slopes where higher earnings actually *reduce* net income. It has vertical drops—cliffs—where crossing an income threshold means losing benefits worth more than the additional earnings [@policyengine2023cliffs].

Consider the New York parent from our opening. As their earnings climb from $20,000 toward $30,000, several benefits taper at once—SNAP, the Earned Income Tax Credit, and reductions in their child's SSI—while income and payroll taxes begin to bite. Across that band, an extra dollar of earnings can leave the family with as little as twenty cents. Take-home pay keeps inching upward, but barely: work that should move the family forward instead runs it into a wall. For households positioned closer to a hard threshold, the wall becomes a true cliff—lose categorical eligibility for a program, or cross the childcare-subsidy or Medicaid limit, and net income can actually fall as earnings rise [@policyengine2023cliffs].

This is the "benefit cliff" or "welfare cliff" that policy analysts have worried about for decades. But until tools like PolicyEngine made it visible, most people affected by cliffs never saw them coming.

> "The cliff is a phenomenon that occurs when an individual is worse off when their income rises, due to the government withdrawing benefits and/or levying taxes."

PolicyEngine quantifies this visibility. Users see an "earnings dead zone"—a shaded region showing where additional work raises net income by almost nothing, or, past a true cliff, lowers it. The marginal tax rate chart shows the same information differently: spikes in the rate that, at a genuine cliff, exceed 100%.

---

## Marginal Tax Rates: The Hidden Incentive

Economists care about marginal tax rates because they affect behavior. If you keep 90 cents of your next dollar earned, you might work more. If you keep only 20 cents, you might not.

For high earners, marginal tax rates are discussed extensively—the top federal rate of 37%, state rates, capital gains rates. But here's the counterintuitive reality: low-income workers often face marginal rates that exceed what any billionaire pays, because benefit phase-outs stack on top of taxes.

Consider that same New York parent as their earnings approach $30,000. They face federal and state income taxes, payroll taxes, the EITC phase-out, the SNAP phase-out, and reductions in their child's SSI as income rises. Stack these together and the marginal rate can approach 80%—more than double the top rate a hedge fund manager pays on their last dollar of income.

This isn't an edge case. The mechanics are structural: SNAP benefits phase out at roughly 30 cents per dollar of additional net income. The EITC phases out at about 16 cents per dollar for a family with one child, and 21 cents for two or more. SSI falls by roughly 50 cents for every dollar of countable income. State programs add more. At certain income ranges, a worker faces combined marginal rates that would provoke outrage if imposed on the wealthy.

PolicyEngine makes these rates visible. The marginal tax rate chart shows users exactly what happens when they earn more: a rate that might sit near 30% at $15,000, then climb toward 80% in the band where benefits phase out together. For a household sitting right at a true cliff, the chart shows the marginal rate spike past 100%—the unmistakable signature of earning more and keeping less.

This visibility serves two purposes. For individuals, it helps with financial planning—knowing where the cliffs are before you fall off them. For policymakers, it reveals the unintended consequences of well-meaning programs that, in combination, create work disincentives.

---

## The What-If Machine

But PolicyEngine isn't just a calculator for current law. Its power comes from letting users change the rules.

Click into the policy editor, and you can adjust any parameter in the model. Raise the EITC maximum. Eliminate the benefit cliff in SNAP. Add a child allowance. Convert the Child Tax Credit to full refundability. Set a universal basic income. Flatten the income tax. The reform space is as broad as the model's coverage.

Then return to your household, and see what changes.

This is the "what if" that wasn't previously possible for ordinary people. What if Congress reformed the CTC? Here's what it would mean for your family. What if your state expanded its EITC? Here's the impact on your take-home pay. What if a candidate's tax plan were enacted? Here's the bottom line for your household.

The visualizations update in real time. The net income chart shows baseline in gray, reform in blue. Two sets of earnings dead zones appear, revealing whether the reform helps or hurts work incentives for your specific situation. The marginal tax rate chart shows both lines stacked, making it immediately visible where a reform smooths out the benefit system or creates new cliffs.

The reform space is surprisingly deep. A user exploring basic income proposals, for example, can create a flat tax at any rate, a universal benefit at any amount, and immediately see how this simplification compares to the current system for their household. Do they come out ahead or behind? Does the marginal rate chart smooth out, eliminating the cliffs? Or does the reform create new problems—a higher average rate, or a loss of targeted benefits that the flat benefit doesn't replace?

For policymakers and their staff, this capability transforms how policy is designed. Rather than proposing a reform and waiting weeks for CBO or JCT to score it, a legislative aide can model dozens of variants in an afternoon. Set the benefit at $3,000 per child versus $4,000. Phase it in at $2,500 versus $0. Cap it at $75,000 versus $150,000. Each variant shows a different household impact chart, revealing design trade-offs that are invisible in legislative text but immediate in simulation.

This isn't abstract policy analysis. It's your life, under different rules.

Consider a concrete example. In 2021, Congress temporarily expanded the Child Tax Credit from $2,000 to $3,600 per child under six and $3,000 per child ages 6-17. The credit was also made fully refundable—families who owed no federal income tax could still receive the full amount. For a single parent earning $15,000 with two young children, this wasn't a marginal change. Under the old CTC, they received roughly $1,800 (limited by the 15% phase-in rate on earnings above $2,500). Under the expansion, they received $7,200. PolicyEngine could show this difference instantly—not as a policy brief about national averages, but as a specific dollar amount for a specific family.

When the expansion expired at the end of 2021, PolicyEngine could show that same family's income dropping by over $5,000. The tool made visible what policy debates often obscure: the concrete financial impact of legislative choices on real households.

---

## Real Cases, Real Complexity

The household view reveals complexity that aggregate statistics hide.

**Case 1: The SSI phase-out.** Supplemental Security Income for disabled individuals phases out at 50 cents per dollar of earnings above certain thresholds. A reform increasing the earnings exclusion to 75% would reduce SSI's marginal rate to 25%. For individuals with disabilities, this could mean the difference between working being worthwhile or not.

**Case 2: The SNAP categorical cliff.** Receiving SSI provides categorical eligibility for SNAP—you qualify regardless of income. But once SSI phases out, you lose categorical eligibility and must meet SNAP's own income test. This creates a cliff at precisely the income level where you're trying to become self-sufficient.

**Case 3: State credit stacking.** Washington's Working Families Tax Credit begins phasing out $5,000 below where the federal EITC phases out, creating an additional marginal tax rate of 12-24% that stacks on top of federal rates [@policyengine2023cliffs].

**Case 4: The marriage penalty.** Consider two single parents, each earning $25,000 with one child. Separately, each qualifies for substantial EITC and CTC benefits. If they marry, their combined $50,000 income pushes them into higher phase-out ranges for both credits. The EITC marriage penalty has been partially addressed by wider phase-out thresholds for married filers, but the interaction with state programs and benefit phase-outs means the combined household often receives less in total transfers than the two separate households did. PolicyEngine can show this precisely: enter the two individuals separately, note the total. Then enter them as a married couple, note the difference. The marriage penalty isn't always obvious from reading the tax code—it emerges from the interaction of multiple programs, each with its own treatment of household structure.

**Case 5: The aging-out cliff.** A family receiving SSI for a disabled child faces a transition when that child turns 18. SSI eligibility rules change from parents' income and resources to the individual's own—often resulting in higher SSI payments but loss of certain family-based benefits. At the same time, the child may age out of pediatric Medicaid provisions, school meal programs, and childcare subsidies. PolicyEngine can model these transitions by adjusting the child's age and watching the cascading effects across programs.

**Case 6: Self-employment and gig work.** Gig workers face a uniquely opaque tax situation. Their self-employment tax (15.3% on net earnings, covering both employer and employee shares of Social Security and Medicare) comes as a surprise to many. But the interaction with benefits is even less intuitive: self-employment income is treated differently by SNAP (which allows a standard deduction for self-employment expenses) and the EITC (which uses net self-employment income). A rideshare driver earning $40,000 gross with $12,000 in expenses has $28,000 in net self-employment income for EITC purposes, but the SNAP calculation may use a different figure. PolicyEngine handles these distinctions because it encodes each program's specific definition of income.

Each case represents millions of real households making real decisions. The household view makes the specific impacts calculable for any individual's circumstances.

---

## The UK Household View

The household calculator originated in the UK, where PolicyEngine launched in 2021 before expanding to the US [@ubicenter2021policyengine]. The UK model carries a different flavor because the tax-benefit system is different—more centralized, with Universal Credit replacing several legacy benefits, and a national health service that removes healthcare from the calculation.

But the UK version demonstrated something the US version later confirmed: the household view is most powerful when the system is most complex.

Universal Credit, the UK's flagship welfare reform, was designed to simplify the benefit system by combining six legacy benefits into one. In practice, it introduced its own complexities. The UC taper rate—the rate at which benefits are withdrawn as income rises—interacts with income tax, National Insurance, council tax support, and student loan repayment to create marginal rates that can exceed 70% for some working families.

PolicyEngine UK made these interactions visible. When Chancellor Rishi Sunak reduced the UC taper rate from 63% to 55% in the 2021 Autumn Budget, PolicyEngine could show exactly what this meant for specific household types: a single parent working 25 hours per week at minimum wage would keep an additional £1,000 per year. A couple with children where one partner worked full-time would see a smaller gain. The distributional effects varied enormously by household composition—details that aggregate statistics masked.

When Prime Minister Liz Truss announced sweeping tax cuts in September 2022, PolicyEngine produced household-level distributional analysis within hours—a rapid response enabled by the infrastructure described in Chapter 8.

As Chapter 5 described, HM Treasury eventually published a formal evaluation of PolicyEngine UK [@hmt2025policyengine]. The household calculator that started as a research prototype had become something government took seriously enough to benchmark against their own internal models.

---

## Trust But Verify

PolicyEngine's household calculations come with a caveat displayed prominently: "PolicyEngine provides estimates only; they do not confer benefit eligibility" [@policyengine2022ssi].

This caveat reflects an important limitation. The model encodes rules as we understand them from legislation and regulation. But actual benefit determinations involve discretion, documentation, and administrative processes that no model fully captures. Asset tests may apply that users don't enter. Categorical requirements may not be met. Local variations may differ from our understanding of state rules.

The household calculator is not a replacement for official agency calculators or professional advice. It's a tool for understanding and exploration—one that's far more comprehensive than what existed before, but still an approximation.

The team invests heavily in validation, comparing results to official calculators and published tables [@policyengine2024ukvalidation]. Where discrepancies appear, they trigger investigation and often improvement. But perfect accuracy is unattainable in a system this complex.

This honest uncertainty matters. The alternative—black-box calculations that claim false precision—would be worse. By showing the model's logic transparently, PolicyEngine allows users to judge whether the calculation matches their understanding of their own situation.

---

## From Calculator to Infrastructure

The household calculator began as a web tool for curious individuals. It became something more when other organizations started building on top of it.

In 2025, MyFriendBen—a benefits screening platform—launched in North Carolina, Illinois, Colorado, and New York using PolicyEngine's API as its calculation engine [@policyengine2025myfriendben]. The platform asks users a series of questions in plain language, available in 12 languages, then calls the same household calculation engine that powers the PolicyEngine website. In about six minutes, users see which programs they're likely eligible for and approximately how much they'd receive.

The results were striking. In Colorado, MyFriendBen reported that users surfaced an average of $1,500 per month in benefits they appeared eligible for but had not claimed [@myfriendben2025pueblo]. PolicyEngine's own launch note reported that the personalized estimates matched expected amounts more than 90 percent of the time—a self-reported figure, not an independent audit [@policyengine2025myfriendben]. The mechanism is the same comprehensive calculation that PolicyEngine's household view performs: evaluating programs together, accounting for interactions, and catching eligibility that single-program screeners miss.

This represents a shift from the household view as analysis tool to the household view as infrastructure. The underlying calculation—given these household characteristics, compute all taxes and benefits—is the same whether it's called by a curious policy wonk on policyengine.org or by a benefits navigator helping a family in Charlotte. The API exposes the same logic, the same parameters, the same interactions.

The next step is to make household simulation event-based rather than form-based. Crossroads, a PolicyEngine prototype, frames the calculation around life events: having a child, becoming pregnant, moving, getting married, losing a job, retiring, turning 65, or watching a child age out of eligibility thresholds [@policyengine2026crossroads]. That interface matches how people actually experience policy. They do not wake up wanting to edit tax parameters. They ask whether a baby, a move, or a raise will change their taxes, benefits, health coverage, and net income.

Other organizations built on the same foundation. The Gary Community Ventures in Colorado integrated PolicyEngine calculations into their financial coaching tools. The Fund for Guaranteed Income used the API to show pilot program participants how their guaranteed income payments would interact with existing benefits—critical information, since participants needed to know whether accepting a cash transfer would reduce their SNAP or SSI benefits dollar-for-dollar.

The household view, it turned out, was not just a product feature. It was a primitive—a basic computation that many different applications needed. Benefits screening, financial coaching, guaranteed income pilot design, tax preparation assistance, legislative staff analysis: all variations on the same question. "Given this household, what are their taxes and benefits?"

---

## From Households to Society

The household view is powerful for individuals. But policy doesn't affect just one household—it affects millions. The question of whether a reform helps "people like you" requires knowing how many people are like you, and how differently they're affected.

This is where the household view connects to the society view. The same microsimulation engine that calculates your personal impact can calculate the impact on a representative sample of the entire population. Your situation becomes one data point in a statistical picture.

That statistical picture—budget costs, poverty impacts, distributional effects—is the subject of the next chapter. But it rests on the foundation of the household view: the ability to correctly calculate how any specific policy affects any specific family.

Without that household-level accuracy, the society-level estimates would be meaningless. Microsimulation works precisely because it gets the individual calculations right, then aggregates them appropriately. This is what distinguishes microsimulation from macroeconomic modeling. A macro model might estimate that a tax cut costs $100 billion and increases GDP by 0.3%. A microsimulation model can also tell you that the same tax cut gives $12,000 to a high-income household in Connecticut and $200 to a low-income household in Mississippi—and that the Mississippi household faces a higher marginal rate afterward because the cut pushed them into a benefit phase-out zone. The aggregate numbers emerge from millions of individual calculations, each grounded in actual rules applied to actual circumstances.

The household view is not just a user-friendly interface. It exposes the underlying model to anyone who cares to check—visible in a way aggregate estimates are not. When a user runs their own scenario and recognizes the result as roughly right, that is an informal sanity check; when a user spots an error and reports it, the model can be corrected. How much that feedback improves accuracy depends on how many people check and report—an informal supplement to systematic validation, not a substitute for it.

---

## References

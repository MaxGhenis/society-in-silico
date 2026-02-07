# Chapter 4: The Accuracy Question

In 2017, the Joint Committee on Taxation estimated the Tax Cuts and Jobs Act would reduce federal revenue by $1.46 trillion over ten years. The Penn Wharton Budget Model projected larger losses—$1.8 to $2.2 trillion on a dynamic basis, accounting for economic effects {cite}`pwbm2017tcja`. Congressional Republicans disputed both. Supply-siders predicted the tax cuts would pay for themselves through growth.

The supply-side fantasy didn't materialize. The microsimulations had been approximately right about the direction and magnitude.

But "approximately right" is the best we can honestly say.

---

## The Trust Question

Throughout the 1990s and 2000s, microsimulation models grew more sophisticated. The IFS refined TAXBEN. The Urban Institute expanded TRIM3. Policy shops on both sides produced analyses supporting their preferred conclusions.

And a reasonable observer might ask: *Do these things actually work?*

It's a fair question. The models are complex. Their assumptions are buried in code. Their data sources are imperfect. And different models, given the same reform, sometimes produce different answers.

The honest response isn't "trust us"—it's "here's how we test ourselves."

---

## What Validation Means

Microsimulation validation happens at three levels:

**Component validation**: Do the individual calculations match the rules? If the model says a married couple with $100,000 income owes a specific amount in federal taxes, is that right? This is straightforward to check—you can verify against IRS worksheets or tax preparation software.

**Aggregate validation**: When the model sums across the population, does it match administrative totals? If a model estimates total SNAP recipients, does that match USDA administrative data? If it estimates total federal income tax revenue, does that match IRS collections?

**Predictive validation**: When the model predicts effects of changes, do those predictions hold up? This is hardest—you rarely get clean experiments. Policy changes come bundled with economic shifts, other reforms, and behavioral responses that weren't anticipated.

Good models pass the first two levels reliably. The third is where humility enters.

---

## The ACA Test Case

The Affordable Care Act provides one of the best natural experiments for testing microsimulation accuracy.

In March 2010, CBO predicted the ACA would reduce the non-elderly uninsured rate from over 18 percent to about 7.6 percent by 2016. This assumed all states would adopt Medicaid expansion {cite}`collins2015aca`.

Then the Supreme Court made Medicaid expansion optional, and 19 states declined. Adjusting for this, CBO's projected uninsured rate for 2016 becomes 9.4 percent. The actual rate, according to CDC data, was 10.4 percent {cite}`kiely2017aca`.

That's remarkably close—within one percentage point—given a six-year forecast horizon and a major legal disruption.

But the aggregate accuracy masked component errors:

| Coverage Source | CBO 2010 Prediction | Actual 2016 |
|-----------------|---------------------|-------------|
| Exchange enrollment | 21-23 million | 10.4 million |
| Medicaid expansion | 10 million | 14.4 million |
| Total uninsured | 30 million | 27.9 million |

Source: {cite}`collins2015aca`, {cite}`kiely2017aca`

CBO overestimated exchange enrollment by more than half. They underestimated Medicaid enrollment by nearly 50%. Yet the total coverage gain was roughly correct because the errors partially canceled.

As one analysis put it: "CBO's mistake was in estimating *where* the uninsured would get covered, not *how many* of them would gain coverage" {cite}`collins2015aca`.

---

## Are Forecasts Improving?

Here's a question rarely asked: Is government forecasting getting *better* over time?

CBO publishes systematic retrospectives comparing their projections to actual outcomes—an unusual level of institutional honesty {cite}`cbo2024deficit`. The data reveals a striking pattern.

For sixth-year deficit projections (the medium-term forecasts that guide major policy debates):

| Period | Average Absolute Error (% of GDP) |
|--------|-----------------------------------|
| 1989-2001 | 3.2% |
| 2002-2019 | 1.0% |

That's a **threefold improvement** in forecast accuracy over two decades {cite}`cbo2024deficit`.

What drove this? Better data—the IRS now provides richer administrative records. Better computing—models can handle more complexity. Better methods—decades of retrospective analysis revealed systematic biases that could be corrected.

But the improvement has limits. CBO's 2025 forecasting record shows their projections remain roughly as accurate as the Blue Chip consensus (an average of 50 private-sector forecasts) and the Administration's forecasts {cite}`cbo2025forecasting`. No one has found a way to consistently outperform the collective wisdom of informed forecasters.

And recent years have shown increased volatility. The 2021 projection had CBO's largest *over*estimate on record. The 2023 projection had the largest *under*estimate—an error of 3.9% of GDP, more than three times the historical average {cite}`cbo2024deficit`. The pandemic scrambled all forecasting models.

### The Random Walk Challenge

Perhaps the most humbling finding comes from academic research. A Berkeley thesis examining CBO forecasts from 1976 to 2007 found that a "random walk" projection—simply assuming next year's deficit equals this year's—would have outperformed CBO on average for both short and medium-term forecasts {cite}`inayatali2023cbo`.

This doesn't mean CBO is incompetent. It means economic forecasting faces irreducible uncertainty. The events that matter most—recessions, financial crises, pandemics—are precisely the events that cannot be predicted. Models calibrated on normal times fail when abnormal times arrive.

### The TCJA Tracking

For the Tax Cuts and Jobs Act specifically, we now have seven years of data. Real (inflation-adjusted) revenue for 2018 through 2024—excluding the anomalous 2022 pandemic spike—came in within 0.5% of CBO's 2018 projections {cite}`crfb2024tcja`.

That's remarkably accurate for a major tax overhaul. The supply-side claims that tax cuts would pay for themselves proved false. The microsimulation estimates proved roughly correct.

---

## The Prediction Market Benchmark

There's another approach to forecasting that sidesteps models entirely: prediction markets. Instead of building simulations, let people bet money on outcomes. The market price becomes the forecast.

The logic is compelling. Markets aggregate dispersed information. Participants have "skin in the game"—wrong predictions cost money. And unlike experts with reputations to protect, markets can update quickly when new information arrives.

How do prediction markets compare to official forecasts?

**For macroeconomic variables**, an NBER study found that prediction markets were "weakly more accurate than survey forecasts" across GDP, inflation, and employment {cite}`wolfers2012prediction`. The advantage was modest but consistent.

**For elections**, the evidence is striking. In the 2024 presidential race, polls showed a coin flip. Polymarket had Trump at 58% the Monday before Election Day—a prediction that proved far more accurate {cite}`polymarket2024election`. Academic studies found prediction markets outperformed FiveThirtyEight's model in 2018 and 2020 {cite}`crane2020prediction`.

**For Fed decisions**, Good Judgment's "superforecasters"—individuals identified through forecasting tournaments as exceptionally calibrated—beat financial futures markets by 30% in 2024-2025 {cite}`goodjudgment2024`.

Philip Tetlock's research revealed the key insight: most experts forecast little better than chance {cite}`tetlock2005expert`. But a small subset—about 2% of participants in the subsequent Good Judgment Project—consistently outperform. These superforecasters share traits: they update frequently, think probabilistically, and avoid ideological commitment to specific predictions {cite}`tetlock2015superforecasting`.

What does this mean for microsimulation?

First, it suggests a validation opportunity. When prediction markets exist for policy-relevant questions—will inflation exceed 3%? will unemployment rise?—microsimulation forecasts can be benchmarked against market prices.

Second, it reveals a limitation. Prediction markets work for questions with clear resolution dates and objective outcomes. They can't easily handle "what would happen under a counterfactual policy that was never implemented?" That's precisely where microsimulation shines.

Third, it points toward synthesis. The best forecasts might combine simulation-based analysis with market-aggregated beliefs. CBO produces structural estimates; prediction markets provide calibration checks; the combination improves on either alone.

---

## The Survey Data Crisis

Before we can assess whether models produce accurate outputs, we need to ask whether their inputs are accurate. The answer is troubling.

Bruce Meyer, an economist at the University of Chicago, has spent two decades documenting what he calls a crisis in household survey data {cite}`meyer2015underreporting`. The problem is straightforward: people don't accurately report their income and benefits to survey takers. And the underreporting isn't random—it's systematically biased in ways that distort policy analysis.

The numbers are stark. When Meyer and colleagues linked survey responses to administrative records, they found that roughly 40-50% of SNAP recipients didn't report receiving benefits in the Current Population Survey. Over 60% of Temporary Assistance for Needy Families (TANF) and General Assistance went unreported. About a third of housing assistance recipients didn't mention it. Even Social Security—arguably the simplest transfer to remember, since it arrives monthly—was underreported by roughly 10% of recipients.

This isn't just an academic concern. It cascades through every model built on survey data.

Consider what happens when a microsimulation model tries to estimate the poverty impact of SNAP. The model assigns SNAP benefits to households that appear eligible based on their survey-reported income. But if half of actual SNAP recipients didn't report receiving benefits—and therefore may also have misreported income or household composition—the model is working with a distorted picture of who gets SNAP, how much they get, and what their financial circumstances actually look like.

The underreporting has gotten worse over time. Survey response rates have declined steadily since the 1990s. The people who don't respond aren't random—they're disproportionately low-income, young, and mobile. The Census Bureau fills in missing data through imputation—statistical inference about what non-responders would have said. But imputed values carry their own biases, and as the imputed share grows, surveys increasingly reflect the models used to fill gaps rather than actual household circumstances.

The problem runs in both directions. Seniors systematically underreport retirement income. A Census Bureau study linking CPS responses to IRS and Social Security Administration records found that median income for those 65 and older was 30% higher in administrative data than in survey reports {cite}`census2017retirement`. The result: CPS-based poverty rates for seniors—9.1%—were 2.2 percentage points higher than rates calculated from validated administrative records, which showed 6.9%. Senior poverty is real, but the headline survey numbers overstate it.

High incomes are top-coded in public-use data—values above a threshold are replaced with that threshold to protect confidentiality. This compresses the income distribution at the top, making policies that affect high earners harder to model accurately. The CPS top-codes individual earnings at around $1.1 million, meaning a household earning $2 million looks identical to one earning $1.1 million.

These data problems affect every microsimulation model that relies on household surveys—which is nearly all of them. The government models with access to confidential IRS data avoid some of these issues, but even they face challenges: tax returns miss non-filers, don't capture non-taxable transfers, and reflect legal tax units rather than economic households.

The honest assessment: microsimulation models are only as good as their data, and their data is imperfect in systematic, consequential ways.

---

## TAXSIM: The Academic Benchmark

TAXSIM, the NBER tax calculator introduced in Chapter 2, offers a useful validation benchmark. Because Feenberg maintained it for over four decades and over a thousand published papers cite it {cite}`feenberg1993taxsim`, widespread use created an informal validation network: if TAXSIM produced results that conflicted with a researcher's expectations, someone would investigate and report bugs. The model improved through collective scrutiny.

TAXSIM's accuracy for its core function—calculating federal income tax for a given set of inputs—is high. The rules are deterministic and well-documented. Where discrepancies arise, they typically involve edge cases in state tax codes or interactions with credits that have complex eligibility rules.

But TAXSIM covers taxes only—not benefits. It doesn't simulate SNAP, Medicaid, SSI, or housing assistance—the benefit programs that create the cliffs and interactions described in later chapters. And it calculates taxes for individual records; it doesn't produce aggregate revenue estimates or distributional tables. TAXSIM established that independent tools could match proprietary accuracy for well-defined calculations. The gap wasn't capability—it was scope.

---

## When Models Disagree

If microsimulation models are accurate, they should agree with each other. They often don't.

During the 2017 Tax Cuts and Jobs Act debate, four major institutions produced revenue estimates. JCT's static score: $1.46 trillion in revenue loss over ten years. Penn Wharton's dynamic estimate: $1.8 to $2.2 trillion. The Tax Foundation's dynamic model: roughly $1.0 trillion, reflecting their more optimistic assumptions about growth effects. TPC produced distributional analysis broadly consistent with JCT on revenue.

The range—from $1.0 trillion to $2.2 trillion—was enormous. All four institutions employed competent economists. All used microsimulation. Why did they disagree by a factor of two?

Three sources of divergence explain most cross-model disagreements:

**Data differences.** JCT uses confidential IRS tax return data—the most comprehensive source available. TPC uses public-use IRS data, which is less granular. The Tax Foundation and PWBM use different combinations of public data sources. Different data produces different baseline distributions, which produces different reform estimates.

**Behavioral assumptions.** Static models assume no behavioral response. Dynamic models assume some combination of labor supply changes, saving changes, and investment shifts. The Tax Foundation's model assumed larger growth effects from corporate tax cuts; PWBM assumed smaller ones. These assumptions drove the gap between $1.0 trillion and $2.2 trillion more than any other factor.

**Modeling choices.** How do you handle income shifting between corporate and individual returns? How do you project economic growth? How do you treat provisions that expire? Each choice is defensible; together they compound into meaningful differences.

The disagreements aren't evidence of failure. They're evidence that policy analysis involves judgment—about data, behavior, and modeling choices—that no amount of technical sophistication eliminates. The value of having multiple models is precisely that the disagreements reveal where assumptions drive results.

When JCT and the Tax Foundation produce different estimates, the question to ask isn't "who's right?" It's "what assumptions differ, and which do I find more plausible?" Microsimulation makes the disagreement specific and tractable. Without it, the debate would be pure assertion.

---

## Where Models Fail

The failures are instructive.

**Behavioral responses**: Static models assume people don't change behavior in response to policy. But tax changes trigger income-shifting, benefit changes affect labor supply, and coverage mandates alter insurance choices. Models that assume static behavior systematically miss these effects. The TCJA led to a surge in pass-through business income as high earners restructured to take advantage of the new 20% deduction—a behavioral shift that no static model predicted.

**Take-up rates**: Models often assume people claim benefits they're eligible for. In reality, take-up varies widely. The IRS estimates EITC take-up at roughly 78-80%—relatively high for a tax credit, but still meaning one in five eligible families miss it {cite}`irs2024eitc`. SNAP take-up runs around 82% nationally but varies dramatically by state {cite}`usda2024snap`. SSI take-up for eligible elderly individuals may be as low as 50-60%. Getting take-up wrong cascades through the entire analysis: overestimate SNAP participation and you'll overestimate both program costs and poverty reduction.

**Data limitations**: As Meyer's work shows, the surveys underlying most models systematically misrepresent who receives benefits, how much income households have, and what their circumstances look like. Administrative records help, but bring their own issues: coverage gaps (non-filers don't appear in tax data), timeliness (there's a two-year lag before IRS data becomes available for research), and linkage challenges (matching records across agencies without common identifiers).

**Structural change**: Models calibrated to past behavior may fail when the structure of the economy shifts. The ACA exchange enrollment miss likely reflected unprecedented market dynamics that historical data couldn't predict. Similarly, the pandemic-era expansion of the Child Tax Credit produced take-up patterns that no historical model would have forecast—the IRS had to build an entirely new delivery system to reach non-filers.

---

## The AHCA Counterfactual

In 2017, CBO estimated that repealing the ACA under the American Health Care Act would cause 23 million people to lose coverage over a decade {cite}`cbo2017ahca`.

We never got to test this prediction—the bill failed. But the analysis forced a conversation that wouldn't have happened otherwise. *Which* 23 million? Low-income? Rural? Elderly? The specificity of microsimulation, even when imperfect, structured the debate.

This illustrates both the power and limitation of these models. They can't predict with certainty what would happen under policies never implemented. But they can illuminate *who* would be affected and through *what mechanisms*—questions that vaguer analysis cannot answer.

---

## The Honest Assessment

Do microsimulation models work?

**Yes**: They calculate correctly. They match administrative data reasonably well. They predict incremental changes with useful accuracy. They're vastly better than intuition or partisan assertion. And they're getting better—sixth-year forecast errors fell by two-thirds between the 1990s and 2010s.

**No**: They can produce false precision. They miss behavioral responses. They struggle with structural change. They're least reliable when stakes are highest—for novel, large-scale reforms. And a simple random walk sometimes beats sophisticated modeling.

**The right frame**: Microsimulation models are like weather forecasts. Tomorrow's forecast is reliable. Next week's is roughly right. Next month's is a best guess.

We don't stop using weather forecasts because they're imperfect. We calibrate our confidence to the forecast horizon. We use them where they're reliable and acknowledge uncertainty where they're not.

---

## Better Than Alternatives

The accuracy question has a flip side: compared to what?

Before microsimulation, policy analysis relied on:
- **Rules of thumb**: "A 10% tax cut increases revenue through growth." (The TCJA data proved this false.)
- **Expert judgment**: "Trust me, this will work." (Philip Tetlock's research showed most experts forecast little better than chance {cite}`tetlock2005expert`.)
- **Partisan assertion**: "This reform will help working families." (Vague and unverifiable.)
- **Back-of-the-envelope calculations**: Quick estimates based on average tax rates applied to aggregate income, missing the distributional complexity that determines who actually benefits.

Microsimulation forces specificity. Which families? How much help? Through what mechanisms? Even when the answer is approximate, the *question* becomes clearer.

Consider the 2021 expansion of the Child Tax Credit. Without microsimulation, the debate would have been "does a bigger credit help families?" With microsimulation, the debate became precise: the expansion would cost approximately $105 billion per year, reduce child poverty by roughly 40%, and deliver the largest benefits to the lowest-income families who previously received zero credit because they owed no federal income tax. These specific claims could be checked, debated, and—after the expansion was implemented—compared to actual outcomes.

The Census Bureau's subsequent data showed child poverty falling from 9.7% to 5.2% in 2021—closely matching the microsimulation projections {cite}`census2022spm`. Columbia University's Center on Poverty and Social Policy tracked the monthly declines in real time as expanded CTC payments went out, confirming the projected magnitude {cite}`parolin2021monthly`. When the expansion expired and the credit reverted to its previous structure, child poverty rebounded. The models had been right about both the effect and its reversal.

This doesn't mean the models were perfect. They didn't fully predict take-up patterns for non-filers, or the macroeconomic interactions of a credit expansion during a pandemic recovery. But they got the direction, magnitude, and distributional shape approximately right—which is more than any alternative method delivered.

---

## The Practitioner's Creed

George Box's famous line—"all models are wrong, but some are useful"—isn't cynicism {cite}`box1976science`. It's epistemic hygiene. The modeler who believes the model captures full truth is more dangerous than the modeler who knows its limits.

The accuracy question doesn't have a triumphant answer. The honest answer is: approximately right, sometimes wrong, better than alternatives, and always improvable.

The practitioners who build these models live with this tension daily. They know the survey data undercounts transfers. They know behavioral responses are hard to model. They know their confidence intervals should be wider than their point estimates suggest. They publish the numbers anyway, because approximate knowledge beats ignorance.

What distinguishes responsible microsimulation from false precision is transparency. When CBO publishes a score, they also publish their methodology, their assumptions, and their track record. When an open-source model like PolicyEngine or Tax-Calculator produces an estimate, anyone can inspect the code, identify the assumptions, and propose corrections. The models improve through this iterative process of publication, scrutiny, and correction.

The closed models of the 1980s and 1990s—accurate but unverifiable—are giving way to open models that are both auditable and improvable. The accuracy question will never have a final answer, because the economy changes, the data improves, and the methods evolve. But the trajectory is toward greater accuracy, greater transparency, and greater accountability.

That's what evidence-based policy actually looks like. Not certainty. Not faith. Just careful reasoning, transparent methods, and the humility to check ourselves against reality.

---

*Next: Part II begins with PolicyEngine—an attempt to build policy simulation infrastructure that's not just accurate, but open.*

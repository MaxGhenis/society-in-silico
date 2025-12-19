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

## Where Models Fail

The failures are instructive.

**Behavioral responses**: Static models assume people don't change behavior in response to policy. But tax changes trigger income-shifting, benefit changes affect labor supply, and coverage mandates alter insurance choices. Models that assume static behavior systematically miss these effects.

**Take-up rates**: Models often assume people claim benefits they're eligible for. In reality, take-up varies widely—sometimes 80%, sometimes 40%. Getting take-up wrong cascades through the entire analysis.

**Data limitations**: The Current Population Survey underreports income at the top and bottom. Models built on CPS data inherit this bias. Administrative records help, but bring their own issues: coverage gaps, timeliness, and linkage challenges.

**Structural change**: Models calibrated to past behavior may fail when the structure of the economy shifts. The ACA exchange enrollment miss likely reflected unprecedented market dynamics that historical data couldn't predict.

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
- **Expert judgment**: "Trust me, this will work." (Track record: poor.)
- **Partisan assertion**: "This reform will help working families." (Vague and unverifiable.)

Microsimulation forces specificity. Which families? How much help? Through what mechanisms? Even when the answer is approximate, the *question* becomes clearer.

---

## The Practitioner's Creed

George Box's famous line—"all models are wrong, but some are useful"—isn't cynicism {cite}`box1976science`. It's epistemic hygiene. The modeler who believes the model captures full truth is more dangerous than the modeler who knows its limits.

The accuracy question doesn't have a triumphant answer. The honest answer is: approximately right, sometimes wrong, better than alternatives, and always improvable.

That's what evidence-based policy actually looks like. Not certainty. Not faith. Just careful reasoning, transparent methods, and the humility to check ourselves against reality.

---

*Next: Part II begins with PolicyEngine—an attempt to build policy simulation infrastructure that's not just accurate, but open.*

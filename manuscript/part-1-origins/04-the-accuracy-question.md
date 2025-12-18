# Chapter 4: The Accuracy Question

In 2017, the Joint Committee on Taxation estimated the Tax Cuts and Jobs Act would reduce federal revenue by $1.46 trillion over ten years. The Penn Wharton Budget Model projected larger losses—$1.8 to $2.2 trillion on a dynamic basis, accounting for economic effects.[^1] Congressional Republicans disputed both. Supply-siders predicted the tax cuts would pay for themselves through growth.

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

In March 2010, CBO predicted the ACA would reduce the non-elderly uninsured rate from over 18 percent to about 7.6 percent by 2016. This assumed all states would adopt Medicaid expansion.[^2]

Then the Supreme Court made Medicaid expansion optional, and 19 states declined. Adjusting for this, CBO's projected uninsured rate for 2016 becomes 9.4 percent. The actual rate, according to CDC data, was 10.4 percent.[^3]

That's remarkably close—within one percentage point—given a six-year forecast horizon and a major legal disruption.

But the aggregate accuracy masked component errors:

| Coverage Source | CBO 2010 Prediction | Actual 2016 |
|-----------------|---------------------|-------------|
| Exchange enrollment | 21-23 million | 10.4 million |
| Medicaid expansion | 10 million | 14.4 million |
| Total uninsured | 30 million | 27.9 million |

Source: Commonwealth Fund, FactCheck.org[^4]

CBO overestimated exchange enrollment by more than half. They underestimated Medicaid enrollment by nearly 50%. Yet the total coverage gain was roughly correct because the errors partially canceled.

As one analysis put it: "CBO's mistake was in estimating *where* the uninsured would get covered, not *how many* of them would gain coverage."[^5]

---

## Where Models Fail

The failures are instructive.

**Behavioral responses**: Static models assume people don't change behavior in response to policy. But tax changes trigger income-shifting, benefit changes affect labor supply, and coverage mandates alter insurance choices. Models that assume static behavior systematically miss these effects.

**Take-up rates**: Models often assume people claim benefits they're eligible for. In reality, take-up varies widely—sometimes 80%, sometimes 40%. Getting take-up wrong cascades through the entire analysis.

**Data limitations**: The Current Population Survey underreports income at the top and bottom. Models built on CPS data inherit this bias. Administrative records help, but bring their own issues: coverage gaps, timeliness, and linkage challenges.

**Structural change**: Models calibrated to past behavior may fail when the structure of the economy shifts. The ACA exchange enrollment miss likely reflected unprecedented market dynamics that historical data couldn't predict.

---

## The AHCA Counterfactual

In 2017, CBO estimated that repealing the ACA under the American Health Care Act would cause 23 million people to lose coverage over a decade.[^6]

We never got to test this prediction—the bill failed. But the analysis forced a conversation that wouldn't have happened otherwise. *Which* 23 million? Low-income? Rural? Elderly? The specificity of microsimulation, even when imperfect, structured the debate.

This illustrates both the power and limitation of these models. They can't predict with certainty what would happen under policies never implemented. But they can illuminate *who* would be affected and through *what mechanisms*—questions that vaguer analysis cannot answer.

---

## The Honest Assessment

Do microsimulation models work?

**Yes**: They calculate correctly. They match administrative data reasonably well. They predict incremental changes with useful accuracy. They're vastly better than intuition or partisan assertion.

**No**: They can produce false precision. They miss behavioral responses. They struggle with structural change. They're least reliable when stakes are highest—for novel, large-scale reforms.

**The right frame**: Microsimulation models are like weather forecasts. Tomorrow's forecast is reliable. Next week's is roughly right. Next month's is a best guess.

We don't stop using weather forecasts because they're imperfect. We calibrate our confidence to the forecast horizon. We use them where they're reliable and acknowledge uncertainty where they're not.

---

## Better Than Alternatives

The accuracy question has a flip side: compared to what?

Before microsimulation, policy analysis relied on:
- **Rules of thumb**: "A 10% tax cut increases revenue through growth." (Often false.)
- **Expert judgment**: "Trust me, this will work." (Track record: poor.)
- **Partisan assertion**: "This reform will help working families." (Vague and unverifiable.)

Microsimulation forces specificity. Which families? How much help? Through what mechanisms? Even when the answer is approximate, the *question* becomes clearer.

---

## The Practitioner's Creed

George Box's famous line—"all models are wrong, but some are useful"—isn't cynicism. It's epistemic hygiene. The modeler who believes the model captures full truth is more dangerous than the modeler who knows its limits.

The accuracy question doesn't have a triumphant answer. The honest answer is: approximately right, sometimes wrong, better than alternatives, and always improvable.

That's what evidence-based policy actually looks like. Not certainty. Not faith. Just careful reasoning, transparent methods, and the humility to check ourselves against reality.

---

*Next: Part II begins with PolicyEngine—an attempt to build policy simulation infrastructure that's not just accurate, but open.*

---

## Sources

[^1]: Penn Wharton Budget Model, "The Tax Cuts and Jobs Act, as Reported by Conference Committee (12/15/17)," December 18, 2017. https://budgetmodel.wharton.upenn.edu/issues/2017/12/18/the-tax-cuts-and-jobs-act-reported-by-conference-committee-121517-preliminary-static-and-dynamic-effects-on-the-budget-and-the-economy

[^2]: Congressional Budget Office, March 2010 baseline projections for the Affordable Care Act.

[^3]: Centers for Disease Control and Prevention, National Health Interview Survey, 2016.

[^4]: Sara Collins et al., "The CBO's Crystal Ball: How Well Did It Forecast the Effects of the Affordable Care Act?" Commonwealth Fund, December 2015. https://www.commonwealthfund.org/publications/issue-briefs/2015/dec/cbos-crystal-ball-how-well-did-it-forecast-effects-affordable; Eugene Kiely, "CBO's Obamacare Predictions: How Accurate?" FactCheck.org, March 2017. https://www.factcheck.org/2017/03/cbos-obamacare-predictions-how-accurate/

[^5]: Commonwealth Fund analysis, 2015.

[^6]: Congressional Budget Office, "American Health Care Act," May 2017.

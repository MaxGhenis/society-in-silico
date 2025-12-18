# Chapter 4: The Accuracy Question

In 2017, the Penn Wharton Budget Model made a prediction: the Tax Cuts and Jobs Act would reduce federal revenue by $1.4 trillion over ten years. Congressional Republicans disputed this. Supply-siders predicted the tax cuts would pay for themselves through growth.

Five years later, we could check. Federal revenues did decline—roughly in line with Penn Wharton's projection, though the pandemic made precise attribution impossible. The supply-side fantasy didn't materialize. The microsimulation had been... approximately right.

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

**Component validation**: Do the individual calculations match the rules? If the model says a married couple with $100,000 income owes $15,420 in federal taxes, is that right? This is straightforward to check—you can verify against IRS worksheets or tax preparation software.

**Aggregate validation**: When the model sums across the population, does it match administrative totals? If TRIM3 says 42 million households receive SNAP benefits, does that match USDA administrative data? If it says total federal income tax revenue is $1.8 trillion, does that match IRS collections?

**Predictive validation**: When the model predicts effects of changes, do those predictions hold up? This is hardest—you rarely get clean experiments. Policy changes come bundled with economic shifts, other reforms, and behavioral responses that weren't anticipated.

Good models pass the first two levels reliably. The third is where humility enters.

---

## The TRIM3 Validation Framework

The Urban Institute's TRIM3 model, one of the most widely used U.S. microsimulation systems, publishes detailed validation documentation. Their approach:

1. **Calibration to administrative data**: Adjust the simulation so totals match known benchmarks—IRS returns, SSA beneficiary counts, CMS enrollment figures.

2. **Cross-model comparison**: Compare TRIM3 results to CBO, JCT, and PWBM for major reforms. Differences get investigated.

3. **Sensitivity analysis**: Vary key assumptions and report ranges, not point estimates.

When TRIM3 analyzed the 2021 expanded Child Tax Credit, they compared their estimates to actual IRS data released later. The model predicted roughly 36 million families would receive payments; administrative data showed 35 million. The model was within 3%.

That's good. But it's one reform, one year. The track record across decades is harder to assess because we rarely get such clean comparisons.

---

## Where Models Fail

The failures are instructive.

**Behavioral responses**: Static models assume people don't change behavior in response to policy. The 1986 Tax Reform Act, which lowered marginal rates, triggered dramatic income-shifting by high earners. Models that assumed static behavior underestimated this.

**Take-up rates**: Models often assume people claim benefits they're eligible for. In reality, take-up varies—sometimes 80%, sometimes 40%. Getting take-up wrong cascades through the entire analysis.

**Data limitations**: The Current Population Survey underreports income at the top and bottom. Models built on CPS data inherit this bias. Administrative records help, but bring their own issues (coverage, timeliness, linkage).

**Structural change**: Models calibrated to past behavior may fail when the structure of the economy shifts. The models that predicted ACA coverage expansion got the direction right but the magnitude varied by millions.

---

## The Penn Wharton Track Record

Penn Wharton Budget Model has published systematic comparisons of their predictions to outcomes for several major reforms:

| Reform | PWBM Prediction | Actual Outcome | Verdict |
|--------|----------------|----------------|---------|
| TCJA Revenue | -$1.4T | ~-$1-2T | Roughly correct |
| ACA Coverage | +24M | +20M | Overstated by 20% |
| Child Tax Credit 2021 | 36M families | 35M families | Within 3% |

The pattern: models get the direction right and usually the order of magnitude. But 10-20% errors are common. 50% errors happen occasionally.

Is this good enough?

Compared to the alternative—flying blind—yes. Compared to the precision the numbers suggest—no. This is why uncertainty quantification matters (Chapter 10).

---

## The Asymmetric Problem

Here's the deeper issue: we mostly test models against incremental reforms. A 10% change to a tax rate. A $500 increase in a benefit. For these, historical relationships roughly hold.

But the most interesting policy questions involve larger departures. Universal basic income. Wealth taxes. Carbon dividends. For these, we're extrapolating beyond experience.

The models can tell you: "If behavior stays the same, the cost would be X." They're much less reliable at telling you whether behavior *will* stay the same.

A UBI that replaces means-tested programs might have very different labor supply effects than theory suggests. A wealth tax might trigger capital flight—or not. The models illuminate the *mechanical* effects while remaining agnostic about *behavioral* effects we haven't observed.

---

## The CBO Standard

The Congressional Budget Office has the most rigorous validation culture in U.S. fiscal modeling. Every major projection comes with retrospective analysis: how did we do on past forecasts?

Their honest assessment: short-term estimates (1-2 years) are reasonably accurate. Medium-term (5-10 years) have substantial error. Long-term (30+ years) are scenarios, not predictions.

CBO's 2010 projection of 2020 GDP was off by 15%—before the pandemic. Add the pandemic, and the projection looks quaint. The error wasn't incompetence; it was the irreducible uncertainty of economic forecasting.

Microsimulation inherits this. A model that calculates taxes correctly still depends on economic projections that might be wrong. The calculation is precise; the scenario is uncertain.

---

## Better Than Alternatives

The accuracy question has a flip side: compared to what?

Before microsimulation, policy analysis relied on:
- **Rules of thumb**: "A 10% tax cut increases revenue through growth." (Often false.)
- **Expert judgment**: "Trust me, this will work." (Track record: poor.)
- **Partisan assertion**: "This reform will help working families." (Vague and unverifiable.)

Microsimulation forces specificity. Which families? How much help? Through what mechanisms? Even when the answer is approximate, the *question* becomes clearer.

The CBO analysis that estimated 23 million would lose coverage under AHCA repeal might have been wrong by millions. But it forced a conversation about *which* millions: low-income? rural? elderly? That conversation wouldn't have happened with vaguer analysis.

---

## The Honest Answer

Do microsimulation models work?

**Yes**: They calculate correctly. They match administrative data reasonably well. They predict incremental changes within 10-20%. They're vastly better than intuition or partisanship.

**No**: They produce false precision. They miss behavioral responses. They struggle with structural change. They're worst when stakes are highest—for novel, large-scale reforms.

**The right frame**: Microsimulation models are like weather forecasts. Tomorrow's forecast is reliable. Next week's is roughly right. Next month's is a best guess. Next year's is a scenario.

We don't stop using weather forecasts because they're imperfect. We calibrate our confidence to the forecast horizon. We use them where they're reliable and acknowledge uncertainty where they're not.

That's the appropriate stance for microsimulation: useful infrastructure, not oracle. Better than nothing, worse than certainty.

---

## What Would Make Models Better?

Several improvements are technically feasible:

**Better data**: Linking survey data to administrative records gives ground truth on income, employment, program participation. The Census Bureau's efforts here are promising.

**Behavioral modeling**: Moving beyond "static" assumptions to capture responses. This is hard—behavioral parameters are uncertain—but partial progress helps.

**Uncertainty quantification**: Instead of point estimates, produce probability distributions. This is the subject of Chapter 10.

**Open source**: Public code allows external scrutiny. Errors get found. Methods improve. This is the subject of Chapter 3.

**Validation culture**: Regular retrospectives comparing predictions to outcomes. Honest accounting of failures.

The models we have are the beginning, not the end. They work well enough to be useful, poorly enough to require humility.

---

## The Practitioner's Creed

Every microsimulation modeler I know operates with what might be called the practitioner's creed:

*The model is wrong. All models are wrong. This model is less wrong than not modeling. Use it with eyes open.*

George Box's famous line—"all models are wrong, but some are useful"—isn't cynicism. It's epistemic hygiene. The modeler who believes the model captures full truth is more dangerous than the modeler who knows its limits.

The accuracy question doesn't have a triumphant answer. The honest answer is: approximately right, sometimes wrong, better than alternatives, and always improvable.

That's what evidence-based policy actually looks like. Not certainty. Not faith. Just careful reasoning, transparent methods, and the humility to check ourselves against reality.

---

*Next: Part II begins with PolicyEngine—an attempt to build policy simulation infrastructure that's not just accurate, but open.*

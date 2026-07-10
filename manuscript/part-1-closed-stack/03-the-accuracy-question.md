# Chapter 3: The accuracy question

In 2017, the Joint Committee on Taxation estimated that the Tax Cuts and Jobs Act would reduce federal revenue by $1.46 trillion over ten years. The Penn Wharton Budget Model projected larger losses—$1.8 to $2.2 trillion on a dynamic basis, once economic effects were counted [@pwbm2017tcja]. Congressional Republicans disputed both; supply-siders predicted the cuts would pay for themselves through growth.

The supply-side prediction didn't materialize. The microsimulations had been approximately right about direction and magnitude.

But "approximately right" is the best anyone can honestly say.

## Do these things actually work?

Through the 1990s and 2000s the models grew more sophisticated. The IFS refined TAXBEN; the Urban Institute expanded TRIM3; policy shops on every side produced estimates that happened to support their preferred conclusions. A reasonable observer might ask whether any of it works. The models are complex, their assumptions buried in code, their data imperfect—and two of them, handed the same reform, will sometimes return different answers.

The institutional fight over who gets to produce those numbers belongs to the previous chapter. What concerns us here is narrower and harder: whether the numbers are any good. The honest response is not "trust us." It is "here is how we test ourselves."

## Three ways to be right

Microsimulation validation happens at three levels, and they are not equally easy.

**Component validation** asks whether individual calculations match the rules. If the model says a married couple earning $100,000 owes a particular amount of federal tax, is that amount correct? This is the tractable case—you can check it against IRS worksheets or commercial tax software.

**Aggregate validation** asks whether the model, summed across the population, matches administrative totals. Does its estimate of total SNAP enrollment match USDA records? Does its total income-tax revenue match IRS collections?

**Predictive validation** asks whether the model's forecast of a change holds up. This is the hard one. You rarely get a clean experiment: policy changes arrive bundled with economic shifts, other reforms, and behavioral responses no one anticipated.

Good models pass the first two levels reliably. The third is where humility enters—and where most of this chapter lives.

## The ACA test case

The Affordable Care Act is one of the better natural experiments for testing that third level. In March 2010, the CBO predicted the ACA would cut the non-elderly uninsured rate from over 18 percent to about 7.6 percent by 2016, assuming every state expanded Medicaid [@collins2015aca]. Then the Supreme Court made expansion optional, and nineteen states declined. Adjust for that, and the CBO's projected 2016 uninsured rate becomes 9.4 percent. The actual rate, from CDC data, was 10.4 percent [@kiely2017aca]—within a point, across a six-year horizon interrupted by a major legal shock.

The aggregate accuracy hid offsetting component errors.

| Coverage source | CBO 2010 prediction | Actual 2016 |
|---|---|---|
| Exchange enrollment | 21–23 million | 10.4 million |
| Medicaid expansion | 10 million | 14.4 million |
| Total uninsured | 30 million | 27.9 million |

Source: [@collins2015aca], [@kiely2017aca]

The CBO overestimated exchange enrollment by more than half and underestimated Medicaid enrollment by nearly half. Yet the total coverage gain came out roughly right, because the two errors ran in opposite directions and partly cancelled. As one analysis put it, the CBO's mistake "was in estimating *where* the uninsured would get covered, not *how many* of them would gain coverage" [@collins2015aca]. Right about the total, wrong about the composition: that is the characteristic signature of a model that passes aggregate validation while failing at the component level, and it is a warning against reading a good headline number as proof the machinery underneath is sound. The cancellation here was closer to luck than to skill—two large errors that happened to point in opposite directions—and the next reform's errors might just as easily compound. A number that comes out right for the wrong reasons has not been validated; it has been lucky, and luck does not generalize.

## Are the forecasts improving?

Here is a question rarely asked. Is government forecasting getting better? The CBO is one of the few institutions that grades itself in public, publishing systematic retrospectives that compare its projections to what actually happened [@cbo2024deficit]. For sixth-year deficit projections—the medium-term forecasts that anchor major policy debates—the average absolute error fell from 3.2 percent of GDP over 1989–2001 to 1.0 percent over 2002–2019, a threefold improvement in two decades [@cbo2024deficit]. Richer IRS administrative data, more capable computing, and decades of retrospective analysis that exposed and corrected systematic biases all contributed. The mechanism worth noting is the feedback loop itself: because the CBO scored its own past forecasts against outcomes, it could find the places it had been reliably wrong and adjust—an accountability loop most forecasters never build, and much of the reason its numbers improved at all.

The improvement has limits. The CBO's projections remain about as accurate as the Blue Chip consensus of some fifty private forecasters, and about as accurate as the Administration's own numbers [@cbo2025forecasting]; no one has found a way to consistently beat the collective wisdom of informed forecasters. And recent years brought more volatility, not less. The 2021 projection was the CBO's largest overestimate on record, and the 2023 its largest underestimate—off by 3.9 percent of GDP, more than triple the historical average [@cbo2024deficit]. The pandemic scrambled every model built for normal times.

### The random walk

The most humbling result comes from academic work. A Berkeley thesis examining CBO forecasts from 1976 to 2007 found that a "random walk"—simply assuming next year's deficit equals this year's—would have beaten the CBO on average, over both short and medium horizons [@inayatali2023cbo].

This is not an indictment of the CBO's competence. It is a statement about irreducible uncertainty. The events that dominate fiscal outcomes—recessions, financial crises, pandemics—are precisely the ones no model foresees, and a model calibrated on ordinary times fails exactly when the times stop being ordinary. That a naive rule can match a sophisticated one, on the questions that matter most, is the first hint that forecasting is a different kind of problem from computing a household's taxes—and may need a different kind of accountability.

### What the TCJA record shows

For the Tax Cuts and Jobs Act we now have seven years of data. Real (inflation-adjusted) revenue for 2018 through 2024—excluding the anomalous 2022 surge, driven by capital-gains realizations and inflation rather than the tax law—came in within 0.5 percent of CBO's 2018 projections [@crfb2024tcja]. That is remarkably accurate for a major tax overhaul. The supply-side claim that the cuts would pay for themselves proved false; the microsimulation estimates proved roughly correct.

One note on currency. The TCJA's individual provisions did not expire on schedule: the One Big Beautiful Bill Act extended them in July 2025, making the pass-through deduction permanent and setting the Child Tax Credit at $2,200 for 2026 [@obbba2025]. So the 2018–2024 window is a completed natural experiment, not the end of the law—the record over those years is closed and gradable, even as the statute itself runs on.

## The prediction-market benchmark

There is a way to forecast that sidesteps models entirely: let people bet, and read the price. Prediction markets aggregate dispersed information, put money on the line, and update quickly when experts with reputations to protect would not.

For macroeconomic variables, an NBER study found prediction markets "weakly more accurate than survey forecasts" across GDP, inflation, and employment—a modest but consistent edge [@wolfers2012prediction]. For elections the gap is sharper: the Monday before the 2024 presidential vote, with polls showing a coin flip, Polymarket had Trump at 58 percent [@polymarket2024election], and academic work comparing market prices to FiveThirtyEight has found the markets competitive with or better than the model [@crane2020prediction]. For Fed decisions, Good Judgment's "superforecasters"—individuals identified through tournaments as unusually well-calibrated—reportedly beat financial futures markets by about 30 percent in 2024–2025 [@goodjudgment2024]. Philip Tetlock's research supplies the frame: most experts forecast little better than chance, but a small minority, roughly 2 percent of participants in the Good Judgment Project, consistently outperform—by updating often, thinking in probabilities, and refusing to marry a prediction to an ideology [@tetlock2005expert; @tetlock2015superforecasting].

Two lessons follow for microsimulation. Where a market exists for a policy-relevant question—will inflation top 3 percent, will unemployment rise—it offers a live calibration check against which a model's forecast can be scored. But markets need clear resolution dates and objective outcomes; they cannot price a counterfactual policy that was never enacted, which is exactly the terrain microsimulation has to itself. The synthesis is the interesting part: structural estimates from a model, calibration from a market, each covering the other's blind spot. That same idea returns in Part IV, as an institution that publishes interval forecasts of government metrics and grades them when the official numbers land—though none have resolved yet, so nothing there is validated, only staked.

## The survey-data crisis

Before asking whether the outputs are accurate, it is worth asking about the inputs—and the answer is unsettling. Bruce Meyer, an economist at the University of Chicago, has spent two decades documenting what he calls a crisis in household survey data [@meyer2015underreporting]. People do not accurately report their income and benefits to survey-takers, and the errors are not random. When Meyer and colleagues linked survey responses to administrative records, they found that roughly 40 to 50 percent of SNAP recipients did not report receiving benefits in the Current Population Survey. More than 60 percent of Temporary Assistance for Needy Families and General Assistance went unreported. About a third of housing-assistance recipients did not mention it. Even Social Security, which arrives monthly and ought to be the easiest transfer to remember, was underreported by about a tenth of recipients.

This cascades through every model built on survey data. When a microsimulation estimates the poverty effect of SNAP, it assigns benefits to households that look eligible from their reported income. But if half of actual recipients never reported the benefit—and may also have misreported the income and household composition that determine eligibility—the model is reasoning from a distorted picture of who gets SNAP and what their circumstances are. And the distortion has grown: survey response rates have fallen since the 1990s, the non-responders skew low-income, young, and mobile, and the Census Bureau's imputations increasingly fill the gaps with inferences that reflect the imputation model as much as the household.

The bias runs both ways. Seniors systematically underreport retirement income. A Census Bureau study linking CPS responses to IRS and Social Security records found median income for those 65 and older was 30 percent higher in administrative data than in survey reports; CPS-based senior poverty of 9.1 percent was 2.2 points higher than the 6.9 percent the validated records showed [@census2017retirement]. Senior poverty is real; the headline survey number overstates it. At the other end of the distribution, very high earnings are top-coded in public-use data—masked to protect confidentiality—which compresses the top and makes reforms aimed at high earners harder to model accurately [NEEDS CITATION: CPS top-coding methodology]. These problems touch nearly every model that leans on household surveys, and the models with confidential IRS access escape only some of them: tax returns miss non-filers, omit non-taxable transfers, and describe legal tax units rather than economic households. Microsimulation is only as good as its data, and the data is imperfect in systematic, consequential ways. Which means accuracy is not only a matter of better equations; it is a matter of better inputs—of reconstructing, from imperfect surveys and partial administrative records, a population that matches the totals we can actually observe.

## TAXSIM, the academic benchmark

TAXSIM, the NBER tax calculator introduced in Chapter 2, doubles as a validation benchmark. Daniel Feenberg maintained it for more than four decades, and the thousand-plus published papers that cite it created an informal validation network: when TAXSIM returned something a researcher didn't expect, someone investigated and reported the bug, and the model improved under collective scrutiny [@feenberg1993taxsim]. For its core job—computing federal income tax from a given set of inputs—its accuracy is high, the rules being deterministic and well documented; the discrepancies that surface tend to sit in state-code edge cases or credit interactions. The lesson in that record is quiet but important: a tool becomes trustworthy less through any single act of certification than through years of exposure to users who had every incentive to catch it in a mistake.

But TAXSIM computes taxes only. It does not simulate SNAP, Medicaid, SSI, or housing assistance—the benefit programs whose cliffs and interactions later chapters turn on—and it works record by record, producing no aggregate revenue estimate or distributional table. What it established was narrower and still important: an independent, inspectable tool could match proprietary accuracy for a well-defined calculation. The limit was scope, not capability.

## When models disagree

If the models were simply accurate, they would agree. They often don't. During the 2017 TCJA debate, four institutions scored the bill and landed a factor of five apart: the JCT's static estimate of $1.46 trillion in revenue loss, Penn Wharton's $1.8-to-$2.2-trillion dynamic range, the Tax Foundation's far more optimistic $448 billion, and the Tax Policy Center's distributional work, broadly consistent with the JCT on revenue. All four employed competent economists and microsimulation. Why the gap?

Three sources account for most cross-model disagreement. The first is data: the JCT uses confidential IRS returns, the most comprehensive source available, while the TPC works from less granular public-use files and others from different combinations again—and different baselines yield different reform estimates. The second is behavioral assumptions: a static model assumes no response, dynamic models add some mix of labor-supply, saving, and investment effects, and the Tax Foundation's larger assumed growth response against Penn Wharton's smaller one drove the gap between $448 billion and $2.2 trillion more than anything else. The third is modeling choices: how to handle income shifting between corporate and individual returns, how to project growth, how to treat expiring provisions—each defensible on its own, and compounding together.

The disagreements are not failures. They are evidence that policy analysis rests on judgment—about data, behavior, and method—that no amount of technical polish removes. The value of running several models is that the disagreement becomes specific: not "who is right?" but "which assumptions differ, and which do I find more plausible?" The model does not settle the argument; it relocates it, from a clash of conclusions to a clash of stated premises—the only kind of policy argument that can actually be adjudicated. Without the models the debate would be pure assertion; with them, it is at least tractable.

## Where models fail

The failures are instructive, and they cluster. Static models assume people don't change behavior, but tax changes trigger income-shifting and benefit changes move labor supply—the TCJA set off a surge of pass-through income as high earners restructured to claim the new 20 percent deduction, a shift no static model saw coming. Take-up is a second fault line: models often assume people claim what they are eligible for, when EITC take-up runs around 78 to 80 percent [@irs2024eitc], SNAP around 82 percent nationally with wide state variation [@usda2024snap], and SSI for eligible elderly individuals perhaps as low as 50 to 60 percent. Get take-up wrong and both program cost and poverty reduction go with it.

Data limitations, as Meyer's work shows, sit underneath all of it, and administrative records bring their own gaps: non-filers missing from tax data, a two-year lag before IRS files are research-ready, no common identifier to link records cleanly across agencies. And structural change defeats models calibrated on the past—the ACA exchange miss reflected market dynamics history couldn't anticipate, just as the 2021 Child Tax Credit expansion produced take-up patterns among non-filers that no prior model would have forecast. These are also where microsimulation earns its keep, because they name the failure precisely enough to fix it, which vaguer methods never do.

## The AHCA counterfactual

In 2017 the CBO estimated that repealing the ACA under the American Health Care Act would cost 23 million people their coverage over a decade [@cbo2017ahca]. The prediction was never tested; the bill failed. But the number forced a conversation that would not otherwise have happened—*which* 23 million? Low-income, rural, elderly?—and the specificity of the model, even unproven, structured the argument. That is both the power and the boundary of these tools: they cannot tell you with certainty what an unenacted policy would have done, but they can tell you who would have been affected, and through what mechanism, which is more than assertion ever manages. A counterfactual can never be checked against reality—that is what makes it a counterfactual—so its only claim to trust is the verifiability of its parts: whether each rule it applied matches the statute, and whether the population it applied them to matches the country. The whole may be untestable; the pieces need not be.

## Better than the alternatives

The accuracy question has a second half: compared with what? Before microsimulation, policy analysis ran on rules of thumb ("a 10 percent tax cut pays for itself"—the TCJA data says otherwise), on expert judgment (which Tetlock showed forecasts little better than chance [@tetlock2005expert]), on partisan assertion, and on back-of-the-envelope arithmetic that applied average rates to aggregate income and missed the distribution entirely. Against that field, microsimulation's demand for specificity is the whole point: which families, how much, through what mechanism.

The 2021 expansion of the Child Tax Credit shows what the specificity buys. Without a model, the debate is "does a bigger credit help families?" With one, it becomes precise: the expansion would cost roughly $105 billion a year, cut child poverty by about 40 percent, and deliver its largest gains to the lowest-income families, who had received little or no credit because they owed no federal income tax. Those claims were checkable—and were checked. Census data showed child poverty falling from 9.7 to 5.2 percent in 2021 [@census2022spm], Columbia's poverty center tracked the monthly declines as the payments went out [@parolin2021monthly], and when the expansion lapsed and the credit reverted, child poverty climbed back. The models had the direction, the magnitude, and the distributional shape roughly right—more than any alternative delivered. They did not nail everything, missing some non-filer take-up and the macroeconomic cross-currents of a credit expansion during a pandemic recovery. Weather forecasting is the right mental model: tomorrow's forecast is reliable, next week's roughly right, next month's a best guess, and the responsible move is to calibrate confidence to the horizon rather than abandon the forecast.

## What the models are for

George Box's line—"all models are wrong, but some are useful"—is not cynicism but epistemic hygiene [@box1976science]. The modeler who believes the model captures the whole truth is more dangerous than the one who knows its limits. The honest verdict on microsimulation is exactly as unheroic as it sounds: approximately right, sometimes wrong, better than the alternatives, and always improvable. Practitioners live with that tension daily—they know the surveys undercount transfers, that behavioral responses resist modeling, that their confidence intervals should be wider than their point estimates admit—and they publish anyway, because approximate knowledge beats ignorance.

What separates responsible microsimulation from false precision is not accuracy; it is verifiability. When the CBO publishes a score, it publishes its methodology and its track record. When an open model like PolicyEngine or Tax-Calculator produces an estimate, anyone can read the code, find the assumptions, and propose a fix. That points at the discipline this whole book is built to enforce, and it is worth stating as a rule.

A simulation is admissible only where its verification chain terminates in ground truth. The three levels that opened this chapter are the terms of admission: a component check against the statute, an aggregate check against administrative totals, a forecast graded when the official number finally lands. Where that chain holds, a number can be trusted no matter who produced it. Where it breaks, the number is assertion wearing the costume of arithmetic, and no amount of computational sophistication redeems it. Everything the rest of this book describes—rules encoded by machines, populations synthesized from surveys, forecasts posted with intervals—is asked to pass that same test. It is a demanding rule, and it disqualifies a great deal: most of what passes for confident analysis cannot say where its chain of checks bottoms out in something an outsider could verify. But it is the only rule that lets a reader trust a number produced by a machine, or a stranger, or an institution with a stake in the answer.

It begins, though, somewhere much smaller than a national model: with one household, one benefit cliff, and the frustration that turned a family's spreadsheet into a reason to build any of this at all.

---

## References

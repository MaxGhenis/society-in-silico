# Facts catalog — Chapter 3: The accuracy question

Source: `manuscript/part-1-closed-stack/03-the-accuracy-question.md`

## Facts

- In 2017, the Joint Committee on Taxation estimated that the Tax Cuts and Jobs Act would reduce federal revenue by $1.46 trillion over ten years.
- The Penn Wharton Budget Model projected larger TCJA losses — $1.8 to $2.2 trillion on a dynamic basis, once economic effects were counted [@pwbm2017tcja].
- Congressional Republicans disputed both estimates; supply-siders predicted the cuts would pay for themselves through growth. The supply-side prediction did not materialize; the microsimulations were approximately right about direction and magnitude.
- Through the 1990s and 2000s the IFS refined TAXBEN and the Urban Institute expanded TRIM3; policy shops on every side produced estimates that happened to support their preferred conclusions.
- Microsimulation validation happens at three levels of increasing difficulty:
  - **Component validation** — whether individual calculations match the rules (e.g., whether a married couple earning $100,000 owes the correct federal tax); checkable against IRS worksheets or commercial tax software. The tractable case.
  - **Aggregate validation** — whether the model, summed across the population, matches administrative totals (e.g., total SNAP enrollment vs. USDA records; total income-tax revenue vs. IRS collections).
  - **Predictive validation** — whether the model's forecast of a change holds up; the hard one, because policy changes arrive bundled with economic shifts, other reforms, and unanticipated behavioral responses.
- Good models pass the first two levels reliably; the third is where humility enters.
- ACA test case: in March 2010 the CBO predicted the ACA would cut the non-elderly uninsured rate from over 18 percent to about 7.6 percent by 2016, assuming every state expanded Medicaid [@collins2015aca]. (The @collins2015aca entry's authors were corrected to Glied, Arora & Solís-Román — see research/part1-verification.md correction #2; the key was kept for citation stability.)
- The Supreme Court made Medicaid expansion optional, and nineteen states declined; adjusted for that, the CBO's projected 2016 uninsured rate becomes 9.4 percent.
- The actual 2016 non-elderly uninsured rate, from CDC data, was 10.4 percent [@kiely2017aca] — within a point of the adjusted projection, across a six-year horizon interrupted by a major legal shock.
- ACA coverage table (data content), Coverage source | CBO 2010 prediction | Actual 2016:
  - Exchange enrollment | 21–23 million | 10.4 million
  - Medicaid expansion | 10 million | 14.4 million
  - Total uninsured | 30 million | 27.9 million
  - Source: [@collins2015aca], [@kiely2017aca]
- The CBO overestimated exchange enrollment by more than half and underestimated Medicaid enrollment by nearly half, yet the total coverage gain came out roughly right because the two errors ran in opposite directions and partly cancelled — closer to luck than skill.
- CBO self-grades in public, publishing systematic retrospectives comparing projections to outcomes [@cbo2024deficit].
- For sixth-year deficit projections, the average absolute error fell from 3.2 percent of GDP over 1989–2001 to 1.0 percent over 2002–2019 — a threefold improvement in two decades [@cbo2024deficit]. (Contributors: richer IRS administrative data, more capable computing, decades of retrospective analysis exposing systematic biases.)
- CBO's projections remain about as accurate as the Blue Chip consensus of some fifty private forecasters, and about as accurate as the Administration's own numbers [@cbo2025forecasting].
- The 2021 projection was the CBO's largest overestimate on record; the 2023 was its largest underestimate — off by 3.9 percent of GDP, more than triple the historical average [@cbo2024deficit].
- Kliesen and Thornton (2012), analyzing CBO forecasts published from 1976 to 2007, found that a "random walk" (assuming next year's deficit equals this year's) would have beaten the CBO on average, over both short and medium horizons [@kliesen2012cbo]. (Attribution corrected per primary source — this finding is Kliesen & Thornton's, quoted in the Berkeley/Inayatali thesis's literature review, not the thesis's own result; the thesis's own contribution is that CBO overestimated the cumulative budget balance by ~3.9% of GDP over long-term 1996–2008 reports [@inayatali2023cbo]. See research/part1-verification.md correction #3.)
- TCJA record (data content): real (inflation-adjusted) revenue for 2018 through 2024 — excluding the anomalous 2022 surge, driven by capital-gains realizations and inflation rather than the tax law — came in within 0.5 percent of CBO's 2018 projections [@crfb2024tcja].
- The One Big Beautiful Bill Act extended the TCJA's individual provisions in July 2025, making the pass-through deduction permanent and setting the Child Tax Credit at $2,200 for 2026 [@obbba2025]; the 2018–2024 window is a completed natural experiment, not the end of the law.
- For macroeconomic variables, an NBER study found prediction markets "weakly more accurate than survey forecasts" across GDP, inflation, and employment [@wolfers2012prediction].
- The Monday before the 2024 presidential vote, with polls showing a coin flip, Polymarket had Trump at 58 percent [@polymarket2024election].
- Academic work comparing prediction-market prices to FiveThirtyEight found the markets competitive with or better than the model [@crane2020prediction].
- For Fed decisions, Good Judgment's superforecasters reportedly beat financial futures markets by about 30 percent in 2024–2025 [@goodjudgment2024].
- Philip Tetlock's research: most experts forecast little better than chance, but a small minority — roughly 2 percent of Good Judgment Project participants — consistently outperform by updating often, thinking in probabilities, and refusing to marry a prediction to an ideology [@tetlock2005expert; @tetlock2015superforecasting].
- Bruce Meyer, an economist at the University of Chicago, has spent two decades documenting a crisis in household survey data [@meyer2015underreporting].
- Meyer and colleagues linked survey responses to administrative records and found (data content): roughly 40 to 50 percent of SNAP recipients did not report receiving benefits in the Current Population Survey; more than 60 percent of Temporary Assistance for Needy Families and General Assistance went unreported; about a third of housing-assistance recipients did not mention it; even Social Security was underreported by about a tenth of recipients.
- Survey response rates have fallen since the 1990s; non-responders skew low-income, young, and mobile; the Census Bureau's imputations increasingly fill the gaps with inferences reflecting the imputation model.
- Seniors systematically underreport retirement income. A Census Bureau study linking CPS responses to IRS and Social Security records found median income for those 65 and older was 30 percent higher in administrative data than in survey reports; CPS-based senior poverty of 9.1 percent was 2.2 points higher than the 6.9 percent the validated records showed [@census2017retirement].
- Very high earnings are top-coded in public-use data (masked for confidentiality), which compresses the top and makes reforms aimed at high earners harder to model [@larrimore2008topcoding]. (Marker resolved — Larrimore, Burkhauser, Feng & Zayatz 2008; see research/part1-verification.md.)
- Confidential-IRS-access models escape only some data problems: tax returns miss non-filers, omit non-taxable transfers, and describe legal tax units rather than economic households.
- TAXSIM doubles as a validation benchmark; Daniel Feenberg maintained it for more than four decades, and the thousand-plus published papers citing it created an informal validation network (users had incentive to catch and report bugs, and the model improved under collective scrutiny) [@feenberg1993taxsim].
- TAXSIM's accuracy for computing federal income tax from given inputs is high (rules being deterministic and documented); discrepancies tend to sit in state-code edge cases or credit interactions. It computes taxes only — not SNAP, Medicaid, SSI, or housing assistance — and works record by record, producing no aggregate revenue estimate or distributional table.
- Model disagreement on TCJA (data content): four institutions scored the bill a factor of five apart — JCT static $1.46 trillion revenue loss; Penn Wharton $1.8-to-$2.2-trillion dynamic range; the Tax Foundation's far more optimistic $448 billion; the Tax Policy Center's distributional work broadly consistent with the JCT on revenue.
- Three sources account for most cross-model disagreement: (1) data (JCT uses confidential IRS returns; TPC works from less granular public-use files; different baselines yield different reform estimates); (2) behavioral assumptions (static = no response; dynamic = some mix of labor-supply, saving, and investment effects; the Tax Foundation's larger assumed growth response vs. Penn Wharton's smaller one drove the $448 billion-to-$2.2 trillion gap more than anything else); (3) modeling choices (income shifting between corporate and individual returns, growth projection, treatment of expiring provisions).
- Static models assume people don't change behavior, but the TCJA set off a surge of pass-through income as high earners restructured to claim the new 20 percent deduction — a shift no static model saw coming.
- Take-up rates (data content): EITC take-up runs around 78 to 80 percent [@irs2024eitc]; SNAP around 82 percent nationally with wide state variation [@usda2024snap]; SSI for eligible elderly individuals perhaps as low as 50 to 60 percent.
- Administrative records bring their own gaps: non-filers missing from tax data, a two-year lag before IRS files are research-ready, and no common identifier to link records cleanly across agencies.
- The 2021 Child Tax Credit expansion produced take-up patterns among non-filers that no prior model would have forecast.
- AHCA counterfactual: in 2017 the CBO estimated that repealing the ACA under the American Health Care Act would cost 23 million people their coverage over a decade [@cbo2017ahca]; the prediction was never tested because the bill failed.
- Before microsimulation, policy analysis ran on rules of thumb ("a 10 percent tax cut pays for itself"), expert judgment (which Tetlock showed forecasts little better than chance [@tetlock2005expert]), partisan assertion, and back-of-the-envelope arithmetic applying average rates to aggregate income.
- 2021 Child Tax Credit expansion (data content): would cost roughly $105 billion a year, cut child poverty by about 40 percent, and deliver its largest gains to the lowest-income families, who had received little or no credit because they owed no federal income tax.
- Census data showed child poverty falling from 9.7 to 5.2 percent in 2021 [@census2022spm]; Columbia's poverty center tracked the monthly declines as payments went out [@parolin2021monthly]; when the expansion lapsed and the credit reverted, child poverty climbed back.
- George Box's line: "all models are wrong, but some are useful" [@box1976science].
- The admissibility rule (chapter's closing rule): a simulation is admissible only where its verification chain terminates in ground truth — a component check against the statute, an aggregate check against administrative totals, and a forecast graded when the official number finally lands.

## Story beats

- **The TCJA framing scene.** 2017: JCT scores TCJA at $1.46T over ten years; Penn Wharton at $1.8–2.2T dynamic; Republicans dispute both; supply-siders predict self-funding growth; that prediction fails; the models were "approximately right." Sets the whole chapter's stakes.
- **The ACA natural experiment.** March 2010 CBO prediction (18% → 7.6% uninsured, assuming full Medicaid expansion) → Supreme Court makes expansion optional, 19 states decline → adjusted projection 9.4% vs. actual 10.4% (CDC). Right on the total, wrong on composition (exchange over by half, Medicaid under by half) — the signature of aggregate validation passing while component validation fails.
- **CBO grading itself.** The retrospective feedback loop: error falls 3.2% → 1.0% of GDP; but 2021 (record over) and 2023 (record under, 3.9% off) show the pandemic scrambling models built for normal times.
- **The random walk.** Kliesen & Thornton (2012), studying CBO forecasts published 1976–2007, find a naive "next year = this year" rule beats the CBO on average — not incompetence, but irreducible uncertainty (recessions, crises, pandemics are exactly what no model foresees). (Attribution corrected — the finding is Kliesen & Thornton's, quoted in the Berkeley/Inayatali thesis, not the thesis's own result.)
- **Prediction-market benchmark.** Polymarket has Trump at 58% the Monday before the 2024 election while polls show a coin flip; superforecasters beat futures by ~30%; Tetlock's 2% who outperform. Synthesis: structural model estimates + market calibration cover each other's blind spots (returns in Part IV).
- **Meyer's survey-data crisis.** Two decades of linking surveys to admin records: 40–50% of SNAP unreported, >60% of TANF/GA, ~1/3 of housing assistance, ~1/10 of Social Security; plus senior income underreporting (30% higher in admin data) and top-coding at the high end.

## Quotes

- ACA analysis (FactCheck.org, Kiely 2017): the CBO's mistake "was in estimating *where* the uninsured would get covered, not *how many* of them would gain coverage" [@kiely2017aca]. (Quote reattributed from @collins2015aca to @kiely2017aca per primary source — the "where…not how many" framing is FactCheck.org's, not the Commonwealth Fund brief's; see research/part1-verification.md correction #2.)
- NBER study (Wolfers/Zitzewitz line): prediction markets are "weakly more accurate than survey forecasts" [@wolfers2012prediction].
- George Box: "all models are wrong, but some are useful" [@box1976science].

(These are the chapter's verbatim external quotations with named sources. Note "random walk" and "approximately right" are recurring phrases, not attributed quotations.)

## Arguments

1. The honest answer to "do these models work?" is not "trust us" but "here is how we test ourselves."
2. Validation has three levels of increasing difficulty — component (vs. statute/rules), aggregate (vs. administrative totals), predictive (vs. realized outcomes). Good models pass 1 and 2 reliably; level 3 is where humility lives.
3. Aggregate accuracy can hide offsetting component errors (ACA: exchange over by half, Medicaid under by half, total roughly right by cancellation). A number right for the wrong reasons has not been validated; it has been lucky, and luck does not generalize.
4. Forecasting has improved (3.2% → 1.0% of GDP) largely because the CBO grades itself against outcomes — an accountability feedback loop most forecasters never build. But improvement has limits: CBO ≈ Blue Chip ≈ Administration, and recent volatility (2021, 2023) shows models failing when times stop being ordinary.
5. A naive random walk beat the CBO 1976–2007 — a statement about irreducible uncertainty, not competence. Forecasting is a different kind of problem from computing a household's taxes and may need a different kind of accountability.
6. Prediction markets and superforecasters offer live calibration where a market with clear resolution and objective outcomes exists — but they cannot price a never-enacted counterfactual, which is exactly microsimulation's exclusive terrain. The synthesis (structural estimate + market calibration) is the interesting move.
7. Inputs are compromised (survey underreporting, senior underreporting, top-coding), so accuracy is as much about better inputs — reconstructing a population that matches observable totals — as about better equations.
8. Model disagreement is not failure but evidence that policy analysis rests on judgment about data, behavior, and method. Running several models relocates the argument from a clash of conclusions to a clash of stated premises — the only kind of policy argument that can be adjudicated.
9. A counterfactual can never be checked against reality (that is what makes it a counterfactual); its only claim to trust is the verifiability of its parts — each rule vs. the statute, the population vs. the country. The whole may be untestable; the pieces need not be.
10. The honest verdict on microsimulation: approximately right, sometimes wrong, better than the alternatives, and always improvable. What separates responsible microsimulation from false precision is not accuracy but verifiability.
11. The admissibility rule: a simulation is admissible only where its verification chain terminates in ground truth (component vs. statute, aggregate vs. administrative totals, forecast graded when the official number lands). Where the chain holds, a number can be trusted no matter who produced it; where it breaks, the number is assertion wearing the costume of arithmetic.

## Author-texture (verbatim, may be reused)

- "But 'approximately right' is the best anyone can honestly say." (protected — see Structural notes)
- "The models had been approximately right about direction and magnitude." (its setup sentence)
- "A number that comes out right for the wrong reasons has not been validated; it has been lucky, and luck does not generalize."
- "Where it breaks, the number is assertion wearing the costume of arithmetic, and no amount of computational sophistication redeems it."
- Weather-forecasting frame: "tomorrow's forecast is reliable, next week's roughly right, next month's a best guess, and the responsible move is to calibrate confidence to the horizon rather than abandon the forecast."
- Chapter-closing handoff: "It begins, though, somewhere much smaller than a national model: with one household, one benefit cliff, and the frustration that turned a family's spreadsheet into a reason to build any of this at all."

## Structural notes

- **Chapter's job in the book.** Third in Part I. Confronts the "do these actually work?" question directly and honestly. Introduces the three-level validation framework that becomes the book's analytical spine, works it through real cases (ACA, TCJA, random walk, prediction markets, survey crisis, TAXSIM, model disagreement), and lands the admissibility rule that the rest of the book is asked to satisfy. Bridges from the institutional/data story (Ch 2) to the personal origin (Ch 4).
- **Cross-references.** TCJA static/dynamic numbers and TAXSIM carry over from Chapter 2. Forward: the prediction-pole institution in Part IV (publishes interval forecasts of government metrics, graded when official numbers land) — explicitly caveated "none have resolved yet, so nothing there is validated, only staked" (consistent with the project rule that the Thesis Institute has zero resolved forecasts as of July 2026). Benefit cliffs and interactions are flagged as what "later chapters turn on." The survey-crisis and reconstruction thread ties back to Ch 2's synthesize-and-calibrate answer.
- **Protected lines** (task-flagged, preserve verbatim): "But 'approximately right' is the best anyone can honestly say." Also load-bearing: the admissibility-rule sentence ("A simulation is admissible only where its verification chain terminates in ground truth.").
- **Handoff.** Explicitly to Chapter 4 — "one household, one benefit cliff, and the frustration that turned a family's spreadsheet into a reason to build any of this at all."

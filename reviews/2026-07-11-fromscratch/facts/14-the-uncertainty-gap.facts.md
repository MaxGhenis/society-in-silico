# Fact catalog — Chapter 13: The uncertainty gap, and the scoreboard
Source: `manuscript/part-4-prediction/13-the-uncertainty-gap.md`. Target chapter number in rewrite: 14. Raw material for a from-scratch rewrite; paraphrased except where marked Quotes/Author-texture.

## Facts

### The opening case (CBO / AHCA)
- In 2017 the Congressional Budget Office released its analysis of the American Health Care Act, the Republican plan to repeal and replace major provisions of the Affordable Care Act [@cbo2017ahca].
- The headline estimate: 23 million fewer Americans would have health insurance by 2026 [@cbo2017ahca].
- The estimate was stated as a single figure — not "approximately 23 million," not "between 18 and 28 million."
- The precision was an illusion — not because CBO erred, and not because 23 million was a poor central estimate, but because any forecast nearly a decade out carries large uncertainty a single figure cannot express (economic conditions, behavioral responses, labor-market evolution).
- Public debate treated "23 million" as a measurement rather than an estimate — a fact to attack or defend, not a distribution to weigh.

### The point-estimate problem
- Every microsimulation result earlier in the book is a single number; illustrative examples given: a reform costs £12 billion; a policy cuts poverty by 15 percent; a marginal tax rate is 47 percent.
- The absence of confidence intervals is structural, not a bug in a particular model. The microsimulation paradigm, from Orcutt onward, was built to answer "what would happen if?" — it produces scenarios, not probability distributions.
- Four distinct kinds of uncertainty ride inside every scenario and are invisible in the output (the uncertainty taxonomy):
  - **Input-data uncertainty.** Models run on survey data — the Current Population Survey (US), the Family Resources Survey (UK). The CPS draws about 100,000 households from a nation of some 130 million; individual cells (example: self-employed workers in Montana with investment income) may hold only a handful of observations; sampling error propagates when weighted household impacts are summed. Calibration to administrative totals — the Enhanced CPS cut deviations from known targets by roughly 97 percent (referenced to Chapter 8) — pins down questions already asked but does nothing for the variance of a question nobody has posed.
  - **Parameter uncertainty.** Tax brackets and benefit rates are usually known exactly; behavioral parameters are not. A meta-regression of 1,720 estimates from 61 studies put the mean elasticity of taxable income (ETI) near 0.30, with individual estimates running from near zero to above 1.0, driven by differences in method, sample, and country [@neisser2021eti]. Illustration of the stakes: a reform raising the top marginal rate by ten points might add $100 billion in revenue at an elasticity of 0.2, or $60 billion at 0.5 — same reform, same model, opposite headlines.
  - **Structural uncertainty.** The model encodes assumptions about how programs interact, how households respond, how the economy adjusts; different assumptions embedded differently in code would produce different results.
  - **Future uncertainty.** Any projection beyond the current year rests on forecasts of wage growth, inflation, and demographic change, which enter the model as fixed numbers.
- The tidy figure on the page is the sum of four kinds of not-knowing reported as if it were one kind of knowing; each layer compounds the ones before it.

### Why it matters
- False precision breeds false confidence: a number reported without a range invites its audience to defend it to the decimal.
- Examples of the failure: legislators treat "23 million" as a fact to attack/defend; PolicyEngine's "£12 billion" prompts "is it worth £12 billion?" not "how sure are you?"; two reforms scored $50 billion and $48 billion make the $2 billion gap read as real even if uncertainty on each is ±$10 billion (i.e., noise).
- The blindness also defeats risk assessment (policymakers often care more about the downside than the central case; a point estimate cannot state a one-in-ten chance the reform costs twice the projection) and undermines model comparison (when Tax-Calculator and PolicyEngine differ, a reader with no interval cannot tell whether one is wrong or both sit inside the same uncertainty).
- The persistence of the single number is a political equilibrium, not mainly a technical oversight: reconciliation rules need one cost figure; journalists need a headline; advocates need a talking point ("this reform lifts two million children out of poverty" mobilizes where "between 1.4 and 2.6 million" does not). Producers know estimates are uncertain; consumers treat them as certain; producers stop reporting a distribution — self-reinforcing.
- The Penn Wharton Budget Model, one of few groups to compare projections to outcomes systematically, found its estimates generally accurate but with meaningful variance [@pwbm2024accuracy].
- CBO publishes retrospective evaluations of its own accuracy: its June 2024 projection underestimated fiscal-year 2025 federal revenues by about 6 percent — $334 billion — largely because it had not anticipated a round of tariff increases [@cbo2025budget_accuracy].
- Across 1984–2023, CBO's record shows revenue is harder to forecast than spending and that errors compound with the horizon [@cbo2024deficit].
- CBO's economic forecasts beat the Administration's, the Blue Chip consensus, and the Survey of Professional Forecasters [@cbo2025forecasting].
- CBO evaluates its aggregate forecast after the fact; no standing, public loop grades each policy score, one by one, against what actually happened.

### Partial solutions
- **Monte Carlo simulation:** run the model many times with inputs drawn from probability distributions and report the spread. Author's example: EggNest, a retirement-planning tool, runs ten thousand scenarios over distributions of market returns, inflation, and wage growth, reporting "a 90 percent chance of between $800,000 and $1.8 million" instead of "you will have $1.2 million at 65." Obstacle for policy microsimulation is cost: PolicyEngine already computes over millions of households; running that ten thousand times multiplies work by four orders of magnitude — seconds become hours.
- **Bootstrap resampling:** draw many samples from the microdata, reweight each to population totals, run the policy on each, read the distribution of results. Embarrassingly parallel — 500 replicates add minutes rather than hours on a cluster. Captures input-data uncertainty (survey is a sample, not a census) and nothing else — says nothing about wrong elasticities or a wrong model. Input-data uncertainty is usually the leading term for the everyday "how much should I trust this?" question.
- **Bayesian methods:** treat a contested elasticity as a distribution (a prior centered near 0.30, updated as evidence accumulates) rather than a constant; requires rebuilding models that hard-code such numbers as fixed values.
- **Squiggle:** a probabilistic-programming language for propagating explicit distributions through a calculation [@squiggle2024]; useful for Fermi-style estimates, awkward to wrap around ten thousand lines of microsimulation.
- **Scenario analysis:** reports a baseline, an optimistic case, and a pessimistic one; conveys sensitivity without attaching probability to the branches.

### The March 31, 2026 paired-subsample demonstration
- Author ran a small paired-subsample experiment in PolicyEngine US on March 31, 2026, to make the leading (input-data) term concrete.
- Method: drew ten 1,000-household subsamples from the then-current Enhanced CPS (data layer since rebuilt as populace); ran the same stylized EITC reform on each baseline/reform pair; recorded the change in aggregate EITC and in household net income.
- Helper script lives at `scripts/policyengine_uncertainty_demo.py`.
- Table (input-data uncertainty only):
  | Statistic | Aggregate EITC change | Aggregate net-income change |
  | --- | ---: | ---: |
  | Full-sample point estimate | -$12.6B | -$13.9B |
  | Mean across 10 paired subsamples | -$12.9B | -$14.0B |
  | Range across 10 paired subsamples | -$11.1B to -$15.0B | -$12.1B to -$16.2B |
- Interpretation: ordinary survey sampling alone — before any behavioral elasticity, forecast, or modeling assumption — moved the national estimate from about 12 percent below the point estimate to about 19 percent above it; large enough to carry a reform across a budget threshold the single figure would have made look safe.
- Caveat stated in text: not a production-grade confidence interval; the subsamples are deliberately small and few; the exercise captures only input-data uncertainty. The reported estimate is the center of a distribution, not the result.
- The experiment was a one-off, run by hand. populace (the calibrated-microdata commons) is meant to make it standing infrastructure: it keeps the machinery that produced the imputations and weights — imputation by quantile regression forests, synthesis across integrated sources, calibration to administrative totals — shipped as certified release bundles, so imputation/synthesis error can be quantified and versioned rather than buried in a fixed file. A later analyst can re-derive the weights and measure how much they could have differed.

### How other fields handle uncertainty (weather = the standard to beat)
- Weather forecasting is the standard the chapter holds everything else to. Modern weather models run an ensemble of simulations from slightly perturbed starting conditions and report a probability distribution.
- "A 60 percent chance of rain" is a calibrated probability: across many such forecasts, it rains on close to 60 percent of the days so labeled.
- What makes it trustworthy is verification: forecasters track whether events predicted at 60 percent happen 60 percent of the time, and recalibrate when the numbers drift. Skill has improved steadily and measurably for decades because every forecast is eventually checked.
- The loop is a procedure, not a metaphor: forecast, resolve, score, recalibrate. Meteorology spent decades building the verification loop; policy analysis has not begun. The parallel to microsimulation is exact in structure (both complex nonlinear systems with many interacting variables).
- Clinical trials report a drug's effect with a confidence interval; "15 percent lower mortality (95% CI: 8–22%)" and "15 percent (95% CI: −2–32%)" are different findings.
- Financial risk management lives on Value at Risk and implied volatility; the 2008 crisis (which exposed how badly those models underweighted tail risk) provoked better uncertainty modeling, not abandonment.
- Climate science runs large model ensembles and reports calibrated language: the IPCC's "likely" means at least 66 percent probability, "very likely" at least 90 percent.
- Election forecasting: a model that gave one 2016 candidate a 29 percent chance and then watched him win was not refuted, because 29 percent is not zero.

### Structural uncertainty and its two cases
- Structural uncertainty is harder than parameter uncertainty: we do not always know whether the model is right. Microsimulation assumes people respond to incentives as they did in historical data; when a policy changes that world dramatically, behavior can move in ways the model was never fitted to see.
- **Finland UBI RCT (the sharp case).** In 2017–2018 the Finnish government ran a randomized controlled trial: 2,000 unemployed people received €560 a month unconditionally, against a control group of 175,000. Microsimulation had predicted that cutting participation tax rates by 23 points would raise employment; the first-year result showed no statistically significant effect on days worked [@kangas2020finland]; the eventual published analysis found only modest second-year gains concentrated in particular subgroups [@hanna2018removing]. The models had the incentive right (participation tax rates did fall by 23 points) and the response wrong, because a permanent unconditional floor is not a marginal tax tweak.
- **ACA individual mandate (the same story from the other direction).** When Congress zeroed the penalty in 2017, CBO projected 13 million fewer insured by 2027, from models in which the mandate was a powerful driver of enrollment [@cbo2017ahca]. The actual effect was far smaller; people had enrolled for subsidies, security, and momentum — reasons the models underweighted because historical data could not separate "enrolled because of the mandate" from "enrolled while the mandate happened to exist."
- Monte Carlo does not rescue this: you can propagate uncertainty through a wrong model and get a precise answer that is precisely wrong. Structural error is the uncertainty we do not know we have; only reality — a forecast committed to in advance that misses by more than its interval allowed — catches it.

### The scoreboard (Thesis Institute)
- The Thesis Institute is the prediction pole of the recomposed stack, the counterpart to Axiom's determinism, under a two-word division of labor: Axiom states, Thesis predicts [@thesisinstitute2026].
- An axiom is accepted truth; a thesis is a proposition put up to be tested. The thing tested is a forecast of a government metric, published with an interval, before the number is known.
- The mechanism is a public docket. Each entry is a forecast of an official statistic — example: the first-print unemployment rate for a given month, meaning the value as the Bureau of Labor Statistics first publishes it, before later revisions. Fixing the target on the first print makes the eventual grade well-defined rather than a matter of argument.
- Each forecast carries an interval, not a point; each is timestamped and locked; each will be graded when the official number lands. On resolution, the ledger records the fact, marks the forecast against its stated interval, and leaves the score where it was made — a public record of first-print facts and resolutions anyone can read.
- This is the accountability loop CBO, the Tax Policy Center, and EUROMOD do not have: not a retrospective study of aggregate accuracy, but a per-forecast, interval-bearing, publicly scored commitment made in advance.
- Counterfactual forecasts ask not only "what will the metric be?" but "what will it be under this policy?" One live entry forecasts Medicaid call-center wait times in March 2027 if the work-requirement verification deadline is delayed — a real administrative answer attached to a policy choice not yet made. Counterfactuals are harder because the world runs only one branch, but the branch actually taken still prints a real figure the forecast can be graded against.
- This is the bridge from simulation to prediction: microsimulation estimates (a reform's cost, its poverty effect, its distributional incidence) become, one by one, forecasts with published intervals that reality will grade.
- The two poles: determinism answers "what does the law say?" and is checked against statute and reference calculators (right or wrong today); prediction answers "what will happen?" and no statutory exactness settles it. The four uncertainties live in the gap between a deterministic calculation and a claim about the future — closed only by making the claim in advance and letting the world grade it.
- Honesty constraint (absolute): as of this writing, not one of those forecasts has resolved. There is no track record — only a mechanism for acquiring one, in public. A scoreboard showing a glowing record on launch day would be untrustworthy because the record would have been assembled unseen. The only credible way to earn trust is to publish before the outcome is known and let outcomes accumulate in the open.
- [Supplementary project fact, not stated in this chapter's text but in scope per the brief: Thesis Institute public launch is planned for roughly September 15, 2026 [@thesisinstitute2026]. Use only if the rewrite needs a launch date; the chapter itself does not name one.]

### Toward epistemic humility, and the CTC re-score
- Practical posture until grades accumulate: treat point estimates as central tendencies, not truths. Read "£12 billion" as "our best guess is near £12 billion, and the true value could reasonably sit twenty percent to either side, or further." Read model disagreements as information about uncertainty. Ask which assumptions move the answer most. Be most skeptical of the most novel policies, where structural uncertainty dominates. An imprecise estimate is still information (roughly $50 billion rules out $5 billion and $500 billion).
- Concrete reform re-score: PolicyEngine scores making the Child Tax Credit fully refundable — removing the refundable cap and the earnings phase-in that hold the poorest families below the full credit — measured against 2026 law [@obbba2025].
- Result: cost of roughly $23 billion for the year; child poverty falls by about 2.6 percentage points, from 16.6 to 14.0 percent.
- Provenance (author's calculation, carried inline as an HTML comment in the source): PolicyEngine US 1.768.3, dense Enhanced CPS, static score, `fully_refundable=True` from 2026; three convergent measures ($22.97B); to be rerun at publication data vintage.
- An uncertainty-aware version would attach a band driven mainly by how many currently non-filing families would claim, and a second band to the child-poverty reduction driven by the systematic income undercount among low-income households in survey data. Central estimates would not move; the poverty effect is robust (even the pessimistic branch shows a meaningful reduction) while the cost has real range.
- The scoreboard can only grade what reality eventually prints — an unemployment rate, a caseload, a wait time, a poverty figure the Census will publish. What people believe, prefer, and are willing to trade away has no first-print release date and no administrative office to certify it — the edge of what ground truth can grade, and the handoff to the opinion chapter.

## Story beats
- **PreCrime / Minority Report frame (opening analogy).** The 2002 film *Minority Report*: three "precogs" foresee future murders with seeming perfection; authorities arrest people before they kill; predictions display as facts, exact to location and minute, no probability attached. The twist: the system produces three forecasts that usually agree and sometimes diverge, and the dissent — the "minority report" — is suppressed to preserve the illusion of certainty. Used as the frame: the suppressed interval on a budget score is "the minority report of policy analysis." (This is the chapter's opening device after the CBO cold open; keep it as intuition, not as the book's Westworld frame — that belongs to the final chapter.)
- **The EggNest aside (author, first person, real specificity).** The author uses Monte Carlo in a real retirement-planning tool that reports a 90% range rather than a single number — a concrete "I built this" beat that grounds the abstract method.
- **The March 31, 2026 demonstration beat (author, first person).** A deliberately small, hand-run experiment presented honestly as a one-off, not production infrastructure — models the book's own humility discipline.
- **The scoreboard reveal / brittleness-of-certainty payoff.** The turn from "here is the problem (false precision)" to "here is the institution being built, in public, to close it" — landing on the absolute honesty constraint that zero forecasts have resolved.

## Quotes
- "There is no track record—only a mechanism for acquiring one, in public." — narrative line, Chapter 13 (protected; see Author-texture).
- No attributed third-party verbatim quotation appears in this chapter. (Brief note: the George Box line "all models are wrong, but some are useful" [@box1976science] listed in the cataloging brief does NOT appear in this chapter's text — it is not present in chapters 13–17 as read; likely lives in an earlier modeling chapter. Flagging so the rewriter does not attribute it here.)

## Arguments
1. Point estimates without intervals are false precision: the tidy single figure is the sum of four kinds of not-knowing (input-data, parameter, structural, future) reported as one kind of knowing.
2. The persistence of the single number is a political equilibrium (reconciliation, headlines, talking points), not merely a technical oversight — which is why the fix has to be institutional, not just methodological.
3. Input-data uncertainty is usually the leading term for everyday trust questions, and it is the cheapest to quantify (bootstrap resampling), so it is where an honest program starts.
4. Structural uncertainty cannot be resampled or prior-widened away; the only thing that catches a missing mechanism is a forecast committed to in advance that reality falsifies (Finland UBI, ACA mandate).
5. Weather forecasting has essentially solved the problem by closing the loop (forecast, resolve, score, recalibrate); policy analysis differs only in never having built the loop, and the loop can be built for policy the same way.
6. The scoreboard is the institutional answer to the uncertainty gap, and it has no track record yet — "There is no track record—only a mechanism for acquiring one, in public." A scoreboard that looked good on day one could not be trusted.
7. The discipline that no simulation is admissible unless its verification chain terminates in ground truth applies most severely to the institution built to enforce it; the prediction pole asks to be checked later, not believed now.
8. An uncertainty-aware estimate is more useful than a clean figure not because it is more precise but because it is more honest about what is known and what is not (the CTC re-score: robust poverty effect, wide cost band).

## Author-texture (verbatim, may be reused; use sparingly)
- "Just: 23 million." (the cold-open punch after the CBO figure)
- "There is no track record—only a mechanism for acquiring one, in public." (protected — the honesty-constraint keeper)
- First-person specific beats worth preserving as raw phrasing (not necessarily verbatim): "I have used this in EggNest, a retirement-planning tool that … reports 'a 90 percent chance of between $800,000 and $1.8 million.'"; "To make the leading term concrete, I ran a small paired-subsample experiment in PolicyEngine US on March 31, 2026."

## Structural notes
- **Chapter job:** Close Part 4 (prediction) by exposing the false-precision problem in microsimulation output, cataloging the four-part uncertainty taxonomy, surveying partial fixes, holding everything to the weather-forecasting verification standard, and introducing the Thesis Institute scoreboard as the institutional answer — while insisting, absolutely, that it has no track record yet.
- **Handoff in (from prior chapter):** picks up microsimulation results that have always been single numbers.
- **Handoff out (13→14, i.e., to the opinion chapter):** the scoreboard can only grade what reality prints; what people believe/prefer/trade has no first-print number, so simulating opinion steps "past the edge of what ground truth can grade."
- **Phrasing constraints (hard):**
  - The zero-resolved-forecasts honesty is ABSOLUTE — never imply the scoreboard has a record. Any track-record language must be negated ("no track record — only a mechanism for acquiring one").
  - Keep "23 million" framed as false precision, not as a CBO error (CBO is explicitly not being faulted).
  - The CTC re-score numbers are the author's static calculation at a specific model version (PolicyEngine US 1.768.3); preserve provenance and the "rerun at publication vintage" caveat; do not present as an official score.
  - The March 31, 2026 experiment is input-data-uncertainty-only and explicitly not a production confidence interval — do not upgrade its status.
  - Retired-name guard: the data layer is populace (never "microplex"); Axiom is the determinism pole; Thesis is the prediction pole.

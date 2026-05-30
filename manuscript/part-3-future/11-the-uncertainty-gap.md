# Chapter 11: The Uncertainty Gap

In 2017, the Congressional Budget Office released its analysis of the American Health Care Act, the Republican plan to repeal and replace Obamacare [@cbo2017ahca]. The headline number: 23 million fewer Americans would have health insurance by 2026.

Not "approximately 23 million." Not "between 18 and 28 million." Just: 23 million.

The number was devastatingly precise—and that precision was an illusion. Not because CBO made an error, and not because 23 million was a poor central estimate, but because any forecast nearly a decade out carries enormous uncertainty that a single number cannot express. Economic conditions might change. Behavioral responses might differ from historical patterns. The labor market might evolve unpredictably. Yet the public discourse treated "23 million" as if it were a measurement, not an estimate.

It's the PreCrime problem from *Minority Report*. In the 2002 film, three "precogs" predict future murders with seemingly perfect accuracy. Authorities arrest people before crimes occur. The predictions look like facts—displayed on screens, precise down to the location and time. No uncertainty, no probability, just destiny.

But the story's twist reveals the system produces *three* different predictions that usually agree but sometimes diverge. The "minority report" is the dissenting prediction, suppressed to maintain the illusion of certainty. When predictions become policy, admitting uncertainty becomes politically impossible.

This is the dirty secret of microsimulation: the models produce point estimates without confidence intervals. And that precision is largely an illusion.

---

## The Point Estimate Problem

Every microsimulation result you've seen in this book has been a single number. The UK reform costs £12 billion. The policy reduces poverty by 15%. The marginal tax rate is 47%. These figures emerge from complex calculations involving millions of simulated households—but they arrive without any indication of how confident we should be in them.

This isn't a bug in any particular model. It's structural. The microsimulation paradigm, from Orcutt onward, was built to answer "what would happen if?" questions. It produces scenarios, not probability distributions.

Consider what goes into a PolicyEngine estimate:

**Input data uncertainty.** The model uses survey data (the Current Population Survey in the US, the Family Resources Survey in the UK) that samples households from the broader population. Every survey has sampling error—the actual population might differ from what the survey captured. The CPS samples about 100,000 households from a nation of 130 million. That's a remarkably good sample by survey standards—but it means that individual cells in the data (say, self-employed workers in Montana with investment income) may contain only a handful of observations. When you compute a national cost estimate by summing weighted household impacts, the sampling uncertainty propagates. PolicyEngine's Enhanced CPS reduced deviations from administrative totals by 97 percent through calibration (Chapter 8), but that calibration optimizes to match known targets—it doesn't eliminate the underlying sampling variance for questions nobody has asked yet. And even calibrated weights carry residual uncertainty that the model ignores.

**Parameter uncertainty.** Tax brackets, benefit rates, eligibility thresholds—these are usually known precisely. But behavioral parameters are estimated from research: how much do people change their labor supply when marginal tax rates change? Different studies produce different estimates. The model picks one and treats it as truth.

The elasticity of taxable income—the key parameter governing how much people adjust their reported income in response to tax changes—illustrates this perfectly. A meta-regression analysis of 1,720 estimates from 61 studies found a mean elasticity of 0.30, but individual estimates ranged from near zero to above 1.0, driven by differences in regression techniques, sample restrictions, and country contexts [@neisser2021eti]. The range isn't just academic: a reform that raises the top marginal tax rate by 10 percentage points might increase revenue by $100 billion with an elasticity of 0.2, or only $60 billion with an elasticity of 0.5. Same reform, same model, wildly different conclusions—depending on which study you trust for a single parameter.

**Structural uncertainty.** The model makes assumptions about how programs interact, how households respond, how the economy adjusts. These assumptions are embedded in the code. Alternative assumptions would produce different results.

**Future uncertainty.** Any projection beyond the current year involves forecasts—wage growth, inflation, demographic change. These forecasts are themselves uncertain, but they enter the model as fixed numbers.

Each layer of uncertainty compounds. Yet the output is a single number.

---

## Why This Matters

You might think uncertainty is a technical detail—interesting to methodologists but irrelevant to users. It's not. The absence of uncertainty quantification distorts how people use and understand policy analysis.

**False precision breeds false confidence.** When CBO says "23 million," legislators treat it as a fact to be attacked or defended rather than an estimate to be understood. When PolicyEngine says a reform costs £12 billion, users don't ask "how confident are you?" They ask "is it worth £12 billion?"

**Comparison becomes impossible.** Suppose Reform A costs $50 billion and Reform B costs $48 billion. Is Reform B cheaper? Maybe—but if the uncertainty on each estimate is ±$10 billion, the difference is noise. Without uncertainty bounds, we can't distinguish meaningful differences from statistical artifacts.

**Risk assessment fails.** Policymakers often care more about downside scenarios than expected values. What's the worst case for this reform? What's the probability it costs twice as much as projected? Point estimates can't answer these questions.

**Model comparison is undermined.** Different microsimulation models produce different estimates for the same policy. Is one right and another wrong? Or are they both within reasonable uncertainty bounds? Without quantification, we can't tell.

The Penn Wharton Budget Model, one of the few groups to systematically compare projections to outcomes, found that their estimates were generally accurate but had meaningful variance [@pwbm2024accuracy]. CBO itself has started publishing retrospective accuracy evaluations—and the results are illuminating. In its June 2024 projections for fiscal year 2025, CBO underestimated federal revenues by 6 percent—$334 billion off [@cbo2025budget_accuracy]. The largest single factor was tariff increases that the agency hadn't anticipated, a reminder that policy itself is uncertain. Over longer horizons, CBO's track record on deficit projections from 1984 to 2023 shows systematic patterns: revenue is harder to forecast than spending, and errors compound over time [@cbo2024deficit]. These aren't failures of competence—CBO's economic forecasts are actually more accurate than those of the Administration, the Blue Chip consensus, and the Survey of Professional Forecasters [@cbo2025forecasting]. They're evidence that even the best forecasters working with the best data face irreducible uncertainty.

But most microsimulation, including PolicyEngine, produces point estimates only.

The persistence of point estimates isn't just a technical oversight. It's a political equilibrium. Budget scoring requires a single number because legislation needs a cost estimate for reconciliation rules—you can't pass a bill that "probably costs between $40 billion and $65 billion." CBO's analysts know their estimates are uncertain, but the legislative process demands precision that doesn't exist. Journalists need a headline, not a probability density function. Advocacy groups need a talking point: "this reform lifts 2 million children out of poverty" mobilizes support in a way that "this reform lifts between 1.4 and 2.6 million children out of poverty" does not.

This creates a perverse dynamic. Producers of analysis know the estimates are uncertain. Consumers of analysis treat them as certain. And the producers, knowing the consumers won't engage with uncertainty, don't bother reporting it. The illusion of precision becomes self-reinforcing.

Breaking this cycle may require institutional leadership. When the National Weather Service first reported probabilistic forecasts, public reception was skeptical—people wanted to know whether it would rain, not that there was a 40 percent chance. But over time, probabilistic thinking became normal. Today, "60 percent chance of rain" is intuitive to most Americans. Policy analysis could follow the same arc: initially uncomfortable, eventually expected. CBO's fan charts are a first step. But they'll only become standard if users demand them—and users will only demand them if they understand what they're missing.

---

## The Welfare Cost of Hidden Uncertainty

Uncertainty is not only a presentation problem for analysts. It changes behavior.

Taxpayers respond to the marginal tax rates they perceive, not the marginal tax rates a model computes. In a separate project, I modeled workers choosing labor supply from a noisy signal of their true marginal tax rate. Under quasilinear-isoelastic preferences, the expected deadweight loss from misperception has a simple approximation: roughly one half times the labor-supply elasticity times the variance of the rate error, divided by one minus the true marginal rate, all multiplied by earnings [@ghenis2026disutility].

The calibrated numbers are preliminary, but the scale is not trivial. Using a 12 percentage point standard deviation for federal marginal-rate misperception, the stylized central estimate is about $30 billion per year in aggregate welfare cost. Applying the same logic to person-level marginal tax rates from PolicyEngine US raises the estimate to about $37 billion, with sensitivity ranges from roughly $10 billion to $71 billion depending on parameter assumptions [@ghenis2026disutility].

The point is not that these are definitive costs. The point is that hidden uncertainty is itself costly. If households cannot tell whether an extra hour of work leaves them better off or worse off, some will make distorted choices. Tools that expose marginal tax rates, benefit cliffs, and confidence ranges are not merely nicer dashboards. They can reduce real welfare losses caused by policy opacity.

---

## Partial Solutions

The problem is recognized. Solutions are emerging, though none is complete.

### Monte Carlo Simulation

The most straightforward approach: run the model many times with different inputs sampled from probability distributions. Instead of one estimate, you get a distribution of estimates.

I've used this approach in EggNest, a retirement planning tool. Rather than telling users "you'll have $1.2 million at age 65," it runs 10,000 scenarios sampling from distributions of market returns, inflation, and wage growth. The output is a probability distribution: "there's a 90% chance you'll have between $800,000 and $1.8 million."

The challenge for policy microsimulation is computational cost. PolicyEngine calculates results for millions of households. Running that calculation 10,000 times would multiply computing requirements by four orders of magnitude. Some policies that currently take seconds would take hours.

### Bayesian Methods

Bayesian inference treats parameters as probability distributions rather than fixed values. Instead of assuming the labor supply elasticity is 0.3, you might specify a prior distribution (perhaps normal with mean 0.3 and standard deviation 0.1) and update it with data.

Fred Forecaster, a time series prediction tool I've built, uses Bayesian structural time series models from PyMC. The output includes credible intervals—ranges within which the true value falls with specified probability.

Applying this to microsimulation would require rethinking the entire architecture. Current models treat parameters as constants embedded in code. A Bayesian approach would require probabilistic programming frameworks and substantial redesign.

### Squiggle and Fermi Estimation

Squiggle, developed by the Quantified Uncertainty Research Institute, is a language for probabilistic estimation [@squiggle2024]. Instead of writing `cost = revenue - expenses`, you write distributions: `cost = normal(100, 10) - lognormal(50, 1.5)`. The output is a probability distribution that propagates uncertainty through calculations.

I've used Squigglepy, a Python implementation, in Democrasim—a model of voter behavior and election outcomes. Rather than predicting "Candidate A wins with 52%," it produces distributions: "Candidate A wins 60% of simulations, with vote shares ranging from 48% to 56%."

The limitation: Squiggle works well for Fermi estimation (rough calculations with explicit uncertainty) but doesn't integrate naturally with detailed microsimulation. You can't easily wrap PolicyEngine's 10,000 lines of Python in Squiggle distributions.

### Bootstrap Resampling

A middle ground between full Monte Carlo and no uncertainty at all: resample the survey data itself. Draw many bootstrap samples from the microdata (say, 500), reweight each to match population totals, and run the policy simulation on each. The result is a distribution of estimates that reflects sampling uncertainty without requiring any changes to the policy engine.

This approach has a practical advantage: it's embarrassingly parallel. Each bootstrap replicate is independent, so the computation scales linearly with the number of processors. On a cloud computing cluster, 500 replicates might add minutes rather than hours to a simulation that currently takes seconds. And it captures the most important source of uncertainty for many estimates—the fact that the survey is a sample, not a census.

The limitation is that bootstrap resampling captures only input data uncertainty. It tells you nothing about parameter uncertainty (wrong elasticities) or structural uncertainty (wrong model). But for many practical questions—"how confident should I be in this cost estimate?"—input data uncertainty is the dominant term, and bootstrapping answers it directly.

### A Simple PolicyEngine Demonstration

To make this concrete, I ran a small paired-subsample experiment in PolicyEngine US on March 31, 2026. Using the Enhanced CPS, I took ten 1,000-household subsamples, ran the same stylized EITC reform on each baseline/reform pair, and recorded the change in aggregate EITC and household net income. The helper script for reproducing this calculation now lives in `scripts/policyengine_uncertainty_demo.py`.

| Statistic | Aggregate EITC change | Aggregate household net income change |
| --- | ---: | ---: |
| Full-sample point estimate | -$12.6B | -$13.9B |
| Mean across 10 paired subsamples | -$12.9B | -$14.0B |
| Range across 10 paired subsamples | -$11.1B to -$15.0B | -$12.1B to -$16.2B |

Across the ten subsamples, ordinary survey sampling alone moved the national estimate by roughly 12% below to 19% above the full-sample point estimate before touching behavioral elasticities, forecast error, or model misspecification.

This is not a production-quality confidence interval. The subsamples are intentionally lightweight, the number of replicates is small, and the exercise captures only input-data uncertainty. But it demonstrates the right intuition: the single reported estimate is not the result. It is the center of a distribution that most policy tools currently hide.

### Scenario Analysis

The simplest approach: run the model under different assumptions and present multiple results. "Under baseline assumptions, the reform costs $50B. Under optimistic labor supply assumptions, $40B. Under pessimistic assumptions, $65B."

This provides some sense of sensitivity but doesn't quantify probability. Users must decide which scenario is most likely. And with dozens of uncertain parameters, the number of combinations explodes.

---

## The Aspiration: Uncertainty-Aware Policy Analysis

What would a fully uncertainty-aware microsimulation look like?

**Input distributions.** Survey weights would have standard errors. Microdata would include variance estimates from the sampling process.

**Parameter distributions.** Behavioral parameters would come with probability distributions reflecting the range of research estimates. The elasticity of taxable income wouldn't be 0.4—it would be a distribution centered on 0.4 with uncertainty reflecting disagreement in the literature.

**Propagated uncertainty.** Calculations would flow through the model as distributions, not points. The output would be a probability distribution over costs, poverty impacts, and other outcomes.

**Communicable results.** Users would see not just "this costs $50B" but visualizations showing the full range of possibilities. They could ask: "What's the probability this costs more than $60B?" and get answers.

This is technically feasible. The tools exist—Monte Carlo, Bayesian inference, probabilistic programming. The barriers are computational (running thousands of scenarios is expensive), architectural (current models weren't designed for uncertainty), and institutional (funders and users expect point estimates).

Some progress is happening. CBO has started publishing uncertainty ranges for some long-term projections. Since 2019, they've reported "fan charts" for major budget forecasts—symmetrical bands showing the range of outcomes consistent with historical forecast errors. Their 10-year deficit projections now include shaded regions covering the 25th to 75th and 5th to 95th percentile ranges from past performance. This is exactly the kind of calibrated uncertainty that policy analysis needs.

Academic researchers increasingly report sensitivity analyses. The Squiggle community is building tools specifically for policy-relevant estimation. And the financial sector's experience with Value at Risk models offers a cautionary template: even imperfect uncertainty quantification is better than none, as long as users understand the models' limitations—which the 2008 crisis showed they often don't.

But we're far from the aspiration. When you use PolicyEngine today, you get a number. You should mentally add "±something" to every result—but the model won't tell you how much.

---

## How Other Fields Handle Uncertainty

Policy microsimulation's failure to report uncertainty is unusual. Most quantitative fields have solved this problem—or at least confronted it honestly.

**Weather forecasting** is the gold standard. Modern weather models don't produce a single forecast—they run ensemble simulations, perturbing initial conditions slightly and seeing how the forecasts diverge. The European Centre for Medium-Range Weather Forecasts runs 51 ensemble members for each forecast cycle, producing not a prediction but a probability distribution. The National Weather Service reports "60% chance of rain"—a calibrated probability that reflects genuine uncertainty about atmospheric dynamics. Crucially, these probabilities are *verified*: meteorologists track whether events predicted at 60% probability actually occur 60% of the time. When they don't, the models are recalibrated. Forecast skill improves continuously, and the improvement is measured precisely: the five-day forecast today is as accurate as the three-day forecast was thirty years ago. The parallel to microsimulation is striking: both involve complex nonlinear systems with many interacting variables. But meteorology invested decades in ensemble methods and calibration. Policy simulation hasn't started.

**Clinical trials** report confidence intervals as a matter of scientific practice. A drug that reduces mortality by 15% (95% CI: 8% to 22%) tells clinicians something fundamentally different from a drug that reduces mortality by 15% (95% CI: -2% to 32%). The first is reliably beneficial. The second might not help at all. The confidence interval isn't optional context—it's the core information.

**Financial risk management** lives on uncertainty quantification. Value at Risk models estimate the worst-case loss at a given confidence level. Portfolio optimization uses covariance matrices. Options pricing depends on implied volatility. The 2008 financial crisis revealed that these models underestimated tail risks—but the response was to improve uncertainty modeling, not to abandon it.

**Climate modeling** runs large ensembles of global climate models, producing probability distributions over temperature increases, sea level rise, and precipitation changes. The IPCC reports use calibrated uncertainty language: "likely" means 66-100% probability, "very likely" means 90-100%.

**Election forecasting** has evolved from punditry to probabilistic modeling. FiveThirtyEight's models didn't say "Candidate X will win." They said "Candidate X wins in 72% of simulations." The models ran thousands of scenarios, varying turnout, polling error, and state-level correlations. When Nate Silver said there was a 29% chance of a Trump victory in 2016, and Trump won, that wasn't a failure—it was an event within the stated uncertainty. The lesson for policy analysis: probabilistic framing changes how people process predictions and prepares them for outcomes that differ from the central estimate.

Policy microsimulation is the outlier. It produces outputs of comparable complexity to climate projections—millions of interacting variables, uncertain parameters, structural assumptions—but reports them without uncertainty bounds. The gap isn't technological; the statistical tools exist. It's institutional and cultural. Funders expect clean numbers. Legislators need single estimates for budget scoring. Journalists want headlines, not distributions.

Closing this gap is the central methodological challenge for the next decade of microsimulation.

---

## The Deeper Issue: Uncertainty About Structure

There's a harder problem beneath parameter uncertainty: we don't know if the model is right.

Parameter uncertainty assumes the model structure is correct and only the numbers are uncertain. But what if the model is missing something fundamental?

Microsimulation models assume people respond to incentives in ways estimated from historical data. But historical data reflects a particular context—specific labor markets, cultural norms, policy environments. When policies change dramatically, behavior might change in ways the model can't anticipate.

Consider universal basic income. Most microsimulation models estimate labor supply responses using elasticities from marginal tax changes—small policy variations that leave the fundamental structure of work unchanged. But UBI might change the meaning of work, the relationship between employment and identity, the nature of economic security. Would responses to UBI mirror responses to a 5% change in marginal tax rates? Maybe not.

Finland tested this. In 2017-2018, the Finnish government ran a randomized controlled trial: 2,000 unemployed individuals received a basic income of €560 per month with no conditions, while 175,000 similar individuals formed the control group. Microsimulation models had predicted that reducing participation tax rates by 23 percentage points—the effective incentive change—would increase employment. The experiment found no statistically significant effect on employment days in the first year [@kangas2020finland]. The eventual AEJ paper found modest positive effects in the second year, concentrated among specific subgroups [@hanna2018removing]. But the headline result was clear: the microsimulation predictions, grounded in historical elasticities, overstated the employment response. The models weren't wrong about the incentive structure—participation tax rates did fall by 23 points. They were wrong about how people would respond to a fundamentally different kind of program.

This is structural uncertainty—uncertainty about whether the model captures the relevant causal mechanisms at all. No amount of Monte Carlo simulation addresses this. You can propagate uncertainty through a wrong model and get precise estimates that are precisely wrong.

The ACA individual mandate tells a similar story from the other direction. When Congress zeroed out the mandate penalty in 2017, CBO projected that 13 million fewer people would have health insurance by 2027—a number derived from models where the mandate was a powerful driver of enrollment [@cbo2017ahca]. The actual effect was far smaller. People had enrolled for reasons the models didn't fully capture: the availability of subsidies, the peace of mind of coverage, the administrative momentum of having signed up. The models overweighted the penalty's importance because historical data couldn't distinguish between "people enrolled because of the mandate" and "people enrolled at the same time the mandate existed."

The honest answer is uncomfortable: we can quantify uncertainty about things we know we don't know (parameter values, sampling error), but we can't easily quantify uncertainty about things we don't know we don't know (model misspecification, structural breaks, emergent behavior).

---

## Toward Epistemic Humility

What does this mean for how we should use microsimulation?

First, treat point estimates as central tendencies, not truths. When PolicyEngine says a reform costs £12 billion, read it as "our best guess is around £12 billion, but the true value could reasonably be 20% higher or lower, and in unusual circumstances might be very different."

Second, pay attention to model comparisons. When Tax-Calculator and PolicyEngine produce different estimates, that's information about uncertainty—not just evidence that one model is wrong.

Third, ask about sensitivity. Which assumptions matter most? If changing the labor supply elasticity from 0.3 to 0.5 changes the cost estimate by 30%, that's worth knowing. If it barely matters, you can have more confidence in the result.

Fourth, be especially skeptical of novel policies. Microsimulation is most reliable for policies similar to existing ones—small changes where historical evidence is relevant. For radical reforms, structural uncertainty dominates, and point estimates become more speculative.

Finally, remember that point estimates are still useful. Knowing that a reform costs "approximately $50 billion" is better than no information. The uncertainty isn't infinite—we know the cost isn't $5 billion or $500 billion. Even imprecise estimates narrow the range of possibilities.

Consider what this looks like in practice. Suppose PolicyEngine estimates that making the Child Tax Credit fully refundable costs $12 billion per year and reduces child poverty by 15 percent. An uncertainty-aware version might report: the cost is $12 billion ±$3 billion (driven mainly by uncertainty in how many currently non-filing families would claim the credit), and the poverty reduction is 15 percent ±4 percentage points (driven by uncertainty in income measurement for low-income households, which surveys systematically undercount). The central estimate hasn't changed. But the user now knows that the poverty impact is robust—even the pessimistic scenario shows meaningful reduction—while the cost estimate has real range. That's more useful than a single number, not because it's more precise, but because it's more honest about what we know and don't know.

---

## The Road Ahead

Uncertainty quantification is coming to microsimulation, slowly. Computational costs are falling—cloud computing makes it feasible to run thousands of parallel simulations that would have been prohibitive a decade ago. Probabilistic programming tools are maturing: PyMC, Stan, and NumPyro make Bayesian inference accessible to engineers who aren't statisticians. The research community increasingly recognizes that point estimates without uncertainty are incomplete.

PolicyEngine will eventually report uncertainty bounds. The infrastructure projects enabling this—Squigglepy for probabilistic estimation, EggNest for Monte Carlo simulation, MicroCalibrate for robust survey weights—are pieces of a larger puzzle. The most tractable first step is probably bootstrapping over survey weights: draw many samples from the microdata, recompute the policy estimate for each, and report the resulting distribution. This captures input data uncertainty—which for many estimates is the dominant source—without requiring any changes to the policy engine itself. Parameter uncertainty is harder, because it requires specifying prior distributions over behavioral parameters that are themselves contested. Structural uncertainty is hardest of all, because it requires imagining models you haven't built.

AI might accelerate progress. Language models can already read research papers and extract parameter estimates. A system that automatically surveyed the literature on labor supply elasticities, compiled the distribution of published estimates, and attached that distribution as a prior to the relevant microsimulation parameter would be genuinely useful—transforming months of manual literature review into something approaching automation. This wouldn't solve structural uncertainty, but it would make parameter uncertainty quantification tractable for models with hundreds of behavioral parameters.

But the deeper lesson is epistemological. Microsimulation is powerful because it simulates complex systems—millions of households, thousands of policy rules, intricate interactions. That power comes with a temptation to believe the outputs are precise.

They're not. They never were. Acknowledging that honestly—quantifying uncertainty where we can, recognizing structural uncertainty where we can't—is part of building tools worthy of trust.

The aspiration isn't perfect prediction. It's calibrated uncertainty: knowing what we know, knowing what we don't know, and being honest about both.

---

*This reform costs $50 billion.*

*Actually: this reform probably costs somewhere between $40 billion and $65 billion, the distribution is roughly normal with a slight right skew, and there's maybe a 5% chance our model is missing something fundamental that would change the answer entirely.*

*Which statement serves the public better?*

---

## References

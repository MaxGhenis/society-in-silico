# Chapter 11: The Uncertainty Gap

In 2017, the Congressional Budget Office released its analysis of the American Health Care Act, the Republican plan to repeal and replace Obamacare {cite}`cbo2017ahca`. The headline number: 23 million fewer Americans would have health insurance by 2026.

Not "approximately 23 million." Not "between 18 and 28 million." Just: 23 million.

The number was devastatingly precise—and almost certainly wrong. Not because CBO made an error, but because any forecast a decade out involves enormous uncertainty. Economic conditions might change. Behavioral responses might differ from historical patterns. The labor market might evolve unpredictably. Yet the public discourse treated "23 million" as if it were a measurement, not an estimate.

It's the PreCrime problem from *Minority Report*. In the 2002 film, three "precogs" predict future murders with seemingly perfect accuracy. Authorities arrest people before crimes occur. The predictions look like facts—displayed on screens, precise down to the location and time. No uncertainty, no probability, just destiny.

But the story's twist reveals the system produces *three* different predictions that usually agree but sometimes diverge. The "minority report" is the dissenting prediction, suppressed to maintain the illusion of certainty. When predictions become policy, admitting uncertainty becomes politically impossible.

This is the dirty secret of microsimulation: the models produce point estimates without confidence intervals. And that precision is largely an illusion.

---

## The Point Estimate Problem

Every microsimulation result you've seen in this book has been a single number. The UK reform costs £12 billion. The policy reduces poverty by 15%. The marginal tax rate is 47%. These figures emerge from complex calculations involving millions of simulated households—but they arrive without any indication of how confident we should be in them.

This isn't a bug in any particular model. It's structural. The microsimulation paradigm, from Orcutt onward, was built to answer "what would happen if?" questions. It produces scenarios, not probability distributions.

Consider what goes into a PolicyEngine estimate:

**Input data uncertainty.** The model uses survey data (the Current Population Survey in the US, the Family Resources Survey in the UK) that samples households from the broader population. Every survey has sampling error—the actual population might differ from what the survey captured. But microsimulation treats the survey as if it perfectly represents reality.

**Parameter uncertainty.** Tax brackets, benefit rates, eligibility thresholds—these are usually known precisely. But behavioral parameters are estimated from research: how much do people change their labor supply when marginal tax rates change? Different studies produce different estimates. The model picks one and treats it as truth.

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

The Penn Wharton Budget Model, one of the few groups to systematically compare projections to outcomes, found that their estimates were generally accurate but had meaningful variance {cite}`pwbm2024accuracy`. CBO publishes uncertainty ranges for some estimates. But most microsimulation, including PolicyEngine, produces point estimates only.

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

Squiggle, developed by the Quantified Uncertainty Research Institute, is a language for probabilistic estimation {cite}`squiggle2024`. Instead of writing `cost = revenue - expenses`, you write distributions: `cost = normal(100, 10) - lognormal(50, 1.5)`. The output is a probability distribution that propagates uncertainty through calculations.

I've used Squigglepy, a Python implementation, in Democrasim—a model of voter behavior and election outcomes. Rather than predicting "Candidate A wins with 52%," it produces distributions: "Candidate A wins 60% of simulations, with vote shares ranging from 48% to 56%."

The limitation: Squiggle works well for Fermi estimation (rough calculations with explicit uncertainty) but doesn't integrate naturally with detailed microsimulation. You can't easily wrap PolicyEngine's 10,000 lines of Python in Squiggle distributions.

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

Some progress is happening. CBO has started publishing uncertainty ranges for some long-term projections. Academic researchers increasingly report sensitivity analyses. The Squiggle community is building tools specifically for policy-relevant estimation.

But we're far from the aspiration. When you use PolicyEngine today, you get a number. You should mentally add "±something" to every result—but the model won't tell you how much.

---

## The Deeper Issue: Uncertainty About Structure

There's a harder problem beneath parameter uncertainty: we don't know if the model is right.

Parameter uncertainty assumes the model structure is correct and only the numbers are uncertain. But what if the model is missing something fundamental?

Microsimulation models assume people respond to incentives in ways estimated from historical data. But historical data reflects a particular context—specific labor markets, cultural norms, policy environments. When policies change dramatically, behavior might change in ways the model can't anticipate.

Consider universal basic income. Most microsimulation models estimate labor supply responses using elasticities from marginal tax changes—small policy variations that leave the fundamental structure of work unchanged. But UBI might change the meaning of work, the relationship between employment and identity, the nature of economic security. Would responses to UBI mirror responses to a 5% change in marginal tax rates? Maybe not.

This is structural uncertainty—uncertainty about whether the model captures the relevant causal mechanisms at all. No amount of Monte Carlo simulation addresses this. You can propagate uncertainty through a wrong model and get precise estimates that are precisely wrong.

The honest answer is uncomfortable: we can quantify uncertainty about things we know we don't know (parameter values, sampling error), but we can't easily quantify uncertainty about things we don't know we don't know (model misspecification, structural breaks, emergent behavior).

---

## Toward Epistemic Humility

What does this mean for how we should use microsimulation?

First, treat point estimates as central tendencies, not truths. When PolicyEngine says a reform costs £12 billion, read it as "our best guess is around £12 billion, but the true value could reasonably be 20% higher or lower, and in unusual circumstances might be very different."

Second, pay attention to model comparisons. When Tax-Calculator and PolicyEngine produce different estimates, that's information about uncertainty—not just evidence that one model is wrong.

Third, ask about sensitivity. Which assumptions matter most? If changing the labor supply elasticity from 0.3 to 0.5 changes the cost estimate by 30%, that's worth knowing. If it barely matters, you can have more confidence in the result.

Fourth, be especially skeptical of novel policies. Microsimulation is most reliable for policies similar to existing ones—small changes where historical evidence is relevant. For radical reforms, structural uncertainty dominates, and point estimates become more speculative.

Finally, remember that point estimates are still useful. Knowing that a reform costs "approximately $50 billion" is better than no information. The uncertainty isn't infinite—we know the cost isn't $5 billion or $500 billion. Even imprecise estimates narrow the range of possibilities.

---

## The Road Ahead

Uncertainty quantification is coming to microsimulation, slowly. Computational costs are falling. Probabilistic programming tools are maturing. The research community increasingly recognizes that point estimates without uncertainty are incomplete.

PolicyEngine will eventually report uncertainty bounds. The infrastructure projects enabling this—Squigglepy for probabilistic estimation, EggNest for Monte Carlo simulation, MicroCalibrate for robust survey weights—are pieces of a larger puzzle.

But the deeper lesson is epistemological. Microsimulation is powerful because it simulates complex systems—millions of households, thousands of policy rules, intricate interactions. That power comes with a temptation to believe the outputs are precise.

They're not. They never were. Acknowledging that honestly—quantifying uncertainty where we can, recognizing structural uncertainty where we can't—is part of building tools worthy of trust.

The aspiration isn't perfect prediction. It's calibrated uncertainty: knowing what we know, knowing what we don't know, and being honest about both.

---

*This reform costs $50 billion.*

*Actually: this reform probably costs somewhere between $40 billion and $65 billion, the distribution is roughly normal with a slight right skew, and there's maybe a 5% chance our model is missing something fundamental that would change the answer entirely.*

*Which statement serves the public better?*

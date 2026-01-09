# Chapter 14: Simulating Values

**Note to readers**: This chapter describes early-stage research, not established methodology. Unlike PolicyEngine (validated by government use and millions of simulations) or even HiveSight (with preliminary empirical validation), value forecasting is at the experiment stage. I ran the first systematic tests in 2024—LLMs outperformed baselines by 2.2×, but also missed an unexpected reversal in the 2024 GSS data. The results suggest this research direction is promising but far from proven. Treat the philosophical framework as speculative and the empirical claims as preliminary findings requiring extensive validation.

**Validation status across the book's tools**:
- **Proven**: PolicyEngine (government-validated, million+ simulations, production system)
- **Preliminary**: Cosilico and HiveSight (prototypes with some validation, not production-ready)
- **Theoretical**: Democrasim and value forecasting (experimental models with limited validation)

---

We've built tools to simulate households, policies, voters, and opinions. But the deepest question isn't "what do people want today?"

It's: *What would they want after reflection?*

This chapter ventures into territory where simulation meets philosophy, where forecasting meets ethics. The practical tools we've built in earlier chapters connect to a larger question: How do we align increasingly powerful AI systems with human values?

In 2024, I ran the first systematic experiments testing whether large language models can forecast value change. The results were striking: LLMs outperformed statistical baselines by a factor of 2.2, but they also revealed the profound difficulty of the problem. When the 2024 General Social Survey showed an unexpected reversal in same-sex acceptance—dropping from 72% to 55%—every model, including the LLMs, missed it.

---

## The Alignment Problem

As AI systems become more capable, a question looms: What should they be trying to do?

The naive answer—"do what humans want"—immediately fractures. Which humans? Their stated preferences or revealed preferences? What they want now or what they'd want with better information? What one culture values or what's universal?

Current approaches to AI alignment take different positions:

**RLHF (Reinforcement Learning from Human Feedback)** trains AI on current human preferences. Rate these outputs; the model learns what we approve of. Problem: our current preferences may be biased, inconsistent, or short-sighted.

**Constitutional AI** defines principles the AI should follow. Don't be harmful, be helpful, be honest. Problem: who writes the constitution? How do you handle genuine moral disagreement?

**Idealized values** asks what fully rational, fully informed humans would want. Problem: this is a philosophical thought experiment, not an empirical research program.

Each approach has merit. None has cracked the fundamental difficulty: values are contested, evolving, and uncertain.

---

## What If We Could Forecast Values?

Here's an alternative framing: What if AI alignment isn't about finding the "correct" values, but about *forecasting* where values are heading?

Consider same-sex marriage. In 1986, 32% of Americans supported it. By 2021, 79% did. The change wasn't random—it followed patterns that, in retrospect, seem predictable. As exposure increased, as generational replacement occurred, as arguments crystallized, support grew.

What if you could have predicted this trajectory in 1996?

More importantly: what if you could predict which of today's contested values will be accepted and which rejected after another generation of reflection?

This isn't about finding moral truth. It's about forecasting moral change—the same way economists forecast economic variables or meteorologists forecast weather. Not perfectly, but better than chance.

---

## The Value Forecasting Proposal

The idea is simple in concept, ambitious in execution:

**Step 1: Train language models on historical data.** Use surveys from decades past—the General Social Survey back to 1972, Gallup polls, the World Values Survey. Train models to understand what people believed, why, and how those beliefs connected to demographic characteristics.

**Step 2: Test predictive accuracy.** If you train a model on data through 1996, can it predict value trajectories through 2021? This is empirically testable. Either the model predicts moral change better than baseline or it doesn't.

**Step 3: If validated, project forward.** What values would humanity converge toward after extended reflection? Not a decade, but a century. Not with today's constraints, but in post-scarcity conditions.

**Step 4: Use that projection as an alignment target.** Instead of aligning AI to our current, possibly confused values, align it to our projected post-reflection values.

This transforms alignment from philosophy to forecasting.

---

## Heterogeneity as Feature

Here's the crucial insight: don't assume humanity converges to one value system.

A post-scarcity, post-reflection humanity might look like:

| Value System | Population Share |
|--------------|------------------|
| Individual liberty priority | 30% |
| Collective welfare priority | 25% |
| Environmental stewardship | 20% |
| Spiritual/transcendent focus | 15% |
| Other frameworks | 10% |

The alignment target isn't picking one. It's the *distribution*.

An AI aligned to this distribution would:
- Take actions that score well across multiple value systems
- Exercise caution when value systems disagree
- Avoid moves that catastrophically violate any significant fraction of values
- Support conditions where diverse value systems can coexist

This is value pluralism as engineering constraint, not philosophical preference.

---

## Uncertainty at Two Levels

The projection comes with uncertainty—not just statistical noise, but two distinct types:

**Aleatoric uncertainty**: genuine heterogeneity across the population. Even in a post-reflection world, different people will value different things. This isn't ignorance to be eliminated; it's reality to be modeled.

**Epistemic uncertainty**: our uncertainty about what the distribution would be. We don't know with confidence what post-reflection humanity values. We have a distribution *over* distributions.

Both must be quantified.

Not "humanity will value X" but "P(humanity values X) = 0.3 with 90% CI [0.2, 0.4]"

This is the same uncertainty quantification theme from Chapter 11, applied to values instead of policy costs.

---

## The Empirical Test

What makes this a research program rather than armchair philosophy?

The key is historical validation. We have decades of survey data capturing how values actually changed. This provides ground truth for testing predictive models.

**The experiment I ran:**
1. Take 17 GSS variables spanning 1972–2022: attitudes on homosexuality, marijuana, gender roles, race, religion, and more
2. Give GPT-4o the historical time series through 2021 and ask for predictions of 2024 values
3. Compare those predictions to actual 2024 GSS data (released in late 2024)
4. Elicit full probability distributions—not just point estimates—using quantile prompting (10th, 25th, 50th, 75th, 90th percentiles)
5. Calibrate uncertainty using EMOS (Ensemble Model Output Statistics), the same technique meteorologists use for weather forecasts

**The results:**

| Metric | GPT-4o | Linear Extrapolation | Historical Mean |
|--------|--------|---------------------|-----------------|
| Mean Absolute Error | 4.8 pp | 7.2 pp | 10.6 pp |
| vs. Baseline | **2.2× better** | — | — |

LLMs genuinely outperformed naive baselines. They captured something about the structure of value change that simple trend extrapolation missed.

But calibration required work. Raw LLM confidence intervals were 21% too narrow—the model was overconfident. After EMOS calibration (multiplying the spread by 1.21×), the 80% prediction intervals achieved proper coverage.

The biggest lesson came from failure. Same-sex acceptance (HOMOSEX) had risen steadily from 11% in 1973 to 72% in 2022. Every model—LLM, linear, historical—predicted continued increase. The 2024 GSS showed 55%, a 17-point drop. The supposed "inevitable" trajectory reversed.

Was this a measurement artifact? A real backlash? It's too early to say. But it demonstrated something crucial: value change contains genuine surprises that no model—statistical or AI—can fully anticipate.

---

## The Historical Record

Consider what a value forecasting model can learn from five decades of GSS data:

| Value | 1973 | 1990 | 2010 | 2022 | 2024 |
|-------|------|------|------|------|------|
| Same-sex relations "not wrong" | 11% | 15% | 44% | 72% | 55%* |
| Marijuana legalization | 19% | 17% | 44% | 68% | 70% |
| Women working outside home | 68% | 78% | 80% | 88% | 83% |
| Confidence in science | 42% | 44% | 40% | 48% | 44% |

*The 2024 HOMOSEX drop is under active investigation—it may reflect survey methodology changes, real backlash, or sampling variation.

The patterns aren't random walks. They show consistent long-term structure:
- **Generational replacement matters**: younger cohorts hold different views that persist as they age
- **Exposure effects**: knowing gay people correlates with supporting their rights
- **Information cascades**: once a threshold is passed, change often accelerates
- **Moral arguments crystallize**: the articulation of principled positions shifts debate

But the 2024 data taught humility. The patterns are tendencies, not laws. Short-term reversals happen. What seemed like inevitable progress can stall or retreat.

## Long-Term Projections

Despite the 2024 surprise, I extended the forecasting exercise to longer horizons. If the 50-year trend matters more than year-to-year noise, what do calibrated forecasts suggest for 2030, 2050, and 2100?

**Same-sex acceptance (HOMOSEX):**

| Year | Median | 80% CI |
|------|--------|--------|
| 2030 | 62% | [49%, 75%] |
| 2050 | 72% | [57%, 87%] |
| 2100 | 80% | [69%, 91%] |

The model projects eventual convergence toward broad acceptance, but with wide uncertainty bands. The 2024 dip may be a temporary fluctuation in a longer trajectory—or the beginning of a sustained reversal. The confidence intervals capture both possibilities.

The key insight: even with short-term forecasting errors, long-term projections may be more reliable. The 50-year trajectory for HOMOSEX shows +44 percentage points despite year-to-year volatility. Generational replacement creates momentum that individual survey years cannot reverse.

---

## The Connection Back

Every tool in this book contributes to value forecasting:

**PolicyEngine** provides the consequence modeling. If we project that future humanity values environmental sustainability, what policies would they enact? What would those policies cost? PolicyEngine calculates.

**HiveSight** provides the heterogeneity infrastructure. Value forecasting doesn't ask "what would humanity think?" but "what would this representative sample of diverse personas think?" The same microdata-grounded diversity applies.

**Democrasim** provides the mechanism modeling. Given a distribution of values, how do democratic processes aggregate them? What policies result? Does the electoral outcome track the value distribution?

**Squigglepy** provides uncertainty quantification. Value forecasts aren't point estimates but probability distributions with confidence intervals.

**Cosilico** provides the integration layer. AI agents that can reason about policies, using deterministic tools, now have a target: not "what do users currently want?" but "what would reflective humanity value?"

The full stack:

```
Value distribution (forecast)
    |
    v
Democratic simulation (Democrasim)
    |
    v
Policy selection (election results)
    |
    v
Policy implementation (PolicyEngine)
    |
    v
Welfare outcomes (measured)
    |
    v
Feedback: do outcomes align with projected values?
```

---

## Why Not Just Ask People?

A reasonable objection: if you want to know what people value, why not just ask them?

Several reasons:

**Current preferences are noisy.** People are busy, distracted, misinformed. Their responses reflect momentary framing, media influence, tribal signaling. What they say they value and what they would value after careful reflection often differ.

**Values evolve.** Asking 1990 Americans about same-sex marriage wouldn't predict 2020 attitudes. Current surveys capture current states, not trajectories.

**Reflection takes time we don't have.** Ideally, every policy decision would follow extended democratic deliberation. In practice, decisions happen faster than reflection. Forecasting approximates the reflective outcome.

**Scale and cost.** Deep deliberative processes are expensive. Value forecasting offers an approximate, scalable complement.

The answer isn't "don't ask people"—it's "ask people, model the patterns, project the trajectories, and be transparent about uncertainty."

---

## The Philosophical Precedents

This isn't entirely new. Philosophers have grappled with the question of which values to take seriously.

**Idealized values** (various philosophers): What would a fully rational, fully informed person choose? The problem is this remains thought experiment; no one specifies how to compute the answer.

**Reflective equilibrium** (Rawls): The back-and-forth between principles and considered judgments until they cohere. Value forecasting operationalizes this as prediction: what would people conclude after that process?

**Axiological futurism** (Danaher): The systematic study of how values change. Value forecasting adds: "and can we predict it?"

The innovation isn't the question but the method: empirical validation, probabilistic framing, computational implementation.

### The Reflection Problem

But here's a crucial caveat: temporal change isn't the same as reflection.

That 79% supported same-sex marriage in 2021 versus 32% in 1986 shows *more time passed*, not necessarily *more careful reasoning*. The mechanisms driving value change—generational replacement, media exposure, information cascades, tribal signaling—are sociological, not purely epistemic.

Some value changes clearly involve improved reasoning: the abolition of slavery, the extension of suffrage. Others may reflect preference drift without moral progress. Still others—like the 2024 HOMOSEX reversal—might represent backlash to perceived overreach rather than either progress or regress.

The philosophers who've thought hardest about this offer partial guidance:

**Rawls** distinguished between reasonable and unreasonable comprehensive doctrines—not all value systems deserve equal weight in political deliberation. But operationalizing "reasonable" is difficult.

**Habermas** emphasized ideal speech conditions: undistorted communication, equal participation, no coercion. Temporal extrapolation doesn't guarantee these conditions obtained during the value change.

**Sen and Nussbaum** warned about "adaptive preferences"—values formed under oppression shouldn't guide alignment. A society that normalizes injustice may show stable preferences for injustice. Extrapolating those preferences forward would be perverse.

The honest answer: we don't have a fully satisfying account of when temporal change tracks moral reflection versus mere drift. The empirical validation helps—if temporal extrapolation predicts well, that's evidence for underlying structure—but it doesn't solve the deeper philosophical problem.

This uncertainty is one more reason for humility. Value forecasting provides evidence, not answers. It should inform democratic deliberation, not substitute for it.

---

## Objections and Responses

**"This is moral relativism."**

Not quite. Value forecasting predicts what values humanity would hold after reflection—not that all values are equally valid. It's empirical, not nihilistic. If the forecast is that post-reflection humanity would reject torture, that's not relativism; that's prediction.

**"Values depend on contingent factors. They're not predictable."**

Maybe. That's an empirical question. The historical validation step tests it. If value change is unpredictable, the model will fail to predict, and we'll know. Current evidence suggests partial predictability.

**"Who decides what counts as 'reflection'? Isn't this smuggling in values?"**

Fair critique. The experimental design makes assumptions: that GSS captures values, that temporal extrapolation is valid, that post-scarcity conditions matter. These are choices. They should be transparent, and different research programs could make different choices.

**"This could be used for manipulation."**

True. Knowing how values evolve could help those who want to accelerate or prevent certain changes. But the same is true of all social science. Understanding doesn't mandate manipulation.

---

## The Governance Question

If value forecasting works, it becomes a technology of power. Who controls it matters.

Consider the stakes. A government could use value forecasts to justify paternalistic policies: "We're implementing what you'll value in 20 years." A corporation could use them to anticipate and shape consumer preferences. An AI lab could use them to align systems to projected values that serve its interests rather than humanity's.

These aren't hypothetical risks. They're the predictable consequences of forecasting technology in a world of unequal power.

The governance framework must address:

**Who generates forecasts?** Academic researchers? Government agencies? Private companies? Each brings different incentives and accountability structures. Distributed generation with open methodology may be more trustworthy than centralized control.

**What conditioning assumptions are transparent?** A forecast conditioned on "post-scarcity with extended deliberation" differs from one conditioned on "persistent inequality with polarized media." The assumptions encode values themselves. They must be explicit and contestable.

**What role for democratic input?** Forecasts should inform democratic deliberation, not replace it. Citizens should be able to examine, critique, and reject forecast-based justifications. The forecast is evidence, not authority.

**What appeals processes exist?** When forecasts are contested—and they will be—how do disagreements resolve? Peer review, public comment, independent replication?

**How do forecasts interact with current feedback?** If value forecasts suggest future humanity will reject a practice that current humanity endorses, what weight does each get? This is the deepest question, and honest answers remain uncertain.

The HOMOSEX reversal illustrates the stakes. Had forecasters in 2020 projected continued acceptance and used that to justify policies, the 2024 data would have revealed overconfidence. The governance system must accommodate surprise, revision, and humility.

Value forecasting as academic research is one thing. Value forecasting as input to deployed AI systems is another. The institutional arrangements for the latter don't yet exist. Building them—with appropriate checks, transparency, and democratic oversight—is as important as the forecasting methodology itself.

---

## The Capstone

Throughout this book, simulation has served as a lens:

- Microsimulation reveals how policies affect households
- Democratic simulation reveals how knowledge affects elections
- Opinion simulation reveals what diverse populations think
- Value forecasting reveals where humanity's values might lead

Each layer builds on the last. Each uses the same core infrastructure: representative microdata, transparent methodology, uncertainty quantification.

And each asks a version of the same question: *What would happen if we could see more clearly?*

PolicyEngine asks: What would happen if households saw their true policy impacts?

HiveSight asks: What would people say if we could ask everyone?

Democrasim asks: What would elections produce if voters were informed?

Value forecasting asks: What would humanity choose if given time to reflect?

The simulation stack doesn't answer these questions definitively. It constructs scenarios, quantifies uncertainty, and makes the implications tractable.

---

## The Aspiration—and the Evidence

The deepest version of this vision:

AI systems aligned not to our current preferences—confused, biased, evolving—but to our projected post-reflection values. Not to what we happen to want this moment, but to what we would endorse after centuries of collective reasoning.

This is humility, not arrogance. It says: we don't know the right values with certainty. We know our current values are provisional. The best we can do is forecast, quantify uncertainty, and update as we learn.

The 2024 experiments provided both encouragement and caution.

**Encouragement**: LLMs captured value dynamics that simple baselines missed. A 2.2× improvement over extrapolation suggests genuine pattern recognition. Calibration techniques from meteorology (EMOS) successfully corrected overconfidence. The infrastructure works.

**Caution**: The HOMOSEX reversal humbled every forecaster. Value change contains irreducible surprises. Any system claiming to know humanity's future values with confidence is selling certainty it doesn't have.

The research program is no longer "just beginning"—the first experiments are complete. Historical validation showed predictive power. Long-term forecasts with calibrated uncertainty now exist. But the work has revealed how much remains unknown.

---

What would humanity want after reflection?

We can't know with certainty. But we might be able to forecast with calibrated uncertainty.

And that forecast—representing our best probabilistic guess about considered human values—might be the most responsible alignment target we can specify.

Not perfect. Not final. But grounded in evidence, transparent in method, and humble about uncertainty.

*Society in silico*: not a deterministic prediction machine, but a probabilistic reflection engine.

We simulate policies to understand their effects.
We simulate opinions to understand what people think.
We simulate elections to understand how preferences aggregate.
We simulate values to understand where we're heading.

The simulation doesn't replace human judgment. It informs it. It makes visible what would otherwise remain hidden. It creates the conditions for more thoughtful collective choice.

That's the aspiration. The work continues.


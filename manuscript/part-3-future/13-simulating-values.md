# Chapter 13: Simulating Values

We've built tools to simulate households, policies, voters, and opinions. But the deepest question isn't "what do people want today?"

It's: *What would they want after reflection?*

This chapter ventures into territory where simulation meets philosophy, where forecasting meets ethics, where the practical tools we've built connect to the most consequential question of our time: How do we align increasingly powerful AI systems with human values?

The answer may not be what you expect.

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

This is the same uncertainty quantification theme from Chapter 10, applied to values instead of policy costs.

---

## The Empirical Test

What makes this a research program rather than armchair philosophy?

The key is historical validation. We have decades of survey data capturing how values actually changed. This provides ground truth for testing predictive models.

**The experiment:**
1. Train a language model on General Social Survey data through 2000 (and web text through that date—no RLHF to avoid contaminating with post-2000 moral attitudes)
2. Ask: "What percentage of Americans will support [same-sex marriage / marijuana legalization / interracial marriage / etc.] in 2010? 2020?"
3. Compare predictions to actual survey data
4. Calculate calibration: did the model's probabilities correspond to actual frequencies?

If this works—if AI can predict moral change trajectories better than simple extrapolation—it suggests the model has learned something genuine about how values evolve.

If it doesn't work, we learn that value evolution is less predictable than hoped. That's also useful.

---

## The Historical Record

Consider what a value forecasting model could learn from:

| Value | 1970 | 1990 | 2010 | 2020 |
|-------|------|------|------|------|
| Interracial marriage approval | 36% | 64% | 84% | 94% |
| Women working outside home | 40% | 58% | 75% | 82% |
| Same-sex marriage support | — | 11% | 40% | 67% |
| Marijuana legalization | 12% | 16% | 46% | 68% |

These aren't random walks. They show consistent patterns:
- Generational replacement matters: younger cohorts hold different views
- Exposure effects: knowing gay people correlates with supporting their rights
- Information cascades: once a threshold is passed, change accelerates
- Moral arguments crystallize: the articulation of principled positions shifts debate

A model trained on earlier data could potentially learn these patterns and project them forward.

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
    ↓
Democratic simulation (Democrasim)
    ↓
Policy selection (election results)
    ↓
Policy implementation (PolicyEngine)
    ↓
Welfare outcomes (measured)
    ↓
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

## The Aspiration

The deepest version of this vision:

AI systems aligned not to our current preferences—confused, biased, evolving—but to our projected post-reflection values. Not to what we happen to want this moment, but to what we would endorse after centuries of collective reasoning.

This is humility, not arrogance. It says: we don't know the right values with certainty. We know our current values are provisional. The best we can do is forecast, quantify uncertainty, and update as we learn.

It's also testable. Historical validation keeps the project honest. If AI can't predict moral change from 2000 to 2020, we shouldn't trust its projections to 2100.

The research program is just beginning. The infrastructure—microsimulation, silicon sampling, uncertainty quantification—is falling into place. The experiments await.

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


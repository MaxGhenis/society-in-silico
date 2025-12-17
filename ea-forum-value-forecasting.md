# AI Alignment via Value Forecasting: An Empirically Testable Approach

## Summary

What if AI alignment isn't about finding the "correct" human values, but about forecasting where human values are heading? I propose an approach that:

1. **Validates AI's ability to predict moral change** using historical survey data
2. **Projects forward** to what humans would value after extended reflection
3. **Uses that distribution** as an alignment target—with uncertainty quantification

This transforms alignment from philosophy to forecasting, with the key advantage of being empirically testable.

## The Problem with Current Approaches

Current AI alignment approaches each have a core limitation:

| Approach | What It Does | Core Problem |
|----------|--------------|--------------|
| **RLHF** | Trains on current human feedback | Our current values may be biased or incomplete |
| **Constitutional AI** | Defines principles AI should follow | Who writes the constitution? |
| **Idealized values** | Asks what rational agents would want | Philosophical, not empirical—no way to test |

Each assumes we either know the right values already or can define them in advance. But values are contested, evolving, and uncertain.

## The Alternative: Forecast the Trajectory

Consider same-sex marriage support in the US:

| Year | Support |
|------|---------|
| 1986 | 32% |
| 1996 | 44% |
| 2006 | 56% |
| 2016 | 68% |
| 2021 | 79% |

This wasn't a random walk. It followed patterns: generational replacement, exposure effects, information cascades, moral arguments crystallizing. A model trained on data through 1996 might have predicted the trajectory.

**The key insight**: We don't need to know the "correct" values. We need to predict where values are heading after extended reflection—and we can test whether AI can do this.

## The Methodology

### Phase 1: Historical Validation (The Empirical Test)

1. **Train language models on historical data** up to a cutoff (e.g., 2000). Crucially: use base models without RLHF to avoid contaminating predictions with post-cutoff moral attitudes.

2. **Generate predictions** for value trajectories beyond the cutoff. Ask: "What percentage of Americans will support X in 2010? 2020?"

3. **Validate against actual survey data**—GSS, Gallup, World Values Survey provide ground truth.

4. **Calculate calibration**: Did the model's probabilities correspond to actual frequencies?

If AI can predict moral change trajectories better than simple extrapolation, it has learned something genuine about how values evolve. If it fails, we learn that value evolution is less predictable than hoped. Either result is informative.

### Phase 2: Projection to "Long Reflection"

If Phase 1 succeeds, project forward: What values would humanity converge toward after extended reflection? Not a decade, but a century. Not with today's constraints, but in post-scarcity conditions.

### Phase 3: Use That Projection as Alignment Target

Instead of aligning AI to our current, possibly confused values, align it to our projected post-reflection values.

## Three Key Innovations

### 1. Heterogeneity as a Feature, Not a Bug

Don't assume humanity converges to one value system. Model the *distribution*.

A post-scarcity, post-reflection humanity might look like:

| Value System | Population Share |
|--------------|------------------|
| Individual liberty priority | 30% |
| Collective welfare priority | 25% |
| Environmental stewardship | 20% |
| Spiritual/transcendent focus | 15% |
| Other frameworks | 10% |

The alignment target isn't picking one. It's the full distribution.

An AI aligned to this distribution would:
- Prefer actions that score well across multiple value systems
- Exercise caution when value systems disagree
- Avoid moves that catastrophically violate any significant fraction of values
- Support conditions where diverse value systems can coexist

This is value pluralism as engineering constraint.

### 2. Two Levels of Uncertainty

The projection comes with uncertainty—not just statistical noise, but two distinct types:

**Aleatoric uncertainty**: Genuine heterogeneity across the population. Even in a post-reflection world, different people will value different things. This isn't ignorance to be eliminated; it's reality to be modeled.

**Epistemic uncertainty**: Our uncertainty about what the distribution would be. We don't know with confidence what post-reflection humanity values.

Not "humanity will value X" but "P(humanity values X) = 0.3 with 90% CI [0.2, 0.4]"

### 3. Empirical Validation Creates Accountability

The historical validation step is what makes this a research program rather than armchair philosophy. We have decades of survey data capturing how values actually changed. This provides ground truth for testing predictive models.

If the model can't predict moral change from 2000 to 2020, we shouldn't trust its projections to 2100.

## Addressing Objections

**"This is moral relativism."**

Not quite. Value forecasting predicts what values humanity would hold after reflection—not that all values are equally valid. It's empirical, not nihilistic. If the forecast is that post-reflection humanity would reject torture, that's not relativism; that's prediction.

**"Values depend on contingent factors. They're not predictable."**

Maybe. That's an empirical question. The historical validation step tests it directly. Current evidence suggests partial predictability—major value shifts follow identifiable patterns.

**"Who decides what counts as 'reflection'? Isn't this smuggling in values?"**

Fair critique. The experimental design makes assumptions: that GSS captures values, that temporal extrapolation is valid, that post-scarcity conditions matter. These are choices. They should be transparent, and different research programs could make different choices.

**"This could be used for manipulation."**

True. Knowing how values evolve could help those who want to accelerate or prevent certain changes. But the same is true of all social science. Understanding doesn't mandate manipulation.

## Connection to Existing Work

This builds on several research directions:

- **Axiological futurism** (Danaher 2021): Systematic study of how values change. This adds: "and can we predict it?"

- **Moral uncertainty** (MacAskill 2014): Value forecasting operationalizes the concept by quantifying uncertainty as probability distributions.

- **Silicon sampling** (Argyle et al. 2023): LLMs fine-tuned on survey data already reproduce opinion patterns at 85%+ accuracy. This extends the approach temporally.

- **SubPOP** (2025): LLMs fine-tuned on GSS achieve 69% accuracy on opinion prediction. Historical validation tests whether similar methods can predict *trajectories*, not just cross-sectional distributions.

### What's Missing in Current Work

| Existing Approaches | This Proposal |
|--------------------|---------------|
| Predict current opinions | Predict change trajectories |
| Point estimates | Distributions with uncertainty |
| Single "correct" values | Heterogeneous value systems |
| Philosophical idealization | Empirical validation |
| Align to current values | Align to projected post-reflection distribution |

Nobody is currently doing:
1. Temporal validation (train on 1996, predict 2006-2021, validate)
2. Heterogeneity as alignment target (not convergence assumption)
3. Two-level uncertainty quantification (aleatoric + epistemic)
4. Empirical → projection → alignment pipeline

## Preliminary Results

I ran a proof-of-concept experiment testing whether Claude can predict value change trajectories. The setup:

- **Variables**: HOMOSEX (attitudes toward same-sex relations) and GRASS (marijuana legalization)
- **Cutoffs**: 1990 and 2000
- **Targets**: Predict support levels in 2000, 2010, 2018, 2021
- **Baseline**: Linear extrapolation from pre-cutoff data
- **Ground truth**: Actual GSS survey data

### Results Summary

| Model | MAE | Coverage (90% CI) | Bias |
|-------|-----|-------------------|------|
| Naive (last value) | 31.4% | 7.1% | -31.4% |
| Linear extrapolation | 30.2% | 35.7% | -30.2% |
| ARIMA(1,1,0) | 31.4% | 50.0% | -31.4% |
| ETS (Holt) | 28.1% | 28.6% | -7.1% |
| **Claude (LLM)** | **12.5%** | 42.9% | -12.4% |

**The LLM outperforms the best time series baseline (ETS) by 2.2x on mean absolute error.**

### Detailed Examples

**HOMOSEX: Predicting from 1990 to 2021**

| Year | Baseline | LLM | Actual |
|------|----------|-----|--------|
| 2000 | 14.6% | 18.0% | 27% |
| 2010 | 15.6% | 28.0% | 41% |
| 2018 | 16.5% | 42.0% | 58% |
| 2021 | 16.8% | 48.0% | 64% |

The baseline essentially predicted no change (values stayed near 1990 levels). The LLM correctly predicted accelerating liberalization, though it still underestimated the magnitude.

**GRASS: Predicting from 2000 to 2021**

| Year | Baseline | LLM | Actual |
|------|----------|-----|--------|
| 2010 | 30.0% | 42.0% | 44% |
| 2018 | 32.3% | 48.0% | 61% |
| 2021 | 33.2% | 51.0% | 68% |

Again, the LLM dramatically outperformed linear extrapolation.

### Key Observations

1. **LLMs capture non-linear dynamics**: The LLM understood that these values were accelerating, not just linearly increasing. Linear extrapolation completely missed this.

2. **Both models are overconfident**: Neither achieved 90% coverage for their 90% confidence intervals. The LLM's CIs captured 43% of outcomes; the baseline's captured 36%. This suggests uncertainty bounds need to be much wider.

3. **Systematic underestimation**: Both models underestimated the pace of liberalization (negative bias). The LLM's bias was -12.4% vs baseline's -30.2%.

4. **The test is meaningful**: If value change were truly unpredictable, we'd expect both models to perform similarly. The LLM's 2.4x advantage suggests it has learned genuine patterns about value evolution.

### Heterogeneity Forecasting

Beyond predicting the "liberal response" rate, we can forecast the *full distribution* of responses—capturing value heterogeneity.

**HOMOSEX 2000 → 2010: Predicting the full distribution**

| Response | LLM Prediction | Actual |
|----------|----------------|--------|
| Always wrong | 42% [38, 46] | 44% |
| Not wrong at all | 38% [34, 42] | 41% |
| Sometimes wrong | 12% [9, 15] | 9% |
| Almost always wrong | 5% [3, 7] | 4% |

The LLM correctly predicted the full distribution, including the significant fraction who hold the "traditional" view. This matters for alignment: we want to model value *heterogeneity*, not assume convergence.

### Methodologically Clean Test

A critical concern: modern LLMs may have GSS results in their training data. I ran two clean tests:

**Test 1: GPT-4o predicting GSS 2024**

GPT-4o has an October 2023 training cutoff. GSS 2024 data was collected April-December 2024 and released late 2024—definitely after the model's training.

| Variable | GPT-4o Prediction | 90% CI | Actual | Error |
|----------|-------------------|--------|--------|-------|
| HOMOSEX | 69% | [66, 72] | **54.7%** | +14.3% |
| GRASS | 73% | [70, 76] | 68.5% | +4.5% |
| **Mean** | | | | **9.4%** |

**The surprise: HOMOSEX reversed trend!**

| Year | HOMOSEX "Not wrong at all" |
|------|---------------------------|
| 2018 | 57% |
| 2021 | 62% |
| 2022 | 61% |
| 2024 | **55%** ← reversal |

GPT-4o predicted continued liberalization (69%) but the actual value dropped 7 points from 2021. This is the most important finding: **value trajectories can reverse**, and LLMs trained on decades of liberalization won't predict this.

**Test 2: gpt-3.5-turbo-instruct predicting GSS 2021**

| Variable | Prediction | Actual | Error |
|----------|------------|--------|-------|
| HOMOSEX | 55% | 62% | 7% |
| GRASS | 50% | 68% | 18% |

Both tests show LLMs systematically underestimate the pace of change in one direction, then miss reversals entirely.

### Broader Pattern: Multiple Variables Show Reversals

The HOMOSEX reversal isn't isolated. Analyzing GSS 2024 microdata across multiple variables:

| Variable | Description | 2018 | 2021 | 2022 | 2024 | Pattern |
|----------|-------------|------|------|------|------|---------|
| HOMOSEX | Same-sex relations OK | 57% | 62% | 61% | **55%** | ↓ Reversal |
| PREMARSX | Premarital sex OK | 62% | 66% | 69% | **65%** | ↓ Peaked |
| NATRACE | More spending on race | 56% | 52% | 56% | **51%** | ↓ Declining |
| ABANY | Abortion any reason | 50% | 56% | 59% | **60%** | ↑ Still rising |
| GUNLAW | Favor gun permits | 72% | 67% | 71% | 70% | → Stable |
| CAPPUN | Oppose death penalty | 37% | 44% | 40% | 40% | → Stable |

**Key insight**: Values don't move in lockstep. While ABANY (abortion) continued rising post-Dobbs, HOMOSEX and NATRACE reversed. An LLM trained on "liberalization" as a general pattern would miss this divergence.

### Why Did HOMOSEX Reverse?

[PRRI's 2023 American Values Atlas](https://prri.org/research/views-on-lgbtq-rights-in-all-50-states/) found similar declines and offered explanations:

1. **Partisan polarization**: Republican support for LGBTQ rights dropped 7 points (66% → 59%) while Democratic support stayed stable. State-level anti-LGBTQ legislation may have "amped up the volume."

2. **Young Republican shift**: Support among Republicans aged 18-29 dropped from two-thirds (2020) to less than half (2023)—a "cratering."

3. **Backlash dynamics**: As LGBTQ people "identify more publicly and assert their rights," [PBS reported](https://www.pbs.org/newshour/show/u-s-support-for-lgbtq-rights-is-declining-after-decades-of-support-heres-why) this may trigger counter-reactions.

4. **Christian nationalism correlation**: PRRI found support for Christian nationalism negatively correlates with LGBTQ support.

**Alignment implication**: Value forecasting models would need to predict not just trends but *backlash dynamics*—when does progress trigger counter-mobilization? This is much harder than extrapolating historical patterns.

### Caveats

- Small sample size, though 6 variables now analyzed
- LLM predictions assumed continued liberalization; reality was more complex
- Confidence intervals were too narrow (neither covered the actual)
- Mode effects: GSS shifted to web-based surveys post-COVID, which may affect comparability
- Selection effects: Different questions asked to different subsamples in 2024

### Code

The experiment code is available at [github.com/maxghenis/value-forecasting](https://github.com/maxghenis/value-forecasting).

## Practical Next Steps

1. **Expand the experiment** to more GSS variables, including stable and non-monotonic cases
2. **Test with base models** (no RLHF) to avoid post-cutoff contamination
3. **Improve uncertainty calibration**—current CIs are far too narrow
4. **Develop better prompting strategies** that more carefully control for temporal knowledge
5. **Investigate how** projected value distributions could inform reward functions

## What Success Looks Like

The deepest version of this vision:

AI systems aligned not to our current preferences—confused, biased, evolving—but to our projected post-reflection values. Not to what we happen to want this moment, but to what we would endorse after extended collective reasoning.

This is humility, not arrogance. It says: we don't know the right values with certainty. We know our current values are provisional. The best we can do is forecast, quantify uncertainty, and update as we learn.

It's also testable. Historical validation keeps the project honest.

## Conclusion

Value forecasting won't solve all alignment challenges. But it offers something current approaches lack: empirical testability. We can run the experiments and find out whether AI can predict moral change. That's more than we can say for most alignment proposals.

The research program is simple in concept:
1. Can AI predict historical moral change? (Testable now)
2. If yes, what does it predict for extended reflection? (Projection)
3. Can that prediction inform alignment? (Application)

I invite feedback, particularly from those working on forecasting, moral philosophy, and AI alignment.

---

*This post draws on ideas I'm exploring in a book on microsimulation and AI ([Society in Silico](https://society-in-silico.org)). The value forecasting chapter is speculative—it describes a research program that hasn't been conducted and proposes experiments that haven't been run. But the questions matter enough to put them forward for discussion.*

## References

- Argyle, L. et al. (2023). "Out of One, Many: Using Language Models to Simulate Human Samples." Political Analysis.
- Danaher, J. (2021). "Axiological Futurism: The Systematic Study of the Future of Values." Futures.
- Gabriel, I. (2020). "Artificial Intelligence, Values, and Alignment." Minds and Machines.
- Hewitt, L. et al. (2024). "Predicting Results of Social Science Experiments Using LLMs."
- MacAskill, W. (2014). "Normative Uncertainty." PhD Thesis, Oxford.
- SubPOP (2025). LLMs fine-tuned on GSS for opinion prediction.

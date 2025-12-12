# AI Alignment as Value Forecasting

## The Novel Thesis

Align AI not to current human values, nor to a single "correct" idealized value system, but to:

**The probability distribution over heterogeneous values that would emerge from extended reflection, with uncertainty quantification, validated empirically.**

This is distinct from existing approaches:

| Approach | Target | Problem |
|----------|--------|---------|
| Current values | What humans want now | Values may be wrong/incomplete |
| Predicted values (Danaher) | What humans *will* want | Descriptive, not normative |
| Idealized values (MacAskill) | What we *would* want after reflection | Philosophical, not empirical |
| **This proposal** | Distribution over post-reflection values, with uncertainty | Empirically testable |

## The Key Innovations

### 1. Heterogeneity as a Feature

Don't assume humanity converges to one value system. Model the *distribution* of values across a reflective population.

A post-scarcity humanity might include:
- 30% prioritizing individual liberty
- 25% prioritizing collective welfare
- 20% prioritizing environmental stewardship
- 15% prioritizing spiritual/transcendent values
- 10% other frameworks

The alignment target isn't picking one—it's the full distribution.

### 2. Uncertainty is Quantified

Not "they'll value X" but "P(X) = 0.3 with 90% CI [0.2, 0.4]"

Two levels of uncertainty:
- **Aleatoric**: Genuine heterogeneity in values across the population
- **Epistemic**: Our uncertainty about what that distribution would be

Both must be modeled.

### 3. Empirically Grounded

Historical validation creates accountability:
- Train on pre-cutoff data
- Predict post-cutoff value trajectories
- Validate against actual GSS/Gallup/WVS data
- Only trust projections to "long reflection" if historical validation succeeds

### 4. Alignment-Relevant

This distribution becomes the reward signal:
- Actions that score well across the distribution are preferred
- High-uncertainty regions warrant caution
- Heterogeneity implies tolerance for multiple value systems

## The Methodology

### Phase 1: Historical Validation

1. **Train base LLMs on historical data** up to a temporal cutoff (no RLHF to avoid contaminating with contemporary moral attitudes)
2. **Generate value forecasts** beyond the training cutoff
3. **Validate against empirical data**: GSS, Gallup, World Values Survey
4. **Test accuracy**: Did the model predict the trajectory of moral change?

Example test case - Gallup data on same-sex relationships:

| Year | Support |
|------|---------|
| 1986 | 32% |
| 1996 | 44% |
| 2006 | 56% |
| 2016 | 68% |
| 2021 | 79% |

A model trained on data through 1996 could be asked to predict 2006, 2016, 2021 values.

### Phase 2: Long Reflection Projection

If Phase 1 succeeds, project forward:
- What values would emerge after 100 years of post-scarcity reflection?
- What is the distribution across the population?
- What is our uncertainty about that distribution?

### Phase 3: Alignment Integration

Use the projected distribution as the alignment target:
- Reward functions that maximize expected value across the distribution
- Penalty for actions that score poorly under high-probability value systems
- Explicit handling of uncertainty (risk-averse under epistemic uncertainty)

## Connection to the Portfolio

Every project contributes a component:

| Project | Contribution |
|---------|-------------|
| **HiveSight** | Population heterogeneity modeling - already simulates diverse opinions |
| **Squigglepy** | Uncertainty quantification infrastructure |
| **Farness** | Epistemics framework - forecasts with CIs, calibration tracking |
| **LLM-ETI** | Methodology for using LLMs as behavioral subjects |
| **Democrasim** | Values → votes → policies simulation |
| **PolicyEngine** | What policies does a society with value distribution X enact? |
| **Cosilico** | AI agents reasoning about those policies |
| **Microdata** | The structured human variation that grounds simulations |

## The Full Integration

```
Phase 1: Validation
─────────────────────────────────────────────────────────────
Historical Survey Data (GSS 1972-2021, Gallup, WVS)
    ↓
Train Base LLM on pre-cutoff data (e.g., through 1996)
    ↓
Generate value forecasts: P(support | demographics, year=2006)
    ↓
Validate against actual post-cutoff data
    ↓
Calibration score: Can the model predict moral change?

Phase 2: Projection
─────────────────────────────────────────────────────────────
If validated → project to "long reflection"
    ↓
Model: What values would emerge after extended post-scarcity reflection?
    ↓
Output: Distribution over value systems + uncertainty bands
    ↓
HiveSight-style: heterogeneous population, not single answer

Phase 3: Alignment
─────────────────────────────────────────────────────────────
Projected value distribution → alignment target
    ↓
Reward = E[value_score across distribution]
    ↓
Penalty for high variance across plausible value systems
    ↓
Risk-averse under epistemic uncertainty

Phase 4: Policy Connection
─────────────────────────────────────────────────────────────
Value distribution → Democrasim: what do these voters elect?
    ↓
Elected policies → PolicyEngine: what are the outcomes?
    ↓
Feedback: do outcomes align with values?
    ↓
Cosilico: AI agents reasoning about this full loop
```

## Key Insights

### From MacAskill on Moral Uncertainty

> "The fact that we very often are just unsure about what we ought, morally speaking, to do... it's also plausible that we ought to be unsure about what we ought morally to do."

Value forecasting quantifies this uncertainty as probability distributions.

### From Dafoe on Cooperative AI

> "If we want things to go well, we ideally have two pieces: systems that are safe... and we're able to deploy AI systems in a way that's jointly peaceful and productive."

Value forecasting could identify which value systems best facilitate cooperation.

### The Uncertainty Quantification Theme

This addresses the "uncertainty gap in microsimulation" at the meta-level:
- PolicyEngine lacks uncertainty bands on policy costs
- Value forecasting lacks uncertainty bands on moral predictions
- Both need the same infrastructure: distributions, not point estimates

## Applications

1. **Long-term alignment**: Design systems that accommodate predicted value changes
2. **Moral uncertainty handling**: Represent uncertainty as probability distributions
3. **Value robustness identification**: Which values are stable across forecasts?
4. **Decision-making under uncertainty**: Implement MacAskill's "moral parliament" computationally
5. **Value pluralism modeling**: Predict population distributions, not just central tendencies

## Challenges

1. **Ground truth contestable**: What counts as "correct" value forecasting is itself value-laden
2. **Data limitations**: Historical records may lack sufficient detail
3. **Selection bias**: Which transitions we test reflects current values
4. **Determinism questions**: Are values predictable or influenced by unpredictable factors?

## Why This is "The Most Important Direction"

The other projects build components:
- Microsimulation infrastructure (PolicyEngine)
- Opinion simulation (HiveSight)
- Forecasting epistemics (Farness)
- Uncertainty quantification (Squigglepy)
- Democratic process modeling (Democrasim)

Value forecasting **integrates** them into an alignment research program:
- Use historical data to validate AI's ability to reason about values
- If validated, project to "reflectively stable" values
- Use those values to inform both AI alignment AND policy design
- Connect to democratic simulation: what does a well-informed electorate choose?

## For "Society in Silico"

This could be the climax of Part III:

> "We've built tools to simulate households, policies, voters, opinions. But the deepest question isn't 'what do people want today?' It's 'what would they want after reflection?' And that question—whether AI can help us answer it—may be the most important forecasting challenge of our time."

## Source

Unpublished EA Forum draft: `/Users/maxghenis/Downloads/ea-forum-post.md`
(December 2024)

## Competitive Landscape (as of Dec 2024)

### What Exists

**Theoretical foundations:**
- Danaher (2021): "Axiological Futurism" - systematic study of future values
- MacAskill (2014): "Normative Uncertainty" - decision-making under moral uncertainty
- Gabriel (2020): "AI, Values, and Alignment" - fair principles for alignment

**LLM + Survey prediction:**
- Hewitt et al. (2024): GPT-4 predicts experimental treatment effects (r=0.85)
- SubPOP (2025): LLMs fine-tuned on GSS achieve 69% accuracy
- Argyle et al. (2023): Silicon sampling reproduces voting patterns at 85%+

**Alignment approaches:**
- RLHF: Align to current human feedback
- Constitutional AI: Align to stated principles
- Debate: Let AI systems argue, humans judge

### What's Missing (The Gap)

| Existing | This Proposal |
|----------|---------------|
| Predict *current* opinions | Predict *change trajectories* |
| Point estimates | Distributions with uncertainty |
| Single "correct" values | Heterogeneous value systems |
| Philosophical idealization | Empirical validation |
| Alignment to current values | Alignment to projected post-reflection distribution |

**Nobody is doing:**
1. Temporal validation (train on 1996, predict 2006-2021, validate)
2. Heterogeneity as alignment target (not convergence assumption)
3. Two-level uncertainty (aleatoric + epistemic)
4. Empirical → projection → alignment pipeline

### Why the Gap Exists

- Alignment research focuses on technical safety, not value content
- Axiological futurism is philosophical, not computational
- Survey prediction research aims at augmentation, not alignment
- MacAskill's idealization is normative, not empirical

This proposal bridges: computational methods + normative framework + empirical validation

## Related Work

- MacAskill, W. "Normative Uncertainty" (2014)
- Gabriel, I. "Artificial Intelligence, Values, and Alignment" (2020)
- Danaher, J. "Axiological Futurism" (2021)
- Hewitt et al. "Predicting Results of Social Science Experiments Using LLMs" (2024)
- Dafoe, A. on cooperative AI (80,000 Hours, 2023)
- Lundgren & Kudlek "Ten Arguments Against Longtermism" (2024) - critiques

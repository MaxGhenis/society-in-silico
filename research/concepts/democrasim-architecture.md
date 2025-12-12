# Democrasim: Simulating Democratic Feedback Loops

## Overview

Democrasim is a Python package for simulating how voter interventions affect election outcomes and ultimately policy metrics. It models the full chain:

**Interventions → Voter Behavior → Elections → Policy → Welfare Outcomes**

Repository: `/Users/maxghenis/PolicyEngine/democrasim/`

## Core Components

### Voters

Each voter has:
- **Weighted preferences** across policy dimensions (economic, social, environmental)
- **Accuracy**: How well they perceive true policy values (higher = less noise)
- **Biases**: Systematic distortions in perception
- **Turnout probability**: Likelihood of voting

Key insight: Voters don't perceive policy "truth" directly. They perceive through noise and bias:
```python
perceived = true_value + noise + bias
# where noise_std = 1.0 / accuracy
```

### Interventions

Can modify voter behavior:
- **accuracy_multipliers**: Civics education, better information access
- **weight_multipliers**: Changing what voters care about
- **turnout_boost**: Get-out-the-vote efforts

Example:
```python
civics_education = Intervention(
    name="civics_education",
    effect={
        "accuracy_multipliers": {"economic": 1.2, "environmental": 1.1},
        "turnout_boost": 0.05
    }
)
```

### Elections

Simple plurality voting:
1. Each voter who turns out evaluates all candidates
2. Utility = sum of (weight × perceived_value) across dimensions
3. Vote goes to highest-utility candidate
4. Most votes wins

### Outcomes

Maps election winners to societal metrics:
- QALYs
- Inequality indices
- Economic growth
- Other welfare measures

## Connection to PolicyEngine

**The key insight:** Democrasim's `accuracy` parameter captures exactly what open microsimulation tools provide.

| Without PolicyEngine | With PolicyEngine |
|---------------------|-------------------|
| Voters perceive policy through noise + bias | Voters can calculate actual impact |
| Low accuracy → bad signal → poor democratic alignment | High accuracy → clear signal → better alignment |
| Interventions must "educate" abstractly | Interventions can point to calculable facts |

## Implications for "Society in Silico"

### 1. The Democratic Case for Open Tools

If democrasim shows that higher voter accuracy leads to better welfare outcomes, then tools that increase accuracy (like PolicyEngine) have democratic value beyond individual utility.

The argument becomes:
> "Open microsimulation isn't just useful for individuals calculating their taxes. It's infrastructure for informed democratic participation."

### 2. Measuring the Value of Transparency

Democrasim could quantify:
- How much does voter accuracy improve outcomes?
- What's the welfare difference between informed and uninformed electorates?
- How does open tool adoption correlate with policy alignment?

### 3. The Full Stack

Three layers of simulation for policy analysis:
1. **Microsimulation** (PolicyEngine): How policies affect households
2. **Democratic simulation** (Democrasim): How voter knowledge affects elections
3. **Agent simulation** (Cosilico?): How AI agents use these tools for reasoning

### 4. Closing the Loop

Future research direction: Connect democrasim to PolicyEngine so that:
1. Candidates have policy platforms (e.g., "expand CTC by $500")
2. PolicyEngine calculates actual impacts on voter households
3. Voters with higher "accuracy" perceive impacts closer to truth
4. Election determines winner
5. PolicyEngine calculates welfare outcomes under winning policy

## Research Questions

- What level of voter accuracy is needed for democratic outcomes to track welfare?
- Does uncertainty/noise in perception systematically benefit certain policy types?
- How do different intervention types compare (education vs turnout vs weight-shifting)?
- What's the interaction between voter accuracy and candidate policy positioning?

## Technical Notes

- Uses squigglepy for probabilistic modeling
- Monte Carlo simulation across voter populations
- Modular: can swap election systems, outcome functions, intervention types

## For the Book

This connects to Part III (Future) themes:
- Democracy requires shared models to reason against
- AI agents as voters (future scenario?)
- The value of transparent policy infrastructure

Potential chapter angle: "Democracy's Accuracy Problem"
- Why do democratic outcomes often diverge from welfare optimization?
- The role of information asymmetry and perception noise
- How transparent tools could improve democratic signal quality

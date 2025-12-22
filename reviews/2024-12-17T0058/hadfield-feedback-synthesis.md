# Synthesis: Hadfield Referee Report on Value Forecasting

**Source**: `reviews/hadfield-referee-report.md`
**Recommendation**: Major Revision
**Reviewer expertise**: AI governance, normative systems, cooperative AI

## Key Strengths Identified

1. **Empirical grounding** in a field dominated by philosophy - the historical validation methodology is concrete and falsifiable
2. **Heterogeneity treatment** - recognizing alignment targets should be distributions, not points
3. **Two-level uncertainty** - distinguishing aleatoric (genuine pluralism) from epistemic uncertainty
4. **Backlash dynamics** - not downplaying the HOMOSEX reversal result

## Major Concerns to Address

### 1. Democratic Legitimacy Gap
**Issue**: Who decides what counts as "adequate reflection"? What conditions define projection scenarios?
**Action for Ch 13**: Add governance section addressing:
- Who controls value forecasting systems?
- What transparency requirements?
- What appeals processes when forecasts contested?
- Democratic input into conditioning assumptions

### 2. Temporal Change ≠ Moral Progress
**Issue**: The validation conflates temporal change with reflection. 79% support in 2021 vs 32% in 1986 shows *more time*, not necessarily *more reflection*.
**Action for Ch 13**: Engage with:
- Reflective equilibrium literature (Rawls, Daniels)
- Idealized deliberation theories (Habermas, Cohen)
- "Adaptive preferences" work (Nussbaum, Elster)
- Why temporal extrapolation might approximate reflection

### 3. Training Data Contamination
**Issue**: Main results use Claude on data potentially in training set. GPT-4o 2024 test is clean, but core 2.2x claim needs base model validation.
**Action**: Run core experiment with base models (no RLHF), ideally with training cutoffs preceding test data.

### 4. Governance Implications Underdeveloped
**Issue**: Value forecasting as research vs. as input to deployed AI systems requires different treatment.
**Action for Ch 13**: Add institutional proposal:
- How forecasts generated, validated, updated?
- Role of ongoing human feedback vs forecasted future feedback?
- Integration with RLHF - override? weight equally? aspirational target?

### 5. Normative Pluralism Too Shallow
**Issue**: Analysis is quantitative (different groups hold different values) but not deeply normative (incommensurable value systems).
**Action for Ch 13**: Engage with:
- Rawlsian "reasonable pluralism"
- Normative systems in law literature
- When "prefer actions that score well across systems" breaks down

## Specific Improvements

1. Foreground the negative result (HOMOSEX reversal) - value forecasting is possible but harder than trend extrapolation
2. Develop formal model of when value progress triggers counter-mobilization (social movement theory, backlash politics, norm cascades)
3. Clarify alignment pathway: Would forecasts override RLHF? Weight equally? Serve as long-term targets?
4. Add sensitivity analysis for long reflection forecasts given 2024 reversal

## Citations to Add

- Dafoe et al. 2020 (cooperative AI)
- Hadfield et al. 2021 (cooperative AI)
- Rawls, Daniels (reflective equilibrium)
- Habermas, Cohen (idealized deliberation)
- Nussbaum, Elster (adaptive preferences)

## Notable Quote

> "The paper's ultimate contribution may not be 'here's how to align AI' but rather 'here's an empirical research program that reveals the limits of value forecasting.' Either way, the field needs this work."

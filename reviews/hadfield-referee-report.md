# Referee Report: "Can Language Models Forecast Human Value Evolution? Evidence from the General Social Survey"

**Reviewer**: Gillian Hadfield (Johns Hopkins University / University of Toronto)
**Journal**: Journal of Artificial Intelligence Research
**Date**: December 16, 2025

## Summary

This paper proposes a novel empirical approach to AI alignment by treating it partly as a forecasting problem. Rather than assuming we know correct values or can define them philosophically, the authors test whether large language models can predict trajectories of value change using historical survey data (GSS 1972-2024). The central finding is that LLMs outperform time series baselines by 2.2x on mean absolute error when predicting historical value shifts. However, a methodologically clean test reveals a critical limitation: GPT-4o predicted 69% acceptance of same-sex relationships for 2024, but the actual rate was 55%—a reversal of decades-long liberalization. The paper argues that value forecasting, with proper uncertainty quantification and attention to heterogeneity across populations, could complement current RLHF approaches to alignment.

## Strengths

**1. Empirical grounding in a field dominated by philosophy.** The AI alignment literature suffers from an excess of thought experiments and a shortage of testable propositions. This paper's historical validation methodology—train on data through year X, predict to year Y, validate against actual surveys—is refreshingly concrete. The fact that the clean test (GSS 2024) contradicts the model's predictions is not a weakness but a feature: it demonstrates the approach is genuinely empirical and falsifiable.

**2. Sophisticated treatment of heterogeneity.** The recognition that alignment targets should be distributions rather than point estimates is important. The analysis showing that HOMOSEX acceptance varies systematically by income quartile (43% for lowest vs. 67% for highest earners) and that different values move independently (HOMOSEX reversed while ABANY continued rising) represents meaningful progress beyond "what does humanity want?" framing. This connects to cooperative AI frameworks—systems must navigate persistent disagreement, not wait for convergence.

**3. Two-level uncertainty quantification.** Distinguishing aleatoric (genuine value pluralism) from epistemic (our uncertainty about the distribution) is theoretically sound and practically important. Too often, alignment proposals collapse these, treating value heterogeneity as mere measurement error to be reduced rather than as fundamental feature of normative systems.

**4. Backlash dynamics.** The finding that HOMOSEX reversed trend in 2024, with explanatory mechanisms (partisan polarization, young Republican shift, counter-mobilization to public LGBTQ assertion), highlights a crucial challenge for forecasting approaches. The paper deserves credit for not downplaying this result. Value trajectories exhibit path dependencies and reactive dynamics that simple extrapolation misses—this is central to normative system evolution.

## Concerns and Weaknesses

**1. Democratic legitimacy and procedural justice.** The paper's framing—aligning AI to "projected post-reflection values" rather than current preferences—raises unresolved governance questions. Who decides what counts as adequate "reflection"? What economic conditions define the projection scenario? The paper acknowledges these are "choices" that "should be transparent," but this undersells the difficulty. These choices encode power. A forecast conditioned on "post-scarcity with extended deliberation" might predict very different values than one conditioned on "persistent inequality with polarized media." The latter may be more realistic, but the former more normatively appealing. This tension needs deeper engagement.

**2. Assumption that value change tracks moral progress.** The paper states it predicts "what values humanity would hold after reflection—not that all values are equally valid." But the validation methodology conflates temporal change with reflection. That 79% supported same-sex marriage in 2021 vs. 32% in 1986 doesn't mean the 2021 value represents more reflection—it represents more time. The causal mechanisms (generational replacement, exposure, information cascades) are sociological, not necessarily epistemic. A future where values reverse—as HOMOSEX did in 2024—isn't less "reflective"; it may reflect different mobilization dynamics. The paper needs clearer argumentation about why temporal extrapolation approximates idealized reflection.

**3. Training data contamination remains unresolved.** While the GPT-4o test on GSS 2024 is methodologically clean, the main results (2.2x improvement over baselines) use Claude on data that may be in its training set. The paper proposes using base models "without RLHF to avoid contaminating predictions with post-cutoff moral attitudes," but RLHF isn't the only concern—pre-training on web text that discusses GSS findings would also contaminate. The proposal to "test with base models" is crucial but hasn't been executed. Until it is, the core quantitative claim remains uncertain.

**4. Insufficient engagement with AI governance implications.** If value forecasting works, it becomes a technology of power. Governments, corporations, or other actors could use these forecasts to justify policies ("we're implementing what you'll value in 20 years") or to strategically intervene in value formation processes. The paper mentions manipulation risk but treats it as generic to all social science. Value forecasting is different: it provides forward-looking predictive targets that could justify paternalistic AI deployment. The paper needs to address: What institutional arrangements would make value forecasting legitimate? What forms of democratic oversight are required? Under what conditions should forecasts influence AI systems vs. remaining research outputs?

**5. Sparse treatment of normative pluralism.** The heterogeneity analysis is quantitative (different groups hold different values) but not deeply normative (different value *systems* may be incommensurable). The proposed alignment approach—"prefer actions that score well across multiple value systems"—works for shallow disagreements but breaks down for deep ones. How should an AI navigate conflicts between individual liberty and collective welfare when these aren't simply different weightings but different ontological frameworks? The Rawlsian "reasonable pluralism" literature and work on normative systems in law would strengthen this section.

## Specific Suggestions

1. **Add a governance section.** Explicitly address: Who should control value forecasting systems? What transparency requirements? What appeals processes when forecasts are contested? What role for democratic input into conditioning assumptions (post-scarcity vs. inequality scenarios)?

2. **Strengthen the philosophical argumentation.** Engage more deeply with the reflective equilibrium literature (Rawls, Daniels) and idealized deliberation theories (Habermas, Cohen) to clarify when temporal change approximates reflection vs. mere preference drift. Consider drawing on work on "adaptive preferences" (Nussbaum, Elster)—values change under oppression shouldn't necessarily guide alignment.

3. **Develop the institutional proposal.** Value forecasting as academic research is one thing; value forecasting as input to deployed AI systems is another. The paper needs a clearer account of the socio-technical system: How would forecasts be generated, validated, updated, and fed into alignment processes? What role for ongoing human feedback vs. forecasted future feedback?

4. **Test the base model claim.** Before publication, run the core experiment (1990→2021 prediction for HOMOSEX/GRASS) using base models without RLHF, ideally with training cutoffs that precede the test data. If results hold, the quantitative claim is much stronger.

5. **Expand the backlash analysis.** The HOMOSEX reversal is theoretically rich. Develop a formal model of when value progress triggers counter-mobilization. This could draw on social movement theory, backlash politics literature, and work on norm cascades. Can LLMs predict inflection points, or only extrapolate trends?

6. **Clarify the alignment pathway.** The paper proposes forecasting as "complement to current RLHF." Be more specific: Would value forecasts override human feedback when they conflict? Weight them equally? Serve as long-term aspirational targets while RLHF handles near-term preferences? The integration matters for evaluation.

## Minor Issues

- The income-values gradient analysis (Table, p.5) is suggestive but needs causal clarity. Does higher income cause more liberal values, or do both reflect education/urbanization? This matters for projecting values under AI-driven growth.
- The "long reflection" forecasts (Table, p.6) show HOMOSEX at 95% [85,99] for post-scarcity 2100, but we know 2024 was 55%. Include sensitivity analysis: what if backlash continues?
- Cite the cooperative AI literature more directly (Dafoe et al. 2020, Hadfield et al. 2021) when discussing heterogeneity and alignment to distributions.

## Recommendation

**Major Revision.** This paper makes a valuable contribution by proposing an empirically testable approach to a problem too often treated as pure philosophy. The historical validation methodology is sound in principle, and the heterogeneity/uncertainty frameworks are important advances. However, the governance implications are underdeveloped, the philosophical argumentation needs strengthening, and the core quantitative results require validation with base models to rule out training data contamination.

If the authors address these concerns—particularly adding institutional analysis and running clean base model tests—this could be a significant paper that shifts how the alignment community thinks about value learning. The negative result (HOMOSEX reversal) is as important as the positive ones and should be foregrounded: value forecasting is possible but harder than trend extrapolation. That's a finding worth publishing.

The paper's ultimate contribution may not be "here's how to align AI" but rather "here's an empirical research program that reveals the limits of value forecasting." Either way, the field needs this work.

**Confidence**: High. This is within my area of expertise (AI governance, normative systems, cooperative AI).

---

**Post-Review Note**: I find the "Society in Silico" infrastructure described in the acknowledgments (PolicyEngine for policy effects, Democrasim for democratic aggregation, HiveSight for heterogeneity) intellectually appealing. The vision of connecting microsimulation, silicon sampling, and value forecasting into an integrated system for studying collective choice is ambitious. However, the current paper should focus on establishing the core value forecasting claim. The broader system can be developed in subsequent work.

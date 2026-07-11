# Fact catalog — Chapter 16: Simulating values
Source: `manuscript/part-5-horizon/16-simulating-values.md`. Target chapter number in rewrite: 17. Raw material for a from-scratch rewrite; paraphrased except where marked Quotes/Author-texture. The empirical numbers here must stay consistent with the value-forecasting paper/EA post [@ghenis2026valueforecasting] (repo `github.com/maxghenis/value-forecasting`, branch `ea-post-rewrite-2026-07`).

## Facts

### Framing (horizon, not foundation)
- Every earlier chapter obeyed one discipline: a simulation earns trust only where its verification chain ends in ground truth — a forecast graded against the official number, an encoding checked against a reference calculator, a statute quoted to the letter.
- This chapter reaches past that line: its verification chain does not yet terminate in ground truth. The author states this at the outset — read it as horizon, not foundation.
- The deepest question in the book's set: not "what do people want today?" but what people would want after reflection — and whether that is something a model could forecast.

### The 2024 miss (the center of the chapter)
- In 2024 the author ran the first systematic test he knows of on whether a language model can forecast value change; the headline result was a miss.
- The General Social Survey's long-running measure of whether same-sex relations are "not wrong at all" had climbed for decades to nearly 63% by 2022; in 2024 it fell to just under 56% [@gss2024; @gss2024homosex].
- Every method tried — the language model, a linear trend, a no-change baseline — expected the climb to continue. Every method missed it. ("Every-method-missed-it.")
- [Underlying series supplied by the cataloging brief, for the rewriter's reference: the GSS "not wrong at all" (HOMOSEX) readings run 57 / 62 / 61 / ~55 for 2018 / 2021 / 2022 / 2024 — a roughly 6-point reversal. The chapter's own prose rounds these to "nearly 63% by 2022" and "just under 56%" in 2024 (a ~7-point turn). Use the chapter's figures in prose; the fuller series is context.] **Mark these exact 2021/2022/2024 values "account-gated, direction corroborated"** per research/part345-verification.md #11: they are gated behind the GSS Data Explorer (var HOMOSEX / 633) and could not be pinned to a primary source this pass. Direction and magnitude ARE corroborated — GSS "always wrong" = 34.9% in 2024 (→ "not wrong at all" mid-50s, ≈ the book's ~56%), and Gallup's parallel moral-acceptance measure fell 71%→~64% (2022→23). Reconcile the internal inconsistency before print: the chapter prose says "nearly 63% (2022)" while the working series says ~61% (2022) — pull the exact survey-weighted value from the Data Explorer at copyedit.
- **MANDATORY caveat — the GSS 2021 mixed-mode discontinuity** (new — primary source; research/part345-verification.md #11 + key discovery for this chapter): the GSS moved to mixed-mode collection with the 2021/2022 waves (COVID). The 2021 wave used an address-based **push-to-web** design with a response rate of **~17% vs ~50%** in 2022; self-administration removes interviewer/social-desirability pressure and **tends to RAISE "not wrong at all"** responses. So **both** the pre-2024 climb (the 2021–22 readings the model trusted) **and** the 2024 reversal partly sit on a **methodological break, not pure attitude change**. NORC "cautions data users to carefully examine how a change they are analyzing relates to this methodological shift" [@gss2024homosex]. **The chapter MUST carry this caveat** — it turns the central "miss" from an unexplained surprise into a doubly-honest one: the model missed the reversal, *and* part of the series it trusted may be a mode artifact.

### Could you have forecast the change? (Gallup anchor)
- Gallup began asking about same-sex marriage in 1996, when 27% of Americans were in favor; by the early 2020s about seven in ten were [@gallup2024marriage]. (Recency nuance per research/part345-verification.md correction #10: 71% was the 2022–23 peak; Gallup then shows 69% (2024), ~68% (2025), 65% (May 2026). "About seven in ten" is fine for the early-2020s framing used here, but should not be presented as the current number.)
- The change was not random — it followed exposure, generational replacement, and the slow crystallization of arguments — and in retrospect looks almost legible. The question: could you have called that trajectory in 1996, and can you now predict which contested values will look obvious in a generation and which will reverse?
- This is not a search for moral truth; it is a forecasting question, the same shape as forecasting inflation or rainfall, done not perfectly but better than chance — the book's same apparatus (a survey, a time series, a model, a calibrated interval, a grade when the next reading lands), with an attitude on the vertical axis instead of a dollar or an unemployment rate.
- It matters because decisions get made against contested values all the time, increasingly by automated systems. "Do what humans want" fractures the moment you ask which humans, and whether you mean what they say now or what they would endorse on reflection.
- Stuart Russell built his account of controllable AI on exactly that uncertainty — machines should be unsure what humans want and learn it from behavior [@russell2019human] — but behavior reveals present preferences, precisely the ones most likely to move. If value change has structure, some of it might be forecastable.

### The 17-variable backtest (with baselines named)
- The GSS has asked Americans the same attitude questions since 1972, with wording stable enough to form real time series.
- The author took 17 of them — spanning sexual morality, drug policy, gender roles, race, religion, confidence in science, guns, capital punishment, and free speech — and gave a frontier model (identified in the cataloging brief as GPT-4o) each variable's history through 2021, asking not for a single guess but for a spread: the 10th, 25th, 50th, 75th, and 90th percentiles. The spread was meant to force the model to express uncertainty rather than default to false confidence.
- Two deliberately simple baselines set the bar: a linear extrapolation (fit a trend line to the history and extend it) and a no-change baseline (next reading equals the historical average). Any method worth having should beat both; beating a straight line is the harder, more meaningful test.
- Results: the model's 2024 forecasts landed at a mean absolute error of about 4.8 percentage points, against about 7.2 for the linear trend (roughly 1.5 times better) and about 10.6 for the no-change baseline (roughly 2.2 times better).
- Naming the baseline matters: "2.2 times better" is true only against the weakest baseline (assumes nothing changes); the honest headline is that the model beat a straight line by about half again.
- The advantage was largest where trends bent (accelerating acceptance on some questions, decelerating change on others), the shape where a straight line goes wrong.
- Interval calibration: raw, the intervals came out too narrow (the familiar overconfidence of language models) and had to be widened with a standard calibration step borrowed from weather forecasting before the 80% intervals actually covered 80% of the outcomes.
- Read carefully, a modest, real result: on three-year forecasts of American social attitudes, a language model beat naive baselines, by more against the weakest and less against the sterner one — and then it, and everything else, missed the reversal.
- Same-sex acceptance was the variable with the cleanest story: climbed half a century through generational replacement and exposure; every hallmark of a one-way trend; exactly the series a forecaster feels safe about. The 2024 reading turned down, nearly seven points off its 2022 level.
- Seven points is not large by the standards of survey noise, and it may yet prove to be noise, a methodological artifact, or the leading edge of a genuine backlash — that question is still open. But the point is direction: every method predicted up and the number went down, on the one series a forecaster would have staked the most on. Value change carries genuine surprises that no model, statistical or neural, reliably anticipates.

### The July 2026 pre-registered replication (persistence won)
- The miss sent the author back to rebuild the experiment; in July 2026 he pre-registered a replication before making a single model call [@ghenis2026valueforecasting].
- Design: twenty GSS items this time, survey-weighted; each model shown the series only through 2022 and asked for 2024; every training cutoff checked against the data's release date so no arm could be "forecasting" a number it had already read.
- The baselines got sterner; the one that matters is persistence — the forecast that 2024 simply equals 2022.
- Result: persistence beat everything. The language models' errors ran 3.9 to 4.1 points against persistence's 3.15 (n = 20).
- A frontier reasoning model did no better than the cheap ones; raising a model's reasoning effort made its accuracy slightly worse, not better.
- Interval calibration: the models' 90% intervals covered the truth roughly half the time; properly computed classical intervals covered at their stated rate.
- The 2024 wave was stranger than one famous reversal: eight of the twenty items broke their pre-2022 trend, and four of them — approval of the school-prayer ban, same-sex relations, rejection of traditional gender roles, and marijuana legalization — posted the largest single-wave declines in their items' recorded histories.
- Every arm, model and baseline alike, missed the same-sex reversal again, with point forecasts between 60 and 66 against an actual just under 56; the only interval that contained the truth did so by being twenty-one points wide.
- Squaring the two runs: baselines are the answer and most of the result. The earlier comparison set the bar at a trend line and the historical average — and against an average over decades of lower readings, any method that merely notices the recent level looks brilliant. Persistence is the bar that matters for slow-moving series, and nothing cleared it.

### Identity-leakage control (recall vs forecast)
- The rebuilt experiment included the control the earlier ones lacked, and it explains where much of the apparent forecasting skill in this literature comes from: run a model on a series it can name and it is not only extrapolating, it is remembering.
- Demonstration: shown the same-sex series through 2010 *with its identity visible*, one model "forecast" the present at 78 — a level the series has never reached in fifty years; shown the same numbers with the name stripped, the same model said 47.5. A thirty-point swing from the label alone.
- Identified backtests inside a model's training window are recall tests wearing a forecast's clothes. The diagnosis reaches past this chapter: a growing literature evaluates language models by "predicting" surveys, elections, and experiments the models have already read about.
- Two protocols fix it — strip the identities, or forecast strictly forward, where no training corpus can help — and the rebuilt experiment adopts both, with forecasts for the 2026 and 2028 GSS waves registered before the data exist.

### Pre-1931 language models (reaching further back)
- Language models trained exclusively on text from before 1931 now exist; such a model has read no poll it could parrot — Gallup's first national surveys came in 1935, the GSS began in 1972, and the entire quantitative record of public opinion lies beyond its horizon [NEEDS CITATION: Talkie-1930, talkie-lm.com].
- Early evaluations locate their weakness at the elicitation layer rather than the knowledge layer (they can complete what they cannot converse about) — an engineering problem, not a wall — and stronger checkpoints at the same cutoff are expected within months.
- The eventual prize: ninety years of graded actuals — every reversal, plateau, and backlash in the polling record, out-of-sample by construction.

### Long-horizon projections (method-output only)
- The same apparatus can be pointed much further out — to 2050, or 2100 — and will dutifully return a tidy median and interval for each.
- The author once tabulated exactly those long-horizon numbers; after 2024 he cut the table, because the only honest way to read such figures is as an illustration of what the method emits when asked, never as a finding about the future.
- The further past the data you push, the more the interval — not the median — is the result worth reporting.

### Heterogeneity is the target, not the noise
- A tempting mistake: to imagine forecasting converges on a single answer (the value system humanity is "heading toward"). It does not and should not. Even granting perfect foresight, people would still hold different things dear; the object worth forecasting is a distribution across a population, not a point on a line.
- That reframing has teeth for anything that would consume the forecast. A point estimate invites a system to optimize toward it; a distribution refuses that — it says that at the end of any plausible reflection there remain people who weigh liberty over welfare and people who weigh welfare over liberty, and both are part of the answer, not error bars around it.
- A system taking the distribution seriously would favor actions that score acceptably across several value systems rather than maximally within one; grow cautious where the value systems disagree most; and treat a move that catastrophically violates any large minority as disqualified rather than merely outvoted. That is value pluralism recast as an engineering constraint (closer to a robustness requirement than a moral theory).
- The author resists (as the old draft did not) printing a table of invented population shares: a made-up table with tidy percentages would be exactly the confident fiction the book is against, dressed as a finding. The distribution is the thing to estimate, not to assume.

### Two kinds of uncertainty (aleatoric / epistemic)
- The forecast carries two different uncertainties that do not reduce to each other:
  - **Aleatoric** — the genuine spread of values across people, which no amount of learning erases, because it is not ignorance but reality; even a perfect model of a population that will never agree still reports disagreement.
  - **Epistemic** — our uncertainty about what that spread even is, a distribution over distributions that better data and better methods narrow.
- They behave differently and demand different responses: epistemic uncertainty is the part you can pay to reduce (more surveys, longer histories, better calibration); aleatoric uncertainty is the part you must design around, because it stays when the study is done.
- Both must be quantified, and quantified separately: not "humanity will value X," but a probability that it does, with an interval around that probability, and a clear account of how much of the interval is ignorance and how much is real variety. The same discipline Chapter 13 applied to policy costs, turned on values.

### Reflection is not the same as time (the deepest problem)
- Temporal change is not reflection. The appeal of forecasting values is the hope that where attitudes are heading is better than where they are — that the forecast points forward in judgment, not just in time. Nothing in the data licenses that hope.
- That support for same-sex marriage rose from 27% to roughly seven in ten over a generation shows that time passed and attitudes moved; it does not show anyone reasoned more carefully.
- The engines of value change — generational replacement, media exposure, information cascades, tribal signaling — are sociological, not epistemic; a model that predicts them predicts a social process, not a deliberative one.
- Some shifts plainly track moral progress (abolition, the widening of the franchise); others may be drift with no progress in them; others might be backlash to perceived overreach — one live reading of the 2024 reversal, and if so, the model that "should" have predicted continued acceptance would have been wrong in a morally loaded direction.
- The philosophers who pressed hardest offer warnings more than solutions:
  - **Rawls** distinguished reasonable from unreasonable comprehensive doctrines — not every value system deserves equal weight in political life — but "reasonable" resists being turned into a forecasting rule; you cannot regress on it.
  - **Habermas** set conditions for undistorted deliberation (equal participation, no coercion) that no historical stretch of attitude change is guaranteed to have met, and mostly did not.
  - **Sen and Nussbaum** warned about adaptive preferences: values formed under oppression, stable and sincerely held, that it would be perverse to extrapolate forward as though they were considered choices (a person raised to expect little may sincerely want little; a society that has normalized an injustice may show stable, well-measured preferences for it).
- A forecasting model does not know the difference between a preference reasoned into and one ground into place — both are just points in a time series — and predicting the second accurately would be an achievement in the service of nothing good.
- Honest position: we have no clean account of when temporal change tracks reflection and when it is mere drift. Predicting well is evidence of underlying structure; it is not evidence that the structure is worth honoring. A permanent reason for humility, not a bug a larger model removes.

### Whose trajectory? (WVS / Inglehart)
- The GSS is American, and value trajectories are not obviously universal — everything in the chapter was measured on one country's attitudes.
- The World Values Survey, run across roughly a hundred countries since 1981, shows both convergence and its opposite. On some dimensions there is a broad drift toward self-expression values with economic development and generational turnover — Ronald Inglehart's post-materialist pattern (as societies grow wealthier and more secure, priorities shift from survival toward autonomy and tolerance).
- On others — religion, family structure, the norms around sexuality — cultural zones persist, and different starting points produce genuinely different paths rather than the same path at different speeds. Recent years have added pointed reversals in several countries, movements rejecting cosmopolitan liberal values outright.
- Any global forecast would have to model heterogeneity at the level of whole societies, not just individuals; there is no neutral vantage from which to call one "ahead" and another "behind."

### Objections (three)
1. **Moral relativism dressed up in statistics?** No — forecasting where values are heading is not the claim that all values are equally valid, any more than forecasting a hurricane endorses the storm. If the honest projection were that a reflective public would reject some cruelty, that would be a prediction, not a shrug.
2. **Values too contingent to predict?** Perhaps — but that is an empirical question, and validation is how one answers it. The 17-variable test says the answer is "partly," and the 2024 miss marks exactly where "partly" runs out.
3. **The same understanding could accelerate or suppress a value shift.** True, and true of all social science; not a reason to stop understanding things — but the reason the next question is not about method at all.

### The governance questions
- If value forecasting one day worked well enough to be worth consulting, it would immediately become a technology of power, and who holds it would matter as much as how accurate it is (a government could dress paternalism as foresight; a firm could steer preferences rather than serve them; a lab could align a system to projected values that happen to coincide with its own interests).
- Questions any serious version must answer before it earns authority:
  - **Who generates the forecasts?** Academics, government, and private companies each bring different incentives and accountability; none should hold a monopoly; distributed production under open methods is more trustworthy than any single center, because it can be checked.
  - **Which conditioning assumptions are on the table?** A forecast conditioned on broad deliberation differs from one conditioned on polarized media, and the choice is itself a value judgment; the assumptions encode values and must be stated where they can be argued with.
  - **What is democratic input for?** Forecasts should inform deliberation, never stand in for it; citizens must be able to examine the method, challenge the assumptions, and reject a forecast-based justification outright.
  - **How are disputes resolved?** Contested forecasts need appeals — replication, public comment, independent review — not an oracle's say-so.
  - **What happens when the forecast and today's expressed values disagree?** The hardest question, and honest answers stay uncertain. The 2024 reversal is the cautionary tale: a 2020 projection of continued acceptance, used to justify anything, would have been overconfident within four years. A governance system for this has to be built to absorb surprise and revise — built like the scoreboard, not like a prophet.

### What this has to do with alignment (restrained)
- If value forecasting ever earned admission on the book's own terms — calibrated, validated across variables and countries and horizons, adversarially tested — it would bear on how AI systems weigh contested human values: as one input, evidence about where considered preferences might sit, never an authority over them.
- Today it has earned no such thing: a research question with one suggestive backtest, one humbling miss, and one pre-registered replication in which nothing beat persistence [@ghenis2026valueforecasting] [NEEDS CITATION: swap in the published essay when it ships].
- The institutional shape, if it ever cohered: value forecasting is at bottom a forecasting problem — a probability distribution over what people will come to value, scored against what actually happens — exactly the kind of claim the Thesis Institute exists to post with an interval and grade (referenced to Chapter 13). None of it has resolved; there is no track record here, only a method and a discipline for eventually being wrong in public.
- One could imagine chaining the book's tools into a single machine — a forecast value distribution feeding a democratic simulation feeding a policy model feeding measured welfare — but that is an unbuilt composition of mostly toy parts, and drawing the diagram is not the same as building the machine.
- Closing posture: everything before this part of the book earned its place by terminating in a check against the world; this chapter did not, and the distinction is kept sharp. The value-forecasting work is a genuine experiment with a genuine result and a genuine, disciplining failure — the one place in the book reasoning past the edge of what can yet be verified. The correct posture toward it is interest without belief.
- What can honestly be said, smaller and sturdier than the grand version: ask people what they value, model the patterns, project them forward with calibrated uncertainty, and stay loud about how uncertain the projection is. Surveys capture current states, not trajectories; forecasting is one way to reach for the trajectory, and the 2024 miss is a standing reminder of how easily that reach exceeds its grasp. We cannot know what humanity would choose after reflection, and should distrust anyone who says they can — but we might, someday, forecast it, badly at first and a little better with each miss admitted in public.
- The fork in the road is already here: the choice the next chapter returns to — open or closed, graded or oracular, plural or singular — does not wait on value forecasting; it is being made now, with the tools already built.

## Story beats
- **The opening humbling beat (the 2024 miss).** The chapter deliberately opens on its own failure — same-sex acceptance fell when every method predicted a rise — and declares the miss "the center of this chapter." Structural inversion: the failure, not the success, carries the lesson.
- **The identity-leakage probe (demonstration beat).** The same model "forecasts" 78 with the series named and 47.5 with the name stripped — a thirty-point swing that exposes recall masquerading as forecasting. A concrete, self-contained demonstration.
- **The cut long-horizon table beat.** The author reveals he once tabulated 2050/2100 value projections and deleted them after 2024 — a visible act of editorial discipline, modeling the "interval, not median, is the result" rule.
- **The mid-build / rebuilt-experiment reflection.** "The miss sent me back to rebuild the experiment properly, and the rebuild cut deeper than the miss" — a first-person reflection on being humbled and doing the harder, pre-registered version.

## Quotes
- The GSS item wording "not wrong at all" (same-sex relations) is survey phrasing, not an attributed quotation.
- Stuart Russell's position ("machines should be unsure what humans want and learn it from behavior") is paraphrased in the chapter, not quoted verbatim [@russell2019human].
- No attributed third-party verbatim quotation appears in this chapter. The load-bearing memorable lines are the author's own (see Author-texture).

## Arguments
1. Horizon, not foundation: this chapter intentionally steps past the ground-truth discipline the rest of the book obeys; the correct posture toward its results is "interest without belief."
2. The 2024 miss is the center, not a footnote — on the cleanest one-way series, every method predicted up and the number went down; value change carries surprises no model reliably anticipates.
3. Baselines are most of the result: in the pre-registered rebuild, persistence (2024 = 2022) beat every language model, and the flattering "2.2× better" from the first run was only against the weakest baseline. Naming the baseline is the honest move.
4. Identity leakage means much apparent forecasting skill in this literature is recall inside the training window; the fix is to strip identities or forecast strictly forward (2026/2028 waves registered before the data exist).
5. Heterogeneity is the target, not the noise: forecast a distribution over a population, never a point; value pluralism is an engineering/robustness constraint, and inventing tidy population-share tables is the confident fiction the book is against.
6. Aleatoric and epistemic uncertainty must be quantified separately — one you pay to reduce, one you design around — the same discipline Chapter 13 applied to policy costs.
7. Reflection is not the same as time: predicting a value shift well is evidence of underlying structure, not that the structure is worth honoring (adaptive preferences; Rawls/Habermas/Sen/Nussbaum warn that temporal change need not track reflection).
8. Value forecasting would be a technology of power and must answer the governance questions (who forecasts, which assumptions, what democratic input is for, how disputes resolve, what happens on disagreement) before earning any authority — built like the scoreboard, not a prophet.
9. The alignment tie-in is restrained: at most one input, evidence about where considered preferences might sit, never an authority — and today it has earned nothing, being one backtest, one miss, and one replication where nothing beat persistence.

## Author-texture (verbatim, may be reused; use sparingly)
- "read what follows as horizon, not foundation." (the framing keeper)
- "The correct posture toward it is interest without belief." / "interest without belief." (the closing-posture keeper)
- "only a method and a discipline for eventually being wrong in public."
- "Heterogeneity is the target, not the noise." (section thesis line)
- First-person keepers (raw phrasing): "In 2024 I ran the first systematic test I know of on whether a language model can forecast value change, and the headline result was a miss."; "I once tabulated exactly those long-horizon numbers; after 2024, I have cut the table…"; "In July 2026 I pre-registered a replication before making a single model call."; "It is also the one place in the book where I am reasoning past the edge of what can yet be verified."

## Structural notes
- **Chapter job:** The horizon chapter — reason honestly past the book's ground-truth edge about whether a model can forecast reflective value change; center on the 2024 same-sex-acceptance miss and the July 2026 pre-registered replication (persistence beat everything); establish heterogeneity-as-target, the aleatoric/epistemic split, reflection≠time, cross-country heterogeneity (WVS/Inglehart), the governance questions, and a restrained alignment tie-in.
- **Handoff in (from the democracy chapter):** the values/beliefs separation ("Values are for humans; facts are for tools") and the ground-truth contrast point straight at forecasting what people would value after reflection.
- **Handoff out (16→17, the fork):** whatever the horizon holds for value forecasting, the open-vs-closed choice does not wait on it — it is being made now with tools already built. This is the explicit setup for the final chapter's fork.
- **Phrasing constraints (hard):**
  - Horizon, not foundation — this chapter must stay flagged as reasoning past the verifiable edge; posture is "interest without belief."
  - No track record: in the pre-registered replication nothing beat persistence, and none of the forward-registered forecasts (2026/2028) has resolved. Never imply value forecasting works or has been validated.
  - Long-horizon projections (2050/2100) appear ONLY as an illustration of what the method emits when asked — never as a finding. The cut-table beat is the model to follow; do not reintroduce invented population-share tables.
  - The empirical numbers must match the paper/EA post [@ghenis2026valueforecasting] (repo `maxghenis/value-forecasting`, branch `ea-post-rewrite-2026-07`); keep book, paper, and post telling the same story with the same figures. First-run: ~4.8pp MAE (17 GSS vars) vs ~7.2 linear (~1.5×) and ~10.6 no-change (~2.2×). Rebuild: LLMs 3.9–4.1 vs persistence 3.15 (n=20); identity-leakage 78 vs 47.5.
  - Carry the [NEEDS CITATION: Talkie-1930, talkie-lm.com] and [NEEDS CITATION: swap in the published essay when it ships] markers — resolve, don't delete. (Both stay open: no primary source was supplied this pass.)
  - **MANDATORY (added 2026-07-11): the GSS 2021 mixed-mode discontinuity caveat is non-negotiable in this chapter.** The 2021/2022 push-to-web switch (response rate ~17% vs ~50%; self-administration tends to raise "not wrong at all") means the pre-2024 climb and the 2024 reversal both partly rest on a methodological break — the chapter must say so [@gss2024homosex]. Exact 2021/2022/2024 HOMOSEX values are "account-gated, direction corroborated"; reconcile the prose's ~63% (2022) with the working series' ~61% at copyedit.
  - Retired-name guard: Thesis Institute is the prediction pole; keep the alignment tie-in one restrained input, never an authority.

# Fact catalog — Chapter 15: Simulating democracy
Source: `manuscript/part-5-horizon/15-simulating-democracy.md`. Target chapter number in rewrite: 16. Raw material for a from-scratch rewrite; paraphrased except where marked Quotes/Author-texture.

## Facts

### Framing (toy status, stated up front)
- The chapter opens with an explicit note to readers: Democrasim, the model at its center, is a toy — a thought experiment in code, built to make one relationship concrete enough to reason about, not to contribute to political science.
- It is explicitly NOT a validated production system like PolicyEngine, nor a benchmarked estimator like the opinion work of the previous chapter. It makes simplifying assumptions political scientists would rightly criticize. Read for intuition about information and democracy, not as established fact.

### The skeptics (Achen & Bartels, Caplan)
- The chapter's motivating question: why do democratic outcomes so often diverge from voter welfare? — a question that has occupied political scientists for decades.
- Christopher Achen and Larry Bartels, in *Democracy for Realists* (2016), argued the textbook story — informed citizens evaluate policies, pick the candidate whose platform fits their preferences, and elections translate public will into government — is largely fiction [@achen2016democracy].
- In their telling, voters mostly choose parties by social identity and group loyalty, not policy evaluation; they punish incumbents for droughts and other things no government controls; they reward growth that began before the incumbent took office. The "folk theory" of the rational, policy-weighing voter bears little resemblance to how democracy runs.
- Bryan Caplan went further in *The Myth of the Rational Voter* (2007): voters are not merely ignorant but *systematically biased* [@caplan2007myth].
- Drawing on a survey that set the public's economic views beside professional economists', Caplan identified four persistent distortions — anti-market, anti-foreign, make-work, and pessimistic bias. These are directional, not random errors that cancel in aggregation, and they push democratic outcomes away from what most economists would call welfare-improving policy.
- The chapter's claim is deliberately modest: not whether information can fix democracy (it can't) but whether voter accuracy about policy impacts matters at the margin, and whether tools can improve it. If identity and loyalty carry most of the vote, anything an information tool can touch is at best a minority share of the decision; the argument lives entirely inside that minority share.

### The perception problem (Sarah)
- Hypothetical voter "Sarah": a schoolteacher with two kids, choosing between two candidates — one would expand the Child Tax Credit, the other would repeal the state income tax. Which leaves her family better off?
- Without doing the arithmetic she has to guess (a vague sense that state income tax stings; a memory that the expanded pandemic credit helped; talking heads framing to persuade, not inform).
- Her vote is a blend of what she values, what she believes each policy would do, what her party and community support, and noise (a candidate's charisma, the morning's headlines, the weather). Even if her values are clear, her vote may not track them because she cannot see the true impacts — she votes on a noisy signal.
- Multiply Sarah by a national electorate: the aggregate only roughly, noisily tracks what voters would choose if they could see clearly. Achen and Bartels would call even this too generous; Caplan would add that the ones who try are systematically wrong. The chapter's narrower question: to the extent *any* part of the vote is policy-driven, does the quality of that signal matter?

### The Democrasim toy model
- Author built a small simulation called Democrasim to reason about that question; the emphasis is on *small*.
- Model structure: each simulated voter carries three things — (1) a set of weighted preferences across policy dimensions (how much they care about the economy vs the environment vs social issues; their true values); (2) an accuracy level (how close their perception of a policy's effects sits to the truth); (3) a bias (a systematic lean beyond random noise — e.g. consistently overstating a tax burden or understating an environmental cost).
- Core equation: **perceived impact = true impact + noise + bias**, where the noise shrinks as accuracy rises. Voters compare candidates on perceived impacts weighted by their preferences, and the majority wins.
- The question the model asks: as voter accuracy varies, what happens to the welfare quality of who wins?
- Results: when accuracy is high, electoral outcomes track welfare (the candidate whose policies would actually improve lives tends to win); when accuracy is low, the link frays (winners might have good or bad policies, because the signal is too corrupted to sort them).
- The model shows something like a threshold: below a certain accuracy, elections become essentially random with respect to welfare; above it, the relationship strengthens quickly.
- Illustrative mechanism (round, invented numbers, chosen to illustrate not to report): Candidate A expands the Child Tax Credit and pays with a small rise in the top marginal rate; Candidate B repeals the state income tax and pays by cutting food assistance. For a middle-income family with children and no food assistance, the credit expansion is worth more than the tax repeal, and the offsetting rate increase never reaches them — so they are better off under A, even though "repeal the income tax" sounds like the bigger deal. An accurate perceiver picks A; a noisy perceiver may pick B against her own interest. Scaled up: lower-income families do far better under A, upper-income families modestly better under B, and whether the election reflects that distribution depends on how much of the vote is signal rather than framing.
- Bias bends outcomes a different way: if voters systematically overvalue tax cuts relative to equivalent benefit increases, elections favor tax-cutting candidates regardless of welfare — Caplan's point reproduced in miniature.
- Overclaim caution (stated in text): the results come from a model with extreme simplifications; real voters have identities, loyalties, and psychology Democrasim ignores; it assumes voters maximize welfare through policy evaluation — the very folk theory Achen and Bartels dismantle. What it captures is one real dynamic: to the degree that *some* of the vote responds to perceived impacts, the quality of those perceptions matters. Even if only a fifth of the vote is policy-driven and the rest is identity, cleaning up that fifth still moves outcomes.
- Read backwards, Democrasim is the motivation model for everything the earlier chapters built: if outcomes track welfare only where perceptions of policy impacts are accurate, then the machinery that makes accurate perception cheap (rules encoded exactly, populations calibrated honestly, forecasts graded in public) is an input to whether self-government works at all. The stack exists to raise the accuracy term in this model.

### What the real evidence shows (mixed)
- Information sometimes moves votes when it reaches people. In Brazil, Claudio Ferraz and Frederico Finan found municipalities where federal corruption audits were released before an election punished corrupt incumbents at the polls — but the effect concentrated where local radio carried the results [@ferraz2008exposing]. Information that existed but did not travel changed nothing.
- Nonpartisan voter guides in the US sit at the weaker end: they tend to raise political knowledge without much shifting vote choice, because in polarized settings most voters have already committed to a party.
- Arthur Lupia and Mathew McCubbins showed that voters lean on trusted-source shortcuts rather than full information [@lupia1998democratic] — which cuts both ways, since a shortcut can approximate an informed choice or entrench identity over evaluation.
- Accurate information and strategic misinformation do not compete on equal terms: a well-crafted misleading claim travels farther and sticks longer than a dry correction. Democrasim, by treating noise as random, understates the problem — in the real world some of that noise is engineered by people with an interest in distortion.
- **Kansas 2012–2017.** In 2012 Kansas enacted large tax cuts its backers billed as a "real live experiment" in supply-side growth; independent analyses (of the kind PolicyEngine now produces) projected large shortfalls instead. The shortfalls came — years of budget crises and school-funding cuts, ending in a bipartisan reversal of the cuts in 2017. Voters paid for the lesson in billions of dollars and lost services over years; better information infrastructure might at least have shortened the loop.
- **ACA (referenced to Chapter 3).** CBO got total coverage gains roughly right but badly missed the composition, overestimating exchange enrollment and underestimating Medicaid. Voters who opposed the law over predicted exchange disruption, and voters who backed it for Medicaid, both experienced something other than what they had been told; the gap between perception and reality persisted for years.
- A 2017 survey found that about 35% of Americans did not know the ACA and "Obamacare" were the same law [@dropp2017obamacare] — a failure of basic information transmission no simulation can fix, and a measure of how far real voter knowledge sits from the idealized version. (Marker resolved per research/part345-verification.md: fielded by Morning Consult (n≈2,000), published by Kyle Dropp & Brendan Nyhan, NYT "The Upshot," 7 Feb 2017; the 35% = 17% who thought they were "different policies" + 18% "don't know." The book's "Morning Consult/NYT" attribution is correct.)
- Some limits no information tool touches: Kenneth Arrow's impossibility theorem (1951) proved that no ranked voting system can satisfy a short list of reasonable fairness conditions at once [@arrow1951social]; Gibbard and Satterthwaite showed any non-dictatorial system can be gamed by strategic voting. Better inputs do not repeal those constraints. (Publisher precision per research/part345-verification.md correction #9: the 1951 first edition of *Social Choice and Individual Values* is John Wiley & Sons (Cowles Commission Monograph 12), NOT Yale — Yale University Press published only the later editions (3rd ed. 2012). The bib entry @arrow1951social is already corrected to John Wiley.)
- Honest summary: better voter information is necessary but nowhere near sufficient — one lever among identity, institutions, and strategy, and the only one infrastructure can move directly rather than through the slow work of changing culture.

### The perception problem, against ground truth
- Democrasim can only *toy* with the perception problem because it has no ground truth to check against — its voters misperceive a policy's effects, but the "true" effects are just more numbers the model invented.
- The version that terminates in ground truth is the Chapter 13 one: forecasting a government metric under a policy counterfactual — what the unemployment rate will actually print next quarter, or how long a Medicaid call-center wait will run in a given month if a work-requirement deadline slips — and grading the forecast when the official number lands [@thesisinstitute2026].
- None of those forecasts has resolved yet; the point is not that the empirical version has been scored, but that the perception problem has an empirical form at all — the difference between a thought experiment (graded against numbers it made up) and a measurement (graded by numbers it did not).

### PolicyEngine as one input
- PolicyEngine computes what a specific household, with its actual circumstances, would pay or receive under a given policy — not "the average family pays X." It is free to anyone with a browser.
- Its transparency is no longer just a claim about open-source code: the rules it applies are open encodings, checked against reference calculators (the verification machinery of Chapter 10) — a stronger warrant than "inspect the source if you like."
- In Democrasim's vocabulary, that makes PolicyEngine an accuracy multiplier for the policy-evaluation slice of a vote: it moves a voter from "I sense this would hurt me" to "this changes my household's income by roughly this much." For Sarah, it turns the guess into a number she can see.
- It does nothing for the identity-driven part of the vote, does not override party loyalty, and does not resolve Arrow's problem in the voting rule itself — it removes one source of noise from one channel. A smaller claim than "informed voters fix democracy," and the right size.

### Futarchy, and the values/beliefs separation
- A more radical proposal: Robin Hanson's *futarchy* [@hanson2013futarchy]. Slogan: "vote on values, but bet on beliefs." Democratic processes decide *what we care about* (a welfare metric, a child-poverty rate); prediction markets decide *which policies achieve it* — a legislature proposes a bill, markets price the welfare metric conditional on passage versus failure, and if the market says welfare is higher with the bill, it becomes law [@hanson2000futarchy].
- No democracy has adopted it, for visible reasons: markets can be manipulated by deep pockets; most policy questions never draw enough trading to price reliably; "welfare" is contested to define; legitimacy depends partly on citizens feeling heard, which a price does not supply.
- But the thought experiment isolates the distinction that matters: values (the outcomes we want) versus beliefs (the policies that would produce them). PolicyEngine works the beliefs side; it never tells anyone what to want. Neither does Democrasim.

### Objections (four, answered)
1. **Maybe the preferences are the problem, not the perceptions.** True but orthogonal: if voters want harmful things and perceive accurately, they get harmful things — a different failure from wanting good things and misperceiving. Better perception at least delivers people what they actually want, the precondition for holding them responsible.
2. **Information won't reach the disengaged.** Partly true — non-voters won't open a calculator, and the ones who would are already relatively informed. But new modalities (an AI assistant that volunteers a policy's household impact; a calculation embedded where people already are) can reach past the self-selected few, and moving the moderately informed to well-informed still improves the signal.
3. **Calculated self-interest isn't good citizenship.** Fair — and PolicyEngine computes societal impacts too (poverty rates, inequality, total cost). The point is replacing perception with calculation, whatever a voter chooses to weigh.
4. **Arrow's theorem means none of this matters.** Arrow constrains the *mechanism*, not the quality of what feeds it. An imperfect aggregator still yields better outcomes from better-informed inputs. Arrow proved no perfect system exists; not that every system is equally good regardless of input.

### The democratic case for open infrastructure
- The argument is bounded on every side and stronger for it: democratic outcomes track voter welfare only to the degree voters perceive policy impacts accurately — one factor beside identity, institutions, and strategy; most voters perceive poorly, through noise and bias and thin information; tools exist that can sharpen the policy-evaluation slice.
- So investing in accessible, trustworthy policy analysis has civic value beyond any one person's tax optimization — not as a fix for democracy but as one contributor to informed self-government.
- That reframes what PolicyEngine is for: not a calculator for people who want to trim their taxes, but one component, among many, of democratic infrastructure.

## Story beats
- **The note-to-readers / toy disclaimer beat.** An unusual, upfront framing device that quarantines Democrasim as intuition-only before the chapter proper begins — a deliberate honesty move worth preserving in spirit.
- **The Sarah hypothetical (explicitly hypothetical).** A named schoolteacher with two kids deciding between a CTC expansion and a state-income-tax repeal; used both to introduce the perception problem and, later, to show PolicyEngine turning her guess into a number. Sarah is invented; keep her hypothetical.
- **The Candidate A vs Candidate B illustration (round, invented numbers).** A concrete two-candidate scenario (CTC + top-rate rise vs income-tax repeal + food-assistance cut) whose numbers are explicitly invented to illustrate the mechanism, not to report a calculation.
- **Democrasim-read-backwards beat.** The turn where the toy becomes the motivation model for the whole book: the stack exists to raise the "accuracy term."

## Quotes
- "vote on values, but bet on beliefs." — Robin Hanson, the futarchy slogan [@hanson2013futarchy].
- Kansas's 2012 tax cuts were billed by their backers as a "real live experiment" in supply-side growth.
- "folk theory" — Achen and Bartels's term for the rational, policy-weighing-voter story they dismantle [@achen2016democracy].
- "Values are for humans; facts are for tools." — narrative line, Chapter 15 (protected; see Author-texture).

## Arguments
1. The chapter's whole argument lives inside the policy-driven *minority share* of the vote: to the degree that *any* of the vote responds to perceived impacts, the quality of those perceptions matters — even if identity and loyalty carry most of it.
2. Democrasim is a toy (absolute framing): its "true" effects are invented, so it can only demonstrate a dynamic, never measure the world.
3. Read backwards, Democrasim is why the rest of the book exists — "the stack exists to raise the accuracy term in this model."
4. Better voter information is necessary but nowhere near sufficient: one lever among identity, institutions, and strategy, and the only one infrastructure can move directly.
5. Values and beliefs must be separated — "Values are for humans; facts are for tools." PolicyEngine (and Democrasim) work only the beliefs side and never tell anyone what to want.
6. Arrow constrains the aggregation *mechanism*, not the quality of the inputs; polishing the inputs still improves outcomes from an imperfect aggregator.
7. This reframes PolicyEngine as democratic infrastructure — one component among many of informed self-government — rather than a private tax-optimization calculator.

## Author-texture (verbatim, may be reused; use sparingly)
- "Values are for humans; facts are for tools." (protected — the values/beliefs keeper)
- First-person keepers (raw phrasing): "To reason about that, I built a small simulation called Democrasim. The emphasis belongs on *small*."; "I take the skeptics seriously enough to start from their side of the ledger."; "I want to be careful not to overclaim."

## Structural notes
- **Chapter job:** Use a deliberately-labeled toy model (Democrasim) to isolate one dynamic — that electoral outcomes track welfare only to the degree voters perceive policy impacts accurately — take the democratic skeptics (Achen/Bartels, Caplan) seriously, survey the mixed real-world evidence, position PolicyEngine as one accuracy-multiplying input (never a cure), separate values from beliefs, and reframe open policy analysis as democratic infrastructure.
- **Handoff in (from the opinion chapter):** a distribution of what people *think* is only an input; this chapter asks what a society *does* with those opinions — how it aggregates them into a decision.
- **Handoff out (15→16, to the values chapter):** the values/beliefs separation ("Values are for humans; facts are for tools") and the ground-truth contrast (Democrasim's invented "truth" vs the scoreboard's empirical form) set up the harder question of forecasting what people would value after reflection.
- **Phrasing constraints (hard):**
  - Democrasim stays a toy — never upgrade it to a validated or benchmarked system; its numbers illustrate, they do not report.
  - Sarah and the Candidate A/B scenario stay explicitly hypothetical with invented numbers.
  - Never claim information *fixes* democracy; the claim is bounded to the policy-evaluation slice ("one contributor," "the right size").
  - Keep the zero-resolved honesty: "None of those forecasts has resolved yet"; the point is that the perception problem *has* an empirical form, not that it has been scored.
  - RESOLVED (2026-07-11): the 35% ACA/Obamacare fact now cites [@dropp2017obamacare] (Dropp & Nyhan, NYT "The Upshot," 7 Feb 2017; Morning Consult, n≈2,000). Arrow 1951 publisher corrected to John Wiley (Cowles Monograph 12), not Yale.

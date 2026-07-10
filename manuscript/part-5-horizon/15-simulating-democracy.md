# Chapter 15: Simulating democracy

**Note to readers:** Democrasim, the model at the center of this chapter, is a toy — a thought experiment in code, built to make one relationship concrete enough to reason about, not to contribute to political science. It is not a validated production system like PolicyEngine, nor a benchmarked estimator like the opinion work of Chapter 14. It makes simplifying assumptions that political scientists would rightly criticize. Read it for intuition about information and democracy, not as established fact.

---

Why do democratic outcomes so often diverge from voter welfare? The question has occupied political scientists for decades, and their answers should humble anyone who expects better information tools to fix democracy.

Christopher Achen and Larry Bartels, in *Democracy for Realists* (2016), argued that the textbook story — informed citizens evaluate policies, pick the candidate whose platform fits their preferences, and elections translate public will into government — is largely fiction [@achen2016democracy]. In their telling, voters mostly choose parties by social identity and group loyalty, not by policy evaluation. They punish incumbents for droughts and other things no government controls. They reward growth that began before the incumbent took office. The "folk theory" of the rational, policy-weighing voter bears little resemblance to how democracy actually runs.

Bryan Caplan went further in *The Myth of the Rational Voter* (2007): voters aren't merely ignorant, they are *systematically biased* [@caplan2007myth]. Drawing on a survey that set the public's economic views beside professional economists', he identified four persistent distortions — anti-market, anti-foreign, make-work, and pessimistic bias. These are not random errors that cancel out in aggregation. They are directional, and they push democratic outcomes away from what most economists would call welfare-improving policy.

Against that backdrop, the question I want to explore is deliberately modest. Not whether information can fix democracy — it can't — but whether voter accuracy about policy impacts matters at the margin, and whether tools can improve it. I take the skeptics seriously enough to start from their side of the ledger: if identity and loyalty carry most of the vote, then anything an information tool can touch is, at best, a minority share of the decision. The argument of this chapter lives entirely inside that minority share, and it is careful never to claim more.

## The perception problem

Suppose a voter — call her Sarah. She teaches school, she has two kids, and she is choosing between two candidates with different platforms. One would expand the Child Tax Credit; the other would repeal the state income tax. Which leaves her family better off?

Without doing the arithmetic, Sarah has to guess. Maybe she has a vague sense that she pays state income tax and that it stings. Maybe she remembers the expanded credit during the pandemic and that it helped. Maybe she has heard talking heads argue both, each framing built to persuade rather than inform.

Her vote will be some blend of what she actually values, what she believes each policy would do, what her party and community support, and plain noise — a candidate's charisma, the morning's headlines, the weather. Even if her values are clear — say she cares most about her family's bottom line — her vote may not track them, because she cannot see the true impacts. She votes on a noisy signal.

Now multiply Sarah by a national electorate: each person deciding on imperfect perceptions, some biased one way and some the other, most well-informed about one issue and clueless about the next. The aggregate only roughly, noisily tracks what voters would choose if they could see clearly. Achen and Bartels would say this is too generous — that many voters aren't evaluating policy at all. Caplan would add that the ones who try are systematically wrong. I think both are partly right, and that the interesting question is narrower than either: to the extent *any* part of the vote is policy-driven, does the quality of that signal matter?

## A toy model

To reason about that, I built a small simulation called Democrasim. The emphasis belongs on *small*. Each simulated voter carries three things: a set of weighted preferences across policy dimensions — how much they care about the economy versus the environment versus social issues, which are their true values; an accuracy level, meaning how close their perception of a policy's effects sits to the truth; and a bias, a systematic lean beyond random noise, such as consistently overstating a tax burden or understating an environmental cost. Perceived impact is true impact plus noise plus bias, where the noise shrinks as accuracy rises. Voters compare candidates on perceived impacts weighted by their preferences, and the majority wins.

The question the model asks is simple: as voter accuracy varies, what happens to the welfare quality of who wins?

## What the model shows

The results are intuitive; putting numbers on them just sharpens the stakes. When accuracy is high, electoral outcomes track welfare — the candidate whose policies would actually improve voters' lives tends to win. When accuracy is low, the link frays; winners might have good policies or bad, because the signal is too corrupted to sort them. The model also shows something like a threshold. Below a certain accuracy, elections become essentially random with respect to welfare, bearing no reliable relationship to what would help voters; above it, the relationship strengthens quickly.

A hypothetical makes the mechanism visible. The numbers here are round and invented, chosen to illustrate rather than to report a calculation. Suppose Candidate A expands the Child Tax Credit and pays for it with a small rise in the top marginal rate, while Candidate B repeals the state income tax and pays for it by cutting food assistance. For a middle-income family with children and no food assistance, the credit expansion is worth more than the tax repeal, and the offsetting rate increase never reaches them — so they are better off under A, even though "repeal the income tax" is the phrase that sounds like the bigger deal. A voter perceiving accurately picks A; a voter perceiving through noise may well pick B, against her own interest. Scale that across an electorate and the pattern compounds: lower-income families do far better under A, upper-income families modestly better under B, and whether the election reflects that real distribution of gains depends on how much of the vote is signal rather than framing.

Bias bends outcomes a different way. If voters systematically overvalue tax cuts relative to equivalent benefit increases, elections will systematically favor tax-cutting candidates regardless of welfare — Caplan's point, reproduced in miniature.

I want to be careful not to overclaim. These results come from a model with extreme simplifications; real voters have identities, loyalties, and psychology that Democrasim ignores entirely, and it assumes voters are trying to maximize welfare through policy evaluation — the very folk theory Achen and Bartels dismantle. What it captures is one real dynamic: to the degree that *some* of the vote responds to perceived impacts, the quality of those perceptions matters. Even if only a fifth of the vote is policy-driven and the rest is identity, cleaning up that fifth still moves outcomes.

## What the evidence shows

Democrasim is a toy, but the question underneath it — does voter information quality change outcomes? — has been studied for real, and the evidence is mixed in a way that is itself informative.

Information sometimes moves votes, when it reaches people. In Brazil, Claudio Ferraz and Frederico Finan found that municipalities where federal corruption audits were released before an election punished corrupt incumbents at the polls — but the effect concentrated where local radio carried the results [@ferraz2008exposing]. Information that existed but did not travel changed nothing. Nonpartisan voter guides in the United States sit at the weaker end of this: they tend to raise political knowledge without much shifting vote choice, because in polarized settings most voters have already committed to a party. Arthur Lupia and Mathew McCubbins showed that voters lean on trusted-source shortcuts rather than full information anyway [@lupia1998democratic] — which cuts both ways, since a shortcut can approximate an informed choice or can simply entrench identity over evaluation.

The noise is not always innocent, either. One of the more robust findings in political communication is that accurate information and strategic misinformation do not compete on equal terms: a well-crafted misleading claim travels farther and sticks longer than a dry correction. Democrasim, by treating noise as random, actually understates the problem — in the real world some of that noise is engineered by people with an interest in distortion.

When information finally arrives as lived experience, it does register, though often at ruinous cost. In 2012, Kansas enacted large tax cuts its backers billed as a "real live experiment" in supply-side growth; independent analyses, of the kind PolicyEngine now produces, projected large shortfalls instead. The shortfalls came — years of budget crises and school-funding cuts, ending in a bipartisan reversal of the cuts in 2017. Voters did not need a simulation to learn the lesson; they paid for it in billions of dollars and lost services, over years, and better information infrastructure might at least have shortened that loop. The Affordable Care Act shows the subtler failure. As Chapter 3 described, the CBO got total coverage gains roughly right but badly missed the composition, overestimating exchange enrollment and underestimating Medicaid. Voters who opposed the law over predicted exchange disruption, and voters who backed it for Medicaid, both experienced something other than what they had been told, and the gap between perception and reality persisted for years. A 2017 survey found that about 35% of Americans did not know the ACA and "Obamacare" were the same law [NEEDS CITATION: Feb 2017 Morning Consult/NYT poll] — a failure of basic information transmission that no simulation can fix, but a fair measure of how far real voter knowledge sits from the idealized version.

Some limits no information tool touches at all. Kenneth Arrow's impossibility theorem (1951) proved that no ranked voting system can satisfy a short list of reasonable fairness conditions at once [@arrow1951social]; Gibbard and Satterthwaite showed that any non-dictatorial system can be gamed by strategic voting. Better inputs do not repeal those constraints. The honest summary is that better voter information is necessary but nowhere near sufficient: it is one lever among identity, institutions, and strategy, and the only one that infrastructure can move directly rather than through the slow work of changing culture.

## The perception problem, against ground truth

Democrasim can only toy with the perception problem because it has no ground truth to check itself against — its voters misperceive a policy's effects, but the "true" effects are just more numbers the model invented. Chapter 13 described the version of this problem that does terminate in ground truth: forecasting a government metric under a policy counterfactual — what the unemployment rate will actually print next quarter, or how long a Medicaid call-center wait will run in a given month if a work-requirement deadline slips — and grading the forecast when the official number lands [@thesisinstitute2026]. That is the accuracy question Democrasim only gestures at, lifted out of the toy and onto a public docket where reality settles it. The difference is the whole difference between a thought experiment and a measurement: one grades itself against numbers it made up, the other waits to be graded by numbers it did not. None of those forecasts has resolved yet; the point is not that the empirical version has been scored, but that the perception problem has an empirical form at all.

## PolicyEngine as one input

This is where a tool like PolicyEngine becomes democratically relevant — not as a cure for democratic dysfunction, but as one input among many. Instead of "the average family pays X," it computes what a specific household, with its actual circumstances, would pay or receive under a given policy. It is free to anyone with a browser. And its transparency is no longer just a claim about open-source code: the rules it applies are open encodings, checked against reference calculators — the verification machinery of Chapter 10 — which is a stronger warrant than "inspect the source if you like" ever offered.

In Democrasim's vocabulary, that makes PolicyEngine an accuracy multiplier for the policy-evaluation slice of a vote. It moves a voter from "I sense this would hurt me" to "this changes my household's income by roughly this much." For Sarah, it turns the guess between the credit and the tax repeal into a number she can see. It does nothing for the identity-driven part of her vote, does not override party loyalty, and does not resolve Arrow's problem in the voting rule itself. It removes one source of noise from one channel. That is a smaller claim than "informed voters fix democracy," and it is the right size.

## Futarchy, and a separation

There is a more radical proposal for wiring information into governance: Robin Hanson's *futarchy* [@hanson2013futarchy]. Its slogan is "vote on values, but bet on beliefs." Democratic processes decide *what we care about* — a welfare metric, a child-poverty rate — and prediction markets decide *which policies achieve it*. A legislature proposes a bill; markets price the welfare metric conditional on passage versus failure; if the market says welfare is higher with the bill, it becomes law [@hanson2000futarchy].

No democracy has adopted it, for reasons that are easy to see: markets can be manipulated by deep pockets, most policy questions never draw enough trading to price reliably, "welfare" is contested to define, and legitimacy depends partly on citizens feeling heard, which a price does not supply. But the thought experiment isolates the distinction that matters here — between values, the outcomes we want, and beliefs, the policies that would produce them. PolicyEngine works the beliefs side; it never tells anyone what to want. Neither does Democrasim.

Values are for humans; facts are for tools.

## Objections

The accuracy-and-welfare framing oversimplifies real democratic life, and four objections deserve a straight answer.

**Maybe the preferences are the problem, not the perceptions.** Perhaps voters perceive fine and simply want policies that harm others. True — but orthogonal. If voters want harmful things and perceive accurately, they get harmful things; that is a different failure from wanting good things and misperceiving. Better perception at least delivers people what they actually want, which is the precondition for holding them responsible for it.

**Information won't reach the disengaged.** People who do not vote will not open a policy calculator either, and the ones who would are already relatively informed. Partly true. But new modalities — an AI assistant that volunteers a policy's household impact, a calculation embedded where people already are — can reach past the self-selected few, and moving the moderately informed to well-informed still improves the signal.

**Calculated self-interest isn't good citizenship.** Democracy might want voters weighing the common good, not just their own household. Fair — and PolicyEngine computes societal impacts too: poverty rates, inequality, total cost. The point is not selfishness; it is replacing perception with calculation, whatever a voter chooses to weigh.

**Arrow's theorem means none of this matters.** No system aggregates preferences perfectly, so why polish the inputs? Because Arrow constrains the *mechanism*, not the quality of what feeds it. An imperfect aggregator still yields better outcomes from better-informed inputs. Arrow proved no perfect system exists; he did not prove every system is equally good regardless of what goes in.

## The democratic case for open infrastructure

The argument, then, is bounded on every side, and stronger for it. Democratic outcomes track voter welfare only to the degree voters perceive policy impacts accurately — and that is one factor beside identity, institutions, and strategy. Most voters perceive those impacts poorly, through noise and bias and thin information. Tools exist that can sharpen the policy-evaluation slice of the decision. So investing in accessible, trustworthy policy analysis has civic value beyond any one person's tax optimization — not as a fix for democracy, but as one contributor to informed self-government.

That reframes what PolicyEngine is for. Not a calculator for people who want to trim their taxes, but one component, among many, of democratic infrastructure.

## References

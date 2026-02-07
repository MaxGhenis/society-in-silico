# Chapter 13: Simulating democracy

**Note to readers**: This chapter describes theoretical research, not validated tools. Democrasim is a toy model—a thought experiment in code designed to explore how voter information might affect democratic outcomes. Unlike PolicyEngine (a validated production system) or HiveSight (a preliminary prototype with some empirical grounding), Democrasim makes simplifying assumptions that real political scientists would rightly criticize. Use this chapter to understand intuitions about information and democracy, not as established political science.

---

Why do democratic outcomes often diverge from voter welfare?

It's a question that has occupied political scientists for decades—and the answers they've found should humble anyone who thinks better information tools will fix democracy.

Christopher Achen and Larry Bartels, in their landmark *Democracy for Realists* (2016), argued that the standard story about democracy—informed citizens evaluate policies, choose candidates whose platforms best match their preferences, and elections translate public will into governance—is largely fiction {cite}`achen2016democracy`. In their analysis, voters mostly choose parties based on social identities and group loyalties, not policy evaluation. They punish incumbents for bad weather. They reward them for economic growth that preceded their term. The "folk theory" of rational, policy-evaluating voters bears little resemblance to how democracy actually functions.

Bryan Caplan pushed further in *The Myth of the Rational Voter* (2007), arguing that voters aren't just ignorant but *systematically biased* {cite}`caplan2007myth`. Using data from the Survey of Americans and Economists on the Economy, he identified four persistent biases: anti-market bias, anti-foreign bias, make-work bias, and pessimistic bias. These aren't random errors that cancel out in aggregation. They're directional distortions that push democratic outcomes away from what economists would consider welfare-maximizing policies.

Against this backdrop, the question I want to explore is more modest: *To what extent does voter accuracy about policy impacts matter for democratic outcomes—and can simulation tools improve it?*

---

## The perception problem

Consider a voter named Sarah. She's 42, works as a teacher, earns $65,000 a year, has two kids, and lives in Ohio. She's deciding between candidates with different policy platforms.

Candidate A proposes expanding the Child Tax Credit by $1,000 per child. Candidate B proposes eliminating the state income tax. Which would benefit Sarah more?

Without calculation, Sarah has to guess. Maybe she has a vague sense that she pays state income tax and that feels painful. Maybe she remembers the expanded CTC during COVID and it felt helpful. Maybe she's heard talking heads argue about either policy, each framing designed to persuade rather than inform.

Her choice will be some combination of:
- Her actual policy preferences (what she values)
- Her perceived policy impacts (what she thinks would happen)
- Identity and group loyalty (what her party, community, or social circle supports)
- Noise (irrelevant factors—candidate charisma, recent weather, what was on the news this morning)

Even if Sarah has clear preferences—say, she cares most about maximizing her family's resources—her vote may not reflect those preferences because she can't perceive the true policy impacts. She votes with a noisy signal.

Now multiply this by 150 million voters. Each making decisions based on imperfect perceptions. Some biased left, some biased right. Some well-informed about economics but clueless about environment. The aggregate result: democratic outcomes that only roughly, noisily track what voters actually want.

Achen and Bartels would argue this understates the problem—that many voters aren't even trying to evaluate policies at all. Caplan would add that those who do try are systematically wrong. I think they're both partly right. And I think the interesting question isn't whether information alone can fix democracy—it can't—but whether better information tools can improve the signal, even at the margins.

---

## A toy model

To explore this intuition, I've built a toy model called Democrasim. I emphasize "toy"—this is not a contribution to political science. It's a thought experiment in code, a way to make the relationship between voter information and outcomes concrete enough to reason about.

Each simulated voter has:

**Weighted preferences** across policy dimensions. One voter might care 50% about economic issues, 30% about social issues, 20% about environment. These are the true values—what voters actually care about.

**Accuracy.** How well voters perceive actual policy impacts. High accuracy means perceiving close to truth. Low accuracy means perceiving through heavy noise.

**Bias.** Systematic distortions beyond random noise. A voter might consistently underestimate environmental costs or overestimate tax burden.

The perception model is simple:

```
perceived_impact = true_impact + noise + bias
```

Where the noise term scales inversely with accuracy. Elections work through utility maximization: each voter evaluates candidates based on perceived impacts weighted by preferences. Most votes wins.

The question Democrasim asks: What happens to welfare outcomes as voter accuracy varies?

---

## What the model shows

The results are intuitive, but putting numbers on them clarifies the stakes.

When accuracy is high—voters perceive close to true policy impacts—electoral outcomes track welfare. The candidate whose policies would actually improve voter lives tends to win. When accuracy is low—voters perceive through heavy noise—the connection frays. Winners might have good policies or bad ones; the signal is too corrupted to reliably select the beneficial option.

There appears to be a threshold effect. Below a certain level of voter accuracy, democracy becomes essentially random with respect to policy welfare—electoral outcomes bear no meaningful relationship to what would actually benefit voters. Above that threshold, the relationship strengthens rapidly.

Consider a concrete scenario. Two candidates propose different approaches to family policy. Candidate A would expand the Child Tax Credit by $2,000 per child and fund it by raising the top marginal rate from 37% to 39%. Candidate B would eliminate the state income tax, funded by cutting SNAP benefits by 30%.

For Sarah, the Ohio teacher earning $65,000 with two kids: Candidate A's plan increases her family income by approximately $4,000 through the CTC expansion, while the top-rate increase doesn't affect her at all. Candidate B's plan saves her roughly $2,500 in state taxes, but since she doesn't receive SNAP, the benefit cuts don't directly affect her either. She's $1,500 better off under Candidate A.

But without running the numbers, Sarah might perceive differently. "Eliminating the state income tax" sounds dramatic—surely that's a bigger deal than a credit increase? If her accuracy is low, she might vote for Candidate B, against her own financial interest. If her accuracy is high—perhaps because she used a policy calculator—she'd recognize that $4,000 in CTC expansion outweighs $2,500 in state tax savings for her specific situation.

Now scale this across the electorate. Low-income families are dramatically better off under Candidate A (the CTC expansion helps them, and the SNAP cuts under Candidate B would devastate them). Upper-income families are modestly better off under Candidate B. With high voter accuracy, the election outcome reflects the actual distribution of gains and losses. With low accuracy, the outcome depends on which candidate's framing is more persuasive—and framing has nothing to do with true impact.

Bias introduces a different distortion. If voters systematically underestimate certain costs or overestimate certain benefits, elections will systematically favor policies that exploit those biases, regardless of actual welfare impact. This echoes Caplan's finding about systematic rather than random voter errors. In the model, anti-tax bias—voters perceiving tax cuts as more valuable than equivalent benefit increases—consistently distorts outcomes in favor of tax-cutting candidates, even when the benefit-expanding candidate would improve welfare for the median voter.

I want to be careful about overclaiming. These results come from a model with extreme simplifications. Real voters have identity attachments, party loyalties, and psychological dynamics that Democrasim ignores entirely. The model assumes voters are trying to maximize welfare through policy evaluation—exactly the "folk theory" that Achen and Bartels argue is wrong for most voters.

But the model captures one real dynamic: *to the extent that some portion of voting behavior is influenced by perceived policy impacts, the quality of those perceptions matters.* Even if only 20% of the vote is policy-driven and 80% is identity-driven, improving the signal quality of that 20% still shifts outcomes.

---

## What the real-world evidence shows

Democrasim is a toy model, but the question it poses—does voter information quality affect outcomes?—has been studied empirically.

The evidence is mixed, which is itself informative.

**Information provision experiments** have shown modest but real effects. When researchers in developing countries provided voters with candidate report cards—scorecards showing incumbents' performance on corruption, public spending, or economic outcomes—voting patterns shifted. In Brazil, Ferraz and Finan (2008) found that municipalities where corruption audit results were publicly disclosed before elections saw corrupt incumbents punished at the polls. The effect was concentrated where local media covered the disclosures—information that existed but didn't reach voters had no effect.

**Voter guide experiments** in the United States have shown smaller effects. When nonpartisan voter guides are distributed, they tend to increase political knowledge without dramatically changing vote choices. The reason: in highly partisan environments, most voters have already committed to a party identity, and additional policy information rarely overrides that commitment. This is Achen and Bartels's point: identity dominates evaluation.

**The persuasion asymmetry.** One of the more robust findings in political communication research is that accurate information and strategic misinformation don't compete on equal terms. A carefully crafted misleading claim can travel further and stick longer than a dry factual correction. Democrasim, by assuming unbiased noise, actually understates the real challenge: in practice, the noise isn't random—it's partially engineered by actors with incentives to distort perceptions.

**The Kansas experiment.** In 2012, Kansas Governor Sam Brownback implemented large tax cuts that he described as a "real live experiment" in supply-side economics. The Tax Foundation and other groups projected economic growth that would offset revenue losses. Independent analysis—including models comparable to what PolicyEngine produces—projected large revenue shortfalls. The independent models proved correct: Kansas faced years of budget crises, school funding cuts, and ultimately a bipartisan reversal of the tax cuts in 2017. Voters didn't need a simulation to learn the lesson—they experienced it. But the experience cost the state billions of dollars and years of disrupted public services. Better information infrastructure might have shortened the feedback loop.

The pattern: voter information tools don't fix democracy by themselves. They work best when combined with media coverage, institutional accountability, and genuine voter interest in policy evaluation. They work least in highly polarized environments where identity dominates evaluation. And they face organized opposition from actors who benefit from voter confusion.

Democrasim captures the information channel in isolation. Reality involves that channel operating alongside—and often overwhelmed by—identity, emotion, and strategic communication. The case for better information tools isn't that they're sufficient. It's that they're one of the few levers that can be improved through infrastructure rather than through the much harder work of changing culture.

---

## What political science actually says

Democrasim's intuitions align with some findings in political science and contradict others.

**Supporting evidence:** Arthur Lupia and Mathew McCubbins showed that voters can use "information shortcuts"—cues from trusted sources—to make decisions that approximate what they'd choose with full information {cite}`lupia1998democratic`. This suggests that the gap between actual and optimal voter behavior is partially an information problem, and that better information delivery could narrow it.

**Complicating evidence:** Achen and Bartels found that even well-informed voters often vote based on group identity rather than policy evaluation {cite}`achen2016democracy`. More information doesn't automatically produce more policy-responsive voting if the information is filtered through partisan lenses. A voter who uses PolicyEngine to calculate that Policy X would save her $2,000 might still vote against it if her party opposes it.

**Fundamental constraints:** Kenneth Arrow's impossibility theorem (1951) proved that no ranked voting system can simultaneously satisfy a small set of reasonable fairness conditions {cite}`arrow1951social`. No amount of voter information resolves this mathematical constraint on aggregating preferences. Gibbard and Satterthwaite independently showed that any non-dictatorial voting system is susceptible to strategic manipulation. Simulation tools might improve sincere voting but don't address strategic voting.

The honest assessment: better voter information is a *necessary but not sufficient* condition for democratic outcomes to track voter welfare. Democrasim isolates the information channel and shows it matters. Real democracy has many other channels—identity, strategy, institutional design—that also matter, and that information tools can't directly address.

---

## The PolicyEngine connection

This is where tools like PolicyEngine become democratically relevant—not as a solution to democratic dysfunction, but as one input among many.

Consider what PolicyEngine offers:
- **Personalized calculation**: Not "the average family pays X" but "your family, with your specific circumstances, would pay/receive Y under this policy."
- **Transparent methodology**: Open-source code anyone can inspect. No hidden assumptions or ideological bias baked in.
- **Instant access**: Free, available to anyone with a web browser.

In Democrasim's terms, PolicyEngine is an accuracy multiplier for the policy-evaluation component of voting. It takes voters from "I vaguely sense this policy would hurt/help me" to "I calculated that this policy would change my household income by $X."

The voter Sarah we met earlier? Instead of guessing whether the CTC expansion or state tax elimination benefits her more, she could enter her household details and see the numbers directly. Now she has signal, not noise—at least for this one dimension of her decision.

This doesn't address the identity-driven components of her vote. It doesn't override party loyalty. It doesn't resolve Arrow-type impossibilities in the voting system itself. But it removes one source of noise from one channel of democratic feedback.

---

## Futarchy and the values-beliefs separation

There's a more radical proposal for connecting information to governance: Robin Hanson's *futarchy* {cite}`hanson2013futarchy`.

The core idea: "Vote on values, but bet on beliefs." Democratic processes determine *what we care about*—national welfare metrics, child poverty rates, median income. But *which policies achieve those goals* is determined by prediction markets, not politicians or voters.

A legislature proposes a bill. Prediction markets open on welfare conditional on the bill passing versus failing. If the market says welfare will be higher with the bill, it becomes law {cite}`hanson2000futarchy`.

Despite its elegance, futarchy faces practical objections that explain why no democracy has adopted it. Markets can be manipulated by wealthy actors. Most policy questions don't attract enough trading volume for reliable price discovery. Defining and measuring "welfare" is contentious. And democratic legitimacy depends partly on citizens feeling they had a voice—market-based decisions may lack that psychological buy-in.

But the futarchy thought experiment clarifies something important: the distinction between *values* (what outcomes we want) and *beliefs* (what policies produce those outcomes). PolicyEngine addresses the beliefs side—it helps voters understand what policies would actually do. It doesn't tell them what to value. Neither does Democrasim.

This separation—values are for humans, facts are for tools—underlies the democratic case for simulation infrastructure.

---

## Objections

The accuracy-welfare model oversimplifies real democratic complexity. These objections deserve engagement.

**Objection: Preferences themselves are the problem.**

Maybe voters don't just perceive poorly—they have bad preferences. They want policies that harm others. They vote from spite rather than self-interest.

Response: True, but orthogonal to the information question. If voters want harmful policies and perceive accurately, they'll get harmful policies. That's a different problem than wanting beneficial policies but perceiving poorly. Better perception at least ensures voters get what they want, even if what they want is bad.

**Objection: Information won't reach the disengaged.**

People who don't vote probably wouldn't use policy calculators either. The voters who would use PolicyEngine are already relatively informed.

Response: Partially true. But new modalities—AI assistants that proactively explain policy impacts, social media tools that embed calculations, voter guides that personalize information—may reach populations that wouldn't seek out a policy calculator. And moving moderately-informed voters to well-informed still improves signal quality.

**Objection: Calculated self-interest isn't good citizenship.**

Democracy might benefit from voters considering communal welfare, not just personal impact.

Response: PolicyEngine can calculate societal impacts too—poverty rates, inequality measures, total cost. The point isn't selfishness. It's replacing perception with calculation, whatever voters choose to calculate.

**Objection: Arrow's theorem means this doesn't matter.**

No voting system can perfectly aggregate preferences, so improving information at the individual level can't fix the aggregation problem.

Response: Arrow's theorem constrains the voting *mechanism*, not the quality of individual decisions. Even an imperfect aggregation mechanism produces better outcomes when it aggregates better-informed inputs. Arrow proved no perfect system exists; he didn't prove that all systems are equally good regardless of input quality.

---

## The democratic case for open infrastructure

The argument crystallizes:

**Premise 1**: Democratic outcomes track voter welfare only to the extent voters accurately perceive policy impacts—and this is one of several factors, alongside identity, institutions, and strategic behavior.

**Premise 2**: Most voters perceive policy impacts poorly—through noise, bias, and inadequate information.

**Premise 3**: Tools exist that could improve voter perception accuracy for the policy-evaluation component of voting.

**Conclusion**: Investing in accessible, trustworthy policy analysis tools has democratic value beyond individual utility—not as a complete fix, but as one contributor to informed self-governance.

This reframes PolicyEngine's mission. It's not just "a useful calculator for nerds who want to optimize their taxes." It's a component—one component among many—of democratic infrastructure.

---

## References

```{bibliography}
:filter: docname in docnames
```

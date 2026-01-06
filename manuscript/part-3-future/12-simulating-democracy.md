# Chapter 12: Simulating Democracy

**Note to readers**: This chapter describes theoretical research, not validated tools. Democrasim is a toy model—a thought experiment in code designed to explore how voter information might affect democratic outcomes. Unlike PolicyEngine (a validated production system) or HiveSight (a preliminary prototype with some empirical validation), Democrasim makes simplifying assumptions that real political scientists would rightly criticize. Use this chapter to understand intuitions about information and democracy, not as established political science.

---

Why do democratic outcomes often diverge from voter welfare?

It's a puzzle that has occupied political scientists for decades. We have mechanisms—elections—designed to translate public preferences into policy. We have representatives whose job is to understand what constituents want. We have a free press, public education, and more access to information than any previous generation.

And yet: policies regularly fail to reflect what would actually benefit voters. Reforms pass that help some constituents while harming others in unexpected ways. Ballot measures with popular support produce unintended consequences. Policies that poll well in the abstract create implementation challenges that reduce their actual impact.

The standard explanations point to special interests, gerrymandering, and media manipulation. These matter. But there's a more fundamental problem hiding in plain sight.

*Voters don't know what policies would actually do for them.*

---

## The Perception Problem

Consider a voter named Sarah. She's 42, works as a teacher, earns $65,000 a year, has two kids, and lives in Ohio. She's deciding between candidates with different policy platforms.

Candidate A proposes expanding the Child Tax Credit by $1,000 per child. Candidate B proposes eliminating the state income tax. Which would benefit Sarah more?

Without calculation, Sarah has to guess. Maybe she has a vague sense that she pays state income tax and that feels painful. Maybe she remembers the expanded CTC during COVID and it felt helpful. Maybe she's heard talking heads argue about either policy on cable news, each spin designed to persuade rather than inform.

Her choice will be some combination of:
- Her actual policy preferences (what she values)
- Her perceived policy impacts (what she thinks would happen)
- Noise (irrelevant factors that shouldn't matter but do)

Even if Sarah has clear preferences—say, she cares most about maximizing her family's resources—her vote may not reflect those preferences because she can't perceive the true policy impacts. She votes with a noisy signal.

Now multiply this by 150 million voters. Each making decisions based on imperfect perceptions. Some biased left, some biased right. Some well-informed about economics but clueless about environment. Some sophisticated about tax policy but misunderstanding healthcare.

The aggregate result: democratic outcomes that only roughly, noisily track what voters actually want.

---

## Modeling the Noise

To explore this idea, I've built a toy model called Democrasim. It's not a validated research tool—it's a thought experiment in code, a way to reason about how voter information affects democratic outcomes. The model makes simplifying assumptions that real political scientists would rightly criticize. But it helps clarify the intuition.

Democrasim simulates the full chain from voter cognition to electoral outcomes to welfare.

Each simulated voter has:

**Weighted preferences** across policy dimensions. One voter might care 50% about economic issues, 30% about social issues, 20% about environment. Another might weight them 20/40/40. These are the true values—what voters actually care about.

**Accuracy**. How well voters perceive actual policy impacts. High accuracy means perceiving close to truth. Low accuracy means perceiving through heavy noise.

**Bias**. Systematic distortions beyond random noise. A voter might consistently underestimate environmental costs or overestimate tax burden.

**Turnout probability**. Whether they vote at all.

The perception model is simple:

```
perceived_impact = true_impact + noise + bias
```

Where the noise term scales inversely with accuracy. A voter with accuracy 0.8 perceives policy impacts with less noise than one with accuracy 0.2.

Elections work through straightforward utility maximization. Each voter evaluates candidates based on perceived impacts weighted by preferences. The candidate with highest perceived utility gets their vote. Most votes wins.

The question Democrasim asks: What happens to welfare outcomes when voter accuracy varies?

---

## The Accuracy-Welfare Connection

The simulation results are intuitive but their magnitude is striking.

When accuracy is high—voters perceive close to true policy impacts—electoral outcomes track welfare. The candidate whose policies would actually improve voter lives tends to win.

When accuracy is low—voters perceive through heavy noise—the connection frays. Winners might have good policies or bad ones; the signal is too corrupted to reliably select the beneficial option.

Bias introduces a different distortion. If voters systematically underestimate certain costs or overestimate certain benefits, elections will systematically favor policies that exploit those biases, regardless of actual welfare impact.

The threshold matters. There appears to be a level of voter accuracy below which democracy becomes essentially random—electoral outcomes bear no meaningful relationship to what would actually benefit voters. Above that threshold, the relationship strengthens.

This has implications for anyone who cares about democratic function.

---

## What Determines Accuracy?

If voter accuracy drives welfare outcomes, what determines accuracy?

**Information availability**. Can voters access relevant data about policy impacts? Or is analysis locked behind paywalls, jargon, and institutional barriers?

**Information quality**. Is available information designed to inform or to persuade? Think tanks with ideological agendas produce analysis, but it's systematically biased.

**Cognitive load**. Even with good information, understanding policy impacts requires effort. Busy people with jobs, families, and finite attention can't spend hours analyzing every ballot measure.

**Trust**. When institutions have been wrong before—or are perceived as biased—voters rationally discount their claims. Even accurate information gets filtered through skepticism.

This explains why throwing more information at voters doesn't automatically help. A 200-page CBO report is technically available; it doesn't mean voters absorb it. Opposing partisan analyses might both be available; voters can't adjudicate between them.

What would actually improve accuracy? Not just more information, but *accessible*, *trustworthy*, *personalized* information about policy impacts.

---

## The PolicyEngine Connection

This is where tools like PolicyEngine become democratically significant.

Consider what PolicyEngine offers:
- **Personalized calculation**: Not "the average family pays X" but "your family, with your specific circumstances, would pay/receive Y under this policy."
- **Transparent methodology**: Open source code anyone can inspect. No hidden assumptions or ideological bias baked in.
- **Instant access**: Free, available to anyone with a web browser. No need to trust intermediaries.

In Democrasim terms, PolicyEngine is an accuracy multiplier. It takes voters from "I vaguely sense this policy would hurt/help me" to "I calculated that this policy would change my household income by $X."

The voter Sarah we met earlier? Instead of guessing whether the CTC expansion or state tax elimination benefits her more, she could enter her household details and see: CTC expansion would give her $2,000; state tax elimination would save her $1,400. Now she has signal, not noise.

Multiply this across millions of voters. Each with clearer perception of actual policy impacts. The aggregate result: elections that more reliably track voter welfare.

This is the democratic case for open microsimulation. It's not just about individual convenience—though that matters. It's about improving the signal quality of democratic feedback loops.

---

## Closing the Loop

Democrasim suggests a research program: connect simulation tools to model the full democratic cycle.

**Step 1**: Candidates have policy platforms. Not vague promises, but specific proposals. "Expand CTC by $500 per child" or "Replace income tax with consumption tax."

**Step 2**: PolicyEngine calculates actual impacts on voter households. Given a representative sample of households, we know the distribution of effects—who gains, who loses, by how much.

**Step 3**: Voters with varying accuracy perceive these impacts. High-accuracy voters perceive close to truth. Low-accuracy voters perceive through noise and bias.

**Step 4**: Votes aggregate to determine the winner.

**Step 5**: PolicyEngine calculates welfare outcomes under the winning policy.

This closed loop lets us ask questions like: What level of voter accuracy is needed for democratic outcomes to track welfare? How do different interventions compare? Does uncertainty systematically favor certain policy types?

Playing with the model—and I emphasize "playing," not "researching"—suggests an intuition: accuracy interventions might matter more than turnout interventions. If the toy model's logic holds, getting low-information voters to perceive better may matter more than getting non-voters to vote. An uninformed vote adds noise; an informed vote adds signal.

Whether this intuition survives contact with real political science is unknown. The model is too simple to make confident claims. Real voter behavior involves identity, tribal loyalty, strategic considerations, and psychological factors that Democrasim ignores entirely. But as a way to reason about why accurate policy information might have democratic value, it's useful.

---

## The Democratic Case for Open Infrastructure

The argument crystallizes:

**Premise 1**: Democratic outcomes track voter welfare only to the extent voters accurately perceive policy impacts.

**Premise 2**: Most voters perceive policy impacts poorly—through noise, bias, and inadequate information.

**Premise 3**: Tools exist that could dramatically improve voter perception accuracy.

**Conclusion**: Investing in accessible, trustworthy policy analysis tools has democratic value beyond individual utility. It's infrastructure for informed self-governance.

This reframes PolicyEngine's mission. It's not just "a useful calculator for nerds who want to optimize their taxes." It's "infrastructure that helps democracy work as intended."

The philanthropic implications are significant. A dollar spent making policy analysis accessible might have higher democratic return than a dollar spent on get-out-the-vote campaigns. Both matter, but one addresses signal quality while the other addresses signal quantity.

---

## Simulating Democratic Scenarios

Democrasim enables scenario analysis for democratic reform.

**Scenario: Universal Policy Calculators**

What if every voter had access to PolicyEngine-style tools and actually used them? Accuracy doubles. Simulations show electoral outcomes significantly closer to welfare-optimal policies.

**Scenario: Improved Civics Education**

What if schools taught policy analysis skills? Accuracy increases modestly. Smaller effect because skills without accessible tools still leave voters unable to calculate.

**Scenario: Reduced Media Bias**

What if news coverage focused on policy impacts rather than horse races? Bias decreases. Accuracy unchanged. Outcomes improve for bias-sensitive questions but not noise-sensitive ones.

**Scenario: AI Policy Advisors**

What if every voter had an AI assistant that could answer "how would Policy X affect me?" based on their circumstances and reliable models? This is accuracy approaching 1.0. Electoral outcomes closely track welfare.

This last scenario isn't science fiction. As we explored with Cosilico, AI systems can already use PolicyEngine to answer household-specific policy questions. The barrier is deployment, not capability.

---

## Futarchy: Vote Values, Bet Beliefs

There's a more radical proposal for connecting information to governance: Robin Hanson's *futarchy* {cite}`hanson2013futarchy`.

The core idea is captured in a slogan: "Vote on values, but bet on beliefs."

Under futarchy, democratic processes still determine *what we care about*—a measure of national welfare, say, or specific metrics like child poverty rates and median income. But *which policies achieve those goals* is determined by prediction markets, not politicians.

Here's how it would work. A legislature proposes a bill. Prediction markets open on national welfare conditional on the bill passing versus failing. If the market says welfare will be higher with the bill than without, it becomes law. If not, it doesn't.

The logic is that markets aggregate information better than deliberation {cite}`hanson2000futarchy`. Traders with relevant knowledge profit by pushing prices toward truth. Ideologues who let conviction override evidence lose money. The market converges on the best available estimate of policy effects.

This sounds extreme. But the underlying mechanism—separating values from facts—clarifies what simulation tools actually do.

PolicyEngine answers factual questions: "What would happen to child poverty if we passed Policy X?" Prediction markets can answer similar questions: "Given Policy X, what do informed bettors expect to happen to child poverty?"

Both separate the *empirical* question (what would happen?) from the *normative* question (is that outcome good?). Democrasim's accuracy-welfare model makes the same distinction: voters have preferences (values), and they perceive policy impacts (facts). Better fact-perception improves the connection between voting and welfare.

### Personal Futarchy

The futarchy framework applies at individual scale too.

I've built a tool called Farness that implements "personal futarchy" for decisions {cite}`ghenis2024farness`. Instead of asking "should I take the new job?" it structures the decision into:

1. **KPIs** (values): What outcomes do I actually care about? Income, satisfaction, work-life balance?
2. **Options**: What are all the choices, including ones I haven't considered?
3. **Forecasts** (beliefs): For each option, what's my prediction for each KPI—with confidence intervals?

The discipline of making explicit numeric forecasts—rather than vague intuitions about what "feels right"—mirrors futarchy's bet-on-beliefs principle. The calibration tracking mirrors prediction market scoring: over time, you learn whether your forecasts are systematically biased.

The connection to this chapter is direct. If a voter could run Farness on "how should I vote on Proposition 12?"—defining KPIs (household income, public services, equity), forecasting each candidate's impact on those KPIs—their vote would contain more signal.

### Why Not Full Futarchy?

Despite its elegance, futarchy faces practical objections that explain why no democracy has adopted it:

**Manipulation**: Can wealthy actors move market prices to get their preferred policies passed? Hanson argues proper market design prevents this, but the concern persists.

**Thin markets**: Most policy questions don't attract enough trading volume for reliable price discovery. Polymarket works for presidential elections with billions wagered; it's less clear how it would work for zoning amendments.

**Conditional complexity**: Markets on "welfare if Policy X passes" require defining welfare, measuring it, and handling the counterfactual. These are hard problems.

**Democratic legitimacy**: People accept losing elections because they had a vote. Would they accept losing market-based decisions? The psychology of legitimacy matters.

Still, the futarchy thought experiment illuminates what democratic information infrastructure could do. Even without replacing elections, we can build tools that help voters bet on beliefs more rigorously—and calibrate those beliefs against outcomes.

---

## Objections and Complications

The accuracy-welfare model simplifies real democratic complexity.

**Objection: Preferences themselves are the problem.**

Maybe voters don't just perceive poorly—they have bad preferences. They want policies that harm others. They vote from spite rather than self-interest.

Response: True, but orthogonal. If voters want harmful policies and perceive accurately, they'll get harmful policies. That's a different problem than wanting beneficial policies but perceiving poorly. Better perception at least ensures voters get what they want, even if what they want is bad.

**Objection: Information won't reach the disengaged.**

People who don't vote probably wouldn't use policy calculators either. The voters who would use PolicyEngine already vote and may already be relatively informed.

Response: Partially true, but the marginal effect still matters. Moving moderately-informed voters to well-informed improves signal quality. And new modalities (AI assistants, social sharing) may reach previously disengaged populations.

**Objection: Calculated self-interest isn't the same as good citizenship.**

Democracy might benefit from voters considering communal welfare, not just personal impact.

Response: True, and PolicyEngine can calculate societal impacts too. The point isn't selfishness—it's replacing perception with calculation, whatever voters choose to calculate.

---

## The Vision

Imagine a voter in 2030.

She's considering a ballot measure to reform her state's tax code. Instead of reading dueling op-eds and trying to guess who's lying, she opens a policy analysis app on her phone.

"Show me how Proposition 12 would affect my household."

The app—powered by something like PolicyEngine, accessed through something like Cosilico's AI layer—returns: "Based on your household profile, this measure would reduce your state taxes by $340 per year. The trade-off is reduced funding for public education, which your children use. The net welfare impact for your household is approximately..."

She might not accept the calculation blindly. She might weigh factors the app doesn't capture. But she starts from signal, not noise.

Now she considers communal impacts. "How would this affect households statewide?"

The app shows distributions: "Households earning over $200,000 receive average benefits of $2,400. Households earning under $50,000 see average benefit of $80. Total revenue reduction of $2.1 billion..."

This voter can make an informed choice—not because she's smarter or more educated, but because she has tools that convert policy proposals into understandable impacts.

Across millions of such voters, elections become more responsive to actual preferences. Democracy functions closer to its ideal.

---

The simulation has limits. Democrasim doesn't capture cultural dynamics, identity politics, or the psychology of tribal belonging. Voters aren't just utility-maximizing calculators.

But the core insight holds: to the extent democracy is *supposed* to translate preferences into outcomes, it needs voters who can perceive what outcomes would actually result from different choices.

Open microsimulation is infrastructure for that perception. PolicyEngine isn't just a tax calculator. It's a component of democratic signal processing.

The code simulates policies. But what we're really simulating is the possibility of informed self-governance.


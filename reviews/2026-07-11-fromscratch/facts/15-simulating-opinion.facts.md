# Fact catalog — Chapter 14: Simulating opinion
Source: `manuscript/part-4-prediction/14-simulating-opinion.md`. Target chapter number in rewrite: 15. Raw material for a from-scratch rewrite; paraphrased except where marked Quotes/Author-texture.

## Facts

### The opening case (Argyle et al.)
- In 2023 a paper titled "Out of One, Many: Using Language Models to Simulate Human Samples" appeared [@argyle2023out].
- Researchers at Brigham Young University asked GPT-3 to adopt specific demographic personas (examples given: a 65-year-old Black woman from Mississippi; a 28-year-old white man from Oregon) and answer survey questions, then compared the model's answers to real survey data.
- Conditioned carefully on demographics, the model tracked human voting patterns across the 2012, 2016, and 2020 presidential elections; captured the partisan divide by education; reproduced regional variation.
- The question it opened: having simulated how policies move through households, could we simulate what households *think* about those policies?

### The emerging field (an argument from the start)
- **Optimists.** Mei and colleagues found that GPT-4 reproduced human behavior across six canonical psychology experiments — well-studied patterns a model has seen described thousands of times [@mei2024llms]. Argyle's voting result worked because decades of polling documented so thoroughly how demographics track the vote that the model absorbed and replayed the correlation. For questions with strong demographic-to-opinion correlations (voting, partisan identity, familiar consumer preferences), models generate plausibly human distributions.
- **Skeptics.** Santurkar and colleagues asked whose opinions these models reflect and found a base model's default view representative of no real population, skewing toward the liberal, educated, Western profile of its training data — a skew that fine-tuning with human feedback shifted but did not erase [@santurkar2023opinions]; prompting could move the default, sometimes only into caricature.
- Bisbee and colleagues compared ChatGPT's simulated responses against real survey data and found the silicon version too tidy: less variation than real humans show, and regression coefficients that differed, sometimes sharply, from human estimates [@bisbee2024synthetic].
- Park and colleagues built "generative agents" — AI characters who lived in a simulated town, formed plans, and produced emergent social behavior [@park2023generative] — captivating, and a caution that fluency is not fidelity.
- Honest reading: silicon sampling does best for well-studied populations answering well-studied questions, worst for underrepresented groups facing novel ones. Marketing researchers converged on a modest role — pretesting instruments and running pilots, not producing final answers [@sarstedt2024silicon]. The optimists tend to test familiar behaviors on well-covered groups; the skeptics probe the tails and the underrepresented; both are telling the truth about the region they sampled. A tool with an operating range.

### The cost of asking (ESOMAR / insights industry)
- Every year, companies and governments spend on the order of $140 billion on the insights industry — surveys, panels, focus groups [@esomar2024market].
- A well-designed survey of a thousand respondents can cost tens of thousands of dollars and take weeks to field; rewording the question means paying again; breaking results across fifty subgroups multiplies the cost.
- Large institutions can absorb that; startups, nonprofits, local governments, and lone researchers often cannot, so many questions worth answering never get asked. When it costs $50,000 to learn what people think, only the well-funded ask — concentrating information, and therefore power.
- Cheap, approximate answers would change who gets to pose the question: a first-time candidate testing a message, a neighborhood association gauging support for a development, a graduate student chasing a hunch without a grant — the same democratizing move that turned budget scoring from an institutional privilege into something a citizen can run, pointed at the survey.
- In 2026 a company called Simile began packaging a broad version of this pitch, describing itself as "the simulation company" and arguing that simulation, not prediction alone, is AI's next frontier [@simile2026company; @simile2026frontier]. For public-interest use, a plausible demo is not enough — what matters is whether the numbers are calibrated, whether the uncertainty is stated, and whether anyone has checked them against ground truth.

### HiveSight — cells, not personas (the arc)
- HiveSight is the tool the author built to explore synthetic opinion; its short history compresses the book's argument.
- Naive version: ask a frontier model "Do you support a $15 minimum wage?" and it returns a careful, hedged essay — the average of everything it has read, no individual's answer and no population's distribution. Turning up the temperature adds random noise, which is not structured human diversity. People differ systematically (income, age, geography, a dozen correlated axes), not randomly; the repair is to condition the model on those axes.
- First prototype (the intuitive thing the literature was debating): built a demographically detailed persona from microdata and asked the model to answer as that person. Illustrative persona prompt used in the chapter: a 45-year-old rural-Ohio nurse earning $62,000, weekly churchgoer, 2020 Republican voter, asked whether she supports a $15 federal minimum wage.
- Ask a thousand such personas drawn from real demographic distributions and you get something shaped like a survey; it demos beautifully.
- Benchmarked against known 2024 survey values, persona roleplay landed roughly 25 points of mean absolute error, on both toplines and subgroups. It demoed like an oracle and scored like a guess. The intuitive mechanism failed the benchmark; the boring one won.
- July 2026 rebuild (what shipped): instead of role-played individuals, HiveSight builds post-stratification cells — roughly 150 demographic cells per geography, drawn from the same calibrated population data, populace, that the rest of the stack shares. For each cell it asks the model not to *be* a person but to estimate a *distribution* of answers, and aggregates those cell-level distributions with calibrated weights [@hivesight2026benchmarkpap]. The idea that survived is microdata grounding; the mechanism that died is the persona.
- The distinction: a persona asks the model to collapse a group into a single imagined individual, so the model produces the most probable/agreeable/legible version (stereotype or hedge-to-center); a survey measures a group's *spread*. Post-stratification asks "across people like this, what is the distribution of answers," cell by narrow cell. The microdata was doing the useful work all along (who is in the room, in what proportion); the role-play added the error.
- Post-stratification is not an AI invention: it is a workhorse of modern survey statistics — pollsters chop a population into demographic cells, estimate opinion within each, and reweight to the known composition (how a skewed online panel can still call an election). HiveSight keeps that apparatus and swaps a language model in to fill each cell.

### The registered benchmark (reported with ties intact)
- The benchmark froze a 63-item anchor bank: 52 attitudes from the 2024 General Social Survey plus 11 from the 2024 Survey of Household Economics and Decisionmaking (SHED).
- It was run under a pre-analysis plan committed before any answer was elicited, and against a model whose training cutoff predates every 2024 target (contamination control — the model could not have memorized the answers).
- On that bank: the cell estimator scored about 9.2 points of mean absolute error on toplines and 9.8 on subgroups.
- A simpler contender — asking the model for the whole population's distribution directly — scored about 8.6 on toplines and 9.8 on subgroups.
- On toplines the two are a tie: statistically equivalent within a ±1.5-point margin. Direct estimation is not worse. (The paper says so.)
- Where the cells earn their keep is structure: they track the *shape* of opinion across subgroups better (rank correlation 0.62 vs 0.48), are far steadier run to run (roughly nine times lower variance), and hold up when the questions are reordered.
- State-level failure, reported not buried: four items across forty-nine states, scored against a different survey (identified in the cataloging brief as BRFSS). The cells beat a naive baseline, but a national-constant guess — which simply assumes every state looks like the country as a whole — stayed competitive. An honest admission that the model's geographic signal on those four questions is thin: cheap national estimates are one thing, trustworthy fifty-state breakdowns another.
- The reason the tie and the competitive baseline appear at all is that the suites, arms, and scoring rules were registered before the results existed — a pre-analysis plan is a promise not to quietly relabel a loss as a win. A tool built to be sold would have led with the subgroup victory and left the topline tie unmentioned.
- HiveSight ships and publishes its benchmark, which puts it ahead of most synthetic-research tools; but shipping is not validation, and the honest tie on toplines is printed on the tin. What the tool earns is a defined operating range with a measured number attached.

### Inside the operating range (congestion-pricing example)
- Suppose a city council is weighing congestion pricing — a $15 charge to drive downtown at peak hours. A real survey might cost $30,000 to $50,000 and take three weeks.
- HiveSight can take the city's demographic composition, elicit a distribution over each cell, and return an estimate in minutes: perhaps 62 percent opposition overall, with a sharp gradient — heaviest among middle-income commuters who cannot easily switch to transit, lighter among low-income residents who do not drive and high-income residents who shrug it off.
- Match to a real poll: approximately, for the broad pattern; probably not for the exact percentages. The value is deciding whether the survey is worth fielding — shelve the idea if opposition is 90 percent everywhere; field the real survey (and know which subgroups to engage) if the split is close and structured.

### Systematic biases (structural, partly correctable)
- **WEIRD bias.** Models are trained mostly on text from Western, educated, industrialized, rich, democratic populations; they simulate Americans better than Nigerians, college graduates better than high-school dropouts. The gaps in the training data become systematic errors for exactly the underrepresented groups.
- **Homogeneity bias.** Models drift toward central tendencies and sand off the extremes; real opinion has long tails (outliers, contradictions, people who defy their demographics); silicon samples come out too clean.
- **Temporal anchoring.** A model trained to a cutoff can render the world up to that date and not past it; it cannot answer to an event it never saw (a pandemic, a crash, a viral moment). This is also why the contamination control matters: a model that has already seen 2024 is not forecasting 2024.
- **Social desirability bias.** Safety-tuned models are trained to be agreeable, making them reluctant to voice extreme or unpopular opinions that some real, matching humans hold — a sanitized public.
- **Stereotyping.** Handed a demographic label, a model sometimes returns the caricature instead of the range (prompted as a rural evangelical, it may produce the cartoon rather than the spread).
- Because these biases are structural, they can be handled the way survey research handles its own: with weights learned against known answers — measure where the model runs hot or cold on historical data where both demographics and real responses are known, then correct. The right output of a calibrated system is "58 percent, give or take eight, given this question type, this population, and our measured error on questions like it," not "58 percent support this."
- The hard part: a correction learned on last year's questions must hold on next year's or it is overfitting; the honest version grades itself on held-out items it never tuned against. The field is not there yet; the discipline is knowing that and saying so.

### Adversarial considerations
- Cheaply simulating how a demographic reacts to a message lets you craft the message that moves it; a campaign can A/B test divisive framing without exposing a real person to it.
- Because silicon results wear the costume of real ones (tables, percentages, crosstabs), a bad actor can pass a simulation off as a poll and manufacture the appearance of public support the methodology never earned.
- Feedback risk: if institutions act on synthetic opinion and those actions reshape the information environment that trains the next model, the estimates can begin to reflect opinions the tool helped create.
- Because models default to the majority within a group, dissenters (the conservative professor, the working-class environmentalist, the minority view inside a minority) get quietly rounded away, undercounted twice.
- Not an argument against building — traditional polling is manipulated too — but a real poll at least sampled somebody, while a simulation can conjure a consensus from no one and dress it in the same chart. The response is to build in the open (model, cells, calibration, error bars disclosed) and label results as estimates rather than surveys. "Clearly labeled" must be taken as seriously as the estimate itself.

### An operating range, not a substitute
- Silicon sampling is not a general replacement for asking people: strongest for well-studied populations on well-studied questions, weakest where representation is thin and the cost of being wrong is high.
- Why this is harder than anything else in the book: a tax flows through rules and a benefit has eligibility criteria — both encodable exactly and checkable against an oracle to the dollar; a first-print unemployment number will arrive and grade a forecast; an opinion has no such clean settlement — it emerges from a whole life, and when a model says "I strongly oppose this," no one is home who opposes anything.
- Opinion simulation is the embryo of the book's third primitive — values elicitation, the layer beside rules and prediction — and still only an embryo, because the ground truth is real but partial, so the discipline has to carry more of the weight.
- Two readings, both true at once: (1) it predicts — given how people like this have answered questions like this, here is the likely distribution (the sample-to-population extrapolation survey research always performed, with a model standing in for sampling weights); (2) it fabricates a plausible artifact resembling opinion with no opinion behind it. For deciding whether to field a survey, reading (1) is enough; for anything touching democratic legitimacy, reading (2) is the warning.
- There is a version that plugs into the rest of the stack: simulate a policy change against the population, then simulate the public's reaction to it, both from the same profiles, both uncertain. But a distribution of what people *think* is only an input; the harder question is what a society *does* with those opinions — how it counts, weighs, and turns them into a decision. That is the handoff to the democracy chapter.

## Story beats
- **The HiveSight naive-failure-to-boring-winner arc.** Prototype persona roleplay demos like an oracle, then scores ~25pt MAE against 2024 survey values; the unglamorous post-stratification-cells rebuild wins on structure and stability while merely tying on toplines. The compressed morality tale of the whole book.
- **The illustrative persona prompt (explicitly a constructed example).** The rural-Ohio-nurse prompt block — a made-up demographic persona used to show what the failed first prototype did. Not a real quote; keep it clearly hypothetical.
- **The congestion-pricing hypothetical (illustrative).** A city council deciding whether to field a $30k–$50k survey; invented percentages (62% opposition, gradient by income) chosen to illustrate the "decide whether the survey is worth fielding" use, not to report a real result.
- **The registered-benchmark honesty beat.** The tie and the competitive national-constant baseline appear in the paper *because* of pre-registration — a tool built to be sold would have hidden them.

## Quotes
- "Out of One, Many: Using Language Models to Simulate Human Samples" — Argyle et al., 2023 (paper title) [@argyle2023out].
- Simile describes itself as "the simulation company" [@simile2026company].
- (No other attributed third-party verbatim quotation in this chapter. The persona-prompt block is an authored illustrative example, not a quotation.)

## Arguments
1. Cells, not personas: this is the book's own method (benchmark against ground truth before believing the demo) turned on its own speculation. The microdata grounding survived; the persona role-play was the part that added the error.
2. A persona collapses a group to one legible individual and so reaches for the stereotype; post-stratification asks for the group's *spread*, which is what a survey actually measures.
3. Pre-registration is what makes honesty automatic: the topline tie and the competitive state-level baseline are in the paper only because the arms and scoring were fixed before the numbers existed. "A demo persuades by looking right; an instrument persuades by telling you how often it is wrong, and on which questions."
4. Silicon sampling is a tool with a measured operating range, not a general replacement for asking people; its value is often deciding whether a real survey is worth fielding, not replacing it.
5. The systematic biases (WEIRD, homogeneity, temporal, social-desirability, stereotyping) are structural, hence partly predictable and correctable with weights learned against known answers — but only if the correction holds on held-out items, or it is "overfitting with extra steps."
6. Opinion simulation is the embryo of the third primitive (values elicitation), and is genuinely harder than rules or prediction because opinion has no clean ground-truth settlement — "no one is home who opposes anything."
7. Labeling must be as serious as the estimate: approximate knowledge, widely distributed and clearly labeled, can serve the public better than precise knowledge held by whoever can afford a poll — but only if "clearly labeled" is enforced.

## Author-texture (verbatim, may be reused; use sparingly)
- "It demoed like an oracle and scored like a guess." (the persona-benchmark punch)
- "The intuitive mechanism failed the benchmark; the boring one won."
- "benchmark against ground truth before believing the demo." (the book's method, stated on its own tool)
- "A demo persuades by looking right; an instrument persuades by telling you how often it is wrong, and on which questions."
- First-person keepers (raw phrasing): "HiveSight is the tool I built to explore synthetic opinion…"; "Then I benchmarked it against known 2024 survey values, and it fell apart"; "That is the test I decided to put my own version of this idea through."

## Structural notes
- **Chapter job:** Introduce synthetic opinion (silicon sampling); map the optimist/skeptic literature as an operating-range argument; tell the HiveSight arc honestly (persona failure → post-stratification cells); establish the registered benchmark with its topline tie intact; catalog the structural biases and adversarial misuses; and frame opinion simulation as the still-embryonic third primitive (values elicitation).
- **Handoff in (from the uncertainty/scoreboard chapter):** opinion is exactly the thing the scoreboard cannot grade — no first-print number, no certifying office — so it must carry more discipline internally.
- **Handoff out (14→15, to the democracy chapter):** a distribution of what people think is only an input; the next question is how a society aggregates opinion into a decision.
- **Phrasing constraints (hard):**
  - The topline result is a TIE (cells ≈9.2/9.8 vs direct ≈8.6/9.8; equivalent within ±1.5). Never claim the cells beat direct estimation on toplines; the cells win on *structure* (rank corr 0.62 vs 0.48) and *stability* (~9× lower variance), not topline accuracy.
  - Report the state-level result honestly: a national-constant baseline stays competitive on the four BRFSS items across 49 states; do not oversell fifty-state breakdowns.
  - The contamination control (model training cutoff predates every 2024 target) is load-bearing — keep it; a model that has seen 2024 is not forecasting 2024.
  - Shipping ≠ validation ≠ accuracy — keep that distinction sharp.
  - Silicon results must be labeled as estimates, never dressed as a survey; the persona prompt and congestion-pricing numbers stay explicitly illustrative.
  - Retired-name guard: the population data is populace; the tool is HiveSight; the third primitive is values elicitation.

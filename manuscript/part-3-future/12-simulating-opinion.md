# Chapter 12: Simulating opinion

**Note to readers**: This chapter describes a research direction, not a validated production tool. Unlike PolicyEngine (which has been used for official government policy costing with validated accuracy), the silicon sampling approaches described here are experimental. HiveSight is a preliminary prototype exploring whether AI can forecast public opinion—the evidence suggests partial success with important limitations. Treat this as hypothesis generation, not established methodology.

---

In 2023, a research paper with a provocative title appeared: "Out of One, Many: Using Language Models to Simulate Human Samples" {cite}`argyle2023out`. The researchers at Brigham Young University had done something that would have seemed like science fiction a decade earlier. They asked GPT-3 to adopt specific demographic personas—a 65-year-old Black woman from Mississippi, a 28-year-old white man from Oregon—and answer survey questions. Then they compared the AI's responses to actual survey data.

The results were striking. When properly conditioned on demographic characteristics, the language model showed high correspondence with human voting patterns across the 2012, 2016, and 2020 presidential elections. It captured the partisan divide by education. It predicted regional variation. In many ways, it predicted responses like the population it was simulating.

This opens a strange new question: Can we simulate not just how policies affect households, but what households *think* about those policies?

---

## The emerging field

Argyle et al. didn't publish in isolation. Their paper landed in a growing body of research exploring whether language models can serve as proxies for human survey respondents.

Santurkar et al. (2023) took a different angle, asking a more pointed question: whose opinions do language models actually reflect {cite}`santurkar2023opinions`? They found that base language models disproportionately reflect the views of liberal, educated, Western populations—the demographic footprint of the training data. Fine-tuning models with reinforcement learning from human feedback (RLHF) shifted this distribution but didn't eliminate it. The models could be prompted to adopt different perspectives, but their default stance was not representative of any actual population.

Park et al. (2023) pushed the concept further with "generative agents"—autonomous AI characters that lived in a simulated town, formed relationships, made plans, and exhibited emergent social behavior {cite}`park2023generative`. Their architecture combined a language model with a memory system that stored experiences, synthesized reflections, and retrieved relevant context for decisions. The result: AI agents that weren't just answering survey questions but simulating ongoing lives.

Bisbee et al. (2024) introduced a critical counterpoint. They systematically compared ChatGPT's simulated survey responses to real human data and found significant problems {cite}`bisbee2024synthetic`. Simulated responses showed less variation than real surveys. Regression coefficients from silicon samples often differed significantly from human-derived estimates. The models struggled to reproduce the full distribution of opinions, tending instead toward central tendencies that smoothed away the messy extremes of real public opinion.

Mei et al. (2024) found more encouraging results in a narrower domain: GPT-4 could reproduce human behavior across six canonical psychology experiments, suggesting that for well-studied behavioral patterns the models have absorbed enough training signal to generate plausible responses {cite}`mei2024llms`.

The picture that emerges is nuanced. Silicon sampling works best for well-studied populations on well-studied questions, and worst for underrepresented groups on novel topics. It's a tool with a specific operating range, not a general substitute for human data.

---

## The market research problem

Every year, companies and governments spend roughly $140 billion on survey research {cite}`esomar2024market`. They want to know what people think—about products, policies, candidates, ideas. The traditional method: find a representative sample of humans, ask them questions, aggregate the responses.

This works, but it's slow and expensive. A well-designed survey with 1,000 respondents might cost $50,000 and take weeks to field. Want to test a slightly different question wording? That's another $50,000. Want to check if opinions differ across 50 demographic subgroups? The costs multiply.

For large corporations and government agencies, this is manageable. For startups, nonprofits, local governments, and individual researchers, it's often prohibitive. Many questions that would be valuable to answer simply don't get asked.

What if you could get approximate answers instantly for a fraction of the cost?

---

## Silicon sampling

The idea is called "silicon sampling"—using AI models to simulate survey respondents {cite}`sarstedt2024silicon`. Instead of recruiting human participants, you prompt a language model to answer as if it were a person with specific characteristics.

The naive approach doesn't work. If you simply ask GPT-4 "Do you support raising the minimum wage?", it will give you a measured, hedged response reflecting its training—probably something about tradeoffs and depending on circumstances. That's not what any individual human would say.

The insight is conditioning. Instead of asking the model what it thinks, you ask it to adopt a specific persona:

> *You are a 45-year-old white woman living in rural Ohio. You work as a nurse, earn $62,000 per year, and have two children. Your husband works in manufacturing. You attend church regularly and voted for Trump in 2020.*
>
> *Answer the following question as this person would: Do you support raising the federal minimum wage to $15?*

Now the model produces something different—not its own hedged take, but its prediction of what this specific person would say.

Ask a thousand personas, each constructed from actual demographic distributions, and you get something approximating a survey.

---

## HiveSight: a prototype

HiveSight is an experimental prototype I've built to explore this idea—not a production platform, but a proof of concept. The goal: enter a survey question, select demographic filters, receive instant results from hundreds of simulated respondents. Whether it works well enough to be useful is an open question.

The technical architecture addresses a key problem. Simply asking an LLM the same question many times with high "temperature" (randomness) doesn't produce meaningful variation. Random noise is not the same as structured human diversity.

Real opinions vary in ways that correlate with demographics, experiences, and circumstances. A wealthy retiree in Florida has different views than a young barista in Seattle—not randomly different, but systematically different in ways that reflect their life circumstances. Temperature-based variation misses this entirely.

HiveSight's approach is microdata-grounded. Just as PolicyEngine simulates policies using representative household data from government surveys, HiveSight generates personas from the same microdata. Each simulated respondent has a coherent demographic profile drawn from actual population distributions—income, age, education, location, family structure, employment status.

This grounds the diversity in reality. Instead of asking "what would a random perturbation of the AI say?", we ask "what would someone with these actual characteristics say?" across a representative sample of real demographic profiles.

A concrete example: suppose a city council is considering a congestion pricing policy—a $15 fee for driving into the downtown core during peak hours. A traditional survey would cost $30,000-50,000 and take three weeks. With HiveSight, the council could enter the question, specify the city's demographic distribution, and receive simulated responses in minutes. The output might show: 62% opposition overall, but with sharp demographic splits—78% opposition among suburban car commuters, 55% support among urban residents who use transit. The income gradient might show that opposition peaks among middle-income households who can't easily switch to transit but feel the fee acutely, while both low-income households (who don't drive) and high-income households (who absorb the fee) show less opposition.

Would these numbers match a real survey? Based on the current evidence: approximately, for the broad patterns (the demographic splits, the income gradient), but probably not precisely for the specific percentages. The value isn't replacing the real survey—it's deciding whether the real survey is worth fielding. If HiveSight shows 90% opposition across all demographics, the council might shelve the proposal without spending $40,000 to confirm. If it shows a close split with interesting demographic variation, that's when the real survey investment pays off.

---

## What the research says about accuracy

Does silicon sampling work? The honest answer: partially, in specific domains, with systematic limitations that aren't yet well understood.

**What works reasonably well:**

The Argyle study showed high correspondence between AI and human voting patterns across presidential elections {cite}`argyle2023out`. Marketing researchers report that silicon sampling holds promise for pretesting survey instruments and pilot studies {cite}`sarstedt2024silicon`. For questions where the training data contains strong demographic-opinion correlations—voting behavior, partisan attitudes, consumer preferences for well-known product categories—the models generate plausible distributions.

**What doesn't work well:**

Bisbee et al. (2024) found that silicon sampling produces less variation than real surveys and yields regression coefficients that often differ significantly from human data {cite}`bisbee2024synthetic`. Santurkar et al. (2023) showed that models default to the opinions of their training data's dominant demographic—liberal, educated, Western—even when prompted otherwise {cite}`santurkar2023opinions`. The models almost never generate "don't know" responses, which real survey respondents give frequently. On sensitive topics, models exhibit social desirability bias, producing answers that sound acceptable rather than ones that match what real people actually say.

**What remains unknown:**

No systematic validation has been conducted for HiveSight specifically. The prototype exists, the architecture is built, but rigorous benchmarking against traditional surveys—the kind of validation that would justify confidence in the results—hasn't been done. I flag this not as a future plan but as a current limitation.

---

## Systematic biases

The biases in silicon sampling are not random—they're structural, which means they're partially predictable and potentially correctable.

**WEIRD bias.** Language models are trained primarily on text from Western, Educated, Industrialized, Rich, Democratic populations. They're better at simulating Americans than Nigerians, better at simulating college graduates than high school dropouts. The training data has gaps, and those gaps produce systematic errors in simulated responses for underrepresented groups.

**Homogeneity bias.** The models tend toward central tendencies, smoothing away the messy extremes of real public opinion. Real survey data has long tails—outlier opinions, surprising responses, contradictory views from people who defy their demographic stereotypes. Silicon samples are too clean.

**Temporal anchoring.** Language models are trained on data up to a cutoff point. They might accurately simulate opinions from 2023 but miss shifts that happened in 2024. They can't capture responses to events they haven't seen—a pandemic, a financial crisis, a viral moment that shifts public sentiment overnight.

**Social desirability bias.** Safety-tuned models are trained to be helpful, harmless, and honest. This training makes them reluctant to express extreme, controversial, or socially undesirable opinions—even when real humans with matching demographics would express exactly those views. The model produces a sanitized version of public opinion.

**Stereotyping.** When prompted with demographic characteristics, models sometimes reproduce stereotypes rather than capturing genuine variation within groups. A prompt describing a rural white evangelical man might produce a caricature rather than the range of views that actual rural white evangelical men hold. Santurkar et al. found that fine-tuning could push models to "embody caricatures of those groups" {cite}`santurkar2023opinions`.

---

## Adversarial considerations

Silicon sampling doesn't just have limitations—it has risks.

**Manipulation targeting.** If you can simulate how specific demographics react to messages, you can craft maximally persuasive content targeted at those demographics. Political campaigns could use silicon sampling to A/B test divisive messaging without ever exposing real people to it. Disinformation campaigns could optimize their content for specific vulnerable populations.

**False legitimacy.** Silicon survey results look like real survey results—tables, percentages, demographic breakdowns. A bad actor could present silicon sampling data as if it were a real poll, manufacturing apparent public support for a position. The format creates legitimacy that the methodology doesn't warrant.

**Feedback loops.** If organizations start making decisions based on silicon sampling, and those decisions shape the information environment that trains future language models, the models could become self-reinforcing. They would simulate the opinions they helped create, not opinions that emerge from genuine human deliberation.

**Erasure of minority views.** Because models default to majority opinions within demographic groups, silicon sampling could systematically undercount minority viewpoints—not just ethnic minorities, but people who hold unusual views within their demographic cohort. The dissenting Republican, the conservative professor, the working-class environmentalist—these voices are already underrepresented in training data and would be further marginalized in silicon samples.

These risks don't mean silicon sampling shouldn't be developed. They mean it should be developed with transparency requirements, clear labeling, and awareness of how it could be misused.

---

## Calibration: the path to trustworthiness

What would make silicon sampling trustworthy? Not perfection, but calibrated uncertainty.

The research program works like this:

1. Take historical survey data—the General Social Survey, Pew polls, election exit polls—where we know both the demographics and the actual responses.
2. Construct matching personas and run the language model.
3. Compare AI responses to human responses across demographic subgroups.
4. Measure the systematic biases: where does the model overestimate conservative responses? Underestimate enthusiasm for certain policies? Miss regional variation?
5. Apply corrections to future results, the same way survey researchers apply demographic weights.

The result would be defensible uncertainty: not "the model says 58% support this policy" but "our calibrated estimate is 58% ±8%, based on historical accuracy for this question type and demographic distribution."

This is the same logic as survey weighting. Traditional surveys oversample some groups and undersample others; weights correct for these imbalances. Silicon sampling has its own biases; calibration weights could correct for those.

This research is ongoing across the field. We're not there yet.

---

## Can we simulate what people think?

There's something philosophically strange about simulating opinions.

Policies have objective effects—or at least effects we can model mechanistically. Taxes flow through defined rules. Benefits have eligibility criteria. But opinions aren't like that. What someone thinks about minimum wage isn't computed from rules. It emerges from a lifetime of experiences, information, identity, and reasoning processes we don't fully understand.

When we simulate an opinion, what are we actually doing?

One view: We're predicting what a person with certain characteristics would say, based on statistical patterns in how similar people have answered similar questions. This is fundamentally what survey research does—extrapolate from samples to populations. Silicon sampling uses AI as the extrapolation mechanism instead of sampling weights.

Another view: We're creating a simulacrum that looks like opinion but isn't. The AI doesn't believe anything; it predicts text. When it says "I strongly oppose this policy," there's no one home who actually opposes anything. For understanding what people actually think, for respecting their autonomy as participants in democracy, this distinction matters.

Both views have merit. For practical purposes—market research, hypothesis generation, policy feedback—the first view suggests silicon sampling can be useful. For democratic legitimacy and genuine understanding, the second view counsels caution.

---

## Toward responsible use

Despite these caveats, I think silicon sampling will become standard infrastructure for a narrow but valuable set of use cases. Not because it's good enough to replace real surveys, but because the alternatives—for many questions—are either impractical surveys or no data at all.

The path forward involves:

**Radical transparency.** Every silicon sampling result should come with methodology: which model, which personas, what calibration, what limitations. Users should understand they're seeing AI predictions, not human responses. No silicon survey should ever be presented without prominent disclosure.

**Complementary use.** Position silicon sampling as augmenting, not replacing, human research. Use it to narrow hypotheses and generate preliminary signals, then verify with real surveys where the stakes are high. The presidential campaign should still field real polls. The pharmaceutical company should still run real focus groups.

**Continuous benchmarking.** Regular comparison against traditional surveys to measure and correct biases. Published accuracy metrics by question type and demographic group. If a silicon sampling platform can't tell you its calibrated error rate, it hasn't done the work.

**Integration with the simulation stack.** HiveSight connects to the same microdata that powers PolicyEngine. This creates a possibility: simulate a policy change (PolicyEngine), then simulate public reaction to that change (HiveSight), all using consistent demographic profiles. Both predictions, both uncertain, both more useful than no information.

---

## The information access question

Traditional survey research is one of the few remaining information moats protecting established institutions. When it costs $50,000 to ask what people think, only well-funded organizations can ask. This concentrates information—and therefore power—among those who can afford it.

Silicon sampling disrupts this in the same way PolicyEngine disrupts budget scoring. The information becomes more accessible. A first-time candidate can test campaign messages. A neighborhood association can gauge support for a development project. A student researcher can explore hypotheses without grant funding.

Not all of these uses will be responsible. Someone could use silicon sampling to craft maximally persuasive targeted messaging. The response isn't to restrict the tools—traditional surveys can be and are used for manipulation too. It's transparency about what these tools are and education about how to interpret them.

Approximate knowledge, widely distributed and clearly labeled, might serve the public interest better than precise knowledge narrowly held. But only if the "clearly labeled" part is taken seriously.

---

## References

```{bibliography}
:filter: docname in docnames
```

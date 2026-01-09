# Chapter 12: Simulating Opinion

**Note to readers**: This chapter describes research directions, not validated production tools. Unlike PolicyEngine (which has been used for official government policy costing with validated accuracy), the silicon sampling approaches described here are experimental. HiveSight is a preliminary prototype exploring whether AI can forecast public opinion—the evidence suggests partial success with important limitations. Treat this as hypothesis generation, not established methodology.

---

In 2023, a research paper with a provocative title appeared: "Out of One, Many: Using Language Models to Simulate Human Samples" {cite}`argyle2023out`. The researchers had done something that would have seemed like science fiction a decade earlier. They asked GPT-3 to pretend to be different people—a 65-year-old Black woman from Mississippi, a 28-year-old white man from Oregon—and answer survey questions. Then they compared the AI's responses to actual survey data.

The results were striking. When properly conditioned on demographic characteristics, the language model showed high correspondence with human voting patterns across the 2012, 2016, and 2020 presidential elections. It captured the partisan divide by education. It predicted regional variation. In many ways, it thought like the population it was pretending to be.

This opens a strange new question: Can we simulate not just how policies affect households, but what households *think* about those policies?

---

## The Market Research Problem

Every year, companies and governments spend roughly $140 billion on survey research {cite}`esomar2024market`. They want to know what people think—about products, policies, candidates, ideas. The traditional method is straightforward: find a representative sample of humans, ask them questions, aggregate the responses.

This works, but it's slow and expensive. A well-designed survey with 1,000 respondents might cost $50,000 and take weeks to field. Want to test a slightly different question wording? That's another $50,000. Want to check if opinions differ across 50 demographic subgroups? The costs multiply.

For large corporations and government agencies, this is manageable. For startups, nonprofits, local governments, and individual researchers, it's often prohibitive. Many questions that would be valuable to answer simply don't get asked.

What if you could get approximate answers instantly for a fraction of the cost?

---

## Silicon Sampling

The idea is called "silicon sampling"—using AI models to simulate survey respondents {cite}`sarstedt2024silicon`. Instead of recruiting human participants, you prompt a language model to answer as if it were a person with specific characteristics.

The naive approach doesn't work. If you simply ask GPT-4 "Do you support raising the minimum wage?", it will give you a measured, hedged response reflecting its training—probably something about tradeoffs and depending on circumstances. That's not what any individual human would say.

The insight is conditioning. Instead of asking the model what it thinks, you ask it to adopt a specific persona:

> *You are a 45-year-old white woman living in rural Ohio. You work as a nurse, earn $62,000 per year, and have two children. Your husband works in manufacturing. You attend church regularly and voted for Trump in 2020.*
>
> *Answer the following question as this person would: Do you support raising the federal minimum wage to $15?*

Now the model produces something different—not its own hedged take, but its prediction of what this specific person would say. The response might be skeptical of government mandates, concerned about small business costs, perhaps sympathetic to workers but doubtful about the policy.

Ask a thousand personas, each constructed from actual demographic distributions, and you get something approximating a survey.

---

## The Diversity Problem

HiveSight is an experimental prototype I've built to explore this idea—not a production platform, but a proof of concept. The goal: enter a survey question, select demographic filters, receive instant results from hundreds of simulated respondents. Whether it works well enough to be useful is an open question.

The technical architecture matters. Simply asking an LLM the same question many times with high "temperature" (randomness) doesn't produce meaningful variation. Random noise is not the same as structured human diversity.

Real opinions vary in ways that correlate with demographics, experiences, and circumstances. A wealthy retiree in Florida has different views than a young barista in Seattle—not randomly different, but systematically different in ways that reflect their life circumstances. Temperature-based variation misses this entirely.

HiveSight's solution is microdata. Just as PolicyEngine simulates policies using representative household data from government surveys, HiveSight generates personas from the same microdata. Each simulated respondent has a coherent demographic profile drawn from actual population distributions—income, age, education, location, family structure, employment status.

This grounds the diversity in reality. Instead of asking "what would a random perturbation of the AI say?", we ask "what would someone with these actual characteristics say?" across a representative sample of real demographic profiles.

---

## The Validation Question

Does it work?

The honest answer is: sometimes, surprisingly well; other times, not so much.

The Argyle study showed high correspondence between AI and human voting patterns across the 2012, 2016, and 2020 presidential elections. Research from Mei et al. found that GPT-4 could reproduce human behavior across six canonical psychology experiments {cite}`mei2024llms`. Marketing researchers report that silicon sampling holds promise for pretesting and pilot studies, though with important limitations {cite}`sarstedt2024silicon`.

But there are systematic limitations.

**WEIRD bias.** Language models are trained primarily on Western, Educated, Industrialized, Rich, Democratic populations. They're better at simulating Americans than Nigerians, better at simulating college graduates than high school dropouts. The training data has gaps, and those gaps show up in simulated responses.

**Sample size requirements.** Just as traditional surveys need sufficient sample sizes for reliable results, silicon sampling needs enough simulated respondents. Results become unstable below about 200 personas.

**Unknown unknowns.** When the model gets a persona wrong, it doesn't tell you. A simulated 70-year-old might respond in ways a real 70-year-old wouldn't, and you have no way to detect this from the output alone.

**Temporal anchoring.** Language models are trained on data up to a cutoff point. They might accurately simulate opinions from 2023 but miss shifts that happened in 2024. They can't capture responses to events they haven't seen.

The responsible position: silicon sampling is useful for rapid prototyping, hypothesis generation, and situations where traditional surveys are impractical. It's not a replacement for high-stakes research where accuracy is critical.

---

## Calibration and Trust

What would make silicon sampling trustworthy?

The answer is calibration—systematically measuring how AI responses compare to human responses and correcting for systematic biases.

The research program works like this:

1. Take historical survey data—the General Social Survey, Pew polls, election exit polls—where we know both the demographics and the actual responses.
2. Construct matching personas and run the language model.
3. Compare AI responses to human responses across demographic subgroups.
4. Learn the systematic biases: where does the model overestimate conservative responses? Underestimate enthusiasm for certain policies? Miss regional variation?
5. Apply corrections to future silicon sampling results.

This is the same logic as survey weighting. Traditional surveys oversample some groups and undersample others; weights correct for these imbalances. Silicon sampling has its own biases; calibration weights would correct for those.

The result would be defensible uncertainty: not "the model says 58% support this policy" but "our calibrated estimate is 58% ±5%, based on historical accuracy for this question type and demographic distribution."

This research is ongoing. We're not there yet.

---

## The Democratization Pattern

Silicon sampling follows the same pattern as the other tools in this book.

| Domain | Traditional | Silicon |
|--------|-------------|---------|
| Policy analysis | JCT/CBO ($millions, months) | PolicyEngine (free, instant) |
| Survey research | Field surveys ($50K, weeks) | HiveSight ($50, minutes) |
| Statistical analysis | Stata licenses, expertise | LLM-assisted analysis |

The cost reduction is roughly 1000x. The time reduction is roughly 100x. The access expansion is enormous.

This creates new possibilities. A local advocacy group can test message framings before a campaign. A product designer can check reactions to features before building them. A policymaker can gauge public sentiment before drafting legislation. A researcher can generate hypotheses before committing to expensive data collection.

None of these replace the rigorous version. A presidential campaign should still field real surveys. A pharmaceutical company should still run clinical trials. High-stakes decisions deserve high-stakes research.

But many decisions don't currently get any research because the bar is too high. For those, approximate answers are better than no answers.

---

## Can We Simulate What People Think?

There's something philosophically strange about simulating opinions.

Policies have objective effects—or at least effects we can model mechanistically. Taxes flow through defined rules. Benefits have eligibility criteria. Labor supply responds to incentives according to (debatable but empirically grounded) economic theory.

But opinions aren't like that. What someone thinks about minimum wage isn't computed from rules. It emerges from a lifetime of experiences, information, identity, and reasoning processes we don't fully understand.

When we simulate an opinion, what are we actually doing?

One view: We're predicting what a person with certain characteristics would say, based on statistical patterns in how similar people have answered similar questions. This is fundamentally what survey research does—extrapolate from samples to populations. Silicon sampling just uses AI as the extrapolation mechanism.

Another view: We're creating a simulacrum that looks like opinion but isn't the real thing. The AI doesn't believe anything; it predicts text. When it says "I strongly oppose this policy," there's no one home who actually opposes anything.

Both views have merit. For practical purposes—market research, hypothesis generation, policy feedback—the first view suggests silicon sampling can be useful. For understanding what people actually think, for respecting their autonomy as participants in democracy, the second view suggests caution.

The question "should we?" is separate from "can we?"

---

## Toward Opinion Infrastructure

Despite these caveats, I think silicon sampling will become standard infrastructure for understanding public sentiment. Not because it's perfect, but because the alternatives are often impractical.

The path forward involves:

**Radical transparency.** Every silicon sampling result should come with methodology: which model, which personas, what limitations. Users should understand they're seeing AI predictions, not human responses.

**Continuous calibration.** Regular benchmarking against traditional surveys to measure and correct biases. Published accuracy metrics by question type and demographic group.

**Complementary use.** Position silicon sampling as augmenting, not replacing, human research. Use it to narrow hypotheses, then verify with real surveys where it matters.

**Integration with simulation stack.** HiveSight connects to the same microdata that powers PolicyEngine. This creates possibilities: simulate a policy change, then simulate public reaction to that change, all using consistent demographic profiles.

The vision is a tool that answers: "If you implemented this policy, here's what would happen to household incomes (PolicyEngine) and here's what people would think about it (HiveSight)." Both predictions, both uncertain, both more useful than no information.

---

## The Information Economy

Traditional survey research is one of the few remaining moats protecting established institutions. When it costs $50,000 to ask what people think, only well-funded organizations can ask. This concentrates information—and therefore power—among those who can afford it.

Silicon sampling disrupts this in the same way PolicyEngine disrupts budget scoring. The information becomes accessible. The playing field levels.

A first-time candidate can test campaign messages. A neighborhood association can gauge support for a development project. A student researcher can explore hypotheses without grant funding.

Not all of these uses will be responsible. Just as calculators can be used for good or ill, survey simulation can serve manipulation as well as understanding. Someone could use HiveSight to craft maximally persuasive disinformation targeted at specific demographics.

The response isn't to restrict the tools. It's transparency about what they are and education about how to interpret them. Silicon sampling is approximate, biased in knowable ways, and best used for exploration rather than conclusion.

But approximate knowledge, widely distributed, might be better than precise knowledge, narrowly held.

---

*What do people think about this policy?*

*We could field a survey. That would take six weeks and cost fifty thousand dollars.*

*Or we could simulate it. That would take six minutes and cost fifty dollars.*

*The simulation won't be as accurate. But is waiting six weeks more accurate than acting on rough information now? Is the policy decision that would otherwise get made with no data better than one informed by approximate data?*

*These are the questions silicon sampling forces us to ask. Not whether AI can replace human research—it can't. But whether the perfect should be the enemy of the good.*

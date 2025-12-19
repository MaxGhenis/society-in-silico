# Chapter 6: The Society View

Making the Child Tax Credit fully refundable would cost $2 billion per year. It would benefit households across the income distribution, with the highest proportion affected in the top decile. Poverty would fall by 0.3 percentage points.

These are not guesses. They are calculations—the product of applying a policy reform to a representative sample of the American population and aggregating the results {cite}`policyengine2023scoring`.

This is the society view: microsimulation scaled from individual households to the entire nation.

---

## From One to Many

The household view answers "what would this policy mean for me?" The society view answers "what would this policy mean for everyone?"

The transition seems straightforward: run the household calculation for every household in the country, sum up the results. In principle, that's exactly what happens. In practice, it requires solving some of the hardest problems in policy analysis.

Start with the obvious challenge: you can't actually survey every household. The Current Population Survey samples about 60,000 households each month—a tiny fraction of the roughly 130 million households in America {cite}`census2024cps`. Each sampled household must represent thousands of similar households in the population.

This is done through weights. Each household in the survey carries a weight indicating how many households it represents. A household in rural Wyoming might represent 5,000 similar households. A household in Manhattan might represent 500. The Census Bureau calculates these weights carefully, adjusting for sampling design and non-response.

When PolicyEngine runs a policy simulation, it calculates the impact on each sampled household, multiplies by that household's weight, and sums across all households. The result is an estimate of national impact—with all the uncertainty that weighted surveys carry.

---

## The Data Foundation

The quality of society-level analysis depends entirely on the quality of the underlying data. PolicyEngine confronts this directly.

The Current Population Survey has known limitations {cite}`policyengine2022enhanced`. Respondents underreport benefit receipt—studies find 40-50% of SNAP recipients don't report their benefits in the CPS {cite}`meyer2015underreporting`. High incomes are top-coded, distorting estimates of policies affecting top earners. The sample is too small for reliable state-level analysis. Asset information is missing, making wealth-based policies unmeasurable.

> "These limitations can reduce the accuracy and usefulness of the CPS for policy simulations. For example, CPS-based projections will tend to underestimate the budgetary impacts of reforming SNAP or instituting a tax on top earners."

PolicyEngine addresses these problems through data enhancement—a technical process that combines multiple data sources using machine learning techniques {cite}`policyengine2022enhanced`.

The process works in stages. First, replace reported taxes and benefits with computed amounts from the microsimulation model, ensuring internal consistency. Second, integrate IRS tax records to correct income distributions, using quantile regression rather than simple matching. Third, reweight the sample using gradient descent to minimize divergence from known administrative totals. Fourth, incorporate additional surveys—the Survey of Consumer Finances for wealth, the Consumer Expenditure Survey for spending patterns.

The result is an enhanced dataset that matches official aggregates more closely than the raw CPS. Budget estimates become more reliable. Distributional analysis becomes more accurate. State-level analysis becomes possible.

---

## Budget Scoring

The most basic question about any policy reform: what does it cost?

Budget scoring is the bread and butter of policy analysis. When a legislator proposes expanding the EITC, the first question is always "how much?" When an advocate proposes a new child benefit, feasibility depends on the price tag.

PolicyEngine calculates net budget impact by summing changes in tax revenue and benefit expenditure across all households. The fully refundable CTC example costs $2 billion because the additional credits paid out exceed any behavioral responses or interactions with other programs {cite}`policyengine2023scoring`.

But budget impact isn't a single number. It varies by:

- **Year**: Tax provisions phase in and out. Inflation adjusts thresholds. Economic conditions change.
- **Baseline**: Impact relative to current law differs from impact relative to scheduled future law.
- **Behavioral assumptions**: Do people work more or less in response to changed incentives?

PolicyEngine shows budget impact as a primary output, but contextualizes it with distributional analysis and household examples that reveal what the numbers mean.

---

## Poverty Impact

Reducing poverty is often the stated goal of tax-benefit reforms. But what does "reducing poverty" actually mean, and how do you measure it?

PolicyEngine uses the Supplemental Poverty Measure (SPM), which the Census Bureau introduced in 2011 as a more comprehensive alternative to the Official Poverty Measure {cite}`policyengine2023sex`. Unlike the older measure, the SPM accounts for taxes, in-kind benefits like SNAP, geographic variation in housing costs, work expenses, and out-of-pocket medical spending.

Under current law, PolicyEngine estimates that 9.6% of Americans have resources below their SPM poverty threshold. 3.3% are in deep poverty—below half the threshold. Women face higher poverty rates than men. Children face higher rates than working-age adults, who face higher rates than seniors {cite}`policyengine2023sex`.

When you apply a reform, PolicyEngine recalculates each household's resources, compares to poverty thresholds, and produces new aggregate rates. The change in the overall rate, broken down by demographics, shows who the reform helps and by how much.

The WIC program, for example, reduces overall poverty by 0.8% and deep poverty by 2.2%. It disproportionately benefits children—reducing child poverty by 2.6%. And it has differential gender impacts: poverty falls 0.9% for women but only 0.7% for men {cite}`policyengine2023sex`.

This granularity matters. A reform that "reduces poverty" might do so primarily for seniors while leaving child poverty unchanged. A reform that appears gender-neutral might have very different effects on men and women. The society view reveals these patterns.

---

## Distributional Analysis

Beyond poverty, who wins and who loses?

PolicyEngine divides the population into deciles by income and shows what fraction of each decile gains, loses, or is unaffected. A bar chart reveals whether a reform is progressive (helping lower deciles more) or regressive (helping higher deciles more) {cite}`policyengine2023scoring`.

For the fully refundable CTC, the distributional picture is counterintuitive. While the reform expands a credit that phases out with income, the highest proportion of people affected is in the top decile. Why? Because the reform extends refundability to higher-income households who previously hit the income tax floor.

This kind of analysis reveals complexities that headline numbers obscure. A "$2 billion reform that reduces poverty" could be distributed in wildly different ways—some more aligned with stated goals than others.

PolicyEngine also breaks down impacts by:

- **Wealth decile**: Using imputed wealth from the Survey of Consumer Finances
- **Age group**: Children, working-age adults, seniors
- **Sex**: Male, female
- **Geography**: State-level estimates where data supports them
- **Race/ethnicity**: Using categories available in the underlying data

Each breakdown tells a different story about who the policy affects.

---

## The Inequality Question

Beyond poverty and distribution, how does a reform affect overall inequality?

PolicyEngine calculates changes in the Gini coefficient—the standard measure of income inequality. A Gini of 0 means perfect equality (everyone has the same income). A Gini of 1 means perfect inequality (one person has everything).

A reform that costs $10 billion might reduce the Gini by 0.5%. Another reform with the same budget cost might reduce it by 0.2%. The difference reveals different distributional philosophies embodied in policy design.

Inequality measures complement poverty measures. A reform could reduce poverty while increasing inequality (by benefiting the near-poor more than the poorest). Or it could reduce inequality while having minimal poverty impact (by redistributing among the middle class).

PolicyEngine doesn't tell you which outcomes to prefer. It tells you what the outcomes are.

---

## The Neutrality Challenge

When PolicyEngine shows that a reform costs $2 billion and reduces poverty by 0.3%, is that good or bad?

The tool deliberately does not answer this question. Different people have different values. Some prioritize budget savings. Some prioritize poverty reduction. Some care most about work incentives, or inequality, or specific demographic groups.

This neutrality is intentional but difficult. The choice of what outputs to display is itself a normative choice. Showing poverty rates implies they matter. Showing distributional charts by income decile frames analysis in a particular way.

The team navigates this by:

1. **Comprehensive outputs**: Show budget, poverty, inequality, distribution by multiple cuts—let users focus on what they care about.

2. **No editorial commentary**: The tool doesn't say "this reform is good" or "this reform is bad." It shows numbers.

3. **Transparency about assumptions**: When behavioral responses are modeled, they're documented. When data has limitations, they're acknowledged.

4. **Open methodology**: Anyone can see how calculations work and challenge assumptions they disagree with.

This isn't perfect neutrality—that's impossible. But it's a deliberate effort to separate analytical infrastructure from advocacy.

---

## Validation and Trust

Society-level estimates carry more uncertainty than household calculations. The sample is weighted, the data is imputed, the interactions are complex. How do you know if the estimates are right?

PolicyEngine approaches validation systematically {cite}`policyengine2024ukvalidation`. Compare model outputs to official statistics. Match aggregate tax revenue to IRS totals. Match benefit expenditure to agency reports. Match poverty rates to Census publications.

When discrepancies appear, investigate. Sometimes the model is wrong—fix it. Sometimes the official statistics are based on different assumptions—document the difference. Sometimes the comparison reveals interesting facts about how programs actually work.

The enhanced microdata process itself is validated. Hold out some administrative targets during reweighting, then check how well the reweighted sample matches those holdout targets. If the sample matches training data but not holdout data, the procedure has overfit and needs adjustment.

No microsimulation model perfectly matches reality. But systematic validation makes the model's limitations knowable rather than hidden.

---

## Real-Time Policy Analysis

The society view enables a form of policy analysis that wasn't previously possible outside government: real-time response to policy proposals.

When Congress debates expanding the Child Tax Credit, PolicyEngine can show the distributional impacts within hours. When a state considers changing its EITC, the model can estimate effects before the vote {cite}`policyengine2022review`.

This speed matters. Policy debates often proceed faster than traditional analytical processes. By the time a think tank publishes a detailed study, the legislative moment may have passed. Real-time tools change who can participate in the debate.

In the UK, PolicyEngine produced analysis of Prime Minister Liz Truss's tax cuts within hours of their announcement—the only independent distributional estimates available while the policies were being debated {cite}`policyengine2022review`.

> "When the Chancellor announced a budget, PolicyEngine had analysis published within a day."

This capability depends on having the model already built and maintained. The investment is in infrastructure, not in each individual analysis.

---

## From Analysis to Platform

The society view is powerful for producing estimates. But its deeper value may be in enabling others to produce their own.

Think tanks use PolicyEngine to power their research. Advocacy organizations model their preferred reforms. Journalists fact-check claims about policy costs. Academic researchers run simulations without building models from scratch.

Each use case has different needs. Researchers want detailed methodology documentation. Advocates want shareable results they can embed. Journalists want quick answers they can verify. Policymakers want comparisons across multiple options.

The same underlying microsimulation engine serves all these users. What varies is the interface, the outputs emphasized, the level of technical detail exposed.

This is the platform potential of open-source policy analysis. Not just a tool that produces estimates, but infrastructure that others can build on.

---

## References

```{bibliography}
:filter: docname in docnames
```

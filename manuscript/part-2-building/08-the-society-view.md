# Chapter 8: The Society View

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

The Current Population Survey has known limitations {cite}`policyengine2022enhanced`. Bruce Meyer and colleagues have documented what they call a crisis in household survey data: declining response rates, rising imputation, and systematic underreporting that distorts our picture of poverty and program effectiveness {cite}`meyer2015underreporting`.

The underreporting is severe. Studies find 40-50% of SNAP recipients don't report their benefits in the CPS. Over 60% of TANF and General Assistance goes unreported. Housing assistance is missed by a third of recipients. This means surveys systematically undercount the safety net—making programs appear less effective than they actually are.

The problem runs in both directions. Seniors underreport retirement income, particularly IRA and 401(k) withdrawals that occur irregularly rather than as monthly pension checks. A Census Bureau study found median household income for those 65+ was 30% higher in administrative records than in survey data {cite}`census2017retirement`. The result: CPS-based poverty rates for seniors (9.1%) were 2.2 percentage points higher than rates calculated using validated administrative data (6.9%). Senior poverty is real, but it's not as high as the headline numbers suggest.

High incomes are top-coded, distorting estimates of policies affecting top earners. The sample is too small for reliable state-level analysis. Asset information is missing, making wealth-based policies unmeasurable.

> "These limitations can reduce the accuracy and usefulness of the CPS for policy simulations. For example, CPS-based projections will tend to underestimate the budgetary impacts of reforming SNAP or instituting a tax on top earners."

PolicyEngine addresses these problems through data enhancement—a technical process that combines multiple data sources using machine learning techniques {cite}`policyengine2022enhanced`.

The process works in stages. First, replace reported taxes and benefits with computed amounts from the microsimulation model, ensuring internal consistency. Second, integrate IRS tax records to correct income distributions, using quantile regression rather than simple matching. Third, reweight the sample using gradient descent to minimize divergence from known administrative totals. Fourth, incorporate additional surveys—the Survey of Consumer Finances for wealth, the Consumer Expenditure Survey for spending patterns.

The result is an enhanced dataset that matches official aggregates more closely than the raw CPS. Budget estimates become more reliable. Distributional analysis becomes more accurate. State-level analysis becomes possible.

---

## Budget Scoring

The most basic question about any policy reform: what does it cost?

Budget scoring is the bread and butter of policy analysis. When a legislator proposes expanding the EITC, the first question is always "how much?" When an advocate proposes a new child benefit, feasibility depends on the price tag. And when a senator needs a revenue estimate before markup, the number determines whether the amendment survives.

PolicyEngine calculates net budget impact by summing changes in tax revenue and benefit expenditure across all households. The fully refundable CTC example costs $2 billion because the additional credits paid out exceed any behavioral responses or interactions with other programs {cite}`policyengine2023scoring`.

The calculation is conceptually simple but computationally intensive. For each of the roughly 100,000 weighted household records in the enhanced dataset, the model runs two simulations: one under current law, one under the reform. The difference in total government revenue and spending, summed across all records with appropriate weights, yields the budget estimate. The whole process takes seconds on a modern server—but under the hood, it's evaluating millions of individual program eligibility checks, tax bracket calculations, and benefit phase-outs.

But budget impact isn't a single number. It varies by:

- **Year**: Tax provisions phase in and out. Inflation adjusts thresholds. Economic conditions change. A reform that costs $10 billion in its first year might cost $15 billion by year five as more people become eligible.
- **Baseline**: Impact relative to current law differs from impact relative to scheduled future law. If the TCJA individual provisions are set to expire, scoring an extension requires specifying whether the baseline includes or excludes that expiration—a choice that can swing estimates by hundreds of billions.
- **Behavioral assumptions**: Do people work more or less in response to changed incentives? Static estimates ignore behavioral response. Estimates with labor supply elasticities may reduce projected costs (if people work more) or increase them (if they work less).

PolicyEngine shows budget impact as a primary output, but contextualizes it with distributional analysis and household examples that reveal what the numbers mean. A $50 billion reform means little in isolation—it matters whether it's $50 billion concentrated on families in poverty or $50 billion distributed across the income spectrum.

---

## Poverty Impact

Reducing poverty is often the stated goal of tax-benefit reforms. But what does "reducing poverty" actually mean, and how do you measure it?

PolicyEngine uses the Supplemental Poverty Measure (SPM), which the Census Bureau introduced in 2011 as a more comprehensive alternative to the Official Poverty Measure {cite}`policyengine2023sex`. Unlike the older measure, the SPM accounts for taxes, in-kind benefits like SNAP, geographic variation in housing costs, work expenses, and out-of-pocket medical spending. For a family of four (two adults, two children) renting their home, the 2024 SPM threshold is about $39,000—meaning a family with resources below that level is considered in poverty {cite}`bls2024spm`.

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

This speed matters. Policy debates often proceed faster than traditional analytical processes. Traditional think tank analysis takes weeks or months: a team reads the legislation, codes it into their model, runs the simulations, writes up findings, goes through review. By the time the study is published, the legislative moment may have passed. Real-time tools change who can participate in the debate—and when.

The model's speed comes from pre-investment. Building and maintaining the microsimulation engine takes years. But once the infrastructure exists, analyzing a new reform takes hours or days, not weeks. The marginal cost of each analysis is low because the fixed cost of the underlying model has already been paid.

Consider the sequence when a major tax proposal is introduced. First, the policy parameters need to be translated from legislative text into model inputs—tax rates, thresholds, phase-out schedules. PolicyEngine's parameter system is designed for this: each program variable is separately adjustable. Second, the simulation runs across the full microdata sample. Third, the outputs—budget impact, poverty rates, distributional charts—are generated automatically.

**The UK Truss episode.** In September 2022, when Chancellor Kwasi Kwarteng announced what became known as the "mini-budget"—eliminating the 45p additional rate of income tax, cutting the basic rate from 20p to 19p, and reversing a planned National Insurance increase—PolicyEngine UK published distributional analysis within hours {cite}`policyengine2022review`. The estimates showed the package overwhelmingly benefiting higher earners: the top decile gained an average of £2,500 per year while the bottom decile gained essentially nothing. These were the only independent household-level distributional estimates available during the critical first days of debate. Media outlets cited the analysis. Within weeks, the government reversed course on the 45p rate abolition; within a month, Truss resigned.

**The US CTC debate.** When proposals circulated in 2024 and 2025 to expand the Child Tax Credit, PolicyEngine could show the trade-offs of different design choices in real time. Making the credit fully refundable cost more but delivered more to the poorest families. Increasing the per-child amount had a different distributional profile than lowering the phase-in threshold. For each variant, PolicyEngine produced budget scores, poverty impacts, and decile-level distributional charts—the same outputs that JCT and TPC produced, but available instantly and queryable by anyone.

This capability depends on having the model already built and maintained. The investment is in infrastructure, not in each individual analysis. And it compounds: each reform analyzed adds to the library of examples, builds user trust, and reveals edge cases that improve the model.

---

## From Analysis to Platform

The society view is powerful for producing estimates. But its deeper value may be in enabling others to produce their own.

Think tanks use PolicyEngine to power their research. Advocacy organizations model their preferred reforms. Journalists fact-check claims about policy costs. Academic researchers run simulations without building models from scratch.

Each use case has different needs. Researchers want detailed methodology documentation and API access for running thousands of scenarios. Advocates want shareable results they can embed in op-eds and campaign materials. Journalists want quick answers they can verify—and crucially, they want to be able to show their work. Policymakers want side-by-side comparisons across multiple reform options.

The same underlying microsimulation engine serves all these users. What varies is the interface, the outputs emphasized, the level of technical detail exposed. The web application provides the most accessible interface—anyone with a browser can run analyses. The Python package provides programmatic access for researchers who need to run custom scenarios, iterate over parameter spaces, or integrate with other tools. The API enables third-party applications to incorporate PolicyEngine's calculations into their own products.

This layered architecture—web application, Python package, API—means the society view can scale in multiple directions simultaneously. A nonprofit advocating for expanded childcare subsidies can model their proposal on the website. A university researcher studying the interaction between SNAP and the EITC can use the Python package to simulate hundreds of reform variants. A fintech company building a financial planning tool can call the API to show users how policy proposals would affect their household.

The platform model also changes the dynamics of policy debate. When analysis is a one-time product—a report published by a think tank—the debate is about whether to trust that specific report. When analysis is infrastructure that anyone can use, the debate shifts to whether the underlying model is sound. That's a more productive conversation, because model quality is testable and improvable in ways that report credibility is not.

This is the platform potential of open-source policy analysis. Not just a tool that produces estimates, but infrastructure that others build on—extending the analytical capacity of every organization that uses it.

---

## References

```{bibliography}
:filter: docname in docnames
```

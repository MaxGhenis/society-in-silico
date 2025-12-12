# Chapter 1: The Birth of Microsimulation

In 1957, an economist named Guy Orcutt published a paper that almost nobody read {cite}`orcutt1957new`. It appeared in the *Review of Economics and Statistics*, a respectable but not glamorous journal. The title was dry: "A New Type of Socio-Economic System." The prose was dense with equations. And the idea at its core was so far ahead of existing technology that it would take nearly two decades to build a working version.

But that paper planted a seed. Every time you use a tax calculator, every time a government agency estimates who will benefit from a policy change, every time someone asks "what would this reform mean for families like mine?"—they're using tools that trace back to Orcutt's vision.

This is the story of how one frustrated economist imagined simulating society from the bottom up.

---

## The Engineer Who Became an Economist

Guy Orcutt came to economics through an unusual path. Trained as an electrical engineer and physicist, he viewed the world as a system to be understood and improved. In his autobiographical reflections, he described "my early fascination with science, my transition from engineering to economics."

Inspired by the econometric work of Jan Tinbergen, the young Orcutt harbored what he called his "Tinbergen dream"—building a model that could capture an entire national economy. Early in his career, he even built an analogue electrical-mechanical "regression analyzer" to calculate statistical estimates. He thought like an engineer: if you want to understand a system, you build a model of it.

But as he worked with macroeconomic models through the 1940s and early 1950s, frustration mounted. The models could predict aggregates—GDP, inflation, unemployment. What they couldn't do was tell you what would happen to actual people.

---

## The Problem with Averages

To understand what Orcutt was reacting against, you need to understand how economists thought about the economy in the 1950s.

The dominant approach was macroeconomic modeling. Economists built systems of equations describing aggregate relationships: total consumption as a function of total income, investment as a function of interest rates, employment as a function of output. These models could predict GDP growth or inflation. They helped governments understand business cycles and plan fiscal policy.

But they had a fundamental limitation. As Orcutt put it, with characteristic understatement:

> "Existing models of our socio-economic system have proved to be of rather limited predictive usefulness."

The problem wasn't the math. The problem was what the math could answer. Macro models told you about averages. They could not tell you about distributions.

Consider a tax cut. A macro model might estimate its effect on total consumption. But it couldn't tell you which families would benefit most. It couldn't distinguish between a tax cut that helps the middle class and one that helps the wealthy. It couldn't show you that a policy with the same aggregate cost might have vastly different effects on poverty, depending on how it was structured.

And yet these distributional questions were exactly what policymakers needed to answer.

---

## The Aggregation Problem

Orcutt's insight was that aggregation itself was the problem—not just a limitation but a fundamental mathematical error.

He illustrated this with a simple example. Suppose you have 100 people, and the relationship between some input X and output Y is nonlinear—say, Y = X². If all 100 people have X = 1, the total output is 100. But what if 50 people have X = 0 and 50 have X = 2? The average X is still 1. A macro model would predict the same total output: 100.

But do the math at the individual level. Fifty people contribute 0² = 0, and fifty contribute 2² = 4. Total output: 200.

The aggregate is the same, but the outcome differs by a factor of two.

> "There is an inherent difficulty, if not practical impossibility, in aggregating anything but absurdly simple relationships about elemental decision-making units."

This wasn't just a theoretical curiosity. Tax systems are nonlinear—full of thresholds, phase-outs, and cliffs. Benefit programs have eligibility rules that depend on specific household circumstances. The real world is dense with the kind of discontinuities and nonlinearities that make aggregation treacherous.

Orcutt's conclusion was radical: if you want to understand how policy affects people, you have to model people.

---

## A New Type of Model

What would that look like?

Orcutt proposed a model built from "interacting units which receive inputs and generate outputs." The units would be actual decision-makers: individuals, households, firms. Each would have characteristics drawn from real data. Each would follow behavioral rules—some deterministic, some probabilistic.

> "The most distinctive feature of this new type of model is the key role played by actual decision-making units of the real world such as the individual, the household, and the firm."

Instead of aggregate equations, you would have a simulated population. Instead of predicting economy-wide averages, you would simulate what happens to each unit, then add up the results.

> "Predictions about aggregates will still be needed but will be obtained by aggregating behavior of elemental units rather than by attempting to aggregate behavioral relationships."

This inversion—derive aggregates from individuals, don't impose relationships on aggregates—was the conceptual breakthrough.

Orcutt called it "microanalytic simulation." Later generations would shorten this to "microsimulation."

---

## The Vision Exceeds the Technology

There was just one problem: the vision was decades ahead of the tools.

In 1957, computers filled rooms and cost millions of dollars. Programming meant punch cards. A dataset of 10,000 households—modest by modern standards—represented an enormous computational burden. And Orcutt wasn't proposing to simulate households once. He wanted to project them forward in time, modeling births and deaths, marriages and divorces, job changes and retirement. Each household would accumulate a life history. The model would track it all.

> "The problem of keeping track of all possible paths and their respective probabilities appears rather appalling."

Orcutt knew this was hard. He published anyway. The idea mattered more than the implementation.

For the next decade, he built prototypes. In 1961, he produced a working microsimulation model—limited in scope but proof that the concept was viable {cite}`orcutt1961microanalysis`. But the gap between proof-of-concept and policy-relevant tool remained vast.

---

## The Treasury Connection

While Orcutt worked on his academic prototypes, microsimulation was quietly entering government.

Between 1962 and 1965, a young economist named George Sadowsky introduced computers for revenue estimation at the U.S. Treasury's Office of Tax Analysis {cite}`sadowsky1991computing`. This was practical, unglamorous work—building systems that could estimate how much a proposed tax change would cost or raise.

Sadowsky developed a microanalytic simulation model to analyze the revenue and distributional effects of preliminary versions of the Revenue Act of 1964. This was Orcutt's vision applied to immediate policy needs: simulate individual taxpayers, apply proposed tax rules, add up the results.

The Treasury model was simpler than Orcutt's dynamic vision—it didn't project households forward in time. But it demonstrated that microsimulation could answer real policy questions. The approach spread to other agencies. By the late 1960s, tax microsimulation was becoming standard practice in government budget analysis.

Sadowsky later spent time at the Brookings Institution and then the Urban Institute—where, not coincidentally, Orcutt would soon launch his most ambitious project.

---

## DYNASIM: The Eighteen-Year Wait

It wasn't until 1969 that Orcutt got the resources to build something at scale.

The Urban Institute, a newly founded think tank in Washington, D.C., hired him to lead a project called DYNASIM—Dynamic Simulation of Income Model. The ambition was comprehensive: simulate all major demographic and economic life events. Births. Deaths. Marriages. Divorces. Education. Employment. Disability. Retirement. Taxes. Benefits.

The technical constraints were still formidable. DYNASIM ran on a DEC system-10 mainframe using a custom software framework called MASH (Microanalytic Simulation of Households). It simulated 10,000 people—a tiny fraction of the U.S. population, but enough to draw statistical inferences.

The team worked for six years. In 1975, the first version was complete {cite}`soa1997dynasim`. Eighteen years after Orcutt's original paper.

That eighteen-year gap between vision and implementation tells you something important. Orcutt wasn't incrementally improving existing methods. He was proposing a different way of thinking about economic modeling. The technology had to catch up to the concept.

---

## What DYNASIM Could Do

Despite its limitations, DYNASIM could answer questions no macro model could touch.

Want to know how a proposed Social Security reform would affect different generations? DYNASIM could simulate cohorts aging through time, accumulating earnings histories, reaching retirement, and collecting benefits under alternative rules.

Want to understand the long-run fiscal implications of demographic change? DYNASIM could project population aging, labor force participation shifts, and their effects on tax revenue and benefit spending.

Want to see how a policy change interacts with existing programs? DYNASIM modeled the tax and transfer system as an integrated whole, capturing interactions that piecemeal analysis would miss.

The modules were organized by domain:

**Demographic Module**: Leaving home, births, deaths, partnership formation and dissolution, disability, education, location changes.

**Labor Market Module**: Labor force participation, hours worked, unemployment, labor income.

**Tax-Transfer and Wealth Module**: Capital income, major tax instruments, transfer programs, feedback loops to the macro economy.

This comprehensive scope came at a cost. DYNASIM was expensive to run, difficult to modify, and required specialized expertise. But it demonstrated that Orcutt's vision was more than a theoretical curiosity.

---

## The Family of Models

DYNASIM didn't stay alone for long.

Its success (and limitations) inspired adaptations around the world {cite}`li2014survey`:

- **CORSIM** (United States): A direct descendant, continuing the dynamic microsimulation tradition at Cornell.
- **CANSIM** (Canada): Adapted DYNASIM's framework for Canadian policy analysis.
- **SVERIGE** (Sweden): Applied the approach to Scandinavian welfare state questions.

Meanwhile, a parallel tradition emerged: static microsimulation. Where Orcutt's dynamic models projected forward in time, static models asked a simpler question: what would happen to today's population if we changed a policy today?

Static models sacrificed the life-course perspective for tractability. They could be updated faster, run more cheaply, and applied to more specific policy questions. The IRS, Congressional Budget Office, and Treasury all developed static tax models. The UK's Institute for Fiscal Studies built influential static models for budget analysis.

Both traditions—dynamic and static—descended from Orcutt's insight that modeling individuals was the path to understanding distributions.

---

## The Micro-Macro Distinction

The difference between microsimulation and macro modeling isn't just technical. It reflects different questions.

| Question Type | Macro Answer | Micro Answer |
|--------------|--------------|--------------|
| "Will GDP grow?" | Yes/No + magnitude | N/A (wrong tool) |
| "What will this cost?" | Aggregate estimate | Aggregate estimate (via summation) |
| "Who benefits?" | Cannot answer | Full distribution |
| "How many fall below poverty?" | Cannot answer directly | Exact count |
| "What's my marginal tax rate?" | Cannot answer | Household-specific |

Macro models are powerful for their intended purpose: understanding aggregate dynamics, business cycles, growth trajectories. But they're the wrong tool for distributional analysis.

And distributional analysis is what democracy demands. When legislators debate a policy, they need to know who wins and who loses. When citizens evaluate proposals, they want to know what it means for people like them. These questions require thinking at the individual level.

Orcutt didn't invent concern for distribution. But he invented the computational framework for taking it seriously.

---

## Why It Matters Beyond Economics

Orcutt was an economist, and his examples were economic: taxes, income, consumption. But the microsimulation idea has spread far beyond economics.

**Health policy**: Microsimulation models project how populations will age, develop diseases, and respond to interventions. The CDC uses microsimulation to estimate the effects of vaccination programs.

**Climate policy**: Integrated assessment models combine physical climate models with economic microsimulation to project how climate change affects different populations differently.

**Transportation**: Urban planners simulate how individuals choose routes, modes, and destinations to evaluate infrastructure investments.

**Epidemiology**: Disease spread models simulate person-to-person transmission through contact networks—a direct application of Orcutt's "interacting units" framework.

The common thread is the same insight Orcutt had in 1957: aggregate relationships hide distributional detail. If you want to understand how a system affects the people within it, you have to model the people.

---

## The Computational Revolution

What Orcutt couldn't anticipate was how completely the technology constraint would dissolve.

DYNASIM simulated 10,000 people on a mainframe. Today, a laptop can simulate millions. The computing power that cost millions of dollars in 1975 now fits in your pocket.

This has transformed what's possible:

**Scale**: Modern microsimulation models routinely use samples of hundreds of thousands or millions of records, enabling analysis of small subgroups that would have been statistically impossible with Orcutt's 10,000.

**Speed**: Calculations that took hours now take seconds. This enables interactive analysis, real-time policy calculators, and rapid iteration.

**Accessibility**: You no longer need mainframe access to run a microsimulation. The tools can be web applications. Anyone with a browser can explore policy impacts.

**Open source**: Code can be shared, inspected, and improved collaboratively. The methodological monopoly of government agencies and elite institutions is breaking down.

This last point—accessibility—would have been unimaginable to Orcutt. He was building tools for experts to inform policymakers. The idea that ordinary citizens might run their own policy simulations wasn't part of the vision. But it's where the vision leads.

---

## The Unfinished Revolution

For all this progress, Orcutt's vision remains incompletely realized.

Most microsimulation models are still proprietary, developed and maintained by government agencies or research institutions. The public can see their outputs but not their methods. This creates an asymmetry: the government can tell you what a policy costs, but you can't check their work.

Dynamic microsimulation—Orcutt's original ambition—remains difficult and expensive. Most practical policy analysis still uses static models, trading the life-course perspective for tractability.

Uncertainty quantification is primitive. Models produce point estimates ("this policy costs $50 billion") without confidence intervals. Users can't distinguish precise estimates from rough guesses.

Behavioral response modeling is contentious. How much do people change their behavior when incentives change? Static models assume no response. Dynamic models make assumptions that are often disputed.

And perhaps most fundamentally: microsimulation tells you what a policy would do, not whether you should do it. It's a tool for analysis, not a substitute for values. Different people can look at the same microsimulation output and reach different conclusions, because they weigh the outcomes differently.

---

## The Legacy

Guy Orcutt died in 2006, having seen his vision transform from impractical dream to standard methodology. Every modern tax calculator, every CBO budget score, every analysis of "who wins and who loses" uses tools that trace back to his 1957 paper.

But the deeper legacy isn't any particular model. It's a way of thinking—and, for Orcutt, a way of *acting*.

Recent scholarship has emphasized that Orcutt saw microsimulation not just as a tool for understanding society but for improving it {cite}`cheng2020orcutt`. As historian Hsiang-Ke Cheng put it, microsimulation was "an engine designed for not only scrutinizing the system but reengineering the society." The engineer who became an economist never lost his engineer's conviction that systems could be made to work better.

Before Orcutt, economists thought about the economy in terms of aggregates. After Orcutt, it became possible to think about the economy as a collection of individuals, each with their own circumstances, each affected differently by the same policy.

That shift—from averages to distributions, from economy to people—changed what questions economics could answer. And those questions turned out to be the ones that matter most for democratic deliberation.

A policy that looks good in aggregate might harm millions of specific people. A policy that helps "the economy" might leave the poorest households behind. The only way to know is to look at the distribution. And the only way to look at the distribution is to model the individuals.

That's Orcutt's insight. It's still being implemented, sixty-seven years later.

---

## Looking Ahead

Orcutt imagined simulating society from the bottom up. He couldn't have imagined how far the technology would advance—or how much further the vision could be pushed.

What if microsimulation models were open source, so anyone could inspect and improve them?

What if they were accessible through web interfaces, so citizens could run their own analyses?

What if they included uncertainty quantification, so users could distinguish confident estimates from guesses?

What if AI could call these models, making policy analysis available through natural language?

What if we could simulate not just how policies affect people, but how people's values evolve over time?

These questions—the subjects of the rest of this book—are extensions of Orcutt's original insight. The tools have changed. The computational constraints have dissolved. But the core idea remains: if you want to understand how society works, you have to model the people within it.

Guy Orcutt, working with punch cards and mainframes, couldn't build that world. But he could imagine it. And that imagination—captured in a dense, technical paper that almost nobody read—set the direction for everything that followed.

---

## References

```{bibliography}
:filter: docname in docnames
```

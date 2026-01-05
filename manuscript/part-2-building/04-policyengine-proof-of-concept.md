# Chapter 4: PolicyEngine - Proof of Concept

By late 2020, Nikhil Woodruff and I had a working microsimulation model of the UK tax and benefit system. OpenFisca UK could calculate taxes, simulate benefits, estimate the effects of policy reforms. But it lived in Python scripts that only programmers could run.

We'd seen this pattern before—Tax-Calculator, OpenFisca, every academic model. Powerful tools locked behind technical barriers. If you wanted to analyze a UBI proposal, you needed to install Python, learn the API, write code to define the reform, run simulations, interpret results. This worked for researchers comfortable with programming. It didn't work for the journalists, advocates, and policymakers who actually shaped policy debates.

The solution was obvious but ambitious: build a web application that put the full power of microsimulation in a browser. Anyone could design a reform, see the costs and distributional effects, understand the impact on their own household. No code required.

We called it PolicyEngine.

---

## Building the Application

The technical challenge was translating microsimulation—a fundamentally computational process—into an interface that felt intuitive. We built the system in layers.

**The model layer** ran in Python on cloud servers. OpenFisca UK encoded the tax and benefit rules as executable code. Feed it a household's circumstances and a policy reform, and it calculated the exact tax liability and benefit entitlement before and after the change.

**The API layer** wrapped the model in HTTP endpoints. The frontend sent requests describing households and reforms; the API ran simulations and returned results. This separation meant we could improve the model without rebuilding the interface, or redesign the interface without rewriting the model.

**The application layer** was a React web app that managed complexity. Users defined households by answering questions—income sources, number of children, housing costs. They specified reforms by adjusting sliders and toggles—income tax rates, benefit levels, eligibility thresholds. The app translated these interactions into API calls, ran simulations, and displayed results: budget impact, poverty changes, inequality effects, household-level impact.

The first version took months to build. Nikhil handled most of the engineering—API design, React components, state management. I focused on the policy logic—which parameters to expose, how to present results, what comparisons mattered.

We launched PolicyEngine UK in September 2021 {cite}`policyengine2021review`.

The premise was simple: enter a policy reform—raise income tax, increase child benefits, introduce a carbon dividend—and see the effects. Not abstract estimates, but specific numbers. The cost to the Treasury. The change in poverty rates. The impact on inequality. And critically: enter your own household circumstances and see what the reform would mean for you personally.

The response surprised us. Within weeks, advocacy groups were using PolicyEngine to design proposals. Parliamentary groups experimented with policies during presentations. When the Chancellor announced Autumn Budget changes to Universal Credit, we published analysis within a day {cite}`policyengine2021review`. News outlets cited our numbers.

In October 2021, we spun PolicyEngine off as a separate nonprofit organization. The mission statement evolved from "Make Everyone a Policymaker" to "Help People Understand and Change Public Policy." The second verb mattered—understanding was passive, changing required agency.

---

## Crossing the Atlantic

In March 2022, we launched PolicyEngine US {cite}`policyengine2022review`.

The US model was different—not just in the policies encoded, but in the entire structure of the challenge. The UK has a single national tax system, though Scotland sets its own income tax rates. The US has fifty states with separate income tax codes, plus a federal system of bewildering complexity.

We started with what we could model: federal income and payroll taxes, major benefit programs like SNAP and the EITC. The household calculator launched first—enter your circumstances, see your taxes and benefits. Then in July 2022, we added population impacts using the Current Population Survey, the same microdata foundation that official government estimates relied on {cite}`policyengine2022review`.

But state-level analysis remained incomplete. We began encoding state income taxes one by one: Maryland, Massachusetts, Oregon, New York, Pennsylvania, Washington. Each state had its own structure, its own EITC variants, its own quirks. By the end of 2022, we had modeled six states. Forty-four remained.

The gap between ambition and capacity was palpable. We wanted comprehensive coverage; we had a small volunteer team encoding policies in their spare time. We wanted immediate updates when policies changed; we struggled to keep models current. We wanted validation against official estimates; we often discovered discrepancies we couldn't easily resolve.

The proof of concept worked—people wanted accessible policy analysis—but scaling it would require more than enthusiasm and weekends.

---

## Who Used It

As PolicyEngine grew, we tracked how different groups engaged with the tool. The patterns revealed both what we'd built successfully and what remained aspirational.

Researchers found PolicyEngine could answer questions other tools couldn't. The Center for Growth and Opportunity used it to analyze how targeted cash assistance affects work incentives. The Social Market Foundation modeled cost-of-living responses. Academic economists cited PolicyEngine results in papers {cite}`policyengine2022review`. The academic use case worked because researchers needed flexibility—they wanted to test specific policy variants, compare alternatives, run sensitivity analyses. PolicyEngine provided that.

Advocacy groups discovered they could make quantitative arguments without hiring consultants. The Maryland Child Alliance analyzed child poverty policies. UBI Lab Northern Ireland modeled recovery basic income proposals. Organizations that had previously relied on government estimates or expensive think tank reports could now run their own simulations. This democratization mattered—it meant smaller organizations with limited budgets could participate in policy debates with numbers, not just narratives.

Journalists appreciated the speed. When UK Prime Minister Liz Truss announced tax cuts during her short-lived administration, we produced distributional analysis within hours. News coverage included our estimates before official government figures appeared {cite}`policyengine2022review`. The journalism use case revealed both capability and risk—we could move fast, but speed created pressure to avoid errors that would undermine credibility.

Policymakers themselves used the tool, though more cautiously. We presented to the US Congressional Budget Office, to UK Parliamentary groups, to the Green Party of England and Wales {cite}`policyengine2022review`. Staff members and elected officials ran scenarios, explored alternatives, asked "what if" questions. But official use remained limited—governments had their own models, their own methodologies, their own validation processes. PolicyEngine could inform but not replace official analysis.

And increasingly, developers built on our API. The Fund for Guaranteed Income integrated PolicyEngine to show pilot program participants how their benefits would change. Gary Community Ventures used the API in their tools. We weren't just a product anymore; we were becoming infrastructure.

---

## The Validation Challenge

Open-source meant anyone could inspect our code, but inspection didn't guarantee correctness. We invested heavily in validation, comparing PolicyEngine results to official calculators and published statistics.

The UK model performed well on standard cases. Our Universal Credit calculations matched HMRC's official calculator within pounds for typical households. Our income tax estimates aligned with ONS statistics at the aggregate level. But edge cases revealed gaps—housing benefit interactions with legacy benefits, Scotland-specific tax provisions, transition rules for households moving between programs.

The US model faced different challenges. With fifty state income tax systems, validation meant comparing against fifty different official sources—when those sources existed. Some states provided online calculators we could test against; others had rules buried in legislative text with no official tool to verify our implementation. Federal programs were better documented, but interactions between federal and state systems created combinatorial complexity.

We tracked our validation systematically. Each model had a test suite comparing PolicyEngine outputs to official calculations across hundreds of household scenarios. When discrepancies appeared, we investigated—was the bug in our code, the official calculator, or our interpretation of ambiguous rules? Sometimes we fixed our implementation. Sometimes we documented known differences. Occasionally we discovered errors in official tools and reported them.

The validation work was never finished. Policies changed constantly—tax brackets adjusted for inflation, benefit eligibility thresholds updated, new programs launched. Keeping models current required sustained attention. But validation mattered for credibility. If journalists, researchers, or policymakers were going to cite our numbers, those numbers needed to be defensible.

---

## From Tool to Infrastructure

By April 2024, we solved the problem that had frustrated me at the UBI Center: state-level analysis. PolicyEngine launched comprehensive income tax modeling for all 50 states and DC. Over 100 open-source contributors had encoded the nation's Byzantine patchwork of tax codes. What we couldn't find in 2019, we built by 2024.

The technical sophistication grew in parallel. In August 2025, we launched the Enhanced Current Population Survey, integrating five datasets using machine learning and calibrating to 9,168 administrative totals. The approach combined Quantile Regression Forests for imputation with gradient descent optimization for reweighting—techniques that cut our deviations from official statistics by 97 percent {cite}`policyengine2023enhanced`. We built two new open-source packages to do it: microimpute and microcalibrate.

But the real validation came from who started using it.

In September 2025, we signed a memorandum of understanding with the National Bureau of Economic Research to build an open-source emulator of TAXSIM, the tax calculator that has powered academic research since the 1970s. Over 1,200 papers had relied on TAXSIM. Brookings used it extensively. The Bureau of Labor Statistics used it for the Consumer Expenditure Survey. The Census Bureau evaluated it for the Supplemental Poverty Measure.

Daniel Feenberg, TAXSIM's creator, joined our advisory board and served as external mentor through our NSF grant. We were building the emulator to ensure researchers maintained access to these capabilities—but also to create something larger: a validation framework where multiple independent models could cross-check each other.

A month later, we signed a second MOU with the Federal Reserve Bank of Atlanta. Their Policy Rules Database covered benefits—SNAP, Medicaid, housing vouchers, childcare subsidies—complementing TAXSIM's focus on taxes. The database powered the Atlanta Fed's CLIFF tools, which Colorado's Workforce Development Council and New Mexico's Caregivers Coalition used to help families understand how earning more would affect their benefits.

The three-way validation approach was deliberate. When independently developed models agree on a calculation, researchers can trust the result. When they diverge, the differences reveal important questions about policy interpretation or implementation details. Having three models—PolicyEngine, TAXSIM, and the Policy Rules Database—helped isolate where discrepancies originated.

We were no longer just another microsimulation model. We had become the integrator, the platform that validated across Python and R, across taxes and benefits, across academic and government implementations.

And then came the UK.

In March 2025, HM Treasury published an Algorithmic Transparency Record revealing they had piloted PolicyEngine UK as a potential supplement to their official Intra-Governmental Tax and Benefit Microsimulation model. The Times reported that the tool "can more accurately predict the outcome of ministers' decisions and is expected to be used mostly in budget periods."

The Treasury highlighted our machine learning approach to fixing survey data errors—combining multiple years of the Family Resources Survey, using random forest models to impute missing income, employing gradient descent to reweight households. The same techniques we'd developed for the Enhanced CPS, now being evaluated by the UK government to supplement their internal models.

From frustrated researcher cobbling together tools in 2019 to government ministries piloting our models in 2025. Six years.

In 2025, MyFriendBen—a benefits screening platform—launched in North Carolina, Illinois, Colorado, and New York using PolicyEngine's API to calculate eligibility and benefit amounts. The tool achieved over 90 percent accuracy in six minutes, available in 12 languages. Colorado users discovered they were eligible for benefits averaging $1,500 per month—money they hadn't known they could access.

This was the vision from 2021: not just researchers using PolicyEngine, but PolicyEngine powering tools that helped people navigate the system. The API had become infrastructure for benefit access.

---

## What We Built, What Remained

By late 2025, PolicyEngine had evolved from a research tool to production infrastructure. We had comprehensive tax and benefit models for the US and UK. We had validation partnerships with NBER and the Atlanta Fed. We had government agencies piloting our models. We had developers building on our API.

But honest assessment revealed what we hadn't solved.

**Accuracy varied by use case.** Standard households with typical income sources—our models handled these well, often matching official estimates within percentage points. But unusual situations revealed limitations: households with complex business income, families transitioning between programs, edge cases where multiple policies interact in unexpected ways. We documented these limitations but couldn't eliminate them. Microsimulation is approximation; the question is whether the approximation is good enough for the decision at hand.

**Usability challenged non-experts.** The interface was simpler than programming, but modeling a complex reform still required understanding policy terminology, tax concepts, and the tool's limitations. We could explain that increasing the personal allowance reduces revenue, but users needed to know what a personal allowance was. We could show distributional effects across income deciles, but users needed to understand what that meant for actual families. The dream of "everyone a policymaker" remained aspirational—though "many more people than before" was real progress.

**Resources constrained what we could build.** A team of five staff plus volunteers maintaining models for multiple countries, responding to user requests, producing research, building new features, and keeping everything updated faced constant tradeoffs. Open source meant anyone *could* contribute, but production-quality policy analysis tools required sustained professional attention. We chose what to prioritize and accepted what we couldn't do.

The proof of concept had worked. We'd demonstrated that open-source, accessible, rigorous policy analysis was possible. But moving from proof of concept to sustainable infrastructure would require thinking differently about what PolicyEngine was and what it could become.

---

## References

```{bibliography}
:filter: docname in docnames
```

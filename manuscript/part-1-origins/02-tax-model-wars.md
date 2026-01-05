# Chapter 2: The Tax Model Wars

In 1983, a small think tank in London did something that would reshape policy analysis for decades: they built a tax-benefit model and used it to critique the government's budget.

The Institute for Fiscal Studies had existed since 1969, founded by four financial professionals frustrated by the opacity of UK tax policy {cite}`ifs2024history`. But TAXBEN—their microsimulation model of British taxes and benefits—gave them something new: the ability to run the numbers themselves. When the Chancellor announced a budget, IFS could simulate its effects on different household types within hours. Their "Green Budget" analyses became essential reading for journalists, politicians, and civil servants alike.

This was a small revolution. For the first time, an independent organization could challenge official government estimates with its own calculations. The asymmetry of information that had always favored those in power was beginning to crack.

But only beginning. Four decades later, that asymmetry persists—and understanding why requires tracing how tax microsimulation spread through governments, think tanks, and eventually into the open.

---

## The American Machinery

While IFS was building TAXBEN in London, American government agencies were constructing their own microsimulation apparatus—but behind closed doors.

The Joint Committee on Taxation, created in 1926, had long been Congress's official scorekeeper for tax legislation {cite}`jct2024history`. By the 1970s, JCT was developing sophisticated microsimulation models: an Individual Model, a Corporate Model, an International Cross Border Model, an Estate and Gift Model {cite}`jct2024revenue`. When a member of Congress proposed a tax change, JCT's models would estimate its cost. These estimates carried legal weight—the Budget Act of 1974 made JCT the official source of revenue estimates for Congress.

The Treasury's Office of Tax Analysis built parallel capabilities for the executive branch. George Sadowsky's work in the early 1960s had demonstrated what was possible {cite}`sadowsky1991computing`; by the 1980s, Treasury maintained the Individual Income Tax Model (ITM), regularly updated with fresh data from IRS tax returns.

The Congressional Budget Office, created in 1974 to give Congress independent analytical capacity, developed its own microsimulation models. For short-term tax analysis, CBO built models similar to JCT's. For long-term projections—especially Social Security—they developed CBOLT, the Congressional Budget Office Long-Term model {cite}`cbo2018overview`.

Outside government, the Urban Institute was building its own analytical infrastructure. Karen Smith joined Urban in the 1980s and would spend three decades developing microsimulation models for Social Security, pensions, taxation, and welfare reform {cite}`urban2024karensmith`. She played lead roles in both MINT (the Social Security Administration's retirement income model) and DYNASIM (Urban's flagship dynamic microsimulation). While Urban's models served government clients rather than challenging official estimates, Smith was building expertise that would bridge the mainframe era into the age of open source.

Three major government institutions, plus Urban's adjacent capacity. Billions of dollars in policy decisions riding on their outputs. And almost none of it was visible to the public.

---

## The Asymmetry Problem

Here was the situation by the 1990s: if you wanted to know how a tax proposal would affect federal revenue, you had to trust the government's numbers. You couldn't check their work. You couldn't see their code. You couldn't run alternative scenarios. The models were black boxes, and the keys were held by a small priesthood of government economists.

This created several problems.

**Trust deficits.** When JCT or Treasury produced an estimate that a politician disliked, they could dismiss it as biased without anyone being able to verify. When estimates turned out wrong—as they inevitably sometimes did—there was no way to understand why.

**Limited debate.** Policy discussions were constrained by what the official scorekeepers would analyze. Novel proposals that didn't fit their modeling frameworks often couldn't get scored at all, making them politically impossible regardless of their merits.

**Expertise hoarding.** The skills to build and maintain these models concentrated in a few institutions. Academic economists could study tax policy, but they couldn't replicate the government's analytical infrastructure.

**Democratic deficit.** Citizens and advocacy groups who wanted to understand how policies affected people like them had to take official estimates on faith. The asymmetry between governors and governed extended to the very tools used to evaluate policy.

Some academics pushed back. At the National Bureau of Economic Research, Daniel Feenberg began building TAXSIM in the early 1980s {cite}`feenberg1993taxsim`. By the 1990s, it had become internet-accessible—one of the first tax calculators available online. Feenberg would maintain TAXSIM for his entire career, a quiet but essential contribution that enabled generations of tax research. When researchers needed to calculate tax liabilities for survey respondents, TAXSIM was there—reliable, documented, freely available to academics.

But TAXSIM was a research tool, not a policy analysis platform. It calculated taxes for individual records; it didn't produce the aggregate estimates and distributional tables that drove policy debates. Feenberg had demonstrated that useful tools could be built outside government, even if they couldn't fully replicate official infrastructure. The question was whether anyone could go further.

---

## The UK Alternative

Across the Atlantic, a different model was emerging.

The IFS had shown that independent analysis was possible. But TAXBEN remained proprietary—academics and journalists could read IFS reports, but they couldn't run the model themselves.

The real breakthrough came from an unlikely source: the European Union.

In 1996, researchers led by Holly Sutherland began building EUROMOD—a tax-benefit microsimulation model that would eventually cover all EU member states {cite}`sutherland2013euromod`. The ambition was staggering: harmonize the wildly different tax and benefit systems of dozens of countries into a single analytical framework, enabling cross-national comparisons that had never before been possible.

EUROMOD was developed at the University of Essex, funded by European Commission research grants. And crucially, it was designed for broad access. Researchers could apply for access to the model, learn its methodology, and conduct their own analyses. The code wasn't fully open source, but the ethos was one of sharing rather than hoarding.

By 2021, EUROMOD had grown so successful that the European Commission took over its maintenance, transferring responsibility to the Joint Research Centre. The university-based project had become official EU infrastructure.

But Essex wasn't done. In 2018, with funding from the Nuffield Foundation, a team led by Mike Brewer spun off the UK component of EUROMOD into a new model: UKMOD {cite}`ukmod2020`. This time, they went further. UKMOD would be fully open source, freely available to anyone who wanted to use it.

"We wanted to democratize access to tax-benefit analysis," Brewer explained. The Scottish Parliament's research service started using UKMOD. So did NHS Health Scotland and the Welsh Government. For the first time, subnational governments in the UK had access to the same analytical tools as Westminster.

This openness enabled a new generation of independent analysts. Howard Reed had run TAXBEN at the IFS from 2000 to 2004, learning the craft of institutional model maintenance {cite}`northumbria2024reed`. After stints at IPPR as Chief Economist, he founded Landman Economics in 2008 and built his own Tax-Transfer Model. Reed used it to analyze Universal Basic Income, welfare reform, and the cumulative impact of austerity—producing the kind of detailed distributional analysis that had once been the exclusive domain of government and established think tanks. His goal, he said, was "a new settlement of the same scale and sustainability as the Beveridge-inspired reforms of 1945."

Malcolm Torry, directing the Citizen's Basic Income Trust, showed what civil society organizations could do with these tools {cite}`torry2019ubi`. Using EUROMOD, he conducted nearly a decade of research on basic income schemes, producing detailed analyses of costs, distributional effects, and implementation options. Torry's work demonstrated that advocacy groups could be rigorous analysts—if they had access to the right tools.

---

## The Open Source Wave

The 2010s brought a new possibility: fully open-source tax microsimulation.

In 2014, Matt Jensen founded the Open Source Policy Center at the American Enterprise Institute {cite}`aei2015taxbrain`. His diagnosis was blunt: "The closed-source approach to estimating the costs and economic impact of policies raises challenges, as there is limited accessibility and transparency in the process, leaving the public and many policymakers in the dark."

Jensen's solution was Tax-Calculator, an open-source microsimulation model of US federal income and payroll taxes. The lead developer, Martin Holmer, brought decades of microsimulation experience and a PhD from MIT {cite}`holmer2024profile`. Holmer built Tax-Calculator in Python, making it accessible to a new generation of analysts comfortable with modern programming languages.

Tax-Calculator joined a growing ecosystem: Tax-Data for preparing input files, Behavioral-Response for modeling how taxpayers react to policy changes, TaxBrain for web-based access. The whole suite was released under open-source licenses, with code on GitHub for anyone to inspect, use, or improve.

"By adopting an open source approach," Jensen said, "we are able to provide policy makers, journalists and the general public with the information they need to understand policy. We are also able to leverage the knowledge and interest of experts and the general public to improve our models and make government better."

The models found users. Tax-Calculator results informed policy discussions across the political spectrum. When the World Bank wanted to build tax microsimulation capacity in India, they asked Holmer to adapt Tax-Calculator for the Indian tax system—demonstrating that open-source approaches could scale internationally.

---

## The Landscape Today

By the 2020s, tax microsimulation had stratified into distinct tiers.

**Government models** remained the most authoritative for official purposes. JCT scores still determined what Congress believed policies would cost. Treasury estimates still informed Administration proposals. CBO projections still anchored long-term fiscal debates. These models had the best data—actual tax returns, confidential and comprehensive—and the institutional authority that came from decades of use.

**Established think tanks** operated the next tier. The Tax Policy Center (a joint venture of Urban Institute and Brookings) maintained a microsimulation model that could challenge government estimates {cite}`tpc2024model`. IFS continued to shape UK budget debates. These institutions had the credibility to be taken seriously, even when their numbers differed from official scores.

**Open-source projects** represented the newest tier. Tax-Calculator and UKMOD made it possible for anyone with technical skills to run tax simulations. They couldn't match government models' data quality, but they offered something government models couldn't: transparency, accessibility, and the ability to be adapted for new purposes.

**Civil society users** like Malcolm Torry demonstrated that the tools could be used effectively by advocates and independent researchers—blurring the line between analyst and advocate, but expanding who could participate in policy debates.

The asymmetry that had characterized the field for decades was finally beginning to break down. Not completely—government still had the best data, the legal authority, and the institutional credibility. But the monopoly on analytical capability was ending.

---

## What the Wars Revealed

The tax model wars weren't really about models. They were about power—specifically, the power to define what policies would cost and who they would affect.

When only government could run the numbers, policy debates were constrained by what government chose to analyze. When think tanks gained analytical capability, they could propose alternatives and critique official estimates. When open-source tools emerged, the barrier to entry dropped further.

Each expansion of capability shifted the terms of debate. IFS's independence from government gave it credibility to challenge official estimates. Tax-Calculator's open-source nature meant anyone could verify its methodology. UKMOD's free availability meant Scottish policymakers didn't have to rely on London for analysis.

But capability isn't enough. The best models in the world are useless if no one trusts them, understands them, or uses them appropriately. The next challenge wasn't building better models—it was making them genuinely useful for democratic deliberation.

That challenge would require going beyond tax microsimulation, beyond any single policy domain, to ask what it would mean to model society itself.

---

## References

```{bibliography}
:filter: docname in docnames
```

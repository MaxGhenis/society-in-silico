# Fact catalog — 01-introduction.md ("Introduction: The model and the world")

Source file: `manuscript/front-matter/01-introduction.md`

## Facts

### Westworld / Rehoboam frame
- The book's Westworld frame is Engerraund Serac, the antagonist of Westworld's third season, whose philosophy is that his job is not to predict the future but to create it. [BANNED as a verbatim quotation — "I don't predict the future. I create it." is NOT a real Serac line; it never appears in the show. Present it only as characterization, never in quotation marks. The nearest verbatim Serac line (S3E2 "The Winter Line," to Maeve) is "For the first time, history has an author." (corrected per primary source — see research/part345-verification.md correction #1) [@westworld2020winterline].]
- In the show, Serac built an AI called Rehoboam after watching a thermonuclear incident destroy Paris. (uncited — TV source)
- Rehoboam predicted individual human lives — when a person would get sick, lose their job, or die — and did not just forecast but manipulated society to make its predictions come true. (uncited — TV source)
- In the show, people who deviated from their predicted paths were flagged for "reconditioning." (uncited — TV source)
- The show's premise is that humans are "just a brief algorithm," reducible to code; its horror is one man controlling that algorithm without anyone else knowing. (uncited — TV source)
- The author watched Westworld's third season in 2020.
- The author had been building microsimulation systems since 2018 — computational models that predict how tax policies affect households and simulate entire economies with millions of synthetic people.
- Real-world analogues to Serac's system named in the text: governments use algorithmic risk scores to allocate child welfare investigations, set bail amounts, and flag potential fraud in benefit claims; insurance companies use uninspectable predictive models to set premiums; credit agencies reduce a financial life to a three-digit number using undisclosed methods. (uncited)

### "The AI can't do your taxes" — benchmark facts
- In July 2025, Column Tax released TaxCalcBench, a benchmark testing whether AI could correctly compute complete federal tax returns [@bock2025taxcalcbench].
- The benchmark gave frontier models the tax rules, the taxpayer's information, and unlimited thinking time [@bock2025taxcalcbench].
- The best-performing model, Gemini 2.5 Pro, got fewer than one in three returns right [@bock2025taxcalcbench].
- Claude Opus 4 managed 27% [@bock2025taxcalcbench].
- Comparison used: a $50 copy of TurboTax does this "without breaking a sweat." (rhetorical comparison)
- Failure mode: models used percentage-based bracket calculations instead of the IRS tax tables, producing returns off by $3–5 each time; they miscalculated credit eligibility and stumbled on supplementary forms; the pattern was consistent across every model tested [@bock2025taxcalcbench].
- In 2023, researchers at Johns Hopkins and the University of Maryland found GPT-4 answered only 67% of true/false tax questions correctly — better than chance, but not reliable enough for financial decisions [@blairstanek2023gpt4tax].
- By mid-2026, PolicyEngine's own benchmark, PolicyBench, scores "some twenty" frontier and open-weight models on complete household tax-and-benefit calculations drawn from realistic family circumstances [@policybench2026].
- PolicyBench found the best model still getting roughly one in six households wrong by more than a dollar, and most models missing a quarter or more [@policybench2026].
- The PolicyBench errors are characterized as family-level mistakes: the wrong Medicaid eligibility, the wrong SNAP amount, a credit granted to a household that doesn't qualify [@policybench2026].
- Stated cause of the limitation: tax law changes every year; fifty states have different rules; benefit eligibility depends on dozens of interacting variables; the combinatorial complexity exceeds what pretraining can memorize.

### Comprehensive-engine gap
- No comprehensive tax-and-benefit engine exists as unified public infrastructure (as of writing).
- Point solutions named: Avalara handles sales tax; ADP handles payroll; TurboTax handles filing.
- The unanswered full-stack question: given a specific household in a specific state, what are all their taxes and all their benefits, how do they interact, and what happens when you change the rules — the question microsimulation was built to answer, connecting a 1957 academic paper to a 2025 AI benchmark failure.

### "Why now" — the three trends and their supporting facts
- Twenty years ago, knowing how a tax reform would affect American families meant two options: read the CBO score (a single national number) or hire a consulting firm to run proprietary models.
- Ten years ago, open-source tools like Tax-Calculator and EUROMOD existed but required programming expertise and statistical training.
- Five years ago, PolicyEngine put microsimulation in a web browser, but the audience was still mostly policy professionals.
- Trend 1 — AI systems are becoming the primary interface for information: people increasingly ask an AI assistant (e.g., "how much would I get from the Child Tax Credit?") rather than navigating IRS.gov; the accurate-answer infrastructure AI systems would call doesn't exist as a unified, production-ready service, so each company building AI assistants solves the tax-and-benefits problem from scratch or gets it wrong.
- Trend 2 — Policy complexity is accelerating: the US tax code has roughly doubled in length since 1985 (uncited); federal + state + means-tested benefit interactions create combinatorial explosion; a single parent earning $35,000 in Texas faces a different effective tax rate than the same parent in New York — potentially by thousands of dollars (illustrative).
- Trend 3 — Open-source infrastructure has matured: PolicyEngine covers US federal taxes plus all fifty states, the UK, and Canada, maintained by more than 100 open-source contributors (uncited); EUROMOD covers twenty-seven EU countries (uncited); OpenFisca has been deployed on four continents (uncited).

### "What simulation reveals" — the benefit-cliff example and microsimulation definition
- Illustrative case: a single parent in Ohio earning $45,000 with two children, deciding whether to accept a promotion that would raise her salary to $55,000. (illustrative)
- As earnings rise toward $55,000, the EITC she collected at $45,000 phases out entirely, SNAP benefits shrink, and — depending on state and childcare arrangement — a subsidy can vanish at a hard threshold; the share of each additional dollar kept can stay strikingly low across that range. (illustrative)
- For families who hit a hard threshold, losses can bunch tightly enough that earning more leaves them with less — a "true benefit cliff" — said to affect millions of families every year. (uncited)
- Definition given: microsimulation calculates how policies affect specific households by applying the actual rules (every bracket, every phase-out, every eligibility test) to specific circumstances, then aggregates across a representative sample of the population.
- Congressional CTC example: when Congress debates expanding the Child Tax Credit, microsimulation answers how much it would cost, which families would benefit, and whether/by how much it would reduce poverty — as calculations applying proposed rules to millions of synthetic households drawn from actual survey data.
- UK example: when the UK Chancellor announces changes to Universal Credit taper rates, a model can show a single parent working 25 hours/week at minimum wage keeps an additional £1,000 per year while a two-earner couple sees a smaller gain (illustrative — "can show").
- Scotland example: when Scotland sets different income tax rates from the rest of the UK, simulation reveals who wins and loses across the income distribution; "the tool is country-agnostic; the rules are country-specific."
- The idea goes back to 1957, when economist Guy Orcutt proposed modeling society from the bottom up — simulating individual households rather than relying on aggregate equations.
- Orcutt's insight: you learn more about how the economy works by tracking millions of individual families than by studying national averages.
- For decades the tools to realize Orcutt's vision were locked inside government agencies: the Congressional Budget Office, the Joint Committee on Taxation, the Treasury Department.
- Open-source microsimulation now lets anyone (researchers, journalists, advocates, curious citizens) run analyses that once required government resources; the code is public, the methodology inspectable, the results reproducible.

### "The stakes" — TCJA scoring
- AI assistants get tax questions wrong "a third of the time" (ties back to the TaxCalcBench result).
- When Congress debated extending the 2017 Tax Cuts and Jobs Act in 2025, the extension was ultimately enacted that July [@obbba2025].
- The ten-year cost estimates for the TCJA extension ranged from $4 trillion to $5 trillion depending on assumptions [@cbo2025tcja] — described as a trillion-dollar range.
- The official scorekeepers at the Joint Committee on Taxation used models the public couldn't inspect.
- Independent groups producing their own estimates, each with different data and methods: the Tax Policy Center, the Penn Wharton Budget Model, and PolicyEngine.
- Members of Congress voted based on whichever number supported their position.
- Illustrative uncertainty framing offered as the alternative: not "this reform costs $4.5 trillion" but "this reform costs $4.5 trillion, with a 90% confidence interval of $3.8 to $5.2 trillion, and here are the assumptions that matter most." (illustrative numbers)

### "What's ahead" — the four questions and the chapter map
- The book's organizing claim: every claim anyone makes about public policy decomposes into four questions — What does the law say? (rules, answerable exactly, checkable against the statute); Who are the people? (data, answerable statistically, checkable against surveys and administrative totals); What will happen? (prediction, checkable only when reality arrives); What do we want? (values, hardest to answer, easiest to smuggle into the other three).
- Stated discipline: every layer verified against ground truth, at the level of the individual unit — one rule, one household, one forecast.
- Chapter map (Part I: The closed stack): Ch 1 follows Guy Orcutt from his engineering background to the invention of microsimulation; Ch 2 maps the tax model wars (how scoring became institutional authority, and how a confidentiality statute became an analytical moat); Ch 3 confronts the accuracy question ("how good are these models, really—and how would you know?"); Ch 4 is the personal origin — the benefit cliff in the author's own family that turned the question from academic to urgent.
- Chapter map (Part II: The open engine): Ch 5 tells the PolicyEngine origin story; Ch 6 shows what the engine reveals for one household and for a country; Ch 7 dissects the three ingredients every microsimulation must solve — rules, data, and dynamics.
- Chapter map (Part III: The agent turn): Ch 8 shows why AI systems can't compute policy unaided (answer is tools, not training); Ch 9 reports on encoding the law at scale, by agents, under gates; Ch 10 confronts how you trust law encoded by machines; Ch 11 takes the method to countries that never had public models at all; Ch 12 explains why the organizations ended up mirroring the epistemology.
- Chapter map (Part IV: The prediction pole): Ch 13 exposes the uncertainty point estimates hide and the scoreboard being built to price it; Ch 14 benchmarks what language models actually add to opinion research.
- Chapter map (Part V: The horizon): Ch 15 models democratic processes; Ch 16 asks whether we can forecast how human values evolve and what that might mean for AI alignment; Ch 17 returns to the fork in the road — Serac's closed system versus the democratic alternative.
- The book ends where it started: at the choice between models that concentrate power and models that distribute it — a choice being made "right now, in code and policy and institutional design."
- Disclosure of interest: the author has built many of the tools described; chapters on his own systems (PolicyEngine, HiveSight, Democrasim, the institutions of Part III) are marked as such, and speculative chapters are labeled.
- Stated limits: the technology "won't save democracy, eliminate poverty, or solve AI alignment"; what it can do is make the invisible visible — the distributional effects hidden in policy details, the uncertainty masked by point estimates, the benefit cliffs that trap families.

### Citation keys used in this chapter (preserve exactly)
- [@bock2025taxcalcbench] — TaxCalcBench (Column Tax, July 2025)
- [@blairstanek2023gpt4tax] — Johns Hopkins / University of Maryland GPT-4 tax study (2023)
- [@policybench2026] — PolicyEngine's PolicyBench (mid-2026)
- [@obbba2025] — 2025 enactment extending the TCJA (enacted July 2025)
- [@cbo2025tcja] — CBO ten-year cost estimate for the TCJA extension

## Story beats

- 2020: author watches Westworld season 3; recognizes the Rehoboam technology because he has been building microsimulation systems since 2018; sees the show's writers taking the same tools to their darkest conclusion (a single closed AI controlling human destiny) and realizes it reveals a choice being made now.
- July 2025: Column Tax releases TaxCalcBench; frontier models given full rules/data/time still fail — Gemini 2.5 Pro (best) under 1/3 correct, Claude Opus 4 at 27% — establishing the book's opening technical fact that AI can't calculate taxes.
- 2023: Johns Hopkins / University of Maryland researchers find GPT-4 gets only 67% of true/false tax questions right — the earlier data point showing the limitation predates the frontier models.
- Mid-2026: PolicyEngine's PolicyBench scores ~20 models on full household calculations; best model still wrong on ~1/6 households by >$1, most missing a quarter or more — showing the limitation survived every model generation.
- 2025: Congress debates extending the 2017 TCJA; estimates from JCT (secret models), Tax Policy Center, Penn Wharton Budget Model, and PolicyEngine range $4–5 trillion over ten years; members vote on whichever number fits their position; the extension is enacted that July — the concrete stakes example.

## Quotes

- "For the first time, history has an author." — Engerraund Serac (Westworld, S3E2 "The Winter Line," 2020) [@westworld2020winterline]. (This is the verified verbatim line to use if the frame is quoted.) [BANNED: "I don't predict the future. I create it." is NOT a real Serac quote — never present it in quotation marks (corrected per primary source — see research/part345-verification.md correction #1).]
- "just a brief algorithm" — the stated premise of Westworld (the show's framing of humans as reducible to code). (No citation key.)
- "reconditioning" — the show's term for what happens to people who deviate from their predicted paths (Westworld). (No citation key.)

## Arguments

1. Language models can generate fluent explanations of tax law and summarize regulations, but they cannot calculate — apply specific rules to specific circumstances and produce a guaranteed-correct number.
2. Benchmarks prove it: TaxCalcBench (best model <1/3 correct; Claude Opus 4 = 27%), the 2023 GPT-4 study (67% on true/false), and PolicyBench in 2026 (~1/6 households still wrong) show the failure is consistent and persistent, not a rounding artifact.
3. The cause is structural: annually changing law × fifty state rulebooks × dozens of interacting eligibility variables exceeds what pretraining can memorize.
4. Therefore the fix is not better training but better tools — deterministic, auditable computational tools AI can call for exact answers — mirroring how AI calls calculators for arithmetic and physics engines for orbital mechanics rather than memorizing them.
5. The tools that matter most for policy questions are microsimulation models; but no comprehensive, unified, public tax-and-benefit engine exists (only point solutions like Avalara, ADP, TurboTax), so each AI builder re-solves the problem or gets it wrong.
6. This moment is different because three trends converge: AI is becoming the primary information interface; policy complexity is accelerating (tax code ~doubled since 1985; large cross-state effective-rate differences); and open-source infrastructure has matured (PolicyEngine across US+50 states+UK+Canada with 100+ contributors, EUROMOD across 27 EU countries, OpenFisca on four continents).
7. Microsimulation makes visible what aggregates hide — benefit cliffs, phase-out interactions, and distributional effects — by applying actual rules to specific households and then aggregating over representative survey samples; the method is country-agnostic while the rules are country-specific.
8. Powerful predictive models of people already exist and operate opaquely (government risk scores, insurance pricing, credit scoring); the real question is not whether such models exist but who controls them — decomposed as: who builds them (closed institutions vs open communities), who can access them (only the powerful vs everyone), and what they are for (optimization vs understanding).
9. The stakes are concrete: on the 2025 TCJA extension, secret and independent models disagreed by a trillion dollars and legislators cherry-picked; open, inspectable, reproducible, challengeable models with visible uncertainty would let disagreements be traced to specific assumptions and let citizens see a proposal's effect on their own household before a vote.
10. Every public-policy claim decomposes into four checkable questions — law (rules), people (data), prediction, values — and the book's discipline is to verify each layer against ground truth at the level of the individual unit (one rule, one household, one forecast).
11. Honest framing / anti-overselling: the technology won't save democracy, end poverty, or solve alignment; its contribution is making the invisible visible, and whether that improves decisions depends on what people do with it. This is "the case for the open path," not a neutral survey.

## Author-texture (verbatim, may be reused)

- The recognition beat that turns the Westworld recap personal (after the show summary): "When I watched this in 2020, I recognized the technology. I'd been building microsimulation systems since 2018—computational models that predict how tax policies affect households, that simulate entire economies with millions of synthetic people. The Westworld writers had taken the same tools and followed them to their darkest conclusion."
- The fork-in-the-road turn (closing the opening section): "That's the fork in the road. That's what this book is about."
- The tools-not-training analogy (from "The AI can't do your taxes"): "AI systems don't memorize multiplication tables—they call calculators. They don't learn orbital mechanics from scratch—they call physics engines. For the same reasons, they shouldn't try to memorize tax law. They should call a tax engine that encodes the rules exactly, traces each calculation to statute, and produces guaranteed-correct results."
- Orcutt's-insight line delivered in the author's voice (from "What simulation reveals"): "A 2% change in GDP tells you nothing about whether the people who need help are getting it. But simulate the change household by household—applying actual tax rules to actual income data—and you see what aggregate numbers hide: the family that falls through the cracks, the benefit cliff that punishes a raise, the interaction between programs that no single-program analysis reveals."
- The three-question "who controls them" chain (from "The stakes"), rendered as bolded questions with answers: "These models exist. The question is who controls them. / **Who builds them?** Closed institutions or open communities? / **Who can access them?** Only the powerful or everyone? / **What are they for?** Optimization or understanding?"
- The four-question decomposition, in the author's voice (opening of "What's ahead"): "Every claim anyone makes about public policy decomposes into four questions. **What does the law say?** — a question of rules, answerable exactly, checkable against the statute. **Who are the people?** — a question of data, answerable statistically, checkable against surveys and administrative totals. **What will happen?** — a question of prediction, checkable only when reality arrives. And **what do we want?** — a question of values, the hardest to answer and the easiest to smuggle into the other three."
- The anti-overselling close (penultimate paragraph): "The technology described in this book won't save democracy, eliminate poverty, or solve AI alignment. What it can do is make the invisible visible—the distributional effects hidden in policy details, the uncertainty masked by point estimates, the benefit cliffs that trap families."
- The one-line closer: "This is the case for the open path."

## Structural notes

- Job of the introduction: open with a vivid hook (the Westworld/Rehoboam closed-AI frame) that names the book's central choice (closed vs open computational models of society), then prove the core technical premise (AI can't calculate taxes → needs tools not training → the tools are microsimulation), argue "why now" (three converging trends), demonstrate what simulation reveals (the benefit-cliff example), state the stakes (TCJA scoring), introduce the four-question decomposition, and lay out the full 17-chapter / 5-part map.
- Required framing device #1 — the Rehoboam/Westworld frame: Serac's closed system that creates the future rather than predicting it is the book's antagonist metaphor; it opens the introduction and Ch 17 returns to it ("Serac's closed system versus the democratic alternative"). Preserve the frame and the closed-vs-open contrast. [Note: "predicts the future by creating it" here is a paraphrase of Serac's characterization, acceptable only if NOT set as a verbatim quotation; the fake line "I don't predict the future. I create it." is BANNED — the verbatim line is "For the first time, history has an author." (S3E2) [@westworld2020winterline].]
- Required framing device #2 — the four-questions map (law / people / prediction / values): this is the book's organizing spine; each question maps to a checkability standard and to parts/chapters. Ch 16 is where "what do we want?" (values) is tackled; the data question maps to Part II Ch 7; the rules question to Part III; the prediction question to Part IV.
- Required disclosure of interest: the introduction explicitly states the book is not a neutral survey, that the author built many of the tools, and that chapters on his own systems (PolicyEngine, HiveSight, Democrasim, the Part III institutions) and the speculative chapters are labeled as such. Keep this disclosure in any rewrite.
- Cross-references seeded here for later payoff: benefit cliff → Ch 4 (author's family) and Ch 6 (what the engine reveals); Guy Orcutt/1957 → Ch 1; tax model wars + confidentiality-statute-as-moat → Ch 2; accuracy/"how would you know" → Ch 3; PolicyEngine → Ch 5–7; AI-needs-tools → Ch 8; agent encoding under gates → Ch 9; trusting machine-encoded law → Ch 10; microsimulation-anywhere/new countries → Ch 11; org-mirrors-epistemology → Ch 12; uncertainty + scoreboard → Ch 13; LLMs in opinion research → Ch 14; simulated democracy → Ch 15; value forecasting + AI alignment → Ch 16; fork-in-the-road return → Ch 17.
- The introduction's chapter map is the most detailed statement of the book's structure and should be treated as canonical for the 17-chapter/5-part layout when reconciling with the preface's higher-level five-part sketch.
- The chapter carries a "## References" heading at the end (empty in the manuscript; Quarto/Pandoc auto-populates the bibliography from the [@key] citations at build time).
- Westworld quotations carry no citation keys in the manuscript; if a rewrite keeps them, cite [@westworld2020winterline]. CRITICAL: the line "I don't predict the future. I create it." is BANNED — it is not a real Serac quote. Use the verbatim line "For the first time, history has an author." (S3E2 "The Winter Line," 2020) instead, or present Serac's create-not-predict stance as unquoted characterization. ("just a brief algorithm" and "reconditioning" are genuine show terms and may stay.)

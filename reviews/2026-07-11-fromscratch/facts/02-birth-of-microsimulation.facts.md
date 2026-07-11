# Facts catalog — Chapter 1: The birth of microsimulation

Source: `manuscript/part-1-closed-stack/01-birth-of-microsimulation.md`

## Facts

- Guy Orcutt published a paper titled "A New Type of Socio-Economic System" in the *Review of Economics and Statistics* in 1957 [@orcutt1957new].
- The 1957 paper was dense with equations and read by almost nobody; the journal was respectable but not glamorous.
- Building a working version of Orcutt's proposed idea would take nearly two decades.
- Orcutt took a B.S. in physics from the University of Michigan in 1939 [@watts1991orcutt].
- Orcutt switched fields for his M.A. in 1940 [@watts1991orcutt].
- Orcutt earned his Ph.D. in 1944 [@watts1991orcutt].
- Near the end of his career, Orcutt referred to "my early fascination with science, my transition from engineering to economics" [@orcutt1990autobiography].
- Inspired by Jan Tinbergen's econometric models, Orcutt designed and built an analogue electrical-mechanical "regression analyzer" to produce statistical estimates [@cheng2020orcutt]. (Chapter does not state the location/institution where he built it. Task brief describes it as "regression analyzer at MIT," but the chapter text omits MIT.)
- Orcutt held what he called a "Tinbergen dream": a single model that could capture an entire national economy [@cheng2020orcutt].
- In 1949, with Donald Cochrane, Orcutt published a method for handling serial correlation in regression, known as the Cochrane-Orcutt procedure, still taught today [@cochrane1949orcutt].
- Orcutt directed the Littauer Statistical Laboratory at Harvard [@watts1991orcutt].
- Orcutt consulted for the Federal Reserve Board and the International Monetary Fund [@watts1991orcutt].
- In the 1950s the dominant approach in economics was macroeconomic modeling: systems of equations describing aggregate relationships (total consumption as a function of total income; investment as a function of interest rates; employment as a function of output). (uncited)
- The Cowles Commission was then the leading center for mathematical economics, pursuing Keynesian simultaneous-equation models. (uncited)
- Milton Friedman argued that the Cowles Commission's forecasts were no better than naive extrapolation. (uncited)
- Aggregation itself was Orcutt's identified culprit — framed as a mathematical error, not merely a limitation. (uncited; conceptual claim)
- The Y = X² toy example (data content): a nonlinear relationship between input X and output Y, with 100 people. If every person has X = 1, total output is 100. Split them into 50 people at X = 0 and 50 at X = 2: the average X is still 1, so a macro model built on the average still predicts 100. Computed at the individual level, the fifty zeros contribute nothing and the fifty twos contribute four apiece, for a total of 200. (The aggregate is identical; the individual-level truth is twice as large.)
- Tax systems are nonlinear — dense with thresholds, phase-outs, and cliffs; benefit programs turn on specific household circumstances. (uncited; conceptual)
- Isaac Asimov's *Foundation* trilogy (1951–53) introduced "psychohistory," a fictional science that predicted the behavior of vast populations through statistical law, with a built-in limit: it worked only for masses, never for a single person. [NEEDS CITATION: Foundation and Empire, 1952 bib entry]
- Orcutt named his method "microanalytic simulation"; later practitioners shortened it to "microsimulation."
- In 1957 computers filled rooms and cost millions; programming meant punch cards and assembly language. (uncited)
- The IBM 704, state of the art when Orcutt published, managed roughly 12,000 floating-point operations per second; a modern laptop does billions. [NEEDS CITATION: IBM 704 FLOPS rate]
- John von Neumann had cast weather forecasting as a computing problem before his death in 1957. (uncited)
- Herbert Simon and Allen Newell were writing the first artificial-intelligence programs at the Carnegie Institute of Technology in the late 1950s. (uncited)
- For four years after 1957, Orcutt built a prototype.
- In 1961, with three co-authors — one of them Alice Rivlin, his doctoral student — Orcutt published *Microanalysis of Socioeconomic Systems: A Simulation Study* [@orcutt1961microanalysis]. (The other two co-authors are not named in the chapter.)
- That book demonstrated a working, if limited, microsimulation of the US economy, modeling fertility, mortality, labor-force participation, and income through time.
- Fourteen years after 1961, Alice Rivlin became the first director of the Congressional Budget Office; she later served as vice chair of the Federal Reserve.
- Between 1962 and 1965, George Sadowsky brought computers to revenue estimation at the Treasury's Office of Tax Analysis [@sadowsky1991computing].
- Sadowsky built a microanalytic model to analyze preliminary versions of the Revenue Act of 1964; it was simpler than Orcutt's dynamic vision and did not age households forward.
- By the late 1960s, tax microsimulation was becoming standard in budget analysis.
- Sadowsky passed through Brookings and then the Urban Institute.
- Orcutt spent the decade after 1958 trying to build a full-scale microsimulation at the University of Wisconsin–Madison, where he founded the Social Systems Research Institute in 1959.
- The Wisconsin effort did not succeed: insufficient computing, wavering institutional support, ambition beyond what a university lab could sustain. Cheng's intellectual biography calls the Wisconsin years a "failed trial" [@cheng2020orcutt].
- The Urban Institute, a newly founded Washington think tank, hired Orcutt in 1968 to lead a project called DYNASIM (Dynamic Simulation of Income Model).
- By 1969 DYNASIM had the resources to begin in earnest; the ambition was to simulate every major life event (births, deaths, marriages, divorces, schooling, employment, disability, retirement, taxes, benefits).
- DYNASIM ran on a DEC System-10 mainframe using a custom framework called MASH, and simulated 10,000 people — enough to draw statistical inferences [@soa1997dynasim].
- The DYNASIM team worked six years; the first version was complete in 1975, eighteen years after the 1957 paper.
- DYNASIM's modules were organized by domain: one for demographic events, one for the labor market, one for taxes/transfers/wealth; it modeled the whole as an integrated system.
- The Urban Institute carried DYNASIM through successive generations: a narrower retirement-income version in the early 1980s; a major overhaul around 2000 that projected the US population across seventy-five years on the Social Security and Medicare trustees' assumptions; and a fourth generation still active today — among the longest-lived computational models in the social sciences [@soa1997dynasim].
- Steven Caldwell built CORSIM at Cornell, a direct descendant of DYNASIM, which in turn seeded POLISIM (for Social Security analysis) and DYNACAN (for Canadian pensions) [@li2013survey].
- Statistics Canada developed SPSD/M, a static Social Policy Simulation Database and Model that became a workhorse of Canadian tax-benefit analysis [@li2013survey].
- Sweden's SVERIGE modeled the country's entire population [@li2013survey].
- Static microsimulation asks what would happen to today's population under a policy changed today; the IRS, CBO, and Treasury all built static models. (uncited)
- In 1974, Joseph Pechman and Benjamin Okner of Brookings merged data on 72,000 households to ask who really bore the burden of American taxes [@pechman1974taxburden].
- Micro-macro distinction table (data content), rows = Question | Macro model | Microsimulation:
  - "Will GDP grow?" | Yes or no, with a magnitude | Not designed to forecast aggregates directly
  - "What will this reform cost?" | Aggregate estimate | Aggregate estimate, summed from units
  - "Who benefits?" | Cannot say | The full distribution
  - "How many fall below the poverty line?" | Cannot say directly | An exact count
  - "What is my marginal tax rate?" | Cannot say | Household-specific
- Microsimulation has since spread beyond economics: health researchers project how a population ages, develops disease, and responds to vaccination programs; climate models pair physical with economic projections to trace how warming lands on different households; transportation planners simulate individuals' choices of route, mode, and destination; epidemiologists model person-to-person transmission across contact networks. (uncited)
- DYNASIM simulated 10,000 people on a mainframe that cost a fortune to run; a present-day laptop simulates millions; computing power costing millions of dollars in 1975 now fits in a pocket. (uncited)
- Guy Orcutt died on March 5, 2006 [@prabook2024orcutt].
- Orcutt's daughter, Alice Orcutt Nakamura, became an economist.
- Orcutt's granddaughter, Emi Nakamura, won the John Bates Clark Medal in 2019 (awarded to the most promising American economist under forty).
- Historian Hsiang-Ke Cheng characterized microsimulation as "an engine designed for not only scrutinizing the system but reengineering the society" [@cheng2020orcutt].
- The chapter frames the 2026 payoff: Orcutt's "interacting units which receive inputs and generate outputs" are the per-unit encoding at the center of the book; building a society one unit at a time buys per-unit verifiability — each simulated household checkable against ground truth (its tax against the statute, its benefits against an administrative total, its forecast against the official number when it lands).

## Story beats

- **Orcutt's arc.** Physics B.S., University of Michigan, 1939 → M.A. 1940 → economics Ph.D. 1944. Built an analogue electrical-mechanical "regression analyzer" inspired by Tinbergen; held a "Tinbergen dream" of one model for a whole national economy. Co-created the Cochrane-Orcutt procedure (1949). Directed Harvard's Littauer Statistical Laboratory; consulted for the Fed and IMF. Grew frustrated that macro models could predict aggregates but not what happens to actual people. Published the 1957 paper. Founded the Social Systems Research Institute at Wisconsin (1959); the decade-long Wisconsin attempt to build a full microsimulation failed ("failed trial"). Hired by the Urban Institute in 1968 to lead DYNASIM; the first version completed 1975.
- **The Rivlin lineage.** Rivlin was a co-author on Orcutt's 1961 book as his doctoral student; fourteen years later she became the first director of the CBO and later Fed vice chair. The chapter stresses the through-line from Orcutt's obscure paper to CBO scoring machinery running "through one advisor-student relationship."
- **The Y = X² example (content).** 100 people; if all have X = 1, total = 100. Split 50 at X = 0 and 50 at X = 2: average still 1, macro prediction still 100, but individual-level total = 200. Used to show aggregation as mathematical error where relationships are nonlinear.
- **Sadowsky / Treasury.** 1962–65, a young economist brings computers to Treasury's Office of Tax Analysis; builds a microanalytic model for the Revenue Act of 1964 (static, no aging); first time a proposed tax change could be run against a sample of real taxpayers before enactment; later moves through Brookings to the Urban Institute — where Orcutt was about to attempt DYNASIM.
- **DYNASIM build.** DEC System-10 mainframe, MASH framework, 10,000 simulated people, six years of work, completed 1975 — eighteen years after the paper.
- **The family of models.** DYNASIM's descendants and cousins: CORSIM (Caldwell, Cornell) → POLISIM, DYNACAN; SPSD/M (Statistics Canada); SVERIGE (Sweden); and the static tradition, exemplified by Pechman & Okner's 1974 study of 72,000 households.
- **Three generations.** Orcutt (physicist) → daughter Alice Orcutt Nakamura (economist) → granddaughter Emi Nakamura (Clark Medal, 2019).

## Quotes

- Orcutt (1957 paper, understatement about macro models' blind spot): "Existing models of our socio-economic system have proved to be of rather limited predictive usefulness." (uncited in chapter; attributed to Orcutt)
- Orcutt: "There is an inherent difficulty, if not practical impossibility, in aggregating anything but absurdly simple relationships about elemental decision-making units." (in-chapter attribution to Orcutt; sentence sits in the §"The aggregation problem")
- Orcutt: the alternative was a model built from "interacting units which receive inputs and generate outputs." [@orcutt1957new]
- Orcutt: "The most distinctive feature of this new type of model is the key role played by actual decision-making units of the real world such as the individual, the household, and the firm" [@orcutt1957new].
- Orcutt: "Predictions about aggregates will still be needed but will be obtained by aggregating behavior of elemental units rather than by attempting to aggregate behavioral relationships." (attributed to Orcutt)
- Asimov (*Foundation and Empire*): "The reaction of one man could be forecast by no known mathematics; the reaction of a billion is something else again" [NEEDS CITATION: Foundation and Empire, 1952 bib entry].
- Orcutt (on the difficulty of dynamic paths): "The problem of keeping track of all possible paths and their respective probabilities appears rather appalling." (attributed to Orcutt)
- Orcutt (autobiographical): "my early fascination with science, my transition from engineering to economics" [@orcutt1990autobiography].
- Hsiang-Ke Cheng (historian): microsimulation was "an engine designed for not only scrutinizing the system but reengineering the society" [@cheng2020orcutt].
- Cheng (on the Wisconsin years): a "failed trial" [@cheng2020orcutt].
- Orcutt's own terms, verbatim: "Tinbergen dream" [@cheng2020orcutt]; "microanalytic simulation" (his name for the method).

## Arguments

1. Macro models can predict aggregates (GDP, inflation, unemployment) but cannot say what happens to actual people — which constituents gain and which fall behind. That distributional silence is precisely the question policymakers must answer.
2. Aggregation is not merely a limitation but a mathematical error when relationships are nonlinear: the average-based aggregate can diverge sharply from the individual-level truth (Y = X² gives 100 vs. 200 for the same average X).
3. Real tax-and-benefit systems are dense with the nonlinear discontinuities — thresholds, phase-outs, cliffs — that make aggregation treacherous exactly where policy matters.
4. Therefore, to understand how policy affects people you must model people: real decision-making units (individuals, households, firms) carrying data-drawn characteristics and following behavioral rules.
5. The inversion: derive aggregates by summing simulated individual behavior, rather than imposing behavioral relationships on aggregates. That reversal is the breakthrough.
6. Orcutt's method is granular and, in principle, democratic — the opposite of Asimov's psychohistory, which worked only for masses and could be read only by Hari Seldon and steered only by a secret Foundation. If any household can be simulated, anyone can ask how a policy lands on families like their own and check the answer against their own life.
7. The vision ran decades ahead of the hardware; the technology had to climb to meet it (~18 years to DYNASIM, 1975).
8. The technology constraint later dissolved almost completely (mainframe-to-laptop, batch-to-interactive, model-behind-a-web-page), making ordinary much of what Orcutt had been denied.
9. The lasting payoff is per-unit verifiability: modeling a society one unit at a time lets each unit be checked against ground truth (tax vs. statute, benefits vs. administrative total, forecast vs. official number). That check is the discipline the rest of the book is built on.

## Author-texture (verbatim, may be reused)

Chapter 1 is third-person historical exposition (no first person), so texture is sparse and mostly protected epigrammatic lines rather than personal scenes. Selectively preserved:

- "The aggregate is identical; the truth is twice as large." (protected — see Structural notes)
- "Orcutt knew it was hard. He published anyway." (the second sentence is a protected line)
- "He had spent years refining instruments that answered the wrong question with steadily improving precision."
- Chapter-closing forward hooks: "What if anyone could run a microsimulation, not just an agency with a mainframe? What if an AI could call one in plain language, on behalf of a person who never learned to code?"
- "The engineer never left the economist."

## Structural notes

- **Chapter's job in the book.** Opens Part I ("The closed stack"). Establishes the intellectual origin of microsimulation (Orcutt, 1957), the founding idea (model individuals, not aggregates), the aggregation-error argument, and the advisor-to-institution lineage (Orcutt → Rivlin → CBO). Ends by naming the book's central discipline: per-unit verifiability against ground truth.
- **Cross-references.** Forward to CBO/JCT/Treasury machinery (Chapter 2); forward to the three-level validation and admissibility rule (Chapter 3); forward to the per-unit-encoding thesis and "society in silico" payoff (rest of book). Note: Chapter 2 later refers to "the kind of work Karen Smith had been doing at Urban since the 1980s (chapter 1)," but the provided Chapter 1 text does not mention Karen Smith — a cross-reference that Chapter 1 as written does not support.
- **Protected lines** (task-flagged, preserve verbatim): "The aggregate is identical; the truth is twice as large." / "He published anyway."
- **Handoff.** Closes on two rhetorical questions (anyone-can-run-it; an AI calling a model in plain language) and the statement of per-unit verifiability as "the discipline everything ahead is built on." Hands off to Chapter 2's institutional/closed-apparatus story.

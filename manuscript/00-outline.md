# Society in Silico - Chapter Outline

## Front Matter

### Preface
- Why I wrote this book
- Who it's for
- How to read it (technical vs. narrative paths)

### Introduction: The Rehoboam Problem
- Westworld hook: Serac's deterministic prediction machine
- The recognition: I've been building something similar
- The key difference: open, democratic, uncertainty-aware
- The question: Can simulation help society realize its goals?
- Overview of the book's arc

---

## Part I: Origins
*How did we get here? The intellectual tradition behind microsimulation.*

### Chapter 1: The Birth of Microsimulation
**Research:** [[guy-orcutt]], [[microsimulation-definition]]

- Guy Orcutt's 1957 vision: simulate the economy household by household
- The audacity: 50 million households when computers filled rooms
- Why macroeconomic models weren't enough
- The gap between vision and capability
- Orcutt's legacy: DYNASIM, CORSIM, and descendants

### Chapter 2: The Tax Model Wars
**Research:** [[taxsim]], [[ifs-taxben]], [[tax-calculator]]

- How governments learned to simulate taxes
- The IFS and UK budget analysis tradition
- TAXSIM and US academic tax modeling
- The problem: these tools stayed inside institutions
- CBO, JCT, and the asymmetry of policy analysis

### Chapter 3: The Open Source Revolution
**Research:** [[openfisca]], [[rules-as-code]]

- OpenFisca: France opens its tax-benefit model
- Rules as code movement: legislation as software
- The democratization premise: if citizens can run the models, power shifts
- Limitations: technical barriers, data access, trust

### Chapter 4: The Accuracy Question
**Research:** [[simulation-accuracy]], validation cases

- Do these models actually work?
- The Penn Wharton validation: predicted vs. actual
- Where microsimulation succeeds and fails
- The honest answer: better than alternatives, not perfect

---

## Part II: Building
*What does it take to build open policy infrastructure?*

### Chapter 5: PolicyEngine - Proof of Concept
**Research:** [[policyengine]], [[ubi-center]]

- Origin story: UBI analysis needed cross-country tools
- The decision to build, not just use
- Technical choices: OpenFisca fork, web interface, API
- What "open" really means: code, data, methodology

### Chapter 6: The Household View
- The calculator: "What do I owe? What do I get?"
- Why personal relevance matters for policy understanding
- Marginal tax rates and the complexity people actually face
- Making the invisible visible

### Chapter 7: The Society View
- From households to populations: microsimulation at scale
- Distributional analysis: who wins, who loses
- Budget scoring: what does this cost?
- The neutrality challenge: analysis without advocacy

### Chapter 8: AI Enters the Picture
**Research:** [[ai-integration-philosophy]]

- How PolicyEngine uses AI: explanation, not calculation
- The insight: "LLMs will call tools"
- Deterministic backends for AI frontends
- Claude explains, the engine computes

### Chapter 9: Cosilico - Infrastructure for the Future
**Research:** [[cosilico]], PolicyEngine future state

- The next layer: agentic rule encoding
- Why PolicyEngine will use Cosilico (not maintain its own models)
- Validation against authoritative oracles
- Building infrastructure others can build on

---

## Part III: Future
*Where does this lead? The deepest questions.*

### Chapter 10: The Uncertainty Gap
**Research:** [[max-ai-portfolio]] Theme 6

- The dirty secret: microsimulation gives point estimates
- "This reform costs $50B" — but what's the confidence interval?
- Why uncertainty quantification matters for trust
- Partial solutions: Monte Carlo, Bayesian methods, squigglepy
- The aspiration: uncertainty-aware policy analysis

### Chapter 11: Simulating Opinion
**Research:** [[hivesight-silicon-sampling]], diversity problem

- HiveSight and silicon sampling
- The diversity problem: temperature isn't enough
- Microdata as the solution: structured human variation
- Can we simulate what people think? Should we?

### Chapter 12: Simulating Democracy
**Research:** [[democrasim-architecture]]

- From opinions to elections to policies
- The "accuracy" parameter: what informed voters provide
- Closing the loop: values → votes → policies → outcomes
- Democratic simulation as infrastructure

### Chapter 13: Simulating Values
**Research:** [[value-forecasting-alignment]] — THE CAPSTONE

- The deepest question: what would humanity want after reflection?
- Why current alignment approaches fall short
- The proposal: empirically validated value forecasting
- Heterogeneity as feature, not bug
- Uncertainty at two levels: aleatoric and epistemic
- From projection to alignment target
- The aspiration: AI aligned to our considered values, not our current ones

### Chapter 14: Society in Silico
- Returning to Rehoboam: what we're building isn't that
- Open vs. closed, democratic vs. authoritarian simulation
- The honest caveat: we're not done, we'll never be done
- Simulation as method, not destination
- An invitation to participate

---

## Back Matter

### Epilogue: The Work Ahead
- What's launching (Cosilico timeline)
- What's unfinished (uncertainty quantification, value forecasting experiments)
- How to contribute

### Appendix A: Technical Primer
- How microsimulation works (for non-technical readers)
- Key concepts: variables, parameters, reforms, microdata

### Appendix B: Try It Yourself
- PolicyEngine walkthrough
- Sample analyses readers can run

### Acknowledgments

### Notes & References

---

## Chapter-Research Mapping

| Chapter | Primary Research Notes |
|---------|----------------------|
| 1 | guy-orcutt, microsimulation-definition, dynasim |
| 2 | taxsim, ifs-taxben, tax-calculator |
| 3 | openfisca, rules-as-code |
| 4 | simulation-accuracy |
| 5 | policyengine, ubi-center |
| 8 | ai-integration-philosophy |
| 9 | cosilico |
| 10 | max-ai-portfolio (uncertainty theme) |
| 11 | hivesight-silicon-sampling |
| 12 | democrasim-architecture |
| 13 | value-forecasting-alignment |
| 14 | 00-thesis, rehoboam-contrast |

## Gaps to Fill

- [ ] Chapter 2: Need more on CBO/JCT institutional history
- [ ] Chapter 6-7: Need concrete PolicyEngine case studies
- [ ] Chapter 10: Need technical detail on uncertainty methods
- [ ] Chapter 13: Need to flesh out experimental design for value forecasting
- [ ] People: Need profiles for more historical figures (Ann Harding, etc.)

## Word Count Targets

| Section | Target |
|---------|--------|
| Front matter | 5,000 |
| Part I (4 chapters) | 20,000 |
| Part II (5 chapters) | 25,000 |
| Part III (5 chapters) | 25,000 |
| Back matter | 5,000 |
| **Total** | **80,000** |

~6,000 words per chapter average

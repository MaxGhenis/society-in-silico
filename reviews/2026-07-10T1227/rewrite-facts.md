# Rewrite fact sheet (2026-07-10) — the only source for new claims

Ground truth for the from-scratch rewrite, compiled from the author's strategy docs
and project state as of July 10, 2026. **Writing agents: every factual claim you add
that is not (a) in this sheet or (b) already in the May 30 manuscript with a
citation must be marked `[NEEDS CITATION: what to verify]` inline.** Never invent a
number, date, name, or quote. Where this sheet marks `[VERIFY]`, carry the marker
into the draft. Cite only BibTeX keys that exist in `references.bib` (read it).

## Hard prohibitions

- **Retired names — never present as current:** Cosilico (as the old infrastructure
  org), Brier Institute, Brier-1, Brier Almanac, Farness, Atlas (the corpus tool),
  RAC / AutoRAC (the format/pipeline), Axiom Labs, microplex, us-data/
  policyengine-us-data (as current). The data layer is called **populace**, full
  stop ("microplex is no more — it's all populace," author, 2026-07-10).
- **No forecast-validation claims.** The Thesis Institute has **zero
  witness-verified resolved forecasts** as of 2026-07-10. Never write "track
  record," "scored answers," "validated," "beats persistence," or any live-forecast
  accuracy claim. Allowed: "the scoreboard is live; every forecast carries an
  interval and will be graded when the official number lands; none have resolved
  yet." Historical *backtests* (the 17-variable GSS experiment) may be reported as
  backtests.
- **Never name** the Brussels/SILC custodian conversation partner, or any close-hold
  BD thread. (The Federal Reserve Bank of Atlanta naming is APPROVED by the author —
  keep existing mentions.)
- **No leaderboard decimals that will drift.** Describe PolicyBench standings in
  round terms ("roughly one in six household calculations wrong by more than a
  dollar for the best model, as of mid-2026"), cite the site, avoid two-decimal
  precision.
- **Do not present the commercial operator (Cosilico PBC) as launched.** See "The
  commons and its operators" below.
- Internal EUROMOD/UKMOD relationship strategy never appears; public treatment is
  respectful, factual, collaborative (we file bugs upstream and credit the
  reference models as essential oracles).

## The thesis and the admission rule

- The book's stated discipline (author's own formulation, 2026-07-10): **"Simulation
  is admissible only where its verification chain terminates in ground truth — a
  forecast score, an oracle parity, statutory exactness, a calibrated marginal."**
  Corollary the book states: agent scale without per-unit ground-truth verification
  is confident fiction.
- Organizing pattern for the projects: "agents can [VERB] the world's [CORPUS]" —
  Axiom = encode the world's policy corpus; populace = integrate the world's
  microdata; Thesis = forecast government metrics. Together: the analytic stack of
  government, rebuilt open. Gating test for any such project: per-unit
  verifiability against ground truth.
- Three primitives frame (author, 2026-07-10): rules (Axiom) + predictions (Thesis)
  + values elicitation (the nascent third — HiveSight is its embryo).

## Organizations (canonical, July 2026)

- **The Axiom Foundation** — Delaware nonprofit, fiscally sponsored by the PSL
  Foundation. Ariel Kennan, President (started July 1, 2026). Ballmer Group anchor
  funding. Max Ghenis, CEO. **Public launch July 28, 2026.** Site
  axiom-foundation.org; GitHub org TheAxiomFoundation. The determinism pole:
  "agents → determinism," encode the law exactly.
- **The Thesis Institute** — the prediction pole: "agents → prediction," forecast
  government metrics, including under policy counterfactuals. thesisinstitute.org;
  live app app.thesisinstitute.org with forecast pages (e.g., an unemployment-rate
  first-print forecast; "Medicaid call wait times in March 2027 if the
  work-requirement deadline is delayed"). Public launch ~September 15, 2026. Its
  ledger records first-print facts, resolution events, and scores; forecasts are
  graded when reality arrives. Zero resolved, witness-verified forecasts as of
  July 10, 2026.
- **Two-pole frame:** "Axiom states, Thesis predicts." An axiom is accepted truth;
  a thesis is a proposition to be tested. Everything estimation-shaped consolidates
  under Thesis over phases; **PolicyEngine keeps its product brand and user-facing
  identity** and is being recomposed AS Axiom (rules) + populace (data) —
  policyengine-core and the policyengine-{country} model repos retire into those
  two layers. The upgrade this buys: every estimate becomes a scoreable forecast
  with a published interval and a grade — an accountability loop CBO, TPC, and
  EUROMOD don't have. (The book may describe this end state; the *affiliation
  language* "PolicyEngine is a project of the Thesis Institute" is gated on later
  milestones — write structurally, not as an announcement.)
- **populace** — the calibrated-microdata commons: synthesis, imputation (quantile
  regression forests), calibration to administrative totals, certified release
  bundles. Successor to the Enhanced CPS line (the August 2025 Enhanced CPS is
  citable as history: five integrated datasets, 9,168 administrative calibration
  targets, deviations cut ~97%). Local-area analysis = filter one national
  calibrated dataset, not fifty bespoke ones. Public framing de-emphasizes the
  brand: name it once, plainly, as infrastructure; lean on the methods elsewhere.
- **The commons and its operators.** The book's own ch-10 principle survives
  verbatim: the infrastructure layer must be a commons — "not well served by a
  private gatekeeper." The 2026 structure implements it two-sidedly: nonprofit
  institutes steward the commons (rules, data, scoreboard); **commercial operators
  build ON the commons — as operators on it, never owners of it** (managed
  runtimes, service-level guarantees, applied products). One such operator entity
  exists in formation around graded simulation; it is not yet public.
  `[DECISION for author at publication: whether to name Cosilico PBC here]`. The
  principled line the foundation publishes: the commercial SLA tier will always be
  a separate entity, so the foundation never competes with builders on its own
  commons.
- **Nikhil Woodruff** — PolicyEngine co-founder/CTO; **joined the UK government at
  No 10 Downing Street in July 2026.** Author has approved using this with a
  disclosure at first mention. Exact role wording: `[VERIFY with Nikhil]`. Beat to
  use: the co-founder recruited from a subreddit now works inside the government
  whose analytical machinery the tools opened up.
- Author location: **Washington, DC** (relocating to New York for the Axiom
  Foundation). Preface signs off "Washington, DC, 2026."

## Rules layer (Axiom) — shipped scale, as of July 2026

- Encoding format: **RuleSpec** — YAML, `format: rulespec/v1`; logic and parameters
  as versioned, testable files with effective dates.
- **rulespec-us**: ~3,000 rule files with ~3,000 companion tests; US federal plus
  28 state codes (absorbed with full git history); signed encoding manifests.
  `[VERIFY counts at publication]`
- Country monorepos: **rulespec-uk** (including a local-authority scheme — the
  Royal Borough of Kingston upon Thames council-tax-reduction policy),
  **rulespec-ca**, **rulespec-nz**, **rulespec-be**, plus African lanes below.
- **axiom-encode** — the AI encoding pipeline: corpus lookup → prompt scaffold →
  LLM backends → merge-blocking gates (compile, CI, proof validation, oracle
  comparison, money-atom grounding) → signed apply manifests. Human review on top.
- **Money-atom gate** (describe as mechanism): a merge-blocking CI check requiring
  every monetary obligation in an encoding to be grounded in a quoted excerpt from
  the governing source; the build fails otherwise. Belgium reached zero ungrounded
  monetary obligations across 539; ratchets ensure the count only falls.
- **Corpus service**: statutes, regulations, agency manuals, and guidance ingested
  as anchored provisions with a ~41,000-entry concept registry. `[VERIFY count]`
- **Mission scope** (July 2026): encode ALL public policy — statutes, regulations,
  agency manuals, statutory guidance, grant conditions, local-authority schemes.
  "Bindingness is metadata, never a scope filter." Authority/delegation chains
  modeled explicitly (US *Accardi* doctrine; English *Lumba* doctrine: an agency
  must follow its own published policy absent good reasons).
- Licensing: Apache-2.0 (code) + CC BY (content). Deliberately permissive.
- **Honest failure to include (the B1 probe):** a July 2026 experiment tested the
  premise that encodings are disposable "cache" — regenerate any module from source
  on demand. It failed at current configuration: modules regenerated cheaply
  (~$0.08 of compute each) but 23 of 25 came back with the *old* version correct
  and the regenerated version introducing consumer-breaking naming instability.
  Conclusion adopted: encodings are durable artifacts with provenance, not cache;
  regeneration is not yet trustworthy. Use as evidence the discipline is real.

## Oracle program (verification against reference models)

- Oracles in use: **TAXSIM** (NBER), **PolicyEngine**, **UKMOD**, **EUROMOD**
  (Belgium), **SOUTHMOD** (UNU-WIDER family), and official calculators.
- **UKMOD parity** (July 2026): UK income tax test suites exact to the pound (5/5,
  including personal-allowance withdrawal); Scottish income tax 9/9 exact across
  the six-band structure; National Insurance suites exact or fully explained
  (UKMOD computes weekly then annualizes — a documented convention difference);
  savings and dividend suites exact. Universal Credit: 8/19 raw matches but 100%
  of mismatches explained with evidence (UKMOD applies a stochastic take-up draw).
  Standing result: **every compared UK surface is at 100% explained, zero
  unexplained.**
- **EUROMOD Belgium**: social-security contributions agree per-record to within
  €0.03/year across 78,479 simulated workers (aggregate difference €643 on €20.9
  billion — float rounding); regional/municipal surcharges 9/9 exact; study
  allowances 6/6 exact (a greenfield encoding); conformance board: every mismatch
  dispositioned with evidence — 100% explained, zero unexplained, zero attributed
  to Axiom-side error.
- **Bugs found in the oracles themselves, filed upstream** (the trust-flip beat):
  a UKMOD savings-allowance interaction bug filed publicly on the UKMOD-PUBLIC
  repository; a EUROMOD adapter batch-processing contamination bug root-caused
  (identical cases scored differently depending on batch position) and reported.
  Frame collaboratively: reference models are essential, and openness means errors
  flow both directions.
- **Conformance ratchets**: CI gates under which coverage may only rise and
  unexplained mismatches may only fall — a one-way valve on correctness, and the
  operational answer to "what stops the encodings quietly going stale?"
- **Dispositions discipline**: every oracle mismatch must carry an evidence-backed
  explanation (an arithmetic reconciliation, a statutory citation, or a documented
  oracle convention); "explained" is a checked artifact, not a shrug.

## The SOUTHMOD lanes (microsimulation anywhere)

- Validated against UNU-WIDER's SOUTHMOD models (the licensed bundle covers 14
  developing-country models). Findings are reported back to UNU-WIDER; each
  country's findings ledger is published as a GitHub Discussion.
- **Ghana** (GHAMOD): complete July 8, 2026 — full-surface parity for GH_2025;
  **13 findings** (encoded statute vs reference model divergences, each
  dispositioned). Ledger: rulespec-gh discussion.
- **Uganda** (UGAMOD): complete July 8, 2026, **in one day** using the proven
  recipe — **zero findings**: "statutorily exact everywhere tested," worst
  deviation 0.4 Ugandan shillings per year of rounding.
- **Zambia** (MicroZAMOD): complete July 9, 2026, ~one day — **8 findings**, the
  first country with findings on both tax and benefit sides (a PAYE base
  definition, stale excise rates carried a year forward, a turnover-tax band).
- **Ethiopia** (ETMOD): complete July 9, 2026, **in a single overnight run** —
  **2 findings**, both in the brand-new Proclamation 1395/2025 minimum alternative
  tax (a new law, understandable first-implementation divergences).
- **Rwanda** (RWAMOD): complete — **5 findings**; first lane with live
  runner-executed comparisons (86/86).
- **Tanzania**: active. **Nigeria**: begun, no oracle exists (outside SOUTHMOD) —
  an honest example of the boundary: without a reference model or admin ground
  truth, claims stay weaker.
- The per-country recipe: capture the governing acts from official gazettes (with
  page-anchored, signed source manifests) → agent-encode instrument by instrument →
  merge-blocking gates → oracle suites per-case, then population-level → publish a
  findings ledger → report upstream. Cost per country: on the order of days of
  agent time, not years of institutional effort.
- Significance to state plainly: countries that never had public, inspectable
  tax-benefit models get them; and the reference models get free, evidence-backed
  QA in return.

## Transfer / custodian evaluation ("open referee")

- Transfer experiment (July 2026, UK leg complete): adapt a US-calibrated populace
  to the UK, score against held-out native FRS-based truth via a pre-registered
  evaluation harness. Honest verdict, quote-ready: **"a credible first pass for
  aggregate, earnings-centric analysis — not a substitute for native microdata on
  benefits, distribution tails, or subnational detail."** One defect found and
  fixed (a stale feed zeroed state pensions, cascading into pension-credit
  errors); one open and dominant (capital gains transfer 1:1 into a survey surface
  that captures none — fix designed: model asset positions and realization rules,
  not transplanted realizations).
- Process honesty beat: a fabricated summary statistic was caught at a
  verification gate before publication and removed — the gates are for our own
  outputs first.
- Belgium: calibration hit all 21 of 21 targets within 1.8%; Axiom↔EUROMOD
  per-record SSC agreement within €0.03/year (same population).
- **Custodian-pack concept**: for countries whose microdata can't leave the
  building, hand the transferred dataset plus a pre-registered evaluation pack
  (pinned code, frozen config, scorecard schema) to the institution that holds
  access; they run it locally and publish only the low-dimensional scorecard.
  Thesis line, quote-ready: **"Open microsimulation anywhere doesn't require open
  microdata anywhere — it requires an open referee."** Do not name candidate
  custodian institutions.

## AI capability (the tools argument)

- TaxCalcBench (Column Tax, July 2025) — already cited in the manuscript
  [@bock2025taxcalcbench]: best model computed fewer than 1 in 3 complete federal
  returns correctly.
- **PolicyBench** (PolicyEngine, 2026, policybench.org): a public benchmark of
  LLMs on complete US household tax-and-benefit calculations over realistic
  populace-drawn scenarios; ~20 frontier and open-weight models on the board.
  Headline metric: share of household calculations within $1. As of mid-2026, the
  best model gets roughly **one in six** household calculations wrong by more than
  a dollar; most models miss a quarter or more; errors are family-level (wrong
  Medicaid eligibility, wrong SNAP amount), not rounding. Use round terms; cite
  [@policybench2026].
- **The benchmark's own integrity arc (meta-lesson, use in the AI or verification
  chapter):** early AI-generated explanation narratives on the benchmark site were
  caught fabricating derivation pathways (e.g., describing seniors as "non-elderly
  expansion" enrollees); audits that read those narratives inherited the
  fabrications. The fix was mechanical grounding: regenerate every narrative from
  the engine's actual internals and add validators that reject ungrounded
  mechanisms. Lesson stated plainly: even the audit layer needs ground truth —
  give judges traces, not prose.
- MCP timeline (already corrected in draft): Anthropic open-sourced November 2024;
  OpenAI adopted March 2025; Google followed.
- Claude/Anthropic model naming if needed: the mid-2026 frontier includes Claude
  Fable 5 (Anthropic), GPT-5.5 (OpenAI), Gemini 3.1 (Google). Prefer "the best
  2026 models" phrasing over version lists that will date.

## Opinion (HiveSight) — the measured result

- HiveSight v2 shipped July 7, 2026 (hivesight.ai) — a graded synthetic-research
  tool. The paper is live at hivesight.ai/paper; registered, pre-analysis plan
  committed before elicitation; 63-item anchor bank (52 GSS 2024 + 11 SHED 2024).
- **The arc to narrate:** persona roleplay — the intuitive approach the first
  prototype used and the literature debated — was benchmarked and **retired**:
  ~25-point mean absolute error on both toplines and subgroups. The shipped
  estimator is unglamorous: **post-stratification cells** (~150 demographic cells
  per geography, drawn from calibrated microdata) with the model eliciting a
  distribution per cell, aggregated with calibrated weights. Registered results:
  cells ≈ 9.2/9.8 points (topline/subgroup MAE); direct whole-population estimation
  ≈ 8.6/9.8 — **an honest tie on toplines** (equivalence-tested within ±1.5
  points); cells win on subgroup *structure* (rank correlation 0.62 vs 0.48),
  run-to-run stability (~9× lower variance), and question-order robustness.
  State-level check (BRFSS, 4 items × 49 states): cells beat the naive baseline
  but a national-constant guess remained competitive — reported honestly.
  Contamination control: the elicitation model's training cutoff predates all 2024
  targets.
- Cite [@hivesight2026benchmarkpap] (check exact key in references.bib). Framing:
  "cells, not personas" — the microdata-grounding idea survived; the persona
  mechanism did not. The measurement discipline is the point.

## Values (chapter 16 corrections — mandatory)

- **GSS same-sex-relations item (HOMOSEX, "not wrong at all"):** 2018 ≈ 57%,
  2021 ≈ 62%, **2022 ≈ 61%, 2024 ≈ 55%** — the reversal is ~6 points off the
  2022 reading, NOT 17. (The 72% figure in the old draft is Gallup's
  moral-acceptability series — a different survey; do not conflate. Cite GSS
  [@gss2024].)
- **The backtest claim:** state baselines explicitly. GPT-4o quantile-prompted
  forecasts of 17 GSS variables for 2024: mean absolute error ≈ 4.8 points vs
  ≈ 7.2 for linear extrapolation (≈1.5× better) and ≈ 10.6 for a no-change
  baseline (≈2.2×). Never quote "2.2×" without naming the baseline. The headline
  event remains the miss: every method, human and model, missed the same-sex-
  acceptance reversal.
- Same-sex-marriage support trajectory: use anchored series only — Gallup begins
  1996 at 27%, reaching ~70% by the early 2020s [@gallup2024marriage — if absent
  from references.bib, mark NEEDS CITATION]. Do not use "32% in 1986" (no clean
  source).
- The long-horizon (2050/2100) projections: keep only as clearly-labeled
  illustration of the *method's* output, never as findings; reconcile numbers to
  the EA-draft versions or drop the table.

## US policy currency (OBBBA)

- **OBBBA enacted July 4, 2025** (H.R. 1, 119th Congress). TCJA individual
  provisions extended (not expired); **CTC $2,200 per child from 2026**;
  pass-through deduction permanent. Cite [@obbba2025].
- SNAP administration (for the encoding chapter's administrative-quality section):
  from FY2028 states pay a share of benefit costs **tiered by their payment error
  rate** (0/5/10/15% for error rates <6/6–8/8–10/≥10%); the FY2025 national
  payment error rate was 10.6%; roughly $9B/year of first-year state exposure per
  CBPP `[NEEDS CITATION: CBPP analysis]`. State administrative cost share rises
  50%→75% in FY2027. Medicaid: work-requirement verification systems due
  December 31, 2026 under a CMS interim final rule; six-month redeterminations.
  Frame: policy now *prices administrative accuracy* — a state's error rate is a
  fiscal line item, which is precisely what verified rules infrastructure
  addresses.
- USDA/FNS bright line: AI may not replace state merit personnel in SNAP
  eligibility determinations `[NEEDS CITATION: FNS guidance]` — supports the
  book's "decision support, not decision replacement" stance.
- Liability precedents (admin-quality section): Australia's Robodebt (automated
  debt claims unwound in court, ministers before a royal commission), Michigan's
  MiDAS false-fraud determinations, Arkansas's algorithmic care-hour cuts
  (*Ledgerwood/Elder*-era litigation) `[NEEDS CITATION each; do not state dollar
  figures without one]`. Deloitte-built eligibility systems span ~25 states with
  ~$6B in contracts `[NEEDS CITATION]`.

## Numbers being recomputed (placeholders)

- CTC full-refundability score: the old draft's contradictory $2B (ch 8) / $12B
  (ch 11) figures are being re-scored against current law (2026, OBBBA baseline,
  reform = remove the refundable cap and the earnings phase-in). Write the
  placeholder token `[[CTC-RESCORE]]` wherever the number belongs; the assembler
  will replace it with the computed value and its poverty effect, or date-and-label
  the old figure if the run doesn't land.

## Bib keys added for this rewrite (safe to cite)

`@obbba2025`, `@policybench2026`, `@unuwider2026southmod`,
`@rulespecgh2026findings`, `@thesisinstitute2026`, `@ukmod2026bugfiling` — plus
everything already in references.bib (read it before citing; hivesight and GSS keys
exist). Anything else: `[NEEDS CITATION: …]`.

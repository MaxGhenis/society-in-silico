# Chapter-level findings — four parallel review passes (2026-07-10)

Full line-level reports from the four reviewers (front matter + Part I; Part II
ch 5–8; ch 9–11; Part III ch 12–15), each briefed on the July 2026 ground truth
(Brier→Thesis, Cosilico→Axiom retirement, the two-institute end state, shipped
rulespec/oracle/SOUTHMOD infrastructure, HiveSight v2, PolicyBench, OBBBA, Nikhil at
No 10, witness-verification discipline). `synthesis.md` is the executive summary;
this file is the appendix with exact line numbers.

One correction to apply on top of the ch 12 report below: the reviewer knew HiveSight
v2 shipped but not the mechanism change. The v2 rebuild **retired persona roleplay**
after a powered SHED-2024 benchmark measured it at 36.6pt topline MAE; the shipped
estimator is post-stratification cells (~150/geography) + verbalized distribution
elicitation + calibrated-weight aggregation (6.2pt subgroup MAE, best in test; direct
estimation still wins toplines at 9.3 — reported honestly in the registered paper,
"What does post-stratifying language-model predictions buy?"). So ch 12's rewrite is
deeper than prototype→shipped: its "microdata-grounded personas" mechanism
(lines 67–73) is empirically superseded — the microdata-grounding *idea* survives,
the persona *mechanism* does not. The chapter's strongest from-scratch version
narrates that benchmark arc as a microcosm of the book's method.

---

# Report 1 — Front matter + Part I (ch 1–4)

## Two structural facts that frame everything below

1. **`00-thesis.md` is not in the shipped book.** `_quarto.yml` lists the chapter
   order as `index.md → 00-preface.md → 01-introduction.md → Part I…`. The thesis
   file is a planning artifact, not a built chapter. That matters: the document doing
   the most to define the book's spine is invisible to readers, and the actual
   first-contact framing lives in `01-introduction.md`.
2. **The build still names the dead brand in a filename.** Part II ch. 10 is
   `manuscript/part-2-building/10-cosilico-infrastructure-for-the-future.md`.
   "Cosilico" is fully retired (→ Axiom Foundation). The preface (line 19) points at
   it as "infrastructure that doesn't yet exist" — see below.

## 1. `00-thesis.md`

### Summary
Frames the book around a single question — "Can simulation help society realize its
goals?" — and deliberately narrows it away from grandiose readings. Lays out the
three-part arc, states a five-point claim (simulation aids reasoning; open simulation
shifts power to citizens; uncertainty quantification enforces honesty; AI will use
these tools; "what do we want?" may itself be simulable), argues the alternative to
open simulation is black-box/vibes-based governance, and closes with an honesty
caveat.

### Strengths
- The negative definition up front (lines 6–8) inoculates against the strongest
  objection before it's raised.
- "Society in silico is not a destination. It's a method" (line 36) is the single
  best line in the front matter and should survive any rewrite.
- The "alternative to simulation isn't 'human judgment uncorrupted by models'"
  framing (lines 49–54) is exactly the counterintuitive, comparative move the style
  guide prizes.
- The honest caveat section (lines 57–63) models the intellectual discipline the
  whole book claims.

### Weaknesses
- Almost entirely conceptual — no numbers, no concrete example, no reproducible
  claim; reads like a manifesto's preamble, which sits awkwardly with the preface's
  explicit "this is not a manifesto."
- The five-point claim (lines 39–43) mixes tiers of confidence without marking them:
  points 1–2 are well-evidenced; point 5 is frankly speculative.
- The thesis question is softer than the work now supports — nearly unfalsifiable,
  while the real project has a sharp, testable spine (per-unit verifiability against
  ground truth) that this document doesn't name.

### Stale / wrong
- **Line 29:** "PolicyEngine, the Axiom Foundation, the Brier Institute, and related
  projects are proof…" — **"Brier Institute" is a dead name** (→ Thesis Institute).
  The framing also predates the two-pole end state: the proof is now Axiom
  (determinism) + Thesis (prediction), with PolicyEngine recomposed *into* Axiom
  (rules) + populace (microdata), not standing alongside them as a peer.
- **Line 59:** "The Brier Institute's forecasting work remains early." — dead name.
- **Line 59:** "The value forecasting thesis has preliminary tests, not independent
  validation." — "preliminary tests" is slightly too generous given the
  zero-witness-verified state; safer: "no resolved, independently verified forecasts
  yet."
- **Line 28:** "The vision preceded the capability by decades" — not wrong, but the
  Part II claim of "possible, not complete" is overtaken: the aspirational
  infrastructure now materially exists.

### From-scratch verdict
**Rewrite, and promote it into the actual build** (or fold into the introduction). A
thesis document readers never see is a wasted asset. The strongest version replaces
the soft question with the project's real, falsifiable spine:

> Rebuild the analytic stack of government in the open, on one discipline: **every
> unit's output must be checkable against ground truth.** Two poles do the work —
> **encode the world's policy corpus exactly** (Axiom: agents → determinism,
> verified against statute and against oracles like TAXSIM, UKMOD, EUROMOD) and
> **forecast what government produces** (Thesis: agents → prediction, verified
> against resolved outcomes) — joined by calibrated microdata (populace). "Society
> in silico" is not a claim to have modeled society; it is a method whose honesty is
> enforced by per-unit verification.

New material that belongs here: the "agents can [VERB] the world's [CORPUS]"
pattern; the determinism/prediction poles; per-unit verifiability as the gating
test; and an honest split of the caveat — Axiom's determinism claims are now backed
by real oracle results, while Thesis's prediction claims are explicitly not yet
validated.

## 2. `00-preface.md`

### Summary
First-person entry: the 2019 UBI question, models locked inside agencies, UBI Center
→ PolicyEngine with Nikhil Woodruff. States what the book is / is not, names three
audiences, gives a reading path. Signs off "San Francisco, 2026."

### Strengths
- The opening (lines 3–5) is the style guide's ideal hook: specific personal
  frustration grounded in named institutions with a concrete question.
- The escalating question chain (line 9) is an elegant, honest map of the book's
  expanding scope.
- "What this book is not" (lines 21–29) earns trust — especially "One chapter
  describes infrastructure that doesn't yet exist. I label the differences clearly."
- Admitting "I've imperfectly served all three [audiences]" (line 33) is exactly the
  non-salesy honesty the style guide asks for.

### Weaknesses
- The tri-audience hedge risks reading as an apology; consider committing to a
  primary reader.
- "Some of what I describe will look different in two years" (line 29) is now
  unintentionally ironic — large parts look different in six weeks.
- "HiveSight, Democrasim" (line 19) dropped without any anchor for a reader 200
  pages from meeting them.

### Stale / wrong
- **Line 60:** "San Francisco, 2026" — **wrong location** (Washington, DC; moving to
  NYC). The most visible factual error in the front matter.
- **Line 19:** "…the Axiom Foundation, and the Brier Institute" — dead name.
- **Line 19:** "One chapter describes infrastructure that doesn't yet exist" — **now
  false.** rulespec-us (~3,000 rule YAMLs + tests, federal + 28 states),
  rulespec-{uk,ca,nz,be}, the encoding pipeline with compile/CI/proof/oracle gates
  and signed manifests, oracle validation against TAXSIM/PolicyEngine/UKMOD/EUROMOD/
  SOUTHMOD. The label must flip from aspiration to accomplishment.
- **Line 29:** "The Axiom Foundation is encoding new statutes. The Brier Institute's
  forecasting work is still early." — dead name, and "encoding new statutes" badly
  understates scope (thousands of rules, multiple countries, SOUTHMOD-validated
  lanes; mission widened to "encode all public policy" with bindingness as
  metadata).
- **Lines 7, 19 (disclosure gap):** Nikhil Woodruff joined the UK government (No 10)
  July 2026. This book is UK-policy-adjacent external writing (UKMOD, IFS,
  PolicyEngine-UK), so his role **must be disclosed** — a footnote at first mention;
  also a genuine narrative beat worth using rather than burying.

### From-scratch verdict
**Keep the structure; targeted light rewrite.** Fix the location sign-off; replace
both Brier instances; invert the "infrastructure that doesn't exist" promise into
"infrastructure I described as aspirational and have since largely built — with the
validation results to show for it"; add the Nikhil/No 10 disclosure. New material: a
single sentence stating the two-pole end state, and one concrete, reproducible
number in the opening instead of the purely qualitative version.

## 3. `01-birth-of-microsimulation.md` (Orcutt)

### Summary
Orcutt's 1957 paper through the 1961 proof-of-concept book, Treasury's early tax
models, and DYNASIM (1975): model individuals and derive aggregates, rather than
impose relationships on aggregates. Develops the aggregation-error argument (Y=X²),
situates Orcutt against Asimov's psychohistory, follows the family of models, closes
on the computational revolution and Orcutt's three-generation legacy.

### Strengths
- **The Y=X² worked example (lines 47–51)** makes "aggregation is a mathematical
  error, not just a limitation" concrete in four sentences.
- **The Asimov inversion (lines 75–77)** — psychohistory elegant but autocratic,
  Orcutt granular and potentially democratic — does real thematic work for the whole
  book.
- **The Rivlin hinge (line 99)** — Orcutt's doctoral student → first CBO director —
  is superb connective tissue that pays off in Chapter 2.
- The 18-year vision-to-implementation gap (lines 129–131) used well.
- The closing three-generations coda (line 253) lands "a way of thinking, not a
  model" without overreaching.

### Weaknesses
- ~4,000 words with three endings ("The Legacy," "Looking Ahead," the
  rhetorical-question cascade at 275–283). Cut "The Unfinished Revolution"
  (233–246) hard — Chapter 4 does that argument better.
- The 10,000-unit figure appears at lines 97, 127, and 217.
- The table (181–187) is textbook-y; the "N/A (wrong tool)" cell is glib.

### Stale / wrong
- **Line 166 — factual error.** "**CANSIM** (Canada): Adapted DYNASIM's framework…"
  No such microsimulation model; CANSIM was Statistics Canada's data-retrieval
  database. Canada's actual models are DYNACAN (already listed) and **SPSD/M**.
  Replace or delete.
- **Line 75 — uncited quote (verified accurate).** The *Foundation and Empire* quote
  needs a bib key.
- **Line 87 — uncited specific.** IBM 704 "roughly 12,000 floating-point operations
  per second" — cite or soften.
- **Lines 121 vs 125 — internal inconsistency.** "1969 resources" vs "hired him in
  1968" — reconcilable but reads as contradiction.
- **Line 265 — dating tell.** "sixty-seven years later" = 2024; the book is dated
  2026 → sixty-nine.
- Line 251 verified correct (Orcutt died March 5, 2006). Line 123 defensible (SSRI
  from 1959).
- Note: this chapter is where a rewrite should plant the Axiom/RuleSpec seed —
  Orcutt's "interacting units which receive inputs and generate outputs" (line 65)
  is literally the per-unit encoding model; the ending currently points only at the
  2015-era payoff (open source + web), not the 2026 one (per-unit verifiability).

### From-scratch verdict
**Keep, with a tightening pass.** Cut one of three endings, de-duplicate "10,000,"
fix CANSIM, the dating, and the 1968/1969 wobble; add the Asimov bib entry; end on
what got built.

## 4. `02-tax-model-wars.md`

### Summary
The "tax model wars" were about power — who defines what a policy costs. IFS/TAXBEN
(1983) as first independent challenge; the closed US apparatus (CBO/JCT/Treasury/
TRIM3); the §6103 data asymmetry; the challengers (TAXSIM, TPC, Penn Wharton, Budget
Lab); the dynamic-scoring wars; the UK/EU alternative (NATSEM/Harding, EUROMOD/
Sutherland, UKMOD); the open-source emergence.

### Strengths
- **The §6103 "analytical moat" (lines 39–40)** is the most important and underused
  idea in Part I — the permanent asymmetry, and the argument for calibrated
  synthetic microdata. Currently under-leveraged.
- The JCT scoring mechanics (line 25) make an abstract institution viscerally
  consequential.
- The four-part asymmetry taxonomy (lines 43–49) is clean and quotable.
- The dynamic-scoring section (lines 77–93) delivers the falsification honestly
  ("the tax cuts did not pay for themselves. The microsimulation models had been
  approximately right").
- The ideological-irony beats (AEI building open tools; France open-sourcing) argue
  "cut across ideological lines" well.

### Weaknesses
- **Heavy TCJA-number duplication with Chapter 4** (lines 67, 89, 91 here; 3, 92,
  162 there). One chapter should own the TCJA retrospective.
- Two uncited quotes (Brewer line 115; Reed line 117).
- The thesis is stated three times (7–9, 157–165, coda).
- Karen Smith re-introduced (line 29 here; ch 1 line 161).

### Stale / wrong
- **Line 113 — attribution/timing, handle with care.** Brewer led the Nuffield grant
  (verified), but UKMOD is housed at CeMPA (ISER, Essex) directed by Matteo
  Richiardi; the introducing paper is Richiardi, Collado & Popova (2021). "In
  2018… spun off… UKMOD" also compresses the timeline (launch ~2019–2021). Name
  CeMPA and both figures factually — diplomacy matters here.
- **Line 115, 117 — uncited quotes.**
- **Line 149 (currency):** PolicyEngine as "newest tier" — fine for history, but add
  a one-clause forward signal of the recomposition to prevent Part II whiplash.
- **Disclosure gap:** most UK-government-adjacent chapter in Part I; the Nikhil
  disclosure should be visible near this material.
- **OBBBA (soft):** TCJA discussed as a closed episode; add a footnote that OBBBA
  extended it.

### From-scratch verdict
**Keep, trim ~20%, de-duplicate.** Own the *institutional* TCJA story; hand the
*accuracy-tracking* numbers to ch 4. Foreground §6103 as the permanent constraint
whose answer is *synthesize and calibrate* — the natural on-ramp to
populace/microplex the draft never builds. Consider merging this chapter's tail with
ch 3's rules-as-code opening.

## 5. `03-open-source-revolution.md`

### Summary
Two chapters in one file. First half (lines 1–77): the 2011 French twin launch
(revolution-fiscale.fr, OpenFisca), Tax-Calculator/OSPC, rules as code, the
promise-and-gap analysis, two architectures (OpenFisca unified vs PSL federation).
Second half (79–217): the personal origin — Berkeley, Google People Analytics and
Project Lorenz, brother Alex's benefit cliff, GiveDirectly/UBI, UBI Center (2019),
recruiting Golden and Woodruff, founding PolicyEngine (2021).

### Strengths
- **The Alex passage (lines 107–117) is the emotional and intellectual core of the
  entire book** — a >100% marginal rate made personal; the best writing in Part I.
- "UBI as benchmark, not proposal" (127, 155) separates the author from advocacy.
- The two-architectures section (63–73) is crisp; Senegal-in-36-hours and
  LexImpact-122-simulations are exactly the concrete specifics the style guide
  wants.
- Honesty about Project Lorenz failing (103) buys credibility.
- The "what was missing" close (183–199) cleanly enumerates the gap Part II fills.

### Weaknesses
- **The file is doing two jobs and the seam shows (79–81).** History and memoir
  collide mid-chapter with no transition — the clearest structural problem in
  Part I.
- Uncited own-analysis numbers: the Yang figures and carbon-dividend figures
  (line 175) warrant links to the reproducible UBI Center reports.
- The Alex cliff numbers (113) presented as literal personal fact could use a
  footnote grounding the marginal-rate figure.
- Line 5's "More than 500,000 people visited the site" is uncited.

### Stale / wrong
- **Line 9 — anachronism.** "France Stratégie… released… OpenFisca" in 2011; the
  body was the Centre d'analyse stratégique until 2013. Use the 2011 name or
  "(later France Stratégie)."
- **Line 161 — disclosure gap (major).** Nikhil enters the story here; this is the
  most natural place for the required No 10 disclosure — and the most powerful place
  to *use* it ("the co-founder I recruited off Reddit now helps run the UK
  government's own analytical machinery").
- **Line 211 (framing currency):** "born… to complete what the open-source
  revolution had started" needs a forward flag of the recomposition.

### From-scratch verdict
**Split.** Move the rules-as-code history (1–77) adjacent to Chapter 2; promote the
personal origin (79–217) into its own short chapter as the bridge into Part II. Fix
France Stratégie; add the Nikhil disclosure; cite the UBI Center analyses. Lean
harder into Alex's cliff as the book's origin image: the reason to encode rules
exactly and check them per-unit is that a single household's >100% marginal rate is
invisible in any aggregate.

## 6. `04-the-accuracy-question.md`

### Summary
Do these models actually work? Three validation levels (component / aggregate /
predictive); the ACA natural experiment (aggregate right, components offsetting);
CBO improvement but random-walk-sometimes-beats-CBO; prediction markets; the
survey-data crisis (Meyer; Bee–Mitchell seniors); TAXSIM as benchmark; why models
disagree; where models fail; "approximately right, sometimes wrong, better than
alternatives, always improvable."

### Strengths
- **The best and most durable chapter in Part I** — arguably the intellectual heart
  of the book's *new* thesis; every section is doing verifiability work.
- The ACA component-vs-aggregate table (49–55) and its synthesis (59) are a model of
  honest quantitative storytelling.
- **The random-walk finding (84–88)** is the counterintuitive, self-implicating fact
  the style guide prizes — and the seed of the entire Thesis/prediction pole.
- The survey-data-crisis section (124–144) is rigorous and correctly sourced — the
  argument for calibrated microdata.
- "When models disagree… the question isn't 'who's right?' It's 'what assumptions
  differ?'" (174–176). Superb.
- The George Box close (238–244) is the book's ethical thesis in miniature.

### Weaknesses
- TCJA duplication with ch 2 (lines 3, 92, 162).
- Good Judgment "beat futures markets by 30%" (110) rides a light citation; CPS
  "$1.1 million top-code" (140) is uncited and methodologically loose
  (rank-proximity swapping, not a clean threshold).
- The prediction-market section (98–121) name-checks Polymarket/superforecasters
  without connecting to the project — a missed setup.
- Line 108's `crane2020prediction` covering the 2020 election is a
  citation-plausibility wrinkle.

### Stale / wrong
- **OBBBA currency (90–95, 184).** TCJA treated as a completed 2018–2024 episode;
  OBBBA extended it (pass-through deduction permanent; CTC $2,200 in 2026). Add the
  footnote or the "seven years of data" framing reads as if the story ended in 2024.
- **Lines 98–121 (framing):** any forward reference to Thesis must obey the
  discipline — 0 witness-verified resolved forecasts; present forecasting as a
  direction, never as validated.
- **Line 254:** "Next: Part II begins with PolicyEngine…" — partly overtaken; Part
  II's subject is really the recomposition.

### From-scratch verdict
**Keep and elevate — this chapter should anchor the new thesis.** Extend with what
now exists: oracle validation as the concrete answer to "do they work?" (TAXSIM
agreement, UK income tax exact to the pound, EUROMOD Belgium 100% explained / 0
unexplained, SOUTHMOD lanes) plus PolicyBench as the quantitative case for a
deterministic, per-unit-verifiable backend. Frame the whole chapter around the
gating test. De-duplicate TCJA with ch 2; keep the Box ending.

## Part-level assessment (Part I + front matter)

**Part I earns its place as a leaner three-beat runway plus a personal bridge, not
four roughly-equal chapters.** Its job: (1) you must model individuals to see
distributions (Orcutt), and (2) the honest test of any such model is whether you can
check it against reality (accuracy/verifiability). Concretely: Orcutt (tightened) →
merged institutional/open-source chapter spined on §6103 → accuracy/verifiability
elevated to the book's hinge → personal-origin bridge into Part II. Net shrink
~15–20%, almost entirely from de-duplicating TCJA and merging the ch 2 / ch 3-history
overlap.

Cross-cutting fixes: (1) every Part I chapter ends gesturing at a gap "someone would
need to" close — in 2026 much of that gap *is* closed; re-point the endings from
"here's what remains open" to "here's the gap we then closed, and how you can check
it." (2) Disclosure + brand hygiene: Nikhil/No 10 at first mention; purge
Brier→Thesis and Cosilico→Axiom including the ch 10 filename; fix "San Francisco";
confirm or strike "Axiom Labs" in `.claude/CLAUDE.md` line 5.

**The front-matter thesis has been overtaken in two directions at once: it names a
dead institution, and it undersells a now-testable claim.** Replace the soft "Can
simulation help society realize its goals?" with the falsifiable spine (rebuild the
analytic stack of government in the open, under per-unit ground-truth verification;
determinism pole backed by real oracle results today, prediction pole explicitly not
yet validated) — and put it *inside the build*, folded into the introduction rather
than stranded in a file readers never reach.

---

# Report 2 — Part II (ch 5–8)

## Cross-cutting (stated once)

- **The data story is the deprecated one.** All four chapters make the Enhanced CPS
  the terminal data achievement; ground truth is populace (calibrated microdata) +
  microplex (synthetic eCPS replacement). Ch 6 has partially caught up (cites
  microimpute/microplex/microcalibrate); ch 8 has not. Note the countervailing
  instruction: populace is deliberately de-emphasized publicly — update the
  *methods* without heavily branding populace.
- **The recomposition is absent.** All four treat PolicyEngine as the enduring
  end-state entity whose only open problem is sustainability. The actual end state:
  Axiom = determinism pole, Thesis = prediction pole, PE recomposed as Axiom (rules)
  + populace (data). The strongest new material — agentic encoding and oracle
  verification — is exactly what Part II is missing.
- Two standing sensitivities: a **close-hold Federal Reserve partnership named in
  the clear** (ch 5), and the **Nikhil/No 10 disclosure** missing everywhere.

## Chapter 5 — PolicyEngine: proof of concept

### Summary
Chronological origin story: the 2019–2021 open-source ferment (UKMOD, TAXSIM35,
EUROMOD open-sourcing), UBI Center frustration, UK launch (Sep 2021), US crossing
(Mar 2022), users, the validation challenge, tool→infrastructure arc (NSF POSE,
Enhanced CPS, NBER/TAXSIM and Atlanta Fed MOUs, HM Treasury pilot, MyFriendBen),
closing on an honest "what we hadn't solved" ledger pointing to ch 10.

### Strengths
- The UBI Center → PolicyEngine origin (15–25) is the style guide's "origin story"
  move executed at its best.
- **"The API was the product; the web app was one consumer of that API" (39)** is
  the chapter's strongest single idea and survives the recomposition intact.
- The US-vs-UK complexity contrast (63) — "multiplicatively rather than additively"
  — is a clean, earned generalization.
- The legislative-staff vignette (89) — arriving at CBO "with proposals already
  refined" — shows how the tool changed behavior.
- Validation honesty (107–109): the ~one-third revenue gap as structural constraint.
- MyFriendBen hedging (145): "a self-reported figure, not an independent audit."

### Weaknesses
- **The ending predates the plot.** "What We Built, What Remained" (151–165) frames
  sustainability as the unsolved problem and defers to ch 10; the resolution now
  exists offstage (the Axiom/Thesis split with institutional anchor funding).
- Duplication with chs 7–8: MyFriendBen (145 ≈ ch 7:153–155); the Truss/mini-budget
  "within hours" beat appears here (85), ch 7 (129), and twice in ch 8 (173, 203).
- "Who Used It" (79–91) is four parallel paragraphs that read like a capabilities
  deck.
- Uncited specifics cluster in the opening timeline.

### Stale / wrong / dubious
- **Line 107:** "required better data, which arrived later with the Enhanced CPS
  (Chapter 8)" — deprecated data story; reframe toward populace/microplex.
- **Line 121:** Enhanced CPS launch "August 2025… 9,168 administrative totals… 97
  percent [@policyengine2022enhanced]… microimpute and microcalibrate." True as
  history; needs a forward pointer to the rebuild. Note the citation key year
  mismatch (2022 key, 2025 launch) — recurs in chs 6 and 8; reconcile in
  references.bib.
- **Lines 129–131 — SENSITIVITY, close-hold partner named in the clear.** "we
  signed a second MOU with the **Federal Reserve Bank of Atlanta**. Their **Policy
  Rules Database**… powered the Atlanta Fed's **CLIFF tools**, which **Colorado's
  Workforce Development Council and New Mexico's Caregivers Coalition** used…" plus
  line 131's three-way-validation naming. Internal guidance: do not name in partner
  materials. Explicit keep/cut decision + partner sign-off required before
  publication.
- **Lines 21, 55, 137–141 — Nikhil/No 10 disclosure missing**, including for the HM
  Treasury pilot passage (137–141) about the government evaluating the tool his
  company built.
- **Line 137 — verify wording.** "The Times reported that the tool could more
  accurately predict the outcomes of ministers' decisions" — match to the exact ATRS
  record and Times wording; confirm line 103's "60 percent of National Insurance
  calculations fell within 0.5 percent" against the published record (flagged for
  source-check; could not independently confirm).
- **Line 7:** "In September 2019, UKMOD became the UK's first freely available
  tax-benefit microsimulation model" — verified date is **October/Autumn 2019**.
- **Line 9:** TAXSIM35 2020; Tax-Calculator v3.2.1 August 2021 — uncited
  versions/dates; verify or cite.
- **Line 11:** EUROMOD open source December 2020, JRC from 2021 — **verified
  correct**; add citation.
- **Line 117:** NSF POSE grant 2024 — real program; add citation.
- **Line 119:** "Over 100 open-source contributors"; line 67: "six states…
  Forty-four remained"; line 125: "Over 1,200 papers had relied on TAXSIM"; line
  161: "five staff" — uncited.
- **Line 101:** "a phase-out rate coded as 21.06% instead of 21.6%" — uncited
  anecdote, and the true EITC two-child phase-out *is* 21.06%, making the example
  confusing as written.

### From-scratch verdict
**Keep, trim, re-point the ending.** (a) Cut "Who Used It" to its two best
vignettes; (b) de-duplicate MyFriendBen and the mini-budget (ch 5 owns the origin);
(c) add the Nikhil disclosure and resolve the Atlanta Fed naming; (d) replace the
sustainability-cliffhanger ending with the real hinge: the tool's success revealed
that **rules, data, and prediction are separable concerns** — the setup for the
recomposition.

## Chapter 6 — The three ingredients of microsimulation

### Summary
Every microsimulation must solve rules encoding, microdata construction, and
behavioral dynamics. Rules: EUROMOD XML/GUI vs code-native Python, TAXSIM as opaque
third pole, rules-as-code. Data: surveys, matching, imputation (QRF), calibration,
projection. Dynamics: static vs dynamic, elasticities (ETI ≈ 0.30), structural
models. Closes on integration.

### Strengths
- **The three-ingredient framework is the book's best organizing idea**, and line
  3's honesty ("doesn't appear explicitly in the literature… but captures what any
  team must solve") is disarming and correct.
- The EUROMOD-vs-code-native comparison (24–82) is illuminating and fair ("This
  isn't about better or worse—it's about different communities," 78).
- The NI code + YAML example (37–66) is the right "show, don't tell"; "logic in
  Python, values in YAML" (66) is crisp.
- The ETI treatment (186–192) is a model of acknowledged uncertainty.
- The integration section (244–254) earns "years, not months."

### Weaknesses
- **The rules ingredient under-delivers the most important story** — the
  rules-as-code section (84–88) gives Axiom two sentences and defers to ch 10, while
  the agentic pipeline + oracle verification are the freshest, most differentiated
  material the author has.
- Cross-chapter data inconsistency: line 96/102 "about 100,000 households" vs ch 8
  line 19 "about 60,000 households each month" — both cite `census2024cps`
  (ASEC vs monthly basic; the book never distinguishes them).
- Partial data update creates internal drift with ch 8.

### Stale / wrong / dubious
- **Line 86:** correct entity (Axiom), thin specifics — format is RuleSpec (YAML);
  differentiator is the agentic pipeline + oracle gates + signed manifests.
- **Lines 124, 236:** Enhanced CPS framing — deprecated; update toward
  populace/microplex methods.
- **Line 138:** "Microplex extends the idea toward multi-source synthesis…"
  understates: it is the synthetic-microdata Enhanced-CPS *replacement*.
- **Lines 148–150:** 9,168 targets, 8.3%→0.2% — internally consistent; keep only if
  they still describe the shipped pipeline.
- **Line 21:** "over 2,700 parameters" — uncited; note unit mismatch vs "~3,000 rule
  YAMLs" (parameters ≠ rules); pick a consistent sourced figure.
- **Line 31:** "EUROMOD's UK component contains over 67 megabytes of XML" — oddly
  specific, uncited, does rhetorical work against EUROMOD; source it or cut it.
- **Line 108:** CPS top-code "around $1.1 million" — uncited; verify or soften.
- **Line 17:** "thirty-one states have their own EITC variants" — plausible,
  uncited.
- **Line 188:** Neisser 1,720 estimates / 61 studies / ~0.30 — cited and consistent.
  Keep.

### From-scratch verdict
**Keep the frame; rebuild Ingredient One, update Two, re-point Three.** Extend "two
architectures" to **three** — spreadsheet/XML (EUROMOD), hand-written code-native
(Tax-Calculator, classic PolicyEngine), agent-encoded + oracle-verified (RuleSpec) —
with the gating test stated explicitly. Ingredient Two updates to synthetic
microdata/calibration-as-infrastructure (populace low-key). Ingredient Three
introduces the determinism/prediction split rather than treating dynamics as a
feature module.

## Chapter 7 — The household view

### Summary
The tax-benefit system as invisible labyrinth; PolicyEngine's household calculator
as the first tool showing taxes and benefits together. Cliffs and marginal rates
(low-income workers facing rates above a billionaire's), the what-if machine, six
worked cases, the UK household view, trust-but-verify, calculator→infrastructure
(MyFriendBen, Crossroads, Gary/FFGI).

### Strengths
- The opening (3–11) is the book's cleanest hook (the New York single parent; "No
  one can calculate this in their head").
- **The cliff/marginal-rate reveal (59–71) is the book's signature counterintuitive
  finding**, grounded in correct statutory mechanics. Fully timeless.
- Six real cases (103–115), varied and specific.
- **"The household view… was a primitive" (163)** maps directly onto per-unit
  verifiability.
- Connecticut-vs-Mississippi (175) is a sharp statement of micro over macro.

### Weaknesses
- Least stale, least updated: never connects the household calculation to
  verification — yet it *is* the atomic unit at which encoding is checked against an
  oracle or a real determination. One sentence away from the new spine.
- MyFriendBen duplication with ch 5.
- **The unattributed block quote (53)** — a definition of "the cliff" with no source
  — violates the book's own citation rule.
- The UK section (131) again lacks the Nikhil disclosure.

### Stale / wrong / dubious
- **Line 93 + the CTC through-line:** the 2021 ARP expansion story is accurate as
  history, but the book uses the pre-OBBBA $2,000 CTC as its reference point and
  never notes OBBBA's $2,200 (2026). Add the current-law anchor.
- **Line 131:** HM Treasury → Nikhil disclosure applies.
- **Line 159:** Crossroads [@policyengine2026crossroads] — confirm still live/named
  at publication.
- **Line 53:** unattributed block quote — cite or convert to prose.
- **Line 127:** "£1,000 per year" UC taper example — specific, uncited (the 2021
  63→55% taper cut); source or soften.
- **Line 107:** WA WFTC "12–24%" — cited; keep.

### From-scratch verdict
**Keep; lightly recast as the verification substrate.** Add one bridge: the
household calculation is the unit of ground-truth verification. Let this chapter own
MyFriendBen; add the OBBBA anchor; strengthen the "primitive" framing.

## Chapter 8 — The society view

### Summary
From one household to the nation: weighting, the Pechman–Okner lineage, the
enhancement pipeline, budget scoring, poverty (SPM), distributional/inequality
analysis, neutrality, validation (the ~33% revenue gap), real-time analysis
(mini-budget, CTC debates, State Legislative Tracker), two case studies (ARP CTC; UK
mini-budget vs UC taper).

### Strengths
- The Pechman–Okner framing (15) gives the society view real lineage.
- **The "where reliable / where caution" split (149–157)** is the most useful
  passage in the chapter and among the most honest in the book.
- The neutrality section (117–135) — "It tells you what the outcomes are" — will
  age well.
- The paired case studies are well chosen; "40% more effectively per pound" is the
  chapter's sharpest analytic moment.

### Weaknesses
- **Most stale data chapter**: the Data Foundation (27–39) and "100,000 weighted
  records" (51) are pure Enhanced CPS with no populace/microplex; conflicts with
  ch 6's partial update.
- Two OBBBA-obsolete framings (below).
- Case-study duplication: mini-budget in the "Speed in practice" box (173) *and* as
  a full case study (199–203); UC taper in ch 7 (127) and here (205).
- A key comparative statistic uncited (205).

### Stale / wrong / dubious
- **Lines 3, 49, 85 — pre-OBBBA baseline.** "Making the CTC fully refundable would
  cost $2 billion per year… poverty would fall 0.3pp" — scored against a $2,000-CTC
  baseline; with OBBBA's $2,200 CTC the cost and incidence differ. Re-score against
  current law or date the baseline explicitly. (Note also the May 30 review's
  unresolved $2B-vs-$12B contradiction with ch 11.)
- **Line 56 — TCJA-expiration framing overtaken.** Written as a live pending
  question; OBBBA resolved it — and OBBBA itself is a cleaner illustration of the
  baseline point than the hypothetical.
- **Lines 35–39, 51 — Enhanced-CPS methodology as current** — update to
  populace/microplex, align with ch 6.
- **Line 147:** the ~33% revenue gap is a property of the deprecated data; re-verify
  against the shipped stack.
- **Line 177:** State Legislative Tracker "routes high-value bills into an encoding
  pipeline" — the seed of the agentic-encoding story told under the PE brand;
  reframe as the on-ramp, don't cut.
- **Line 189 — wrong as written.** "The expanded CTC alone lifted 2.9 million
  children out of poverty [@census2022childpoverty]." Census (verified): the CTC
  lifted 5.3M people *including* 2.9M children; the **expansion alone lifted 2.1M
  children**. Fix to one or the other. (Companion facts — SPM child poverty 5.2% in
  2021, record low — verified correct.)
- **Line 69 — unexplained gap from official SPM.** PolicyEngine 9.6% vs Census
  official SPM ~12.4% (2022) / ~12.9% (2023), undated and unexplained — date it
  and/or reconcile.
- **Line 205 — uncited load-bearing specifics.** "40% more effectively… METRs above
  70% fell from 26% to 9%." Source them.
- **Line 19 vs 51 vs ch 6:** 60,000 vs 100,000 — reconcile and distinguish
  monthly-basic vs ASEC vs enhanced-file counts.
- **Line 67:** 2024 SPM threshold "about $39,000" for two-adult/two-child renter —
  reads high vs published (~$34–37k for 2023); verify year/tenure.
- **Line 15:** Pechman–Okner 72,000 households — cited, plausible; keep.

### From-scratch verdict
**Rewrite the data + baseline scaffolding; keep the analysis, neutrality, and case
studies.** (a) Replace Enhanced-CPS pipeline with the synthetic-microdata account;
(b) refresh every US baseline for OBBBA; (c) fix the 2.9M/2.1M attribution and date
the 9.6%; (d) de-duplicate case studies (this chapter owns them); (e) use the
Tracker as the encode-the-corpus on-ramp and the revenue-gap/behavioral discussion
to hand off to the determinism-vs-prediction split — without any "Thesis predicts
well" language (0 witness-verified).

## Part-level assessment (Part II)

Keep four chapters but re-cast three around the three-ingredients spine, which maps
one-to-one onto the new architecture: rules → Axiom (encode the corpus); data →
populace (integrate the microdata); dynamics → the seam where determinism ends and
Thesis begins. Ch 5 stays the origin story with the recomposition hinge ending. Ch 6
becomes the load-bearing chapter. Ch 7 recast as the verification substrate. Ch 8
becomes calibrated aggregation + the boundary. Framings that survive: the API/
household-calc-as-primitive; the cliff finding; reliable-vs-caution honesty;
neutrality; validation-upgraded-to-oracles; Pechman–Okner and Orcutt grounding.
Framings that must go: PolicyEngine-as-end-state with sustainability as the open
question; Enhanced CPS as the data achievement; rules-as-code as a ch 10 footnote;
TCJA-expiration-as-pending; the $2,000 CTC as current law.

---

# Report 3 — Ch 9–11 (AI, infrastructure, uncertainty)

## Chapter 9 — AI enters the picture

### Summary
PolicyEngine's AI arc from the March 2023 "Explain with AI" button through ChatGPT
prompt-generation, tool-calling, MCP, and multi-agent workflows, to government
deployments (IRS Agentforce, California's Poppy) and policy-designing AI (AI
Economist, TaxAgent). Organizing thesis: deterministic backends, AI frontends. Best
idea: the binding constraint shifted from model capability (2023) to tool quality
(2025). Closes by handing "should AI design policy?" to Part III.

### Strengths
- **The bottleneck-shift argument (line 78)** is the load-bearing insight and the
  cleanest bridge into ch 10. Keep prominent.
- **"AI as priors, not authorities" (130–136)** is the model for how the whole book
  should handle AI — the LLM's value is "diagnostic," not authoritative.
- "What AI doesn't do" (114–126) crisply defines the trust boundary.
- Concrete grounding: the Connecticut WIC family (13, 21), the ARPA EITC prompt
  with real output (49), the 67% marginal-rate decomposition (106).
- The convergence beat (194–204): PolicyEngine, IRS Agentforce, and Poppy all
  landing on the same architecture is a genuine, non-hype observation.

### Weaknesses
- Mantra repetition: "deterministic backend / AI frontend" (or paraphrase) at lines
  29, 33, 35, 37, 70, 148, 202, 204, and the close. Cut at least half.
- "The research assistant vision" (140–148) and "Toward intelligent policy analysis"
  (176–192) cover the same ground. Merge.
- The regulation close (224) — EU GPAI, "1,208 AI-related bills," Colorado AI Act —
  is an appended grab-bag, not an earned ending.

### Stale / wrong
1. **Line 118 — CTC figure now wrong.** "The Child Tax Credit maximum is $2,000
   because Congress set it at $2,000, not because an AI inferred it." OBBBA: $2,200
   for 2026. The pedagogical point survives with the number swapped.
2. **Line 80 — LLM-capability numbers stale as *current* state.** Gemini 2.5 Pro
   ~1/3, Claude Opus 4 27% (TaxCalcBench, 2025 models). Fix: add **PolicyBench** as
   the current evidence (Claude Fable 5 at #2) that even frontier-2026 models fail
   complete calculations without deterministic tools. Do not assert an unsourced
   pass rate.
3. **Line 224 — Colorado AI Act tense/date needs verification** ("effective June
   2026… would require") — we are past June 2026 and the effective date has moved
   before.
4. **Line 148 — conceptual.** "The microsimulation model would remain the
   authoritative source of truth" → post-recomposition, that's the rules layer
   (Axiom/RuleSpec) + calibrated microdata (populace).

### From-scratch verdict
**Keep, light rewrite.** Fix the CTC number; refresh capability evidence with
PolicyBench; tighten mantra repetition; merge the two vision sections; re-end on a
forward hook into verification ("a good tool for AI to call is one whose every
number can be checked against ground truth — which turns out to be buildable").

## Chapter 10 — Infrastructure for the future

### Summary
AI systems need deterministic, auditable tax-benefit tools; no one provides the full
stack; it should be a public good. Surveys partial solutions (April, Column Tax,
Avalara, screeners), the "Priya" fintech composite, "can't be trained away," an
original administrative-quality argument (Medicaid unwinding, Deloitte
eligibility-system failures), then names Axiom Foundation, Brier Institute, Atlas,
RAC, AutoRAC. Explicit framing: "aspiration, not accomplishment."

### The problem: the core frame is now false
The governing note-to-reader (line 3) — "This chapter describes infrastructure that
doesn't yet exist… the solutions are speculative" — is no longer true, and the
chapter is at war with itself (line 107 concedes "That gap no longer feels purely
hypothetical" while lines 3 and 243 insist on aspiration). The infrastructure
exists at scale, launches July 28, 2026, has an anchor funder (Ballmer), a President
(Ariel Kennan), a fiscal sponsor (PSL-F), and a CEO (Max). Deepest rewrite of the
three.

### Catalogue of "doesn't exist yet / aspiration / planned" statements overtaken

| Line | Quote | Reality |
|---|---|---|
| 3 | "infrastructure that doesn't yet exist… the solutions are speculative." | Built and launching; premise void. |
| 3 | "a technical exploration of what would be needed" | Now describes what was done. |
| 82–85 | "Such infrastructure **would require** three components" | All three exist (RuleSpec + populace/microplex + simulation layer). |
| 93–95 | "Such infrastructure **must be** deterministic… **When** an AI agent calls…" | Realized: signed manifests, bi-temporal parameters, oracle validation. |
| 105 | "That gap… still has to be filled." | Being filled at scale. |
| 113 | "is attempting to build… through Atlas, RAC, and AutoRAC" | Built; tool names retired. |
| 115 | "Recent RAC **prototypes**" | ~3,000 rule YAMLs with ~3,000 companion tests in production repos. |
| 209 | "**is taking shape**… **being built** as public goods" | Shipped; launching publicly. |
| 211 | "beginning with US federal and several states" | Federal + **28 states** with history; + UK (incl. Kingston-upon-Thames local scheme), CA, NZ, BE; + SOUTHMOD lanes (GH/UG/ZM/ET/RW done, TZ active, NG started). |
| 229 | "**Early experience suggests** this can meaningfully reduce encoding time" | Full pipeline: corpus lookup → prompt scaffold → Claude/Codex → gates (compile, CI, proof, oracle, money-atom) → signed manifests. |
| 237 | "The work is early… no production-scale public deployment yet." | The headline staleness: production-scale, multi-country, launch imminent. |
| 239 | "not because the infrastructure **has been built**…" | It has been. |
| 241 | "**If this specific attempt stalls**…" | The hedge is now coyness about the author's own launched org. |
| 243 | "The honest framing is aspiration, not accomplishment." | Inverted. |
| 245 | "the path to building it remains uncertain" | Path taken. |

### Naming issues (every retired name)

| In draft | Line(s) | Now |
|---|---|---|
| "cosilico" | filename (chapter title on line 1 is already clean) | Rename file; update `_quarto.yml` TOC + website slug map. |
| Brier Institute | 209, 213 | **Thesis Institute** — and the mapping is wrong, not just the name (see below). |
| RAC ("Rules as Code") | 113, 115 (×2), 211 (×2), 219, 225, 227; citation `@axiomrac2026` | **RuleSpec** (YAML). |
| AutoRAC | 113, 211, 229 | **axiom-encode** (the AI encoding pipeline). |
| Atlas | 113, 211 | The **corpus** service (~41k-concept registry, provision anchors, staged release scopes). |
| "The Axiom Project" | 211 | Verify — not confirmed as a current sub-brand. |
| "Axiom Labs" | not in body; `.claude/CLAUDE.md` line 5 | Existence unverified — confirm before it appears anywhere. |

### Substantive mapping error beyond the rename (209, 213)
Line 209 calls Brier "the home, now, for PolicyEngine's microsimulation alongside
calibration-native forecasting"; line 213 says microdata lives "with PolicyEngine
and the Brier Institute." The real end state is **three-way**: Axiom =
rules/determinism; **populace** = calibrated microdata (microdata does *not* live
at Thesis); Thesis = forecasting/prediction. PolicyEngine is recomposed *as* Axiom +
populace. Model it correctly; don't find-and-replace.

### Under-stated (true but now sells reality short)
- **Line 227** — oracle validation is far broader than "TAXSIM + state calculators":
  TAXSIM, PolicyEngine, UKMOD, EUROMOD, SOUTHMOD, with conformance scoreboards and
  ratchet CI gates. The seed of the chapter's best untapped vein.
- **Line 87** — "every computation includes a citation" is now *enforced* by the
  money-atom gate (build fails otherwise). The draft asserts the principle; reality
  has a mechanism. Show the mechanism.
- **Line 115** — the Housing Act notice-validity demonstrator is prescient: it
  anticipates the July 7 mission scope (ALL public policy; bindingness as metadata;
  authority/delegation chains first-class). Promote from aside to thesis.

### Other weaknesses
- The gap/aspiration hedge is restated at 15, 33, 37, 105, 177–187, 239, 241, 243,
  245 — most become deletable once reality is acknowledged.
- Framing devices stack up (April → Column Tax → Priya → Medicaid unwinding); the
  **administrative-quality section (126–143) is the most original material** and
  should be elevated.

### From-scratch verdict
**Rewrite (largest surgery).** Flip prophecy → field report: kill the line-3 note
and the line-243 close; keep the problem framing as the *why*; preserve the
administrative-quality section intact; replace RAC/AutoRAC/Atlas/Brier with
RuleSpec/axiom-encode/corpus/Thesis and model the three-way decomposition correctly;
make the oracle/verification program the new spine; answer the "quiet staleness"
governance fear concretely with the conformance ratchet; optionally land the Nikhil/
No 10 beat as evidence governments are absorbing this capability (with disclosure).

## Chapter 11 — The uncertainty gap

### Summary
Microsimulation's dirty secret: point estimates without confidence intervals.
Taxonomizes uncertainty (input/parameter/structural/future), shows why it matters,
surveys partial solutions (Monte Carlo, Bayesian, Squiggle, bootstrap, scenario),
runs a real paired-subsample PolicyEngine demonstration (March 31, 2026),
benchmarks fields that handle uncertainty well (weather, clinical trials, finance,
climate, elections), confronts structural uncertainty (Finland UBI, ACA mandate),
closes on epistemic humility.

### Strengths
- **Best-argued chapter of the three.** The CBO "23 million" opening and Minority
  Report frame land without purple prose.
- The uncertainty taxonomy (25–33) and the ETI meta-regression (29) — 1,720
  estimates, 61 studies, mean 0.30, $100B-vs-$60B swing — are textbook "numbers
  that illuminate."
- **The paired-subsample demonstration (111–123)** is the chapter's peak: real,
  dated, reproducible, honest about scope.
- "How other fields handle uncertainty" (155–171): the weather standard —
  probabilities *verified* against outcomes and recalibrated — is precisely the
  right bar.
- Structural uncertainty (175–191) with Finland UBI and the ACA mandate is
  sophisticated and honestly told.
- The closing triptych (229–233) earns its rhetorical turn.

### Weaknesses
- **The one conceptual blind spot: the chapter doesn't know Thesis exists.** It
  frames uncertainty-aware analysis entirely as a future feature of PolicyEngine
  ("The Aspiration," 133; "PolicyEngine will eventually report uncertainty bounds,"
  217) — while a whole institution is being stood up as the prediction pole.
  A PolicyEngine-shaped hole where the institutional answer belongs.
- Portfolio-tour risk: EggNest (83), Fred Forecaster (91), Democrasim (99),
  Squigglepy (99), MicroCalibrate (217) start to read like a tools inventory. Keep
  the ones that carry argument, prune the rest.
- Mild list-iness in the six-field and six-solution surveys.

### Stale / wrong
1. **Lines 133, 217 — "aspiration" framing now half-answered institutionally.** Not
   wrong, but incomplete: name Thesis as the forecasting pole and populace/microplex
   as the input-uncertainty machinery.
2. **CRITICAL DISCIPLINE — the Thesis addition must not become a forecast-accuracy
   claim.** 0 witness-verified resolved forecasts. Describe Thesis as *building
   toward* the weather standard, explicitly not as having achieved validated
   accuracy. The chapter's existing epistemic-humility voice is the perfect register
   for exactly this caveat.
3. **Line 25** — Enhanced CPS 97% (Chapter 8 back-reference): true as history; add a
   forward pointer to populace/microplex, whose purpose is to *quantify* the error
   this chapter cares about.
4. **Line 113** — the dated experiment is a legitimate record; note the data
   substrate is now populace so a late-2026 reader isn't confused.

Not stale: no validated-forecast claims, no close-hold partners, CBO/PWBM/weather
treated respectfully. The problem is an *absence* (Thesis), not an *error*.

### From-scratch verdict
**Keep, targeted addition.** Give the "Road ahead / Aspiration" arc an institutional
subject: the uncertainty gap now has a named answer being built, holding itself to
the weather standard, with zero verified forecasts yet — and the chapter says so.
Trim the personal-tool name-drops.

## Cross-cutting assessment (ch 9–11)

The three chapters were drafted as a uniform "vision" block; reality has moved them
to different distances from "now." Ch 9: delivered — report it (PolicyBench as the
current evidence). Ch 10: delivered — retire the disclaimer; field report, not
thought experiment. Ch 11: half-delivered — name the vehicle, keep the humility.

The unifying spine is the gating test the book implies but never states: **per-unit
verifiability against ground truth; absent it, agent-scale generation is confident
fiction.** Cast that way, the three become one argument — Axiom encodes (10),
populace integrates (threaded through 8/11), Thesis forecasts (11) — with ch 9
establishing why (AI is the interface; tools are the constraint).

**What the verification program offers that the draft entirely lacks** (currently
one thin sentence, ch 10 line 227):
1. **The money-atom gate** turns "traceable to statute" from promise to
   merge-blocking mechanism.
2. **Oracle parity numbers** give the deterministic layer its own "numbers that
   illuminate": UK income tax 5/5 exact incl. Scottish bands 9/9; EUROMOD Belgium
   100% explained / 0 unexplained; TAXSIM, PolicyEngine, SOUTHMOD lanes.
3. **Upstream bug filings are the strongest single new beat in the book** — the
   machine encoding became precise enough to catch errors in the human-built
   reference models; handled as collaborative bug-filing, it stays respectful
   rather than triumphalist. Nothing in the draft has this much narrative torque.
4. **The conformance ratchet** is the concrete answer to ch 10's "quiet staleness"
   governance fear: coverage only rises, unexplained only falls, enforced in CI.

Housekeeping: share one vocabulary across 9/10/11 (Axiom/populace/Thesis); rename
the ch 10 file; check `_quarto.yml` and references.bib keys (`@axiomrac2026`,
`@axiomfoundation2026`, any cosilico/brier keys); confirm or strike "Axiom Labs" in
`.claude/CLAUDE.md`.

---

# Report 4 — Part III (ch 12–15)

Global note: **"Cosilico" is already scrubbed from these four chapters** — they say
"Axiom" correctly. The rename that has NOT happened is **Brier → Thesis** (ch 14
lines 7, 212; ch 15 lines 49, 69) — the most mechanical, highest-priority fix in
Part III.

## Chapter 12 — Simulating opinion

### Summary
Opens with Argyle et al. (2023), builds a balanced survey of silicon sampling
(optimists Argyle/Mei vs skeptics Santurkar/Bisbee), lands on "works for
well-studied populations on well-studied questions." Introduces HiveSight as a
microdata-grounded persona engine, walks a congestion-pricing example, catalogs
systematic biases, adversarial risks, and a calibration research program. Closes on
information access.

### Strengths
- The empirical-literature section (15–27) is the best-argued passage in Part III —
  counterarguments presented *before* the sell. The book's stated standard actually
  met.
- "Systematic biases" (102–113) and "Adversarial considerations" (119–129) are
  specific and non-defensive: manipulation targeting, false legitimacy, feedback
  loops, minority-view erasure.
- The congestion-pricing example (75) is concrete and correctly hedged; "the value
  isn't replacing the real survey, it's deciding whether the real survey is worth
  fielding" is a genuinely useful reframe.
- The microdata-grounding distinction (67–73) — structured demographic diversity vs
  temperature noise — ties HiveSight to the book's spine.

### Weaknesses
- **Over-hedged to the point of self-erasure**: the note-to-readers (3), "a
  prototype" (63), and stacked "experimental/proof of concept/open question"
  qualifiers. Now that v2 shipped, dial back to *earned* humility.
- The calibration section (133–149) restates the biases section (102–113). Merge.
- Line 95 imports an engineering status note into a book.

### Stale / wrong
- **Lines 63–65 — HiveSight described as pre-product** ("not a production platform,
  but a proof of concept"). v2 rebuilt and shipped July 7, 2026. Reframe as a tool
  in use while keeping accuracy humility (shipping ≠ validated). Also line 3 and
  line 187.
- **Line 95 — frozen in-progress engineering detail** ("12,295 rows… GSS
  normalization and the full runner remain unfinished"). Cut the row-count; keep
  "benchmark protocol before benchmark claims."
- **Lines 71, 181 — "the same microdata that powers PolicyEngine"** — defensible;
  note the layer is now populace/microplex for consistency with ch 15's recap.
- **Line 33 — "$140 billion on survey research" [@esomar2024market]: VERIFIED**
  (~$142B insights industry, 2023). Minor: that's the whole insights industry;
  soften the noun.

*(Orchestrator addendum: the v2 mechanism change — persona roleplay retired after
benchmarking at 36.6pt MAE; shipped estimator = post-stratification cells +
verbalized distributions, 6.2pt subgroup MAE best-in-test, direct estimation still
best on toplines — supersedes the persona mechanism at lines 67–73 and should
become the chapter's centerpiece result. See the header note.)*

### From-scratch verdict
**Keep, light rewrite** (deepened per the addendum): update status, report the
registered benchmark arc honestly (including the tie on toplines), cut the
row-count, compress the redundant calibration section. The "operating range, not a
general substitute" conclusion survives.

## Chapter 13 — Simulating democracy

### Summary
Why democratic outcomes diverge from voter welfare, through the strongest skeptics
(Achen & Bartels; Caplan), narrowed to a modest claim: does voter *accuracy about
policy impacts* matter at the margin? Builds Democrasim as an explicitly labeled toy
model, runs the Sarah worked example, surveys real-world evidence (Ferraz–Finan,
voter guides, Kansas, ACA), covers Arrow/Gibbard–Satterthwaite and futarchy, closes
with PolicyEngine as "one component among many."

### Strengths
- **The most intellectually honest chapter in the book**: leads with the evidence
  against its own thesis; the objections section (158–184) steelmans four real
  counters.
- The values/beliefs separation via futarchy (142–154) — "values are for humans,
  facts are for tools" (154) — is the cleanest articulation in Part III of the
  book's core move.
- **Democrasim's "toy model" framing (3, 43) is accurate to ground truth** — no
  rename or status correction needed here.
- The persuasion-asymmetry point (99) is a sharp self-critique most authors would
  omit.

### Weaknesses
- **The Sarah worked example (73–79) strains**: precise dollar figures ("$4,000
  through the CTC expansion," "$2,500 in state taxes," "$1,500 better off") wear
  the costume of calculation without being sourced or reproduced. Mark clearly
  hypothetical or make it a real PolicyEngine run.
- "What the real-world evidence shows" (89–107) and "What political science
  actually says" (111–121) overlap. Merge.
- The PolicyEngine framing (125–138) predates the recomposition; the "transparent
  methodology" claim (131) is now backed by RuleSpec encodings — stronger evidence
  than the chapter musters.

### Stale / wrong
- **Line 103 — uncited specific**: "35% of Americans didn't know the ACA and
  'Obamacare' were the same law" (the Feb 2017 Morning Consult/NYT poll — real but
  needs a key).
- Line 101 Kansas 2017 — verified correct. Lines 95, 115, 119, 144, 148 citations
  spot-checked, plausible/correct.
- No Brier/HiveSight/Cosilico staleness in this chapter.

### From-scratch verdict
**Keep, trim and re-anchor.** Merge the two empirical sections; decide the Sarah
numbers (hypothetical-label vs real run). Crucially, **this chapter — not ch 14 —
is the better candidate to carry weight toward the climax**: its "facts for tools,
values for humans" thesis is the bridge to Thesis's counterfactual forecasting. Add
a paragraph connecting the accuracy-multiplier idea to counterfactual forecasting —
the empirically-scored version of the perception problem Democrasim only toys with.

## Chapter 14 — Simulating values

### Summary
Proposes reframing AI alignment as forecasting where human values are heading.
Surveys the alignment landscape (Russell, RLHF, Constitutional AI, idealized
values), presents the 2024 experiment — 17 GSS variables, GPT-4o quantile-prompted,
reportedly 2.2× better than baseline but missing the same-sex-acceptance reversal —
extends to long-term projections, heterogeneity-as-target, cross-cultural
trajectories, philosophical precedents (Rawls, Habermas, Sen/Nussbaum), governance,
and a "capstone" synthesis.

### Strengths
- **The failure is the best part**: foregrounding the HOMOSEX reversal that
  "humbled every forecaster" (155–157, 386) is exactly right.
- The reflection-problem section (281–299) — temporal change ≠ reflection, adaptive
  preferences, operationalizing "reasonable" — is philosophically serious.
- Heterogeneity-as-engineering-constraint (78–101) is a genuinely interesting
  reframe; the aleatoric/epistemic split (104–115) is technically correct.
- The governance section (323–345) asks the right adversarial questions.

### Weaknesses
- **Inverts the book's own epistemic hierarchy by making the least-validated
  material "The Capstone" (349)** — the most theoretical plank in the most
  prominent structural position.
- **EA/rationalist register**: "post-scarcity, post-reflection humanity" (70, 82),
  "the long reflection," aligning AI to "projected 2100 values" — in-group-coded;
  costs credibility with the book's policy/general audience.
- **The stack diagram (214–233) overstates integration**: three of its five boxes
  are toy/preliminary/unbuilt; the prose admits it, the diagram doesn't.

### Stale / wrong — the most, and the most serious
1. **Lines 7, 212 — "Brier Institute" dead name**; line 212's whole paragraph names
   **Brier-1** and **the Brier Almanac** (retired product names; the scoring board
   maps to the fact ledger). Rename to Thesis; get current product names from Max —
   don't invent.
2. **Lines 7, 212 — overclaim of a validated forecast track record
   (witness-verification violation).** "the track record is public and improvable"
   + "prototypes with some validation" imply a live, scored record. Ground truth: 0
   witness-verified resolved forecasts. Soften to: will post falsifiable,
   ledger-scored forecasts; no resolved track record yet. (The 17-variable
   *backtest* is a legitimate historical result — the prohibition bites on *live*
   forecasts.)
3. **Lines 18, 155, 167 — the HOMOSEX "72% → 55%" drop is inflated and contradicts
   the author's own data.** The 72% conflates GSS with Gallup's moral-acceptability
   series (peak 71% in 2022). GSS "not wrong at all" was ~58% (2018), low-60s
   (2022); **Max's own ea-forum draft uses 61% for 2022** and 54.7% for 2024. Real
   GSS move ≈ **6–7 points (61%→55%), not 17**. Fix or the reversal loses
   credibility the moment a reviewer opens the GSS.
4. **Lines 148–149 — "2.2× better" is baseline-shopped and inconsistent across the
   author's two writeups.** 2.2× only vs the *weakest* baseline (historical mean
   10.6/4.8); vs linear it's 1.5× (7.2/4.8). The EA draft's "2.2×" is a *different*
   computation (Claude vs ETS on 2 variables). State the baseline explicitly,
   report both multiples, reconcile which experiment the book describes.
5. **Lines 52, 284 — same-sex marriage "32% in 1986" dubious/uncited.** Gallup's
   series begins 1996 (27%); GSS MARHOMO begins 1988 (~11–12%). No clean source for
   32%/1986. Cite or move the baseline to a real data point.
6. **Lines 186–194 vs EA draft — long-term projections don't match** (book: 2030
   62%/2050 72%/2100 80%; draft: 68%/75%/85%). Reconcile or note the calibration
   step explicitly.

### From-scratch verdict
**Demote and de-risk; consider spinning out.** (1) Rename Brier→Thesis; strip every
track-record implication; (2) fix the HOMOSEX numbers; (3) cut the EA-coded 2100
register in favor of the near-term testable claim (LLMs vs naive baselines at
3-year survey forecasting — sometimes yes, sometimes catastrophically no);
(4) demote from Capstone to a clearly-bounded speculative horizon that explicitly
does not bear the book's weight. The full alignment argument already has its honest
home: the EA Forum post.

## Chapter 15 — Society in Silico

### Summary
The synthesis: returns to Serac/Rehoboam, contrasts closed vs open path, recaps
what's built (Orcutt → CBO/JCT → OpenFisca → PolicyEngine → Axiom/Brier), honestly
lists what hasn't, makes three closing arguments (democratic, AI tool-calling,
five-year vision), lands the Rehoboam payoff.

### Strengths
- **The Rehoboam bookend lands**; "The open-source movement changed this not by
  producing better models, but by making models *improvable*" (199) is the book's
  thesis in one sentence.
- "What We Haven't Built" (59–71) — naming the four gaps explicitly is more
  persuasive than any success claim.
- The "Why It Matters" failure-mode catalog (93–105) is concrete; "the
  counterfactual is worse" (105) is the right register.
- The AI tool-calling argument (129–149) correctly grounds the thesis with
  TaxCalcBench, tying back to the intro.

### Weaknesses
- **"What We've Built" (51) undersells the now-real Axiom scale** — the strongest
  evidence for the book's thesis, nearly absent. The climax should lead with the
  encoding infrastructure that shipped.
- The three closing arguments repeat the "voter enters household circumstances /
  analysis within hours" scenario three times (119, 165, 221). Pick the best.
- PolicyBench is absent; the chapter leans entirely on TaxCalcBench (139).

### Stale / wrong
1. **Line 49 — "Brier Institute" + inaccurate architecture.** (a) Brier → Thesis;
   (b) the recomposition is Axiom (rules) + populace (microdata) — microsimulation/
   microdata is *not* "housed at Thesis"; (c) "scored answers" implies a live
   scoreboard — soften per 0-witness-verified.
2. **Line 69 — "Axiom and the Brier Institute are early."** Rename; "early" is now
   also slightly stale for Axiom.
3. **Line 51 — uncited/verify specifics**: "9,000 administrative totals,"
   MyFriendBen "four states," and the Enhanced CPS→microplex supersession.
4. **Line 51 — CLOSE-HOLD SENSITIVITY: "Federal Reserve Bank of Atlanta"** named as
   a validation partner. Per standing guidance (do NOT name in partner materials),
   a published book is the most public possible partner material. Needs Max's
   explicit sign-off — flag, do not silently keep.
5. **Line 67 — "When Congress debated the 2025 TCJA extension"** — enacted (OBBBA;
   CTC $2,200 in 2026). Update; same currency issue in intro lines 93–95.
6. **Line 171 — "HM Treasury would formally evaluate PolicyEngine…"** — verify the
   characterization; adjacent to the Nikhil/No 10 context.

### From-scratch verdict
**Keep as the closer; re-weight the recap.** Lead "What We've Built" with the
shipped Axiom scale and the two-pole architecture over populace; rename
Brier→Thesis; resolve the Atlanta Fed sensitivity; de-duplicate the thrice-told
scenario; add PolicyBench.

## Part-level assessment (Part III)

**(a) Restructure.** The current escalation (opinion → democracy → values) is
thematically elegant but empirical solidity *falls* as the chapters climb — the
book crescendos into its least-grounded material. The stronger spine now exists:
**Thesis's live counterfactual forecasting** ("Medicaid call-wait-times in Mar 2027
if the work-requirement deadline is delayed") — simulate society, then get scored
by reality — satisfies the gating test with a public scoreboard and is a far more
credible climax than forecasting 2100 values. Recommended: opinion (shipped tool) →
prediction/two-poles spine chapter (the climax) → democracy re-anchored as the
civic why-it-matters → values demoted to a bounded coda → synthesis.

**(b) Ch 14 is separable, and yes it risks credibility.** The book's thesis is
carried completely by chs 1–13 + 15. Value forecasting rests on none of the
microsimulation machinery. It's the least-validated material in the most prominent
slot; its headline empirical claim is shaky on the author's own terms (HOMOSEX
inconsistency; baseline-shopped 2.2×); and its register is EA-coded. Don't cut the
ideas — cut their *load*: demote to a clearly-bounded penultimate chapter, fix the
numbers, and let the Thesis spine + ch 13's civic argument carry the climax. The
book is more credible if its last big idea before Rehoboam is something that gets
scored by reality rather than something that forecasts the year 2100.

### Highest-priority fixes (mechanical → strategic)
1. Brier → Thesis everywhere (ch 14: 7, 212; ch 15: 49, 69).
2. Strip validated-forecast-track-record language (ch 14: 7, 212; ch 15: 49).
3. Fix HOMOSEX 72%→55% to ~61%→55% (ch 14: 18, 155, 167).
4. HiveSight prototype→shipped, keep humility (ch 12: 3, 63–65; cut 95's
   row-count) — plus the cells-not-personas mechanism update (header note).
5. Resolve Atlanta Fed close-hold (ch 15: 51).
6. State the 2.2× baseline explicitly / reconcile the two experiments (ch 14:
   148–149).
7. Rebuild ch 15's "What We've Built" (51) around the real scale + two-pole
   architecture; add PolicyBench.
8. Restructure Part III around Thesis counterfactual forecasting; demote ch 14 to a
   bounded coda.

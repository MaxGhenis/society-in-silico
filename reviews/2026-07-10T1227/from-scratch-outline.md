# Society in Silico — from-scratch architecture (2026-07-10)

*What this book would look like designed today, given everything that changed between
the May 30 draft and July 10 reality. Companion to `synthesis.md` (the review itself).*

---

## Why the redesign is warranted

The May 30 draft was written as **vision-plus-history**: Parts I–II tell the story up
to PolicyEngine, chapter 10 sketches infrastructure that "doesn't yet exist," and
Part III speculates. Six weeks later, the vision chapters have been overtaken by
shipped reality, and — more importantly — the *shape* of the story changed:

1. **The infrastructure exists.** ~3,000 US rule files plus 28 states in `rulespec-us`;
   UK/CA/NZ/BE monorepos; an AI encoding pipeline with compile/proof/oracle gates,
   signed manifests, and money-atom source-grounding; oracle parity with UKMOD to the
   pound and EUROMOD Belgium at 100%-explained. The book's central "aspiration" is now
   a demonstration.
2. **Five countries in a week.** Ghana, Uganda, Zambia, Ethiopia, Rwanda encoded and
   validated against UNU-WIDER's SOUTHMOD models — Ethiopia in one overnight run —
   with findings ledgers reported back upstream (Ghana 13, Uganda **zero**, Zambia 8,
   Ethiopia 2, Rwanda 5). This is the single strongest evidence for the book's thesis
   and it happened after the draft was frozen.
3. **The org followed the epistemology.** PolicyEngine is being recomposed as
   **Axiom** (determinism: what does the law say?) + **populace** (representation: who
   are the people?), with **Thesis** (prediction: what will happen?) as the
   forecasting pole. "Axiom states, Thesis predicts." The two-institute frame is a
   better book spine than the project-by-project tour the draft inherited.
4. **The speculation got measured.** HiveSight v2's registered benchmark retired
   persona roleplay (36.6pt topline MAE) in favor of post-stratified cells (6.2pt
   subgroup MAE, best in test) — chapter 12's speculation now has empirical results,
   including honest negative ones. PolicyBench put 20 frontier models on a public
   board (best: ~1 in 6 household calculations still wrong by >$1). The uncertainty
   chapter's "aspiration" now has an institution being built around it.
5. **The names died.** "Cosilico" and "Brier Institute" (and Brier-1 / Brier Almanac)
   are retired; the forecasting institute is the **Thesis Institute**. Ten "Brier"
   mentions across six manuscript files, plus the ch-10 filename, are stale.

The May 30 review fixed factual errors and applied the first Axiom reframe. What it
could not do is what a from-scratch design does: move the book's center of gravity
from "PolicyEngine, then a vision" to "a working method for building verified public
infrastructure at agent scale."

---

## The thesis, restated for today

> Every claim about public policy decomposes into four questions — **what does the
> law say** (rules), **who are the people** (data), **what will happen**
> (prediction), and **what do we want** (values). Each is answerable by an open,
> verifiable layer of computational infrastructure, each verified differently: rules
> against statute and reference calculators, populations against surveys and
> administrative totals, predictions against reality when the official number lands,
> values against what people actually say and choose. AI agents just collapsed the
> cost of building all four layers — but agent scale without per-unit verification is
> confident fiction. The book is the story of building the stack, the discipline
> that keeps it honest, and the fork — open versus closed — that decides who it
> serves.

Compared to the current thesis (00-thesis.md), this keeps the aspiration and the
Rehoboam fork, but adds the two things the draft lacks: the **four-layer
decomposition** (which reality now instantiates as Axiom / populace /
PolicyEngine-simulation / Thesis / HiveSight) and the **verification law** ("agent
scale without ground truth = confident fiction"), which is the book's most
generalizable idea and is entirely absent from the May draft.

---

## Proposed structure

Five parts, 17 chapters, ~80-85k words. Chronology survives as the surface (Part I is
still history — it reads well), but the argument is the stack. Part II compresses the
current six PolicyEngine chapters to three; the agent turn expands from two chapters
to five, because that is where the new material and the new ideas live.

### Front matter
- **Preface** — rewrite. Current org reality (Axiom launched, Thesis launching,
  PolicyEngine recomposing), Washington DC (not "San Francisco"), and the honest
  "written mid-build" frame — now with the twist that parts of the 2025 draft's
  *future* chapter became the 2026 draft's *past* chapter, which is itself evidence
  for the book's claim about the pace of the agent era.
- **Introduction: The model and the world** — keep the Rehoboam fork and the "AI
  can't do your taxes" hook (both work; every 2025 reader persona praised them).
  Update the evidence spine: TaxCalcBench 2025 (best model < 1/3 of full returns) →
  PolicyBench 2026 (20 models on a public board; best ≈ 1 in 6 household
  calculations wrong by > $1; errors are family-level, not rounding). Close by laying
  out the four questions as the book's map.

### Part I — The closed stack (origins)
*How government built an analytic stack the public couldn't see — and the test any
model must pass.*

1. **The birth of microsimulation** — Orcutt 1957, DYNASIM, the audacity of
   simulating households before the compute existed. Ending re-pointed: Orcutt's
   "interacting units which receive inputs and generate outputs" is literally the
   per-unit encoding model, and the 2026 payoff is per-unit *verifiability*, not
   just web access. (Current ch 1, trimmed; fix CANSIM→SPSD/M, the 67-vs-69-years
   dating, the 1968/1969 wobble; ration the "model the people" mantra.)
2. **The tax model wars** — one merged chapter from current ch 2 + ch 3's history
   half (they tell the same institutional→open story and currently triplicate the
   TCJA numbers with ch 4). Spine = the IRC §6103 "analytical moat": government
   models run on the universe of actual returns, outsiders get top-coded files —
   the permanent asymmetry whose answer is *synthesize and calibrate*, seeding the
   populace/microplex layer. OpenFisca/rules-as-code history lives here. UKMOD
   attribution made even-handed (Brewer led the Nuffield grant; the model is
   CeMPA's, directed by Richiardi).
3. **The accuracy question** — current ch 4, elevated to the hinge of the book: the
   three-level validation framework, the ACA natural experiment, random-walk-beats-
   CBO presented against interest (the seed of the prediction pole), the
   survey-data crisis (the seed of the data layer). Ends by stating the discipline
   the rest of the book is judged by: per-unit verifiability against ground truth.
4. **A wall of frustration** — new short chapter split out of current ch 3: the
   personal origin. Alex's >100% marginal rate, the family spreadsheets, Project
   Lorenz failing at Google, GiveDirectly, the UBI Center, recruiting Nikhil off
   Reddit. The memoir connective tissue the preface promises, placed as the bridge
   into Part II — and the reason to encode rules exactly: a single household's
   benefit cliff is invisible in any aggregate. (Nikhil's No 10 disclosure lands
   at first mention, pending his sign-off.)

### Part II — The open engine (PolicyEngine)
*Proof that the closed stack could be rebuilt in public.*

5. **Proof of concept** — UBI Center → PolicyEngine; the UK launch, HM Treasury
   pilot, US expansion; what "open" bought and what it cost. Nikhil's arc threads
   through here. Replace the current ending ("sustainability is the unsolved
   problem → ch 10") with the real hinge: building the tool proved that rules,
   data, and prediction are *separable concerns* — which is what makes the
   recomposition possible. (Current ch 5, trimmed; owns the origin story only.)
6. **The household and the society** — the calculator view and the population view as
   one chapter: marginal rates, benefit cliffs, distributional analysis, budget
   scoring, the neutrality challenge. (Current ch 7 + ch 8 merged — the review found
   the mini-budget beat told four times and MyFriendBen twice across Part II, which
   is evidence these chapters want to be one. Alternative if the merge loses too
   much: keep both but assign ownership — ch 5 origin, household chapter
   MyFriendBen, society chapter the case studies. Either way, the household
   calculation gets one new bridge sentence: it is the *atomic unit of ground-truth
   verification*, the level at which an encoded rule is provable against an oracle
   or a real determination.)
7. **Three ingredients** — rules, data, dynamics as the anatomy of microsimulation,
   now with the review's best structural idea: extend "two architectures" of rules
   encoding to **three** — spreadsheet/XML (EUROMOD), hand-written code-native
   (Tax-Calculator, classic PolicyEngine), and agent-encoded + oracle-verified
   (RuleSpec) — introducing the per-unit-verifiability criterion that Part III
   delivers in full. Updated data story: Enhanced CPS → **populace** (calibrated
   population priors) and **microplex** (synthetic microdata), methods foregrounded
   with the populace brand kept low-key per the public de-emphasis call. Dynamics
   reframed as the seam where determinism ends and prediction begins. This chapter
   becomes the hinge to Part III: each ingredient is an agent-buildable layer.
   (Current ch 6, revised; the deep encoding/verification/SOUTHMOD material lives
   in Part III where it has room, not stuffed in here.)

### Part III — The agent turn (Axiom and the verification discipline)
*The new heart of the book. What changed when agents could do the work — and the
discipline that keeps agent work honest.*

8. **The AI can't do your taxes** — LLMs as interface, not calculator;
   TaxCalcBench → PolicyBench; why the answer is tools, not training. Includes the
   MCP/tool-calling turn and PolicyEngine's AI integrations. (Current ch 9,
   rebuilt around the benchmark arc — including the meta-lesson that PolicyBench's
   own June narrative layer was caught fabricating derivations and had to be
   re-grounded in engine internals: even the audit layer needs ground truth.)
9. **Encoding the law** — Axiom: RuleSpec, the encoding pipeline, the corpus;
   money-atom gates (every monetary obligation traced to a quoted source excerpt);
   signed manifests; the mission scope — *all* public policy, statutes to agency
   manuals to a London borough's council-tax reduction scheme, with bindingness as
   metadata and authority chains modeled explicitly. (Current ch 10, rewritten from
   "what it would take" to "how it works" — with the launch-era story of the
   Foundation: Ballmer anchor, Ariel Kennan as President, PSL-F sponsorship.)
10. **The verification problem** — the chapter the current draft doesn't have and the
   book most needs. How do you trust law encoded by agents? Oracles (TAXSIM,
   PolicyEngine, UKMOD, EUROMOD, SOUTHMOD); parity to the pound; 100%-explained
   conformance boards with ratchets (coverage only rises, unexplained only falls);
   findings that cut both ways — including bugs found *in the oracles* and filed
   upstream; and the honest failures: the regeneration probe that showed encodings
   are not yet reproducible artifacts, the fabricated number caught at a gate. The
   argument: verification is not overhead on the method — it *is* the method.
11. **Microsimulation anywhere** — the SOUTHMOD week: five countries encoded and
    validated in days each; Uganda's zero-findings ledger vs Ghana's 13; what
    reporting findings back to UNU-WIDER looks like; the transfer paper and the
    custodian-pack idea — "open microsimulation anywhere doesn't require open
    microdata anywhere; it requires an open referee." What this means for countries
    that never had public policy-analysis infrastructure. (New chapter; the book's
    emotional peak for the infrastructure argument.)
12. **The decomposition** — why PolicyEngine is recomposing as Axiom + populace, and
    why the org chart followed the epistemology: determinism and prediction are
    different epistemic products with different verification loops, different failure
    modes, and different institutional homes. "An axiom is accepted truth; a thesis
    is a proposition to be tested." Introduces the Thesis Institute and the claim
    that turns Part IV: every estimate becomes a scoreable forecast. (New chapter,
    replacing the org-structure material currently scattered through ch 10/14/15.)

### Part IV — The prediction pole (Thesis)
*From point estimates to graded forecasts.*

13. **The uncertainty gap, and the scoreboard** — the dirty secret of point
    estimates; why CBO has no accountability loop; Monte Carlo/Bayesian methods as
    partial answers; then the institutional answer: a public docket of forecasts of
    government metrics — including under policy counterfactuals — each with an
    interval, each graded when the official number lands. Honest status: the
    scoreboard is live; the grades arrive with reality; none have resolved yet.
    (Current ch 11, upgraded from methods-survey to institution story.)
14. **Simulating opinion** — silicon sampling, HiveSight, and what measurement did to
    the romance: persona roleplay failed a registered benchmark; post-stratified
    cells over calibrated microdata won on subgroup structure; direct estimation
    stays competitive on toplines — reported honestly, tie and all. The
    "cells, not personas" result as a microcosm of the book's method: benchmark
    against ground truth before believing the demo. (Current ch 12, rebuilt around
    the registered results.)

### Part V — The horizon (values, and the fork)
*Clearly-labeled research directions; the return to Rehoboam.*

15. **Simulating democracy** — from opinions to elections to policy feedback loops;
    Democrasim as design study; what the accuracy parameter buys; why this remains
    aspiration. (Current ch 13, kept honest and slightly trimmed.)
16. **Simulating values** — demoted from "capstone" to a clearly-bounded speculative
    coda: can we forecast what an informed, reflective humanity would want?
    Aleatoric vs epistemic uncertainty in value space; CEV made empirical; Goodhart
    risks. The review verdict is firm: this material is separable from the book's
    thesis (it uses GSS time series + LLM prompting, none of the microsimulation
    machinery), it currently inverts the book's own proven→preliminary→theoretical
    hierarchy by sitting in the most prominent slot, and its headline numbers need
    correction (the GSS same-sex-acceptance reversal is ~61%→55%, not the draft's
    72%→55%; the "2.2×-better" claim is baseline-shopped). Fix the numbers, strip
    the EA-coded "2100 values" register, present it as "where the ground-truth test
    starts to fail" — and let the full alignment argument live in the EA Forum
    essay, where a research program that hasn't been conducted belongs.
17. **Society in silico** — the Rehoboam bookend: what we built is the anti-Rehoboam
    — open where Serac's was closed, graded where his was oracular, plural where his
    was singular. The fork restated as a live institutional choice. Invitation to
    participate. (Current ch 15, updated to the two-institute reality.)

### Back matter
- **Epilogue: written mid-build** — replaces scattered "this is early" hedges with
  one dated, honest status page: what existed at each draft (a device the book can
  keep updating edition to edition — the 2025 aspiration that became 2026 shipping
  is itself the argument).
- Technical appendix; try-it-yourself walkthrough (PolicyEngine, the Axiom rule
  graph, the Thesis docket); acknowledgments; references.

---

## What this design changes, in one table

| Current (May 30) | From-scratch (today) |
|---|---|
| 3 parts: Origins / Building / Research directions | 5 parts: Closed stack / Open engine / Agent turn / Prediction pole / Horizon |
| PolicyEngine = 6 of 15 chapters | PolicyEngine = 3 of 17; agent turn = 5 |
| Ch 10 describes infrastructure "that doesn't yet exist" | Ch 8–11 describe how the shipped infrastructure works and is verified |
| Verification appears as one section of ch 10 | Verification is a full chapter and the book's organizing discipline |
| "Brier Institute" as forecasting pillar | Thesis Institute; "Axiom states, Thesis predicts"; scoreboard chapter |
| Ch 12 speculates about silicon sampling | Ch 13 reports registered benchmark results (cells, not personas) |
| Global story = US/UK/Canada | Global story includes five SOUTHMOD countries + transfer method |
| Org story: PolicyEngine, then a foundation | Org story: the stack decomposed; org chart follows epistemology |
| AI evidence: TaxCalcBench (July 2025) | TaxCalcBench → PolicyBench 20-model board (July 2026) |

## What survives untouched in spirit

- The Rehoboam/Serac open→close bookend and the fork framing.
- "The AI can't do your taxes" as the technical hook.
- Part I's history (with the ch 3+4 merge).
- The honesty apparatus: speculation banners, validation tiers, volunteered
  limitations (the 33% revenue gap), "note to readers" boxes.
- The three-ingredients framework.
- The neutrality challenge section.

## Publication-sequencing constraints (why some of this can't ship yet)

The book should be *drafted* to the end state but *released* in step with the
institutional calendar:

- **No public two-institute story before Axiom's July 28 launch window closes**
  (~Aug 11); Thesis's frame debuts with its own launch (~Sep 15).
- **"PolicyEngine is a project of the Thesis Institute" language** only after
  Calibration Report #1 lands and the first Thesis-named grant closes (Phase 2, Q4
  2026). Until then, drafts can say the estimation work "is consolidating under"
  Thesis — or the manuscript simply stays private, which it is.
- **No forecast-accuracy claims** beyond witness-verified resolutions (currently
  zero). The scoreboard's honesty is the product; the book must model it.
- **Nikhil's No 10 role**: a gift to the narrative arc and a disclosure obligation in
  any UK-policy-adjacent external writing — but his title/role architecture is
  explicitly his call to shape. Nothing in the manuscript about it without his
  sign-off.
- **Never name close-hold partners**: the regional-Fed relationship and the Brussels
  SILC custodian conversation stay unnamed in all drafts.
- **UK entity freeze**: nothing about PolicyEngine UK Ltd while the visa process is
  in flight.

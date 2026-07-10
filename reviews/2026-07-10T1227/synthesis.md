# Society in Silico — full review + from-scratch verdict (2026-07-10)

*Whole-book review against July 2026 reality, run as four parallel chapter-group
passes plus an orchestrating read of the front matter, introduction, strategy docs
(two-institute end state), and current project state (Axiom launch, Thesis, populace/
microplex, SOUTHMOD lanes, HiveSight v2, PolicyBench, transfer paper). Companions:
`from-scratch-outline.md` (the proposed redesign) and `chapter-findings.md`
(line-level findings, all 15 chapters + front matter).*

---

## Verdict

The manuscript is in better shape than most drafts that sit for six weeks — the May
30 pass left citation hygiene clean and the honesty apparatus intact — but it has
been **overtaken by its own subject matter in a way no edit pass can fix**. The book
was designed as vision-plus-history: PolicyEngine is the achievement, chapter 10
sketches "infrastructure that doesn't yet exist," Part III speculates. Since the
draft froze, that infrastructure shipped at scale, five African countries were
encoded and validated against UNU-WIDER's models in about a week, the org
decomposed along the exact epistemic seam the book gropes toward
(determinism/prediction), and the speculation got measured — sometimes in your
favor (PolicyBench), sometimes against the draft's mechanism (HiveSight's personas
lost to post-stratified cells).

Written from scratch today, this is a different — and better — book: not "here's a
vision, watch us try" but **"here is a working method for building verified public
infrastructure at agent scale, the discipline that keeps it honest, and the fork
that decides who it serves."** The redesign in `from-scratch-outline.md` (5 parts,
17 chapters) keeps roughly 60% of existing material, but moves the center of
gravity from the PolicyEngine product tour (6 of 15 chapters → 3 of 17) to the
agent turn (2 → 5 chapters), makes verification a full chapter rather than one
sentence, and demotes value forecasting from capstone to bounded coda.

---

## The reality gap, in one table

| The draft says | Reality (July 2026) |
|---|---|
| "Brier Institute" (10 mentions, 6 files), Brier-1, Brier Almanac | **Thesis Institute**; product names retired; the scoring board is the fact ledger |
| Ch 10: "infrastructure that doesn't yet exist… aspiration, not accomplishment" | rulespec-us ~3,000 rules + 28 states; UK/CA/NZ/BE monorepos; launch July 28 |
| "Atlas, RAC, AutoRAC" (ch 10) | corpus service, **RuleSpec**, **axiom-encode** |
| Validation = "TAXSIM + state calculators" (one sentence) | Oracle program: TAXSIM, PolicyEngine, UKMOD (exact to the pound), EUROMOD Belgium (100% explained / 0 unexplained), SOUTHMOD ×5 countries; money-atom gates; signed manifests; conformance ratchets; upstream bug filings |
| Microdata "lives with PolicyEngine and the Brier Institute" | Three-way: Axiom (rules) + **populace** (microdata) + Thesis (prediction); PE recomposed as Axiom + populace |
| Enhanced CPS as the terminal data achievement | populace + **microplex** (synthetic eCPS replacement); us-data deprecated |
| HiveSight = "experimental prototype," persona-based | **v2 shipped July 7**; personas retired after benchmarking (36.6pt MAE); post-stratified cells won (6.2pt subgroup, best in test); registered paper live |
| AI evidence = TaxCalcBench (2025 models) | + **PolicyBench**: 20-model public board; best ≈ 1 in 6 household calcs wrong by >$1 |
| "When Congress debated the 2025 TCJA extension"; CTC $2,000 | **OBBBA enacted**; CTC $2,200 in 2026 |
| Signed "San Francisco, 2026" | Washington, DC (→ NYC) |
| Nikhil = co-founder/CTO | **+ No 10 since July 2026** — disclosure obligation in UK-adjacent writing, and the book's best unused narrative beat |

---

## Critical findings (fix regardless of any redesign)

**1. Close-hold partner named in the clear — needs your explicit decision.**
[05-policyengine-proof-of-concept.md:129](manuscript/part-2-building/05-policyengine-proof-of-concept.md)
names the Federal Reserve Bank of Atlanta MOU, the Policy Rules Database, CLIFF
tools, and the Colorado/New Mexico users;
[15-society-in-silico.md:51](manuscript/part-3-future/15-society-in-silico.md) names
them again as a validation partner. Standing guidance: do not name in partner
materials — and a published book is the most public partner material there is.
Keep only with the partner's sign-off on wording, otherwise generalize ("a
regional Federal Reserve Bank").

**2. Forecast-accuracy overclaims violate the ledger discipline.**
[14-simulating-values.md:212](manuscript/part-3-future/14-simulating-values.md)
("the track record is public and improvable") and
[15-society-in-silico.md:49](manuscript/part-3-future/15-society-in-silico.md)
("open, scored answers") imply a live, validated forecast record. As of today there
are **zero witness-verified resolved forecasts**. The scoreboard exists; the grades
arrive with reality. The book must model the same discipline Thesis does — it's the
thesis of ch 11 applied to yourself. (The 17-variable GSS *backtest* is fine to
report as a historical result.)

**3. Factual errors found by this pass** (beyond the May 30 fixes):
- **GSS same-sex-acceptance numbers are wrong and contradict your own EA draft**:
  ch 14 lines 18/155/167 claim 72%→55% ("a 17-point drop"); GSS and
  `ea-forum-value-forecasting.md` say ~61%→55% (~6 points). The 72% is Gallup's
  series. As written it triples the drama of the chapter's central example.
- **"2.2× better than baseline" is baseline-shopped** (ch 14:148): 2.2× only vs the
  weakest baseline (historical mean); 1.5× vs linear — and the EA draft's "2.2×" is
  a different experiment (Claude vs ETS, 2 variables). State baselines explicitly.
- **CTC poverty attribution** (ch 8:189): "the expansion alone lifted 2.9 million
  children" conflates the whole credit (2.9M children) with the expansion (2.1M).
- **CANSIM** (ch 1:166) is not a microsimulation model (it was StatCan's data
  service) — should be SPSD/M or deleted.
- **"Sixty-seven years later"** (ch 1:265) dates the draft to 2024; the preface says
  2026 → sixty-nine.
- **France Stratégie anachronism** (ch 3:9): didn't exist under that name until
  2013; in 2011 it was the Centre d'analyse stratégique.
- **UKMOD launch** (ch 5:7): October/Autumn 2019, not September.
- **CTC "$2,000" as current law** (ch 9:118 and throughout): OBBBA set $2,200 for
  2026.
- **Unexplained SPM gap** (ch 8:69): PolicyEngine 9.6% vs Census official ~12.4% —
  undated and unreconciled.
- **Same-sex-marriage "32% in 1986"** (ch 14:52): no clean source; Gallup starts
  1996 (27%), GSS MARHOMO 1988 (~11–12%).
- Still open from May 30: the **$2B vs $12B CTC-refundability contradiction**
  (ch 8 vs ch 11) — now also OBBBA-stale, so re-score once against current law.

**4. Disclosure gap: Nikhil at No 10.** Missing at every natural site (preface:7,
ch 3:161, ch 5:137–141, ch 7:131, ch 15:171). The book discusses UKMOD, IFS, and HM
Treasury piloting PolicyEngine — UK-policy-adjacent external writing where the
disclosure is obligatory. It's also the best unused beat in the book ("the
co-founder I recruited off Reddit now helps run the government's own analytical
machinery"). His role architecture is explicitly his to shape — nothing ships
without his sign-off.

**5. UKMOD/CeMPA attribution** (ch 2:113): the draft credits Mike Brewer (who led
the Nuffield grant) but omits CeMPA/Richiardi, whose model it is. Given the
relationship, the book should be scrupulously even-handed: name both, factually.

**6. Diplomatic assets the draft doesn't know it has:** the SOUTHMOD findings
ledgers (Ghana 13, Uganda **zero** — "UGAMOD statutorily exact everywhere tested,"
Zambia 8, Ethiopia 2, Rwanda 5) are reported back to UNU-WIDER collaboratively, and
the UKMOD/EUROMOD upstream bug filings flip the trust question — the encodings
became precise enough to catch errors in the reference models. Handled as
collaboration (which it is), this is the strongest single new material available to
the book, and it stays respectful to the EUROMOD/UKMOD teams.

---

## Chapter verdicts at a glance

| Current chapter | Verdict | One line |
|---|---|---|
| 00-thesis | Rewrite + put in build | Not in `_quarto.yml` — readers never see it; replace soft question with the falsifiable spine |
| 00-preface | Light rewrite | Fix SF→DC, Brier→Thesis, "doesn't yet exist"→field report, add Nikhil disclosure |
| 01-introduction | Light rewrite | Rehoboam + "AI can't do your taxes" keep; add PolicyBench, OBBBA, the four-question map |
| 1 Orcutt | Keep, tighten | Fix CANSIM, 67→69 years, 1968/69; end on per-unit verifiability |
| 2 Tax model wars | Merge with ch 3's history | §6103 moat becomes the spine; even-handed UKMOD attribution |
| 3 Open source | **Split** | History merges into ch 2; the personal origin (Alex's cliff — best writing in Part I) becomes its own bridge chapter |
| 4 Accuracy | **Keep + elevate** | Best chapter in Part I; becomes the book's hinge; extend with oracle results + PolicyBench |
| 5 Proof of concept | Keep, trim | Re-point ending: rules/data/prediction are separable → the recomposition |
| 6 Three ingredients | Keep frame, rebuild | "Two architectures" → three (XML / code-native / agent-encoded+oracle-verified); data → populace/microplex |
| 7 Household view | Keep | Signature cliff material timeless; add one bridge: the household calc is the unit of verification |
| 8 Society view | Rewrite scaffolding | OBBBA baselines, data stack, 2.9M/2.1M fix; keep neutrality + case studies |
| 9 AI enters | Keep, light rewrite | PolicyBench replaces stale capability numbers; cut mantra repetition |
| 10 "Cosilico"/infrastructure | **Deepest rewrite** | Prophecy → field report; RuleSpec/axiom-encode/corpus names; verification as spine; keep the administrative-quality section intact |
| 11 Uncertainty gap | Keep + targeted add | Best of ch 9–11; give the aspiration its institution (Thesis) without claiming validation |
| 12 Simulating opinion | Keep, rebuild core result | v2 shipped; report the registered benchmark arc — personas failed, cells won, direct still wins toplines |
| 13 Simulating democracy | Keep, trim | Most honest chapter; re-anchor to counterfactual forecasting; fix the Sarah numbers |
| 14 Simulating values | **Demote to coda** | Separable from the thesis; fix GSS numbers + 2.2×; strip EA register; full argument lives in the EA Forum essay |
| 15 Society in silico | Keep as closer | Rebuild "What We've Built" around shipped scale + two poles; resolve Atlanta Fed; Brier→Thesis |

---

## The from-scratch design (summary — full version in `from-scratch-outline.md`)

**Thesis, restated:** every policy claim decomposes into four questions — what does
the law say (rules), who are the people (data), what will happen (prediction), what
do we want (values) — each answerable by an open layer verified differently, and AI
agents just collapsed the cost of building all four. The gating law: **agent scale
without per-unit ground-truth verification is confident fiction.** The Rehoboam
fork stays as the frame; "Axiom states, Thesis predicts" becomes the institutional
embodiment.

**Structure:** 5 parts, 17 chapters. Part I "The closed stack" (Orcutt; the merged
tax-model-wars/§6103 chapter; accuracy elevated to the hinge; the personal-origin
bridge). Part II "The open engine" (PolicyEngine compressed to three chapters).
Part III "The agent turn" — the new heart: the AI-can't-do-your-taxes chapter
(PolicyBench), encoding the law (Axiom/RuleSpec/money-atoms), **the verification
problem** (oracles, ratchets, upstream bugs — the chapter the draft doesn't have),
**microsimulation anywhere** (the SOUTHMOD week + "open microsim anywhere requires
an open referee, not open microdata"), and the decomposition (why the org followed
the epistemology). Part IV "The prediction pole" (uncertainty gap → the Thesis
scoreboard; opinion → the cells-not-personas result). Part V "The horizon"
(democracy; values as bounded coda; the Rehoboam close).

**What survives untouched in spirit:** the Rehoboam bookend, the taxes hook, Part
I's history, the honesty apparatus (speculation banners, validation tiers,
volunteered limitations), the three-ingredients frame, the neutrality challenge,
Alex's cliff.

---

## Decisions only you can make

1. **Atlanta Fed naming** — ~~keep or generalize?~~ **RESOLVED 2026-07-10 (Max):
   keep the naming.** Residual copyedit check only: match the wording to the MOU's
   public description.
2. **Nikhil's treatment** — ~~how much of the No 10 arc to use?~~ **RESOLVED
   2026-07-10 (Max): use it.** Add the disclosure at first mention (preface / ch 3)
   and the narrative beat; exact role wording still tracks whatever Nikhil settles
   on for Phase 2.
3. **Ch 14 (values)**: demote-and-fix inside the book, or spin out to the EA Forum
   essay entirely and keep a 2-page gesture? (Review's lean: demote and de-risk;
   the ideas are good, their *load* is the problem.)
4. **Ch 7+8 merge** vs keep-separate-with-ownership (review found the mini-budget
   beat told 4×, MyFriendBen 2× — evidence they want to be one chapter, but the
   cliff material is strong enough to defend two).
5. **Publication sequencing**: the book can be *drafted* to the end state now, but
   "PolicyEngine is a project of the Thesis Institute" language is Phase-2-gated
   (Calibration Report #1 + first Thesis-named grant), the two-institute story
   shouldn't circulate before Thesis's own launch (~Sep 15), and no
   forecast-accuracy claims until witness-verified resolutions exist.
6. **"Axiom Labs"**: `.claude/CLAUDE.md:5` still names it as an entity you founded;
   everything else says pre-Axiom names are retired. Confirm or strike.
7. **populace naming**: public framing de-emphasizes populace, but the book has to
   name its data layer something. Recommend: name it once, plainly, as
   infrastructure ("calibrated population data — populace"), and lean on the
   methods elsewhere.
8. **The audiobook** (Jan 2026 render, two majors stale): re-render only after the
   rewrite lands.

---

## Repo hygiene (mechanical, no decisions needed)

- Rename `10-cosilico-infrastructure-for-the-future.md` → update `_quarto.yml:26`
  and `website/src/pages/book/[slug].astro` (slug map still says `cosilico → "Axiom
  Labs"`).
- `.claude/CLAUDE.md:5` — drop "and Axiom Labs" (pending decision 6).
- Delete the stale root `outline.md` (10-chapter, pre-Rehoboam); refresh
  `manuscript/00-outline.md` (still has `[[cosilico]]` links and the old part
  names).
- `references.bib`: reconcile `policyengine2022enhanced` (cited for an Aug 2025
  launch), retire/rename `@axiomrac2026`-style keys, add keys for the Asimov quote
  (ch 1:75), the Brewer/Reed quotes (ch 2:115/117), the ACA-Obamacare poll
  (ch 13:103), and the ~20 new sources the rewrite needs (PolicyBench, HiveSight
  paper, transfer paper, SOUTHMOD/UNU-WIDER, OBBBA scores).
- ~15 research notes under `research/` still carry Cosilico/Farness/Brier names.
- Data-consistency sweep: CPS 60k vs 100k households (ch 6 vs ch 8 — ASEC vs
  monthly basic, never distinguished); "2,700 parameters" vs "~3,000 rules"
  (different units — pick one sourced figure per concept).

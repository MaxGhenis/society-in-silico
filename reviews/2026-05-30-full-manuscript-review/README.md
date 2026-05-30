# Full manuscript review — 2026-05-30

A whole-book review of *Society in Silico* (15 chapters + front matter, ~60k words),
run as 11 parallel specialist passes (one per chapter pair, plus cross-book continuity,
web fact-checking, and a neutrality/overselling audit), with worked-example numbers
re-derived against PolicyEngine itself.

**Verdict:** the manuscript is strong and far more polished than the December 2025
review implies — citation hygiene is clean (all 140 in-text keys resolve), the historical
chapters are well-researched, and the honesty-about-limitations framing (per-chapter "note
to readers" banners, the thesis's "honest caveat," Ch. 8's "neutrality challenge") is better
than most trade nonfiction. The problems were concentrated in a set of **specific, checkable
factual errors** — exactly the kind a book whose thesis is "deterministic tools beat AI
guessing" cannot afford — plus a handful of overselling lapses and naming/structure drift
left over from the Cosilico → Axiom rename and the MyST → Quarto migration.

This pass **fixed** the high-confidence items directly (see below) and **flagged** the few
that need the author's decision.

---

## Fixed in this pass

### Factual errors (web- or PolicyEngine-verified)

| Location | Was | Now |
|---|---|---|
| Ch1 — Orcutt's heir | "His grandson, **Eli** Nakamura" | "His granddaughter, **Emi** Nakamura" (Clark Medal 2019 ✓) |
| Ch1 — Asimov | "Hari Seldon in *Foundation*" + misquote | narration in *Foundation and Empire*, verbatim quote |
| Ch1 — Simon & Newell | "at **Carnegie Mellon**" (1950s) | "at the **Carnegie Institute of Technology** (today Carnegie Mellon)" |
| Ch1 — SSRI chronology | "After the 1961 book, Orcutt moved to Wisconsin… founded SSRI in 1959" (impossible) | "moved… in 1958, founding the SSRI a year later" (before the book) |
| Ch2 — JCT | "the Budget Act of 1974 made JCT the official source" | "…**as later amended**…" (designation came via the 1985 amendment) |
| Ch2 — TCJA dynamic | growth "would generate **$389 billion**" | "would offset roughly **$385 billion**" (closes the $1.46T→$1.07T math) |
| Ch3 — OSPC founding | "In **2014**, he founded" | "In **2013**" (matches Ch2; Jensen was founding director 2013) |
| Ch3 — FRB/US | "publicly available since the **late 1990s**" | "dates to 1996 and became publicly available in **2014**" |
| Ch4 — Tax Foundation | dynamic TCJA "roughly **$1.0 trillion**" | "roughly **$0.45 trillion ($448 billion)**" (the $1.0T was the growth *offset*) |
| Ch4 — model spread | "disagree by a **factor of two**" ($1.0T–$2.2T) | "**nearly a factor of five**" ($0.45T–$2.2T) |
| Ch7 — EITC rate | "phases out at **21 cents** per dollar for families with children" | "**~16 cents** for one child, 21 cents for two or more" (verified in PolicyEngine) |
| Ch9 — MCP | "launched **May 2025**… Anthropic, OpenAI, and **Mistral**" | "Anthropic open-sourced it **Nov 2024**; OpenAI **Mar 2025**, Google followed" |
| Ch10 — April raise | "In **March 2025**, April raised $38M" | "In **July 2025**" (announced July 23, 2025) |
| Ch10 — EITC threshold | childless earned-income amount "**$7,840** for 2024" | "**$8,260**" ($7,840 is the 2023 figure; verified in PolicyEngine) |

### Worked examples re-derived against PolicyEngine

- **Ch7 benefit-cliff example.** The flagship NY single-parent-with-a-disabled-child case
  was used to claim a "$45,000 cliff" where the parent "may have less disposable income than
  the parent who earns $20,000." Running the actual household, **net income rises
  monotonically** — there is no $45k cliff and no reversal. What the household *does* face is
  a very high marginal rate (~80%) in the band around $25–30k. Rewrote the passage to describe
  that accurately, and kept the "true cliff" concept where it belongs (program-specific
  thresholds like childcare or Medicaid, where net income genuinely falls). Same fix applied to
  the introduction's Ohio example (the EITC was mischaracterized as "a cliff worth over $3,000"
  — the EITC phases out smoothly, it has no cliff).

- **Ch8 CTC distributional reasoning.** The text said making the CTC fully refundable most
  affects the **top decile** "because the reform extends refundability to higher-income
  households who previously hit the income tax floor" — mechanically backwards. Refundability
  by definition helps families whose credit exceeds their tax liability, i.e. **low- and
  moderate-income** families. The microsim confirms the largest shares gaining are in deciles
  2–4. Rewrote the reasoning in both places it appeared (Ch8 opening and the distributional
  section).

### Overselling / neutrality (author builds many of the tools described)

- Ch5 "We had become **the integrator**" → "We were positioning PolicyEngine as… an integrator."
- Ch5 "an outside tool demonstrating **comparable accuracy** … could **match** the government's
  internal estimates" → "good enough for the Treasury to pilot … could **even partly reproduce**"
  (the cited HMT evidence is 60% of NI calcs within 0.5%, income-tax validation inconclusive).
- Ch5 uncited *Times* direct quote → reported speech (no bare uncited quote). **If you have the
  article, re-add it as a direct quote with a `[@...]` key.**
- Ch5 "government **ministries** piloting our models" → "HM Treasury" (one ministry).
- Ch7 "makes microsimulation **self-correcting** in a way that aggregate models never are" →
  "an informal supplement to systematic validation, not a substitute for it."
- Ch7/Ch5 MyFriendBen "over 90 percent accuracy" → "matched expected amounts more than 90% of the
  time — a self-reported figure, not an independent audit"; "$1,500/month" reframed from "benefits"
  to "benefits they appeared eligible for but hadn't claimed" (matches the source).
- Ch10 Axiom present tense ("the foundation **maintains** Atlas… **builds** AutoRAC…
  encodings… **are maintained**") → "**is building**…", consistent with the chapter's own "both
  organizations are early" admission. "Cuts encoding time roughly in half" → qualitative (no cite).
- Ch2 "a small **priesthood** of government economists" → "a small circle of specialists."
- Ch4 "the supply-side **fantasy**" → "the supply-side **prediction**."
- Ch2/Ch4 "the anomalous 2022 **pandemic spike**" → "2022 surge, driven by capital gains and
  inflation" (the 2022 revenue surge wasn't a pandemic effect).

### Structure / naming (rename + migration cleanup)

- Part names aligned to the canonical `_quarto.yml`: **Part I: Origins** (thesis said "History"),
  **Part III: Research Directions** (thesis/intro said "Future").
- Intro roadmap: "Chapter 3 covers the **European tradition**" → "follows the open-source
  revolution" (Ch3 is transatlantic — France's OpenFisca *and* the US projects).
- PolicyEngine contributor count harmonized to "**more than 100**" (verified: 132 in
  policyengine-us alone, 262 across the main repos) — intro said "over fifty," Ch10 said "50+."
- Ch15 ending: cut the product-launch title-drop ("Welcome to society in silico") and the
  staccato fragments for a single understated close. **Stylistic — revert if you prefer the
  title-drop.**
- README and `.claude/CLAUDE.md`: "Cosilico" → "Axiom"; the CLAUDE.md also still documented the
  old MyST `{cite}` citation format and "early outlining" status — updated to Quarto `[@key]` and
  "full draft, in revision."

---

## Flagged — needs your decision (not changed)

1. **CTC full-refundability cost: $2B (Ch8) vs $12B (Ch11).** Same described reform, 6× apart.
   This is a real contradiction, but the right number depends on the *exact* reform you mean:
   removing only the refundable cap vs. removing the cap **and** the earnings phase-in give very
   different costs. A microsim here (`fully_refundable=True`, removing both, 2024, Enhanced CPS)
   came in around **$24–25B**, matching neither chapter. Decide the precise reform, score it once,
   and use that figure (and its poverty effect) consistently in both chapters. *I fixed the
   distributional reasoning but left both dollar figures as you wrote them.*

2. **Chapter-10 filename** is still `10-cosilico-infrastructure-for-the-future.md` (content is all
   Axiom). Renaming it to `10-infrastructure-for-the-future.md` would also touch `_quarto.yml:26`
   and the website slug map in `website/src/pages/book/[slug].astro` — which is part of your
   in-progress website changes, so I left it to avoid a conflict.

3. **Stray "Cosilico" in internal docs** (not reader-facing): `outline.md` (a stale 10-chapter
   outline that no longer matches the book — consider deleting), `manuscript/00-outline.md`
   (`[[cosilico]]` wiki-links), and the `agents/`+`skills/` tooling. Quick scrub when convenient.

4. **`"within 0.5%" of CBO's 2018 projections`** (Ch2 and Ch4, cited to CRFB) — two reviewers
   flagged the tolerance as suspiciously tight. Worth confirming against the CRFB piece; soften to
   "tracked CBO's projections closely" if it isn't load-bearing.

5. **Part III literature gaps** (the prior review's #3, still partly open). The chapters now engage
   Santarsuk/Bisbee on silicon-sampling bias and Sen/Rawls on adaptive preferences — but two
   one-paragraph additions would close the most visible holes and *strengthen* the argument:
   naming **Coherent Extrapolated Volition** (Ch14's "what humanity would want on reflection" *is*
   CEV restated empirically) and **Goodhart's Law** (a value forecast that steers AI becomes a
   target that gets gamed). Draft text for both is in the per-agent notes if you want it.

---

## Strengths to preserve (don't edit these)

- The four "note to readers" speculation banners (Ch10, 12, 13, 14) and Ch14's
  Proven/Preliminary/Theoretical validation tiers.
- Ch8 "The Neutrality Challenge" — "PolicyEngine doesn't tell you which outcomes to prefer; it
  tells you what the outcomes are," plus the admission that choosing what to display is itself
  normative.
- The volunteered 33% revenue gap (Ch5/Ch8) and "where PolicyEngine is most reliable / where
  caution is warranted."
- Ch4's framing of cross-model disagreement as "judgment, not failure," and the
  random-walk-beats-CBO finding presented against interest.
- The Westworld/Rehoboam open→close bookend; the introduction's "AI can't do your taxes" hook.

---

## Lower-priority polish (a future copyedit pass)

- Recurring motifs that have started to wear: "make the invisible visible" (~7× in Ch7 alone),
  "we became infrastructure," the benefit-cliff metaphor, "deterministic backends / AI frontends."
  Ration to the highest-leverage moments.
- Heading case is mixed (Title Case in most chapters, sentence case in Ch10/12/13). Pick one;
  the house style (and Max's global preference) is sentence case.
- The "model the people" mantra repeats 4× in Ch1; the "averages → distributions" point 4×.
- One **financial**-COI disclosure for Axiom Labs (the book argues for a market the commercial
  layer intends to enter; the disclosure currently covers "I built these tools" but not a stake
  in the commercial entity).

*All findings, with file:line detail, are in the per-chapter agent notes from this review run.*

---

## Update — Axiom / Brier reframe (same day)

Per the author: **Cosilico is dead; the current structure is two open public-good institutions** —
**Axiom** ("the rules — computable law for all": RuleSpec, Encoder, corpus, microsimulation) and the
**Brier Institute** (fka Farness; "the forecasts — open, agentic predictions": Brier-1, the
calibration-native prediction agent, and the open, continuously-scored Brier Almanac). They map
onto the book's own spine — *deterministic backends / AI frontends* and *legal confidence /
household-and-future uncertainty* — and share a substrate of calibrated synthetic populations.

Applied across the manuscript:
- **Dropped "Axiom Labs" everywhere** (thesis, preface, Ch10, Ch14, Ch15) — it's no longer the name,
  and the commercial/open-core/"is this a business" framing came out with it. Both pillars are
  public goods.
- **Ch10 reframed from commercial to public good:** the "two organizations (Foundation + Labs)"
  structure is now one nonprofit Foundation; the open-core/Red Hat/PostgreSQL section became
  "Governing a public good"; "The market question / is this a real business" became "Is the need
  real?"; the commercial tax-tech players (Avalara, April, Column Tax) are now framed as the closed
  contrast that motivates an open public layer, not a market to capture.
- **Brier Institute named as the forecasting pillar** in Ch14's "connection back" (replacing
  "Axiom Labs provides the integration layer") and in Ch15's conclusion ("its counterpart, the
  Brier Institute"), with Brier-1 and the Brier Almanac as the concrete products.
- The earlier **financial-COI flag for Axiom Labs is now moot** — both institutions are public
  goods, so there's no commercial venture to disclose a stake in.

Still open: the chapter-10 *filename* (`10-cosilico-…`) and the website slug map
(`book/[slug].astro` maps `cosilico → "Axiom Labs"`, now doubly stale) — both entangled with the
in-progress website work; and the internal planning docs (`00-outline.md`, `research/`) still say
Cosilico/Farness/Axiom Labs. Book prose and `_quarto.yml`-driven build are clean and render
without errors.

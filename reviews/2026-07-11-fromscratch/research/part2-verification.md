# Part II verification — PolicyEngine-era fact set

Primary-source verification of the claims in `manuscript/part-2-open-engine/` (ch 5
"Proof of concept", ch 6 "The household and the society", ch 7 "The three
ingredients") plus the UK/US policy examples. Research date: 2026-07-11.

**Verdict tallies:** 32 CONFIRMED · 8 CORRECTED (values below) · 9 UNVERIFIED/open.
New BibTeX in `part2-new-sources.bib` (16 primary sources).

Method: gov.uk, IRS/Census/BLS, NSF award record + API, NBER, PolicyEngine's own
blog/research posts (primary for their milestones), UBI Center reports, and the
GitHub API. The Times article and any paywalled/blocked host could not be fetched
(noted under UNVERIFIED).

---

## CORRECTIONS (lead with these)

### C1 — NSF POSE grant is **2025, not 2024** (ch 5) ★ most important
Manuscript: "In 2024 the National Science Foundation awarded PolicyEngine a
Pathways to Enable Open-Source Ecosystems grant … That year we finally closed the
gap … in April 2024, PolicyEngine launched income tax modeling for all fifty
states and DC."
- **The NSF POSE award is FY2025.** NSF award **#2518372**, title *"POSE: Phase I:
  PolicyEngine — Advancing Public Policy Analysis,"* awardee **PSL Foundation**, PI
  **Max Ghenis**, **award date 15 August 2025**, start 1 September 2025, expiry
  31 August 2026, amount **$299,974** (the "$300,000" is the rounded figure).
  PolicyEngine's own announcement is dated **18 August 2025**.
- Fix: change "In 2024" → "In 2025" for the NSF grant, and **decouple it from the
  April 2024 50-state launch** (two different years now sit in one sentence). The
  50-state launch remains a 2024 event (see U-note below); the grant is 2025.
- Sources: NSF award #2518372 (award record + api.nsf.gov); PolicyEngine blog
  `nsf-pose-phase-1-grant`.

### C2 — HM Treasury ATRS was published **17 December 2024, not "March 2025"** (ch 5)
Manuscript: "In March 2025, HM Treasury published an Algorithmic Transparency
Record…"
- The gov.uk record itself states **"Published 17 December 2024."**
- Fix: "In December 2024, HM Treasury published…" (The existing citation key
  `hmt2025policyengine` also carries `year = {2025}` — change to 2024.)
- Source: gov.uk `hmt-modelling-policy-engine`.

### C3 — National Insurance accuracy wording (ch 5)
Manuscript: "60 percent of National Insurance calculations fell within 0.5 percent
of its internal model."
- The ATRS actually says: **"NI calculations proved to be very accurate, with
  almost 60% of datapoints falling within 0.5% of one another."**
- Two refinements: it is **"almost 60%"** (not a round 60%), and the comparison is
  **agreement between the two models' datapoints** ("of one another"), which the
  manuscript's "within 0.5 percent of its internal model" paraphrases acceptably.
  Recommend "almost 60 percent … within 0.5 percent of the government's own model."
- Source: gov.uk ATRS.

### C4 — Mini-budget top-decile gain: **£2,738 (2.5%)**, not "about £2,500" (ch 6)
Manuscript: "the top decile gaining about £2,500 a year while the bottom gained
almost nothing."
- PolicyEngine's own same-day post (*Tax cuts in Prime Minister Truss's Growth Plan
  2022*, 23 Sep 2022): the Growth Plan **"raises the top income decile's net income
  by an average of £2,738 (2.5%) and that of the bottom decile by £45 (0.4%)."**
  Also: Gini +1.2%, top-10% share +1.0%, top-1% share +2.2%.
- Fix: "about £2,700" / "nearly £2,750." ("bottom gained almost nothing" = £45 ✓.)
  This is also the primary source that resolves the same-day-analysis beat (the post
  is dated the day of the mini-budget).
- Source: PolicyEngine blog `tax-cuts-in-prime-minister-trusss-growth-plan-2022`.

### C5 — CPS ASEC "roughly 100,000 households" is high (ch 6)
Manuscript: "its Annual Social and Economic Supplement … reaches roughly 100,000";
and later "each of the roughly 100,000 records."
- The **monthly CPS ~60,000 is correct.** But the current **ASEC sample is ~75,000–
  90,000 households** (Census describes it as "more than 75,000"; ~89k addresses in
  recent years). "Roughly 100,000" reflects the pre-2014/expanded-sample era.
- Two clean fixes: (a) change the ASEC figure to "roughly 90,000" (or "75,000 to
  90,000"); (b) the *second* "roughly 100,000 records" can legitimately stand if it
  refers to **PolicyEngine's enhanced dataset record count** rather than the raw
  ASEC sample — but then say so, because as written both numbers read as the survey.
- Source: Census CPS-ASEC methodology.

### C6 — Enhanced CPS "five datasets / 9,168 targets / 8.3%→0.2%" is **unverified in public sources**, and the citation year is wrong (ch 5, 6, 7)
Manuscript (ch 7): "fused five datasets … then calibrated the result to 9,168
administrative targets, cutting the average deviation from those totals from 8.3
percent to 0.2 percent [@policyengine2022enhanced]." (Ch 5/6 carry the 97% version.)
- The cited key **`policyengine2022enhanced` is a December 2022 blog post** that
  predates these figures and does not contain them (this is the `[VERIFY: citation
  key year mismatch]` the draft already flags — confirmed real).
- No public PolicyEngine source I could find states "five datasets / 9,168 targets /
  8.3%→0.2%." The closest public artifacts describe **different, smaller numbers**:
  the beta post (`enhanced-cps-beta`, 25 Mar 2024) = **3 sources, ~90 targets**;
  the `policyengine-us-data` docs = **2 datasets (CPS + IRS PUF), 2,813 targets.**
- Action for author: this is an internal/August-2025 (populace-era) figure. Point
  the citation at the **actual August 2025 release notes / populace or
  policyengine-us-data changelog** that documents 9,168 targets and the 8.3%→0.2%
  reduction, or soften to the publicly documented numbers. Do **not** leave it on
  the 2022 key. (The "five datasets" named in ch 7 — CPS, SCF, Consumer Expenditure,
  RECS, ATUS — are plausible but I could not confirm them in one published place.)

### C7 — TAXSIM paper count: keep 1,200, but note PolicyEngine's own inconsistency (ch 5)
Manuscript: "more than 1,200 papers had relied on it."
- **Supported.** PolicyEngine–NBER MOU post (5 Sep 2025): **"Over 1,200 papers have
  applied TAXSIM, based on citations of the Feenberg and Coutts (1993) paper."**
- Caveat: PolicyEngine's *NSF POSE* post (18 Aug 2025) says **"over 1,100."** Cite
  the MOU post (the 1,200 source) and be aware of the internal 1,100/1,200 drift.
- Source: PolicyEngine `policyengine-nber-mou-taxsim`.

### C8 — Washington WFTC "12–24% marginal rate" not found in Part II; docs say ~12–18%
The "12–24%" WFTC claim is **not present** in ch 5–7 (grep-checked). If it appears
elsewhere in the book, note that PolicyEngine's WA WFTC documentation describes the
phase-out as producing **marginal rates ~12–18%** (childless phase-out = 18% per
additional dollar), not up to 24%. Flag for the author to locate and reconcile.
- Source: PolicyEngine WA WFTC docs.

---

## CONFIRMED

### PolicyEngine history (ch 5)
- **UK launch — September 2021.** UBI Center *Introducing PolicyEngine UK*,
  **published 1 September 2021**; "developed OpenFisca UK, the UK's first open source
  tax and benefit microsimulation model … four reports and three conference
  presentations." ✓ (`ubicenter2021policyengine`, already in refs.)
- **OpenFisca UK built from late 2020.** GitHub repo (now `policyengine-uk`) created
  **5 Aug 2020** — consistent with "By late 2020 … a working model." ✓
- **UBI Center founded 2019.** *Introducing the UBI Center*, 24 June 2019. ✓
  (`ubicenter2019intro`.)
- **PSL membership.** microdf, policyengine-uk, and policyengine-us all appear in the
  Policy Simulation Library catalog; PolicyEngine joined PSL (PSL 2021 year-in-review
  blog). ✓
- **Tax-Calculator v3.2.1 — August 2021.** GitHub release tag `3.2.1` published
  **6 Aug 2021** (title "3.2.1 (2021-08-06)"). ✓ Resolves the `[NEEDS CITATION:
  Tax-Calculator v3.2.1 release date]` marker.
- **">100 open-source contributors."** GitHub API: `policyengine-us` alone has
  **~141 contributors** (contributors endpoint last page = 141 at per_page=1,
  anon=true). ✓ Resolves the `[NEEDS CITATION: contributor count]` marker.
- **US 50-state income tax coverage — 2024.** PolicyEngine US 2024 year-in-review
  (29 Dec 2024): "We introduced comprehensive state income tax models for all 50
  states and DC." ✓ (year confirmed; see U-note on the specific "April" month.)
- **HM Treasury ATRS content:** income tax "less promising … likely due to
  difficulty in finding appropriate variables to compare" ✓ (matches "the two
  systems had trouble even identifying which variables corresponded"); ML approach =
  multi-year FRS + random-forest imputation + gradient-descent reweighting ✓;
  "not currently deployed" ✓.
- **NBER MOU — September 2025.** `policyengine-nber-mou-taxsim`, **5 Sep 2025**;
  TAXSIM "gold standard … since the 1970s," emulator to preserve researcher access,
  Feenberg as NBER IT Director / external POSE mentor. ✓
- **Atlanta Fed / Policy Rules Database MOU — 2025.** `policyengine-atlanta-fed-mou-
  prd`; PRD covers "SNAP, Medicaid, housing vouchers, and child care subsidies" plus
  taxes/EITC/CTC, powers the CLIFF tools. ✓ (Enrichment: PRD is co-developed with
  the **National Center for Children in Poverty**, not the Atlanta Fed alone.)
- **Nikhil Woodruff at No 10.** `policyengine-10-downing-street`: since **summer
  2025** he served as an **"Innovation Fellow with 10DS"** (No 10 data science team)
  for ~six months, building a package called **`10ds-microsim`** on PolicyEngine that
  was "intensively validated against external projections and official forecasts."
  ✓ Resolves the `[VERIFY with Nikhil: role wording]` marker — precise wording is
  "Innovation Fellow with 10DS," not a permanent government post.

### UBI Center reports (ch 5 examples)
- **Freedom Dividend (Yang), 24 June 2019.** "$12,000 per year to all 236 million
  adult citizens is $2.8 trillion"; "The new tax revenue raises $1.2 trillion,
  leaving the total unfunded cost at $1.4 trillion"; poverty **−74% (7.3%→1.9%)**;
  child poverty −54% (7.9%→3.6%). ✓ All of "$2.8T cost vs $1.2T raised, 74% poverty
  cut" confirmed exactly.
- **UK carbon dividend, 23 Apr 2022.** "£100 per tonne carbon dividend … cut poverty
  by 14%"; bottom decile +6.2%, top decile −2.1%, Gini −3.4%. ✓ Poverty −14%
  confirmed. Deep-child-poverty **−33%** is the source's own summary (search
  corroborated; the figure lives in the page's charts, not cleanly isolated in
  fetched prose — treat as source-reported). Companion **US** page: $100/ton →
  poverty −10%, deep child poverty −27%.

### US policy examples (ch 6)
- **2021 ARP Child Tax Credit.** SPM child poverty **9.7% (2020) → 5.2% (2021)**,
  record low; CTC "lifted **5.3 million people — including 2.9 million children** —
  out of poverty in 2021"; "the **expansion … alone lifted 2.1 million children**."
  ✓ All three of the book's figures (2.9M / 2.1M / 9.7→5.2) confirmed. (Census
  SEHSD-WP-2022-24 + "Child Poverty Fell to Record Low 5.2%" story.)
- **EITC phase-out rates.** One child **15.98%**, two-or-more **21.06%** (IRS Rev.
  Proc. 2024-40 / TPC EITC parameters). ✓ Confirms both ch 6 ("~sixteen … twenty-one
  cents") and the ch 5 transposition anecdote ("21.06 percent" is the real two-child
  rate).
- **SNAP ~30% benefit reduction rate** ✓ (SNAP reduces the max allotment by 30% of
  net income — the statutory net-income contribution rate).
- **SSI ~50% earned-income offset** ✓ (SSI reduces the payment by roughly $1 per $2
  of earned income after the general/earned-income disregards).
- **SPM threshold, two adults + two children, renters, 2024 ≈ $39,430** ✓ (BLS 2024
  research SPM thresholds; `bls2024spm`). "About $39,400" is right; vintage 2024 ✓.
- **Census official SPM 2022 = 12.4%** (up from 7.8% in 2021) ✓ — relevant to the
  ch 6 `[VERIFY]` on PolicyEngine's 9.6%: the gap to the official ~12.4% is real, so
  keep the marker and pin the PolicyEngine estimate's data vintage.

### Foundations (ch 6, 7)
- **Pechman & Okner (1974), MERGE file, 72,000 households.** ✓ "a representative
  sample of 72,000 American families" (1966 income/tax data; SEO × IRS merge; MERGE
  file documented in Appendix A of *Who Bears the Tax Burden?*). "Essentially
  proportional for the vast majority of families" ✓. (`pechman1974taxburden`.)
- **Neisser (2021) ETI meta-regression.** ✓ "**61 studies containing 1,720
  estimates**"; mean ETI ≈ 0.30 (Economic Journal 131(640):3365–3391). Matches ch 7
  exactly. (`neisser2021eti`.)
- **CPS monthly ~60,000 households** ✓ (`census2024cps`).

### MyFriendBen (ch 6)
- Launched on PolicyEngine's API in **Colorado, North Carolina, New York, and
  Illinois** (Illinois = the 4th state, per the Illinois Benefit Hub post) ✓;
  **12 languages** ✓; **~6 minutes** ✓; **">90% accuracy"** (self-reported) ✓;
  **Colorado: ~$1,500/month** in benefits surfaced ✓. All confirmed.
  (`myfriendben-nc` Apr 2025; `illinois-benefit-hub`; `myfriendben2025pueblo`.)

### UK example (ch 6)
- **UC taper cut 63% → 55%**, Autumn Budget 2021 (Sunak), effective 1 Dec 2021,
  plus a **£500/yr work-allowance increase.** ✓ PolicyEngine's own analysis exists:
  *Analysing Autumn Budget Universal Credit reforms with PolicyEngine* (Nikhil
  Woodruff): cost **£2.8bn/yr**, poverty **−3.1%**, benefits 12% of the population;
  MTRs fall 5.4–63pp for those between the work allowance and UC entitlement, rise
  37.4pp for those previously above UC. ✓ (`analysing-autumn-budget-universal-
  credit-reforms`.)

---

## UNVERIFIED / open

- **The Times quote (ch 5).** "The Times reported that the tool could more
  accurately predict the outcomes of ministers' decisions and was expected to be
  used mainly in budget periods." **Could not verify** — thetimes.co.uk is blocked
  to the research crawler, and the claim is **cited to `hmt2025policyengine` (the
  gov.uk ATRS), which is not The Times** — a citation mismatch. Action: obtain the
  Times article's date/headline/author and add a distinct key, **or** re-attribute
  the paraphrase to the ATRS (whose "not currently deployed / experimental,
  supplementary, budget-period" framing supports the substance).
- **UC taper "£1,000/yr for a single parent at 25 hrs/wk minimum wage" (ch 6).** Not
  in PolicyEngine's UC-taper post. Nearest official comparator is HM Treasury / House
  of Commons Library "**~£1,200/yr for a single parent of two on the NMW**" — but a
  different household spec (and it bundles the £500 work-allowance rise). Treat as a
  PolicyEngine household calculation to **recompute and cite**, or soften.
- **UC taper "share facing >70% MTR fell from 26% to 9%" (ch 6).** Not found in the
  PolicyEngine post (which reports MTR *deltas*, not the >70% share). Recompute/cite.
- **2021 ARP CTC annual cost "~$105 billion" (ch 6).** Broadly consistent with
  JCT/Treasury estimates (~$100–110B for the one-year expansion) but no single
  primary pinned this session. Add a JCT or Treasury cite.
- **Enhanced CPS 9,168 / five datasets / 8.3%→0.2% / 97%** — see **C6**.
- **"April" 2024 for the 50-state launch (ch 5).** The year (2024) is confirmed by
  the year-in-review; the specific **month** is not stated there — pin "April" to a
  launch-specific post or soften to "in 2024."
- **"Revenue runs about a third below official" (ch 5, 6).** Author/internal claim;
  the ATRS confirms the *direction* (high-income under-sampling, benefit under-
  reporting) but not the one-third magnitude. Keep the ch 6 `[VERIFY]` marker.
- **US launch "March 2022" (ch 5).** Consistent with the cited 2022 year-in-review
  and not contradicted, but the exact month could not be re-pinned to a fresh primary
  post this session (the "Make Everyone a Policymaker" relaunch post sits on Medium,
  which blocks clean date extraction). Low risk; keep as-is or confirm at copyedit.
- **Atlanta Fed "a month later" (Oct 2025) + specific CLIFF users (Colorado
  Workforce Development Council, New Mexico Caregivers Coalition).** MOU confirmed as
  a 2025 event; the exact month and the two named user orgs were not re-verified —
  carries the existing `[VERIFY wording vs MOU at copyedit]` marker.

---

## Discoveries worth using (one or two per chapter)

- **Ch 5 — real, publicly documented bug flow to replace the `[VERIFY: real
  incident]` EITC transposition.** Two genuine, on-the-record examples exist in the
  fact sheet's oracle program: a **UKMOD savings-allowance interaction bug** filed
  publicly on the UKMOD-PUBLIC repo, and a **EUROMOD adapter batch-processing
  contamination bug** (identical cases scored differently by batch position) root-
  caused and reported upstream. Either is a documented "whose bug is it?" anecdote —
  and it's the stronger, trust-flip version (the *oracle* was wrong). The 21.60/21.06
  EITC story can stay as illustrative if labeled as such, but a real incident is
  available. (The 21.06% two-child rate itself is now verified via IRS.)
- **Ch 5 — the ATRS one-liner worth quoting.** *"NI calculations proved to be very
  accurate, with almost 60% of datapoints falling within 0.5% of one another."* Pair
  with the honest counterpart: *"Income tax calculations were less promising … due to
  difficulty in finding appropriate variables to compare."* Both are quotable gov.uk.
- **Ch 5 — mini-budget turnaround mechanics.** PolicyEngine's Growth Plan post is
  **date-stamped the day of the mini-budget (23 Sep 2022)** and its numbers "broadly
  resemble those from the IFS and the Resolution Foundation" — concrete evidence for
  "within hours … among the only independent estimates in the first days."
- **Ch 5 — Nikhil's exact role.** "**Innovation Fellow with 10DS**," ~six months from
  summer 2025, package **`10ds-microsim`** — replaces the vague `[VERIFY with Nikhil:
  role wording]` and is more accurate than "joined the UK government at 10 Downing
  Street" (it was a fellowship on the data-science team, clearly labeled experimental
  analysis).
- **Ch 6 — mini-budget exact figures** (£2,738 / £45 / Gini +1.2% / top-1% +2.2%)
  are sharper than "about £2,500," and PolicyEngine-reproducible.
- **Ch 7 — Neisser is exactly right** (1,720 / 61 / ≈0.30): safe to state without
  hedging.

---

## Citation-key actions (for references.bib)

- **Fix** `hmt2025policyengine`: `year = {2024}`, add `note`/`month` = December 2024
  (published 17 Dec 2024).
- **Fix** the Enhanced CPS citation off `policyengine2022enhanced` (2022) onto the
  real Aug-2025 source (see C6) — or add a new key for it.
- **Add** the 16 new keys in `part2-new-sources.bib` (NSF award + blog, NBER MOU,
  Atlanta Fed MOU, No 10 post, Growth Plan post, UC-taper post, two UBI Center
  reports, Tax-Calculator release, Illinois Benefit Hub, Census CTC working paper,
  Census SPM-2022 story, IRS/TPC EITC parameters, WA WFTC docs).

# Max's Keep notes — 2026-08-05 (decoded and dispositioned)

Second decode round, same pattern as [2026-07-21](2026-07-21-max-phone-notes.md).
The 8/5 dump repeats all eighteen 7/21 items (decoded then, fixes not yet applied)
plus ~25 new ones, so this round applied both sets. Every disposition below was
verified this session against primary sources, the policyengine/axiom repos, or
gh history before editing — evidence inline. Statuses: **FIXED** (commit),
**ALREADY ADDRESSED** (evidence), **NEEDS MAX** (specific question),
**COULDN'T DECODE/LOCATE**.

Commits this round: `7d51ff1` (August family architecture — the separate Job 1),
`ccba406` (repo-verified fix batch), `4c40c87` (web-verified corrections), plus
the notebook/data commit if the PE run lands. Decode confidence is HIGH unless
flagged.

---

1. **"40 to 50 percent of snap recipients - different from aggs could be response bias"**
   — FIXED (`ccba406`), ch 3. Added the mechanism split: an aggregate survey-vs-admin
   gap folds together denial, nonresponse, and misremembering; person-level linkage is
   what isolates the denial. `[NEEDS CITATION]` marker added to pin the recipient-level
   rates to the linked-records papers (Meyer & Mittag) rather than the
   aggregate-comparison paper the passage cites.

2. **"Vaseline different shops"** (= baseline) — ALREADY ADDRESSED. Ch 3 ("different
   shops assume different baselines — the assumed path of current law a reform is
   measured against") and ch 6's score-anatomy paragraph both carry the shop-plural
   treatment; both predate this round. No singular-baseline claim found.

3. **"Openfusca us young"** — FIXED (`ccba406`), ch 4. `openfisca-us` was created
   2021-06-23 (gh api; renamed policyengine-us 2022-10-13), so in the 2019 scene it
   could not have been "young and incomplete" — it did not exist. Text now says no US
   country package existed yet.

4. **"State tax"** — decode MEDIUM; the state-tax claims near the flagged chapters were
   all verified: six states by end-2022 CONFIRMED (repo tree at the last 2022 commit:
   MA/MD/NY/OR/PA/WA, matching PE's 2022 year-in-review), and the 50-state claim
   re-dated — encodings finished late 2023 (Mississippi, v0.466.0, 2026-09-14 →
   2023-09-14), nationwide **beta** launch April 15, 2024. FIXED in ch 5. If the note
   meant a different state-tax claim, NEEDS MAX for which one.

5. **"Freedom dividend I did myself"** — FIXED (`ccba406`/`4c40c87`), ch 4. Byline
   verified (ubicenter.org, `author: max`): "I ran the arithmetic all the way through
   myself." Also corrected the funding gap to the report's own figure: **$1.4T**
   unfunded (the draft said $1.6T; the post nets other offsets).

6. **"Should to to adults"** — ALREADY ADDRESSED / FIXED. The dividend already read
   "every American adult." The adjacent adults-vs-children sentence was verified: the
   analysis is Nate Golden's (byline confirmed), and his actual finding is
   budget-dependent — child allowance wins up to ~$500B/year, universal wins past it —
   which the text now says instead of the unconditional "child allowances cut poverty
   most."

7. **"Matt jensen pointed to openfusca nikhil choose"** — FIXED (`ccba406`), ch 4:
   "Matt Jensen … pointed us to OpenFisca, and Nikhil made the call to build on it,"
   placed at the openfisca-uk build decision.

8. **"Microdf"** — FIXED (`ccba406`), ch 4. Origin verified: repo created 2018-06-15
   by Max as **taxcalc-helpers** (initial README: "Helper functions for
   Tax-Calculator"); the text now carries that origin. No documented microdf↔Blank
   Slate tie exists (searches: zero hits), and the timeline contradicts one
   (microdf 2018, Blank Slate 2021+) — the 7/21 decode guessed wrong there.

9. **"Blank slate uni"** (= Blank Slate UBI) — FIXED (`ccba406`), ch 4. Added as the
   UBI Center's house genre: UK piece 2021 (authors max/nikhil/deepak/charles), US
   version carried by Nikhil (UBICenter/blank-slate-ubi-us, 41/41 commits his,
   presented at the 2022 BIG conference). `[NEEDS CITATION]` marker for the bib
   entries.

10. **"Tax data"** — ALREADY ACCURATE, one open naming question. Ch 7's claim
    (matches CPS records to IRS PUF data for Tax-Calculator's microdata) is what
    taxdata does. The book styles it "Tax-Data"; the repo is `PSLmodels/taxdata`.
    NEEDS MAX (trivial): keep the styled form or switch to the repo name.

11. **"Tax brain app"** — FIXED (`ccba406`), ch 2. TaxBrain added: OSPC's browser app
    over Tax-Calculator (move federal parameters, watch revenue/distribution
    recompute), framed as the first crack at the last-mile problem, with ch 2's
    "everything demanded a programmer" line reconciled (TaxBrain the exception that
    proved it — federal parameters only, no benefits/states/own-household).

12. **"UCL Durham"** — FIXED (`4c40c87`), ch 5. **Durham University, computer
    science** (LinkedIn/RocketReach bio data; Durham student-paper profile "third-year
    Computer Science student at Durham, on a year out to co-found PolicyEngine").
    UCL appears nowhere in sources; also dropped "mathematics and".

13. **"Mit"** + 14. **"Capstone"** — FIXED (`4c40c87`), ch 4. The blended master's
    closes with "a capstone … in lieu of a master's thesis" (MIT DEDP program page),
    and third-party bios confirm Max holds the degree; text now says the coursework
    was laddered into the blended master's, capstone rather than thesis. NEEDS MAX
    (optional): name the capstone project if you want it in the book.

15. **"C3"** — FIXED (`4c40c87`), ch 5. PolicyEngine is a **fiscally sponsored
    project of the PSL Foundation** (policyengine.org/us/donate: "Donate securely
    through our fiscal sponsor, the PSL Foundation"; NSF award recipient = PSL
    FOUNDATION; PSL Foundation EIN 86-3092437). The "Incorporating as a 501(c)(3)"
    sentence replaced; the trust argument kept.

16. **"Democracy lab"** — FIXED (`4c40c87`), ch 5. DemocracyLab verified (project
    #1043, owned by Max, live volunteer listings); credited as the volunteer
    pipeline.

17. **"Net of applicable deductions"** — FIXED (`ccba406`), ch 5: reframed as the
    unlisted-set ambiguity, `[VERIFY: swap in a specific logged case]`. NEEDS MAX:
    a real case from the old discrepancy log would land this properly (the adjacent
    transposed-digit example still carries its own `[VERIFY: real incident]`).

18. **"Nsf award number"** — ALREADY ADDRESSED; re-verified via the NSF API this
    round (award 2518372, PSL FOUNDATION, 08/15/2025, $299,974, PI Max Ghenis).
    Ch 5 has carried the number since the from-scratch rewrite.

19. **"Nikhil still innovation fellow"** — FIXED (`ccba406`), ch 4 footnote: present
    tense, fixed six-month duration dropped ("As of this writing … an Innovation
    Fellow with 10DS"). `[VERIFY with Nikhil: role wording]` stays (also a
    publication-checklist item).

20. **"Given up on improving on"** — COULDN'T LOCATE. The phrase (and near
    variants) does not appear in the current manuscript; likely eliminated by the
    from-scratch rewrite. If it survives in an export you read, NEEDS MAX for the
    chapter.

21. **"80% more than double hedge fund - state local tax niit"** — FIXED
    (`ccba406`), RECOMPUTED 2026-09-07 (item 33). Chapter 6 now specifies both
    households and earnings increments. The NC parent gives up 92.7% of a
    $38,000→$39,000 raise; the NYC long-term capital-gains comparison is 23.8%
    federal plus 14.78% state/city, or 38.6% combined. These are illustrative
    households, not population averages. The previous ~80%/~67% prose is replaced
    by the checked notebook calculation.

22. **"Asset tests estimates"** — FIXED (`ccba406`), ch 6. Verified in code: SNAP
    and SSI asset/resource tests are encoded (parameters + `meets_snap_asset_test`,
    `is_ssi_eligible`), and since Feb 2026 the enhanced CPS carries SIPP-imputed
    bank/stock/bond assets (present and nonzero in `enhanced_cps_2024.h5`), so
    population runs exercise the tests. Removed "asset tests" from the list of
    things "no rules engine sees" (an asset test is a rule; what was missing was
    asset data) and added the SIPP-imputation sentence.

23. **"Unattainable - axiom?"** — FIXED (`ccba406`), ch 6. Split the claim: matching
    rules-as-written is a closable gap (Part III's statutory exactness), matching
    determinations-as-made is not (discretion, documentation, local practice).
    "Perfect accuracy is unattainable" no longer contradicts Part III.

24. **"Myfriendben 2025"** — FIXED (`4c40c87`), ch 6. Colorado launch was **2023**
    (Gary Community Ventures), expansion through 2025 (NC April, IL October).
    NEEDS MAX: PE's own Illinois post calls **New York** the third state, but
    MyFriendBen's materials list CO/IL/MA/NC/TX/WA and no NY announcement was
    found — the book now names only NC and IL ("among them"); confirm whether NY
    actually launched. The $1,500/month figure re-scoped to its source (40,000+
    Coloradans statewide, not Pueblo).

25. **"Self reported"** — ALREADY ADDRESSED (the self-reported flag on the >90%
    figure predates this round); wording tightened to the sources' actual claims
    ("the operators' own figure").

26. **"Tax cut nudging to phase out"** — FIXED (`ccba406`), ch 6. A cut cannot nudge
    a family into a phase-out (it doesn't move income); the mechanism is that the
    new benefit phases out across the family's income range, and a withdrawal rate
    is a marginal rate. Rewritten to say that.

27. **"Sspm threshold varies by locally"** — FIXED (`ccba406`), ch 6: "$39,400
    **nationally**, before the local housing adjustment moves it up or down for the
    place a family actually lives." (BLS 2024 2A2C renter threshold $39,430.)

28. **"Wic gender neutral"** — FIXED (`4c40c87`), ch 6. The old line ("looks
    gender-neutral on its face") was unsupported and backwards — WIC's face is its
    name. Reframed per the cited PE post: sex-targeted eligibility, with household
    pooling explaining the nearly even adult split (−0.9% women vs −0.7% men; child
    −2.6%).

29. **"Revenue a third too low - no we also use the puf"** — FIXED (`7d51ff1`),
    ch 6 (and ch 5's forward-promise). The CPS-only "roughly a third" era framing
    replaced: the enhanced dataset imputes PUF tax detail (QRF, per the us-data
    docs) and calibrates to bracket-level IRS totals; residual caution re-scoped to
    statics, conventions, and un-targeted questions. `[VERIFY]` marker asks for the
    current computed gap at publication. Related flag: the public us-data docs say
    **2,813** calibration targets; ch 6 says 9,168 (author-internal, already behind
    its own `[VERIFY]`) — reconcile at citation pass.

30. **"Arpa CTC more consequentlally"** — FIXED (`ccba406`), ch 6: "more
    consequentially **for poverty**" (refundability drove the poverty effect; the
    raise drove much of the cost).

31. **"9.7 and 5.2 repeated and do the pct reduction"** — FIXED (`ccba406`), chs 3+6.
    Ch 6 now carries "a 46 percent drop" (Census's own characterization: "declining
    46% from 9.7% in 2020 to 5.2%"); ch 3's repeat lightened to "cut nearly in
    half … chapter 6 walks through the numbers."

32. **"Mechanical also true because asec calculates tax credits…matches Columbia"**
    — FIXED (`ccba406`/`4c40c87`), ch 6. Added, with the SPM technical
    documentation cited directly ("The CPS ASEC does not collect information on
    taxes paid, but instead relies on a tax calculator to simulate taxes paid"):
    the measured drop and Columbia's projection both rest on modeled credits, so
    the close numerical match is partly two calculators agreeing. Also swapped the
    mis-pointed Columbia citation to the actual pre-enactment fact sheet
    (March 2021, −56%) and resolved ch 3's ex-ante marker with the CTC-alone
    40–45% roundup figure, and the $105B cost to the JCT figure via CRS R46839.

33. **"Numbers that can come straight from pe we should calculate, maybe link a
    ipynb"** — CALCULATIONS VERIFIED (2026-09-07); final book checks pending.
    `scripts/notebooks/pe-computed-numbers.ipynb` executes all four code cells
    using managed PolicyEngine 5.3.0 / US 1.764.6, with saved outputs and exact
    environment pins. The specified NC family's $38,000→$39,000 raise leaves
    $73 (92.7% withdrawn); the NYC long-term-gains comparison is 38.6%.
    Explicit parental roles and no SSI spouse replace the under-specified old
    curve. CTC receipt at $15,000 is $1,875→$4,400 with full refundability in
    2026; historical 2020/2021/2022 credits are $1,875/$7,200/$1,875.
    The locally cached, hash-verified certified Microcosm Build P national run
    uses MicroSeries/map_to: $20.87bn net fiscal cost, child SPM poverty
    17.02%→15.12%, 1.48m fewer children in poverty. Fiscal accounting includes
    the model's health-cost interaction. Chapters 6 and 13 now use this score
    and identify its vintage; the uncomputed uncertainty-band claims are
    removed. Chapter 6 links the notebook; receipts and figures are saved in
    `scripts/results/pe-computed-numbers/`. These static results do not recreate
    the older dense Enhanced CPS score or estimate behavioral uncertainty.

34. **"Taxsin doesn't answer all three questions"** — FIXED (`ccba406`), ch 7:
    TAXSIM scoped to the rules question only, "by design … which is precisely what
    let four decades of effort concentrate on getting the rules right."

35. **"Second architecture mention openfusca"** — FIXED (`ccba406`), ch 7: the
    code-native architecture is "the approach OpenFisca pioneered … PolicyEngine's
    engine descends directly from OpenFisca's."

36. **"Taxsin it's tax return validation"** — FIXED (`4c40c87`), chs 3+7, with a
    nuance from Feenberg & Coutts (1993): TAXSIM is built on large SOI samples of
    **actual returns that carry the tax actually owed** — reality beside every
    computation — but the paper describes construction, not a formal validation
    exercise (and records Ladd's state-aggregates criticism). Both passages now say
    the supportable version.

37. **"Penalty for moving weights - we don't always do that"** — FIXED (`ccba406`),
    ch 7. Verified in code (microcalibrate `metrics.py`/`reweight.py`, us-data
    `enhanced_cps.py`, L0 `calibration.py`): the loss is squared relative error to
    targets, **no** stay-close-to-survey-weights penalty anywhere (one current
    pipeline even starts from uniform weights). Rewritten: textbook calibration
    penalizes weight movement; this machinery relies on target breadth, dropout
    during optimization, and holdout checks.

38. **"Used to live as one of scripts"** — ALREADY ADDRESSED: ch 7's "These stages
    used to live as one-off scripts inside each modeling team" — read as the
    location cue for note 37.

39. **"The methods are the point - avoid this writing style everywhere"** — FIXED
    (`ccba406`), global. The literal sentence (ch 7) removed; sweep applied to the
    family of narrator-verdict tics across chs 1, 2, 6, 7, 8, 9, 10, 13, 16, 17
    ("Pause on," "worth keeping/naming/pausing/restating," "deserves its own
    paragraph," "Notice, finally," "hold that … in mind," "that is the point").
    Content kept; scaffolding removed.

40. **"Contrast human review needs on benefits with tax administration"** — FIXED
    (`ccba406`/`4c40c87`), ch 9, beside the existing FNS merit-personnel passage:
    SNAP adjudicates first (merit-system caseworker behind every determination,
    7 CFR 272.4), the income tax self-assesses (machine processing, math-error
    authority, audit by exception — NTA 2026 mid-year report quoted and cited).
    Note for currency: USDA renamed FNS to the Food and Nutrition Administration
    effective June 2026; the book's "has held" phrasing names the issuing agency
    correctly, but check any present-tense FNS references at copyedit.

41. **"Effectiveness"** — FIXED (`ccba406`), ch 7 (decode MEDIUM: read as the vague
    word in "revenue, distribution, and effectiveness"): now "decide whether a
    reform accomplishes what it was written to do."

42. **"March 2023 AI explanation was about microsim household was later"** — FIXED
    (`ccba406`/`4c40c87`), ch 8. Verified from the posts: March 17, 2023 =
    reform-level ChatGPT prompt integration; the household "Explain with AI" button
    shipped **December 26, 2024** (Anthony Volk, Claude 3.5 Sonnet). Opening
    re-sequenced; bib entry corrected (author, date, canonical URL).

43. **"Pause on, detail worth keeping, avoid this style"** — FIXED (with 39);
    the flagged instances were ch 8's "Pause on" and "The detail worth keeping."

44. **"PolicyBench failure did this happen?"** — YES — CONFIRMED against the
    policybench repo record, and the passages now track it: commit `df473cb` +
    PR #110 + issue #107 (2026-07-07): **29 of 177** published Medicaid narratives
    described 65+ people as qualifying through the ACA adult expansion (a
    non-elderly pathway); one misled the automated failure audit into a false
    reference-suspect flag; the fix injected an authoritative-grounding block from
    engine facts and regenerated all 177 behind a category-specific
    forbidden-claims validator. Chs 8 and 10 updated to the record's numbers and
    mechanism. One precision note: the validator ran at regeneration time and is
    asserted in the commit/PR text, not a persistent committed file — current book
    wording is compatible with that.

45. **"Had no home was the whole but pe did"** — FIXED (`ccba406`), ch 9: the whole
    did exist (PolicyEngine, open and free, since Part II); what the market lacked
    was the whole **sold with a warranty** — which also sharpens the operator-tier
    argument later in the chapter.

46. **"Payment error rate: also zero above a level / Define payment error rate"**
    — FIXED (`ccba406`/`4c40c87`), ch 9. Defined (QC re-adjudication of sampled
    cases; overpayments + underpayments added, never netted) and the tolerance
    mechanism added: errors under $57/case (FY2025, indexed) don't count at all.
    Decode resolution: "zero" almost certainly refers to the tolerance — and the
    verified fact is sharper than either reading: the **House-passed** bill would
    have zeroed the tolerance (H.R.1 §10010), the **enacted** OBBBA dropped that
    provision (its QC section is §10105 cost-sharing), and FNS published the FY2026
    threshold ($58) post-enactment. The book now says exactly that.

47. **"Rulespec logic and parameters separate - not anymore all just concepts…"**
    — FIXED (`ccba406`), chs 7+9. Verified against axiom-rules-engine docs and the
    rulespec-us migration commits (2026-02-11/20, "unified syntax"): one YAML
    module per provision, a single `rules` list, each rule a named concept
    (number-valued or formula-valued) with dated versions; names are public
    fragments of durable legal IDs; separate parameter files affirmatively banned.
    The EITC two-kinds-of-change diff story survives, re-told on concepts. (Nuance
    preserved: records still carry kinds — parameter vs derived — the unification
    is the file/versioning envelope and the naming.)

48. **"Pipelines sharpest idea"** — KEPT AND SHARPENED (`ccba406`), ch 9: "The
    money-atom gate is the pipeline's sharpest idea," with the narrator framing
    ("deserves its own paragraph") removed per the style rule.

49. **"What does openness to forks actually buy? We ensure an accurate corpus.
    Really the ultimate check on capture?"** — FIXED (`ccba406`), ch 9. "The
    ultimate check on capture" slogan replaced with the mechanics: a fork
    disciplines nobody day to day (governance and contributor plurality do); what
    the license guarantees is exit, credible because the tests, oracle suites, and
    gates travel with the code; the protected asset is the accurate corpus, and the
    fork right is how the corpus survives its steward.

50. **"What's the not yet public graded simulation"** — ANSWER: the commercial
    operator entity in formation around graded-simulation-as-a-service is
    **Cosilico PBC** (per the fact sheet; the ch 9 and ch 12 HTML decision comments
    already gate whether to name it at publication). NEEDS MAX: that standing
    decision, plus whether the new applications-tier reserve name changes how the
    operator is described. Text left structural (unchanged).

51. **"Failed experiment 23/25 - was it wrong or just inconsistent…"** — FIXED
    (`ccba406`), chs 9+10, per the actual B1 record (rulespec-us#535 probe report,
    2026-07-05): 23 old-correct / 1 mixed / 1 identical; dominant failure =
    public-name instability (same statute, new decompositions, zero name overlap in
    the worst cases); a minority regressed outright (two empty stubs, one dropped
    deferral, one formula drift); and semantic equivalence of the renamed majority
    was **not adjudicated** (the PE oracle ran 0/25 — dark for the probe). The book
    now says exactly that, which is also your reading ("breaking provisions into
    different concepts").

52. **"Medicaid and aca didn't cancel randomly right? Like Medicaid mechanically
    displaces ptc"** — FIXED (`ccba406`), chs 3+10. The mechanism is now stated
    both places: Medicaid eligibility disqualifies a person from exchange
    subsidies, so misplacing people between the two channels moves both errors in
    opposite directions while the total barely stirs — the total was the
    structurally protected number, and the components were where the model's real
    claims lived.

---

## Standing flags out of this round

- **New York / MyFriendBen** (item 24) — the one live factual conflict.
- **Cosilico PBC naming** (item 50) — existing checklist item, now with the
  applications-tier question attached.
- **Calibration-target count** (item 29): public docs 2,813 vs manuscript 9,168
  (gated).
- **Capstone topic** (item 14), **net-of-deductions logged case** (item 17),
  **"given up on improving on" location** (item 20) — each needs a fact only you
  hold.
- **Repo renames**: mid-session, another agent reported executing
  populace→microcosm / ledger→chronicle repo renames; a same-day GitHub check
  still showed the old names live. The book uses the new working names per the
  naming discipline either way; nothing depends on the repo cutover date.
- **FNS→FNA rename** (June 2026): check present-tense agency references at
  copyedit.

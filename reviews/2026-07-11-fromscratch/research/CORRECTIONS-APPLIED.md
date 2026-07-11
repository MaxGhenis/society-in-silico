# Corrections applied — primary-source merge into the fact base

Date: 2026-07-11. Completes the interrupted merge of the three verification passes
(`part1-verification.md`, `part2-verification.md`, `part345-verification.md`) and their
new-source bibliographies into `references.bib` and `reviews/2026-07-11-fromscratch/facts/*.facts.md`.

Scope of this pass: verify the bib merge; spot-verify the already-edited facts files 01–09;
apply the outstanding corrections to 00, 05, and 10–18; resolve every `[NEEDS CITATION]` for
which a verification file supplied a source; keep the genuinely unresolved markers. No git operations.

---

## 1. Bibliography verification — COMPLETE

- `references.bib`: **201 entries, 0 duplicate keys** (`grep '^@' … | sort | uniq -d` empty).
- Every key across the three `*-new-sources.bib` files resolves in `references.bib`, either
  directly or via a documented in-place fold (the "updated-in-place counts" rule):
  - `glied2015aca` → folded into existing **`collins2015aca`** (authors corrected to Glied/Arora/Solís-Román; note documents the fold). Key retained for citation stability.
  - `hmt2024policyengine` → folded into **`hmt2025policyengine`** (year corrected 2025→2024, month December; note documents it).
  - `inayatali2019cbo` → folded into **`inayatali2023cbo`** (year corrected 2023→2019, title completed; note documents it).
  - `orcutt1990engineering` → already present as **`orcutt1990autobiography`** (same article, complete metadata).
  - `tetlock2005epj` → already present as **`tetlock2005expert`** (same book).
- Citation-integrity sweep: **0 dangling citekeys** in the facts files and **0** in `manuscript/`
  (the only apparent hit is the literal `[@key]` format example in doc prose).
- No new entries needed to be added; no key collisions to rename.

---

## 2. Files 01–09 spot-verification (already edited by the prior run)

Confirmed PRESENT and correct:
- **02** — Historian name corrected to **Chung-Tang Cheng** (was "Hsiang-Ke Cheng"); note flags the confusion with Hsiang-Ke Chao. (lines 64, 87)
- **02** — DISCOVERY present: Sadowsky "probably the most useful program I ever wrote," ~3 months, 1963 [@sadowsky2005interview]. (line 37)
- **03** — **§6103(f)** for JCT access (was §6103(l)); §6103(h) for Treasury/OTA. (line 23)
- **03** — DISCOVERY present: IFS founding — Hopper/Buist/Taube/Chown, 1965 Finance Act, dinner **30 July 1968** at the Stella Alpina, incorporated 1969 [@ifs2024history]. (line 9)
- **04** — Random-walk finding reattributed to **Kliesen & Thornton (2012)** [@kliesen2012cbo], quoted in the Inayatali thesis; thesis's own 3.9%-of-GDP result kept on [@inayatali2023cbo]. (lines 29, 63, 81) AHCA "23 million" correctly on [@cbo2017ahca]. (line 51)
- **06** — **POSE Phase I, award #2518372**, $299,974, 15 Aug 2025, year corrected 2024→2025 and decoupled from the April 2024 50-state launch [@nsf2025pose; @policyengine2025nsfpose]. (line 77) ATRS **"Published 17 December 2024"** and the exact NI wording **"almost 60% of datapoints falling within 0.5% of one another"** [@hmt2025policyengine]. (lines 69, 91)
- **07** — Mini-budget (23 Sep 2022) top-decile **+£2,738 (2.5%)**, bottom +£45 [@policyengine2022growthplan] (was "about £2,500"). (line 122) ASEC corrected to **~75,000–90,000 households** (was "roughly 100,000"); enhanced-dataset "100,000" clarified as record count. (lines 69, 82)
- **09** — GPT-4 given the **SARA subset (nine curated IRC sections)**, not the full Code [@blairstanek2023gpt4tax; @holzenberger2020sara]. (line 14)
- **01** — Westworld ban already fully applied (banned fake quote + verified line at lines 8, 94, 132).

FIXED this pass (corrections the 01–09 batch had missed):
- **09 / TaxCalcBench** — enriched line 15 with the exact strict/complete-return numbers requested for verification: **Gemini 2.5 Pro 32.35% (best), Claude Opus 4 27.45%**, Gemini 2.5 Flash 25.98%, Claude Sonnet 4 23.04%; lenient ±$5/line 38–52%; the ~15–20% bracket-vs-tax-table "$3" mechanism. (was "fewer than one in three" with no figures)
- **09 / California Poppy** — line 48 was still UNCORRECTED. Fixed to **67 departments** (was "fifty"), **~10 models / CDT lists Claude, Gemini, GPT, Nova** (was "eleven"), **pilot began 29 Sept 2025** (was "a month later (December 2025)"), **2,800+ employees** (was "more than two thousand"), statewide rollout July 2026. Story-beat timing (line 57) fixed to stop framing Poppy as *after* the IRS deployment (its pilot predates it).

---

## 3. Corrections applied to 00, 05, 10–18

### 00-preface
- Nikhil disclosure (fact + structural note): enriched with the public trace — "Innovation Fellow with 10DS," ~six months from summer 2025, `10ds-microsim` [@policyengine2026downingstreet]. **`[VERIFY with Nikhil: role wording]` marker KEPT.**

### 05-a-wall-of-frustration
- Yang Freedom Dividend figures (74% poverty cut, $2.8T cost, $1.2T raised, $1.6T gap): `[NEEDS CITATION: UBI Center report]` → **[@ubicenter2019freedomdividend]** (note: report's own headline is "$1.4T unfunded" net of offsets; the "$1.6T gap" = $2.8T − $1.2T).
- Carbon-dividend figures (£100/tonne, −14% poverty, −33% deep child poverty): `[NEEDS CITATION: UBI Center report]` → **[@ubicenter2022ukcarbon]**.
- Nikhil disclosure (fact + author-texture footnote + structural note): enriched with the "Innovation Fellow with 10DS" public trace; **marker KEPT**; verbatim footnote left intact with an editorial note beside it.

### 10-encoding-the-law
- Kentucky Deloitte anecdote: **"his Medicaid coverage" → "her Medicaid coverage" (Beverly Likens, she/her)**; citation switched **[@kffhealthnews2024deloitte] → [@liss2024deloittefix]** (verified byline Liss & Pradhan; the old key lists an unverified author "Houghton, Kim" for the same article). (line 30)
- Deloitte state count / contract value: `[NEEDS CITATION]` → **[@pradhan2024deloitte]** (vintage note: 25 states / "at least $5B" June 2024, "$6B" Oct 2025). (line 31)
- OBBBA: tagged **(Public Law 119-21)**; short title struck during Senate amendment. (line 34)
- FY2025 SNAP national payment error rate 10.6%: `[NEEDS CITATION]` → **[@usda2026snapper]** (exact **10.62%**, released **24 June 2026**). (line 35)
- Medicaid work-requirement verification deadline: `[NEEDS CITATION]` → **[@cms2026communityengagement]** (CMS-2454-IFC, 80-hr/month, deadline 31 Dec 2026). (line 37)
- Robodebt / MiDAS / Arkansas: `[NEEDS CITATION]` ×3 → **[@robodebt2023report] / [@bauserman2022midas] / [@ledgerwood2017]**; added the Robodebt "crude and cruel" quote pointer, the ~93% MiDAS figure, and the caption fix **Arkansas DHS v. Ledgerwood** (due-process finding is from RELATED FEDERAL litigation, not *Ledgerwood*). (line 39)
- FNS merit-personnel boundary: `[NEEDS CITATION]` → **[@fns2024aiframework; @fns2024automation]**; added the quotable AI-Framework line "All AI must be used in compliance with program requirements for the use of merit systems personnel, such as those applicable to SNAP." (line 40)
- Structural-note marker list updated (resolved vs open).

### 14-the-uncertainty-gap
- **"13 million fewer insured by 2027": [@cbo2017ahca] → [@cbo2017mandate]** (CBO Nov 2017, pub 53300); the AHCA "23 million by 2026" stays on [@cbo2017ahca]. (line 68)
- Softened "largely [tariffs]" → CBO attributes ~half (note added); softened "beat" → "tend to be more accurate / broadly similar" (note added). (lines 29, 31)
- Finland control-group N (175,000): added `[VERIFY: control-group N]` — treated N and €560 confirmed, control N not confirmable at primary. (line 67)

### 15-simulating-opinion
- Simile: added the new fact that it is the **Stanford "Generative Agents" team (Park, Bernstein, Liang, Yallen) commercializing** — $100M Series A led by Index Ventures, stealth exit 12 Feb 2026 — a through-line from [@park2023generative] to [@simile2026company]. (line 24)
- Bisbee: annotated as a **five-author** paper (Bisbee, Clinton, Dorff, Kenkel, Larson), *Political Analysis* 32(4):401–416. (line 15)
- Mei: annotated with the correct eLocator **PNAS 121(9):e2313925121** (not 121(10)/e2401336121). (line 13)
- ESOMAR (~$140B) already carried [@esomar2024market] — confirmed, no change.

### 16-simulating-democracy
- ACA/"Obamacare" 35% poll: `[NEEDS CITATION: Feb 2017 Morning Consult/NYT poll]` → **[@dropp2017obamacare]** (Dropp & Nyhan, NYT Upshot, 7 Feb 2017; 35% = 17% "different" + 18% "don't know"). (line 43)
- Arrow (1951): annotated publisher **John Wiley & Sons (Cowles Monograph 12)**, not Yale (bib already corrected). (line 44)
- Structural-note marker line updated (resolved).

### 17-simulating-values
- **ADDED the mandatory GSS 2021 mixed-mode discontinuity caveat** (new — primary source): push-to-web 2021–22, response rate **~17% vs ~50%**, self-administration tends to **RAISE** "not wrong at all"; **both** the pre-2024 climb and the 2024 reversal partly sit on a methodological break; NORC's own caution quoted [@gss2024homosex]. Flagged non-negotiable in prose (fact block + structural note).
- Exact 2021/2022/2024 HOMOSEX values marked **"account-gated, direction corroborated"**; noted the internal ~63%(2022) vs ~61%(2022) inconsistency to reconcile at copyedit; series citation now [@gss2024; @gss2024homosex]. (lines 13, 15)
- Gallup recency annotated (71% = 2022–23 peak; 69% 2024). (line 18)

### 18-society-in-silico
- **Westworld epigraph**: replaced the banned fake line with the verified verbatim **"For the first time, history has an author." (S3E2 "The Winter Line," 2020)** [@westworld2020winterline]; marked **"I don't predict the future. I create it." as BANNED** (not a real Serac quote — unquoted characterization only). Applied at the frame (line 8), the story beat (line 71), and the Quotes list (line 78).

---

## 4. Markers — resolved vs still open

### Resolved this pass (verification supplied a source)
| Fact | File | Marker → source |
|---|---|---|
| Yang Freedom Dividend figures | 05 | → [@ubicenter2019freedomdividend] |
| UK carbon-dividend figures | 05 | → [@ubicenter2022ukcarbon] |
| Deloitte state count / $ | 10 | → [@pradhan2024deloitte] |
| FY2025 SNAP error rate 10.62% | 10 | → [@usda2026snapper] |
| CMS Dec 31 2026 verification deadline | 10 | → [@cms2026communityengagement] |
| Robodebt royal commission | 10 | → [@robodebt2023report] |
| Michigan MiDAS | 10 | → [@bauserman2022midas] |
| Arkansas home-care litigation | 10 | → [@ledgerwood2017] |
| FNS merit-personnel guidance | 10 | → [@fns2024aiframework; @fns2024automation] |
| ACA/"Obamacare" 35% poll | 16 | → [@dropp2017obamacare] |
| (already-resolved in 01–09: IBM 704→weik1961survey; JCT scores→jct2017budget/jct2017macro; CPS top-coding→larrimore2008topcoding; Asimov→asimov1952foundation; Tax-Calc 3.2.1→taxcalculator2021v321; contributor count→GitHub API) |

### Still open — deliberately kept (no primary source supplied, or flagged to verify with a person)
- **03** — Brewer quote `[NEEDS CITATION: Brewer quote]`; Reed quote `[NEEDS CITATION: Reed quote]` (both UNVERIFIED at primary).
- **06** — Times-citation mismatch `[VERIFY]`; Enhanced CPS 9,168-targets/97% `[VERIFY: publish or soften]`; EITC transposition `[VERIFY: real incident]`; Atlanta Fed wording; "April" 2024 month; Nikhil role `[VERIFY with Nikhil]`.
- **07** — UC-taper "£1,000/single parent at 25 hrs" `[NEEDS CITATION]`; ">70% MTR 26%→9%" (recompute/soften); 2021 ARP CTC ~$105B `[NEEDS CITATION]`.
- **08** — EITC-state count; PolicyEngine US parameter count; EUROMOD UK file size (all author-internal).
- **10** — Accardi and Lumba authority doctrines `[NEEDS CITATION]`; corpus concept-registry ~41k `[VERIFY]`; US rule-file/state counts `[VERIFY]`.
- **12** — Rwanda findings ledger URL; UK transfer pre-registered harness; Belgium calibration / EUROMOD per-record agreement (all author-internal).
- **14** — Finland control-group N `[VERIFY]` (added this pass).
- **17** — Talkie-1930 / talkie-lm.com `[NEEDS CITATION]`; "swap in the published essay when it ships" `[NEEDS CITATION]`; exact GSS values account-gated.
- **00 / 05** — Nikhil `[VERIFY with Nikhil: role wording]` (enriched, kept).

---

## 5. WRITERS MUST (non-negotiables)

1. **Westworld / Serac**: the epigraph is **"For the first time, history has an author."** (S3E2). The line **"I don't predict the future. I create it." is BANNED** — it is not a real quote; use only as unquoted characterization.
2. **§6103(f)** governs JCT access to returns — never §6103(l) (which is disclosure for non-tax-administration purposes).
3. **Random walk beat the CBO** is **Kliesen & Thornton (2012)** [@kliesen2012cbo], quoted in the Inayatali thesis — not the thesis's own finding.
4. **POSE grant is 2025** (award #2518372, $299,974, 15 Aug 2025) and is **decoupled** from the April 2024 50-state launch.
5. **HM Treasury ATRS**: **17 December 2024** (not March 2025); exact NI wording **"almost 60% of datapoints falling within 0.5% of one another."**
6. **TaxCalcBench** strict numbers: **Gemini 2.5 Pro 32.35%, Claude Opus 4 27.45%** (best model completes fewer than one in three complete returns).
7. **GSS mode-change caveat is mandatory in the values chapter (17)**: the 2021–22 push-to-web switch means the pre-2024 climb *and* the 2024 reversal partly rest on a methodological break. Exact 2021/22/24 values are "account-gated, direction corroborated."
8. **OBBBA = Public Law 119-21** (short title struck during Senate amendment; popular name fine in prose).
9. **Orcutt's three milestones**: 1957 proposal / 1961 first realization (the *Microanalysis* book) / 1975 DYNASIM — never collapse to "eighteen years to a working model."
10. **Beverly Likens is a woman** — "her" Medicaid coverage (Kentucky Deloitte anecdote).
11. **SPM child-poverty attribution**: the 2021 CTC lifted **2.9M children** out of poverty; the **expansion alone lifted 2.1M children** — keep the credit (2.9M) and the expansion (2.1M) distinct.
12. **Mini-budget top-decile gain is £2,738** (2.5%), not "about £2,500."
13. **"13 million fewer insured by 2027"** is [@cbo2017mandate] (pub 53300); the AHCA "23 million by 2026" is [@cbo2017ahca] (pub 52752) — different reports.
14. **Chung-Tang Cheng** (not "Hsiang-Ke Cheng"); **Bisbee et al. = five authors**; **Mei et al. = PNAS 121(9) e2313925121**; **Arrow 1951 = John Wiley** (Cowles Monograph 12).
15. **Zero resolved forecasts**: the Thesis Institute has no track record — never imply one.

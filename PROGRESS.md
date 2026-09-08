# Reproducibility sprint progress

## State

- Final source continuation active from verified live draft PR #5 at `ed1b26fbb1057edd40225704155ed46d703a4a32`: integrate the bounded chapter 2/12/16 source packets and seven bibliography entries, with all calculations and other claims preserved.
- Branch: `codex/society-final-sources-20260907`, in a new isolated worktree; normal pushes update the existing PR branch `codex/society-reproducibility-20260907`. The isolated continuation preserves all six authorized commits through `e8e034c10c220faac4a0eed727d00e8362cec56c`.
- Original worktree and main checkout were clean at inspection and remain untouched. No reset or clean was used.
- Full host network is now available. Fetched `origin/main` on September 7, 2026 at about 18:09 ET: `11dee8b5658c549f1a052cbdf506b013b36a7aa3`, still an ancestor. The clean continuation needs no base merge. Live PR #5 is open and remains a draft; its head and current base were fetched and verified again around 20:05 ET. No base integration is needed because current main remains an ancestor.
- No publication or merge. No usage reset, automatic reset, paid overflow, or paid remote compute. `auto_reset.enabled=false` and the sprint no-reset marker remain intact.
- Deadline: September 7, 2026, 21:00 America/New_York. No additional nested review will be launched. The coordinator has killed the disconnected review process; its attempt supplied no approval.

## Done

- Read global and project instructions, inspected status/branch/remotes/base, and committed this progress file before substantive edits.
- Loaded current PolicyEngine analysis, US domain, data, and healthcare instructions. All calculations use actual managed PolicyEngine; national statistics use MicroSeries and explicit `map_to`, without manual survey-weight aggregation.
- Verified PolicyEngine 5.3.0 on live PyPI and installed the pinned environment entirely offline: US 1.764.6, core 3.30.1, Python 3.14.4. Saved complete dependency pins.
- Independently hash-checked the local certified Microcosm Build P dataset (57,240 households; SHA256 `48b9d479fb4fd1c3537f9383ce4697d130b6f618658409d74f6233c43b994c7e`). No data download or paid compute was required.
- Reproduced the NC family's $38,000→$39,000 raise: $73 kept, 92.7% marginal rate. The NYC long-term-gains comparator is 38.58%. Inputs explicitly handle parent/dependent roles and the absence of an SSI spouse.
- Reproduced CTC receipt at $15,000: $1,875→$4,400 with full refundability in 2026, and $1,875/$7,200/$1,875 under 2020/2021/2022 rules with ages fixed. Receipt uses applied credits, not uncapped entitlement.
- Completed all four notebook code cells on the final source. National result: $20.868bn net fiscal cost, $20.885bn federal income-tax revenue loss, child SPM poverty 17.017%→15.122%, and 1.477m fewer children in poverty. A repeated execution differs by at most $0.000069; poverty results are identical.
- Followed the pinned package's fiscal accounting, including health costs once. Documented the filing-status path that can connect refundable-credit eligibility to ACA and Medicaid rules. No behavioral confidence interval or pessimistic scenario is claimed.
- Replaced unusable MicroSeries pickle checkpoints with weighted JSON aggregates. The final checkpoint totals reconcile to the saved deltas within $0.046; child counts and rates match exactly. Removed only this lane's two known unusable generated pickle files.
- Updated chapters 6/13 and feedback items 21/33. Integrated five supported source-lane corrections, with primary-source locators and hashes: AHCA chronology, Finland control count and confounding reform, dated state EITC count, scoped recipient underreporting, and historical elderly SSI take-up.
- Nine targeted tests, Ruff, `make check`, and the full HTML/PDF builds pass. The artifact validator checks final-source hashes, execution counts, derived chapter numbers, internal anchors, and byte-identical notebook/supporting downloads. Visual inspection covered both notebook figures and eight affected PDF pages. Fixed duplicate automatic chapter numbering.
- `make check` now reports 19 citation, 25 verification, and 2 decision markers (from 23/25/2); unrelated markers and approval conditions remain.
- One bounded semantic Subfleet review was requested on pinned `.codex-3`. DNS prevented connection to `chatgpt.com`, so no independent findings or approval exist. The coordinator subsequently killed the disconnected process; no further nested review will run. Details are in `reviews/2026-09-07-reproducibility/semantic-review-status.md`.

- Reconciled the FINAL source recovery against the completed branch: Pennsylvania EITC omission, exact 2008–2011 New York table window, approximately 173,000 Finnish controls, activation-rule confounding, an explicit unresolved Finnish model-prediction marker, and historical SSI limits. Final recovery and cached-source hashes match their manifests. Computation code, notebook and receipts are unchanged.
- Re-ran `make check` after recovery: pass, with 19 citation / 25 verification / 2 decision markers. The added Finnish marker intentionally restores an unresolved claim.

- Opened draft PR #5 at `2d7f7defa3bbcfdbd1f666733a85c928731f5e97`; `REVIEW-READY.md` and exact file hashes were delivered in the lane directory. Independent review remains pending.
- Refreshed full HTML/PDF, nine tests, artifact agreement and all generated links. At the fixed review head, all 1,326 internal links/assets resolved; 167 external URLs were checked. Four confirmed 404s led to supported repairs: Cheng DOI, Society of Actuaries PDF route, retired UK validation docs, and USDA SNAP report. The USDA repair also corrects the nonexistent 2019–2021 report title and replaces the undated 82% claim with the report's scoped FY 2022 estimate (88% under federal income/resource eligibility).
- Actual WebKit desktop/mobile inspection found long bibliography URL overflow; a scoped wrapping rule fixes all four affected mobile pages. Fixed Ruff 0.16.6's implicit-string-concatenation style finding in the artifact validator. Computation code, notebook, receipts and chapter 6/13 computed numbers are unchanged. The coordinator is explicitly notified that this is a follow-up revision.

- Received the coordinator host computational review of frozen `61c5ce5`: no actionable findings. Supplied hashes match the unchanged computation/receipt artifacts. Preserved the report, 15 fresh household checks, targeted national health results, scripts and logs under `reviews/2026-09-07-reproducibility/independent/`. The review checked weighting and arithmetic but did not rerun the entire national pipeline; source integration remains outside its verdict.
- Documented the reviewer's nonblocking accounting clarification: raw ACA entitlement is not expenditure; assigned PTC, annual premium PTC and BHP changes are zero for this reform. The README preserves that evidence and the need to cover nonzero terms for other reforms.

- Final continuation validation passes: 20 HTML inputs, 158-page PDF, ten real WebKit page/viewport checks over chapters 1/3/6/7/13, notebook download bytes, 1,346 internal links/assets, current artifact agreement and Ruff. The four external 404s are repaired; 50 automated access denials and five network/TLS/DNS exceptions are preserved for manual follow-up. Refreshed logs, marker inventory and source/display evidence are committed in the review directory.

- Received and preserved unchanged the independent source review of `d43b859`; its two P2 findings are accepted for repair. It confirms the other recovered caveats and markers but does not approve the whole manuscript or a fresh full render. Verified the current clean branch/PR head at `755f75d` and fetched unchanged `origin/main` (`11dee8b`); no base integration is needed.

- Implemented both accepted P2 source fixes in three existing paragraph lines: explicit recipient household denominators in chapters 3/6, and a chapter 6 clause limited to published UK aggregate comparisons with official statistics and UKMOD. Social Security remains person-level and age-qualified.
- Fresh focused checks pass: make check; unchanged protected computation/notebook/receipt/bibliography/config files and all 46 markers; all 20 HTML inputs; artifact/number/download agreement; full PDF with physical pages 36/56/57 visually inspected; chapters 3/6 in desktop/mobile WebKit with zero page/HTTP errors or horizontal overflow. No national pipeline was rerun. Targeted coordinator rereview remains pending.

## Next

1. Deliver `SOURCE-FIXES-REVIEW-READY.md` with the exact focused commit, diff and evidence; update existing draft PR #5 and verify its head/body.
2. Await the coordinator's targeted rereview of the two P2 repairs. Keep the source revision fixed or explicitly disclose any further change. Do not launch a nested review.
3. Preserve all 19 citation / 25 verification / 2 decision markers, external-access exceptions, computational-review limits and editorial/author/partner/publication gates. No merge, publication, reset or paid jobs.

## Final source integration continuation — September 7, 20:14 ET

- State: read both final source packets and pinned primary evidence. Full patch hashes match the coordinator-specified values. Group B independent host review is pending; no nested review will be launched.
- Done: preserved the clean delivered worktree at `ed1b26f`, main at `11dee8b`, and the original six-commit editorial worktree; created this continuation from the live PR head. Saved all tracked baseline blobs and no-reset identity in the external `final-source-validation/` artifact directory.
- Next: integrate split chapter patches, append seven unique bibliography entries and update only the OpenFisca access note; incorporate independent Group B findings, validate full HTML/PDF and protected hashes, and deliver `FINAL-SOURCE-INTEGRATION-READY.md` for focused coordinator review. No national computation will be rerun.

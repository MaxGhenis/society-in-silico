# Reproducibility sprint progress

## State

- The requested local implementation and validation are complete: feedback item 33 has an executed notebook, scripts, figures, pinned environment, certified data provenance, and corrected chapter 6/13 numbers.
- Branch: `codex/society-reproducibility-20260907`. The isolated continuation preserves all six authorized commits through `e8e034c10c220faac4a0eed727d00e8362cec56c`.
- Original worktree and main checkout were clean at inspection and remain untouched. No reset or clean was used.
- Cached `origin/main` is `11dee8b5658c549f1a052cbdf506b013b36a7aa3`, already an ancestor. Fetch attempts before edits and at handoff failed with `Could not resolve host: github.com`; current remote base and a hosted draft PR remain blocked.
- No publication or merge. No usage reset, automatic reset, paid overflow, or paid remote compute. `auto_reset.enabled=false` and the sprint no-reset marker remain intact.
- Deadline: September 7, 2026, 21:00 America/New_York. Final validation and draft PR text are committed; the final handoff includes a verified Git bundle and output report. No further simulation is needed for this milestone.

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
- `make check` now reports 19 citation, 24 verification, and 2 decision markers (from 23/25/2); unrelated markers and approval conditions remain.
- One bounded semantic Subfleet review was requested on pinned `.codex-3`. DNS prevented connection to `chatgpt.com`, so no independent findings or approval exist. A stop request for its retrying process was denied by sandbox process permissions. Details are in `reviews/2026-09-07-reproducibility/semantic-review-status.md`.

## Next

1. When network access returns, fetch current `origin/main`, integrate safely, obtain the outstanding independent semantic review, and create a draft PR. Do not merge or publish.
2. If still active, have the sprint coordinator stop review run `20260907-173749-society-pe-review` (PID 56952); this sandbox could not signal it.
3. Leave wider manuscript verification, uncertainty scenarios, and partner approvals for their authorized follow-up work.

# Society in Silico reproducibility report

Draft PR: https://github.com/MaxGhenis/society-in-silico/pull/5

Branch: `codex/society-reproducibility-20260907`. The six original editorial
commits through `e8e034c` remain in history. Main and the original worktree are
untouched. Base `11dee8b` was fetched and remains an ancestor.

The missing notebook is implemented and actually executed. Managed PolicyEngine
5.3.0 / US 1.764.6 on the certified, hash-verified local Build P dataset reproduces
the NC family's 92.7% marginal rate and 2026 CTC full refundability. The saved
national static score is $20.87bn net fiscal cost, 1.90 percentage points less child
SPM poverty and 1.48m fewer children in poverty. Chapters 6/13 agree with the
notebook and JSON; no uncertainty band or behavioral forecast is asserted.

Calculation code, notebook and receipts are unchanged from `61c5ce5`. The
coordinator's independent computational review found no actionable findings. It
reran 15 household cases and targeted national health terms, checked weighting,
formulas and arithmetic, and did not rerun the entire national poverty pipeline.
The review and zero assigned-PTC/BHP change evidence are committed in
`reviews/2026-09-07-reproducibility/independent/`.

Source changes through `d43b859` integrate the FINAL recovered source artifacts,
preserve the approximate Finnish control count, exact sample/time windows,
activation-rule confound, unresolved Finnish forecast marker and Pennsylvania
EITC correction. Four confirmed broken source URLs were repaired from primary
evidence; the USDA repair also scopes the SNAP take-up estimate to FY 2022 and
its federal eligibility denominator. Mobile bibliography URLs now wrap.

Validation passes: nine tests, Ruff, `make check`, 20-page HTML build, 158-page PDF,
notebook/JSON/chapter/download agreement, ten desktop/mobile WebKit checks, and
1,346 internal links/assets. All 167 external URLs were checked; 50 access-denied
and five network/TLS/DNS exceptions are preserved for manual follow-up. There
are 19 citation, 25 verification and two decision markers still visible.

Coordinator review of the later source edits remains pending. The PR is a draft;
no publication or merge occurred. Author/partner signoffs remain, including
Nikhil's exact role wording and commercial-operator naming decisions; no new
close-hold partner assertion was introduced. Static estimates remain conditional
on model take-up, filing, calibration and future-year assumptions.

The exact current Git head, review manifest, final output and refreshed bundle
are recorded in `/Users/maxghenis/capacity-sprint-20260907/society/`. Start with
`REVIEW-READY.md`, `result.md` and `handoff-manifest.json`. Full artifact/test paths
are in `reviews/2026-09-07-reproducibility/validation.md`.

Next step: coordinator source findings on the fixed revision, followed by explicit
fixes if needed. No resets, paid overflow or new paid compute were used. The
no-reset marker and `auto_reset.enabled=false` remain preserved.

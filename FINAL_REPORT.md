The Society in Silico reproducibility milestone is complete locally on branch
`codex/society-reproducibility-20260907`. All six authorized editorial commits
through `e8e034c` are preserved. The original checkout remains clean and untouched.
The validated implementation is committed through `4539158`, followed by this
handoff commit.

| Verified calculation | Result |
| --- | --- |
| NC parent, earnings $38,000→$39,000 | $73 kept; 92.7% marginal rate |
| NYC resident, $30m long-term gains plus $10,000 | 38.58% combined marginal rate |
| Two-child CTC at $15,000, 2026 baseline→full refundability | $1,875→$4,400 |
| Same ages/income, CTC under 2020 / 2021 / 2022 rules | $1,875 / $7,200 / $1,875 |
| National 2026 full refundability | $20.87bn net fiscal cost; child SPM poverty 17.02%→15.12%; 1.48m fewer children in poverty |

The [executed notebook](scripts/notebooks/pe-computed-numbers.ipynb),
[setup instructions](scripts/notebooks/README.md),
[household receipts](scripts/results/pe-computed-numbers/households.json), and
[national receipt](scripts/results/pe-computed-numbers/national.json) use actual
managed PolicyEngine 5.3.0 / US 1.764.6, Python 3.14.4, and the locally cached,
hash-verified certified Microcosm Build P dataset. Population calculations retain
MicroSeries weights and use `map_to`. No manual survey weights were used.
Chapters 6/13 and feedback items 21/33 are updated. Five supported source-lane
corrections were integrated with [evidence locators and hashes](reviews/2026-09-07-reproducibility/source-integration.md).

[Validation](reviews/2026-09-07-reproducibility/validation.md): nine tests, Ruff,
`make check`, full HTML/PDF builds, and the artifact/link validator pass. All four
notebook code cells executed on the final source. A repeat national run differed
by less than $0.0001, with identical poverty results. Both figures and eight
updated PDF pages were visually inspected; duplicate chapter numbering was fixed.
The built book is at `_book/index.html`; the PDF is at
`output/pdf/Society-in-Silico.pdf`. The remaining manuscript marker count is
19 citation / 24 verification / 2 decision markers.

A hosted draft PR and independent semantic review remain blocked. Git fetch
failed with `Could not resolve host: github.com`; the last cached base is
`11dee8b5658c549f1a052cbdf506b013b36a7aa3`. The one bounded Subfleet review on
pinned `.codex-3` could not resolve `chatgpt.com`, so no independent approval is
claimed. Its stop request was denied by sandbox process permissions; if still
active, the coordinator should stop run `20260907-173749-society-pe-review`
(PID 56952). Browser launch was blocked; visual inspection used the rendered PDF,
with separate checks of the actual HTML and downloadable resources.

The sprint output directory
`/Users/maxghenis/capacity-sprint-20260907/society/` contains the final `result.md`,
`draft-pr.md`, `society-reproducibility.bundle`, `full-review.patch`, logs, and
`rendered-page-inspection/`. The incremental bundle preserves the pending commits
and requires the cached base above. It is verified against the existing repository.

Next: when connectivity returns, fetch and integrate current `origin/main` safely,
complete the independent semantic review, and open the prepared draft PR. No merge
or publication occurred. Static outputs are conditional model estimates, not
confidence intervals or forecasts. Wider manuscript verification and partner
approvals remain separate work.

No usage reset, automatic reset, paid overflow, or paid remote compute was used.
`auto_reset.enabled=false` and the sprint no-reset marker remain intact.

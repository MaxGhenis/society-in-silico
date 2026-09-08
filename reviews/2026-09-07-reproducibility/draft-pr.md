# Finish pending editorial corrections and reproduce PolicyEngine scores

The book promised a reproducibility notebook that was absent, while chapters 6
and 13 retained numbers without an executable trail. This change adds the executed
notebook, shared computation/reporting scripts, exact environment pins, certified
dataset provenance, numeric receipts, figures and targeted tests. The specified
North Carolina family's $1,000 raise leaves $73 (92.7% marginal rate). The 2026
CTC full-refundability score is $20.87bn net fiscal cost, with child SPM poverty
falling 1.90 percentage points, or 1.48m children. Both chapters now use those
results and explicitly exclude uncomputed uncertainty-band claims.

The branch also preserves the six pending editorial commits through `e8e034c`,
integrates supported primary-source corrections on five remaining claims, and
fixes duplicate Quarto chapter numbering. Feedback item 33 links the actual
notebook and records completed validation. PolicyEngine retains its name;
publication and partner-approval conditions remain pending.

Validation: all four notebook code cells executed with managed PolicyEngine
5.3.0 / US 1.764.6 on the hash-verified local certified Build P dataset. National
outputs reproduced to within $0.0001; poverty results matched exactly. Nine tests,
Ruff, `make check`, the full HTML/PDF builds, and the artifact/link validator pass.
Both figures and eight affected PDF pages were inspected. See
`reviews/2026-09-07-reproducibility/validation.md` and its committed logs.

Keep this PR in draft: the independent semantic review could not connect because
of DNS restrictions. Static model outputs are conditional on the pinned data and
model assumptions; the earlier dense Enhanced CPS score and behavioral uncertainty
are not reproduced. Wider manuscript citation/verification markers and approval
conditions remain.

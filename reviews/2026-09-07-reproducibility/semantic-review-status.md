# Semantic review status

One bounded read-only Subfleet review was requested on the authorized pinned
Axiom Codex lane (`/Users/maxghenis/.codex-3`) using the existing subscription.

- Run: `20260907-173749-society-pe-review`
- Prompt and diagnostics: `/Users/maxghenis/capacity-sprint-20260907/society/semantic-review-*`
- Scope: computation semantics, entity/weight handling, fiscal accounting,
  reproducibility, tests, and manuscript claims through commit `6db8bc7`.
- Result: **blocked before review**. The subprocess could not resolve
  `chatgpt.com` and repeatedly failed to connect. No findings or independent
  approval were produced.
- The sprint coordinator subsequently killed this disconnected run, as confirmed
  in the continuation instructions. No further nested review may be launched.

No usage reset, automatic reset, paid overflow, or new paid API/compute job was
used. This status is not a review pass. The local tests, executed receipts,
rendered-page inspection, and build checks are separate validation evidence.
At the first source handoff, the coordinator's independent computational/source
review was pending.
`/Users/maxghenis/capacity-sprint-20260907/society/REVIEW-READY.md` identifies
the fixed revision and the artifacts to review.

## Coordinator host review received

The coordinator supplied `society/independent-computation-review-host.md` with
**no actionable computational findings** at frozen head
`61c5ce5ee55032419d1021bbde6bd9e62dc27884`. Exact copies of the report,
results, scripts and logs are in `independent/`. Their supplied hashes and the
current calculation/receipt hashes were checked on receipt. Computation source,
reporting/execution code, notebook, requirements and numeric receipts have not
changed since that reviewed head.

The review independently reran 15 scalar household cases and a targeted managed
national health calculation, and checked weighting, fiscal accounting, artifact
arithmetic and the nine tests. It did not rerun the full national poverty/fiscal
pipeline. The raw ACA entitlement increase is accompanied by zero assigned PTC,
annualized premium-tax-credit and BHP changes for this reform, so no missing
health expenditure must be added. The README now preserves this scope and warns
against reusing the accounting without checking those terms for another reform.

Later source edits, including the FINAL recovery and explicit link repairs, are
outside this computational verdict. Coordinator source review remains pending.
No approval of the whole manuscript, empirical forecast, publication, author or
partner claims follows from this scoped review.

## Focused source findings and owner fixes

The independent source delta review of `d43b859` returned two P2 findings. Its
unchanged report and receipt are retained in `independent/source-delta-review.md`
and `source-review-receipt.json`. It supported the remaining recovered source
caveats and markers, within the scope and environment limits in that report.

The owner explicitly repaired recipient household denominators in chapters 3/6
and narrowed chapter 6's validation sentence to the pinned UK aggregate/UKMOD
comparison. The person-level Social Security sentence, numerical calculations,
raw receipts, other caveats and all 46 markers are unchanged. `source-fixes.md`
records the evidence and fresh local HTML/PDF/source checks. The coordinator's
targeted rereview is pending; implementation and local checks do not change the
independent verdict to a pass by themselves. No nested review was launched.

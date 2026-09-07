# Reproducibility sprint progress

## State

- Assignment: finish feedback item 33 with reproducible PolicyEngine household marginal rates and CTC full-refundability calculations; validate chapters 6 and 13.
- Deadline: 2026-09-07 21:00 America/New_York. No publication or merge authorized.
- Isolated continuation: `codex/society-reproducibility-20260907`, preserving all six authorized commits through `e8e034c`.
- Original worktree and main checkout were clean at inspection and remain untouched.
- Cached `origin/main`: `11dee8b5658c549f1a052cbdf506b013b36a7aa3`, already an ancestor. Fetch attempted before edits but blocked by `Could not resolve host: github.com`; current remote base is not yet verified.
- No resets, overflow, or paid remote compute. The no-reset marker is present and `auto_reset.enabled=false`.

## Done

- Read global `AGENTS.md`, project `.claude/CLAUDE.md`, sprint instructions, and feedback item 33.
- Inspected status, branch, remotes, commit history, and available base before substantive edits.
- Loaded PolicyEngine analysis, US domain, and data skills. Calculations will use the managed package; population statistics will retain MicroSeries weights and use `map_to`.
- Confirmed the promised `scripts/notebooks/pe-computed-numbers.ipynb` is missing.

## Next

1. Inventory local model environments and certified data; record exact reproducibility pins.
2. Execute and validate household earnings increments and full-refundability examples.
3. Run a managed national rescore only if local certified data and resources suffice; otherwise record the exact blocker without replacing claims with invented results.
4. Commit executable notebook, script, receipts, and verified chapter/feedback updates in coherent steps.
5. Run `make check`, `make build`, inspect affected rendered pages, and integrate useful supported source-lane findings.
6. Prepare a draft PR if network access permits; write final handoff to `/Users/maxghenis/capacity-sprint-20260907/society/result.md`.

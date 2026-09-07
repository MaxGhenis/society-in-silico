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
- Verified PolicyEngine 5.3.0 from the live PyPI release listing and installed its US extra entirely offline in the isolated `.venv-pe` (US 1.764.6, core 3.30.1, Python 3.14.4). Saved complete dependency pins.
- Located and independently hash-checked the certified Build P dataset (57,240 households; SHA256 `48b9d479fb4fd1c3537f9383ce4697d130b6f618658409d74f6233c43b994c7e`) in the existing Hugging Face cache. A national rescore is feasible locally.
- Baseline `UV_OFFLINE=1 make check` passed; its marker census reports 23 citation, 25 verification, and 2 decision markers. Saved log in the lane artifact directory.
- Exploratory runs confirmed CTC entitlement must be distinguished from applied credits. Household validation is checking explicit parent and spouse roles before any manuscript numbers change.
- Household milestone verified: explicit parent/SSI spouse roles; NC $38,000→$39,000 leaves $73 (92.7% MTR), NYC long-term gains 38.6%; CTC at $15,000 rises $1,875→$4,400; historical 2020/2021/2022 credits are $1,875/$7,200/$1,875. Seven targeted statistical, SSI-boundary, fiscal-accounting, and resource-reconciliation tests pass.
- Updated chapter 6's household figures and notebook link, chapter 13's recap, and feedback items 21/33. The old national totals remain unchanged pending verification.
- The first national run caught a ~$20m Medicaid interaction, invalidating the simplifying assumption of unchanged health costs. Revised fiscal accounting follows PolicyEngine 5.3.0's budget helper components on MicroSeries outputs, adding federal/state health costs once. A full notebook execution is now validating this, with local simulation checkpoints.
- Jupyter kernel startup is blocked by local socket permissions; the notebook has a pure-Python executor that actually runs every code cell and records outputs/errors without ports. Local WebKit launch also aborts in this environment; plan HTML structural checks plus Quarto PDF visual inspection with the PDF skill.
- Saved the executable notebook with its completed household cells while the national cell runs. Added clone/setup/execution instructions and exact calculation conventions. Inspected both generated household figures visually: labels, curves, comparison and wider cliff are legible.

- Completed every notebook code cell with real managed PolicyEngine. The certified national result is $20.868bn net fiscal cost, $20.885bn federal income-tax revenue loss, child SPM poverty 17.017%→15.122%, and 1.477m fewer children in poverty. Chapter 6 and chapter 13 now use that vintage and remove uncomputed uncertainty-band claims.
- A checkpoint reload probe found plain pandas pickling drops MicroSeries weights. Replaced it with JSON totals/rates computed while weights are intact; nine tests pass. The completed result predates this serialization-only change (its receipt identifies the exact executed source hash). A final execution will validate the final source and weighted checkpoints.

- `make check` and the full HTML build pass. The notebook and supporting resources are copied correctly, and chapters 6/13 render the verified figures. PDF rendering also succeeds; visual inspection caught a preexisting duplicate chapter-number problem (“8 Chapter 6”), now fixed by disabling automatic numbering. Added an artifact-chain validator for execution counts, source hashes, derived chapter figures, anchors, and copied notebook/resources. Final source-hash validation awaits the planned final execution.

## Next

1. Request one bounded read-only semantic Subfleet review and fix actionable findings.
2. Run `make check`, `make build`, and inspect the affected rendered pages and notebook resources.
3. Integrate useful supported findings from the separate source lane.
4. Execute the final notebook source and preserve final output hashes and validation logs.
5. Prepare a draft PR if network access permits; write final handoff to `/Users/maxghenis/capacity-sprint-20260907/society/result.md`.

# Group B source handoff

Frozen book: `ed1b26fbb1057edd40225704155ed46d703a4a32`. Retrieved 2026-09-07 (America/New_York). This artifact owns only chapter 12 line 35 and chapter 16 lines 51 and 73. Group A owns chapter 2. The book checkout was not edited. Exact proposed text is in `corrected-prose.md`; `group-b.patch` contains only the two chapter files and six appended bibliography entries. `entries.bib` is also separate for the bibliography owner.

## Exact claim dispositions

| Frozen location/claim | Disposition | Primary evidence |
| --- | --- | --- |
| Chapter 12: reduced-complexity emulator/IPCC scenario-work marker | Resolve with a bounded, dated clause naming FaIR and AR6. | C1, C2, C3; C4 corroborates. |
| Chapter 16: exclusive pre-1931 training/no polls unseen by construction | Replace the paragraph. Treat the cutoff as intended; leakage remains an empirical question. | T1, T2, T3. |
| Chapter 16: weakness only in elicitation, not knowledge | Remove unsupported generalization. | T1, lines 48–55. |
| Chapter 16: stronger checkpoints within months | Remove unverified timeline. The checked public listing contains three 13B models, including the modern comparator; an empty GitHub Releases endpoint is not proof of no other release. | T1, lines 47 and 87–92; T4, T5, T6. |
| Chapter 16: all quantitative opinion records postdate cutoff | Remove the inference; no claim here about absence of earlier quantitative records. | Not established by any cited source. |
| Chapter 16: roughly 100 countries since 1981/WVS waves marker | Resolve with WVS alone: 108 countries/territories cumulatively, seven waves, 1981–2022, per June 2024 documentation. | W1 composition table, W2 methods. |

## Talkie evidence and limits

T1 is the authors' April 2026 project report, not a peer-reviewed model paper. Its detailed leakage and post-training sections qualify its introductory categorical language. Local text locators: cutoff and contamination 66–73; synthetic prompts/judging/chats 80–86. The 7B example and 13B discussion must not be conflated. The report does not establish poll-specific contamination or leakage-free polling performance.

T2 identifies the released base model, 260B pretraining tokens, and the separate instruction-tuned model (line 9). T3 identifies the derivative and historical instruction-response material plus online DPO (lines 11–13). The model-card revisions below pin documentation, not the exact weights used for every reported evaluation. The report does not provide a weight digest mapping its figures to those revisions. T7/T8 provide repository-reported weight identities only: base `final.ckpt` LFS SHA-256 `caa3c1691dd8cdd2cbae9167437aaa6630144f7303f75883658698f2061b6f9f`; instruction-tuned `rl-refined.pt` LFS SHA-256 `c6fd903b67ad312c7537095fa982b0e77735ccb689c8cfc774ca492694e70064`. These remote metadata digests were not verified against downloaded weights. No weights were downloaded, no model was run, and no new forecasting result is claimed.

The replacement preserves a conditional research opportunity and requires checks of the selected checkpoint, survey targets, post-training, and prompt information. The exact extent of unseen historical polling remains unresolved. Future checkpoint availability and capability remain unverified beyond the specific public listings checked; no prediction of a release date survives in the proposed prose.

## Climate evidence and limits

C1: Smith et al. (2018), published June 18, 2018, DOI `10.5194/gmd-11-2273-2018`. Printed pp. 2273–2274 (PDF pages 1–2), abstract and introduction, describe the simple emissions-driven model and scenario projections. The paper documents v1.3; it is not the AR6 configuration.

C2: IPCC (2022), Annex III, section A.III.II.2.5.1, printed p. 1880 (PDF page 40), left column, “WGI-calibrated emulators”; right column describes combined uncertainty. MAGICC v7 supplies main classification; FaIR v1.6.2 adds uncertainty ranges. Page 40 was rendered and visually checked (`ipcc-annex-p40.png`). The annex's suggested citation and DOI appear on PDF page 1.

C3: AR6 WGIII implementation documentation, “Climate emulators,” local text lines 46–55, explicitly names FaIR v1.6.2, MAGICC v7.5.3 and CICERO-SCM. This corroborates the implemented assessment workflow; the manuscript does not claim FaIR alone performed the main classification.

C4: IPCC (2022), Chapter 3, printed p. 306 (PDF page 12), paragraph beginning “Each scenario,” names the three assessed emulators. The chapter is supplementary; the minimal bibliography cites the more precise Annex III.

The new citations end at the scenario-emulator clause. They provide no evidence that Max's proposed climate composition, household-resolution integrated assessment, encoded-carbon coupling, model launch, or organization already exists or works. Those adjacent author/project claims remain untouched and unvalidated by this packet. No climate or Axiom output was produced.

## WVS evidence and limits

W1: official page headed v4.1, June 30, 2024 (local text line 35). Its “Composition of the IVS 1981–2022” table (lines 63–91) gives distinct IVS/EVS/WVS columns. WVS alone has seven waves and 108 countries/territories; 120 is the combined IVS count. The extracted table preserves column structure in `wvs-composition-table.json`. This is cumulative participation, not one-wave coverage or a balanced country panel.

The page also contains older prose referring to 115 combined countries and an earlier version citation. The patch attributes its count to the dated documentation table; it does not treat that inconsistent prose as a current denominator or combine versions. The multiple-wave page's release-note and downloadable-file versions also differ, so it is used only for its explicit sampling explanation.

W2: local text lines 5–6 describes repeated cross-sections and explicitly distinguishes the dataset from a panel following the same people. Coverage metadata does not substantiate the paragraph's adjacent convergence, post-materialism, cultural-zone, or recent-reversal claims. Those assertions are outside this marker repair and remain unchanged, requiring their own evidentiary assessment. No survey microdata or GSS values were downloaded or calculated.

## Local evidence manifest

Each entry below records the requested primary URL, publication/version date, retrieval time and SHA-256 of saved bytes. Line locators refer to the saved `.txt` or `.md` files, not unstable search-render line numbers. PDF locators specify both physical PDF and printed pages. `source-manifest.json` additionally records resolved URLs, response status, size, ETag/Last-Modified when supplied, and HTML text-extraction hashes. These metadata timestamps are not treated as publication dates.

### T1: talkie-report.html

- Source: [talkie-report.html](https://talkie-lm.com/introducing-talkie)
- Date/locator: April 2026; author byline Nick Levine, David Duvenaud, Alec Radford; text lines 3–4, 66–86.
- Retrieved UTC: `2026-09-07T23:51:43.118219+00:00`.
- Local bytes: `evidence-local/talkie-report.html`.
- SHA-256: `c976e2530a95da9ca647192aedc8c076db634676322bc84c172be6dc2df02a6f`.
- Line-reference extraction: `evidence-local/talkie-report.html.txt`; SHA-256 `fa2fe545438e69c6842019ef009dc939d9747a445f3af530995e7790598cbd71`.

### T2: talkie-base-card.md

- Source: [talkie-base-card.md](https://huggingface.co/talkie-lm/talkie-1930-13b-base/raw/b7c97680791f7fca4262c3c80b36ff7d666faab0/README.md)
- Date/locator: 2026; repository revision b7c97680791f7fca4262c3c80b36ff7d666faab0; line 9.
- Retrieved UTC: `2026-09-07T23:52:58.492009+00:00`.
- Local bytes: `evidence-local/talkie-base-card.md`.
- SHA-256: `a7b8e49f049be3f79bb80da7a4d4d47192243cfc6ea0ecdc76a81b0a0051ac86`.

### T3: talkie-it-card.md

- Source: [talkie-it-card.md](https://huggingface.co/talkie-lm/talkie-1930-13b-it/raw/8033675be6360ae0127fa75f941c12d52064f1dc/README.md)
- Date/locator: 2026; repository revision 8033675be6360ae0127fa75f941c12d52064f1dc; lines 11–13.
- Retrieved UTC: `2026-09-07T23:52:58.492433+00:00`.
- Local bytes: `evidence-local/talkie-it-card.md`.
- SHA-256: `261ccb773a37726995107d9665f218b3494a93f2a21199c10cb3cc3ef87da2ce`.

### T4: talkie-model-list.json

- Source: [talkie-model-list.json](https://huggingface.co/api/models?author=talkie-lm&limit=100&full=true)
- Date/locator: Live listing retrieved September 7, 2026; three returned model IDs.
- Retrieved UTC: `2026-09-07T23:51:43.118736+00:00`.
- Local bytes: `evidence-local/talkie-model-list.json`.
- SHA-256: `7dccd4b709ded34422225ad117b6797cefff754f73632df4023745e604c86635`.

### T5: talkie-repo-readme.md

- Source: [talkie-repo-readme.md](https://raw.githubusercontent.com/talkie-lm/talkie/35317ba3a84861a84c84065bd73faf88ad19329c/README.md)
- Date/locator: Pinned repository commit; lines 7–25 (model family/table).
- Retrieved UTC: `2026-09-07T23:52:58.729931+00:00`.
- Local bytes: `evidence-local/talkie-repo-readme.md`.
- SHA-256: `70bf547271598b334fbc7ab0677f6569602f9b314237c4b0c91a9afab262ff2c`.

### T6: talkie-releases.json

- Source: [talkie-releases.json](https://api.github.com/repos/talkie-lm/talkie/releases)
- Date/locator: Live endpoint retrieved September 7, 2026; empty array.
- Retrieved UTC: `2026-09-07T23:51:43.118868+00:00`.
- Local bytes: `evidence-local/talkie-releases.json`.
- SHA-256: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`.

### T7: talkie-base-tree.json

- Source: [talkie-base-tree.json](https://huggingface.co/api/models/talkie-lm/talkie-1930-13b-base/tree/b7c97680791f7fca4262c3c80b36ff7d666faab0)
- Date/locator: Pinned base repository revision; final.ckpt LFS object metadata.
- Retrieved UTC: `2026-09-08T00:00:17.819326+00:00`.
- Local bytes: `evidence-local/talkie-base-tree.json`.
- SHA-256: `a405a2af772955bb16f294438d7a6eb5bf4f5a927bd5370a68d6d9337dd2142e`.

### T8: talkie-it-tree.json

- Source: [talkie-it-tree.json](https://huggingface.co/api/models/talkie-lm/talkie-1930-13b-it/tree/8033675be6360ae0127fa75f941c12d52064f1dc)
- Date/locator: Pinned instruction-tuned repository revision; rl-refined.pt LFS object metadata.
- Retrieved UTC: `2026-09-08T00:00:17.819714+00:00`.
- Local bytes: `evidence-local/talkie-it-tree.json`.
- SHA-256: `afde66e3213f2e1c2916f314a94a62642897c99cb90eff9c9400253be7cb6f8a`.

### C1: fair-paper.pdf

- Source: [fair-paper.pdf](https://gmd.copernicus.org/articles/11/2273/2018/gmd-11-2273-2018.pdf)
- Date/locator: June 18, 2018; pp. 2273–2274 (PDF 1–2).
- Retrieved UTC: `2026-09-07T23:51:43.200536+00:00`.
- Local bytes: `evidence-local/fair-paper.pdf`.
- SHA-256: `1f9381709e14c29c4cbb032a7f6dcf726448dd63afaccec3998c4663a8d4fe50`.

### C2: ipcc-wgiii-annex-iii.pdf

- Source: [ipcc-wgiii-annex-iii.pdf](https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Annex-III.pdf)
- Date/locator: 2022; p. 1880 (PDF 40), section A.III.II.2.5.1.
- Retrieved UTC: `2026-09-07T23:51:43.331826+00:00`.
- Local bytes: `evidence-local/ipcc-wgiii-annex-iii.pdf`.
- SHA-256: `87e5009b7b9b743f6341ecf4d4911c04ee93879b352c11448d7b9899289ded79`.

### C3: climate-assessment-emulators.html

- Source: [climate-assessment-emulators.html](https://climate-assessment.readthedocs.io/en/stable/emulator.html)
- Date/locator: AR6 WGIII version; page publication date not supplied; text lines 46–55.
- Retrieved UTC: `2026-09-07T23:51:43.253142+00:00`.
- Local bytes: `evidence-local/climate-assessment-emulators.html`.
- SHA-256: `2600fc66ba7de47bf7854adc81cb53362fe861323d9d36006d96b84a5296ec8b`.
- Line-reference extraction: `evidence-local/climate-assessment-emulators.html.txt`; SHA-256 `ca5cd704021a26d26b02d82a457c45fcd450be5094b0c660623a13a4295b23a1`.

### C4: ipcc-wgiii-ch03.pdf

- Source: [ipcc-wgiii-ch03.pdf](https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Chapter03.pdf)
- Date/locator: 2022; p. 306 (PDF 12).
- Retrieved UTC: `2026-09-07T23:51:43.259940+00:00`.
- Local bytes: `evidence-local/ipcc-wgiii-ch03.pdf`.
- SHA-256: `84a86c2a186b00a763918c22d9a56b9ad96347d5151817b6273b6f38e92936d1`.

### W1: wvs-trend.html

- Source: [wvs-trend.html](https://www.worldvaluessurvey.org/WVSEVStrend.jsp)
- Date/locator: June 30, 2024, v4.1; text lines 35, 63–91 and 127.
- Retrieved UTC: `2026-09-07T23:51:43.392679+00:00`.
- Local bytes: `evidence-local/wvs-trend.html`.
- SHA-256: `71744fae7603ba2e3a2d68e652a7ffa8294f9fa925c8152e7d8c2c039ec85b16`.
- Line-reference extraction: `evidence-local/wvs-trend.html.txt`; SHA-256 `a30a6e1b3f169f6c3b9b5425e4bd41fb64445465abb8486b84c41de930fd2412`.

### W2: wvs-methods.html

- Source: [wvs-methods.html](https://www.worldvaluessurvey.org/AJDocumentationSmpl.jsp?CndWAVE=-1&INID=&SAID=-1)
- Date/locator: Release notes label 1981–2022, V3.0; no page publication date; text lines 5–6 and 11.
- Retrieved UTC: `2026-09-07T23:51:43.606411+00:00`.
- Local bytes: `evidence-local/wvs-methods.html`.
- SHA-256: `067ef7622b1c2365eb3af2c584ea7901d3412757610455d710c1b8175988c8e9`.
- Line-reference extraction: `evidence-local/wvs-methods.html.txt`; SHA-256 `389e9fa80fc1f0a26e6f30403ec3605ad970c49de622d289adf7db13809cb9b6`.

## Retention and redistribution

Full source PDFs, HTML captures, model-card captures, derivative text, and page images stay in `evidence-local/`, outside every patch. The FaIR paper expressly displays CC BY 4.0 on page 1. The Talkie model cards label Apache 2.0; the repository's separate license file is retained. No license for wholesale redistribution of the Talkie report, IPCC files, or WVS page captures was assumed. WVS methods explicitly prohibit redistribution of original datasets; no datasets were downloaded. Only original corrective prose and bibliographic metadata are proposed for book integration.

## Validation and handoff

See `validation/validation.json` and `REVIEW-READY.md` for patch, citation, preservation and no-reset checks. The initial patch-check command used a wrong relative path and failed before applying anything; rerunning from the snapshot with the correct `../../group-b.patch` path passed. This is artifact-only work: no branch, PR update, public upload, publication, merge, external message, model inference, paid compute or usage reset was performed. The frozen upstream base remains the coordinator's integration responsibility; do not use a source patch as approval of unrelated author/project claims.

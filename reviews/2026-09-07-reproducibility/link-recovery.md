# Link and display repairs after the fixed review handoff

A full generated-book audit at `2d7f7defa3bbcfdbd1f666733a85c928731f5e97`
checked 1,326 internal links/assets without failures and all 167 unique external
URLs. Four external URLs returned 404. These repairs follow that evidence;
access-denied responses and network failures are reported separately and are not
represented as verified dead citations.

| Reference | Supported repair | Evidence |
| --- | --- | --- |
| `cheng2020orcutt` | DOI `10.1215/00182702-8718000` replaces `...8717953`. | Crossref's publisher-deposited record matches Chung-Tang Cheng, the exact article title, *History of Political Economy* 52(S1), 191–217, 2020. The old DOI returns 404; the corrected DOI resolves to Duke (automated access can be denied there). |
| `soa1997dynasim` | Remove the obsolete `/493824/` prefix from the PDF URL. | The Society of Actuaries serves the DYNASIM chapter at the canonical `/globalassets/` URL, HTTP 200. Its text identifies chapter 3 and the August 13, 1997 document date. |
| `policyengine2024ukvalidation` | Replace retired documentation with the actual repository validation notebook, pinned to `5e57717fcb7fa12c969e0aa33eeb1d9786fccaeb`. | The first-party notebook compares model aggregates against UKMOD figures and official-statistics inputs. It was read as source evidence, not executed or copied into this book's computation workflow. The bibliography records the current retrieval year; the citation key is kept stable. |
| `usda2024snap` | Correct the report title to *Fiscal Year 2020 and Fiscal Year 2022*, authors Alma Vigil and Nima Rahimi, October 2024, and link the official PDF. Correct chapter 3's undated 82% claim to an estimated 88% for FY 2022, explicitly among individuals eligible under federal income and resource rules. | Official executive summary, printed p. xiii (PDF page 13), read and visually inspected. This denominator excludes people eligible only under state categorical rules, among other exclusions; it is not a share of all SNAP recipients or a current 2026 estimate. USDA's series page explicitly says there was no FY 2021 report because pandemic waivers left incomplete data. |

Source cache and retrieval manifest:
`/Users/maxghenis/capacity-sprint-20260907/society/review-head-validation/link-recovery/`.
The committed `link-recovery-evidence.json` pins successful source retrievals.
No new PolicyEngine computations or national claims were introduced.

WebKit desktop and 390px mobile inspection identified bibliography URLs extending
beyond the viewport on all four affected chapters. `book.css` allows bibliography
and footnote URLs to wrap without hiding or truncating them. The probe eliminated
horizontal overflow at both inspected viewport widths. The final generated pages
are checked again using the actual stylesheet, without injected styles.

Ruff 0.16.6 also flagged an implicit concatenation in the artifact validator.
Parenthesizing that expression preserves the exact checked string and satisfies
the linter. Calculation source, notebook, JSON receipts, and the computed chapter
6/13 numbers are unchanged from the fixed computational/source review head.

These are explicit follow-up changes. Coordinator independent computational/source
review remains pending; the local checks are not an independent national-effects
approval.

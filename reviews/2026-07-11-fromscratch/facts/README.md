# The knowledge layer

The from-scratch rewrite is fact-driven: writers compose from verified catalogs,
never by paraphrasing old prose. Four artifacts hold the truth.

1. `research/concepts/registry.yml` — **concept truth.** Every term a general
   reader needs defined once, its one-sentence definition, the chapter that owns
   its first full definition, aliases, and links. The linter
   (`scripts/check_book.py concepts`) enforces introduce-once, in dependency order.
2. `reviews/2026-07-11-fromscratch/facts/*.facts.md` — **per-chapter fact
   catalogs.** One file per chapter: the claims, numbers, dates, names, and quotes
   that chapter is allowed to make, each carrying its source or a `[NEEDS CITATION]`
   / `[VERIFY]` marker. This is what a writer reads before drafting.
3. `research/verification/*.md` — **primary-source verdicts.** The adjudicated
   record of what was checked against the statute, dataset, or paper, and how it
   came out; a fact is "verified" only when a verdict backs it.
4. `reviews/2026-07-10T1227/rewrite-facts.md` — the canonical fact sheet for claims
   about the author's projects (orgs, counts, retired names).

Rule: writers read the facts, never the old prose. New claims come from these
catalogs or arrive marked for verification — nothing is inherited from a prior draft.

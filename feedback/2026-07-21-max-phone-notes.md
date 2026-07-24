# Max's read-through feedback — 2026-07-21 (phone notes, decoded)

Raw notes from Max's phone read; each flags a manuscript passage to investigate.
Decodings below are Claude's best interpretation — items marked (?) are
uncertain readings; confirm against the manuscript before editing, and where
the fix needs a fact only Max holds, leave a [MAX] flag rather than guessing.
Standing rules: no fabricated mechanisms; verify against sources/repos/git
history; every fix passes `make check`; voice per
reviews/2026-07-11-fromscratch/voice.md; rebuild listen edition + deploy site
after edits.

1. **"40 to 50 percent of snap recipients - different from aggs could be
   response bias"** — find the 40–50%-of-SNAP-recipients claim. Survey-reported
   receipt famously undercounts vs administrative aggregates (response bias /
   underreporting). Either reconcile the number to admin data or add the
   response-bias caveat.
2. **"Vaseline different shops"** — (?) almost certainly autocorrect for
   **"baseline"**: passage claiming a/the baseline, when different modeling
   shops (CBO, JCT, TPC, Tax Foundation) maintain different baselines. Find the
   baseline discussion and make it shop-plural.
3. **"Openfusca us young"** — the OpenFisca-US passage: check the account of
   the US package's youth/origins (PolicyEngine US began as the `openfisca-us`
   package). Verify against repo git history.
4. **"State tax"** — a state-tax claim to re-verify. Search state-tax mentions
   near the OpenFisca/PolicyEngine chapters; check coverage/dates claims
   against policyengine-us history.
5. **"Freedom dividend I did myself"** — the Freedom Dividend (Yang UBI)
   analysis is attributed wrongly; **Max did it himself**. Fix attribution
   (check ubicenter/maxghenis repos for the artifact to cite).
6. **"Should to to adults"** — (?) likely: the Freedom Dividend description
   should say it went **to adults** (18+), not to everyone. Verify the
   dividend's design in the passage.
7. **"Matt jensen pointed to openfusca nikhil choose"** — origin-story
   correction: **Matt Jensen pointed them to OpenFisca; Nikhil chose it.**
   Fix the lineage anecdote to match.
8. **"Microdf / Blank slate uni"** — microdf's origin ties to the UBI Center's
   **Blank Slate UBI** project (uni = UBI autocorrect). Check how the book
   introduces microdf; verify against ubicenter/microdf history.
9. **"Tax data / Tax brain app"** — the Tax-Calculator/**Tax-Brain** passage:
   check the description of what Tax-Brain was (PSL web app over
   Tax-Calculator) and the tax-data pipeline claims (taxdata repo). Don't
   conflate Tax-Brain/COMP/Tax-Calculator.
10. **"UCL Durham"** — a university is wrong: likely Nikhil's — check whether
    the book says UCL where it should say **Durham** (or vice versa). Verify
    the person's actual affiliation before editing. [MAX if unresolvable]
11. **"Mit / Capstone"** — Max's MIT DEDP program: the culminating project is a
    **capstone**, not a thesis. Check how the book describes it.
12. **"C3"** — (?) a **501(c)(3)** claim to verify — likely about the UBI
    Center's or PolicyEngine's legal form (UBI Center was not itself a
    501(c)(3); PE operates under PSL Foundation sponsorship). Find and fix the
    legal-form claim. [MAX to confirm the intended entity]
13. **"Democracy lab"** — (?) an org named Democracy Lab appears or should
    appear — possibly early fiscal sponsorship or volunteer-platform history.
    Search manuscript; if absent, [MAX] for what this points to.
14. **"Net of applicable deductions"** — find this (or near-identical) tax
    phrase; it's imprecise or wrong in context. Recompute/reword.
15. **"Nsf award number"** — the NSF grant mention should carry (or correctly
    state) the award number. Verify against NSF's public award search
    (PolicyEngine POSE award) and cite the number.
16. **"Nikhil still innovation fellow"** — tense fix: Nikhil is **currently**
    an Innovation Fellow with the No 10 data science team; the book may use
    past tense or a fixed duration. Align with PE's own post and present
    reality.
17. **"Given up on improving on"** — find the phrase "given up on improving
    on" (or close); awkward/overclaiming — rework the sentence.
18. **"80% more than double hedge fund - state local tax niit"** — a top
    marginal-rate style claim: something like "80%... more than double [what a]
    hedge fund [manager pays]" — the computation should account for **state and
    local taxes and the Net Investment Income Tax**. Find the passage,
    recompute the comparison properly (federal + state/local + NIIT on the
    relevant income types), and fix the numbers.

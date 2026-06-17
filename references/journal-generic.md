# Journal Style — Generic Quantitative-Science Journal

Load this file when the user selects `generic` in the startup interview — i.e. their target journal is not one of the named profiles (HJ, JHRS, TIM) and they want sensible cross-journal defaults.

**This profile is a baseline, not a substitute for the target journal's author guidelines.** It encodes conventions common to most quantitative-science journals (IMRaD structure, SI units, sequential numbering, a mandatory Limitations subsection). Wherever a rule genuinely varies between journals — citation style, word limits, abstract format, first-person policy — this file says so explicitly and **defers to the user's journal**. Do not invent a specific journal's rule. If the user pasted author guidelines, those override this file on every point of conflict; otherwise ask, or flag the item for the user to confirm before submission.

## Language and register

- English, formal academic register. Define every abbreviation on first use; use one term per concept throughout (terminological consistency is a core Audit check).
- **First person:** journal-dependent. Many quantitative journals now accept "we"; some still require the impersonal passive. If the user has not stated a preference and pasted no guidelines, ask once, then apply the choice consistently. Default to impersonal passive if no answer.
- Reference figures and tables by capitalized label ("Figure 2", "Table 3", or the journal's abbreviation "Fig. 2" — match the journal; default to spelling out "Figure" / "Table").

## Verb tense by section

Standard scientific convention (overridden by journal guidelines if they differ):

- **Methods:** past tense ("was applied", "were calibrated")
- **Results:** past or present, used consistently ("the model achieved" / "Figure 3 shows")
- **Discussion:** present tense for interpretation
- **Established facts (Introduction):** present tense

## Document structure (IMRaD; decimal headings, ≤3 levels)

```
Title
Authors and affiliations
Abstract  (length and structure per journal — default ≤250 words)
Keywords  (count per journal — default 4–6)
1.  Introduction
2.  Materials and methods (or Methods)
    2.x  Study system / data
    2.x  Approach / model / procedure
    2.x  Analysis / parameter estimation
3.  Results
4.  Discussion
    4.x  Limitations and future directions   ← mandatory subsection
5.  Conclusions
Acknowledgements
References
```

Subsection count is driven by the study, not the template — copy the structure the user confirmed in the interview. Some journals merge Results and Discussion or place Methods last; follow the target journal if the user specifies it.

## Abstract

- Default: single paragraph, ≤250 words, no citations, no undefined abbreviations.
- Some journals require a **structured** abstract (Background / Methods / Results / Conclusions headings) — use that form only if the journal requires it.
- Lead with the problem's importance and the main quantitative finding; state objectives, methods (approach, data, period, sample size), key results with real values, and implications. Never put a number in the abstract that is not sourced from the manuscript data.

## Citation format

**Journal-dependent — do not guess.** The two dominant families are:

- **Author–year (Harvard/APA-like):** `(Author Year)` in text; reference list alphabetical by surname.
- **Numbered (Vancouver/IEEE):** `[1]`, `[2]` in text; reference list in citation order.

Determine which the journal uses (from pasted guidelines, the user, or an existing reference list in the manuscript). If it cannot be determined, ask before formatting citations. Resolve every citation through Semantic Scholar; never fabricate a reference or DOI. Use a `[CITATION NEEDED]` marker rather than inventing a source.

## Equations

- Number displayed equations sequentially `(1)`, `(2)`, … ; inline equations unnumbered.
- Italic single-letter variables; upright for functions (exp, sin, log), operators, and multi-letter abbreviations (RMSE, KGE).
- Multiplication as `×` or `·`, never an asterisk in display math.
- Define every symbol immediately after the equation in which it first appears.

## Figures and tables

- Independent sequential numbering for figures and tables.
- Figure captions below the figure; table captions above the table (unless the journal specifies otherwise).
- Captions complete and self-contained; every figure/table must be cited in the body, and every cited figure/table must exist (a core Audit cross-reference check).

## Numerals and units

- SI units throughout; space between number and unit ("531 m", "24 °C"); no space for percentages/angles ("40%", "90°").
- Spell out integers below ten in running prose unless paired with a unit; use numerals with units.
- Decimal separator: full stop. Report consistent significant figures for a given quantity across the manuscript.

## Pre-submission checklist (generic — augment with the journal's own list)

Before export, verify:

- [ ] Structure follows IMRaD (or the journal's required order)
- [ ] Abstract within the journal's word limit; no citations unless the journal allows them
- [ ] Keyword count matches the journal
- [ ] Citation style (author–year vs numbered) matches the journal and is applied consistently
- [ ] All in-text citations resolve to a reference-list entry, and vice versa
- [ ] All equations numbered with every symbol defined
- [ ] Every figure/table is cited in the body and every citation has a matching caption
- [ ] Limitations subsection present, each item as *limitation → impact → remedy*
- [ ] SI units, consistent significant figures, consistent terminology throughout
- [ ] Study period, coordinate system (if any), and sample sizes consistent across sections
- [ ] Remaining journal-specific items (line spacing, section order, declarations) checked against the author guidelines

## Export details for .docx

Follow the baseline in `references/manuscript-docx-style.md` (serif body, decimal numbered headings, SI units, OMML equations, citeproc citations). Apply any journal-specific overrides the user supplies (margins, line spacing, column count, font).

# Journal style — Physiological Measurement (PM, IOP Publishing / IPEM)

Source: IOP publishing-support pages for the journal, verified 2026-09-01:
`about-physiological-measurement/` (scope, article types, word limits, abstract headings),
`journals/physiological-measurement/` (structure, references, figures, declarations, portal),
`questions/style-guide-journal-articles/` (Harvard examples, "figure 1"/"table 1", units),
`questions/references/` (Harvard in-text forms, *et al* rule).

Re-verified 2026-09-01 by loading all four pages in a real browser. That pass surfaced the SAGER
requirement, the 30-subject floor, the mandatory-Harvard and mandatory-article-title rules, the
`(doi: ...)` reference form and the figure-placement rule. None of these appear in summarised
fetches of the same pages.

Where this profile is silent, fall back to `references/manuscript-docx-style.md`.

---

## Scope (verbatim)

> "publishes papers about sensing, assessing, visualising, modelling, classifying, predicting, and
> controlling physiological functions in clinical research and practice"

with emphasis on "state-of-the-art methods such as artificial intelligence (AI) and machine learning
algorithms, novel applications, and rigorous large-scale validation".

Two declared tracks:

- **Methodological:** signal processing, AI/ML for physiological signals (ECG, EEG, EMG),
  measurement techniques, wearables, modelling, regulatory and ethical considerations.
- **Application:** patient monitoring, disease diagnostics, brain health, mobile health, sleep,
  maternal and fetal health, sports medicine, environmental physiology.

Unlike the vaguer society-journal scopes, this one names machine learning and classification
explicitly, so scope fit for a biosignal-ML paper is stated rather than argued. PM also publishes
the PhysioNet/Computing in Cardiology Challenge collections, so its reviewer pool already treats
threshold-free discrimination and threshold placement as separate quantities.

## Article types and limits

| Type | Words | Abstract |
|---|---|---|
| **Research paper** | not normally more than **8000** | max **250**, structured |
| Letter | ~3000 | requires a justification statement |
| Note | ~3500 | structured, same headings |
| Comment / Reply | ~1800 | — |
| Topical Review | 12000–18000 | commissioned |
| Tutorial | ~18000 | — |

A correction-shaped or reanalysis manuscript has somewhere to go here, which is not true of every
society journal. Comments apply only to papers published in PM itself.

## Structured abstract — mandatory headings

**Objective. / Approach. / Main results. / Significance.**

Max 250 words for a research paper (the general author page says 300; the journal's own About page
says 250, so treat 250 as binding and leave a 10-word margin). No citations, no undefined acronyms,
no references to figures, tables or equations. Clinical trials must give the registration number.

## Hard journal policies discovered only on the About page

These are not general IOP rules; they are PMEA-specific and they bind.

- **Minimum group size.** "For papers that report measurements on groups of human subjects we require
  the number of subjects in each group to be 30+. This is for both statistical reasons and for
  clinical credibility." Authors with smaller groups are told to contact the journal before
  submitting. Check every *reported* group, including subgroups that carry an argument.
- **SAGER.** "For articles that report on subjects capable of differentiation by sex and/or gender
  Physiological Measurement requires that assessment and reporting of sex and gender information is
  considered in study design, data analyses, results and interpretation of findings." The manuscript
  **must** contain "a statement on whether sex as a biological variable has been considered in the
  study and justifying any imbalance in sex in subject groups". A dataset with no sex variable does
  not exempt the paper; it makes the statement mandatory and negative.
- **Article titles in references are mandatory.** IOP's style guide makes article titles optional in
  general, then names Physiological Measurement among the journals where they are required.
- **Harvard is mandatory.** IOP lets most journals choose Harvard or Vancouver, then names
  Physiological Measurement among those that "require all references to be written using the Harvard
  alphabetical style". Numeric citations are not an option here.
- **Peer review is the author's choice:** single-anonymous or double-anonymous. Single-anonymous
  requires author names and institutes at the start of the submission PDF; double-anonymous requires
  a fully anonymised manuscript with names, institutions and funding stripped from the
  acknowledgements.
- **Articles previously considered elsewhere:** authors are *encouraged* to upload the earlier
  journal's reviews and their responses, which "may expedite the review process".

## Structure

1. Title (sentence case, key terms for discoverability)
2. Authors and affiliations; corresponding author marked, with e-mail
3. Abstract (structured), then keywords
4. 1. Introduction
5. 2. Methods (decimal subsections written `2.1.`, `2.2.`, …)
6. 3. Results
7. 4. Discussion (limitations as the final subsection)
8. 5. Conclusion
9. Acknowledgments — **must contain the conflict-of-interest disclosure and all funding sources with
   agency names and grant numbers**; IOP places both here, not in separate sections
10. Author contributions (CRediT encouraged)
11. Data availability statement
12. Ethical statement (required for human or animal research)
13. References

The guidance page lists the section as "Method" singular; published PM papers use "Methods". Either
passes.

## Citations — Harvard alphabetical, IOP variant

In text: `(Smith 2001)` or `Smith (2001)`; two authors `(Smith and Jones 2001)`; **more than two
authors `(Smith et al 2001)` — "et al" carries no full stop**. Same-year works by the same author
take `2001a`, `2001b`. Page-specific: `Smith (2001, p 39)`.

Reference list, alphabetical. IOP's own worked example for a journal article:

```
Chapman S, Trancoso R, Syktus J, Eccles R and Toombs N 2025 Impacts on compound drought heatwave
events in Australia per global warming level Environ. Res. Lett. 20 054070
```

Pattern: `Surname Initials, Surname Initials and Surname Initials YEAR Article title in sentence
case *Journal Abbrev.* **Volume** page-or-article-number`. Initials are spaced and unpunctuated, the
year follows the authors with no brackets, the journal title is abbreviated and italic, the volume
is bold, and the DOI is included where available. Use `et al` in the reference list only beyond ten
authors; list all authors up to ten.

Book: `Whelan C T 2018 Atomic Structure (IOP Publishing)`. Preprint: `Jones R and Brown A 2011
arXiv:0912.1470`.

The DOI is given in parentheses with a `doi:` prefix, not as a URL:
`... Environ. Res. Lett. **20** 054070 (doi: 10.1088/1748-9326/adc8bd)`.

IOP states that exact conformity is not required provided the system is sensible and consistent, so
minor abbreviation choices are not a rejection risk. The three PMEA-specific requirements above
(Harvard, article titles, DOIs) are not in that discretionary category.

## Language and typography

- **"figure 1" and "table 1" in text, lowercase.** The contractions "fig." and "tab." are
  **prohibited**. Capitalise only at the start of a sentence.
- Full space between a number and its unit (`8 s`, `15 mg dL⁻¹`); no hyphen between number and unit.
- Percentages closed up (`20.4%`), matching published PM practice.
- Acronyms defined at first occurrence, lowercase unless containing proper nouns.
- Zero first-person pronouns is a house rule, not an IOP rule, but it travels well here.
- **En dashes are correct for ranges** and IOP asks for no spaces around them (`1043–65`,
  `0.909–0.981`). IOP also permits em dashes in place of commas or brackets; the house rule here
  forbids them, so use commas, colons or parentheses instead. En dashes are unaffected by that rule.
- Acronyms are defined at first occurrence **in the abstract and again in the main text**, then used
  alone. Do not introduce an acronym for a phrase used only once. Definitions are lower case unless
  they contain proper nouns.
- Only Roman characters in the body and the reference list. CJK characters are permitted in the
  author list only.
- Follow `references/anti-ai-style.md` in full. No em-dashes.

## Figures and tables

- Vector preferred (**EPS, PDF**); TIFF, PNG, JPEG accepted, as are graphics embedded in Word.
- Figure text **8 to 12 pt at final size**.
- **Colour must not be the sole carrier of information.** Use distinct line styles, markers or
  labels alongside colour. This is an explicit accessibility requirement and reviewers do cite it.
- Micrographs need scale bars. Captions must be **self-contained, free of acronyms, and state the
  main points the figure demonstrates** so the figure is usable without the text.
- **Figures and tables go at their first citation point in the submission PDF, not in a block at the
  end.** Multi-part figures label parts `(a)`, `(b)` and every part must be explained in the caption.
- Body text at least **12 pt** with reasonable line spacing, for reviewer readability. Line numbers
  are added automatically on submission; do not add them.
- Tables: no colour, referenced by number in the text.

## Files and submission

- LaTeX (any variant) or Word. **Fonts restricted to Times, Helvetica, Courier or Symbol.**
- Submit a **single PDF with figures embedded**; supplementary uploaded separately, 50 MB per file
  and 150 MB combined. Supplementary files need a title (≤30 characters) and description (≤30 words).
- Equations via Word Equation Editor or MathType.
- Videos MPEG-4 (H.264), max 10 MB, no music.
- Portal: **https://mc04.manuscriptcentral.com/pmea-ipem** (ScholarOne).
- For double-anonymous review, anonymise the manuscript and strip identifying content from the
  acknowledgements, including grant numbers.

## Practical notes

- 2025 Impact Factor 2.5; CiteScore 5.5; Q2 Engineering (Biomedical).
- Hybrid open access. Subscription publication is **free of charge**. Gold OA APC is
  GBP 2410 / EUR 2765 / USD 3325 excluding VAT, with reduced rates for Group B countries
  (GBP 500 / EUR 575 / USD 675) and zero for Group A. **IPEM members outside centrally paid
  agreements get a 25% APC discount.** No submission charges.
- Cohorts of one to three hundred subjects are normal for a proof-of-concept here, which is a real
  scope advantage over ABME, Computers in Biology and Medicine or IEEE JBHI for small-cohort work.
- For a prediction-model paper, file the **TRIPOD+AI** checklist (Collins *et al* 2024) as
  supplementary material.

## Pre-submission checklist

**Submission presentation — check these first.** They are not stated in this
journal's guide for authors and are the most common cause of a pre-review desk
return. Read `references/submission-format.md`; apply with
`scripts/apply_submission_format.py`; verify with `scripts/validate_docx.py` on
the exact file to be uploaded.

- [ ] Continuous line numbers present, restarting `continuous`
- [ ] Page numbers present as a footer field, not typed digits
- [ ] Body text double-spaced (table cells may stay single)
- [ ] Single-column layout; source is .doc/.docx/.tex, never a PDF
- [ ] No strikethrough, no underline, no live tracked changes
- [ ] Separate files (highlights, graphical abstract, supplementary data) built AND
      confirmed with the user as uploaded in the submission system — upload state
      cannot be read from the filesystem
- [ ] `scripts/validate_docx.py` output shown to the user verbatim, not summarised

Unverified for this journal specifically: the baseline above is applied because
guide silence is not evidence that nothing is required. Do not tell the user
this journal states these rules.


- [ ] Body ≤ 8000 words
- [ ] Abstract ≤ 250 words under **Objective / Approach / Main results / Significance**, no citations
- [ ] Keywords supplied
- [ ] Harvard author-year citations, `et al` with no full stop beyond two authors
- [ ] Reference list alphabetical, IOP pattern, journal abbreviated and italic, volume bold, DOIs present
- [ ] "figure N" and "table N" lowercase throughout; no "fig." or "tab."
- [ ] Space between number and unit; percentages closed up
- [ ] Figure text 8–12 pt; no colour-only encoding; vector where possible
- [ ] Conflict of interest **and** funding with grant numbers, both inside Acknowledgments
- [ ] Data availability statement present and specific
- [ ] Ethical statement present for human data, with approval body and ideally protocol number
- [ ] Author contributions (CRediT); ORCIDs for all authors
- [ ] Fonts limited to Times, Helvetica, Courier, Symbol
- [ ] Single submission PDF with figures embedded
- [ ] Every abbreviation defined at first use
- [ ] No em-dashes; `references/anti-ai-style.md` self-check passed
- [ ] Any cohort overlap with prior publications disclosed in Methods and cover letter, prior paper attached
- [ ] **SAGER statement present**, saying whether sex as a biological variable was considered and
      justifying any imbalance (mandatory, negative statement required when sex is unrecorded)
- [ ] **Every reported group has 30+ subjects**, or the journal has been contacted in advance
- [ ] Article titles present in every reference; DOI given as `(doi: ...)`
- [ ] Tables and figures placed at first citation, not blocked at the end
- [ ] Body text 12 pt or larger; no manually added line numbers
- [ ] Peer review model chosen (single- or double-anonymous) and the PDF prepared to match
- [ ] Supplementary files each carry a title (<=30 characters) and description (<=30 words) inside the file
- [ ] TRIPOD+AI checklist attached if the paper reports a prediction model

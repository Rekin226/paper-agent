# Journal style — Journal of Medical and Biological Engineering (JMBE, Springer)

Source: JMBE aims-and-scope (https://link.springer.com/journal/40846/aims-and-scope) and
submission guidelines (https://link.springer.com/journal/40846/submission-guidelines), verified
2026-08. Conventions not stated by the publisher are taken from the group's own accepted JMBE
manuscript (`ECG/ecg_glucose/manuscript.md`) and are marked HOUSE below, not as journal rules.

Where this profile is silent, fall back to `references/manuscript-docx-style.md`.

---

## Scope (verbatim)

> "The purpose of the *Journal of Medical and Biological Engineering*, JMBE, is committed to
> encouraging and providing the standard of biomedical engineering. The journal is devoted to
> publishing papers related to medical and biological engineering, biomedical signals, medical
> imaging, bio-informatics, tissue engineering, and so on. Other than the above articles, any
> contributions regarding hot issues and technological developments that help reach the purpose are
> also included."

The scope is permissive by vagueness. A biosignal or clinical-ML paper qualifies under "biomedical
signals". There is no sentence naming machine learning, classification, or diagnostic modelling, so
scope fit should be argued in the cover letter rather than assumed.

## Article types

Only **Original Article** and **Review Article**. Special or guest-edited issues exist.

There is **no Short Communication, Technical Note, Brief Report, Letter, Correspondence, Comment,
Reply, or Matters Arising type.** A paper that responds to or corrects other published work has no
dedicated vehicle and must be submitted as an Original Article, which means it carries a novelty
expectation it may not be able to meet. Flag this to the user before targeting JMBE with a
correction-shaped manuscript.

## Hard limits — these bind, and they bind early

| Item | Limit |
|---|---|
| Body word count | **3000 words maximum** ("longer articles may be considered by editors only under special circumstances") |
| Figures + tables | **8 combined** |
| Abstract | **150–250 words**, structured |
| Abstract headings | **Purpose, Methods, Results, Conclusion** (singular "Conclusion") |

The 3000-word cap is the single most consequential constraint. It is roughly half the length of a
typical Elsevier or IOP research paper, and it forces hard choices: a multi-arm validation or
sensitivity analysis will not fit in the main text alongside a full Introduction and Discussion.
Plan the supplementary material *before* drafting, not after, and decide explicitly which analyses
live in the main text.

Word-count triage order when over budget, most expendable first:
1. Background prose in the Introduction that a domain reader does not need
2. Methods detail that is standard practice (cite rather than describe)
3. Secondary or sensitivity analyses → supplementary, leaving a one-sentence pointer and a table row
4. Discussion paragraphs that restate Results
5. Never cut: the limitations, the primary result's uncertainty, or the reproducibility statements

## Structure

1. Title
2. Authors and affiliations, corresponding author with email
3. Structured Abstract (Purpose / Methods / Results / Conclusion)
4. Keywords
5. 1. Introduction
6. 2. Materials and Methods (decimal subsections: 2.1, 2.2, …)
7. 3. Results
8. 4. Discussion (limitations as the final subsection)
9. 5. Conclusion
10. References
11. **Statements and Declarations** (Springer umbrella heading, placed *after* References)

## Statements and Declarations (Springer order) — HOUSE, per the group's accepted JMBE paper

Under a single "Statements and Declarations" heading after References, in this order:
Funding; Competing Interests; Ethics Approval; Consent to Participate; Consent to Publish;
Data Availability; Code Availability; Author Contributions.

Springer operates a **type 1 research data policy** for JMBE: data deposition is encouraged, not
mandated. A Data Availability statement is still expected and must be specific. "Available on
request" alone is weak; name the holder and the conditions.

## Language and style

- **Zero first-person pronouns.** No "we", "our", "I", "my", anywhere. The group's accepted JMBE
  manuscript contains none. Use passive voice in Methods ("the model was fitted"), and attribute
  agency to the data or the analysis elsewhere ("the matched analysis shows", "discrimination fell").
- Past tense in Methods, present tense in Results and Discussion.
- Define every abbreviation at first use.
- SI units. Glucose in mg dL⁻¹ is acceptable in this literature; be consistent.
- Follow `references/anti-ai-style.md` in full. No em-dashes.

## Citations — numeric, Springer style

In text: bracketed numerals in citation order, `[1]`, `[2,5]`, `[7–9]`.

Reference list, numbered in citation order (HOUSE format, matching the group's accepted paper):

```
[1] Sun, H., Saeedi, P., Karuranga, S., et al. (2021) IDF Diabetes Atlas: global, regional and
country-level diabetes prevalence estimates for 2021 and projections for 2045. Diabetes Research
and Clinical Practice 183:109119. https://doi.org/10.1016/j.diabres.2021.109119
```

Pattern: `Surname, Initials., …, et al. (Year) Title in sentence case. Journal Volume:pages or
article number. https://doi.org/...`

Use "et al." beyond three authors. Give the DOI as a full URL. Do not italicise the journal name in
the plain-text draft; the .docx pipeline handles typography.

## Reporting guidelines

Springer Nature "advocates complete and transparent reporting" and points authors at the **EQUATOR
Network**, naming CONSORT, STROBE, PRISMA, **STARD/TRIPOD**, CARE and ARRIVE. This is
recommendation language, not a submission gate, but a reviewer can cite it. For a prediction-model
paper, filing a **TRIPOD+AI** checklist as supplementary material is cheap insurance and pre-empts
the most predictable methods objection.

## Overlapping publication

The guidelines state the manuscript "should not be submitted to more than one journal for
simultaneous consideration", prohibit splitting "a single study … into several parts to increase the
quantity of submissions" (salami-slicing), and allow that "concurrent or secondary publication is
sometimes justifiable, provided certain conditions are met".

If the manuscript reanalyses a cohort the same authors have already published, that overlap must be
disclosed in the cover letter **and** stated in the Methods, with the prior paper cited. Per ICMJE,
attach a copy of the prior publication at submission. Undisclosed overlap is a desk-reject risk on
redundancy grounds regardless of scientific merit.

## Practical notes

- 2025 Impact Factor 2.1; median time to first decision approximately 20 days.
- Hybrid open access.
- There is no stated minimum sample size and no stated policy requiring external validation.

## Pre-submission checklist

- [ ] Body ≤ 3000 words (excluding abstract, references, and statements)
- [ ] Figures + tables ≤ 8 combined
- [ ] Structured abstract 150–250 words under Purpose / Methods / Results / Conclusion
- [ ] Zero first-person pronouns
- [ ] Numbered `[N]` citations in citation order; reference list matches the Springer pattern
- [ ] "Conclusion" is singular in both the abstract heading and the section heading
- [ ] Statements and Declarations block present, after References, in Springer order
- [ ] Data Availability statement is specific, not a bare "on request"
- [ ] Every abbreviation defined at first use
- [ ] No em-dashes; `references/anti-ai-style.md` self-check passed
- [ ] Any cohort overlap with the authors' prior publications disclosed in Methods and cover letter
- [ ] Supplementary material assembled for whatever the 3000-word cap displaced
- [ ] TRIPOD+AI checklist attached if the paper reports a prediction model

# Journal Style — Hydrogeology Journal (Springer / IAH)

Load this file when the user selects `hj` in the startup interview.

## Language and register

- English only. **Zero first-person pronouns** (I, we, my, our). Use passive voice or noun phrases: "This study demonstrates...", "The results indicate...".
- No contractions. Formal academic register throughout.
- 'groundwater' (one word), 'water table' (two words), 'hydrogeology' (not 'geohydrology').
- Define all abbreviations on first use.
- Reference figures and tables with initial capitals: "As shown in Fig. 2 and Table 3..."

## Verb tense by section

- **Methods:** past tense ("was applied", "were calibrated")
- **Results:** present tense ("the model achieves", "Fig. 3 shows")
- **Discussion:** present tense
- **Established facts in Introduction:** present tense ("groundwater provides")

## Document structure (decimal headings, max 3 levels)

```
Title (sentence case)
Authors and affiliations
Abstract (≤250 words, single paragraph, no citations)
Keywords (up to 5)
1.  Introduction
2.  Materials and methods
    2.1  Study area
    2.2  Data and preprocessing
    2.3  [method-specific subsections]
    2.x  Parameter estimation
    2.x  Model selection (if applicable)
3.  Results
    3.1  [results subsections driven by the study design]
4.  Discussion
    4.1  [interpretation subsections]
    4.x  Limitations and future directions  ← mandatory subsection
5.  Conclusions
Acknowledgements
References
```

The exact subsection count under Methods, Results, and Discussion is driven by the study — copy the structure the user confirmed in the interview.

## Abstract structure (≤250 words, no citations)

Single paragraph. No internal headings. Order:

1. Sentences 1–2: importance of the problem + main finding (with real cached numbers).
2. Problem statement and objectives.
3. Methods summary: approach, data, period, sample size.
4. Key results with specific values.
5. Conclusions and broader implications.

## Citation format (Harvard)

**In-text:**
- One author: `(Thompson 1990)` or `Thompson (1990)` when author is the sentence subject
- Two authors: `(Kelso and Smith 1998)`
- Three or more: `(Barakat et al. 1995)`
- Multiple citations: alphabetical, semicolon-separated: `(Abbott 1991; Barakat et al. 1995)`

**Reference list entry:**
```
Burns ER, Bentley LR (2012) Title of paper in sentence case. Hydrogeology J 18(6):1357–1373. doi 10.1007/s10040-010-0607-z
```

- No comma before year
- Journal names abbreviated per ISSN LTWA
- DOI prefixed with `doi ` (lowercase, no colon), not a URL
- Alphabetical by first author surname, deduplicated by DOI

## Equations

- Number displayed equations sequentially: `(1)`, `(2)`, ... at right margin
- Inline equations not numbered
- Multiplication: `A×B` or `A·B` (never asterisk)
- Italic for single-letter variables (h, a, b, K, t)
- Upright for functions (exp, sin), operators, multi-letter abbreviations (RMSE, AMP)
- Define every symbol immediately after the equation it first appears in

## Figures and tables

- In-text: "Fig. 1", "Table 1" (initial capital, "Fig." abbreviated)
- Figure captions **below** the figure; table captions **above** the table
- Independent sequential numbering for figures and tables
- Captions must be complete and self-contained

## Numerals and units

- Numbers 1–9 spelled out unless followed by a unit: "nine stations" but "9 m"
- Space between number and unit: "531 m", "24 °C"
- No space for percentages and angles: "40%", "90°"
- SI units throughout
- Decimal separator: full stop. Thousands separator: comma ("10,347")

## Pre-submission checklist (HJ-specific)

Before export, verify:

- [ ] Abstract ≤250 words, single paragraph, zero citations
- [ ] Up to 5 keywords
- [ ] Zero first-person pronouns in the full manuscript
- [ ] All in-text citations use Harvard format `(Author Year)` — no commas before year
- [ ] All reference entries formatted as `Surname AB, Surname CD (Year) Title. Journal Vol(Issue):pages. doi ...`
- [ ] Reference list ≥15 entries, alphabetical, deduplicated
- [ ] All equations numbered sequentially with symbols defined
- [ ] Fig./Table references use initial capitals and "Fig." abbreviation
- [ ] Limitations subsection present with every user-supplied item formatted as *limitation → impact → remedy*
- [ ] 'groundwater' one word, 'water table' two words everywhere
- [ ] Study period, coordinate system, and sample sizes consistent across sections

## Export details for .docx

- A4 page, 1-inch margins, single-column
- Times New Roman 12pt body (or equivalent serif)
- Line spacing: 1.5 or double (reviewer-friendly)
- Decimal numbered headings via Heading1/Heading2/Heading3 styles

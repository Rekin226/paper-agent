# Journal style — IEEE Transactions on Instrumentation and Measurement (TIM)

Source: *IEEE Editorial Style Manual for Authors* (29 July 2024, IEEE Publishing
Operations) and *Information for Authors* at https://ieee-ims.org/publication/ieee-tim/information-authors.
All rules below are anchored to those documents — do not invent rules. When
TIM-specific guidance is silent, fall back to the IEEE Transactions baseline
or `references/manuscript-docx-style.md`.

This profile overrides the generic `manuscript-docx-style.md` baseline in the
places noted below. Everything else (TNR coercion, Springer table style fall-
back, TIFF figures, mean ± std merging, OMML equations, reproducible pipeline)
still applies.

---

## Article structure (mandatory order)

Per *IEEE Editorial Style Manual* §II:

1. Title Page (article title, byline, membership, first footnote)
2. Abstract — one paragraph, **150–250 words**
3. Index Terms — alphabetical, final paragraph of the Abstract section
4. Nomenclature (optional)
5. Introduction
6. Body
7. **Conclusion** (singular — not "Conclusions")
8. Appendix(es)
9. Acknowledgment (singular — *no* "s", no "e" between g and m)
10. References
11. Photographs and Biographies

Re-order any draft to match this sequence before audit.

## Length

- IEEE double-column Transactions format
- **Minimum 5 pages.** Below that, submit as a Short Paper.
- No fixed maximum — overlength charges apply above ~10 pages.

## Abstract

- One paragraph
- 150–250 words
- **No numbered equations, no numbered citations, no footnotes** — must be a
  self-contained, standalone reflection of the article
- Variables in lightface italic; numbers and units stay bold

## Index Terms

- Alphabetical order
- Final paragraph of the Abstract section, separated by a line space
- Capitalize first word; lowercase the rest unless capitalized in text
- Define acronyms in parentheses on first appearance

## Section headings

Four levels with established specifications:

- **Primary** (section): Roman numerals, **centered**, 10-pt and 8-pt small
  caps. Example: `I. INTRODUCTION`. *Introduction*, *Conclusion*, and
  *Acknowledgment* are **Singular** heads — Introduction has no Roman numeral
  in some styles; Acknowledgment and References never have Roman numerals.
- **Secondary** (subsect1): capital letter + period, flush left, italic. Example:
  `A. Formal Frameworks`
- **Tertiary** (subsect2): Arabic numeral + paren, indented one em, italic,
  followed by colon. Run into text. Example: `1) Sophisticated Local Control:`
- **Quaternary** (subsect3): lowercase letter + paren, indented two em.
  Example: `1a) Communication policies:`

Pandoc maps `\section{}`/`\subsection{}`/`\subsubsection{}`/`\paragraph{}` to
the four levels. The post-process pass should not renumber — IEEEtran or the
journal copy-editor does that.

## Citations and references

**Numeric bracketed, citation order.** Override the baseline's Chicago author-
date CSL with `ieee.csl`.

In-text citation rules (verbatim from §II.B "References"):

- Cite as `[1]`, not `reference [1]`
- "in [1]" not "In Smith [1]" — drop the author name unless integral to the
  sentence (e.g., "Smith [1] reduced …")
- Cross-references use IEEE notation: `[1, Fig. 2]`, `[1, eq. (8)]`,
  `[1, Sec. IV]`, `[1, Th. 4.2]`, `[1, Ch. 3]`
- **Do not** write "in Fig. 2 of reference [1]"
- **Do not** use reference dates as identifiers
- One reference per number — never group `[1–3]` into one entry; each must be
  a separate numbered list item

Pandoc invocation:

```
pandoc main.tex -o manuscript_v1.docx \
    --bibliography=refs.bib --citeproc --csl=ieee.csl
```

The `ieee.csl` file lives next to `main.tex` (or use the URL form
`--csl=https://www.zotero.org/styles/ieee`).

## Manuscript LaTeX class

Use **IEEEtran** if compiling to PDF directly. The class handles section
numbering, double-column layout, and IEEE-style references automatically.
For the Word pipeline (pandoc → docx), the documentclass is mostly cosmetic —
pandoc reads structure from `\section{}`/`\cite{}` regardless of the class.

Replace natbib commands before exporting:

- `\citep{key}` → `\cite{key}`
- `\citet{key}` → `\cite{key}` (CSL handles narrative vs. parenthetical via
  context; for forced narrative, write "Smith \cite{key}" manually)

## Equations

- Numbered consecutively `(1), (2), …` from beginning to end of article
- Section-prefixed numbering `(1.1), (1.2.1)` permitted in some Transactions
- Appendix equations restart with `(A1), (A2), …`
- Hyphens and periods accepted: `(1a), (1.1), (1-1)` — be consistent
- Equation numbers right-aligned in parentheses (IEEEtran default)
- Reference equations as `(1)`, not "equation (1)"

## Figures

- Caption format: `Fig. 1.` then period, then em space, then caption text.
  First word capitalized. Example: `Fig. 1. Theoretical measured values of n.`
- Use the abbreviation `Fig.` even when beginning a sentence — singular
- First citation of figures must be in numerical order
- Subpart citation: `(a)`, `(b)` appear **before** the corresponding caption
  part. Example: `Fig. 4. (a) and (b) Plain and side views, respectively, of …`
- Figure footnotes go in the caption itself
- **Lena image is banned (effective 1 April 2024)** — do not include
- For reused IEEE graphics: add the source reference number at end of caption

**Figure file specs** (from IEEE Author Center, not in the style manual but
binding for production):

- Line art: 600 dpi minimum, TIFF or vector (EPS/PDF) preferred
- Photographs: 300 dpi minimum, TIFF
- The `manuscript-docx-style.md` baseline emits TIFF at 300 dpi LZW — bump
  line-art figures to 600 dpi for TIM submission.

## Tables

- Roman numeral numbering: `TABLE I`, `TABLE II`, …
- Caption number **centered above** the table, label `TABLE I` on one line
- Descriptive text **centered directly below the number caption**, inverted-
  pyramid style
- **No period** at the end of the table caption
- Subpart notation `(a)`, `(b)` follows the figure convention

This differs from the manuscript-docx-style.md baseline (which uses Springer-
style table-number-and-caption-on-one-line above the table). The post-process
styler should detect TIM mode and split the caption into a centered number
line + a centered descriptive line below it.

## Acknowledgment

- Placement: after the body, **before** References, after any Appendixes
- Singular spelling: `Acknowledgment` (no "s", no "e")
- Primary heading, **not enumerated** (no Roman numeral)
- Written in third person
- Drop Mr., Mrs., Miss; keep Dr. and Prof.
- **Do not put financial support here** — it goes in the first footnote (see
  below). Acknowledgments are reserved for non-financial credit and
  AI-disclosure language.
- **AI disclosure is mandatory** in the Acknowledgment if any AI system was
  used to generate text, figures, images, or code (IEEE Publishing policy,
  in effect since 2024). Use this template, filling in the system name and
  scope:
  > `Fig. X was created using <AI system used>. <Brief explanation regarding
  > the level at which the AI system was used to generate the content.>`
- AI use for editing/grammar enhancement is exempt from disclosure but
  recommended.

## First footnote (author affiliation paragraph)

This is the IEEE-specific block at the bottom of page 1, distinct from a body
footnote. Three paragraphs, unnumbered:

1. **Paragraph 1:** Manuscript received/revised/accepted dates; date of
   publication; date of current version; financial support; corresponding
   author marker (italicized, parenthesized at end). Example:
   > Manuscript received 2 May 2026; revised 9 September 2026; accepted 12
   > October 2026. Date of publication 9 November 2026. This work was
   > supported by NSF under Grant 12345. *(Corresponding author: Jane Doe.)*
2. **Paragraph 2:** Author affiliations — department, institution, city, state,
   ZIP, country, email. Country **mandatory**. Email of corresponding author
   mandatory.
3. **Paragraph 3:** Supplementary materials notice and/or online-only color-
   figure notice with DOI link.

Place a separate "Human/Animal Research" paragraph below the first footnote
and before the affiliations if human or animal subjects were involved (TIM
papers often include this — instrumentation studies frequently use volunteer
subjects).

## Biographies

Required at submission. Three paragraphs per author:

1. Birth (place + date optional), education in order with **years** and full
   locations (institution, city, state if US, country)
2. Work experience, current position, research interests
3. Professional title (Dr./Prof./Mr.), memberships, awards, IEEE-committee
   service

Author photographs are required (professional head-and-shoulders). Squibs
("photograph and biography not available at time of publication") are allowed
per-author. If all authors squib, no squib line is used.

## What changes vs. the manuscript-docx-style.md baseline

| Baseline rule | TIM override |
|---|---|
| Pandoc Chicago author-date | `--csl=ieee.csl` numeric bracketed |
| Author–year cite commands | `\cite{}` numeric only |
| Table caption: Springer style above | `TABLE I` centered above, descriptive text centered below, **no terminal period** |
| Table numbering: Arabic | **Roman numerals** |
| Figure DPI: 300 | 300 for photos, **600 for line art** |
| Section headings: bold | Bold + Roman numeral primary, capital letter secondary (per IEEEtran default) |
| Acknowledgment placement: anywhere | **Between body and References**, never enumerated |
| Financial support: anywhere | **First footnote only**, never in Acknowledgment |
| AI use disclosure: optional | **Mandatory** if AI generated text/figures/code |
| Abstract: any length | **150–250 words, single paragraph, no citations** |
| Index Terms: optional | **Mandatory, alphabetical**, end of Abstract block |

## Pre-submission checklist (TIM)

Run during Audit mode before declaring the manuscript submission-ready:

- [ ] Abstract is one paragraph, 150–250 words, no citations, no equations, no footnotes
- [ ] Index Terms present, alphabetical, after Abstract
- [ ] Section order matches §II of the IEEE Style Manual (Title → Abstract → Index Terms → Intro → Body → Conclusion → Appendix → Acknowledgment → References → Biographies)
- [ ] All citations are `\cite{}` numeric — no remaining `\citep{}`/`\citet{}`
- [ ] First citation of every figure/table is in numerical order
- [ ] Tables numbered `TABLE I, TABLE II, …`, captions above without terminal period
- [ ] Figures captioned `Fig. N. <text>.` with em space after period
- [ ] Equations numbered `(1), (2), …`; appendix equations `(A1), (A2), …`
- [ ] First footnote present with received-date placeholder, financial support, corresponding author marker
- [ ] Acknowledgment is singular, third person, no financial support
- [ ] AI disclosure included in Acknowledgment if AI was used
- [ ] References ≥ 5 pages worth of body content (minimum-length rule)
- [ ] Author biographies drafted (3 paragraphs each) or squib decided
- [ ] Lena image not used (banned since April 2024)
- [ ] Reference list: one entry per number, no grouped `[1–3]` items
- [ ] In-text refs use `[1, Fig. 2]` / `[1, eq. (8)]` / `[1, Sec. IV]` not "in Fig. 2 of [1]"

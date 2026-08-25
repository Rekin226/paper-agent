# Journal Style — Water Resources Research (AGU / Wiley)

Load this file when the user selects `wrr` in the startup interview.

> **Verified 2026-08-25** against AGU's text requirements at
> <https://www.agu.org/publish-with-agu/publish/author-resources/text-requirements>, which
> govern all AGU journals including WRR. Rules below come from that page. The exact
> reference-list format is delegated to AGU's Publications Style Guide and was **not**
> verified here — see "Unverified" at the end.

## At a glance

| Field | Value |
|---|---|
| Publisher | AGU / Wiley |
| Key Points | **Required** — at least one, **up to three**, each ≤140 characters, no abbreviations |
| Abstract | **Less than 250 words**, single paragraph |
| Plain Language Summary | **Optional for WRR** (required only for other AGU titles); ≤200 words if included |
| Length | **25 publication units**; 1 PU = 500 words **or** one figure/table |
| Headings | **Numbered**, Arabic numerals, up to four levels: `1.`, `1.1.`, `1.1.1.`, `1.1.1.1.` |
| In-text citation | `(Author, Year)` / `Author (Year)` — AGU author-date |
| Open Research | **Required section** with an Availability Statement |
| Fig caption | In the text, not inside the graphic |

## What differs most from the HJ default

1. **Key Points are mandatory, but the count is one to three — not exactly three.** Each is
   at most 140 characters, must be a complete thought or sentence, and must contain **no
   abbreviations**. They are excluded from the word count. Count characters literally.
2. **Citations take a comma before the year** — `(Barakat et al., 1995)`, not HJ's
   `(Barakat et al. 1995)`. A find-and-replace across the manuscript is required when
   converting from HJ.
3. **Length is measured in publication units, not words.** 25 PU, where one PU is 500 words
   *or* one display element. Every figure and table you add costs the same as 500 words.
   Never quote the user a plain word budget for WRR; compute PU including display elements.
4. **An Open Research section is mandatory**, and "data are available from the authors" is
   explicitly **not allowed** as a statement.

Headings are numbered, as in HJ, so an HJ-shaped manuscript ports across without
restructuring the section hierarchy.

## Key Points (required, before the abstract)

- At least one, at most three
- Each ≤140 characters **including spaces**
- Each a complete thought or sentence
- **No abbreviations**
- Not counted in the word count

## Abstract

- **Less than 250 words** (150 for GRL, which does not apply here)
- Set as a **single paragraph**
- States the nature of the investigation and summarises the important conclusions
- Suitable for indexing
- **No table or figure mentions**
- Avoid reference citations unless directly dependent on another paper (companion, comment, reply)
- **Define all abbreviations**

## Plain Language Summary

Required for AGU Advances, G-Cubed, GeoHealth, GRL, JAMES, the JGR titles, Space Weather, and
Reviews of Geophysics. **Optional for WRR.** If the user wants one: no longer than 200 words,
free of jargon, acronyms, equations, and any technical content unfamiliar outside the field.

## Headings

- Numbered with Arabic numerals, maximum four levels: `1.`, `1.1.`, `1.1.1.`, `1.1.1.1.`
- Written as sentence fragments
- Must not begin with a lowercase letter or a number
- Must not contain parenthetical citations or figure/table callouts

## Length accounting

- Research Articles: up to **25 publication units**
- 1 PU = 500 words **or** one display element (figure or table)
- **Excluded from the word count:** title, authors, affiliations, Key Points, keywords, text
  inside tables (but *not* table captions), and the reference list
- Equations count as one word each
- Over-length papers are charged an excess length fee

## Citation format (AGU author-date)

**In-text:**
- One author: `(Thompson, 1990)` or `Thompson (1990)` when the author is the sentence subject
- Two authors: `(Kelso & Smith, 1998)`
- Three or more: `(Barakat et al., 1995)`
- Multiple citations: semicolon-separated: `(Abbott, 1991; Barakat et al., 1995)`

**Reference list entry** — the shape below follows AGU's author-date house style, but the
authoritative source is AGU's Publications Style Guide, which was not read during
verification. Treat it as a starting point and check the Style Guide before submission:
```
Lastname, I. N. (Year). Title of the paper. Journal Name, Vol(Issue), pages. https://doi.org/xx
```

**Reference rules that were verified:**
- Every source cited in text, tables, figures, or supporting information must appear in the
  reference list
- **"Unpublished", "in press", and "personal communication" references are not allowed.**
  Every reference must be publicly available online or in print before acceptance.
- Supporting information must not carry its own separate reference list
- Reference text is not counted in the word count
- **Data and software must be formally cited** in the reference list, both your own (as
  described in the Availability Statement) and other people's

## Open Research section (required)

- Must contain an **Availability Statement** saying where readers can access the data and software
- **Statements implying that data are available from the authors are not allowed**
- Data and software described there must also be formally cited in the reference list
- Data supporting every table and figure must be preserved in a repository, with the DOI or
  URL in the Open Research section and a citation in the reference list
- Where a table aggregates underlying data, provide the workflow or script that produced it

Draft this from `references/reproducibility.md`. If the user has not supplied a repository,
flag it as a blocker: this is a stated requirement, and a placeholder will not pass.

## AI disclosure

AI tools cannot be authors. If AI tools were used in writing, in producing images or graphical
elements, or in collecting and analysing data, the use must be disclosed in the Materials and
Methods (or equivalent) section, naming **which tool** was used and **how**.

## Figures

- Formats: JPG, TIFF, EPS, PS, or PDF
- Embedded in the manuscript at submission; uploaded as separate files at revision
- A multi-part figure must be one consolidated file
- **Do not put the caption or the figure title (e.g. "Figure 1") inside the graphic itself.**
  Captions live in the text.
- Do not put information in a figure that could as easily go in the caption

## Inherit from the HJ profile

Unless stated above, follow `references/journal-hydrogeology.md` for language and register,
verb tense by section, equation formatting, and numerals and units, and flag to the user that
you are extrapolating rather than following an AGU rule.

## Pre-submission checklist (WRR-specific)

- [ ] Key Points present: **one to three**, each ≤140 characters, complete sentences, **no abbreviations**
- [ ] Key Points placed before the abstract
- [ ] Abstract **under 250 words**, single paragraph, no figure or table mentions, all abbreviations defined
- [ ] Length within **25 publication units**, counting each figure and table as 500 words
- [ ] Headings numbered, ≤4 levels, sentence fragments, no citations or callouts inside headings
- [ ] Every in-text citation has a comma before the year
- [ ] No "unpublished", "in press", or "personal communication" references
- [ ] Data and software formally cited in the reference list
- [ ] **Open Research** section present with an Availability Statement
- [ ] No statement that data are "available from the authors"
- [ ] Data behind every figure and table deposited, with DOI in Open Research and a reference-list citation
- [ ] AI tool use disclosed in Materials and Methods, if applicable
- [ ] No captions or figure titles baked into the graphics
- [ ] Limitations content present (inherit the HJ mandatory-limitations rule)

## Unverified — confirm before submission

- **The exact reference-list format.** AGU delegates this to its Publications Style Guide,
  which was not read. Check author-count cutoffs for `et al.`, italicisation, and issue-number
  handling there before submitting.
- Keyword count and whether an AGU index-term list is required
- WRR-specific deviations from the AGU-wide rules above, from the journal's own page
- Figure resolution requirements

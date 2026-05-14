# Journal Style — Journal of Hydrology: Regional Studies (Elsevier, EJRH)

Load this file when the user selects `jhrs` in the startup interview.

JHRS has several **mandatory structural elements** that differ from most hydrology journals. Get these wrong and the paper is desk-rejected for formatting before it reaches a reviewer. Read this file carefully.

## Language and register

- English only. **Zero first-person pronouns** (I, we, my, our). Use passive voice or noun phrases.
- Formal academic register. No contractions.
- Define all abbreviations on first use.
- Reference figures and tables with initial capitals: "Fig. 2", "Table 3".

## Verb tense by section

- **Methods:** past tense
- **Results:** past or present tense (be consistent within a section)
- **Discussion:** present tense

## MANDATORY: Structured abstract

JHRS requires a **structured abstract with three labelled sections**. This is non-negotiable — the journal specifically calls out formatting screening for this. Format:

```
Study Region: [brief description of the region studied, location, size, relevant context]

Study Focus: [problem statement, methods summary, data, period, sample size — what was done and why]

New Hydrological Insights for the Region: [the findings, with real cached numbers, and their regional significance]
```

No citations anywhere in the abstract. Total length typically 200–300 words across all three sections combined. The third section must emphasise **regional** insights — JHRS rejects papers that are purely local or purely global without a regional-scale contribution.

## MANDATORY: Highlights

JHRS requires a **Highlights** block: 3–5 bullet points, each a single sentence of ≤85 characters including spaces. Place immediately after the title/author block, before the abstract. Each highlight must be a concrete finding or contribution, not a vague statement.

Example format (replace placeholders with your project's actual findings):
```
Highlights
• `<Model class>` achieves median `<metric>` of `<value>` across `<N>` `<units>`
• `<Distinguishing parameter>` separates `<subgroup 1>` from `<subgroup 2>` behaviour
• `<Alternative-model selection mechanism>` improves `<metric>` by `<value>` in `<subgroup>`
```

## MANDATORY: KMZ/KML file

JHRS requires a `.kmz` or `.kml` file submitted alongside the manuscript, containing at minimum the location and names of the sites or stations used in the study. **Remind the user at export time** that this file is required — the skill does not generate it, but should flag the requirement in the export confirmation message.

## Document structure

```
Title (sentence case)
Authors and affiliations
Highlights (3–5 bullets, ≤85 chars each)
Abstract (structured: Study Region / Study Focus / New Hydrological Insights for the Region)
Keywords (up to 6)
1.  Introduction
2.  Materials and methods
3.  Results
4.  Discussion
5.  Conclusions
CRediT author statement
Declaration of competing interest
Acknowledgements
References
Supplementary material (including KMZ/KML)
```

Subsection depth is at the author's discretion but limit to 3 levels. The Limitations discussion typically appears as the final subsection of the Discussion (§4.x) or can be merged into the Conclusions — check with the user. Either way, the limitations must be present.

## Citation format (Elsevier author-year, not numeric)

JHRS uses **author-year, not numeric** citations. Format:

**In-text:**
- One author: `(Thompson, 1990)` or `Thompson (1990)`
- Two authors: `(Kelso and Smith, 1998)`
- Three or more: `(Barakat et al., 1995)`
- Multiple citations: chronological, then alphabetical within year, semicolon-separated: `(Abbott, 1991; Barakat et al., 1995; Chen, 2020)`

**Note: JHRS uses a comma between author and year, HJ does not.**

**Reference list entry (Elsevier style):**
```
Burns, E.R., Bentley, L.R., 2012. Title of paper in sentence case. J. Hydrol. Reg. Stud. 18, 1357–1373. https://doi.org/10.1007/s10040-010-0607-z
```

- Authors: `Surname, F.M.`, comma-separated, year after authors with comma
- Journal name abbreviated per ISSN LTWA
- DOI as full `https://doi.org/...` URL
- Alphabetical by first author surname, deduplicated by DOI

## Formatting requirements

- **Single-column Word layout** (double-column only allowed for LaTeX submissions)
- **Double line spacing** (not 1.5)
- **Line numbers** throughout the manuscript (continuous)
- Remove all strikethrough and underlined text before submission

## Equations, figures, tables, numerals

Same conventions as HJ (see `journal-hydrogeology.md`): numbered displayed equations, symbols defined on first use, figure captions below, table captions above, SI units, decimal separator full stop.

## Pre-submission checklist (JHRS-specific)

Before export, verify:

- [ ] **Structured abstract** with three labelled sections (Study Region / Study Focus / New Hydrological Insights for the Region)
- [ ] **Highlights** block present: 3–5 bullets, each ≤85 characters
- [ ] **KMZ/KML reminder** flagged to user at export time
- [ ] Zero first-person pronouns in the full manuscript
- [ ] All in-text citations use comma between author and year: `(Author, Year)`
- [ ] All reference entries use Elsevier format with full DOI URL
- [ ] Reference list ≥15 entries, alphabetical, deduplicated
- [ ] Regional scope explicitly justified — not a purely local study dressed up as regional
- [ ] Limitations present (in Discussion or Conclusions)
- [ ] Single-column layout, double line spacing, continuous line numbers
- [ ] All equations numbered sequentially with symbols defined
- [ ] CRediT author statement and competing-interest declaration drafted or marked as TODO

## Export details for .docx

- A4 page, 1-inch margins, **single-column**
- 12pt body (Times New Roman or Arial both acceptable)
- **Double line spacing** (not 1.5)
- **Continuous line numbers** enabled
- Decimal numbered headings via Heading1/Heading2/Heading3 styles
- At export time, print this reminder to the user:
  > ⚠ JHRS submission requires a **KMZ/KML file** containing site locations, a **CRediT author statement**, and a **competing-interest declaration**. These are not part of the .docx — prepare them as separate items before submission.

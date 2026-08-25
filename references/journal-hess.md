# Journal Style — Hydrology and Earth System Sciences (EGU / Copernicus)

Load this file when the user selects `hess` in the startup interview.

> **Verified 2026-08-25** against the Copernicus submission guidelines at
> <https://www.hydrology-and-earth-system-sciences.net/submission.html>. Rules below are
> taken from that page. Where the guide states no rule, this file says so rather than
> supplying a plausible default, per `anti-fabrication.md`.

## At a glance

| Field | Value |
|---|---|
| Publisher | EGU / Copernicus (open access) |
| Abstract | **No word limit is stated.** Must stand alone, no citations unless urgently required, all abbreviations defined |
| Short summary | **Required, 500 characters including spaces**, non-technical, paragraph form |
| Body word limit | **None stated** |
| Headings | Numbered, no trailing punctuation: `1`, `1.1`, `1.1.1` |
| In-text citation | `(Smith, 2009)` or `Smith (2009)`; multiple separated by semicolons |
| Reference style | Copernicus — colon after the author block, **year last** |
| Data availability | **Required named section**, at the end, before the acknowledgements |
| Code availability | **Required named section** when code is used |
| Author contribution | **Required named section**, before the acknowledgements |
| Competing interests | **Required declaration** |

## What differs most from the HJ default

1. **The reference format is unlike every other supported journal.** The author block ends
   with a **colon**, and the year comes **last**, after the DOI. Confirmed directly from the
   guide's own example: `Smith, P.: …, 2009.`
2. **A 500-character short summary is mandatory** and is pasted into the upload form, not
   written into the manuscript. Non-technical, paragraph form, no lists, no abbreviations.
   It is easy to miss because it is not part of the manuscript file.
3. **Three named back-matter sections are mandatory**, not merely recommended: Data
   availability, Author contribution, and Competing interests.
4. **No word limits exist** — not for the abstract, not for the body. Length is governed by
   what the work needs. Do not impose the HJ 250-word abstract cap here, and do not tell the
   user they are over a limit that the journal does not set.
5. **No bold or italic** in in-text citations or in the reference list.

## Abstract

No word limit is stated. The guide requires that the abstract:

- Be intelligible to a general reader without reference to the text
- Briefly introduce the topic, recapitulate the key points, and mention possible directions
  for future research
- Contain no reference citations unless urgently required
- Define every abbreviation it uses (and they must be defined again at first use in the body)

## Short summary (required, separate from the abstract)

500 characters **including spaces**. Non-technical, written in English, paragraph form with
no lists, no abbreviations (spell the terms out). It should state the main conclusions and
results and their implications, and briefly why and how the research was done. Count the
characters literally before submission.

## Citation format (Copernicus)

**In-text:**
- Author outside the sentence: `Precipitation increase was observed (Smith, 2009)`
- Author inside the sentence: `As we can see in the work of Smith (2009), the precipitation has increased`
- Multiple references: all inside one set of parentheses, semicolon-separated:
  `(Smith, 2009; Mueller et al., 2010)`
- **Ordering is the author's choice** — relevance, chronological, or alphabetical. Unlike HJ,
  alphabetical order is not required. Be consistent.
- Two works by the same first author in the same year take `a`, `b`, `c` suffixes, in both the
  in-text citation and the reference list.

**Reference list entry:**
```
Lastname, I. N. and Lastname2, I. N.: Title of the paper, Hydrol. Earth Syst. Sci., Vol, pages, https://doi.org/xx, Year.
```

- Full author list, last name followed by initials
- Author block closed with a **colon**
- Then: title, abbreviated journal name, volume, complete page range (first and last), DOI,
  and finally the **year**
- Use the full journal title if you do not know the standard abbreviation
- `and` spelled out between the last two authors
- No bold, no italic

**Reference list ordering** is more specific than plain alphabetical. For a given first
author: single-author papers first (chronologically, oldest first), then two-author papers
(alphabetically by second author, then chronologically), then `et al.` team papers
(chronologically, then alphabetically by second author within a year).

**Data and software must be cited** like literature: in the body text and in the reference
list, with a persistent identifier. For code on GitHub, mint a DOI through Zenodo and cite that.

## Mandatory back-matter sections

Draft these from `references/reproducibility.md`. If the user has not supplied a repository
or archive location, flag it as a blocker rather than writing a placeholder.

- **Data availability** — required, placed at the end before the acknowledgements. Data
  belong in a FAIR-aligned repository with a persistent identifier (preferably a DOI). If the
  data are not publicly accessible, a detailed explanation of why is required (applicable
  laws, institutional policy, funder terms, privacy, IP and licensing, ethical context).
- **Code availability** — required when software, algorithms, or model code were used. Title
  it `Code availability`, or `Code and data availability` when covering both.
- **Author contribution** — required, before the acknowledgements, describing what each
  co-author did. CRediT is recommended. Example from the guide: *"AA and BB designed the
  experiments and CC carried them out. DD developed the model code and performed the
  simulations. AA prepared the manuscript with contributions from all co-authors."*
- **Competing interests** — required. If none: *"The authors declare that they have no
  conflict of interest."*
- **Sample availability** — required only if IGSN-registered geoscientific samples were used.
- **Statement on inclusion in global research** — optional, up to 100 words.

## AI disclosure

If AI tools were used to generate any part of the manuscript, the usage must be described in
the Methods section or the Acknowledgements. This is a stated requirement, not a courtesy.

## Manuscript composition

- Single-column, following the Copernicus Word or LaTeX template
- **Line numbers and page numbers throughout** — both are required
- Figures and tables placed near their first mention in the text, **not appended at the end**
- URLs spelled out, not hyperlinked behind text
- Submission PDF with embedded fonts, portrait, 50 MB maximum

## Figures

- 300 dpi, width not less than 8 cm
- Individual figure files 5 MB maximum; all submitted files (excluding supplements) 30 MB maximum
- Vector formats (`.eps`, `.pdf`) preferred, with fonts embedded and no hidden objects;
  otherwise a non-lossy bitmap such as `.png`
- Accepted: `.pdf`, `.ps`, `.eps`, `.jpg`, `.png`, `.tif`
- **One font family only**, sans-serif preferred (e.g. Arial or Helvetica)
- The legend belongs **inside the figure**, not described in words in the caption. Write
  "dashed line" into the figure legend, not into the caption text.
- Multi-panel figures collected into a single file, labelled `f01`, `f02`, …
- Check colour schemes for colour-vision deficiency

## English conventions

- Any standard variety of English, but consistent within the article. Oxford `-z-` spelling
  is common; if used, use it throughout. Serial-comma usage must also be consistent.
- **"data" is a countable noun**: *data are*, *data were*, *data include*. Never "data is".
- Abbreviations avoided in the title; defined in the abstract and again at first use in the body
- Units do not need to be defined

## Inherit from the HJ profile

For anything not stated above — verb tense by section, equation formatting and numbering,
numerals and units — follow `references/journal-hydrogeology.md`, and flag to the user that
you are extrapolating rather than following a HESS rule.

## Pre-submission checklist (HESS-specific)

- [ ] Short summary written, **500 characters including spaces**, non-technical, no lists, no abbreviations
- [ ] Abstract stands alone, no citations, all abbreviations defined (no word limit applies)
- [ ] Headings numbered with **no** trailing punctuation
- [ ] Every reference uses the colon-after-authors, **year-last** Copernicus pattern
- [ ] Reference list ordered by the single-author / two-author / team-paper rule, not plain alphabetical
- [ ] Same-author same-year entries disambiguated with a/b/c in text **and** list
- [ ] No bold or italic in citations or the reference list
- [ ] Data and software cited in the text and the reference list with a DOI
- [ ] **Data availability** section present, before the acknowledgements
- [ ] **Code availability** (or **Code and data availability**) section present if code was used
- [ ] **Author contribution** section present, before the acknowledgements
- [ ] **Competing interests** declaration present
- [ ] AI tool usage disclosed in Methods or Acknowledgements, if applicable
- [ ] Line numbers and page numbers present
- [ ] Figures and tables placed near first mention, not appended
- [ ] Figures 300 dpi, ≥8 cm wide, one font family, legend inside the figure
- [ ] "data" used as a plural throughout
- [ ] Limitations content present (inherit the HJ mandatory-limitations rule)

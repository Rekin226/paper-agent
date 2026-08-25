# Journal Style — Water Resources Research (AGU / Wiley)

Load this file when the user selects `wrr` in the startup interview.

> **Provenance.** Ported on 2026-08-25 from the retired project-scoped profile
> (`single_tankV2/.claude/skills/paper-agent/references/journal-styles.md`, committed
> 2026-03-26). Every rule stated below came from that file. Fields it did not cover are
> marked *inherit* or listed under "Unverified — confirm before submission". Do not
> silently fill those gaps: ask the user for the current AGU author guidelines and flag
> every extrapolation, per `anti-fabrication.md`.

## At a glance

| Field | Value |
|---|---|
| Publisher | AGU / Wiley |
| Abstract | ≤ 250 words |
| Key Points | **Required** — exactly 3 bullets, ≤ 140 characters each, placed *before* the abstract |
| Plain Language Summary | Recommended, 100–150 words, non-specialist audience |
| Body word limit | ≤ 12,000 words |
| Headings | **NOT numbered** — plain bold headings |
| In-text citation | `(Author, Year)` / `Author (Year)` — AGU author-date |
| Journal name in refs | Full name, italic |
| Fig caption | Below figure |
| Table caption | Above table |

## What differs most from the HJ default

Three things will bite if the draft is carried over from an HJ-shaped manuscript:

1. **Headings lose their numbers.** No `1.`, `2.1`, `3.1.1`. Plain bold headings only
   (Introduction, Methods, Results…). Any cross-reference written as "see Sect. 3.2" must
   be rewritten to name the section instead.
2. **Key Points are mandatory and come first.** Exactly 3, each ≤ 140 characters
   *including spaces*. Count them literally before export — this is a desk-reject trigger.
3. **Citations take a comma before the year** — `(Barakat et al., 1995)`, not
   `(Barakat et al. 1995)`. A find-and-replace across the whole manuscript is required when
   converting from HJ.

## Abstract and front matter order

```
Title
Authors and affiliations
Key Points (exactly 3 bullets, ≤140 characters each)
Abstract (≤250 words)
Plain Language Summary (100–150 words, recommended)
```

## Citation format (AGU author-date)

**In-text:**
- One author: `(Thompson, 1990)` or `Thompson (1990)` when the author is the sentence subject
- Two authors: `(Kelso & Smith, 1998)`
- Three or more: `(Barakat et al., 1995)`
- Multiple citations: alphabetical, semicolon-separated: `(Abbott, 1991; Barakat et al., 1995)`

**Reference list entry:**
```
Lastname, I. N. (Year). Title of the paper. *Journal Name*, *Vol*(Issue), pages. https://doi.org/xx
```

- Comma before the year, year in parentheses, full stop after
- Journal name written in **full** and italicised (not LTWA-abbreviated as in HJ)
- Volume italicised; issue in parentheses, not italic
- DOI as a full `https://doi.org/...` URL, not the bare `doi ` prefix HJ uses

## Verifying the format against live papers

Sample recent published papers to confirm current practice before export:

```
tool: mcp__semantic-scholar__search_papers
query: "Water Resources Research groundwater hydrology"
fields: paperId,title,authors,year,venue,externalIds
limit: 3
filter: year >= 2022
```

Confirm `venue` matches, then `get_paper` on a paperId for full metadata including
`externalIds.DOI`.

## Inherit from the HJ profile

Unless the AGU author guide says otherwise, follow `references/journal-hydrogeology.md`
for: language and register, verb tense by section, equation formatting and numbering,
numerals and units, and figure/table numbering conventions.

## Pre-submission checklist (WRR-specific)

- [ ] Key Points present, **exactly 3**, each ≤ 140 characters (count including spaces)
- [ ] Key Points placed before the abstract
- [ ] Abstract ≤ 250 words
- [ ] Plain Language Summary present, 100–150 words, free of jargon and undefined abbreviations
- [ ] Body ≤ 12,000 words (excluding abstract, references, captions)
- [ ] **Zero numbered headings** anywhere in the manuscript
- [ ] Every in-text citation has a comma before the year
- [ ] Reference list uses full italic journal names and `https://doi.org/` URLs
- [ ] Figure captions below figures, table captions above tables
- [ ] Limitations content present (inherit the HJ mandatory-limitations rule)

## Unverified — confirm before submission

The retired profile did not record these. Ask the user for the current AGU author
guidelines rather than guessing:

- Keyword count and whether an AGU index-term list is required
- Data Availability / Open Research statement wording (AGU has a specific mandated form)
- Author contribution (CRediT) requirement
- Supporting Information packaging rules
- Figure resolution and file-format requirements

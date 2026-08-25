# Journal Style — Hydrology and Earth System Sciences (EGU / Copernicus)

Load this file when the user selects `hess` in the startup interview.

> **Provenance.** Ported on 2026-08-25 from the retired project-scoped profile
> (`single_tankV2/.claude/skills/paper-agent/references/journal-styles.md`, committed
> 2026-03-26). Fields that file did not cover are marked *inherit* or listed under
> "Unverified". Do not fill those gaps by guessing, per `anti-fabrication.md`.

## At a glance

| Field | Value |
|---|---|
| Publisher | EGU / Copernicus (open access) |
| Abstract | ≤ **300** words (the most generous of the supported hydrology titles) |
| Body word limit | No strict limit; typically 8,000–12,000 words |
| Headings | Numbered, **no trailing punctuation**: `1`, `1.1`, `1.1.1` |
| In-text citation | `(Author, Year)` / `Author (Year)` |
| Reference style | Copernicus — colon after the author block, year **last** |
| Fig caption | Below figure, prefixed `Figure N.` (full word) |
| Table caption | Above table, prefixed `Table N.` |
| Data availability | **Required section** |
| Code availability | **Required section** if code is used |

## What differs most from the HJ default

1. **The reference format is unlike every other supported journal.** The author block ends
   with a **colon**, the title is followed by commas rather than full stops, and the year
   comes **last**, after the DOI. Getting this wrong is the single most common HESS
   formatting error.
2. **"and", never "&"**, between authors in the reference list.
3. **Figures are "Figure 1", not "Fig. 1"** — the full word, in captions and in text.
   HJ's abbreviated "Fig." must be expanded throughout when converting.
4. **Headings drop the trailing dot** — `2.1`, not HJ's `2.1` (same) but definitely not
   Journal of Hydrology's `2.1.`.
5. **Abstract gets 300 words**, not 250. Do not pad to fill it; the extra room exists for
   open-access readers who may never reach the full text.

## Citation format (Copernicus)

**In-text:**
- One author: `(Thompson, 1990)` or `Thompson (1990)`
- Two authors: `(Kelso and Smith, 1998)`
- Three or more: `(Barakat et al., 1995)`
- Multiple citations: alphabetical, semicolon-separated: `(Abbott, 1991; Barakat et al., 1995)`

**Reference list entry:**
```
Lastname, I. N. and Lastname2, I. N.: Title of the paper, Hydrol. Earth Syst. Sci., Vol, pages, https://doi.org/xx, Year.
```

Read that pattern carefully:
- Author block, then a **colon** (not a year in parentheses)
- Title, then a **comma** (not a full stop)
- Journal, volume, pages, DOI — all comma-separated
- **Year last**, followed by a final full stop
- `and` spelled out between the last two authors

## Mandatory back-matter sections

HESS requires these as named sections, not optional courtesies:

- **Data availability** — required in all cases. State where the data live and under what
  licence, with a DOI or persistent link.
- **Code availability** — required whenever code was used to produce the results.

Draft both from `references/reproducibility.md`. If the user has not supplied a repository
or archive location, flag it as a blocker rather than writing a placeholder.

## Verifying the format against live papers

```
tool: mcp__semantic-scholar__search_papers
query: "Hydrology and Earth System Sciences groundwater"
fields: paperId,title,authors,year,venue,externalIds
limit: 3
filter: year >= 2022
```

## Inherit from the HJ profile

Unless the Copernicus guide says otherwise, follow `references/journal-hydrogeology.md`
for: language and register, verb tense by section, equation formatting and numbering,
and numerals and units.

## Pre-submission checklist (HESS-specific)

- [ ] Abstract ≤ 300 words
- [ ] Headings numbered with **no** trailing punctuation
- [ ] Every reference entry uses the colon-after-authors, year-last Copernicus pattern
- [ ] `and` (never `&`) between authors in the reference list
- [ ] Every figure reference reads "Figure N", not "Fig. N", in captions and body text
- [ ] Figure captions below figures, table captions above tables
- [ ] **Data availability** section present and specific
- [ ] **Code availability** section present if any code was used
- [ ] Limitations content present (inherit the HJ mandatory-limitations rule)

## Unverified — confirm before submission

- Keyword requirements
- Author contribution and competing-interests statement wording
- Whether the manuscript targets the interactive public-discussion (HESSD) stage and any
  preprint-specific formatting that implies
- Figure resolution and file-format requirements

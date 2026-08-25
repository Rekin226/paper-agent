# Journal Style — Groundwater (NGWA / Wiley)

Load this file when the user selects `gw` in the startup interview.

> **Provenance.** Ported on 2026-08-25 from the retired project-scoped profile
> (`single_tankV2/.claude/skills/paper-agent/references/journal-styles.md`, committed
> 2026-03-26). Fields that file did not cover are marked *inherit* or listed under
> "Unverified". Do not fill those gaps by guessing, per `anti-fabrication.md`.

## At a glance

| Field | Value |
|---|---|
| Publisher | NGWA / Wiley |
| Abstract | ≤ 250 words |
| Body word limit | ~ **6,000** words — the most concise of the supported hydrology titles |
| Headings | **NOT numbered** — plain bold headings |
| In-text citation | `(Author Year)` / `Author (Year)` — Harvard, **no comma**, as in HJ |
| Fig caption | Below figure |
| Table caption | Above table |
| Audience | Practitioners **as well as** researchers |

## What differs most from the HJ default

1. **The word budget is roughly 6,000** — about a quarter tighter than HJ. A manuscript
   drafted for HJ will usually need real cutting, not trimming. Say so plainly to the user
   rather than compressing the Methods past the reproducibility standard in
   `references/reproducibility.md`.
2. **Headings lose their numbers.** Plain bold headings only. Rewrite any "see Sect. 3.2"
   cross-reference to name the section instead.
3. **The audience includes practitioners.** This is a register instruction, not a
   formatting one, and it is the defining feature of the title — see below.

## Register: writing for practitioners

Groundwater is read by consulting hydrogeologists and well contractors alongside academics.
That changes the prose without loosening the science:

- Define specialist terminology and every abbreviation on first use, including terms an
  academic hydrogeology audience would take for granted.
- State the practical consequence of a result explicitly. Where an HJ discussion might stop
  at the physical interpretation, add what it means for someone managing or drilling the
  system.
- Keep the mathematics, but carry the reader through it in words as well as symbols.
- Do **not** trade precision for accessibility. Vague plain language is worse than precise
  technical language that has been properly defined. The anti-fabrication and
  anti-AI-style rules apply unchanged.

Citation style otherwise follows HJ closely, so an HJ draft ports here with less citation
rework than to any other journal in this set.

## Citation format (Harvard, no comma)

**In-text:**
- One author: `(Thompson 1990)` or `Thompson (1990)`
- Two authors: `(Kelso and Smith 1998)`
- Three or more: `(Barakat et al. 1995)`
- Multiple citations: alphabetical, semicolon-separated: `(Abbott 1991; Barakat et al. 1995)`

**Reference list entry:**
```
Lastname IN, Lastname2 IN. Year. Title of the paper. Groundwater Vol(Issue):pages. https://doi.org/xx
```

- Initials follow the surname with no punctuation between them (`Burns ER`), as in HJ
- Author block closed with a **full stop**, then the year, then a full stop
- DOI as a full `https://doi.org/...` URL (HJ uses a bare `doi ` prefix — this differs)

## Verifying the format against live papers

```
tool: mcp__semantic-scholar__search_papers
query: "Groundwater NGWA hydrogeology"
fields: paperId,title,authors,year,venue,externalIds
limit: 3
filter: year >= 2022
```

Check `venue` carefully — "Groundwater" is a common word and will match unrelated venues.

## Inherit from the HJ profile

Unless the NGWA author guide says otherwise, follow `references/journal-hydrogeology.md`
for: verb tense by section, equation formatting and numbering, numerals and units,
terminology rules ('groundwater' one word, 'water table' two words), and figure/table
numbering. The register guidance above **overrides** the HJ language section where the two
conflict.

## Pre-submission checklist (Groundwater-specific)

- [ ] Abstract ≤ 250 words
- [ ] Body ~ 6,000 words or under — verify with an actual word count, not an estimate
- [ ] **Zero numbered headings** anywhere in the manuscript
- [ ] In-text citations use `(Author Year)` with **no** comma before the year
- [ ] Reference entries use `Lastname IN, Lastname2 IN. Year. Title. Groundwater Vol(Issue):pages. https://doi.org/xx`
- [ ] Every abbreviation and specialist term defined on first use
- [ ] Practical implications stated explicitly in the Discussion
- [ ] Methods still meet the reproducibility standard despite the tighter word budget
- [ ] Figure captions below figures, table captions above tables
- [ ] Limitations content present (inherit the HJ mandatory-limitations rule)

## Unverified — confirm before submission

- Keyword count
- Whether the target is a full Article, a Research Note, or another category (the ~6,000
  word figure is for the standard concise format — ask which category the user is targeting)
- Data availability and author-contribution statement requirements
- Figure resolution and file-format requirements

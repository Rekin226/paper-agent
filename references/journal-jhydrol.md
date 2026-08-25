# Journal Style — Journal of Hydrology (Elsevier)

Load this file when the user selects `jhydrol` in the startup interview.

> **Not to be confused with** `references/journal-jhrs.md` — *Journal of Hydrology:
> Regional Studies* is a separate Elsevier title with a **structured** abstract (Study
> Region / Study Focus / New Hydrological Insights). This file is the **main** Journal of
> Hydrology, which uses an unstructured abstract. Confirm which one the user means before
> drafting.

> **Provenance.** Ported on 2026-08-25 from the retired project-scoped profile
> (`single_tankV2/.claude/skills/paper-agent/references/journal-styles.md`, committed
> 2026-03-26). Fields that file did not cover are marked *inherit* or listed under
> "Unverified". Do not fill those gaps by guessing, per `anti-fabrication.md`.

## At a glance

| Field | Value |
|---|---|
| Publisher | Elsevier |
| Abstract | ≤ 250 words, unstructured |
| Highlights | **Required** — 3–5 bullets, ≤ 85 characters each |
| Body word limit | ~ 10,000 words |
| Headings | Numbered **with a trailing full stop**: `1.`, `1.1.`, `1.1.1.` |
| In-text citation | `(Author, Year)` — Elsevier Harvard |
| Journal name in refs | Abbreviated **with full stops**: "J. Hydrol.", "Water Resour. Res." |
| Fig caption | Below figure |
| Table caption | Above table |
| CRediT statement | **Required** (author contributions) |

## What differs most from the HJ default

1. **Headings carry a trailing full stop** — `2.1.` not `2.1`. Mechanical, easy to miss,
   and applies at every level.
2. **Highlights are mandatory**, 3–5 bullets at ≤ 85 characters each. Tighter than the AGU
   Key Points limit, so Key Points cannot be reused verbatim.
3. **Citations take a comma before the year** — `(Barakat et al., 1995)`.
4. **Abbreviated journal names use full stops** — "J. Hydrol." — unlike HJ's LTWA style
   ("Hydrogeology J") which omits them.

## Citation format (Elsevier Harvard)

**In-text:**
- One author: `(Thompson, 1990)` or `Thompson (1990)`
- Two authors: `(Kelso and Smith, 1998)`
- Three or more: `(Barakat et al., 1995)`
- Multiple citations: alphabetical, semicolon-separated: `(Abbott, 1991; Barakat et al., 1995)`

**Reference list entry:**
```
Lastname, I.N., Lastname2, I.N., Year. Title of the paper. J. Hydrol. Vol, pages. https://doi.org/xx
```

- Initials without spaces (`I.N.`), comma-separated author list
- Year follows the author block after a comma, **no parentheses**, then a full stop
- Journal abbreviated with full stops
- Alphabetical by first author surname, deduplicated by DOI

## Verifying the format against live papers

```
tool: mcp__semantic-scholar__search_papers
query: "Journal of Hydrology groundwater hydrology"
fields: paperId,title,authors,year,venue,externalIds
limit: 3
filter: year >= 2022
```

Check `venue` carefully — it must read "Journal of Hydrology", not "Journal of Hydrology:
Regional Studies".

## Inherit from the HJ profile

Unless the Elsevier guide for authors says otherwise, follow
`references/journal-hydrogeology.md` for: language and register, verb tense by section,
equation formatting, numerals and units, and figure/table numbering.

For Elsevier back matter and declarations generally, `references/journal-engineering-geology.md`
(also Elsevier) is the closer model — consult it for the declarations block, and flag any
point where you are extrapolating between the two titles.

## Pre-submission checklist (Journal of Hydrology-specific)

- [ ] Highlights present, **3–5 bullets**, each ≤ 85 characters (count including spaces)
- [ ] Abstract ≤ 250 words, unstructured (no Study Region / Study Focus headings — that is JHRS)
- [ ] Body ~ 10,000 words or under
- [ ] Every heading at every level ends with a full stop (`1.`, `2.1.`, `2.1.1.`)
- [ ] Every in-text citation has a comma before the year
- [ ] Reference entries use `Lastname, I.N., Year.` with no parentheses around the year
- [ ] Journal abbreviations use full stops ("J. Hydrol.")
- [ ] CRediT author contribution statement present
- [ ] Figure captions below figures, table captions above tables
- [ ] Limitations content present (inherit the HJ mandatory-limitations rule)

## Unverified — confirm before submission

- Keyword count
- Data Availability statement wording
- Declaration of Competing Interest exact wording
- Graphical abstract requirement
- Figure resolution and file-format requirements

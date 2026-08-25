# Journal style — Engineering Geology (Elsevier, ENGEO, ISSN 0013-7952)

Source: the Engineering Geology *Guide for Authors* at
https://www.sciencedirect.com/journal/engineering-geology/publish/guide-for-authors,
retrieved 2026-08-25, supplemented by Elsevier's journal-wide "Your Paper Your Way"
policy. Rules marked **[EG]** are stated by the journal itself. Rules marked
**[ELS]** are Elsevier house policy that applies to this title. Rules marked
**[UNVERIFIED]** could not be retrieved and MUST be confirmed against the live
guide before submission: do not present them to the user as journal rules.

Where this profile is silent, fall back to `references/manuscript-docx-style.md`.
This profile overrides that baseline wherever they conflict.

Submission portal: https://submit.elsevier.com/ENGEO

---

## Scope gate (check BEFORE drafting)

**[EG]** verbatim:

> "*Engineering Geology* is an international interdisciplinary journal bridging the
> fields of the **earth sciences and engineering**, particularly **geological and
> geotechnical engineering**. The focus of the journal is on geological or engineering
> studies that are of interest to engineering geologists, whether their initial
> training is in geology or civil/mining engineering. The studies published in this
> journal must show relevance to engineering, environmental concerns, and safety."

Sample topics **[EG]**: applied geomorphology and structural geology, applied
geophysics and geochemistry, environmental geology and hydrogeology, land use
planning, natural hazards, remote sensing techniques, soil and rock mechanics and
applied geotechnical engineering.

**The relevance sentence is a hard gate.** EG rejects otherwise-sound geoscience that
does not demonstrate relevance to engineering, environmental concerns, or safety. A
purely descriptive hydrogeological characterisation is out of scope unless the
manuscript states what engineering, environmental, or safety decision it informs.

Before drafting, confirm with the user in one sentence which of the three
(engineering / environmental / safety) the paper speaks to, and make sure the
Introduction states it explicitly. If none applies, say so and recommend a different
journal rather than drafting a paper that will desk-reject.

**Paper types [EG]:** original research articles, case histories, comprehensive
reviews. Case studies in particular "should emphasize why the paper is of interest to
the international readership of this journal, and/or what new or novel research or
theoretical methods are being presented." For a case history, that justification
belongs in the Introduction, not the Conclusions.

---

## Language and register

- Third person throughout. Zero first-person pronouns (per the skill-wide rule).
- Past tense for Methods and what was done; present tense for Results, established
  facts, and what figures/tables show.
- **[ELS]** Inclusive language required. Avoid assumptions about age, gender, race,
  ethnicity, culture, sexual orientation, disability, or health condition.
- Apply `references/anti-ai-style.md` in full.

---

## Document structure

```
Title page  [EG: required fields not retrieved — UNVERIFIED, confirm]
Highlights  [ELS: 3–5 bullets, ≤85 characters each]
Abstract    [EG: must stand alone; NOT included in section numbering]
Keywords    [EG: 1 to 7]
Graphical abstract  [EG: optional, encouraged; separate file]
1.  Introduction
2.  Materials and methods
3.  Results
4.  Discussion
5.  Conclusions
    CRediT author contributions   [EG: required]
    Declaration of competing interests   [EG: required]
    Declaration of generative AI use     [EG: required]
    Funding sources                      [EG: required]
    Data statement / Data availability    [EG: required]
    Acknowledgements
    References
```

**[EG] Section numbering rules, verbatim:**
- "Divide your manuscript into clearly defined and numbered sections. Number
  subsections 1.1 (then 1.1.1, 1.1.2, ...), then 1.2, etc."
- "Use the numbering format when cross-referencing within your article. Do not just
  refer to 'the text.'"
- "You may give subsections a brief heading. Headings should appear on a separate line."
- "Do not include the article abstract within section numbering."

That cross-referencing rule is stricter than most journals. Every internal pointer
must name a number ("as described in Section 3.2"), never "as described above" or
"see the text". Enforce this in Draft, Revise, and Audit modes.

The Results/Discussion split is not mandated by the guide; a combined "Results and
discussion" section is acceptable in EG practice. Ask the user which they want rather
than assuming.

---

## Abstract

**[EG]** verbatim:
- "Abstracts must be able to stand alone as abstracts are often presented separately
  from the article."
- "Avoid references. If any are essential to include, ensure that you cite the
  author(s) and year(s)." Note this is *avoid*, not *forbid*: unlike HJ, a citation in
  the EG abstract is permitted when genuinely essential, and **[EG]** adds that
  "references cited in your abstract must be given in full."
- "Avoid non-standard or uncommon abbreviations. If any are essential to include,
  ensure they are defined within your abstract at first mention."

**[ELS]** A concise and factual abstract stating the purpose of the research, the
principal results, and the major conclusions.

**Word limit: [UNVERIFIED].** The guide did not state one in the retrieved text.
Third-party template sites suggest roughly 250 words, which is the common Elsevier
default, but that is not a journal statement. Draft to ~250 words, flag the figure as
unconfirmed, and tell the user to check the live guide.

Unstructured single paragraph. EG does **not** use the JHRS labelled Study Region /
Study Focus / New Hydrological Insights format. Do not carry that structure over.

---

## Keywords

**[EG]** verbatim: "You are required to provide 1 to 7 keywords for indexing purposes.
Keywords should be written in English. Please try to avoid keywords consisting of
multiple words (using 'and' or 'of'). We recommend that you only use abbreviations in
keywords if they are firmly established in the field."

---

## Highlights

**[ELS]** 3–5 bullet points, each ≤85 characters including spaces. The EG guide
"encourages" highlights and links Elsevier's example page; it does not restate the
count and character cap, so those come from Elsevier house policy **[ELS]**, which is
what the submission system enforces.

Each highlight must be a concrete finding, not a vague statement of activity.

---

## Graphical abstract

**[EG]** Optional but encouraged. Submit as a separate file.
- Minimum 531 × 1328 pixels (h × w), or proportionally more.
- Must be readable at 5 × 13 cm at 96 dpi.
- Preferred file types: TIFF, EPS, PDF, or MS Office files.

---

## Citation format (Elsevier author-year, not numeric)

**[EG]** verbatim rules:
- Single author: the author's name (without initials, unless there is ambiguity) and
  the year of publication.
- Two authors: both authors' names and the year of publication.
- Three or more authors: first author's name followed by 'et al.' and the year.
- Citations can be made directly or parenthetically.
- Groups of references can be listed either first alphabetically then chronologically,
  or vice versa.

**[EG]** examples, verbatim:
> "as demonstrated (Allan, 2020a, 2020b; Allan and Jones, 2019)"
> "as demonstrated (Jones, 2019; Allan, 2020). Kramer et al. (2023) have recently shown"

Note EG uses a **comma before the year** (`Allan, 2020`), matching JHRS/Elsevier and
differing from Hydrogeology Journal's `Allan 2020`.

**Reference list [EG]:**
- Arranged alphabetically, then chronologically if necessary.
- More than one reference from the same author(s) in the same year is identified by
  'a', 'b', 'c' placed after the year.
- Abbreviate journal names per the LTWA (https://portal.issn.org/ltwa).

**[EG]** Book example, verbatim:
```
Strunk Jr., W., White, E.B., 2000. The Elements of Style, fourth ed. Longman, New York.
```

**[EG] Reference formatting at submission is relaxed:** "This journal does not set
strict requirements on reference formatting at submission... Our journal reference
style will be applied to your article after acceptance, at proof stage." This is
Elsevier's "Your Paper Your Way". Author, title, year, volume, and pages/article
number must all be present and the style must be internally consistent, but a
submission is not desk-rejected over punctuation. Still produce a clean, consistent
list: it is what the reviewers read.

**[EG]** Unpublished results and personal communications follow the journal's standard
reference style, substituting "unpublished results" or "personal communication" for
the publication date.

---

## Back matter (all required)

**[EG] CRediT author contributions.** Corresponding authors are required to
acknowledge co-author contributions using CRediT roles. The full taxonomy:
Conceptualization, Data curation, Formal analysis, Funding acquisition,
Investigation, Methodology, Project administration, Resources, Software, Supervision,
Validation, Visualization, Writing – original draft, Writing – review and editing.
Not every role applies to every manuscript, and one author may hold several.

**[EG] Declaration of competing interests.** Required. Covers employment,
consultancies, stock ownership, honoraria, paid expert testimony, patent applications
or registrations, grants or other funding, and affiliation with the journal as an
Editor or Advisory Board Member.

**[EG] Declaration of generative AI use.** Required. Authors must declare the use of
generative AI tools in the manuscript preparation process at submission, per
Elsevier's GenAI Policies for Journals.

**Relevant to this skill:** a manuscript drafted with `paper-agent` needs this
declaration. Raise it with the user at export time. State plainly that AI assistance
was used in drafting and that the authors reviewed and take responsibility for the
content. Do not draft a declaration that understates the tool's role.

**[EG] Generative AI in figures.** "Authors are responsible for ensuring the accuracy
and originality of all images submitted for publication. If you used generative AI
tools to create images in your manuscript, you should disclose this in each image
caption as well as in the general Generative AI disclosure statement." Plotting real
data with matplotlib is not generative AI image creation and needs no caption
disclosure.

**[EG] Funding sources.** Required, with grant numbers.

**[EG] Data statement and data linking.** Provide a link to the dataset when prompted
during submission. Entities can be linked in text using `Database: identifier` format
(e.g. `TAIR: AT1G01020`). Per `references/reproducibility.md`, a bare "available upon
request" is not acceptable.

---

## Figures, tables, equations

Numbering and caption placement follow `references/manuscript-docx-style.md`
(figure caption below, table caption above, sequential numbering, no gaps).

**Figure resolution and file-format requirements: [UNVERIFIED].** The specifics were
not retrieved. Elsevier's general artwork standard is 300 dpi for halftones, 1000 dpi
for line art, and 500 dpi for combination art, saved as TIFF or EPS, but confirm
against the live guide before final export rather than asserting these as EG rules.

The skill-wide figure necessity assessment and the 6-figure cap in `SKILL.md` still
apply. EG publishes figure-heavy case histories, which makes the cap easier to breach
and more important to hold.

---

## Pre-submission checklist (EG-specific)

- [ ] **Scope gate passed:** the manuscript states its relevance to engineering,
      environmental concerns, or safety, explicitly, in the Introduction
- [ ] For a case history: the Introduction states why it interests an international
      readership, or what novel method it presents
- [ ] Sections numbered; subsections as 1.1, 1.1.1, 1.2
- [ ] Abstract NOT included in the section numbering
- [ ] Every internal cross-reference names a section number, never "above" or "the text"
- [ ] Abstract stands alone; abbreviations defined at first mention in the abstract
- [ ] Any reference cited in the abstract is given in full
- [ ] Abstract word count checked against the live guide (limit UNVERIFIED here)
- [ ] Keywords: 1 to 7, English, single words where possible
- [ ] Highlights: 3–5 bullets, each ≤85 characters
- [ ] In-text citations use a comma before the year (`Allan, 2020`)
- [ ] Three or more authors abbreviated to `et al.`
- [ ] Reference list alphabetical, then chronological; same-year duplicates get a/b/c
- [ ] Journal names abbreviated per LTWA
- [ ] Reference list internally consistent and complete (author, title, year, volume,
      pages or article number)
- [ ] CRediT statement present, using only the 14 official role names
- [ ] Declaration of competing interests present
- [ ] **Declaration of generative AI use present** (required if this skill drafted it)
- [ ] Funding sources with grant numbers
- [ ] Data statement present and specific, not "available upon request"
- [ ] Zero first-person pronouns
- [ ] Every UNVERIFIED item above confirmed against the live guide, or flagged to the
      user as unconfirmed

---

## Export details for .docx

Follow `references/manuscript-docx-style.md`. EG-specific notes:
- Single column, numbered sections via Heading1/Heading2/Heading3 styles so the
  decimal numbering survives.
- Graphical abstract is a **separate file**, never embedded in the manuscript .docx.
- Highlights go in a separate file or the dedicated submission-system field, not the
  manuscript body. Confirm placement with the user at export time.
- Elsevier accepts a single-file submission for initial review ("Your Paper Your Way"),
  so figures and tables may sit inline in the .docx for the first submission.

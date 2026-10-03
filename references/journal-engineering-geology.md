# Journal style — Engineering Geology (Elsevier, ENGEO, ISSN 0013-7952)

Source: the Engineering Geology *Guide for Authors* at
https://www.sciencedirect.com/journal/engineering-geology/publish/guide-for-authors,
retrieved 2026-08-25, supplemented by Elsevier's journal-wide "Your Paper Your Way"
policy. Rules marked **[EG]** are stated by the journal itself. Rules marked
**[ELS]** are Elsevier house policy that applies to this title. Rules marked
**[UNVERIFIED]** could not be retrieved and MUST be confirmed against the live
guide before submission: do not present them to the user as journal rules.

**Retrieval note.** ScienceDirect serves a Cloudflare block page to headless
browsers, so `gstack /browse`, `curl`, and `pandoc` cannot fetch this guide. The
2026-08-25 pass that filled in the abstract limit, title-page fields, artwork specs,
file-format rules, and table rules used an authenticated desktop Chrome session
(`mcp__claude-in-chrome__*`). If a future session needs to re-verify, go straight to
a real browser instead of burning calls on headless fetches that return
`CLOUDFLARE_ERROR_1000S_BOX`.

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
Title page  [EG: required fields — see the Title page section below]
Highlights  [EG: required at submission; 3–5 bullets, ≤85 characters each]
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

**[EG] Acknowledgements placement**, verbatim: "Acknowledgements should be placed in
a separate section which appears **directly before the reference list**. Do not
include acknowledgements on your title page, as a footnote to your title, or anywhere
else in your article other than in the separate acknowledgements section." This fixes
the order of the back matter: every other declaration comes first, Acknowledgements
last before References.

**[EG] Theory and calculation.** Where a manuscript has them, "the theory section
should lay the foundation for further work by extending the background you provided in
the introduction", and "the calculation section should represent a practical
development from a theoretical basis."

That cross-referencing rule is stricter than most journals. Every internal pointer
must name a number ("as described in Section 3.2"), never "as described above" or
"see the text". Enforce this in Draft, Revise, and Audit modes.

The Results/Discussion split is not mandated by the guide; a combined "Results and
discussion" section is acceptable in EG practice. Ask the user which they want rather
than assuming.

---

## File format

**[EG]** verbatim requirements:
- "Save files in an editable format, using the extension .doc/.docx for Word files and
  .tex for LaTeX files. **A PDF is not an acceptable source file.**"
- "Format Word files in a **single-column layout**. Double-column formatting is only
  permitted for LaTeX submissions."
- "Remove any strikethrough and underlined text from your manuscript, unless it has
  scientific significance related to your article."
- Run spell-check and grammar-check.

Editable source files are required for the *entire* submission, including figures,
tables and text graphics.

---

## Title page

**[EG]** The following are required on the title page:

- **Article title.** "Article titles should be concise and informative. Please avoid
  abbreviations and formulae, where possible, unless they are established and widely
  understood, e.g. DNA." Judgement call for domain abbreviations: GNSS, InSAR and
  similar are established in this readership, but flag the choice to the user rather
  than deciding silently.
- **Author names.** Given name(s) and family name(s) of each author. The order must
  match the order in the submission system. Authors may add their name in their own
  script in parentheses after the English transliteration.
- **Affiliations**, below the author names, "referring to where the work was carried
  out". Indicate with a **lower-case superscript letter** immediately after the
  author's name and in front of the corresponding address. "Ensure that you provide
  the full name and postal address of each affiliation, **including the country
  name**."
- **Corresponding author**, clearly indicated. "The email address of the
  corresponding author must be included on the title page and will be included in the
  published article."
- **Present/permanent address**, where an author has changed affiliation, as a
  footnote to the author's name using **superscript Arabic numerals**. The address
  where the work was carried out stays as the main affiliation.

Note the two different superscript systems: **letters** for affiliations, **Arabic
numerals** for present-address footnotes. A manuscript that numbers its affiliations
is not following this rule.

A postcode is **not** required. "Full postal address ... including the country name"
is satisfied by street, district, city and country; do not invent a postcode or block
an export waiting for one.

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

**Word limit: 250 words. [EG]** verbatim: "You are required to provide a concise and
factual abstract which **does not exceed 250 words**. The abstract should briefly
state the purpose of your research, principal results and major conclusions." This is
a hard cap, not a convention.

Count the way Word does, **whitespace-delimited tokens**, because that is what an
editor checks. A `\w+` regex over the same text inflates the count by 5–8% on a
quantitative abstract by splitting subscripts, hyphenated compounds and numbers like
`1.5–3.4 × 10⁻⁵`; `scripts/extract_docx.py` reports the inflated figure, so verify a
borderline abstract with `len(text.split())` before cutting content.

When adding required framing pushes an abstract over 250, cut the least-resolved
result rather than the framing, but say which result was cut and why.

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

**[EG]** verbatim: "You are **required** to provide article highlights at
submission." and "Highlights should consist of **3 to 5 bullet points, each a maximum
of 85 characters, including spaces**." Highlights are mandatory for EG, not
encouraged, and the cap is stated by the journal.

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

**[EG] Tables**, verbatim:
- "Place tables next to the relevant text or on a separate page(s) at the end of your
  article."
- "Cite all tables in the manuscript text."
- "Number tables consecutively according to their appearance in the text."
- "Please provide captions along with the tables."
- "Place any table notes below the table body."
- "**Avoid vertical rules and shading within table cells.**" (Consistent with the
  booktabs three-rule style in `manuscript-docx-style.md`.)
- "We recommend that you use tables sparingly, ensuring that any data presented in
  tables is not duplicating results described elsewhere in the article." 

**[EG] Artwork must be supplied as separate files** alongside the manuscript, each
image its own file, "using a logical naming convention for your files (for example,
Figure_1, Figure_2 etc)". Text graphics may be embedded in the text at the
appropriate position.

**[EG] Formats and resolution**, verbatim:

| Artwork type | Format | Minimum | Single column | Full page |
|---|---|---|---|---|
| **Vector drawings** | **EPS or PDF**, "embedding the font or saving the text as 'graphics'" | n/a | n/a | n/a |
| Colour/greyscale photographs (halftones) | TIFF, JPG, PNG | 300 dpi | 1063 px | 2244 px |
| Bitmapped line drawings | TIFF, JPG, PNG | 1000 dpi | 3543 px | 7480 px |
| Combination line/halftone | TIFF, JPG, PNG | 500 dpi | 1772 px | 3740 px |

**The 300 dpi tier applies to photographs only.** This is the single most common
mistake: a matplotlib figure exported at "300 dpi TIFF, publication quality" is *not*
compliant, because it is line art or combination art and needs 1000 or 500 dpi.

**Prefer the vector route.** Matplotlib, R and most plotting stacks are vector-native,
so exporting **PDF with fonts embedded** (`plt.rcParams["pdf.fonttype"] = 42`)
satisfies the rule outright and sidesteps every pixel threshold. Recommend this before
re-rastering at higher dpi. A colourbar gradient or a basemap tile will still appear
as an embedded raster inside an otherwise-vector PDF; that is expected and fine.

**[EG] Do not submit:**
- "Files that are too low in resolution."
- "Artwork where text is disproportionately small compared to the image size, as text
  may become unreadable."
- "Different images or graphs combined into one, as this affects accessibility." Read
  this as barring composites of *unrelated* images. EG publishes multi-panel figures
  routinely, so do not tell a user to split a legitimate (a)/(b) panel pair, but do
  flag a figure that staples unrelated graphics together.

**[EG] Captions.** "All artwork must have a caption. A caption should consist of a
brief title (**not displayed on the figure itself**) and a description of the image.
Keep the amount of text in any image to a minimum, though any symbol or abbreviation
should be explained." A title duplicated inside the figure image is a finding.

**[EG] Colour.** Colour figures appear in colour online at no charge; print colour is
quoted after acceptance. "Please ensure that color images are accessible to all,
including those with impaired color vision." Prefer perceptually-uniform,
colourblind-safe maps (viridis, cividis) and encode a second channel with **shape or
pattern**, not colour alone.

The skill-wide figure necessity assessment and the 6-figure cap in `SKILL.md` still
apply. EG publishes figure-heavy case histories, which makes the cap easier to breach
and more important to hold.

---

## Submission format — enforced by the editorial office, absent from the guide

**Verified 2026-09-11 by a desk return.** A manuscript was returned by
Engineering Geology before peer review with this notice:

> "the continuous line numbers are not provided, the page numbers are missing,
> the text is not double-spaced, or the highlights are not provided as required"

A live search of the Engineering Geology guide for authors on the same day
returns **zero matches** for "line number", "page number", "line spacing" and
"double-spac". All three are required and none of them is stated on that page.
They are checked by an editorial assistant before a reviewer is invited.

Required for every EG submission:

| Item | Requirement |
|---|---|
| Continuous line numbers | Every line, restart `continuous`, across the whole document |
| Page numbers | `PAGE` field in the footer |
| Line spacing | Double throughout the body; table cells may stay single |
| Columns | Single column for Word; two columns permitted only for LaTeX |
| Source file | `.doc` / `.docx` / `.tex`; a PDF is never acceptable |
| Markup | No strikethrough, no underline, no live tracked changes |

Apply and verify with the bundled scripts, on the exact file to be uploaded:

```bash
"$SKILL_DIR/.venv/bin/python" "$SKILL_DIR/scripts/apply_submission_format.py" manuscript_eg.docx
"$SKILL_DIR/.venv/bin/python" "$SKILL_DIR/scripts/validate_docx.py" manuscript_eg.docx --font "Times New Roman"
```

Where the manuscript is generated by a build script, put line numbers and page
numbers in that script rather than patching the output, so a rebuild cannot
silently drop them.

**Highlights are a separate uploaded file.** The guide is explicit: "Submit
highlights as a separate editable file in the online submission system with the
word 'highlights' included in the file name." A highlights block inside the
manuscript body does not satisfy this, and a `.txt` is a weak reading of
"editable file" — ship a `.docx`. Whether the file was actually attached in
Editorial Manager, and under which item type, is invisible from the filesystem.
**Ask the user; never assume.**

```bash
"$SKILL_DIR/.venv/bin/python" "$SKILL_DIR/scripts/make_highlights_docx.py" highlights.txt \
  -o highlights.docx --max-chars 85 --min 3 --max 5
```

See `references/submission-format.md` for the general rule behind this section.

#### Highlights rules (verified 2026-09-11 on elsevier.com/researcher/author/tools-and-resources/highlights)

- **Word document**, uploaded under the "Highlights" item type. Not a .txt.
- 3 to 5 bullets, each **85 characters or fewer including spaces**.
- Verbatim: "**No jargon, acronyms, or abbreviations: aim for a general audience and
  use keywords.**" Spell out or replace every acronym, even a field-standard one.
- Write numbers in publication notation. `1.5-3.4e-5` is computer notation; use
  `1.5\u20133.4 \u00d7 10\u207b\u2075`, with an en dash for the range.
- Both worked examples Elsevier publishes are **entirely qualitative, with no numbers**.
  Numbers are permitted and are not a violation, but highlights exist for search
  discoverability, so keywords earn their place more than figures do.
- Conflict to be aware of: the general Elsevier page says highlights are "not part of
  editorial consideration and not required until the final files stage", but the
  Engineering Geology guide says "You are **required** to provide article highlights at
  submission", and a 2026-09-11 desk return named missing highlights. **The journal guide
  wins.** Supply them at submission.
- `scripts/make_highlights_docx.py` enforces the count and character caps and warns on
  acronyms, computer notation, and hyphenated numeric ranges.

---

## Pre-submission checklist (EG-specific)

- [ ] **Continuous line numbers present** (desk-return cause; not stated in the guide)
- [ ] **Page numbers present** as a footer field (desk-return cause; not stated in the guide)
- [ ] **Body text double-spaced** (desk-return cause; not stated in the guide)
- [ ] **Highlights uploaded as a separate editable .docx** with "highlights" in the file
      name — confirmed with the user, not inferred from a file on disk (desk-return cause)
- [ ] `scripts/validate_docx.py` run on the exact file to be uploaded, output shown verbatim
- [ ] **Scope gate passed:** the manuscript states its relevance to engineering,
      environmental concerns, or safety, explicitly, in the Introduction
- [ ] For a case history: the Introduction states why it interests an international
      readership, or what novel method it presents
- [ ] Sections numbered; subsections as 1.1, 1.1.1, 1.2
- [ ] Abstract NOT included in the section numbering
- [ ] Every internal cross-reference names a section number, never "above" or "the text"
- [ ] Abstract stands alone; abbreviations defined at first mention in the abstract
- [ ] Any reference cited in the abstract is given in full
- [ ] Abstract ≤ 250 words, counted as whitespace tokens (Word-style), not by `\w+` regex
- [ ] Keywords: 1 to 7, English, single words where possible
- [ ] Highlights present (REQUIRED at submission): 3–5 bullets, each ≤85 characters
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
- [ ] Title page: affiliations use **lower-case superscript letters**, each with full
      postal address **including country**; corresponding author's email present
- [ ] Present/permanent-address footnotes use superscript **Arabic numerals**
- [ ] Source file is .doc/.docx or .tex (never PDF), Word in single-column layout
- [ ] No strikethrough or underlined text left in the manuscript
- [ ] Artwork supplied as **separate files** named Figure_1, Figure_2, ...
- [ ] Figures meet the tier that applies: vector PDF/EPS preferred; 1000 dpi line art;
      500 dpi combination; 300 dpi is for photographs ONLY
- [ ] No figure caption title duplicated inside the figure image
- [ ] Colour figures readable with impaired colour vision; second channel is shape or
      pattern, not colour alone
- [ ] Tables carry no vertical rules or cell shading; notes sit below the table body
- [ ] Acknowledgements sit directly before the reference list, nowhere else
- [ ] No rule in this profile currently carries [UNVERIFIED]. If one is added later,
      confirm it against the live guide (real browser, not headless) or flag it to the
      user as unconfirmed rather than presenting it as a journal rule

---

## Export details for .docx

Follow `references/manuscript-docx-style.md`. EG-specific notes:
- Single column, numbered sections via Heading1/Heading2/Heading3 styles so the
  decimal numbering survives.
- Graphical abstract is a **separate file**, never embedded in the manuscript .docx.
- Highlights go in a separate editable .docx, never the manuscript body. Build it with
  `scripts/make_highlights_docx.py` and confirm with the user that it was uploaded.
- Continuous line numbers, footer page numbers and double spacing are mandatory and are
  not mentioned in the guide. See the submission-format section above.
- **"Your Paper Your Way" is NOT offered by this journal.** Verified 2026-09-11 against
  the live guide: the phrase returns zero matches on the page. Do not tell the user that
  relaxed first-submission formatting applies to Engineering Geology.
- **Figures are uploaded separately and taken OUT of the manuscript file; their captions
  are listed at the end of the manuscript instead.** The EG guide page alone does not
  settle this, but the Elsevier artwork FAQ it links to does, verbatim (verified
  2026-09-11):
  > "Should my figures be included in my manuscript file when submitting in the submission
  > system? **We prefer if you upload your figures separately to your manuscript. When our
  > system converts your paper to PDF for the review process it will include your figures
  > at the end of the PDF file.**"

  and on captions:
  > "If the journal provides for a submission item type called 'Figure Caption', submit
  > your caption here in the form of a text file. **If there is no submission item type
  > provided for 'Figure Caption', you should list your figure captions at the end of your
  > manuscript text file.**"

  So: strip the images from the .docx, keep every in-text `Fig. N` citation, and append a
  `Figure captions` section after the references. Ask the user whether Editorial Manager
  offers a "Figure Caption" item type; if it does, the captions go there instead.
  LaTeX is the exception the FAQ names: separately uploaded EPS files may be embedded in
  the source.
- **Tables stay in the manuscript.** The guide gives tables a choice the figures do not
  get: "Place tables next to the relevant text or on a separate page(s) at the end of your
  article." Inline is fine; do not move them without a reason.
- Validate this arrangement with `scripts/validate_docx.py --figures-separate`, which
  then requires the captions to be present and the embedded images to be absent.

### Artwork specifications (verified 2026-09-11 on Elsevier's artwork instructions)

Source: elsevier.com/about/policies-and-standards/author/artwork-and-media-instructions,
the page the EG guide links to as "artwork and media instructions".

- **Fonts.** Only Arial (or Helvetica), Courier, Symbol, and Times (or Times New Roman)
  are recommended. Verbatim: "If your artwork contains other, non-standard fonts, Elsevier
  may substitute these fonts with an Elsevier standard font (to match the style of the
  journal), and that may lead to problems such as missing symbols or overlapping type."
  **matplotlib defaults to DejaVu Sans for mathtext even when the base font is Times**, so
  a figure can embed DejaVu without the author noticing. Set `mathtext.fontset` to a Times
  variant, or `mathtext.fontset = "custom"` with the math families pointed at the body
  font, and verify by listing the embedded BaseFonts in the output PDF.
- **Standard column widths:** minimal 30 mm, single column 90 mm, 1.5 column 140 mm,
  double column (full width) 190 mm. Size artwork to one of these so production does not
  rescale it, since rescaling changes the effective lettering size.
- **Lettering:** finished printed size 7 pt for normal text, no smaller than 6 pt for
  subscripts and superscripts. Check this AFTER applying the scale factor from the native
  figure width to the nearest standard column width.
- **Resolution** (only when supplying raster): 1000 dpi for graphs and line art, 500 dpi
  for others, 300 dpi for photographs. Vector PDF or EPS sidesteps the pixel thresholds
  entirely and is the preferred route for plotted figures.
- **Check every figure for edge clipping.** `bbox_inches="tight"` does not always capture
  rotated or outer axis labels. Test by sampling the outermost row and column of the
  rendered raster: any non-white pixel on an edge means content is cropped.

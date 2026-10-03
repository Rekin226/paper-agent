# Submission format — the presentation layer that desk-returns manuscripts

Read this before telling any user their manuscript is ready to submit, and
before every `.docx` export. It is short because it has to be obeyed every time.

---

## The governing rule

**Silence in a journal's guide for authors is not evidence that nothing is
required.**

Public author guides describe the *article*: structure, abstract, citation
style, figure resolution, declarations. The *submission presentation* that
peer review depends on (line numbers, page numbers, line spacing) is usually
enforced at the editorial-office quality-control step and is often stated
nowhere on the guide page. An editorial assistant checks it before a reviewer
is ever invited, and returns the manuscript unreviewed if it fails.

A manuscript can be fully compliant with every rule the guide states and still
be returned before review. That is the failure this file exists to prevent.

**Worked example, verified 2026-09-11.** A manuscript submitted to Engineering
Geology was returned pre-review for missing continuous line numbers and page
numbers. A live search of the Engineering Geology guide for authors returns
**zero matches** for "line number", "page number", "line spacing" and
"double-spac". Both requirements are real and neither is on the page.

---

## Never say this

> "The format meets the journal requirements."

That sentence conflates two separate things and is the exact claim that failed:

| Layer | What it covers | How it is checked |
|---|---|---|
| **Article style** | structure, abstract, citations, references, declarations, figures | the journal profile checklist |
| **Submission presentation** | line numbers, page numbers, spacing, columns, file format, separate files | this file + `scripts/validate_docx.py` |

Report the two separately, and name which one you actually verified. If you
have not run the validator on the final file, you have not verified either.

---

## Universal baseline

Apply all of these unless the journal's own guide contradicts a specific line.
Contradiction means the guide states a different rule, not that it is silent.

| # | Requirement | Default | Notes |
|---|---|---|---|
| 1 | Continuous line numbers | every line, restart `continuous` | Restarting per page is a different thing and some offices reject it. |
| 2 | Page numbers | centred `PAGE` field in the footer | Must be a field, not typed digits. |
| 3 | Line spacing | double (2.0) on body text | Table cells and footer stay single; that is normal and not a failure. |
| 4 | Columns | single column | Two-column Word files are rejected by Elsevier. LaTeX is exempt. |
| 5 | Source file | `.doc` / `.docx` / `.tex` | A PDF is never an acceptable source file. |
| 6 | Markup | no strikethrough, no underline, no tracked changes left on | Accept or reject everything before export. |
| 7 | Highlights | separate **editable** file, "highlights" in the file name | See below. A `.txt` is a weak reading of "editable". Ship `.docx`. |
| 8 | Graphical abstract | separate file, never embedded in the manuscript | Only where the journal offers one. |

Anonymised or double-blind submissions add their own rules. Ask; do not assume.

---

## Highlights are a separate file, and that is where they get lost

Where a journal requires highlights, they are a **separate uploaded file with a
distinct item type in the submission system**, not a section of the manuscript.
A correct highlights block sitting inside the manuscript body still counts as
"highlights not provided".

Three failure points, all of which must be checked:

1. **Content.** Bullet count and the per-bullet character cap, spaces included.
2. **File.** An editable Word file whose name contains "highlights".
3. **Upload.** Actually attached in the submission system under the highlights
   item type. **You cannot verify this from the filesystem. Ask the user, every
   time.** A file sitting in the working directory is not a submitted file.

Build the file with the bundled script, which enforces 1 and warns on 2:

```bash
"$SKILL_DIR/.venv/bin/python" "$SKILL_DIR/scripts/make_highlights_docx.py" highlights.txt \
  -o highlights.docx --max-chars 85 --min 3 --max 5
```

---

## Figure placement: follow the link, do not reason from the guide's silence

Most journal guides say artwork "must be supplied as separate files" and then say nothing
about whether the manuscript file should also contain the images. That silence invites a
wrong inference in either direction. Resolve it from the publisher's artwork policy, which
the guide links to, not from the guide page alone.

**Elsevier, verified 2026-09-11** on the artwork FAQ linked from the guide:

> "Should my figures be included in my manuscript file when submitting in the submission
> system? **We prefer if you upload your figures separately to your manuscript. When our
> system converts your paper to PDF for the review process it will include your figures at
> the end of the PDF file.**"

> "If the journal provides for a submission item type called 'Figure Caption', submit your
> caption here in the form of a text file. **If there is no submission item type provided
> for 'Figure Caption', you should list your figure captions at the end of your manuscript
> text file.**"

So for an Elsevier submission the correct shape is:

1. Images **removed** from the manuscript file.
2. Every in-text `Fig. N` citation left exactly as it is.
3. A `Figure captions` section appended after the references.
4. The image files uploaded separately, named Figure_1, Figure_2, and so on.
5. Tables left inline, unless the journal says otherwise. Elsevier gives tables an explicit
   choice ("next to the relevant text or on a separate page(s) at the end") that figures do
   not get.

LaTeX is the stated exception: separately uploaded EPS files may be embedded in the source.

Ask the user whether the submission system offers a "Figure Caption" item type, since that
changes where the captions belong and cannot be checked from here.

Validate with `scripts/validate_docx.py --figures-separate`, which inverts the embedded-image
check: captions must be present, images must be absent.

**The general lesson.** When a guide is silent on a submission-shape question, the answer is
usually one link away on the publisher's own policy pages. Follow the link. An inference
drawn from what the guide does not say is not a fact, and must not be reported as one.

---

## Applying and checking

Stamp presentation onto any existing `.docx`. Idempotent, and it rewrites
presentation only, so it is safe on a final manuscript:

```bash
"$SKILL_DIR/.venv/bin/python" "$SKILL_DIR/scripts/apply_submission_format.py" MS.docx
"$SKILL_DIR/.venv/bin/python" "$SKILL_DIR/scripts/apply_submission_format.py" MS.docx -o MS_formatted.docx
"$SKILL_DIR/.venv/bin/python" "$SKILL_DIR/scripts/apply_submission_format.py" MS.docx --spacing 1.5
```

Then verify. `validate_docx.py` checks all four presentation items (line
numbers, page numbers, body spacing, columns) alongside the style checks:

```bash
"$SKILL_DIR/.venv/bin/python" "$SKILL_DIR/scripts/validate_docx.py" MS.docx --font "Times New Roman"
```

Flags: `--spacing` sets the required multiple, `--body-pt` calibrates
exact-rule spacing, `--skip-submission-format` disables the four checks for a
journal that genuinely forbids them. Prove the exemption before using it.

**Always re-run the validator on the exact file that will be uploaded.** A
build script that is supposed to add line numbers is not evidence that the file
on disk has them.

### Preferred order of operations

Put the requirement in the **build pipeline**, not in a post-hoc patch, whenever
the manuscript is generated from source. A patched file is correct once; a
patched build script is correct every rebuild. Use
`apply_submission_format.py` for a manuscript you did not build, or when a
rebuild would risk changing text.

After any rebuild, diff the extracted text against the previous file and confirm
the word count and text hash are unchanged before shipping. Presentation fixes
must never move a word.

---

## Journal-specific status

Verified means checked against the live guide or against real editorial-office
correspondence, with the date given. Everything else takes the baseline.

| Journal | Status |
|---|---|
| Engineering Geology | **Verified 2026-09-11 by desk return.** Line numbers and page numbers required; absent from the public guide. Double spacing requested in the same notice. Highlights required, separate editable file, 3–5 bullets, ≤85 characters. |
| All others in this skill | Baseline applies. Not independently verified. Say so to the user rather than implying the journal states it. |

Adding a row requires evidence: a quote from the live guide, or correspondence
from the editorial office. Do not populate this table from memory. When you add
one, record the date and the source in the row.

---

## What to report to the user

At export, and any time the user asks whether the manuscript is ready, give
both layers and the validator's own words:

```
Article style     : <journal> profile, N/N checklist items  (or the open items)
Submission format : line numbers / page numbers / spacing / columns  <validator result>
Separate files    : highlights <state>, graphical abstract <state>, ESM <state>
Cannot verify     : whether the separate files were uploaded in the system
```

The last line is not optional. Upload state is invisible from here, and it is
one of the four things editorial offices return manuscripts for.

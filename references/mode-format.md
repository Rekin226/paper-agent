# Mode — Format

Bring an existing `.docx` to submission-ready presentation for a named journal,
and produce the separate files the submission system asks for. Outputs a
reformatted `.docx`, any missing companion files, and a two-layer compliance
report. **No language edits, no scientific changes, no restructuring.**

Read `references/submission-format.md` first. It carries the governing rule and
the baseline this mode enforces.

## Why this mode exists

A manuscript that satisfies every rule in a journal's guide for authors can
still be returned before peer review, because the presentation requirements the
editorial office enforces are frequently absent from that guide. Format mode is
the pass that catches what the style checklist structurally cannot see.

## Scope

The agent **may** change:
- Line numbering, page numbering, line spacing, column count
- Margins, page size, body font and size
- Heading styles, so decimal numbering survives
- Table width and rule style, per the journal profile
- Image sizing to the text width
- Strikethrough and underline left in the text, and lingering tracked changes
- File format (`.doc` → `.docx`), and file names

The agent **may also create**, as separate files:
- The highlights file
- A title page file, where the journal wants it separated
- A blinded copy, where the journal requires double-blind review

The agent **may not**:
- Change any word of the manuscript text
- Add, remove, or reorder sentences, paragraphs, sections, or references
- Renumber figures, tables, or equations, or move them
- Fix grammar, style, terminology, or citation format (that is Proofread mode)
- Fix factual or numerical inconsistencies (that is Audit, then Revise)

Anything out of scope is **flagged at the end of the report**, never fixed. Say
which mode handles it.

## Procedure

1. **Extract and report** per SKILL.md → "Reading existing manuscripts". The
   user confirms before anything is written.

2. **Load the journal profile** and read its submission-format section. Read
   `references/submission-format.md` alongside it.

3. **Diagnose before changing anything.** Run the validator on the file as it
   stands and show the user the result verbatim:
   ```bash
   "$SKILL_DIR/.venv/bin/python" "$SKILL_DIR/scripts/validate_docx.py" MS.docx --font "<journal font>"
   ```
   Name every FAIL. Do not summarise it as "some formatting issues".

4. **Choose where the fix belongs.**
   - The manuscript is built from source (Markdown, LaTeX, a build script):
     **patch the build script**, then rebuild. A patched file is correct once;
     a patched pipeline is correct every rebuild.
   - No build pipeline, or a rebuild would risk changing text: stamp the file
     directly.
   ```bash
   "$SKILL_DIR/.venv/bin/python" "$SKILL_DIR/scripts/apply_submission_format.py" MS.docx
   ```
   Back up the original first. The script writes a `.bak` when editing in place.

5. **Prove that nothing moved.** After any rebuild or stamp, extract the text
   from the old and new files and compare word count and text hash. A
   presentation fix that changes a word is a failed fix. Report the comparison.

6. **Settle figure placement from the publisher's artwork policy, not the guide page.**
   For Elsevier this means images out of the .docx, in-text `Fig. N` citations kept, and a
   `Figure captions` section after the references. See the figure-placement section of
   `references/submission-format.md` for the verbatim source. Then validate with
   `--figures-separate`, which requires captions present and images absent.

7. **Build the separate files.** Highlights where required:
   ```bash
   "$SKILL_DIR/.venv/bin/python" "$SKILL_DIR/scripts/make_highlights_docx.py" highlights.txt \
     -o highlights.docx --max-chars <cap> --min <lo> --max <hi>
   ```
   Never invent highlight text. If the manuscript has no highlights, say so and
   ask the user to supply them, or offer to draft candidates from the abstract
   for their approval.

8. **Re-validate the exact file that will be uploaded**, and show the output.

9. **Ask about upload state.** Which separate files are already attached in the
   submission system, and under which item type. This is invisible from the
   filesystem and is a standard desk-return cause. Ask every time.

## Report format

```
FORMAT PASS — <manuscript> → <journal>

Before
  <validator output, verbatim, FAILs included>

Changed
  - <each change, one line, with where it was applied: build script or file>

Text integrity
  Words before / after : N / N
  Text hash identical  : yes | no  <if no, stop and explain>

After
  <validator output, verbatim>

Separate files
  Highlights        : <path>, N bullets, max M chars  | not required | missing
  Graphical abstract: <state>
  Supplementary     : <state>

Cannot verify from here
  - Whether the above files are uploaded in the submission system, and as what item type

Out of scope, flagged not fixed
  - <issue> → <Proofread | Audit | Revise> mode
```

Report the validator's own output rather than your reading of it. If a check
still fails, it goes in the report as a failure, never as a caveat.

## Standing trigger

Run this mode, or at minimum steps 3 and 7, whenever the user asks any form of
"is this ready to submit". Answering that question from the style checklist
alone is the failure this mode was built to prevent.

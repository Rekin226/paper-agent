# Mode — Proofread

Line-level language and style polish on an existing manuscript. Produces a revised `.docx` file. **No scientific restructuring, no content changes, no figure changes, no new citations.**

## Philosophy

Proofread mode is narrow by design. The agent may fix:
- Grammar, punctuation, spelling
- Clarity within a sentence (word choice, phrasing)
- Conciseness (remove redundancy, tighten wordy constructions)
- Journal-style terminology (e.g. 'groundwater' vs 'ground water' for HJ, abbreviation consistency)
- Tense consistency within a section
- First-person pronoun removal (I, we, my, our → passive or noun phrases)
- Equation symbol formatting (italic variables, upright functions)
- Citation format compliance (`(Author Year)` vs `(Author, Year)` depending on journal)
- Reference list formatting compliance (Elsevier vs Springer conventions)
- **AI-style markers** per `references/anti-ai-style.md` (em-dashes in body prose, hedge openers like "Importantly," and "Of note,", filler intensifiers, "utilize"/"leverage", and other patterns listed in that file)

The agent **may not**:
- Change the meaning of any sentence
- Add or remove scientific claims
- Restructure paragraphs or sections
- Add or remove figures, tables, or equations
- Add new citations or resolve [CITATION NEEDED] markers
- Rewrite the abstract, structured or not, in a way that changes its content
- Reorder points within a section
- Challenge or correct factual content (that's Review or Revise mode)

If the agent encounters a factual error, unsupported claim, or missing content during proofreading, it **flags** the issue at the end of the pass but does not fix it. The user can then start a Revise session to address it.

## Before proofreading

1. **Extraction complete** via SKILL.md → "Reading existing manuscripts".
2. **Journal reference file loaded.** Terminology, citation format, and equation conventions come from there.
3. **Scope confirmed.** The startup interview asked: (a) language only, (b) language + journal style compliance, (c) language + style + reference list verification. Apply exactly the chosen scope — no scope creep.
4. **Backup the original.** Before any edits, copy the input `.docx` to `<filename>_proofread_backup.docx` in the same directory. The user can always recover the original.

## Proofreading pass — procedure

Proofread mode produces an actual edited `.docx`, unlike Review and Revise. Use the public docx skill for the edit.

1. **Extract the manuscript as structured text** using pandoc via the docx skill.
2. **Run the edit pass section by section** — Abstract, Introduction, Methods, Results, Discussion, Conclusions, References. Within each section:
   - Read every sentence.
   - Apply allowed edits.
   - Record each edit in a running log: `[Section / paragraph] BEFORE → AFTER | reason`.
3. **For reference list verification (scope c only):** sample 5–10 references and verify format compliance with the journal reference file. Do not attempt to verify every entry — flag systematic issues rather than hunting every typo.
4. **Write the edited content back to .docx** using the docx skill's editing methods (unpack → edit XML → repack, as the docx skill describes). Preserve all formatting, figures, tables, and equations.
5. **Validate the output** with `python scripts/office/validate.py <filename>_proofread.docx` (as described in the docx skill).

## Output

Save the edited file as `<original_filename>_proofread.docx` in the same directory as the input. Then present to the user:

```
# Proofread Complete — <filename>

**Scope:** [a / b / c]
**Original file:** <path>
**Proofread file:** <path>_proofread.docx
**Backup of original:** <path>_proofread_backup.docx

## Summary of edits

**Total edits:** N
- Grammar / spelling / punctuation: N
- Clarity / conciseness: N
- Journal terminology: N
- Tense consistency: N
- First-person pronoun removal: N
- Equation formatting: N
- Citation format: N
- Reference list formatting: N

## Edit log

<Section-by-section list of every edit made, format:
 [Section, paragraph] BEFORE → AFTER | reason
 
 Keep this compact — one edit per line. For a long manuscript with 200+ edits,
 group minor edits by type ("Abstract: 4 punctuation fixes") and list the
 substantive edits individually.>

## Issues flagged but NOT fixed

<Anything encountered that falls outside Proofread scope: factual errors,
unsupported claims, missing content, broken citations, figure problems.
For each, give location and nature of the issue. Recommend starting a
Revise session to address them.>

## Journal compliance after proofread

<Re-run the relevant items from the journal pre-submission checklist and
report pass/fail. This lets the user know whether the manuscript is ready
for submission or still needs work.>
```

## Edit discipline — what "line-level" means

The test for whether an edit is in-scope: **can you describe the change without referring to anything outside the sentence itself?**

**Even within scope, never invent content.** A "clarity fix" that adds a fact not present in the original is fabrication, not proofreading. Read `references/anti-fabrication.md`. Specifically:
- Do not add specific numbers, units, or values to vague sentences. "The model performed well" stays as is, or gets flagged for Revise. It does not become "The model achieved R² = 0.74" unless the source sentence already contained that number.
- Do not add citations to unsourced claims. Flag them.
- Do not "complete" abbreviations or terms by guessing what they stand for. Flag them.
- Do not "fix" equations by adding missing terms based on guessing what the author meant. Flag them.

- ✓ "Changed 'We present' to 'This study presents' to remove first-person pronoun" — in-scope, describable at sentence level.
- ✓ "Changed 'ground water' to 'groundwater' per HJ terminology" — in-scope.
- ✓ "Split a 48-word sentence into two for clarity, preserving both clauses verbatim" — in-scope.
- ✗ "Moved this sentence from §3.1 to §3.2 because it fits better there" — out of scope, structural.
- ✗ "Added a sentence noting that the R² threshold is arbitrary" — out of scope, content addition.
- ✗ "Rewrote this paragraph to be clearer" — out of scope, wholesale rewrite. Fix specific sentences individually or flag the paragraph for Revise mode.

When in doubt: flag, don't fix.

## Handling equations

Equation content is never changed. Equation *formatting* can be fixed:
- Variables italicised (h, a, t)
- Functions upright (exp, sin, log)
- Multi-letter abbreviations upright (RMSE, AMP)
- Multiplication signs: `×` or `·`, never asterisk
- Sequential numbering verified and gaps fixed

If an equation has a symbol defined nowhere in the text, flag it — do not add a definition.

## Handling references

For scope (c) — reference list verification — check format compliance only:
- Author name format (surname first, comma, initials)
- Year placement (parenthesised vs. after authors)
- DOI format (prefixed `doi ` for HJ, full URL for JHRS)
- Journal name abbreviation per ISSN LTWA
- Alphabetical ordering and deduplication

Do **not** verify whether the cited paper actually says what the manuscript claims it says. That is Review mode.

## What Proofread mode does NOT do

- Does not restructure or rewrite
- Does not add or remove content
- Does not resolve [CITATION NEEDED] markers
- Does not fact-check claims
- Does not generate reviewer feedback
- Does not produce a response letter
- Does not update figures or tables (except caption language fixes)

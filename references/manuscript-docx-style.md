# Manuscript .docx style — Word output reference

Use this style for any `.docx` export of a journal manuscript when the user has
not specified a journal-specific override. Journal-specific reference files
(`journal-hydrogeology.md`, `journal-jhrs.md`) may override individual rules —
follow those overrides where they conflict with this baseline.

The pipeline is reproducible: (1) generate tables in LaTeX, (2) convert to
`.docx` via `pandoc --citeproc`, (3) post-process with `python-docx` to enforce
the formatting spec below. Do not try to set every property inside `docx-js`
or pandoc alone — the post-process pass is where the table style, font
coercion, and line spacing become reliable.

---

## Document-level formatting

- **Font:** Times New Roman, applied via every variant in the run properties:
  `w:ascii`, `w:hAnsi`, `w:cs`, `w:eastAsia`. Setting only `w:ascii` is not
  enough — Word falls back to Calibri on math runs and East Asian characters.
- **Color:** black (`RGB 000000`) on every run. Do not rely on the Normal
  style alone; the title and heading styles in pandoc-output docx files
  override color, so set it per-run.
- **Line spacing:** double (2.0) for body paragraphs, abstract, headings, and
  captions. Single inside tables (override the double-spaced default).
- **Justification:** body paragraphs justified. Title centered. Headings keep
  default (left) alignment unless the journal specifies otherwise.
- **Output extension:** `.docx`. Do not also produce a `.pdf` — that's a
  downstream concern.

## Title

- 14 pt, **bold**, centered, Times New Roman.

## Headings (all levels)

- 12 pt, **bold**, Times New Roman.
- Default (left) alignment.
- Apply via the existing `Heading 1`, `Heading 2`, etc. styles — do not invent
  new styles. Pandoc maps LaTeX `\section{}`, `\subsection{}`, etc. to these.

## Body, abstract, captions

- 12 pt, regular weight, Times New Roman, black, justified, double-spaced.
- Caption paragraphs (figure / table captions) follow body style — same font,
  same spacing — not a separate "Caption" style.

## Tables — Springer / booktabs style

The original Castro-Pimentel (OQE 2023) paper Table 1 is the reference: three
horizontal rules, nothing else.

- **Three horizontal rules only:**
  - 1.5 pt top rule above the header row (`w:sz="12"` in eighths of a point)
  - 0.5 pt rule under the header row (`w:sz="4"`)
  - 1.5 pt bottom rule below the last data row (`w:sz="12"`)
- **No vertical lines, no internal horizontal lines, no cell shading, no row
  banding.** Clear any inherited `w:tblStyle` and `w:tblBorders` before
  applying cell-level rules.
- **Header row:** bold, centered horizontally.
- **Body rows:** left-aligned.
- **Cell font:**
  - 9 pt by default
  - 7.5 pt for any table with ≥ 10 columns (wide-table override)
- **Cell paragraph spacing:** single (1.0), not double — override the
  document-level double-spacing inside table cells.
- **Table width:** preferred-width = 100 % of text area (`w:tblW
  w:type="pct" w:w="5000"`), autofit columns (`w:tblLayout w:type="autofit"`).
- **Drop fixed per-cell widths.** Remove every `<w:tcW>` element so Word
  recomputes column widths to fit content. Pandoc sets narrow fixed widths
  that cause per-character wrapping in 12-pt cells — this is the single
  biggest cause of unreadable tables in pandoc output.
- **Table alignment on page:** centered.
- **Layout containers** (pandoc wraps side-by-side `\includegraphics{}` in a
  1×1 `tbl` element to control placement): detect by checking for any
  `<w:drawing>` descendant or by dimensions = 1×1, then strip *all* borders
  on those tables. Do not style them as data tables.

## Table content conventions

- **Mean ± std** merged into single cells using the literal Unicode `±`
  (U+00B1), not `$\pm$` math. Halves column count for typical
  metric-with-uncertainty tables.
- **Unicode literals over LaTeX math** in table headers and body: `±`, `²`,
  `³`, `—`, `°`, `µ`, `α`, `β`, `σ`. Pandoc renders LaTeX math inside table
  cells as embedded OMML, which Word styles differently from the surrounding
  cell text. Literals avoid the mismatch.
- **Single-row headers.** Call `.reset_index()` before `to_latex(...,
  index=False)` so the pandas index name (e.g. `model`, `feature_set`)
  becomes a regular first column instead of producing a second header row
  with the index-name plus empty cells.
- **Friendly header labels.** Map internal column names to display labels:
  `rmse → RMSE`, `mard → MARD`, `mae → MAE`, `r2 → R²`,
  `iso_within_tol → ISO ±15%`, `feature_set → Feature set`.
- **Numeric precision:** 2 decimals for percentage- or RMSE-scale metrics,
  3 decimals for coverage- or probability-scale metrics. Round before
  formatting; don't rely on `float_format`.

## Figures

- **Format:** TIFF, 300 dpi, LZW-compressed. Concrete matplotlib call:
  ```python
  fig.savefig(out_path, dpi=300,
              pil_kwargs={"compression": "tiff_lzw"})
  ```
- File extension `.tiff` (not `.tif`); coerce any caller path with
  `Path(out).with_suffix(".tiff")` to keep the convention consistent across
  the codebase.
- Embedded inline at the LaTeX `\includegraphics{}` location.
- Caption follows the figure in body text (pandoc default for `\caption{}`
  inside `\begin{figure}`).

## Citations and references

- Resolved at conversion time via pandoc `--citeproc` (default Chicago
  author-date CSL unless the journal reference file specifies otherwise).
- The `refs.bib` shipped with the manuscript must contain *only* cited
  entries — trim uncited keys before exporting. Cross-check by grepping
  `\cite[pt]?{...}` against the `@type{key,` entries in the `.bib`.
- References section auto-appended at the end of the document by citeproc.
  Don't write a manual `## References` heading; pandoc adds one.

## Math

- Display equations rendered as OMML (editable in Word, not images) — pandoc's
  default behavior. Do not convert to PNG.
- **Forbidden inside `$...$` math:** `\textsc{}`, `\text{}` is fine.
  `\textsc{}` triggers a pandoc warning and renders as raw TeX. Replace
  `\textsc{name}` with `\text{name}` (or plain unstyled text) inside math
  environments before exporting.

## Spreadsheet companions (xlsx, not csv)

When the user asks for the data tables in spreadsheet form alongside the
manuscript, emit `.xlsx` files — **never CSV**:

- CSV loses Unicode when Excel or Numbers auto-detects MacRoman on macOS
  (em-dash `—` displays as `,Äî`).
- XLSX embeds UTF-8 natively in its XML stream, so all symbols survive.

XLSX content rules:
- **Long-form columns** for analysis (`rmse_mean`, `rmse_std`, ...). The
  merged `mean ± std` form belongs in the manuscript only — spreadsheets need
  separable numeric columns for filtering and sorting.
- **Per-cell numeric coercion.** If a column mixes numbers and placeholders
  (e.g. `—`), coerce per cell, not per column. Numbers must land as `float`
  or `int`, placeholders as text. Per-column `pd.to_numeric` forces the
  whole column to text on the first non-numeric value, which Excel then
  flags with the green "number stored as text" triangle.
- Bold header row with a fill (e.g. `1F4E78`), frozen top pane
  (`ws.freeze_panes = "A2"`), auto-fit column widths.

## Build pipeline (reproducible)

End-to-end, from clean parquet artefacts to a finished `.docx`:

1. **Generate LaTeX tables** with merged ± format from parquet sources.
   Pandas → `to_latex(index=False, escape=False, column_format=...)`.
2. **Generate xlsx companions** from the same parquet sources, long-form
   columns, per-cell numeric coercion.
3. **Convert TeX → docx with pandoc**, invoked from the manuscript directory
   so `\input{}` paths and `\includegraphics{figures/...}` resolve:
   ```
   pandoc main.tex -o manuscript_v1.docx \
       --bibliography=refs.bib --citeproc
   ```
4. **Post-process with python-docx** to apply the document-level and
   table-level formatting in this file. The pandoc step alone never
   produces a journal-ready document — the post-process pass is the
   canonical formatting step.

Validate the resulting file by reading paragraphs back via python-docx and
checking: title is 14 pt bold centered TNR, headings are 12 pt bold TNR,
body is 12 pt TNR black double-spaced justified, every table has a top rule
and a bottom rule but no inner rules, every table cell is single-spaced
9 pt (or 7.5 pt if wide). If any assertion fails, the post-process pass
has a bug — do not ship.

## When to deviate

A journal-specific reference file (`journal-hydrogeology.md`,
`journal-jhrs.md`) takes precedence over this baseline for:

- Page size, margins, single vs. double column
- Heading style (decimal numbering, capitalization)
- Reference / citation style (Vancouver, APA, Harvard, etc.)
- Abstract structure (structured abstract, highlights block, KMZ reminder)
- Specific table or figure requirements (e.g. JHRS highlight bullets)

If a journal file silently omits a rule, fall back to this baseline.

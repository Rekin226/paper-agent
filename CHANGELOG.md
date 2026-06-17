# Changelog

All notable changes to `paper-agent` are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.5.0] — 2026-06-17

### Added

- **One-command plugin install.** `paper-agent` is now packaged as a Claude Code plugin. The repo carries its own marketplace, so users can run `/plugin marketplace add Rekin226/paper-agent` then `/plugin install paper-agent@paper-agent` instead of cloning into `~/.claude/skills/`. New files: `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`.
- **Bundled Semantic Scholar MCP.** A root `.mcp.json` defines the citation server as `uvx semantic-scholar-mcp`, so a plugin install wires it up automatically — no separate MCP setup step. Works anonymously; honors `SEMANTIC_SCHOLAR_API_KEY` for higher throughput.
- **Two more journal targets, widening the audience beyond hydrology.** A new field-agnostic `references/journal-generic.md` lets the skill handle any quantitative-science journal out of the box — IMRaD defaults, SI units, mandatory Limitations subsection — while deferring to the target journal's author guidelines on points that genuinely vary (citation style, word limits, abstract format). Block 1 of the startup interview now offers four targets: HJ, JHRS, IEEE TIM, and generic.
- **Bundled try-it-in-60-seconds demos** under `examples/` (all synthetic data, clearly labelled). `examples/demo-draft/` turns synthetic CSVs + project notes into manuscript prose via Draft mode (with an auto-detect fast-path preset, `references/preset-demo.md`); `examples/demo-audit/` is a short manuscript seeded with planted inconsistencies plus an answer key, so a new user can watch Audit mode catch them. README gains a "See it in action" before/after section.

### Fixed

- **The IEEE TIM profile is now selectable.** `references/journal-tim.md` already shipped and was listed in SKILL.md's file index, but Block 1 of the startup interview never offered it — so the skill could never actually load it. Block 1 now lists it (`tim`). Also fixed the readiness-summary template, which omitted the Audit mode and only listed HJ/JHRS as journals.
- **`.docx` features no longer dead-end on local installs.** SKILL.md hard-coded the public `docx` skill at `/mnt/skills/public/docx/SKILL.md`, a cloud-sandbox path absent on local Mac/Linux installs, silently breaking `.docx` reading and export. Both the reading and export steps now detect the `docx` skill at the cloud *or* local (`~/.claude/skills/docx/`) path and fall back to the documented `pandoc → python-docx` pipeline when it is absent, so `.docx` round-trip works in every environment.

### Changed

- README: plugin install is now the recommended Option A (clone/symlink demoted to B/C); Dependencies section corrected to mark the public `docx` skill as optional, document the `pandoc`/`python-docx` fallback, and reflect the bundled MCP. Version badge aligned to the current release.

## [1.4.0] — 2026-06-10

### Added

- New **"Provenance-leak tells"** subsection in `references/anti-ai-style.md` targeting artifacts that betray a manuscript was assembled from a code repository or LaTeX/internal source rather than written as prose:
  - **Code-file paths and script names in body prose** (e.g. "implemented in `experiments/11_wavelength_sweep.py`"). Filenames, module paths, function names, CLI flags, config keys, and commit hashes are banned from the Methods/Results/Discussion narrative; the prose describes the *method*, and code locations live only in the Code Availability statement.
  - **Raw internal cross-reference labels** (`[eq:...]`, `[fig:...]`, `[tab:...]`, `[sec:...]`, `\ref{...}`, `\eqref{...}`, `\cref{...}`, `{#eq-...}`) that never resolved. These must render as "Eq. (N)", "Fig. N", "Table N", "Section N"; an unknown target number is treated as a fabrication risk to resolve, not guess.
  - **Placeholder and template residue** (`<N>`, `[TODO]`, `XXX`, "the figure above").
- Two new pre-finalize self-check items (9, 10) and two Proofread edit-candidate rules in the same file.

### Changed

- Wired the new tells into the three modes that scan for them: `mode-proofread.md` (fixable — the one structural-looking edit Proofread may make, since a path carries no scientific content), `mode-review.md` (flagged as a **Major** reviewer comment), and `mode-audit.md` Check 4 (unresolved labels **Critical**, code paths **Major**, categorized under cross-reference integrity so they don't collide with the audit rule that defers AI-style markers to Proofread).

## [1.3.0] — 2026-05-20

### Added

- New journal style profile **`references/journal-tim.md`** for IEEE Transactions on Instrumentation and Measurement. First non-hydrology profile in the skill, validating the v1.1.2 "extensible to other quantitative-science fields" claim. Source-grounded entirely on the *IEEE Editorial Style Manual for Authors* (29 July 2024, IEEE Publishing Operations) and the IEEE IMS *Information for Authors* page — no invented rules. Covers:
  - Mandatory article structure (11-element order: Title → Abstract → Index Terms → Nomenclature → Introduction → Body → Conclusion → Appendix → Acknowledgment → References → Biographies)
  - Abstract: 150–250 words, single paragraph, no equations/citations/footnotes
  - Index Terms: alphabetical, end of Abstract block, mandatory
  - Four heading levels with IEEEtran enumeration: Roman primary, capital-letter secondary, Arabic tertiary, lowercase quaternary
  - Numeric bracketed citations via `ieee.csl`; in-text patterns including `[1, eq. (8)]`, `[1, Sec. IV]`, `[1, Fig. 2]`
  - Figures: `Fig. N.` em-space caption, subpart `(a)`/`(b)` before caption parts, 600 dpi line art / 300 dpi photos, Lena image banned
  - Tables: `TABLE I` Roman numerals, caption centered above without terminal period, inverted-pyramid descriptive text
  - Equations: consecutive `(1)…`, Appendix restart with `(A1)…`
  - First-footnote pattern (3 paragraphs: received-dates + financial support + corresponding-author marker; affiliations with country and email; supplementary materials notice)
  - Mandatory AI-disclosure block in Acknowledgment when AI was used to generate text/figures/code
  - Pre-submission checklist for Audit mode
- Index entry added to `## REFERENCE FILES IN THIS SKILL` in `SKILL.md`.

### Note

The TIM profile demonstrates the extension pattern in practice: ~250 lines, drops in as a single file, no changes to the universal framework or other journal profiles. The `manuscript-docx-style.md` baseline still applies for everything the TIM profile doesn't override (TNR coercion, table styling fallback, mean ± std merging, TIFF figures, reproducible pipeline). The biggest TIM-specific overrides are: numeric citations (`--csl=ieee.csl`), table caption format, table numbering (Roman), Acknowledgment placement and AI-disclosure mandate, and mandatory first-footnote pattern.

## [1.2.0] — 2026-05-20

### Added

- New reference file `references/manuscript-docx-style.md` — the canonical Word-output formatting spec, distilled from a real end-to-end build of a Springer/OQE-style manuscript. Covers: Times New Roman coercion across all run variants (`w:ascii`, `w:hAnsi`, `w:cs`, `w:eastAsia`); 14 pt bold centered title; 12 pt bold headings; 12 pt double-spaced justified body; Springer/booktabs three-rule table style (1.5 pt top, 0.5 pt under header, 1.5 pt bottom, no verticals, no banding); 9 pt single-spaced cells (7.5 pt for ≥ 10-column tables); autofit + 100 % preferred-width tables with `<w:tcW>` widths removed; `mean ± std` cell merging via literal Unicode `±`; Unicode-over-LaTeX-math in table headers; single-row headers via `.reset_index() + index=False`; TIFF figures at 300 dpi LZW; OMML equations (no `\textsc{}` inside `$...$`); pandoc `--citeproc` with trimmed `refs.bib`; XLSX (never CSV) for spreadsheet companions with per-cell numeric coercion to avoid Excel's "number stored as text" green triangles; the reproducible `pandoc → python-docx post-process` pipeline.
- `## EXPORT TO .DOCX` section in `SKILL.md` now points export tasks at the new reference file as the canonical baseline; journal reference files continue to override per-journal specifics.

### Note

This release codifies a writing/formatting style validated end-to-end on a multi-table, multi-figure manuscript with citeproc citations. The baseline applies to any quantitative-science paper; the HJ/JHRS journal files override individual rules where their submission requirements differ.

## [1.1.2] — 2026-05-15

### Changed

- **Scope widened from "hydrology and water-resources" to "quantitative-science manuscripts, calibrated for hydrology."** The skill's underlying framework (Audit mode's 8 checks, anti-fabrication directive, anti-AI-style rules, five-move Introduction funnel, reproducibility/back-matter standards) is field-agnostic; only the two journal style files (`journal-hydrogeology.md`, `journal-jhrs.md`) are hydrology-specific. This release reframes the positioning to reflect that, while keeping hydrology as the proof case and trigger anchor.
- SKILL.md frontmatter description rewritten: "quantitative-science papers, currently calibrated for hydrology and water-resources (HJ, JHRS) and extensible to other quantitative-science fields via a journal style file."
- README hero tagline widened: "scientific manuscripts" (was "hydrology and water-resources manuscripts"), with an explicit hydrology-calibration note.
- New README subsection **"Extending to other quantitative-science fields"** under Configuration, documenting the three-step process for applying the skill to atmospheric sciences, hydrochemistry, soil science, ecology, geophysics, and related fields.
- Version badge bumped to 1.1.2.

### Note

This is a positioning/framing change, not a functionality change. The skill behaves identically to v1.1.1; hydrology remains the only domain with shipped journal style profiles. The reframe is intended to invite contributions from adjacent quantitative-science fields rather than implying out-of-the-box support for them.

## [1.1.1] — 2026-05-14

### Changed

- README repositioned: the skill ships *with profiles for* HJ and JHRS rather than being scoped to them. Most of the skill (anti-fabrication, anti-AI-style, Introduction funnel, Audit mode, reproducibility standard) is journal-agnostic; only the two journal style files are journal-specific.
- New README subsection **"Extending to other journals"** documenting the three-step process for adding a new journal profile.
- CONTRIBUTING promotes new-journal PRs to a top-priority callout with a list of high-impact target journals (WRR, Journal of Hydrology, HESS, WRM, Hydrological Processes, Groundwater).
- Version badge bumped to 1.1.1.

## [1.1.0] — 2026-05-14

### Added

- **Audit mode (fifth mode).** Read a full manuscript and produce a severity-tagged consistency-and-coherence report (Critical / Major / Minor findings). Runs 8 checks: coherence chain (gap → objectives → methods → results → discussion → conclusions → abstract → highlights), numerical consistency across sections, terminological consistency, cross-reference integrity (figures/tables/equations/citations), argument honesty (do conclusions exceed what limitations admit), tense consistency, citation usage consistency, and JHRS-specific Highlights/Abstract integrity. No file edits, no revision proposals — Audit identifies; user fixes via Revise mode. New reference file: `references/mode-audit.md`.
- **Anti-fabrication directive (most important rule in the skill).** A standalone reference file (`references/anti-fabrication.md`) enumerating the agent's four acceptable responses when uncertain: ask the user, flag a gap inline (`[CITATION NEEDED]`, `[VALUE NEEDED]`, `[VERIFY]`, `[FROM USER]`), search Semantic Scholar, or decline to make the claim. Covers fabrication of citations, numbers, methodological details, study-area facts, physical interpretation, author metadata, and manuscript text. Applies to all five modes.
- **Anti-fabrication pre-export QC checklist.** Eight new pre-export checks in `SKILL.md` covering invented values, fabricated citations, unhedged causal claims, "well-known" appeals to consensus, invented study-area facts, invented methodological details, invented author metadata, and complete reporting of bracketed placeholders.
- **Mode-specific anti-fabrication paragraphs** at the top of `mode-review.md`, `mode-revise.md`, and `mode-proofread.md`, plus a "never invent content during proofread" subsection in `mode-proofread.md` Edit discipline.

### Changed

- `SKILL.md` mode count: "four distinct modes" → "five distinct modes". MODES table now includes the Audit row.
- `references/startup-interview.md`: Block 0 now offers five mode options. Block 4′ adds an Audit-scope question (full / consistency-only / coherence-only).
- README mode table updated to five rows with the new Audit icon (🧭). Architecture tree shows the two new reference files.

### File inventory

`SKILL.md` plus `references/` containing: `startup-interview.md`, `journal-hydrogeology.md`, `journal-jhrs.md`, `mode-review.md`, `mode-revise.md`, `mode-proofread.md`, `mode-audit.md`, `introduction-structure.md`, `reproducibility.md`, `anti-fabrication.md`, `anti-ai-style.md`, `anti-summary-rules.md`, `preset-example.md`. Thirteen reference files total.

## [1.0.0] — 2026-05-14

Initial public release.

### Added

- **Four-mode architecture.** Draft, Review, Revise, and Proofread modes, each with its own protocol, allowed/forbidden operations, and output format. Mode is selected once per session at Block 0 of the startup interview.
- **Two journal style profiles.** *Hydrogeology Journal* (Springer / IAH, Harvard citations, single-paragraph abstract) and *Journal of Hydrology: Regional Studies* (Elsevier, structured abstract, Highlights, KMZ requirement). Style files cover language register, document structure, citation format, equation conventions, numerals, and journal-specific pre-submission checklists.
- **Semantic Scholar citation pipeline.** Every literature claim resolves through `mcp__semantic-scholar__search_papers` with field-limited queries; fabricated citations are refused and `[CITATION NEEDED]` markers are inserted when no match clears the relevance threshold.
- **`.docx` round-trip via the public `docx` skill.** Manuscripts are extracted with pandoc for Review/Revise/Proofread input and written back for Draft export and Proofread output.
- **Five-move funnel for Introductions.** A dedicated reference file (`references/introduction-structure.md`) enforces broad significance → narrowing literature review → specific gap → study objectives → roadmap.
- **Reproducibility and back-matter standard.** Methods replicability requirements, Data Availability Statement, Code Availability Statement, CRediT taxonomy, Conflict of Interest declaration, and Funding statement, all keyed to HJ and JHRS expectations.
- **Anti-AI-style and anti-summary safeguards.** Two reference files codify the patterns reviewers increasingly flag as AI-generated (em-dashes in body prose, hedge openers, filler intensifiers, three-item lists, `utilize` / `leverage`) and require complete prose instead of skeleton outlines.
- **Figure necessity assessment.** Every candidate figure must pass a four-question check before being proposed; hard caps of 6 figures per paper and 2 per result class.
- **Section-by-section pause protocol.** After each Draft section or each Revise proposal, the skill stops and asks whether to continue, revise, or export.
- **Project preset mechanism.** `references/preset-example.md` provides a template for project-specific fast-paths that auto-detect by workspace file presence and inject cached project facts (study area, period, CRS, model variants, parameter counts, classification rules, mandatory limitations, pre-curated Semantic Scholar queries).
- **Private-preset workflow.** Gitignored `.local/` directory with a documented symlink pattern lets users keep real project presets out of the public repository while preserving auto-detection.

### File inventory

`SKILL.md` plus `references/` containing: `startup-interview.md`, `journal-hydrogeology.md`, `journal-jhrs.md`, `mode-review.md`, `mode-revise.md`, `mode-proofread.md`, `introduction-structure.md`, `reproducibility.md`, `anti-ai-style.md`, `anti-summary-rules.md`, `preset-example.md`.

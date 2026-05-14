# Changelog

All notable changes to `paper-agent` are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

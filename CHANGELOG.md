# Changelog

All notable changes to `paper-agent` are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

# Contributing to paper-agent

Thanks for your interest in improving `paper-agent`. This skill is small and opinionated, so contributions are most useful when they are scoped tightly and respect the existing mode boundaries.

## Reporting issues

Open a GitHub issue with:

- **What you were doing** — mode, journal, and a redacted example of the prompt or input file (no manuscript text you do not want public).
- **What you expected** — referencing the relevant section of `SKILL.md` or `references/<file>.md` when possible.
- **What happened** — the actual output, including any `[CITATION NEEDED]` markers, missing back matter, or mode-boundary violations.
- **Claude Code version** — `claude --version`.
- **Skill version** — see `CHANGELOG.md`.

Please redact personal data, manuscript IDs, and unpublished results before posting.

## Submitting pull requests

1. **One concern per PR.** A PR that adds a new journal profile should not also rewrite the anti-AI-style rules. Small, focused changes review faster and are less likely to introduce regressions.
2. **Preserve mode boundaries.** Each of the four modes has a precise scope (see the `references/mode-*.md` files). Do not expand Proofread to restructure paragraphs, do not let Revise silently edit `.docx` files, etc.
3. **No fabricated examples.** If you add a worked example, use placeholder tokens (`<study region>`, `<metric>`, `<value>`) or a clearly-fictional setup. Do not paste real unpublished data.
4. **Update reference cross-links.** If you rename or split a reference file, update every cross-link in `SKILL.md` and the other reference files.
5. **Run the local test below** before opening the PR.

### Good PR ideas

- New journal style file (Water Resources Research, Journal of Hydrology, HESS, etc.) following the structure of `references/journal-hydrogeology.md`.
- Additional `references/preset-<project>.md` templates for common project archetypes (catchment rainfall-runoff, aquifer water-balance, isotope tracer studies, …) — kept generic, no real data.
- Tightening or expanding the anti-AI-style checklist as reviewer-recognised patterns evolve.
- Bug fixes for mode-boundary violations.

### PR ideas that need discussion first

- Changes to the four-mode architecture itself (adding, splitting, or removing a mode).
- Switching the citation backend away from Semantic Scholar.
- Changing the `.docx` round-trip strategy.

Open an issue first for these so we can agree on the design before code review.

## Testing the skill locally

The skill is text-only, so "tests" mean exercising each mode against a known-good workspace and confirming the behaviour matches the spec in `SKILL.md` and the relevant `references/mode-*.md` file.

1. **Install the skill in a scratch location** so you do not overwrite your working copy:

   ```sh
   ln -s "$(pwd)" ~/.claude/skills/paper-agent-dev
   ```

   In Claude Code, invoke `/paper-agent-dev` (the directory name becomes the skill name).

2. **Draft mode smoke test.** Create a scratch workspace with a CSV containing a few rows of numeric results. Run `/paper-agent-dev`, choose Draft, pick HJ. Confirm the startup interview asks for project data sources and refuses to proceed when files are missing.

3. **Review mode smoke test.** Point the skill at any short `.docx` (your own or a public preprint converted to `.docx`). Confirm the extraction report appears before any review content, and that the report follows the structure in `references/mode-review.md`.

4. **Revise mode smoke test.** Same `.docx`, this time with a fake numbered reviewer comment block. Confirm every proposed revision maps to a comment ID and uses the BEFORE / AFTER / RATIONALE format.

5. **Proofread mode smoke test.** Same `.docx`. Confirm a backup file is created, that no sections are restructured, and that the edit log captures every change as a single-sentence-level operation.

6. **Citation pipeline smoke test.** Inside any drafting flow, force a section that requires a literature claim and confirm the citation either resolves via Semantic Scholar (real DOI returned) or inserts `[CITATION NEEDED: <topic>]` — never fabricates.

When all five smoke tests pass and your change does not regress them, the PR is ready.

## Code of conduct

Be specific, be honest, be kind. Reviewing academic writing is a craft; helping people produce better manuscripts is the only goal here.

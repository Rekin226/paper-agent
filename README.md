<div align="center">

# 📄 paper-agent

**Journal-quality hydrology manuscripts, drafted and reviewed by Claude.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.1-green.svg)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-orange.svg)](https://docs.claude.com/en/docs/claude-code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

*Drafts, reviews, revises, proofreads, and audits hydrology and water-resources manuscripts.*  
*Ships with style profiles for* **Hydrogeology Journal** • **Journal of Hydrology: Regional Studies** *— extensible to others via a single reference file.*

</div>

---

## ✨ Overview

`paper-agent` runs in your local Claude Code session and produces journal-submission-quality output. It is not a writing assistant in the usual sense — it follows strict mode boundaries, refuses to invent values or fabricate citations, and pauses for confirmation after every section.

Use it when you have:

- A workspace of project data (CSVs, source code, metadata) and need a complete first manuscript draft.
- An existing `.docx` manuscript and need reviewer-style feedback, section-by-section revision suggestions, or a language-level polish.
- Reviewer comments from a journal decision letter and need help producing a point-by-point response and revised text.

## 🎯 Modes

| | Mode | Input | Output |
|---|---|---|---|
| ✍️ | **Draft** | Project data files (CSVs, source code, metadata) | Complete manuscript sections with inline citations, plus a `.docx` export |
| 👀 | **Review** | Existing `.docx` manuscript | Structured reviewer report in chat (no file edits) |
| 🔄 | **Revise** | Existing `.docx` + optional reviewer comments | Section-by-section BEFORE / AFTER / RATIONALE suggestions in chat (you apply them), plus a response-to-reviewers letter when reviewer comments are provided |
| 🔍 | **Proofread** | Existing `.docx` manuscript | Revised `.docx` with language-level fixes only — no scientific changes, no restructuring, no new citations |
| 🧭 | **Audit** | Existing `.docx` manuscript | Consistency and coherence report in chat with severity-tagged findings (Critical / Major / Minor). Catches gap-vs-conclusions mismatches, sample-size inconsistencies, broken cross-references, terminology drift, argument honesty conflicts |

The user selects one mode at session start. Each mode has its own reference file under `references/` with the exact protocol, allowed/forbidden operations, and output format.

## 📦 Installation

`paper-agent` is a Claude Code skill. It lives at `~/.claude/skills/paper-agent/` on your machine.

**Option A — Clone directly into the skills directory:**

```sh
git clone https://github.com/<your-user>/paper-agent.git ~/.claude/skills/paper-agent
```

**Option B — Clone anywhere and symlink:**

```sh
git clone https://github.com/<your-user>/paper-agent.git ~/code/paper-agent
ln -s ~/code/paper-agent ~/.claude/skills/paper-agent
```

Restart your Claude Code session (or open a new one) so it picks up the skill.

## 🚀 Quickstart

In any Claude Code session, invoke the skill explicitly:

```
/paper-agent
```

…or trigger it implicitly by phrasing the task naturally:

```
I want to draft a manuscript for Hydrogeology Journal from the CSVs in ./workspace.
```

```
Please review my manuscript at ~/papers/my-paper.docx and tell me what a JHRS reviewer would say.
```

```
Proofread ~/papers/my-paper.docx for language only — no scientific changes.
```

The skill will run a short startup interview to pick the mode, the target journal, and the data sources, then proceed section-by-section with a pause-and-confirm protocol.

## 🧩 Architecture

```
paper-agent/
├── SKILL.md                         # entry point + Draft-mode workflow
├── .claude/settings.json            # enables the semantic-scholar MCP
├── .local/                          # gitignored: your private presets
└── references/
    ├── startup-interview.md         # mode/journal/data interview
    ├── journal-hydrogeology.md      # HJ style, citation format, checklist
    ├── journal-jhrs.md              # JHRS style, structured abstract, KMZ
    ├── mode-review.md               # Review-mode report format
    ├── mode-revise.md               # Revise-mode BEFORE/AFTER protocol
    ├── mode-proofread.md            # Proofread-mode allowed scope
    ├── mode-audit.md                # Audit-mode 8-check protocol
    ├── introduction-structure.md    # five-move funnel for Introductions
    ├── reproducibility.md           # Methods replicability, back matter
    ├── anti-fabrication.md          # ask, flag, search, or decline — never invent
    ├── anti-ai-style.md             # patterns reviewers recognise as AI
    ├── anti-summary-rules.md        # write prose, not outlines
    └── preset-example.md            # project-preset template
```

Reference files are loaded lazily — only the mode and journal files the current session needs are read. This keeps Claude's context budget small.

## 🔌 Dependencies

- **Claude Code** — the CLI is the runtime. See [Claude Code docs](https://docs.claude.com/en/docs/claude-code) for setup.
- **Semantic Scholar MCP** — required for citation resolution. The `.claude/settings.json` shipped with this repo enables it; install the MCP separately following the [Semantic Scholar MCP](https://github.com/) instructions for your environment.
- **Public `docx` skill** — required for `.docx` reading and writing. The skill expects it at `/mnt/skills/public/docx/SKILL.md` (Claude Code's standard public-skill path).
- **`pandoc`** — used by the `docx` skill for text extraction. Install via `brew install pandoc` (macOS) or your platform equivalent.

## ⚙️ Configuration

### Project presets

If you work on the same project repeatedly, define a project preset to skip the generic data-source interview each time.

1. Copy `references/preset-example.md` to `references/preset-<your-project>.md` (or to `.local/preset-<your-project>.md` if you want to keep it private — see `.local/README.md` for the symlink workflow).
2. Fill in the placeholders: detection-trigger filename, data file paths, fixed project facts, mandatory limitations, Semantic Scholar search queries.
3. Whenever `paper-agent` starts in Draft mode, it scans `references/preset-*.md` and auto-loads any preset whose trigger file exists in your workspace.

### Extending to other journals

The skill currently ships with style profiles for two journals (HJ and JHRS), but most of its value is journal-agnostic: the anti-fabrication directive, anti-AI-style rules, five-move Introduction funnel, Audit-mode consistency checks, and reproducibility/back-matter standards apply to any hydrology or water-resources manuscript. To target a different journal:

1. Copy `references/journal-hydrogeology.md` to `references/journal-<your-journal>.md`.
2. Adapt the citation format, abstract structure, equation conventions, and pre-submission checklist to match the journal's author guidelines.
3. Add the new option to Block 1 of `references/startup-interview.md` so the skill can offer it at session start.

PRs adding journal profiles for *Water Resources Research*, *Journal of Hydrology*, *Hydrology and Earth System Sciences*, *Water Resources Management*, and similar venues are explicitly welcomed — see `CONTRIBUTING.md`.

### MCP servers

The shipped `.claude/settings.json` enables the `semantic-scholar` MCP server. If you do not want this enabled by default, edit or remove the file.

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for issue and PR guidelines, plus instructions for testing the skill locally.

## 📜 License

[MIT](LICENSE) — see the LICENSE file for the full text.

---

<div align="center">

*Built for researchers who want Claude as a rigorous co-author, not a stylish ghostwriter.*

</div>

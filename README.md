<div align="center">

# 📄 paper-agent

**Journal-quality hydrology manuscripts, drafted and reviewed by Claude.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.5.0-green.svg)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-orange.svg)](https://docs.claude.com/en/docs/claude-code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

*Drafts, reviews, revises, proofreads, and audits scientific manuscripts.*  
*Currently calibrated for hydrology, with profiles for* **Hydrogeology Journal** • **Journal of Hydrology: Regional Studies** *— extensible to other quantitative-science fields via a single reference file.*

</div>

---

## ✨ Overview

Most LLM writing tools are general-purpose and produce text that reviewers immediately recognise as AI-generated. `paper-agent` is purpose-built for hydrology and water-resources peer review: it enforces journal-specific structure, refuses to fabricate citations, and surfaces consistency failures — gap-vs-conclusions mismatches, sample-size drift, terminology inconsistency — that authors and reviewers routinely miss.

`paper-agent` runs in your local Claude Code session and produces journal-submission-quality output. It is not a writing assistant in the usual sense — it follows strict mode boundaries, refuses to invent values or fabricate citations, and pauses for confirmation after every section.

Use it when you have:

- A workspace of project data (CSVs, source code, metadata) and need a complete first manuscript draft.
- An existing `.docx` manuscript and need reviewer-style feedback, section-by-section revision suggestions, or a language-level polish.
- Reviewer comments from a journal decision letter and need help producing a point-by-point response and revised text.

## 🎬 See it in action

Two bundled, **synthetic** demos let you try the skill in ~60 seconds with no data of your own — see [`examples/`](examples/).

**Audit mode** reads a manuscript and surfaces inconsistencies authors miss. Given this (synthetic) draft:

> *Abstract:* "We analysed **six years** of monitoring data (**January 2018–December 2022**)… a network of **33 wells**…"
> *Results:* "Across all **35 wells**, the model reproduced the seasonal cycle (Figure 1)… the spatial pattern is shown in **Figure 3**… the correlation with the tidal signal was **not significant (rho = 0.02, p = 0.94)**."

Audit flags, among others:

- 🔴 **Temporal error** — "six years" but January 2018–December 2022 is **five** years.
- 🔴 **Sample-size drift** — **33** wells in the Abstract/Methods, **35** in the Results.
- 🔴 **Argument-honesty conflict** — the Abstract calls the tidal correlation "strong", but the Results report it as **not significant**.
- 🟠 **Broken cross-reference** — the text cites **Figure 3**, but only Figures 1–2 are captioned.

The full demo (with answer key) and a **Draft-mode** demo that turns synthetic CSVs into manuscript prose are in [`examples/`](examples/).

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

`paper-agent` is a Claude Code skill. Install it as a plugin (recommended) or clone it into your skills directory.

**Option A — Install as a plugin (recommended, one command each):**

```sh
/plugin marketplace add Rekin226/paper-agent
/plugin install paper-agent@paper-agent
```

This registers the repo as a marketplace and installs the skill. The bundled `.mcp.json` also wires up the Semantic Scholar MCP server automatically (see [Dependencies](#-dependencies)).

**Option B — Clone directly into the skills directory:**

```sh
git clone https://github.com/Rekin226/paper-agent.git ~/.claude/skills/paper-agent
```

**Option C — Clone anywhere and symlink:**

```sh
git clone https://github.com/Rekin226/paper-agent.git ~/code/paper-agent
ln -s ~/code/paper-agent ~/.claude/skills/paper-agent
```

With Option B or C, restart your Claude Code session (or open a new one) so it picks up the skill.

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
├── .claude-plugin/                  # plugin + marketplace manifests (one-command install)
│   ├── plugin.json
│   └── marketplace.json
├── .mcp.json                        # defines the semantic-scholar MCP server
├── .claude/settings.json            # enables the semantic-scholar MCP
├── .local/                          # gitignored: your private presets
├── examples/                        # bundled synthetic demos (Draft + Audit) — try it in 60s
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
    ├── preset-example.md            # project-preset template
    └── preset-demo.md               # auto-detect preset for the bundled Draft demo
```

Reference files are loaded lazily — only the mode and journal files the current session needs are read. This keeps Claude's context budget small.

## 🔌 Dependencies

- **Claude Code** — the CLI is the runtime. See [Claude Code docs](https://docs.claude.com/en/docs/claude-code) for setup.
- **Semantic Scholar MCP** — required for citation resolution. The shipped `.mcp.json` defines it as `uvx semantic-scholar-mcp`; the plugin install wires it up automatically. Requires [`uv`](https://docs.astral.sh/uv/) on your PATH. **No API key is required** — it uses Semantic Scholar's shared anonymous pool, which is fine for the low-volume lookups during drafting. No key is bundled with this skill; each user supplies their own. For a dedicated, steadier rate (1 request/sec), set your own `SEMANTIC_SCHOLAR_API_KEY` environment variable.
- **`pandoc`** — required for `.docx` reading and for the `.docx` export fallback. Install via `brew install pandoc` (macOS) or your platform equivalent.
- **`python-docx`** — used by the export fallback's post-process pass. Auto-installed on demand (`pip install python-docx`).
- **Public `docx` skill** *(optional)* — if the public `docx` skill is present (`/mnt/skills/public/docx/SKILL.md` in Claude Code cloud, or `~/.claude/skills/docx/SKILL.md` locally), `paper-agent` uses it for `.docx` read/write. If it is absent — common on local installs — the skill falls back to the `pandoc → python-docx` pipeline automatically, so `.docx` features work either way.

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

### Extending to other quantitative-science fields

The skill's reference framework (Audit mode's 8 checks, anti-fabrication directive, anti-AI-style rules, five-move Introduction funnel, reproducibility/back-matter standards) is **field-agnostic** — it applies to any quantitative-science manuscript with a Methods / Results / Discussion structure. Only the two journal style files (`references/journal-hydrogeology.md`, `references/journal-jhrs.md`) are hydrology-specific.

To apply the skill to a different field (atmospheric sciences, hydrochemistry, soil science, ecology, geophysics, …):

1. Add a journal style file for your target venue, following the "Extending to other journals" instructions above.
2. Optionally, replace hydrology-flavored illustrative examples in `references/preset-example.md` with examples from your field.
3. No core `SKILL.md` changes are needed — the mode protocols, citation workflow, and pause-and-confirm structure are domain-neutral.

The skill currently ships with hydrology as its proof case. PRs adding profiles for related quantitative-science fields are welcomed — see `CONTRIBUTING.md`.

### MCP servers

The shipped `.claude/settings.json` enables the `semantic-scholar` MCP server. If you do not want this enabled by default, edit or remove the file.

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for issue and PR guidelines, plus instructions for testing the skill locally.

## 📜 License

[MIT](LICENSE) — see the LICENSE file for the full text.

## 📚 Citation & background

Built by [Ouédraogo Abdoul Rachid](https://scholar.google.com/citations?user=AFrUnG0AAAAJ), Postdoctoral Researcher at National Central University and Adjunct Lecturer at Feng Chia University. Designed alongside research on gray-box groundwater modeling for the Zhuoshui Alluvial Fan, Taiwan (accepted, *Hydrogeology Journal*).

---

<div align="center">

*Built for researchers who want Claude as a rigorous co-author, not a stylish ghostwriter.*

</div>

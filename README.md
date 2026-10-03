<div align="center">

# 📄 paper-agent

**Journal-quality hydrology manuscripts, drafted and reviewed by Claude.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.7.0-green.svg)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-orange.svg)](https://docs.claude.com/en/docs/claude-code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

*Drafts, reviews, revises, proofreads, audits, and submission-formats scientific manuscripts.*  
*Calibrated for hydrology (* **Hydrogeology Journal** • **Journal of Hydrology: Regional Studies** • **Journal of Hydrology** • **Water Resources Research** • **HESS** • **Groundwater** *), with profiles for* **Engineering Geology** *,* **IEEE Transactions on Instrumentation and Measurement** *,* **JMBE** *and* **Physiological Measurement** *, plus a generic profile for any other quantitative-science journal — extensible via a single reference file.*

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
| 📐 | **Format** | Existing `.docx` + target journal | Submission-ready `.docx` (continuous line numbers, page numbers, double spacing, single column) plus the separate files the portal needs (e.g. highlights), and a two-layer compliance report. Changes presentation only, never a word of text |

The user selects one mode at session start. Each mode has its own reference file under `references/` with the exact protocol, allowed/forbidden operations, and output format.

## 📦 Installation

`paper-agent` is a Claude Code skill. Install it as a plugin (recommended) or clone it into your skills directory.

**Option A — Install as a plugin (recommended, one command each):**

```sh
/plugin marketplace add Rekin226/paper-agent
/plugin install paper-agent@paper-agent
```

This registers the repo as a marketplace and installs the skill. The bundled `.mcp.json` also wires up the Semantic Scholar MCP server automatically (see [Setup](docs/SETUP.md#dependencies)).

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

**Option D — Upload to claude.ai or Claude Desktop:** run `./package_for_claude_ai.sh` from a clone. It writes `paper-agent.zip` (to `~/Downloads` by default) with the frontmatter adjusted for claude.ai's skill validator. Upload that zip through the Skills section of your claude.ai settings. Requires Python with PyYAML.

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

```
Is ~/papers/my-paper.docx ready to submit to Engineering Geology?
```

The skill will run a short startup interview to pick the mode, the target journal, and the data sources, then proceed section-by-section with a pause-and-confirm protocol.

## 📖 Setup and customization

Requires Claude Code, [`uv`](https://docs.astral.sh/uv/) for the bundled Semantic Scholar server, and `pandoc` for `.docx` round-trips. No API keys needed.

Dependencies, project presets, MCP configuration, and how to add a profile for your own journal or field are in **[docs/SETUP.md](docs/SETUP.md)**. New journal profiles are the easiest way to contribute.

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

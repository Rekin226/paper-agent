# Setup and customization

Everything beyond the [quickstart](../README.md#-quickstart): what the skill depends on, how to configure it, and how to extend it to new journals and fields.

## Dependencies

- **Claude Code** — the CLI is the runtime. See [Claude Code docs](https://docs.claude.com/en/docs/claude-code) for setup.
- **Semantic Scholar MCP** — required for citation resolution. The shipped `.mcp.json` defines it as `uvx semantic-scholar-mcp`; the plugin install wires it up automatically. Requires [`uv`](https://docs.astral.sh/uv/) on your PATH. **No API key is required** — it uses Semantic Scholar's shared anonymous pool, which is fine for the low-volume lookups during drafting. No key is bundled with this skill; each user supplies their own. For a dedicated, steadier rate (1 request/sec), set your own `SEMANTIC_SCHOLAR_API_KEY` environment variable.
- **OpenAlex MCP** *(optional but recommended)* — used to verify DOIs resolved from Semantic Scholar. The shipped `.mcp.json` defines it as `npx -y openalex-research-mcp`. **No API key is required**, but set `OPENALEX_EMAIL` to your own address in `.mcp.json` to use OpenAlex's polite pool. If the server is absent the skill still runs on Semantic Scholar alone and says so at session start, with DOI verification degraded for that session.
- **`pandoc`** — required for `.docx` reading and for the `.docx` export fallback. Install via `brew install pandoc` (macOS) or your platform equivalent.
- **`python-docx`** — used by the export fallback's post-process pass. Auto-installed on demand (`pip install python-docx`).
- **Public `docx` skill** *(optional)* — if the public `docx` skill is present (`/mnt/skills/public/docx/SKILL.md` in Claude Code cloud, or `~/.claude/skills/docx/SKILL.md` locally), `paper-agent` uses it for `.docx` read/write. If it is absent — common on local installs — the skill falls back to the `pandoc → python-docx` pipeline automatically, so `.docx` features work either way.

## Project presets

If you work on the same project repeatedly, define a project preset to skip the generic data-source interview each time.

1. Copy `references/preset-example.md` to `references/preset-<your-project>.md` (or to `.local/preset-<your-project>.md` if you want to keep it private — see `.local/README.md` for the symlink workflow).
2. Fill in the placeholders: detection-trigger filename, data file paths, fixed project facts, mandatory limitations, Semantic Scholar search queries.
3. Whenever `paper-agent` starts in Draft mode, it scans `references/preset-*.md` and auto-loads any preset whose trigger file exists in your workspace.

## Extending to other journals

The skill ships with named profiles for **Hydrogeology Journal**, **Journal of Hydrology: Regional Studies**, **Journal of Hydrology**, **Water Resources Research**, **Hydrology and Earth System Sciences**, **Groundwater**, **Engineering Geology**, **IEEE Transactions on Instrumentation and Measurement**, **Journal of Medical and Biological Engineering**, and **Physiological Measurement**, plus a field-agnostic **generic** profile for everything else. Most of the skill's value is journal-agnostic anyway: the anti-fabrication directive, anti-AI-style rules, five-move Introduction funnel, Audit-mode consistency checks, and reproducibility/back-matter standards apply to any quantitative-science manuscript.

**For a one-off submission to an unlisted journal:** select `generic` at session start and paste the journal's author guidelines — the generic profile uses them to fill in the specifics (citation style, word limits, abstract format) and applies sensible defaults for the rest.

**For a journal you target repeatedly,** add a reusable named profile:

1. Copy the closest existing profile (`references/journal-hydrogeology.md` for author–year journals, `references/journal-tim.md` for numbered/IEEE journals, or `references/journal-generic.md` as a neutral starting point) to `references/journal-<your-journal>.md`.
2. Adapt the citation format, abstract structure, equation conventions, and pre-submission checklist to match the journal's author guidelines. Anchor every rule to the guidelines — do not invent formatting rules.
3. Add the new option to Block 1 of `references/startup-interview.md` so the skill can offer it at session start.

PRs adding journal profiles — *Water Resources Management*, *Advances in Water Resources*, *Environmental Modelling & Software*, or venues in adjacent quantitative fields — are explicitly welcomed and are the easiest way to contribute. Improving a shipped profile counts too: `journal-jhydrol.md` and `journal-groundwater.md` were ported from an earlier version of this skill and carry an explicit **"Unverified — confirm before submission"** list of fields that still need checking against the journal's current author guide (Elsevier and Wiley both block automated access, so these need a human with a browser). Closing those out is a genuinely useful, low-risk first PR. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Extending to other quantitative-science fields

The skill's reference framework (Audit mode's 8 checks, anti-fabrication directive, anti-AI-style rules, five-move Introduction funnel, reproducibility/back-matter standards) is **field-agnostic** — it applies to any quantitative-science manuscript with a Methods / Results / Discussion structure. Only the named journal style files are venue-specific, and six of the ten (`journal-hydrogeology.md`, `journal-jhrs.md`, `journal-jhydrol.md`, `journal-wrr.md`, `journal-hess.md`, `journal-groundwater.md`) are hydrology titles; `journal-engineering-geology.md`, `journal-tim.md`, `journal-jmbe.md`, and `journal-physiological-measurement.md` already demonstrate the extension to other fields.

To apply the skill to a different field (atmospheric sciences, hydrochemistry, soil science, ecology, geophysics, …):

1. Add a journal style file for your target venue, following the "Extending to other journals" instructions above.
2. Optionally, replace hydrology-flavored illustrative examples in `references/preset-example.md` with examples from your field.
3. No core `SKILL.md` changes are needed — the mode protocols, citation workflow, and pause-and-confirm structure are domain-neutral.

The skill currently ships with hydrology as its proof case. PRs adding profiles for related quantitative-science fields are welcomed — see [CONTRIBUTING.md](../CONTRIBUTING.md).

## MCP servers

The shipped `.claude/settings.json` enables the `semantic-scholar` MCP server, and `.mcp.json` also declares the optional `openalex` server. If you do not want either enabled by default, edit or remove the relevant file. Replace the placeholder `OPENALEX_EMAIL` in `.mcp.json` with your own address.

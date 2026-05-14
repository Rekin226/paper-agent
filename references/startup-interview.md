# Startup Interview

Run once per session before any work. The interview branches by mode — not all blocks apply to all modes.

## Block 0 — Mode selection (ALWAYS FIRST, ALL MODES)

Ask the user exactly this:

> Which mode do you want for this session?
>
> 1. **Draft** — write a new manuscript (or new sections) from project data
> 2. **Review** — read an existing .docx manuscript and give reviewer-style feedback
> 3. **Revise** — read an existing .docx manuscript and suggest section-by-section revisions (with or without reviewer comments)
> 4. **Proofread** — read an existing .docx manuscript and produce a language-level polish (no scientific restructuring)
> 5. **Audit** — read an existing .docx manuscript and report consistency and coherence issues across sections (numerical, terminological, cross-reference, argument-chain). Output is a severity-tagged report; the user fixes issues via Revise mode.

Based on the answer, load the corresponding mode reference file immediately:
- Draft → stay in SKILL.md body (no extra file needed)
- Review → `references/mode-review.md`
- Revise → `references/mode-revise.md`
- Proofread → `references/mode-proofread.md`
- Audit → `references/mode-audit.md`

**Do not proceed to Block 1 until the mode is confirmed.**

## Block 1 — Journal target (ALL MODES)

> Which journal is this manuscript for?
>
> 1. **Hydrogeology Journal** (Springer / IAH) — `hj`
> 2. **Journal of Hydrology: Regional Studies** (Elsevier) — `jhrs`
> 3. Something else — please paste the author guidelines or pick the closest match above.

Load either `references/journal-hydrogeology.md` or `references/journal-jhrs.md` and keep it in mind throughout the session. All five modes need the journal style: Draft uses it for writing, Review and Revise use it to check compliance, Proofread uses it for terminology rules, Audit uses it for journal-specific consistency checks.

---

## Draft mode path (Blocks 2–5)

If mode = Draft, continue with Blocks 2–5 below. If mode is anything else, skip to the **Non-Draft path** further down.

### Draft fast path (project preset)

Before asking Blocks 2–5, scan `references/preset-*.md` (excluding `preset-example.md`) for any preset whose declared detection-trigger file exists in the current workspace. If a match is found:

1. Load the matching `references/preset-<project>.md`.
2. Read the data files listed in the preset using the Read tool and cache the values the preset tells you to cache.
3. Skip straight to Block 4 (manuscript metadata) and Block 5 (limitations) — Blocks 2 and 3 are preloaded.
4. Still ask the user: "I detected the `<project name from preset>` project and loaded the preset. Is that correct? If you want to override any cached values, tell me now."

To add a new project preset, copy `references/preset-example.md` to `references/preset-<your-project>.md` (or symlink it from `.local/`) and fill in the placeholders.

### Block 2 — Project data sources (Draft only)

> Tell me where the project data lives. For each of the following, give me the exact file path relative to the workspace root (or say "none"):
>
> - Main results table(s) — CSVs with the numbers that will end up in the paper
> - Model / method source code — Python, R, or notebook files that define equations, algorithms, parameters
> - Config / parameter files — YAML, JSON, or files defining bounds, thresholds, optimizer settings
> - Station / site metadata — spatial, temporal, or classification info
> - Figures directory — where generated plots live

Use the Read tool to load each file the user provides. Cache:
- Results CSVs: sample sizes, group counts, summary statistics, top/bottom performers, classification breakdowns
- Source code: every equation verbatim, parameter lists, optimizer settings, bounds
- Metadata: station counts, classification rules, coordinate system, study period

**If any file the user names is missing, stop and report it. Do not proceed with invented data.**

### Block 3 — Domain facts (Draft only)

> Give me the core facts about the study:
>
> - Study area (name, region, country)
> - Study period (exact start and end dates)
> - Coordinate system (e.g. WGS84, a UTM zone, or a regional projected CRS — give name and EPSG code)
> - What is being modelled or measured
> - Key variables with units
> - Performance thresholds or classification rules to enforce throughout

### Block 4 — Manuscript metadata (Draft only)

> Provide the manuscript identity:
>
> - Title (sentence case)
> - Authors — full names, affiliations, ORCIDs if available
> - Corresponding author email
> - Up to 5 keywords (HJ) or 6 keywords (JHRS)
> - Which sections to draft (default: all — Abstract through References)

### Block 5 — Limitations list (Draft only, mandatory)

> List the honest limitations of the study for the Limitations subsection. I will refuse to invent these. For each, give the limitation, its assessed impact, and a proposed remedy. Typical categories: temporal coverage, missing forcings, parameter uncertainty, cross-validation, unvalidated coefficients, process simplifications, comparison with alternatives, single- vs. multi-objective calibration.

Cache the complete list — every item goes verbatim into the Limitations subsection.

---

## Non-Draft path (Review, Revise, Proofread, Audit)

If mode is Review, Revise, Proofread, or Audit, replace Blocks 2–5 with the following:

### Block 2′ — Manuscript file path

> Give me the path to the `.docx` manuscript you want me to work on.

Verify the file exists. If it's a `.doc` (legacy), convert to `.docx` first via the public docx skill before continuing.

### Block 3′ — Manuscript extraction

Run the extraction protocol in SKILL.md → "Reading existing manuscripts". Present the extraction summary to the user and wait for confirmation.

### Block 4′ — Mode-specific questions

**If mode = Review:** Ask the user:
> What is the focus of the review? Options: (a) general reviewer report covering everything, (b) focused on a specific section, (c) focused on a specific concern (e.g. methods rigour, citation coverage, figure quality, language only). Default: (a) general report.

**If mode = Revise:** Ask the user:
> Do you have reviewer comments to address? Paste them now if yes, or say "no — propose your own revisions" if you want me to do a critical read and suggest revisions from scratch.
>
> Also: should I revise the whole manuscript, or focus on specific sections?

If the user pastes reviewer comments, number them sequentially and cache them. Every revision suggestion must map to a specific comment number.

**If mode = Proofread:** Ask the user:
> Proofread scope: (a) language only — grammar, clarity, conciseness, (b) language + journal style compliance (terminology, abbreviations, citation format, equation formatting), (c) language + style + reference list verification. Default: (b).

**If mode = Audit:** Ask the user:
> Audit scope: (a) full audit — all 8 checks (coherence chain, numerical, terminological, cross-reference, argument honesty, tense, citation usage, JHRS Highlights/Abstract if applicable), (b) consistency only — skip the argument-chain check, run only the mechanical consistency checks (numerical, terminological, cross-reference, tense, citation), (c) coherence only — focus on the argument-chain check and skip mechanical consistency. Default: (a). Full audit is slower but the argument-chain check is where the most damaging issues hide.

---

## Confirm readiness (all modes)

After all applicable blocks are complete, report:

> **Mode:** [Draft / Review / Revise / Proofread]
> **Journal:** [HJ / JHRS]
> **[Draft-specific]** Data loaded: [summary of cached values, N stations/samples, period, study area]. [N] limitation items cached.
> **[Non-Draft]** Manuscript loaded: <filename>. [extraction summary].
> Semantic Scholar citation resolution active. Ready to proceed — confirm to begin.

Wait for explicit confirmation before acting.

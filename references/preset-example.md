# Preset — Example Project Template

This file is a **template** for defining a project-specific fast-path preset. It is not loaded automatically.

To create a real preset:

1. Copy this file to `references/preset-<your-project-name>.md` (or keep it private at `.local/preset-<your-project-name>.md` and symlink it from `references/` if you want auto-detection without exposing project details to the repo).
2. Fill in every `<placeholder>` with values from your project.
3. The fast-path mechanism in `SKILL.md` and `references/startup-interview.md` picks up any `references/preset-*.md` file (other than `preset-example.md` itself) whose declared detection trigger matches a file in the current workspace.

A project preset lets `paper-agent` skip the generic Block 2 (data sources) and Block 3 (domain facts) startup questions when it recognises the workspace, jumping straight to manuscript metadata (Block 4) and Limitations (Block 5). It also locks in project-specific Semantic Scholar search queries and forbids invented values.

## Detection trigger

Declare one workspace file path whose presence signals the project. The fast-path matches by file existence:

**Trigger file:** `<workspace/your-signature-results-file>.csv`

If you do not want a fast-path detection (manual preset selection only), set this to `<none — load manually>`.

## Files to read and cache

| File path | What to extract and cache |
|---|---|
| `<workspace/results-file>.csv` | sample sizes; group counts; summary statistics (mean ± SD of key metrics); top-N and bottom-N units by primary metric; classification breakdowns |
| `<workspace/comparison-file>.csv` | per-unit baseline vs. alternative metric; count of units where alternative wins |
| `<data/metadata-file>.csv` | unit metadata; spatial/temporal classifications; group labels |
| `<src/model-code>.py` (lines `<N>`–`<M>`) | governing equations verbatim; parameter lists per variant |
| `<src/calibration-code>.py` | parameter bounds table; optimizer settings; any auxiliary procedures |

If any file is missing, report `File <path> not found. Please verify the workspace structure before continuing.` and do not proceed with invented data.

## Cached project facts

- **Study period:** `<YYYY-MM-DD>` to `<YYYY-MM-DD>` (fixed)
- **Coordinate system:** `<CRS name, EPSG:<code>>`
- **Study area:** `<region, country>`
- **Model variants and parameter counts:**
  - `<variant 1 name>`: `<N>` parameters (`<list of parameter symbols>`)
  - `<variant 2 name>`: `<N>` parameters (`<list>`)
  - `<additional variants as needed>`
- **Classification rule:** `<one-sentence rule that splits units into groups>`
- **Performance thresholds:** `<Good metric ≥ X; Medium Y–X; Low < Y>`
- **Optimizer:** `<library.function (algorithm)>, <N> random starts, <ftol/xtol>, <maxfev/maxiter>, <any auxiliary scan range>`
- **<Any other project-locked facts>:** `<value>`

## Abbreviations to define on first use

`<list of project-specific abbreviations the manuscript will use>`

## Mandatory limitations

Format each as *limitation → assessed impact → proposed remedy*. List every honest limitation so the Draft-mode workflow can paste the section verbatim. The Draft workflow refuses to invent limitations, so this list must be complete.

1. **`<limitation name>`** — `<assessed impact and proposed remedy>`
2. **`<limitation name>`** — `<assessed impact and proposed remedy>`
3. ...

## Semantic Scholar search queries by section

Pre-curated queries for the citation workflow. Each query is run once per section as needed, with `limit=5`. Project-specific queries make literature resolution faster and more relevant than generic prompts.

**Introduction:**
- `"<topic keywords 1>"`
- `"<topic keywords 2>"`

**Materials and methods:**
- `"<method keywords 1>"`
- `"<method keywords 2>"`

**Results:**
- `"<benchmark keywords>"`

**Discussion:**
- `"<interpretation keywords 1>"`
- `"<interpretation keywords 2>"`

## Forbidden content

- ❌ Invented unit names, coordinates, metric values, or parameter values
- ❌ Methodologies not present in the cached source files
- ❌ Fabricated citations or DOIs not returned by Semantic Scholar
- ❌ Any reference to `SKILL.md` or preset files in the manuscript output

## Candidate figure pool (not a prescription)

Each candidate must still pass the four-question necessity assessment in `SKILL.md` before being proposed.

| Candidate | Typical necessity rationale | Likely to pass? |
|---|---|---|
| `<spatial performance map>` | shows pattern that prose and tables cannot convey | Usually yes |
| `<representative time-series fits, best/median/worst>` | shows fit-quality shape across the metric distribution | Usually yes — limit to 3 panels |
| `<metric distribution figure>` | only if the distribution is non-trivial (bimodal, long tail) | Conditional |
| `<comparison scatter, baseline vs. alternative>` | only if the alternative wins often enough to matter | Conditional |
| `<study area map>` | only if the Discussion depends on geographic features the reader cannot infer from one sentence | Interrogate hard |
| `<parameter distribution boxplots>` | only if the Discussion uses the distributions, not single values | Conditional |

Aim for **4 figures total** for a full research paper. If the assessment cuts none of your candidates, you are probably not being strict enough.

## Mandatory tables

- **Table 1:** `<e.g., parameter bounds read from the cached calibration code>`
- **Table 2:** `<e.g., summary performance statistics by group>`
- `<add more if your project requires>`

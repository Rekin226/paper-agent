# Preset — Demo Alluvial Fan (SYNTHETIC)

Auto-detection preset for the bundled Draft demo in `examples/demo-draft/`. It exists so a new user can run Draft mode against the demo with zero interview friction. All facts are **synthetic** — see `examples/demo-draft/project_notes.md`.

This preset only triggers when the demo's signature file is present at its repo-relative path, so it never activates in a real project workspace.

## Detection trigger

**Trigger file:** `examples/demo-draft/calibration_results.csv`

## Files to read and cache

| File path | What to extract and cache |
|---|---|
| `examples/demo-draft/calibration_results.csv` | 6 wells; per-well `kge_cal`, `kge_val`, `rmse_val_m`, `recession_a`, `recharge_b`; coastal/inland split |
| `examples/demo-draft/wells.csv` | well coordinates, coastal/inland class, screen depth |
| `examples/demo-draft/gw_levels.csv` | seasonal GWL series per well (long format) |
| `examples/demo-draft/project_notes.md` | fixed facts, abbreviations, mandatory limitations, citation query hints |

If any file is missing, report `File <path> not found.` and do not proceed with invented data.

## Cached project facts

- **Study period:** 2018-01 to 2020-12 (fixed; seasonal January/July sampling)
- **Study area:** Demo Alluvial Fan (synthetic — fictional coastal–inland transect)
- **Wells:** 6 (3 inland, 3 coastal)
- **Model:** per-well gray-box single-tank water-balance ODE; recession term `recession_a`, recharge response `recharge_b`
- **Calibration:** differential evolution; model selection by validation KGE
- **Performance metrics:** KGE and RMSE on the validation period

## Abbreviations to define on first use

GWL, KGE, RMSE, ODE, DE

## Mandatory limitations

Use the three limitations listed in `examples/demo-draft/project_notes.md` verbatim in substance. Do not invent additional limitations.

## Semantic Scholar search queries by section

**Introduction:**
- `"alluvial fan groundwater dynamics"`
- `"lumped water balance aquifer model"`

**Materials and methods:**
- `"Kling-Gupta efficiency hydrological model"`
- `"differential evolution parameter calibration"`

**Discussion:**
- `"coastal aquifer seawater intrusion monitoring"`
- `"groundwater recession analysis"`

## Forbidden content

- ❌ Invented well names, coordinates, metric values, or parameter values beyond the cached files
- ❌ Any study-area claim presenting "Demo Alluvial Fan" as a real site
- ❌ Fabricated citations or DOIs not returned by Semantic Scholar
- ❌ Any reference to `SKILL.md` or preset files in the manuscript output

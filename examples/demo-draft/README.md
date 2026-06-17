# Draft demo — synthetic data → manuscript prose

Run paper-agent's **Draft** mode against this folder to watch it turn raw project files into journal-style manuscript text with resolved citations — without using any data of your own.

> All data here is **synthetic** (see `project_notes.md`). It is for exercising the skill, not for citation.

## Files

| File | Role |
|---|---|
| `wells.csv` | 6 synthetic monitoring wells with coordinates, coastal/inland class, screen depth |
| `gw_levels.csv` | seasonal groundwater levels per well (long format) |
| `calibration_results.csv` | per-well gray-box model results — `kge_val`, `rmse_val_m`, recession/recharge parameters (the *signature* file Draft mode keys on) |
| `project_notes.md` | fixed facts, abbreviations, mandatory limitations, and citation query hints |

## Run it

```
/paper-agent
```

1. **Mode:** Draft
2. **Journal:** Hydrogeology Journal (or JHRS)
3. **Data source:** point it at `examples/demo-draft/` (from the repo root, the bundled `references/preset-demo.md` fast-path may auto-detect it)
4. Confirm the metadata it reports back, then let it draft section by section.

## What to expect

- A short startup interview, then a report of what it loaded (6 wells, the metrics, the fixed facts) **before** writing anything.
- Draft prose for **Methods** and **Results** grounded only in the CSV values and `project_notes.md` — no invented numbers, no invented study-area facts.
- Inline citations resolved through Semantic Scholar (real papers), or a `[CITATION NEEDED]` marker rather than a fabricated reference.
- A pause-and-confirm after each section.

## What to look for (the point of the demo)

- It **does not invent** a study-area name, a parameter, or a sample size that isn't in the files — it uses "Demo Alluvial Fan (synthetic)" and the six wells as given.
- The Limitations it writes match the three in `project_notes.md` verbatim in substance — it will not manufacture new ones.
- The prose avoids the AI tells the skill is built to suppress (em-dash pile-ups, throat-clearing transitions, reflexive three-item lists).

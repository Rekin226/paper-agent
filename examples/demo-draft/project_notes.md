# Project notes — Demo Alluvial Fan (SYNTHETIC)

> **Synthetic dataset.** "Demo Alluvial Fan" is not a real place. Wells, coordinates, water levels, and calibration metrics were generated to exercise the skill, not to describe real measurements. Do not cite any value here as a scientific result.

These notes supply the fixed, non-inventable facts paper-agent needs so the anti-fabrication directive does not block Draft mode. They mirror the structure of a real project preset (see `references/preset-example.md`).

## Fixed project facts

- **Study period:** January 2018 to December 2020 (three years of seasonal observations: January and July each year).
- **Study area:** Demo Alluvial Fan (synthetic), a fictional coastal–inland aquifer transect.
- **Coordinate system:** geographic, decimal degrees (illustrative).
- **Wells:** 6 monitoring wells (`wells.csv`), classified `inland` (3) or `coastal` (3) by `class`.
- **Model:** a per-well gray-box single-tank water-balance ODE; each well is calibrated independently.
  - Recession term governed by `recession_a`; recharge response by `recharge_b` (`calibration_results.csv`).
  - Calibration by differential evolution; model selection by validation KGE.
- **Data split:** calibration on the earlier portion, validation on the later portion (the same split underlies `kge_cal` vs `kge_val`).
- **Performance:** report KGE (Kling–Gupta efficiency) and RMSE on the validation period.

## Abbreviations (define on first use)

GWL (groundwater level), KGE (Kling–Gupta efficiency), RMSE (root-mean-square error), ODE (ordinary differential equation), DE (differential evolution).

## Mandatory limitations (paper-agent will not invent these — list is authoritative)

1. **Sparse temporal sampling** — two observations per year cannot resolve sub-seasonal dynamics; impact: recession parameters are weakly constrained; remedy: higher-frequency logging.
2. **Independent per-well calibration** — no spatial regularization across wells; impact: parameters may be non-physical at poorly observed wells; remedy: joint or attribute-conditioned calibration.
3. **No uncertainty quantification** — single best-fit parameter sets only; impact: confidence in projections is unstated; remedy: ensemble or Bayesian calibration.

## Semantic Scholar query hints by section

- **Introduction:** "alluvial fan groundwater dynamics", "lumped water balance aquifer model"
- **Methods:** "Kling-Gupta efficiency hydrological model", "differential evolution parameter calibration"
- **Discussion:** "coastal aquifer seawater intrusion monitoring", "groundwater recession analysis"

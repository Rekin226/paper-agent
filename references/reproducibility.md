# Reproducibility — Data, Code, and Methods Replicability

Read this when drafting Methods, when drafting the back matter (Data Availability, Code Availability, Acknowledgements), and when reviewing or revising any manuscript for any of the supported journals. All of them require a Data Availability Statement and encourage a Code Availability Statement; reviewers increasingly require both. Check the loaded journal profile for the title-specific wording and placement.

A paper that fails reproducibility standards can pass peer review but get retracted later, or get cited as an example of poor practice. Get this right.

## What "replicable Methods" actually means

The standard is: a competent researcher in the same field, given only your Methods section, could rerun your study and obtain comparable results. For a hydrology paper this requires:

### Data sources

- **Forcing data:** Source (agency, dataset name, version), spatial resolution, temporal resolution, time period used, access URL or DOI. Example: "Daily precipitation was obtained from the `<national meteorological agency>` station network (`<URL>`, accessed `<YYYY-MM-DD>`) for `<YYYY-MM-DD>` to `<YYYY-MM-DD>` across `<N>` rain gauges within the `<study region>` basin."
- **Observation data:** Same level of detail. Number of stations, sampling frequency, instrument type if relevant, quality-control procedures applied.
- **Spatial data:** Coordinate system (e.g. `WGS84 / UTM zone <N>`, EPSG:`<code>`), source of basemaps and aquifer boundaries, elevation data resolution.
- **Pre-processing:** Every step that transformed raw data into model input. Gap-filling rules, filtering, aggregation, normalization. State the exact procedure, not just "data were quality-controlled".

### Software and computational environment

- Software name and version. "scipy 1.11.4", not just "Python".
- Operating system if it matters for results (rare in hydrology, common in numerical solver work).
- Random seed for any stochastic procedure (multi-start optimization, bootstrap, MCMC).
- Hardware if runtime is reported as a result.

### Model formulation

- Every governing equation with all symbols defined.
- Parameter ranges and bounds (preferably as a table).
- Initial conditions and boundary conditions.
- Numerical solver: method, time step, convergence tolerance, maximum iterations.
- Calibration objective function and any weighting.
- Calibration period vs. validation period (if separate). If you used the same period for both, say so explicitly — this is a known limitation, not a hidden one.

### Performance evaluation

- Every metric reported, with its formula or a citation to a standard reference.
- Sample size for each metric.
- Whether metrics are computed on calibration data, validation data, or both.

### What is NOT required

- Proprietary code does not need to be in the public repository. It does need to be described in enough detail for a competent reader to reimplement.
- Data that cannot be shared (commercial, sensitive, or licensed) must be named and the reason for non-availability stated. Do not omit it silently.

## Data Availability Statement

Both HJ and JHRS require this. It goes after the Conclusions and before the References (HJ) or in a labelled section near the end (JHRS).

Format options, in descending order of preference:

1. **Open data, deposited:** "All data used in this study are available at [repository] under DOI [doi]." Use a domain-appropriate repository: Zenodo, HydroShare, PANGAEA, figshare, or a national data center.
2. **Open data, third-party:** "Precipitation and groundwater level data are publicly available from [agency] at [URL]. Derived datasets (e.g. station classifications, aggregated time series) are archived at [DOI]."
3. **Restricted access with conditions:** "Raw observation data are owned by [agency] and available upon reasonable request to [contact]. Processed datasets used for modeling are archived at [DOI]."
4. **Restricted access, no sharing possible:** "Raw observation data cannot be shared due to [specific reason: licensing, sensitivity, ownership]. Aggregated and anonymized results are available at [DOI]." This is the weakest option and reviewers will challenge it.

**Never write:** "Data are available upon request" without further detail. Editors increasingly reject this as non-compliant with FAIR principles.

## Code Availability Statement

Strongly encouraged across the supported journals. JHRS in particular flags missing code statements as a desk-rejection trigger for computational papers.

Format:

> "Source code for the `<model name>` and the calibration pipeline is available at `https://github.com/<user>/<repo>` (commit `<hash>`) and archived at Zenodo under DOI `<doi>`. Analysis scripts that produced the figures and tables in this manuscript are included in the same repository under `/analysis/`."

Best practice:

- **GitHub for development, Zenodo for archival.** GitHub repos can be deleted; Zenodo DOIs are permanent. Use Zenodo's GitHub integration to mint a DOI from a release tag.
- **Pin the exact version used.** Cite a commit hash or release tag, not just the repository URL.
- **Include a README with installation instructions and a worked example.** A repository that does not run when cloned is worse than no repository.
- **License explicitly.** MIT, Apache 2.0, or BSD-3-Clause for permissive; GPL-3.0 for copyleft. No license means no one can legally reuse the code.

If code cannot be shared (proprietary, in-development, or institutionally restricted), the Methods section must contain enough detail for reimplementation, and the Code Availability Statement must say "Source code is not publicly available because [specific reason]. The model formulation is described in full in Section 2."

## Author Contributions / CRediT (JHRS required, HJ optional)

JHRS requires the CRediT taxonomy. The 14 roles are standardized by CASRAI:

| Role | What it covers |
|---|---|
| Conceptualization | Study design, framing the questions |
| Methodology | Developing or designing the methodology |
| Software | Programming, code development |
| Validation | Verifying results, reproducibility |
| Formal analysis | Statistical or computational analysis of data |
| Investigation | Conducting research, data collection |
| Resources | Providing materials, instruments, samples |
| Data Curation | Managing data, metadata maintenance |
| Writing — Original Draft | Drafting the initial manuscript |
| Writing — Review & Editing | Critical review, revisions |
| Visualization | Preparing figures and tables |
| Supervision | Oversight, mentorship of the work |
| Project administration | Coordination, management |
| Funding acquisition | Securing financial support |

Format for the manuscript:

> "**[Author 1 Initials]:** Conceptualization, Methodology, Software, Formal analysis, Writing — Original Draft, Visualization. **[Author 2 Initials]:** Methodology, Validation, Writing — Review & Editing, Supervision. **[Author 3 Initials]:** Resources, Data Curation, Funding acquisition."

Rules:
- Every listed author must have at least one CRediT role.
- Not every role needs to be assigned — only the ones that apply.
- The first author typically has Writing — Original Draft. The corresponding/senior author typically has Supervision.
- Funding acquisition belongs to whoever held the grants, not everyone on the paper.

## Conflict of Interest / Competing Interests

JHRS requires a labelled declaration. HJ recommends one.

Two valid forms:

> "The authors declare no competing interests."

or

> "Author X has received research funding from Company Y. Author Z serves on the advisory board of Organization W. The remaining authors declare no competing interests."

Disclose: paid consultancies, board memberships, stock holdings >5%, patents related to the work, employment by an entity with a financial stake in the outcome. Do not disclose: routine grant funding (that goes in Acknowledgements), employer-employee relationships unrelated to the work, personal opinions.

## Funding statement

Lists the grant numbers and funding agencies that supported the work. Goes in Acknowledgements (HJ) or a labelled Funding section (JHRS).

> "This work was supported by the `<funding agency>` under grant numbers `<grant-number-1>` and `<grant-number-2>`. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript."

The "no role in study design" clause is increasingly expected by editors and protects against perceived conflicts.

## Self-check before finalizing back matter

1. Is there a Data Availability Statement, and does it specify *what* data, *where*, and under *what conditions*?
2. Is there a Code Availability Statement (or an explicit, justified absence)?
3. If the manuscript is for JHRS, is there a CRediT statement covering every author with at least one role?
4. Is there a Conflict of Interest declaration?
5. Are funding sources listed with grant numbers?
6. Are all repositories cited in the manuscript actually live and reachable?
7. Are DOIs (when present) functional? Test them.

If any answer is no, fix before submission. These are the items most commonly missed by authors and most commonly flagged by editors at the desk-check stage.

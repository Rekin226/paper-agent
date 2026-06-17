# Audit demo — catch the planted inconsistencies

Run paper-agent's **Audit** mode against this short manuscript to watch it surface consistency failures that authors and reviewers routinely miss. The manuscript is **synthetic** and seeded with deliberate errors.

## Build the `.docx` and run

Audit mode reads `.docx`. Build it from the markdown source (nothing is committed — `*.docx` is gitignored):

```sh
pandoc examples/demo-audit/sample_manuscript.md -o examples/demo-audit/sample_manuscript.docx
```

Then:

```
/paper-agent
```

1. **Mode:** Audit
2. **Journal:** Hydrogeology Journal (or JHRS)
3. **Manuscript:** `examples/demo-audit/sample_manuscript.docx`

Audit returns a consistency report with severity-tagged findings (Critical / Major / Minor). It does **not** edit the file.

## Answer key — what Audit should catch

The source manuscript (`sample_manuscript.md`) contains these planted inconsistencies. Use this to verify the report:

1. **Temporal error (Critical).** The Abstract claims "six years of monitoring (January 2018–December 2022)", but 2018–2022 is **five** years.
2. **Sample-size drift (Critical).** Abstract and Methods say **33** wells; Results says "across all **35** wells".
3. **Argument-honesty conflict (Critical).** The Abstract claims coastal levels "showed a strong correlation" with the tidal signal, but Results report the correlation was **not significant** (rho = 0.02, p = 0.94) — the Abstract overstates a null result.
4. **Aim-vs-conclusion mismatch (Major).** The Introduction states the objective is "to quantify recharge rates", but the Abstract and Conclusions claim the study "quantifies groundwater–surface-water exchange" — a different quantity than the stated aim.
5. **Broken cross-reference (Major).** The Results text refers to "Figure 3", but only Figure 1 and Figure 2 are captioned.
6. **Terminology drift (Minor).** The recession parameter is called the "recession coefficient" in Methods/Results and the "depletion constant" in Methods/Table 1 — two names for one quantity.

A good Audit run flags all six (it may phrase or group them differently, and may surface additional minor issues). If it misses a Critical item, that's a regression worth filing.

# Mode — Audit

Read an existing manuscript end-to-end and report consistency and coherence issues across sections. Output is a structured, severity-tagged report in chat. **No edits to the file. No revision proposals.** The audit identifies issues; the user starts a Revise session to fix them.

Audit is the orchestrator mode. Where Review evaluates scientific quality, Revise proposes specific text changes, and Proofread polishes language, Audit asks one question across the whole manuscript: **does this paper hold together as a single coherent document?**

**Apply `references/anti-fabrication.md` rigorously.** Every finding must quote the exact text being audited. Do not assert an inconsistency without showing both occurrences side by side. Do not infer what the author "must have meant" — flag the ambiguity instead.

## Philosophy

A manuscript is a chain of arguments. The Introduction promises a gap will be filled; Methods describes how; Results reports what was found; Discussion interprets; Conclusions claims what was contributed; Abstract summarizes; Highlights distill. Each link must hold.

The same chain runs in parallel for every shared element: every numerical value that appears in multiple sections must be the same; every term used twice must be spelled the same way; every figure referenced must exist; every abbreviation used must be defined.

Audit catches the failures editors and reviewers catch on first read: the Abstract claims `<N+1>` stations but Methods says `<N>`; the Introduction's gap statement is "no study has tested X" but the Conclusions claim "we have shown Y"; Fig. 3 is referenced twice in §3.2 but the caption list ends at Fig. 2; the Highlights list four findings but only three appear in Results; the Limitations admit the model is uncalibrated for units with metric below threshold but the Conclusions claim model transferability.

These failures are unglamorous, easy to miss when drafting section-by-section, and very visible once the manuscript is read as a whole.

## Before auditing

1. **Extraction complete.** Run the extraction from SKILL.md → "Reading existing manuscripts" and confirm with the user. Audit is more demanding of the extraction than other modes — it needs the full text of every section, the complete reference list, every figure and table caption, and every equation. If the extraction reported gaps, those gaps will limit what Audit can check; tell the user what is and is not auditable before proceeding.
2. **Journal reference file loaded.** Some consistency rules are journal-specific (HJ uses "groundwater"; JHRS uses Elsevier citation format; both have specific section structures Audit can verify).
3. **Anti-fabrication file loaded.** Findings must be sourced to exact manuscript passages.

## The audit protocol

Run the following checks in order. Each check produces zero or more findings for the report. Do not skip a check because earlier checks found issues — Audit is comprehensive by design.

### Check 1 — Coherence chain

Build a one-paragraph summary of each of these elements, in this exact order, from the manuscript:

1. **The gap statement** — the single sentence in the Introduction that names what is unknown
2. **The study objectives** — the explicit list in the Introduction of what this study does
3. **The methods scope** — what Methods actually describes the study as doing
4. **The reported results** — what Results actually shows
5. **The interpretation** — what Discussion interprets the results as meaning
6. **The conclusions** — what Conclusions claims the study contributed
7. **The abstract narrative** — what the Abstract says the paper is about
8. **The Highlights** — what the Highlights (if present) distill as the key findings

Then check each link in the chain:

- **Gap → Objectives:** Do the stated objectives directly address the gap? If the gap is "no study has tested X" and the objectives are "we developed Y", these are not aligned. Flag.
- **Objectives → Methods:** Does Methods describe doing every objective? Does Methods do things that aren't in the objectives? The former is a coverage gap; the latter is scope creep.
- **Methods → Results:** Does Results report on every method described? Are there results for analyses Methods didn't describe?
- **Results → Discussion:** Does Discussion interpret every major result? Does Discussion make claims not supported by Results?
- **Discussion → Conclusions:** Do the Conclusions follow from Discussion, or do they overreach? Does the paper claim more than it showed?
- **Conclusions → Abstract:** Does the Abstract summarize the same paper the Conclusions describes?
- **Abstract → Highlights:** Does each Highlight bullet correspond to a real finding in the manuscript, in the same words or close to them?

Findings from this check are usually **Critical** (the paper has an internal logical break) or **Major** (the chain bends but does not break).

### Check 2 — Numerical consistency

Build a table of every numerical value that appears in two or more sections. Examples:
- Total sample size (N stations, N samples, N events)
- Subgroup sample sizes (e.g. `<subgroup 1>` / `<subgroup 2>`, control/treatment)
- Study period (start year, end year, duration)
- Key performance metrics (overall `<metric>`, mean `<metric>`)
- Spatial extent (basin area, region size)
- Threshold values (`<metric>` ≥ `<value>` for the "Good" class, etc.)
- Parameter counts (number of model parameters per variant)

For each value, verify it is stated identically in every section. Acceptable variations:
- Rounding consistent with significant-figures policy (`<value>` in Abstract, full precision in Results table)
- Range vs. specific value when the range is established and the specific is a particular case
- Units conversions that are explicitly noted

Unacceptable:
- Same value, different number ("`<N>` stations" vs "`<N+1>` stations")
- Same value, inconsistent rounding (e.g. `0.74` in Abstract, `0.75` in Results)
- Same value, inconsistent units (m vs cm without conversion)
- Date inconsistency ("`<YYYY-YYYY>`" vs "`<YYYY+1-YYYY>`")

Findings here are usually **Critical** for sample sizes and primary metrics (editors check these), **Major** for secondary metrics.

### Check 3 — Terminological consistency

Build a list of every term, abbreviation, and parameter symbol used in two or more sections. Check:

- **One word vs. two words:** "groundwater" must be consistent. "`<compound term>`" or "`<compoundterm>`" must be consistent. Journal style file specifies the correct form; flag any deviation.
- **Abbreviation casing:** "RMSE" not "Rmse"; "`<ABBR>`" not "`<abbr>`".
- **Abbreviation introduction:** Every abbreviation used must be defined on first occurrence. Flag abbreviations used before definition, defined but not used, or defined twice.
- **Parameter symbols:** `<symbol>` must be `<symbol>` everywhere, not sometimes spelled out as `<spelled-out-form>` or with different casing. Same for every model parameter.
- **Variable names in text vs. equations:** If the equation uses `h`, the prose must use `h`, not `H` or "`<full-name> h`".

Findings here are usually **Minor** unless the inconsistency causes scientific ambiguity (e.g. two different definitions of `R²`), in which case **Major**.

### Check 4 — Cross-reference integrity

- Every "Fig. N" reference in the body must have a corresponding figure caption.
- Every "Table N" reference must have a corresponding table caption.
- Every "Eq. (N)" reference must have a corresponding numbered equation.
- Every "Section X.Y" or "§X.Y" reference must point to a real section.
- Every "Section X.Y" reference outside the Introduction must point *backward*. A body section that cites a later section forces the reader to jump ahead or hold an unresolved promise; report each one with its location and the section it points to. See `references/anti-ai-style.md` for the rule and the exemptions (Introduction roadmap; the Conclusion, which is exempt by construction).
- Every figure, table, and equation that exists must be referenced in the body at least once.
- Every reference list entry must be cited in the body at least once.
- Every in-text citation must have a matching reference list entry.

These integrity checks were partly run during extraction. Audit re-runs them and reports them in the structured format. Findings here are **Critical** for missing figures/tables (you cannot submit a manuscript that references nonexistent content) and **Major** for unused entries (orphan figures or uncited references).

### Check 4b — Reference existence (does the cited work exist?)

Checks 1–4 verify the manuscript is internally consistent. This one verifies it is consistent with reality. A reference list can be perfectly self-consistent and still cite papers that do not exist, which is the single most damaging thing a reviewer can find.

Take `reference_dois` from the extractor's `--json` output and pass them to `mcp__openalex__batch_resolve_references`, 20 at a time. Then compare each resolved record's `title`, first author, and `publication_year` against the manuscript's entry.

| Finding | Severity |
|---|---|
| DOI does not resolve | **Critical** — fabricated or malformed reference |
| DOI resolves to a different paper than the entry describes | **Critical** — misdirects the reader; also the signature of a borrowed DOI |
| Right paper, wrong year or misspelled author | **Minor** — metadata drift |
| Entry has no DOI at all | **Minor** — note it; verify by title lookup if the claim it supports is load-bearing |

Report as counts, not prose: `Reference existence: 23 DOIs checked, 21 resolved, 1 unresolvable (Critical), 1 mismatched (Critical), 4 entries without DOI`.

If the manuscript has no DOIs in its reference list at all, say that plainly and mark this check **not run**. Do not report it as passing.

If `mcp__openalex__*` is unavailable in this environment, this check cannot run at all. Mark it **not run (no resolver available)** and say so in the report header, so the user does not read a clean audit as a verified reference list. Sampling a few titles through `mcp__semantic-scholar__search_papers_match` is a partial substitute, not a replacement.

### Check 5 — Argument honesty

Read the Limitations subsection. Then read the Conclusions and Abstract. Check whether the paper's strongest claims are consistent with what the limitations admit:

- If Limitations admits "model not validated against independent data", do Conclusions claim "transferable across `<study settings>`"? Conflict.
- If Limitations admits "single-objective calibration", does Discussion claim "robust optimal parameter values"? Conflict.
- If Limitations admits "temporal coverage `<period>` may not capture inter-annual variability", does the Abstract claim "long-term `<process>` dynamics"? Conflict.

This is the subtlest check. Findings are usually **Major**. The fix is rarely to remove limitations (which would be dishonest); it is to soften the overclaim.

### Check 6 — Tense consistency

For each major section, sample 5–10 sentences and verify tense matches the journal's rules from the loaded journal reference file:
- Methods: past tense ("was calibrated", "were measured")
- Results: present tense ("achieves", "shows") — journal-dependent; JHRS allows past
- Discussion: present tense

Findings here are **Minor** unless the section is uniformly wrong-tensed, in which case **Major**.

### Check 7 — Citation usage consistency

Sample 5–10 in-text citations that appear in two or more sections. For each:
- Same author/year format throughout (HJ: no comma; JHRS: comma)
- Same paper being cited (not a different paper with the same first author)
- Consistent role: if §1 cites Smith (2018) for "showed X", §4 should not cite Smith (2018) for "showed Y" unless the paper actually showed both

Findings here are usually **Minor**.

### Check 8 — Highlights and Abstract integrity (JHRS only)

If the journal is JHRS, additionally check:
- Highlights: 3–5 bullets, each ≤85 characters including spaces
- Each Highlight must correspond to a finding stated in Results
- Abstract has the three required labelled sections (Study Region / Study Focus / New Hydrological Insights for the Region)
- Each section of the Abstract corresponds to real content in the manuscript

Findings here are **Critical** — these are JHRS desk-rejection triggers.

## Severity levels

- **Critical** — manuscript cannot be submitted in current form. Includes: gap-objectives misalignment so severe the paper does not deliver what it promises; primary sample size or key metric inconsistency; missing figure/table referenced in body; JHRS structured abstract or Highlights missing/malformed.
- **Major** — must fix before submission. Includes: secondary metric inconsistency; conclusions exceeding what limitations allow; uniformly wrong tense in a section; terminology inconsistency affecting scientific meaning.
- **Minor** — should fix. Includes: stylistic terminology drift (e.g. "groundwater" vs "ground water" in different sections); occasional tense slip; orphan unused reference entries; citation format minor variations.

## Report format

Output the report in chat using this exact structure:

```
# Audit Report — <manuscript title>

**Journal target:** [HJ / JHRS]
**Date:** [today]
**Auditor:** Paper Agent (consistency and coherence pass)

## Summary

- **Critical findings:** N
- **Major findings:** N
- **Minor findings:** N
- **Audit limitations:** <if extraction was incomplete, what could not be audited>

## Verdict

<One of:
 - "Ready for submission after addressing N Minor findings."
 - "Substantial revision needed: N Major and N Minor findings. Recommend Revise mode."
 - "Not submittable in current form: N Critical findings must be resolved first. Recommend Revise mode immediately."

Justify in 2–3 sentences citing the most consequential findings.>

## Critical findings

<For each Critical finding:

**[C1] <one-line title>**

*Category:* [Coherence chain / Numerical / Cross-reference / Argument honesty / Journal-mandatory]

*Evidence (quoted from manuscript):*
> Section X.Y: "<exact quote>"
> Section A.B: "<exact quote>"

*Issue:* <2–3 sentences explaining the conflict>

*Recommended action:* <Specific. "Update Abstract sample size from <N+1> to <N> to match §2.1" not "fix the inconsistency">

>

## Major findings

<Same format, numbered M1, M2, ...>

## Minor findings

<Same format, numbered m1, m2, ... Can be more concise — single-line evidence acceptable for clear-cut terminology issues>

## Coherence chain summary

<For documentation, show the chain Audit built. This is useful for the user
to verify Audit understood the manuscript correctly. Format:

**Gap:** <one sentence quoted or paraphrased from Introduction>
**Objectives:** <one sentence>
**Methods scope:** <one sentence>
**Results:** <one sentence>
**Discussion:** <one sentence>
**Conclusions:** <one sentence>
**Abstract narrative:** <one sentence>
**Highlights:** <bullet count and one-sentence summary>

If any link could not be summarized from the manuscript, say so explicitly. That itself is a finding.>

## Next steps

<Tell the user what to do:
 - If 0 Critical, 0 Major findings: "Manuscript is internally consistent. Address Minor findings via Proofread mode, then submit."
 - If Major findings only: "Start a Revise session and address Major findings first. Re-run Audit after revisions."
 - If Critical findings: "Critical findings block submission. Start a Revise session and resolve them before any further work. Re-run Audit after each Critical is fixed.">
```

## Tone

Forensic, not judgmental. The audit is not a review of scientific quality — it is a structural inspection. Quote the manuscript verbatim. State the inconsistency in neutral terms. Recommend the specific fix without speculation about why the inconsistency exists.

Good: "Abstract states 'across `<N>` monitoring stations' (line 12). §2.1 states 'a total of `<N+1>` `<unit-class>` stations were monitored' (line 87). Update one to match the other; verify against cached data which is correct."

Bad: "The Abstract appears to contradict §2.1 regarding the number of stations, suggesting the author may have miscounted or updated the dataset partway through writing. Please clarify."

The first version is auditable, specific, and actionable. The second is speculative and patronizing.

## What Audit mode does NOT do

- Does not edit the .docx file
- Does not propose BEFORE/AFTER revisions (that is Revise mode)
- Does not produce reviewer-style scientific feedback (that is Review mode)
- Does not fix line-level grammar (that is Proofread mode)
- Does not verify external citations against their source papers (that is Review mode's citation sampling)
- Does not flag AI-style markers (that is Proofread mode using `anti-ai-style.md`)
- Does not evaluate scientific novelty, originality, or contribution magnitude
- Does not check whether claims are true — only whether claims are consistent with each other across the manuscript

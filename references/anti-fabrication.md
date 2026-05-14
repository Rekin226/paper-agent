# Anti-Fabrication Rules — When in Doubt, Ask or Flag

This is the single most important rule in this skill. Read it before any writing, revision, review, or proofreading work.

## The principle

**If you do not know something with confidence, either ask the user or flag the gap. Never fill in a plausible-sounding answer.**

A fabricated fact in an academic manuscript is worse than a missing one. A missing fact is visible and can be fixed. A fabricated fact looks like a real fact and gets cited, repeated, or built upon by readers who trust the source. The agent's job is to produce text the user can defend to a reviewer or an examination committee. Every sentence must be traceable to a real source.

This applies to all five modes (Draft, Review, Revise, Proofread, Audit) and to every kind of content the agent produces.

## What counts as fabrication

Fabrication is anything the agent writes that is presented as fact but is not grounded in one of:

1. A file the agent has read (cached workspace data, source code, the existing .docx manuscript)
2. A Semantic Scholar–resolved citation
3. Information the user has provided in this session or in a loaded preset
4. A claim explicitly framed as the agent's interpretation, hedged appropriately

Anything else, regardless of how plausible it sounds, is fabrication.

## Specific failure modes to watch for

### Citations and references

- **Inventing a citation to support a claim.** If a claim needs support and Semantic Scholar returns nothing, the placeholder `[CITATION NEEDED: <topic>]` stays. Do not insert a real-looking but unverified `(Author, Year)` citation. Do not pad reference lists with plausible-sounding entries.
- **Inventing DOIs.** Use `externalIds.DOI` from Semantic Scholar. If absent, omit the DOI rather than constructing one.
- **Inventing author names, journal names, or page numbers.** All bibliographic fields come from the Semantic Scholar result.
- **Misattributing claims to real citations.** If you cite Author (Year), the cited paper must actually contain the claim. Do not extend a real citation to cover a claim the paper does not make.

### Numerical facts

- **Inventing values absent from cached files.** If the user did not provide a value and it is not in any read file, ask. Do not write "approximately 1,800 km²" or "around 50 stations" or "roughly 10 years" to fill space.
- **Inventing precision.** If the cached value is "0.74", do not write "0.7421". If the data is monthly, do not present daily-level claims.
- **Inventing sample sizes.** "`<N>` stations" must be in the cached data. Not "`<N>`", not "`<N>` stations". Both require a source.
- **Inventing units or conversions.** If the cached value is in metres, do not convert to feet "for general readers" without verifying the conversion and noting it.
- **Inventing uncertainty.** If a cached value is reported as a point estimate, do not add a fabricated ± SD or CI. Either report the point estimate or flag the missing uncertainty.

### Methodological facts

- **Inventing software versions.** "scipy was used" in cached files does not license "scipy 1.11.4 was used" in the manuscript.
- **Inventing parameter rationale.** If the source code shows `ftol=1e-8` with no documentation, do not write "this tolerance balances precision against runtime." Either ask the user why this value was chosen, or write "Convergence tolerance was set to ftol = 1×10⁻⁸" with no justification.
- **Inventing random seeds.** If the code uses `np.random.seed(42)`, that is fact. If no seed is set, do not invent one for the manuscript.
- **Inventing calibration vs. validation period splits.** If the cached files do not distinguish, the manuscript must not distinguish. Ask the user before introducing a split that is not in the data.
- **Inventing solver, optimizer, or convergence details** beyond what the source code shows. Real values from code; flagged gaps otherwise.

### Study area and context

- **Inventing geological, climatic, or geographic facts.** Basin area, mean annual precipitation, aquifer type, soil class, population, agricultural fraction — every such number needs a citation or a user-supplied value. Do not write background "from general knowledge."
- **Inventing administrative or political context.** Year of water management policy changes, names of governing agencies, regulatory thresholds — all need sources.
- **Inventing prior study counts.** Do not write "several previous studies have addressed this" or "no published study has examined" without Semantic Scholar evidence. Both claims are factual and both can be wrong.

### Physical and scientific interpretation

This is the subtlest failure mode. Discussion sections invite speculation, but speculation must be labelled.

- **Acceptable:** "Higher `<parameter>` values at `<subgroup 1>` stations may reflect deeper recharge pathways, consistent with Smith et al. (2018) who reported similar patterns in alluvial settings."
- **Acceptable:** "One possible interpretation is that the bimodal `<parameter>` distribution reflects two connectivity regimes, although this hypothesis requires field validation."
- **Acceptable:** "The mechanism behind the `<subgroup>` underperformance is unclear from the present data."
- **Not acceptable:** "The bimodal `<parameter>` distribution reflects two distinct connectivity regimes" (asserted as fact without evidence)
- **Not acceptable:** "`<subgroup>` stations underperform because of `<process>` interference." (causal claim without supporting evidence in the cached results)
- **Not acceptable:** "This is a well-known phenomenon in `<class of system>`." (vague appeal to consensus, no citation)

The rule: causal claims, mechanistic explanations, and "well-known facts" all require either a Semantic Scholar–resolved citation or an explicit hedge ("may", "one possible interpretation", "we hypothesize"). If a sentence can be read as asserted fact, it must be defensible as such.

### Author metadata

- **Inventing affiliations, ORCIDs, or emails.** If the user does not provide them, the agent must ask. Do not guess from author names or generate plausible institutional addresses.
- **Inventing CRediT assignments.** Author contributions come from the user, not from the agent's guess about who likely did what.
- **Inventing funding sources or grant numbers.** Same rule. Ask.

### Manuscript content (Review, Revise, Proofread, Audit)

- **Inventing manuscript text.** If extraction failed on a section, do not fill in what the section "probably" says based on context. Stop and re-extract, or report the gap.
- **Inventing reviewer intent.** If a reviewer comment is ambiguous, ask the user to interpret it. Do not decide what they "really meant."
- **Inventing existing figures or tables.** Work only with figures and tables the extraction actually identified.
- **Inventing audit findings.** Every Audit-mode finding must quote the exact text being audited from both occurrences. Do not infer an inconsistency from a paraphrase.

## What to do instead

When the agent encounters a gap, there are exactly four acceptable responses:

### 1. Ask the user

For specific, answerable questions. Format:

> "I need [specific fact] to write [specific section]. The cached files do not contain this. Can you provide it, or should I leave a placeholder?"

Examples:
- "I need the mean annual precipitation for the `<study region>`. The cached files do not include this. Can you provide it with a source, or should I flag this as a gap?"
- "The reviewer comment R1.4 is ambiguous to me. Are they asking about (a) the choice of objective function, (b) the choice of optimizer, or (c) both? Or something else?"
- "I see scipy is imported but no version is pinned. What version was used for the final runs?"

Ask **before** writing. Do not write a sentence with a placeholder and then ask later.

### 2. Flag a gap inline

For places where the gap can be marked in the draft itself and addressed at revision. Use bracketed placeholders:

- `[CITATION NEEDED: <topic>]` — for unsourced claims
- `[VALUE NEEDED: <description>]` — for missing numbers
- `[VERIFY: <description>]` — for facts the agent has used but is uncertain about
- `[FROM USER: <description>]` — for facts the user must supply (metadata, funding, etc.)

Every placeholder must include enough description that the user can fix it without going back to the agent. `[CITATION NEEDED]` alone is useless; `[CITATION NEEDED: prior work on tidal loading in unconfined coastal aquifers]` is actionable.

At the end of each section, report the placeholder count and the list, so nothing is lost.

### 3. Search Semantic Scholar

For literature gaps that might be fillable. If a claim needs a citation and the agent has not yet searched, search before writing. Do not write the sentence first and search after — that biases the search toward confirming the sentence rather than testing it.

### 4. Decline to make the claim

For places where the claim cannot be supported and the manuscript does not require it. The simplest fix is often to delete the sentence. If Discussion has a paragraph about "the mechanism behind X" and no evidence supports any specific mechanism, the paragraph itself is the problem.

## Self-check before presenting any output

Before showing the user any drafted section, revision proposal, review comment, proofread edit, or audit finding, scan for fabrication. For each factual claim in the output, ask:

1. **What is the source of this fact?**
   - Cached file? Name the file.
   - Semantic Scholar citation? Name the result.
   - User-provided? Name the session input.
   - Hedged interpretation? Verify the hedge is present.
   - None of the above? Fabrication. Fix before presenting.

2. **For every number:** Where did this number come from?

3. **For every citation:** Did Semantic Scholar return this exact paper? Does the paper actually support the claim?

4. **For every "well-known", "established", "previous studies have shown":** Where is the citation?

5. **For every causal or mechanistic claim:** Is there evidence in the cached results, or is this an inference dressed as a fact?

6. **For every methodological detail:** Is this in the source code, or is the agent embellishing?

7. **For every Audit finding:** Are both quoted passages verbatim from the extracted manuscript, with exact section and line references?

If any answer is unclear, treat the claim as fabrication and revise before presenting.

## Why this matters

The user is a researcher who will defend this manuscript to reviewers, examination committees, or future readers. Every fabricated fact is a trap. The agent's value is producing text that survives scrutiny, not text that looks impressive.

A draft with twenty `[CITATION NEEDED]` placeholders is more useful than a draft with twenty plausible-sounding fabricated citations. The placeholders are honest and fixable. The fabrications are dishonest and dangerous.

When in doubt: ask, flag, search, or decline. Never invent.

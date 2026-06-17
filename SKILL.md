---
name: paper-agent
description: Full academic manuscript skill for quantitative-science papers, currently calibrated for hydrology and water-resources (Hydrogeology Journal, JHRS) and extensible to other quantitative-science fields via a journal style file. Five modes — Draft (write from scratch), Review (reviewer-style feedback), Revise (section-by-section revision suggestions, with or without reviewer comments), Proofread (language polish), Audit (consistency and coherence checks across the manuscript). Use whenever the user wants to draft, write, review, revise, polish, proofread, audit, edit, or respond to reviewer comments on a journal manuscript — especially for Hydrogeology Journal (HJ) or Journal of Hydrology Regional Studies (JHRS). Reads workspace data files and existing .docx manuscripts, resolves citations via Semantic Scholar, outputs publication-ready prose or structured feedback. Trigger on "write the paper", "draft the manuscript", "review my manuscript", "respond to reviewers", "revise section", "polish my draft", "audit my paper", "/paper-agent", or any manuscript writing/revision/review/audit request. Also triggers when the user uploads a .docx and asks for feedback or edits.
allowed-tools: Read, Glob, Grep, Bash, mcp__semantic-scholar__search_papers, mcp__semantic-scholar__get_paper, mcp__semantic-scholar__search_papers_match
---

# Paper Agent — Academic Manuscript Generator and Reviewer

Generate, review, revise, or proofread hydrology and water-resources manuscripts at journal-submission quality. Read project data or existing .docx manuscripts directly, resolve every citation inline via Semantic Scholar, and produce outputs calibrated to the user's chosen mode.

Never produce outlines, summaries, or bullet-point drafts in Draft mode. Every Draft-mode output is complete academic writing ready for direct manuscript development.

---

## MODES

This skill supports five distinct modes. The user selects one at startup (Block 0 of the interview). Each mode has its own reference file with specific workflow, output format, and boundaries.

| Mode | Input | Output | Reference file |
|---|---|---|---|
| **Draft** | Project data (CSVs, source code, metadata) | Complete manuscript sections, .docx export | Body of this SKILL.md |
| **Review** | Existing .docx manuscript | Reviewer-style feedback report in chat (no file edits) | `references/mode-review.md` |
| **Revise** | Existing .docx + optional reviewer comments | Section-by-section revision suggestions in chat (BEFORE / AFTER / RATIONALE blocks). Never edits the .docx file directly — user applies changes themselves. | `references/mode-revise.md` |
| **Proofread** | Existing .docx manuscript | Revised .docx with language-level fixes only. No scientific changes, no restructuring, no new citations. | `references/mode-proofread.md` |
| **Audit** | Existing .docx manuscript | Consistency and coherence report in chat with severity-tagged findings (Critical / Major / Minor). No edits, no revision proposals — identifies issues for the user to fix via Revise mode. | `references/mode-audit.md` |

**Mode determines what is allowed.** Once a mode is selected, re-read the relevant reference file to understand the specific protocol. Do not mix mode behaviours — e.g. Proofread must not restructure sections; Revise must not silently edit the .docx file; Review must not rewrite paragraphs.

---

## ANTI-FABRICATION DIRECTIVE — read `references/anti-fabrication.md` before any work.

This is the most important rule in the skill. If the agent does not know something with confidence, it asks the user, flags the gap, searches Semantic Scholar, or declines to make the claim. It never fills in a plausible-sounding answer. Applies to citations, numbers, study area facts, methodological details, physical interpretations, author metadata, and manuscript content read from existing files. The rules file enumerates the specific failure modes and the four acceptable responses.

## ANTI-SUMMARY DIRECTIVE — read `references/anti-summary-rules.md` before writing any section.

This is one of the two most common failure modes. The rules file is short and mandatory.

## ANTI-AI-STYLE DIRECTIVE — read `references/anti-ai-style.md` before writing any prose.

Manuscripts written by AI tend to give themselves away through stylistic tells: em-dashes, hedge words, throat-clearing transitions, three-item lists for everything, and long sentences padded with caveats. Reviewers notice. The rules file lists what to avoid and what good academic prose actually looks like. It applies to Draft mode, Revise mode (every AFTER block), and Proofread mode (which uses it as a compliance checklist).

---

## STARTUP SEQUENCE

Run once per session, before any writing or review. Follow `references/startup-interview.md` verbatim — it contains the exact questions, mode-specific branches, and fast-path rules.

**Block 0 — Mode selection (always first).** Ask which mode the user wants: Draft, Review, Revise, Proofread, or Audit. Load the corresponding reference file immediately.

**Block 1 — Journal target** (all modes). Load `references/journal-hydrogeology.md` or `references/journal-jhrs.md` based on the answer. The journal style matters for Review (is the manuscript HJ-compliant?), Revise (do the edits match journal style?), and Proofread (what terminology rules to enforce?), not just Draft.

**Remaining blocks branch by mode.** Read `references/startup-interview.md` for the full protocol.

**Draft-mode fast path:** If the workspace contains a recognised project-signature file declared by any `references/preset-<project>.md` (see `references/preset-example.md` for the template and detection convention), auto-load that preset and skip straight to journal selection + metadata. Still confirm with the user before writing.

After the interview, report data loaded, mode selected, journal selected, and wait for explicit confirmation before acting.

---

## READING EXISTING MANUSCRIPTS (Review, Revise, Proofread modes)

When the mode is Review, Revise, or Proofread, the user provides a path to an existing `.docx` manuscript. Before any analysis:

1. **Extract via the public `docx` skill if available, otherwise via `pandoc` directly.** First check for the public `docx` skill at `/mnt/skills/public/docx/SKILL.md` (Claude Code cloud) or `~/.claude/skills/docx/SKILL.md` (local install). If found, read its reading section and use it — it uses `pandoc` for text extraction plus direct XML access for structure. If neither path exists (common on local installs), extract directly: `pandoc <file>.docx -t markdown` for section text, and `unzip -p <file>.docx word/document.xml` for structure when needed. Either way, do not parse `.docx` with ad-hoc byte-level scripts.
2. **Extract and cache:**
   - Full text by section (Title, Abstract, Highlights if present, 1. Introduction, 2. Methods, ..., References)
   - All in-text citations (every `(Author Year)` or `(Author, Year)` occurrence)
   - Full reference list entries
   - Figure captions and table captions with their numbers
   - Equation count and numbering
   - Total word count and per-section word counts
3. **Cross-reference check:** Verify every figure and table referenced in the body exists in the caption list, and vice versa. Report any orphans or gaps.
4. **Citation integrity check:** Extract the author-year from each in-text citation and verify a matching entry exists in the reference list. Report unmatched citations or unused reference entries.
5. **Report the extraction summary to the user before proceeding:**
   ```
   Manuscript loaded: <filename>
   Sections: [list]
   Word count: N (Abstract: N, Introduction: N, ..., References: N entries)
   Figures: N  |  Tables: N  |  Equations: N
   Citations in text: N  |  Reference entries: N
   Integrity: [OK / N orphan citations, M unused references, K figure/table gaps]
   ```

**Do not proceed with mode-specific work until this extraction report is presented and the user confirms.** If the manuscript is a .doc (legacy Word), convert to .docx first using the method in the docx skill.

---

## DRAFT MODE — workflow below

The sections from here down (Citation workflow, Pause protocol, Section content guidance, QC, Export) apply to **Draft mode only**. For Review, Revise, or Proofread, read the corresponding mode reference file instead:

- Review → `references/mode-review.md`
- Revise → `references/mode-revise.md`
- Proofread → `references/mode-proofread.md`
- Audit → `references/mode-audit.md`

The **Figure necessity assessment** (further down) applies to all modes — Review checks whether existing figures earn their place, Revise can recommend cutting them, Draft gates new ones.

## CITATION WORKFLOW

Execute before drafting each section except the Abstract (most journals, including HJ, forbid citations in abstracts).

1. **Identify citation needs.** List the claims in the upcoming section that require literature support.
2. **Search Semantic Scholar.** One focused query per topic. Call `mcp__semantic-scholar__search_papers` with fields `paperId,title,authors,year,venue,externalIds,citationCount` and limit 5. Never batch unrelated topics into one query.
3. **Auto-select the best match.** Rank by: (a) topical relevance to the specific claim, (b) year — prefer 2010–present unless a seminal older work is clearly needed, (c) venue quality (peer-reviewed journal > conference > preprint), (d) citation count as a proxy for community acceptance. Select the single top-ranked result. If nothing scores adequately on relevance, insert `[CITATION NEEDED: <topic>]` inline and continue. Never insert a low-quality citation to fill a slot.
4. **Format in the journal's style.** Use the in-text and reference formats defined in the loaded journal reference file (`references/journal-hydrogeology.md` or `references/journal-jhrs.md`). Use `externalIds.DOI` when available.
5. **Insert inline + append to running reference list.** Place the formatted in-text citation at the exact sentence location. Append the full reference entry to a `## REFERENCE LIST` block that grows across the session, alphabetically sorted and deduplicated by DOI or title.
6. **Post-section citation summary.** After each section output, report:
   ```
   Citations resolved this section: N
   Unresolved [CITATION NEEDED] items: <list or "none">
   Running reference list total: N entries
   ```

**Never fabricate citations, DOIs, or author names.** If Semantic Scholar returns nothing useful, the placeholder stays.

---

## SECTION-BY-SECTION PAUSE PROTOCOL

After completing each section, stop and present:

> **[Section Name]** is drafted. Would you like to:
> **(A)** Continue to the next section
> **(B)** Revise this section before proceeding
> **(C)** Export what we have so far to .docx

Do not proceed to the next section until the user confirms. This is non-negotiable, it protects the user from long runs of drift.

## RECOMMENDED WRITING ORDER

If the user picks "all sections" or does not specify a starting point, recommend this writing order, not the IMRAD reading order:

1. **Materials and Methods** first. Methods is the most factual and least style-dependent section. Drafting it first surfaces gaps in cached data and equations early, before they propagate.
2. **Results** second. Now that Methods is fixed, every Results claim has a defined source.
3. **Discussion** third. Discussion benchmarks Results against the literature; both must exist first.
4. **Introduction** fourth. The Introduction's gap statement must align with what the paper actually delivers in Results and Discussion. Writing it last prevents the common failure of an Introduction that promises more than the Results show.
5. **Conclusions** fifth. Three to five paragraphs distilling Results and Discussion. Cannot be written without them.
6. **Abstract** sixth. The Abstract is a 250-word summary of a paper that already exists. Writing it first produces vague, generic abstracts.
7. **Title** last. Refine the working title once you know what the paper actually argues.
8. **Back matter** (Data Availability, Code Availability, CRediT, Conflict of Interest, Funding, Acknowledgements) at any point, but typically alongside Methods or as the final pass before export.

If the user explicitly asks to write a different section first (e.g. "draft the Introduction"), do that, but warn once: "Writing the Introduction before Results is harder because the gap statement and study objectives need to align with what the paper actually delivers. I can draft it now and we revise after Results, or draft it later. Which would you prefer?"

---

## SECTION CONTENT GUIDANCE

The section structure, verb tenses, required sub-headings, abstract format, and reference list format all come from the **loaded journal reference file**. Re-read that file before writing each section if you're unsure about a detail — do not guess.

Generic guidance that applies to both supported journals:

- **Abstract** — no citations. State the real cached numbers (sample sizes, key metrics). Follow the journal's required structure (HJ = single paragraph; JHRS = three labelled parts: Study Region, Study Focus, New Hydrological Insights for the Region). Write the Abstract LAST, after Discussion is drafted, not first.
- **Introduction** — read `references/introduction-structure.md` before drafting. The Introduction must follow the five-move funnel (broad significance → narrowing literature review → specific gap → study objectives → roadmap). Every cited paper must support a specific claim, not pad the section.
- **Materials and Methods** — past tense. Read `references/reproducibility.md` for the replicability standard. Every equation, parameter, and setting must come from the cached source files. Methods must include enough detail for independent replication: data sources with access details, software versions, parameter ranges, calibration period, optimizer settings, convergence criteria.
- **Results** — present tense. Every quantitative claim must cite a table, figure, or cached value. Refuse to write "the model performs well", always give numbers. Report metrics with sample sizes and uncertainty (SD or CI) where available.
- **Discussion** — present tense. Benchmark against Semantic Scholar–resolved references. Interpret fitted parameters physically. Do not restate results.
- **Limitations** (usually §4.5 in HJ, end of Discussion in JHRS) — mandatory. Write each as: *limitation → assessed impact → proposed remedy*. Use only the limitations the user supplied in the startup interview (or from the loaded preset). Do not invent.
- **Conclusions** — 3–5 paragraphs. No new results, no new citations.
- **Back matter** (Data Availability, Code Availability, Author Contributions / CRediT, Conflict of Interest, Funding, Acknowledgements) — read `references/reproducibility.md`. JHRS requires Data Availability and CRediT; HJ requires Data Availability and recommends the rest. These are not optional; missing back matter triggers desk rejection at both journals.
- **References** — alphabetical, deduplicated, formatted per journal. Target ≥15 resolved entries for a full paper.

---

## PRE-EXPORT QUALITY CONTROL

Before generating the .docx, verify every item below. Fix or flag any failure.

**Anti-fabrication** (per `references/anti-fabrication.md`)
- [ ] Every numerical claim traces to a cached file, figure, or user-supplied fact (no invented values, sample sizes, units, or precision)
- [ ] Every citation was resolved via Semantic Scholar (no fabricated references, DOIs, or author names)
- [ ] Every causal or mechanistic claim has either a citation or an explicit hedge ("may", "one possible interpretation", "we hypothesize")
- [ ] No "well-known", "established", or "previous studies have shown" without a real citation
- [ ] No invented study-area facts (basin area, climate, geology) — all sourced or supplied
- [ ] No invented software versions, parameter rationales, random seeds, or calibration/validation splits beyond what the source code shows
- [ ] No invented author metadata (affiliations, ORCIDs, emails, CRediT roles, funding details)
- [ ] All bracketed placeholders ([CITATION NEEDED], [VALUE NEEDED], [VERIFY], [FROM USER]) are listed for the user

**Content accuracy**
- [ ] Every equation matches the cached source file (no invented terms)
- [ ] Every quantitative claim is traceable to a cached CSV row, figure, or user-supplied fact
- [ ] Study period, coordinate system, and sample sizes are consistent throughout
- [ ] Nothing in §4.5 / Limitations is invented — all items came from the user or preset

**Language**
- [ ] Zero first-person pronouns (I, we, my, our) anywhere
- [ ] All abbreviations defined on first use
- [ ] Terminology follows the journal style file (e.g. 'groundwater' one word, 'water table' two words for HJ)
- [ ] All displayed equations numbered sequentially; all symbols defined on first appearance

**Citation integrity**
- [ ] All in-text citations resolved via Semantic Scholar with real DOIs where available
- [ ] All `[CITATION NEEDED]` items listed for the user
- [ ] No fabricated citations
- [ ] Reference list ≥15 entries, alphabetically sorted, deduplicated, formatted per journal
- [ ] In-text and reference-list styles match the loaded journal file

**Figures & tables**
- [ ] Every figure passed the four-question necessity assessment — no reflex figures, no redundant-with-table figures
- [ ] Total figure count ≤6 for a full paper
- [ ] Sequential numbering with no gaps
- [ ] Captions complete and informative (figure caption below, table caption above)
- [ ] Any figure whose rationale was weak has been dropped or moved to supplementary

**Journal-specific QC**
- [ ] Re-read the "Pre-submission checklist" section of the loaded journal reference file and verify every item

**Reproducibility and back matter** (per `references/reproducibility.md`)
- [ ] Methods describe data sources with names, versions, access URLs/DOIs, and time periods
- [ ] Methods specify software versions, random seeds (if stochastic), and calibration vs. validation periods
- [ ] Data Availability Statement present and specific (no bare "available upon request")
- [ ] Code Availability Statement present (or explicit, justified absence)
- [ ] CRediT author contributions drafted (mandatory for JHRS, recommended for HJ)
- [ ] Conflict of Interest declaration present
- [ ] Funding statement with grant numbers
- [ ] All cited repositories live and reachable; all DOIs functional

**Introduction structure** (per `references/introduction-structure.md`)
- [ ] Funnel structure visible: broad significance → narrowing literature review → specific gap → study objectives → roadmap
- [ ] A reviewer can point to the single sentence that states the gap
- [ ] Study objectives are a direct response to the gap, not new scope
- [ ] First sentence is concrete, not generic
- [ ] Literature review is purposeful (grouped by approach/finding), not chronological inventory

---

## EXPORT TO .DOCX

When the user confirms export, generate the `.docx` via the public `docx` skill if it is installed, otherwise via the local `pandoc → python-docx` pipeline. **Detection:** check `/mnt/skills/public/docx/SKILL.md` (Claude Code cloud) and `~/.claude/skills/docx/SKILL.md` (local install); if either exists, read its SKILL.md before generating — it is the canonical path in that environment and uses `docx-js`. **Fallback (no docx skill present):** follow the reproducible pipeline in `references/manuscript-docx-style.md` — `pandoc` converts the manuscript to `.docx`, then a `python-docx` post-process pass enforces the formatting spec. Run `pip install python-docx` first if the import is missing. Both paths must satisfy the export requirements below.

Export requirements regardless of journal:
- A4 page, 1-inch margins, single-column layout
- 12pt body; serif for HJ (Times New Roman or equivalent), sans-serif acceptable for JHRS drafts
- Decimal numbered headings via Heading1/Heading2/Heading3 styles
- Full manuscript text + resolved reference list + any `[CITATION NEEDED]` markers preserved for user review
- Equations as plain text with right-aligned sequential numbering
- Validate with `python scripts/office/validate.py <filename>.docx` after generation

For the full Word-output formatting spec (Times New Roman coercion across all run variants, Springer/booktabs three-rule table style, autofit + 100% width tables, mean ± std merging, TIFF figure format, citeproc citations, OMML equation handling, and the reproducible `pandoc → python-docx post-process` pipeline), read `references/manuscript-docx-style.md` before generating. That file is the canonical baseline; the journal reference file overrides it where they conflict.

Journal-specific export details (line spacing, highlights block, abstract structure, KMZ reminder) are in the loaded journal reference file.

Save to the workspace root with a filename the user specifies. Confirm creation and offer post-delivery revisions.

---

## FIGURE SPECIFICATIONS

Figures are expensive — every figure costs reviewer attention, page budget, and production work. A paper with four strong figures is stronger than one with eight mediocre ones. This skill does **not** generate a default figure list. It proposes figures only after each candidate passes a necessity assessment.

### Necessity assessment (run for every candidate figure)

Before proposing a figure, answer all four questions in writing (for yourself — do not show this to the user). If any answer is weak, **do not propose the figure**.

1. **What specific claim in the manuscript does this figure support?** Name the sentence or paragraph. "Shows the results" is not an answer. "Supports the claim in §3.2 that inland stations outperform coastal ones by ~15 percentage points in median R²" is an answer.
2. **Can the same information be conveyed by a single sentence or a small table?** If yes, the figure is redundant — drop it. Distributions of 3–5 numbers belong in a table, not a histogram. A single comparison belongs in prose.
3. **Does this figure show something the reader cannot get from the cached numbers alone?** Figures earn their place by revealing *shape*, *spatial pattern*, *temporal structure*, or *relationships across many units* that prose and tables cannot show compactly. If a figure only restates numbers already in a table, cut it.
4. **Is the underlying data actually in the workspace?** If the data source is hypothetical or would require analysis you have not seen in the cached files, do not propose the figure. Flag the gap to the user instead.

### When to run the assessment

Propose figures **once, at the end of Discussion drafting** — not after Results, and never after every section. The timing matters:

- The necessity assessment depends on knowing *what each section actually argues*. A figure like "base vs. filtered RMSE scatter" is necessary only if §4.4 argues that filtered-model benefit correlates with base-model error — and you cannot know that until §4.4 is written. Assessing figures after Results forces you to guess what the Discussion will claim, which leads to over-proposing "just in case".
- Batching all figure proposals into one pass at the end prevents the drip-drip of "here's another figure idea" that accumulates unchecked. One pass forces you to compare candidates against each other and apply the 6-figure cap.
- By the end of Discussion, you also know which tables exist. A figure that would duplicate Table 2 is obvious once Table 2 is written — not before.

If the user explicitly asks for figure ideas earlier (e.g. "what figures should I be preparing while we draft?"), you can list *candidate* figures with the caveat that the necessity assessment runs after Discussion. Do not skip the assessment just because the user asked early.

### Proposal format

For figures that pass all four checks, format each as:

**Fig. [N]: [Title]**
- *Supports:* Exact section and claim this figure is attached to
- *Necessity rationale:* One sentence explaining why prose or a table cannot replace this figure (answers questions 2 and 3 above)
- *Data source:* Exact file path and column names from the workspace
- *Visual type:* scatter / histogram / time series / spatial map / boxplot / etc.
- *What the reader should take away:* One sentence stating the visual conclusion

### Hard caps

- **Maximum 6 figures for a full research paper.** If more than 6 pass the necessity assessment, keep only the 6 strongest and move the rest to supplementary material.
- **Maximum 2 figures showing the same class of result** (e.g. no more than two performance-distribution figures). Consolidate or drop.
- **No "study area overview" figure unless the manuscript genuinely depends on spatial context the reader cannot infer from a sentence.** A study-area map is a reflex, not a necessity — interrogate it like any other figure.

### When to propose zero figures

It is acceptable and sometimes correct to propose zero figures for short sections, revision rounds, or papers where all the key findings are captured in 2–3 tables. If the necessity assessment fails for every candidate, say so explicitly:

> "No figures recommended for this manuscript beyond what is already in the tables. The key findings are captured by Table [N] and Table [M], and adding figures would duplicate rather than extend the information."

Do not generate plotting code. Provide specifications only.

---

## REFERENCE FILES IN THIS SKILL

- `references/anti-fabrication.md` — when in doubt, ask or flag, never invent. The most important rule in the skill. Read before any work in any mode.
- `references/anti-summary-rules.md` — write prose not outlines. Read before every Draft-mode writing session and before any Revise-mode proposed revision.
- `references/anti-ai-style.md` — write like a human, not like an AI. Read before every Draft-mode and Revise-mode writing session, and consulted by Proofread mode for compliance checks.
- `references/introduction-structure.md` — the five-move funnel for Introduction sections (broad significance → narrowing review → gap → objectives → roadmap). Read before drafting or revising any Introduction.
- `references/reproducibility.md` — Methods replicability standard, Data Availability and Code Availability statements, CRediT taxonomy, Conflict of Interest, Funding. Read when drafting Methods or back matter, and when reviewing/revising.
- `references/manuscript-docx-style.md` — canonical Word-output formatting spec: TNR coercion, Springer-style tables, mean ± std merging, TIFF figures, OMML equations, citeproc citations, and the reproducible `pandoc → python-docx post-process` pipeline. Read during Export to .docx.
- `references/startup-interview.md` — mode selection, exact startup questions, fast-path rules.
- `references/journal-hydrogeology.md` — HJ style, structure, citation format, pre-submission checklist.
- `references/journal-jhrs.md` — JHRS style, structured abstract, highlights, Elsevier reference format, pre-submission checklist.
- `references/journal-tim.md` — IEEE Transactions on Instrumentation and Measurement style: numeric bracketed citations, Roman-numeral primary headings, IEEEtran class notes, mandatory abstract/Index-Terms/Conclusion/Acknowledgment/References/Biographies order, first-footnote pattern, mandatory AI-disclosure block, pre-submission checklist. Read when targeting IEEE TIM (or as a starting point for other IEEE Transactions).
- `references/preset-example.md` — Draft-mode fast-path preset **template**. Defines the structure of a project preset: detection trigger, data files to cache, fixed project facts (study area, period, CRS, model variants, parameter counts, classification rules, thresholds, optimiser), abbreviations, mandatory limitations, Semantic Scholar queries per section, forbidden content, candidate figure pool, mandatory tables. Copy to `references/preset-<your-project>.md` (or symlink from `.local/`) and fill in the placeholders to enable workspace-based fast-path detection.
- `references/mode-review.md` — Review mode: reviewer feedback rubric and report format.
- `references/mode-revise.md` — Revise mode: section-by-section suggestion format, reviewer-comment mapping, response letter drafting.
- `references/mode-proofread.md` — Proofread mode: allowed/forbidden edit scope, language and style compliance pass.
- `references/mode-audit.md` — Audit mode: end-to-end consistency and coherence checks across the manuscript, severity-tagged report.

Read reference files lazily, only loading what the current mode and session need.

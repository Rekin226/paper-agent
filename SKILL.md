---
name: paper-agent
description: Full academic manuscript skill for quantitative-science papers, with journal profiles for Hydrogeology Journal, Journal of Hydrology Regional Studies, Journal of Hydrology, Water Resources Research, HESS, Groundwater, Engineering Geology, IEEE TIM, and JMBE, plus a field-agnostic generic profile for any other journal. Five modes, namely Draft, Review, Revise, Proofread, and Audit. Use whenever the user wants to draft, write, review, revise, polish, proofread, audit, or respond to reviewer comments on a journal manuscript. Reads workspace data and existing .docx manuscripts, resolves citations via Semantic Scholar with OpenAlex DOI verification where available, and outputs publication-ready prose or structured feedback. Trigger on "write the paper", "draft the manuscript", "review my manuscript", "respond to reviewers", "audit my paper", "/paper-agent", or any manuscript writing, revision, review, or audit request. Also triggers when the user uploads a .docx asking for feedback or edits.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Skill, mcp__semantic-scholar__search_papers, mcp__semantic-scholar__get_paper, mcp__semantic-scholar__search_papers_match, mcp__openalex__search_works, mcp__openalex__batch_resolve_references, mcp__openalex__check_venue_quality, mcp__openalex__get_work
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

## ENVIRONMENT DETECTION — run once, before anything else

This skill runs in two environments with different toolchains. Detect which one you are in at the start of the session and record the answer; every `.docx` and citation step below branches on it.

```bash
# 0. Resolve this skill's own directory. It varies by install method (plugin,
#    ~/.claude/skills/paper-agent, or a symlinked clone), so never hard-code it.
SKILL_DIR=$(dirname "$(find ~/.claude -name SKILL.md -path '*paper-agent*' 2>/dev/null | head -1)")
echo "SKILL_DIR=$SKILL_DIR"
# A. Is a docx skill present? (Claude Desktop / claude.ai)
ls /mnt/skills/public/docx/SKILL.md 2>/dev/null && echo "DOCX_SKILL=yes" || echo "DOCX_SKILL=no"
# B. Is the bundled venv present? (Claude Code, local filesystem)
ls "$SKILL_DIR/.venv/bin/python" 2>/dev/null && echo "LOCAL_VENV=yes" || echo "LOCAL_VENV=no"
```

`$SKILL_DIR` is used throughout this file for the bundled `scripts/` and `.venv`. If the
`find` above returns nothing, ask the user where the skill is installed rather than
guessing a path.

Also check your own tool list for `mcp__openalex__*`. That is not detectable from the shell.

| Environment | Signal | `.docx` handling | Citation handling |
|---|---|---|---|
| **Claude Code** (CLI, Claude Code desktop app, IDE) | `LOCAL_VENV=yes` | bundled `scripts/` + venv | Semantic Scholar + OpenAlex |
| **Claude Desktop / claude.ai** | `DOCX_SKILL=yes` | delegate to the `docx` skill | Semantic Scholar only, unless OpenAlex tools are present |

Neither path is a fallback for the other; they are different environments with different tools available. If **both** signals are present, prefer the bundled scripts: they compute the citation-integrity and cross-reference checks this skill needs in one pass, which the generic docx skill does not.

If **neither** is present, say so and stop. Do not improvise a .docx parser.

**State the detected environment to the user in the startup report**, so it is obvious which capabilities are active. When OpenAlex is unavailable, say so explicitly at that point: DOI verification will be degraded for the whole session, and the user should know before drafting, not at export.

---

## SUPPORTED JOURNALS

Block 1 of the startup interview selects one. Load that file and keep it loaded for the whole session: it governs section structure, citation format, abstract rules, and the pre-submission checklist, and it overrides `references/manuscript-docx-style.md` wherever the two conflict.

| Journal | Publisher | Citation style | Profile |
|---|---|---|---|
| Hydrogeology Journal (HJ) | Springer / IAH | author-year | `references/journal-hydrogeology.md` |
| Journal of Hydrology: Regional Studies (JHRS) | Elsevier | author-year | `references/journal-jhrs.md` |
| Journal of Hydrology (J. Hydrol.) | Elsevier | author-year | `references/journal-jhydrol.md` |
| Water Resources Research (WRR) | AGU / Wiley | author-year | `references/journal-wrr.md` |
| Hydrology and Earth System Sciences (HESS) | EGU / Copernicus | author-year | `references/journal-hess.md` |
| Groundwater | NGWA / Wiley | author-year | `references/journal-groundwater.md` |
| Engineering Geology (EG) | Elsevier | author-year | `references/journal-engineering-geology.md` |
| IEEE Trans. Instrumentation and Measurement (TIM) | IEEE | **numeric bracketed** | `references/journal-tim.md` |
| J. Medical and Biological Engineering (JMBE) | Springer | author-year | `references/journal-jmbe.md` |
| *Any other quantitative-science journal* | — | per author guidelines | `references/journal-generic.md` |

For any journal not listed, load `references/journal-generic.md` and ask the user to paste the author guidelines; those guidelines override the generic baseline. Flag every point where you are extrapolating rather than following a stated rule. Never invent a journal rule.

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

**Block 1 — Journal target** (all modes). Load the matching profile from the journal table below. The journal style matters for Review (is the manuscript HJ-compliant?), Revise (do the edits match journal style?), and Proofread (what terminology rules to enforce?), not just Draft.

**Remaining blocks branch by mode.** Read `references/startup-interview.md` for the full protocol.

**Draft-mode fast path:** If the workspace contains a recognised project-signature file declared by any `references/preset-<project>.md` (see `references/preset-example.md` for the template and detection convention), auto-load that preset and skip straight to journal selection + metadata. Still confirm with the user before writing.

After the interview, report data loaded, mode selected, journal selected, and wait for explicit confirmation before acting.

---

## READING EXISTING MANUSCRIPTS (Review, Revise, Proofread modes)

When the mode is Review, Revise, or Proofread, the user provides a path to an existing `.docx` manuscript. Before any analysis:

1. **Extract the manuscript**, per the environment detected above.

   **Claude Code (`LOCAL_VENV=yes`)** — run the bundled extractor. Absolute paths, so it works from any working directory:
   ```bash
   "$SKILL_DIR/.venv/bin/python" \
     "$SKILL_DIR/scripts/extract_docx.py" <manuscript.docx> --sections
   ```
   If the venv is missing, bootstrap it once:
   ```bash
   cd "$SKILL_DIR" && python3 -m venv .venv && .venv/bin/pip install python-docx lxml
   ```

   **Claude Desktop / claude.ai (`DOCX_SKILL=yes`)** — the bundled `scripts/extract_docx.py` still runs if `python-docx` is importable, which it normally is in that container:
   ```bash
   python3 scripts/extract_docx.py <manuscript.docx> --sections
   ```
   If that fails, delegate to the `docx` skill at `/mnt/skills/public/docx/SKILL.md`, read its reading section, and compute the integrity checks in step 2 by hand. That is slower and easier to get wrong, so try the script first.

   Either way: do not write ad-hoc .docx parsers. `pandoc in.docx -t markdown` is the last-resort fallback.

2. **What the extractor returns.** `--sections` adds the full text of every section; `--json` gives the machine-readable structure. In one pass it computes:
   - Full text and word count by section
   - All in-text citations, both `(Author, Year)` and `Author (Year)` forms
   - Reference list entries, split even when an export collapses them into one paragraph
   - Figure and table captions with their numbers, and the embedded table objects
   - Equation count and numbering
   - **Cross-reference integrity:** figures and tables that are captioned but never cited, and cited but never captioned
   - **Citation integrity:** orphan citations with no matching reference entry, and reference entries never cited

   Steps 3 and 4 are therefore already done by the tool. Read its `Integrity:` line rather than re-deriving it by hand.

3. **Sanity-check the extraction before trusting it.** If the report shows `Reference entries: 0` or a section list that is obviously wrong, the manuscript's heading styles did not survive whatever produced the .docx. Say so, and fall back to `pandoc <file>.docx -t markdown` before drawing any conclusion. A citation-integrity result computed against an empty reference list is not a clean bill of health, and the extractor prints an explicit warning in that case.

4. **Report the extraction summary to the user before proceeding:**
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

**Two backends, different jobs.** Semantic Scholar finds the right paper; OpenAlex supplies the metadata needed to cite it. Use both, in that order.

> **Known limitation of the Semantic Scholar MCP server.** Its `search_papers` and `get_paper` return only `title`, `authors`, `year`, and `venue`. They silently drop `externalIds`, `citationCount`, and `openAccessPdf` even when those fields are explicitly requested, and `venue` is often an empty string. Verified 2026-08-25 on both endpoints, including a lookup by DOI. **Do not rely on Semantic Scholar for a DOI, a citation count, or venue quality.** If a future server version returns those fields, this note can be dropped, but check before trusting them.

1. **Identify citation needs.** List the claims in the upcoming section that require literature support.

2. **Discovery: search Semantic Scholar.** One focused query per topic. Call `mcp__semantic-scholar__search_papers` with `limit` 5. Never batch unrelated topics into one query. Semantic Scholar has the better topical relevance on narrow domain queries, which is why it leads. Expect only title, authors, year, and possibly venue back.

3. **Shortlist by relevance.** From the Semantic Scholar results, pick the 1–3 candidates that actually support the specific claim. Judge on topical fit alone at this stage; you do not yet have the metadata to judge anything else. If nothing is topically relevant, insert `[CITATION NEEDED: <topic>]` inline and skip to the next claim. Never insert a loosely-related paper to fill a slot.

4. **Resolution: look the candidates up in OpenAlex.** Call `mcp__openalex__search_works` with the candidate title (set `exact_phrase: true` for a distinctive title). This returns what Semantic Scholar cannot: `doi`, `cited_by_count`, `fwci`, `source` with `source_issn_l`, and open-access status.

   If OpenAlex cannot find the paper, the citation is **unresolved**. Insert `[CITATION NEEDED: <topic> — found in Semantic Scholar as "<title>" but not resolvable in OpenAlex, DOI unverified]` and tell the user. Do not write a reference entry from the Semantic Scholar result alone, and never reconstruct a DOI from a pattern.

   **If `mcp__openalex__*` tools are not available at all** (Claude Desktop / claude.ai, unless you have added an OpenAlex connector), this step cannot run. Then:
   - Cite from the Semantic Scholar result: authors, title, year, and venue where present.
   - **Omit the DOI.** Do not substitute one from memory. An omitted DOI is a formatting gap the user can fill in minutes; a wrong one is a fabricated citation.
   - Mark every such entry `[DOI UNVERIFIED]` in the running reference list, and list them all in the post-section summary.
   - Say once, at the start of the session, that DOI verification is unavailable in this environment and the reference list will need a manual DOI pass before submission.

   This is a real capability difference, not a stylistic one. Do not paper over it.

5. **Select the best match.** Now rank the shortlist by: (a) topical relevance to the specific claim, (b) year, preferring 2010–present unless a seminal older work is clearly needed, (c) venue quality, (d) community acceptance.

   For (c), use `source` and `source_issn_l` from the OpenAlex result. When the venue is unfamiliar or its standing matters to the argument, call `mcp__openalex__check_venue_quality` with the venue name or ISSN: it returns h-index, `two_year_mean_citedness`, and DOAJ indexing status. A venue with no meaningful h-index and no indexing is a reason not to cite.

   For (d), prefer **`fwci`** (field-weighted citation impact) over raw `cited_by_count`. FWCI normalizes for field and publication age, so it does not penalize a strong 2023 paper against a mediocre 2005 one. Raw counts are still useful as a sanity check.

6. **Format in the journal's style.** Use the in-text and reference formats defined in the loaded journal reference file (see the journal table above). Note that TIM uses numeric bracketed citations, not author-year, so the whole insertion pattern changes when that profile is loaded. Include the DOI from the OpenAlex `doi` field. Strip the `https://doi.org/` prefix if the journal profile wants a bare DOI.

7. **Insert inline + append to running reference list.** Place the formatted in-text citation at the exact sentence location. Append the full reference entry to a `## REFERENCE LIST` block that grows across the session, alphabetically sorted and deduplicated by DOI or title.

8. **Post-section citation summary.** After each section output, report:
   ```
   Citations resolved this section: N (N with verified DOI)
   Unresolved [CITATION NEEDED] items: <list or "none">
   Running reference list total: N entries
   ```

**Never fabricate citations, DOIs, or author names.** Every DOI in the reference list must have come back from an OpenAlex lookup in this session. A DOI you have not seen returned by a tool call does not go in the manuscript, no matter how confident the pattern looks. If neither backend produces the paper, the placeholder stays.

**Rate limits.** Semantic Scholar is 1 request/second (authenticated free tier); OpenAlex is 10/second. Neither is a practical constraint at one query per claim, but do not fan out parallel Semantic Scholar calls.

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

Generic guidance that applies across the supported journals (the loaded profile overrides anything below where they conflict):

- **Abstract** — no citations. State the real cached numbers (sample sizes, key metrics). Follow the journal's required structure (HJ = single paragraph; JHRS = three labelled parts: Study Region, Study Focus, New Hydrological Insights for the Region). Write the Abstract LAST, after Discussion is drafted, not first.
- **Introduction** — read `references/introduction-structure.md` before drafting. The Introduction must follow the five-move funnel (broad significance → narrowing literature review → specific gap → study objectives → roadmap). Every cited paper must support a specific claim, not pad the section.
- **Materials and Methods** — past tense. Read `references/reproducibility.md` for the replicability standard. Every equation, parameter, and setting must come from the cached source files. Methods must include enough detail for independent replication: data sources with access details, software versions, parameter ranges, calibration period, optimizer settings, convergence criteria.
- **Results** — present tense. Every quantitative claim must cite a table, figure, or cached value. Refuse to write "the model performs well", always give numbers. Report metrics with sample sizes and uncertainty (SD or CI) where available.
- **Discussion** — present tense. Benchmark against resolved references (Semantic Scholar for discovery, OpenAlex for the DOI and metadata). Interpret fitted parameters physically. Do not restate results.
- **Limitations** (usually §4.5 in HJ, end of Discussion in JHRS) — mandatory. Write each as: *limitation → assessed impact → proposed remedy*. Use only the limitations the user supplied in the startup interview (or from the loaded preset). Do not invent.
- **Conclusions** — 3–5 paragraphs. No new results, no new citations.
- **Back matter** (Data Availability, Code Availability, Author Contributions / CRediT, Conflict of Interest, Funding, Acknowledgements) — read `references/reproducibility.md`. The loaded journal profile is the authority on which are mandatory: JHRS and Journal of Hydrology require Data Availability and CRediT; HESS requires Data Availability and, where code was used, Code Availability as named sections; HJ requires Data Availability and recommends the rest. These are not optional; missing back matter triggers desk rejection at every supported journal.
- **References** — alphabetical, deduplicated, formatted per journal. Target ≥15 resolved entries for a full paper.

---

## PRE-EXPORT QUALITY CONTROL

Before generating the .docx, verify every item below. Fix or flag any failure.

**Anti-fabrication** (per `references/anti-fabrication.md`)
- [ ] Every numerical claim traces to a cached file, figure, or user-supplied fact (no invented values, sample sizes, units, or precision)
- [ ] Every citation was found in a search AND resolved in OpenAlex (no fabricated references, DOIs, or author names)
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
- [ ] Zero forward section references outside the Introduction — no sentence in Methods, Results or Discussion sends the reader to a section they have not reached (per `references/anti-ai-style.md`)

**Citation integrity**
- [ ] All in-text citations resolved, each DOI taken from an OpenAlex result in this session
- [ ] No DOI was constructed, inferred, or pattern-matched rather than returned by a tool
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
- [ ] CRediT author contributions drafted (mandatory for JHRS and Journal of Hydrology, recommended for HJ — check the loaded journal profile)
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

When the user confirms export, branch on the detected environment.

**Claude Code** — follow the `pandoc → python-docx post-process` pipeline in `references/manuscript-docx-style.md`. Write the manuscript as Markdown or LaTeX, convert with `pandoc`, then run the post-process pass that enforces the formatting spec.

**Claude Desktop / claude.ai** — delegate to the `docx` skill at `/mnt/skills/public/docx/SKILL.md`. Read its SKILL.md before generating. It is the canonical .docx creation path in that environment and handles the OOXML details directly. The formatting spec in `references/manuscript-docx-style.md` still governs *what* the output must look like; only the mechanism differs.

Export requirements regardless of journal:
- A4 page, 1-inch margins, single-column layout
- 12pt body; serif for HJ (Times New Roman or equivalent), sans-serif acceptable for JHRS drafts
- Decimal numbered headings via Heading1/Heading2/Heading3 styles
- Full manuscript text + resolved reference list + any `[CITATION NEEDED]` markers preserved for user review
- Equations as plain text with right-aligned sequential numbering
- Validate after generation. **Claude Code:**
  ```bash
  "$SKILL_DIR/.venv/bin/python" \
    "$SKILL_DIR/scripts/validate_docx.py" <filename>.docx --font "Times New Roman"
  ```
  **Claude Desktop / claude.ai:** run the same bundled checker with `python3 scripts/validate_docx.py <filename>.docx`, and additionally `python scripts/office/validate.py <filename>.docx` from the `docx` skill, which checks OOXML validity that the bundled checker does not.
  It checks package integrity, font coercion across every run variant, heading styles, sequential figure/table/equation numbering, unresolved `[CITATION NEEDED]`-style placeholders, first-person pronouns, percentage-width tables, and embedded figure media. Exit code 1 means at least one check failed. Fix or report every FAIL before delivering.

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

### Handoff to `paper-figures`

Do not generate plotting code in this skill. Produce the specification, then hand off.

Once the user approves a figure specification, offer to invoke the sibling **`paper-figures`** skill, which turns a results file (CSV, Excel, NumPy, JSON, or a DataFrame in session) into a publication-ready TIFF/PNG:

> "Fig. [N] is specified. Want me to hand this to `paper-figures` to render it? It takes the data source and visual type from the spec above and exports at journal resolution."

Pass it the *Data source*, *Visual type*, and *What the reader should take away* lines verbatim: they are exactly the inputs that skill needs. `paper-figures` plots only what is in the named file, which keeps the anti-fabrication rule intact across the handoff. Figure *format* requirements (TIFF, resolution, embedded fonts) come from the loaded journal profile and `references/manuscript-docx-style.md`, so state them in the handoff.

Do not invoke `paper-figures` without the user confirming the specification first.

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
- `references/journal-engineering-geology.md` — Engineering Geology (Elsevier) style: scope gate, structure, author-year citations, Elsevier back matter and declarations, pre-submission checklist.
- `references/journal-jmbe.md` — Journal of Medical and Biological Engineering (Springer) style: scope, structure, Springer author-year citations, pre-submission checklist.
- `references/journal-tim.md` — IEEE Transactions on Instrumentation and Measurement style: numeric bracketed citations, Roman-numeral primary headings, IEEEtran class notes, mandatory abstract/Index-Terms/Conclusion/Acknowledgment/References/Biographies order, first-footnote pattern, mandatory AI-disclosure block, pre-submission checklist. Read when targeting IEEE TIM (or as a starting point for other IEEE Transactions).
- `references/journal-wrr.md` — Water Resources Research (AGU/Wiley) style: mandatory 3-bullet Key Points (≤140 chars), Plain Language Summary, unnumbered headings, AGU author-date citations with full italic journal names.
- `references/journal-jhydrol.md` — Journal of Hydrology (Elsevier) style: mandatory Highlights (3–5 bullets, ≤85 chars), trailing-full-stop numbered headings, Elsevier Harvard citations, CRediT. **Distinct from JHRS** — check which title the user means.
- `references/journal-hess.md` — Hydrology and Earth System Sciences (EGU/Copernicus) style: 300-word abstract, Copernicus colon-after-authors year-last reference format, "Figure N" not "Fig. N", mandatory Data and Code availability sections.
- `references/journal-groundwater.md` — Groundwater (NGWA/Wiley) style: ~6,000-word concise format, unnumbered headings, HJ-style no-comma Harvard citations, practitioner-facing register.
- `references/journal-generic.md` — field-agnostic baseline for any other quantitative-science journal: IMRaD structure, standard scientific tense, SI units, sequential numbering, mandatory Limitations subsection. Defers to the target journal's author guidelines on points that genuinely vary (citation style, word limits, abstract format, first-person policy). Read when the user selects `generic`.
- `references/preset-example.md` — Draft-mode fast-path preset **template**. Defines the structure of a project preset: detection trigger, data files to cache, fixed project facts (study area, period, CRS, model variants, parameter counts, classification rules, thresholds, optimiser), abbreviations, mandatory limitations, Semantic Scholar queries per section, forbidden content, candidate figure pool, mandatory tables. Copy to `references/preset-<your-project>.md` (or symlink from `.local/`) and fill in the placeholders to enable workspace-based fast-path detection.
- `references/preset-demo.md` — Synthetic demo preset used by the bundled try-it examples in `examples/`. Auto-detected from the demo workspace. Safe to delete in a real project.
- `references/mode-review.md` — Review mode: reviewer feedback rubric and report format.
- `references/mode-revise.md` — Revise mode: section-by-section suggestion format, reviewer-comment mapping, response letter drafting.
- `references/mode-proofread.md` — Proofread mode: allowed/forbidden edit scope, language and style compliance pass.
- `references/mode-audit.md` — Audit mode: end-to-end consistency and coherence checks across the manuscript, severity-tagged report.

Read reference files lazily, only loading what the current mode and session need.

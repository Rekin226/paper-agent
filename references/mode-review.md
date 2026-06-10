# Mode — Review

Produce a reviewer-style report on an existing manuscript. **No edits to the file.** Output is a structured feedback report in chat.

**Apply `references/anti-fabrication.md` rigorously in this mode.** A reviewer who invents criticisms is worse than a reviewer who misses real ones. If the manuscript makes a claim you cannot verify against the extracted text, do not assert it makes the claim — quote the exact passage you are reviewing. If you suspect a citation is fabricated, sample-check via Semantic Scholar before flagging. If you cannot tell whether a methodological detail is in the manuscript, re-extract that section rather than guessing.

## Philosophy

Act as a rigorous but constructive peer reviewer for the chosen journal. The goal is to give the author feedback they can actually use: specific, evidence-based, and tied to the manuscript's own claims — not generic writing advice.

A good review:
- Identifies the paper's core contribution in one sentence before critiquing anything
- Separates structural/scientific issues from language/presentation issues
- Cites specific page/section/line locations for every comment
- Distinguishes *Major* (must address for publication) from *Minor* (should address) from *Optional* (author discretion)
- Never recommends changes for the sake of changing — every suggestion earns its place

A bad review:
- Gives vague feedback like "the methods could be clearer"
- Lists generic writing tips not grounded in the actual manuscript
- Focuses only on language while missing scientific problems (or vice versa)
- Recommends restructuring without explaining the benefit

## Before writing the report

1. **Read the full manuscript.** The extraction from SKILL.md → "Reading existing manuscripts" must be complete before review begins. If the extraction reported integrity issues (orphan citations, figure/table gaps), note them — they go in the report.
2. **Identify the core contribution.** In one sentence, state what this paper claims to contribute. If you cannot state it clearly, that itself is the first Major comment.
3. **Load the journal reference file** and check compliance. Every compliance failure is a comment.
4. **Verify existing citations** via Semantic Scholar. Pick 5–10 of the in-text citations and search for them. If any cannot be resolved (wrong year, nonexistent paper, misattributed), flag as Major. Do not attempt to verify every citation — this is a sampling check.
5. **Run the figure necessity assessment** (SKILL.md → Figure Specifications) against every figure in the manuscript. Figures that fail the assessment become review comments recommending removal or consolidation.

## Review report format

Output the report in chat using this exact structure:

```
# Review Report — <manuscript title>

**Journal target:** [HJ / JHRS]
**Reviewer:** Paper Agent (automated peer-review pass)
**Date:** [today]

## 1. Summary of contribution

<One paragraph, 3–5 sentences. State what the paper does, what data and methods
it uses, and what it claims. No critique yet — just an accurate summary.>

## 2. Overall recommendation

<One of: Accept / Minor revision / Major revision / Reject and resubmit / Reject.
Justify in 2–3 sentences based on the comments below.>

## 3. Major comments

<Numbered list. Each comment has:
 - **Location:** Section/subsection/page/line
 - **Issue:** What is wrong, with evidence from the manuscript
 - **Impact:** Why this matters for the contribution
 - **Suggested action:** What the author should do — specific, actionable

Major comments are issues the author MUST address before the paper can be
accepted. Scientific errors, missing controls, unsupported claims, missing
limitations, broken citation integrity, inappropriate figures, journal-style
non-compliance that would trigger desk rejection.>

## 4. Minor comments

<Same format as Major. Minor comments are issues the author SHOULD address
but that do not block publication. Unclear sentences, missing context, minor
citation gaps, optional figure improvements, non-critical style nits.>

## 5. Language and presentation

<Group language issues here, not scattered through Major/Minor. Include:
 - First-person pronoun violations (with line numbers)
 - Abbreviation definitions missing on first use
 - Tense inconsistencies
 - Terminology issues (e.g. 'groundwater' vs 'ground water' for HJ)
 - Equation formatting and symbol definition gaps
 - Figure/table caption quality
 - **AI-style markers** per `references/anti-ai-style.md`: count em-dashes in body prose, list hedge openers ("Importantly,", "Of note,", "It is worth noting that"), filler intensifiers ("very", "particularly"), and instances of "utilize"/"leverage". If the manuscript shows multiple of these patterns, flag it as a Major comment recommending a Proofread pass before submission, since reviewers increasingly recognize and penalize AI-style prose.
 - **Provenance-leak tells** per `references/anti-ai-style.md`: code-file paths or script names in the narrative (e.g. "implemented in `experiments/...py`") and unresolved cross-reference labels (`[eq:...]`, `\ref{...}`, `{#eq-...}`). Either one is a Major comment — a reviewer reads them as evidence the text was machine-assembled and not proofread. Note that code locations belong only in the Code Availability statement and labels must render as "Eq. (N)" / "Fig. N" / "Table N".

If the manuscript needs professional language editing, say so explicitly.>

## 6. Journal compliance check

<Bullet list mapping to the pre-submission checklist in the loaded journal
reference file. For each checklist item: ✓ pass, ✗ fail (with location), or
N/A. This is where the HJ "zero first-person pronouns" and JHRS "structured
abstract / Highlights / KMZ requirement" checks live.>

## 7. Citation integrity

<Report from the 5–10 citation sample check:
 - N citations verified via Semantic Scholar
 - N resolved correctly
 - N with issues (listed with specifics)
 - Orphan citations from extraction (in text but not in reference list)
 - Unused reference entries (in list but not cited)>

## 8. Figure assessment

<For each figure in the manuscript, state whether it passes the four-question
necessity assessment from SKILL.md. Figures that fail become Major or Minor
comments recommending removal or consolidation, but the per-figure detail
lives here.>

## 9. Introduction structure

<Apply the five-move funnel test from `references/introduction-structure.md`:
 - Move 1 (broad significance): present? concrete or generic?
 - Move 2 (narrowing literature review): purposeful or chronological inventory?
 - Move 3 (gap statement): can you point to the single sentence?
 - Move 4 (objectives): direct response to the gap, or new scope?
 - Move 5 (roadmap): present, absent, or excessive?

Failures here are usually Major comments. An Introduction without a clear
gap statement is the single most common reason hydrology manuscripts get
returned for major revision.>

## 10. Reproducibility and back matter

<Per `references/reproducibility.md`:
 - Methods replicability: does Methods describe data sources with names/versions/access details, software versions, calibration vs. validation periods?
 - Data Availability Statement: present and specific, or missing/bare?
 - Code Availability Statement: present, justified absence, or missing?
 - CRediT (mandatory for JHRS): drafted with all authors having at least one role?
 - Conflict of Interest declaration: present?
 - Funding statement with grant numbers: present?
 - All cited repositories and DOIs: live and reachable?

Missing back matter is a desk-rejection trigger at both HJ and JHRS. Flag
each absence as a Major comment.>
```

## Tone

Professional, direct, specific. No hedging language like "perhaps consider" or "it might be nice if". Reviewers speak plainly: "Section 3.2 overstates the performance of the `<subgroup>` model. The median `<metric>` of `<value>` is below the threshold the authors themselves define as adequate, yet the text claims 'the model performs well across the `<subgroup>` subset'. Revise to reflect the actual result."

Constructive, not cruel. Every Major comment must propose a concrete fix, not just identify the problem.

## What Review mode does NOT do

- Does not edit the .docx file
- Does not rewrite paragraphs (suggest the fix in the comment, do not write it)
- Does not draft new sections
- Does not produce a response letter (that's Revise mode)
- Does not proofread line-by-line (that's Proofread mode — mention language issues in aggregate under Section 5, don't list every typo)

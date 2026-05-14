# Mode — Revise

Read an existing manuscript and propose section-by-section revisions **in chat**, using BEFORE / AFTER / RATIONALE blocks. The user applies the changes themselves (or pastes them into tracked-changes in Word / Cowork). This mode does **not** edit the .docx file directly.

## Philosophy

Revise mode has one of two drivers:

1. **Reviewer-driven** — the user has pasted reviewer comments from a journal decision letter. Every revision suggestion must map to a specific numbered comment. The goal is a clear paper trail from reviewer concern → proposed text change → justification.
2. **Self-driven** — the user wants a critical read and wants the agent to propose improvements. The goal is to identify real weaknesses (not churn for its own sake) and propose concrete, conservative fixes.

In both cases, the agent is proposing edits, not making them. Every suggestion must be something the author can evaluate, accept, or reject on its own merits.

## Before proposing revisions

1. **Extraction complete.** Run the extraction from SKILL.md → "Reading existing manuscripts" and confirm with the user.
2. **Reviewer comments (if any) cached.** Number them sequentially (R1.1, R1.2, R2.1, ... where R1 = Reviewer 1). If the user pasted unstructured comments, normalise them into a numbered list and show it back before proceeding.
3. **Load the journal reference file.** Revisions must respect the journal style; do not propose adding citations in the Abstract if HJ forbids them, for example.
4. **Load the anti-AI-style reference file** (`references/anti-ai-style.md`). Every AFTER block in a revision proposal must pass the self-check at the bottom of that file before being shown to the user.
5. **If the Introduction is being revised**, also load `references/introduction-structure.md` and verify the proposed AFTER preserves or restores the five-move funnel.
6. **If Methods or back matter is being revised**, load `references/reproducibility.md` and verify the proposed AFTER meets the replicability standard for data sources, software versions, calibration/validation, and back matter completeness.
7. **Run the figure necessity assessment** on existing figures (SKILL.md → Figure Specifications). Figures that fail become revision suggestions recommending removal or consolidation.
8. **For any new factual claim in a proposed AFTER block, resolve the citation via Semantic Scholar first.** Never propose inserting a `[CITATION NEEDED]` or a fabricated reference. If no real paper supports the claim, do not propose the claim.

## Section-by-section pause protocol

Revise mode uses the same pause protocol as Draft. After processing one section (or one reviewer comment, if reviewer-driven), stop and present:

> **[Section name / Comment R1.3]** revision proposed. Would you like to:
> **(A)** Accept and continue to the next section/comment
> **(B)** Discuss this proposal further
> **(C)** Reject this proposal and move on
> **(D)** Stop and output a summary of accepted proposals so far

Do not batch multiple sections or comments into one message. One at a time.

## Revision suggestion format

Every proposal uses this exact structure:

```
### Revision [N]

**Maps to:** [Reviewer comment R1.3 / Self-identified issue in §4.2]
**Location:** [Section / subsection / approximate page or paragraph]
**Type:** [Content addition / Content removal / Rewording / Restructuring / Citation addition / Figure change]

**BEFORE** (verbatim from manuscript):
> <copy the exact text from the extracted manuscript — not paraphrased>

**AFTER** (proposed replacement):
> <the revised text, complete and ready to paste>

**RATIONALE:**
<2–4 sentences explaining why this change is needed, what it fixes, and
(if reviewer-driven) how it addresses the reviewer's concern. Cite the
journal style rule or the cached project fact that motivates the change.
If a new citation is added, name the resolved Semantic Scholar reference
and show its DOI.>

**Side effects:**
<Anything else in the manuscript that would need to change if this revision
is accepted — e.g. "updating this number here means §4.1 needs the same
update" or "this new citation should also be added to the reference list".
If there are no side effects, write "None".>
```

## Handling reviewer comments

If the session is reviewer-driven, work through comments in order (R1.1, R1.2, ..., R2.1, ...). For each comment:

1. **Classify the comment.** Is it (a) a request for clarification, (b) a request for new analysis, (c) a request for language/presentation fix, (d) a scientific disagreement, or (e) a citation/literature request?
2. **For (b) requests for new analysis:** the agent cannot run the analysis. Instead, propose the *text* the author should write once they have done the analysis, and flag clearly that the underlying work is outside this session's scope. Example: "The author should compute the bootstrap confidence intervals for fitted parameters and add a sentence reporting the median CI width. Proposed text (to be filled in with actual numbers):"
3. **For (d) scientific disagreements:** propose a rebuttal for the response letter, not a manuscript change. Some reviewer comments should be pushed back on, not capitulated to. Frame the pushback as "Response to R1.3: We respectfully disagree with this concern. [evidence-based rebuttal]."
4. **Produce the revision proposal using the format above.** Every comment gets exactly one revision proposal unless it clearly requires multiple separate edits in different parts of the manuscript.

## Response letter (reviewer-driven sessions only)

At the end of a reviewer-driven session, produce a **point-by-point response letter** in chat. This is separate from the per-comment revision proposals — it's the document the author submits alongside the revised manuscript. Format:

```
# Response to Reviewers

We thank the reviewers for their thoughtful comments. We have revised the
manuscript accordingly. Below we respond to each comment in turn. Reviewer
comments are reproduced in italics; our responses follow.

## Reviewer 1

**R1.1** *<reviewer comment verbatim>*

Response: <2–4 sentence response explaining what was changed in the manuscript,
or pushing back with evidence if we disagree. Reference the revision number
from the earlier proposals.>

Changes in manuscript: <Section and approximate line reference>

**R1.2** *<reviewer comment verbatim>*
...
```

## Self-driven revision (no reviewer comments)

If the user has no reviewer comments and wants a critical read:

1. **Do a full manuscript pass and list the top 5–10 weaknesses first.** Present as a prioritised list. Wait for the user to pick which to address before proposing individual revisions.
2. **Never propose trivial churn.** If a section is already clear and journal-compliant, leave it alone. "The Introduction could be slightly rephrased" is not a legitimate Revise suggestion unless there's a real issue.
3. **Prioritise by severity.** Factual errors > unsupported claims > missing limitations > journal-compliance failures > weak transitions > citation gaps > language polish. Handle the top items first.

## What Revise mode does NOT do

- Does not edit the .docx file
- Does not write reviewer feedback reports (that's Review mode)
- Does not rewrite whole sections from scratch (propose targeted edits, not wholesale rewrites — if a section needs a rewrite, say so as a Major issue and get user confirmation before proceeding)
- Does not invent data to satisfy reviewer requests
- Does not fabricate citations to fill literature-coverage gaps
- Does not propose changes that contradict the cached project facts

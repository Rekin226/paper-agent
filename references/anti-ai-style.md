# Anti-AI-Style Rules

AI-generated academic prose has stylistic tells that experienced reviewers recognize. Manuscripts that read as AI-written get penalized, regardless of scientific quality. The fix is not to avoid clarity. It is to drop the specific patterns that mark text as machine-produced.

Read this file before writing any prose in Draft mode, before composing any AFTER block in Revise mode, and use it as a compliance checklist in Proofread mode.

## What to avoid

### Punctuation tells

- **Em-dashes (—) for parenthetical insertion.** This is the single strongest AI tell. In academic writing, em-dashes are rare. Use commas, parentheses, or two short sentences instead. Em-dashes are acceptable only when standing in for "to" in numerical ranges (`2012–2020`, which is an en-dash anyway) and in author lists per journal style.
- **Strings of em-dashes within one paragraph.** A paragraph with two or more em-dashes reads as AI-written even if individual uses are defensible.
- **Semicolons used as soft em-dashes.** A semicolon should join two independent clauses that share a logical link. It is not a substitute for a period when the sentence is too long.

### Phrase tells

- **Hedge openers:** "It is worth noting that...", "Importantly,", "Notably,", "It should be emphasized that...", "Of particular interest is...". Drop them. State the point.
- **Throat-clearing transitions:** "In order to", "It is important to recognize that", "It is well known that". Cut to the substance.
- **Filler intensifiers:** "very", "quite", "extremely", "particularly", "indeed", "moreover", "furthermore", "additionally", "thus", "hence". Strong scientific writing rarely needs these. If a result is large, give the number; do not call it "particularly large".
- **Vague qualifiers as substitutes for evidence:** "robust", "comprehensive", "novel", "innovative", "state-of-the-art", "cutting-edge", "leverages", "utilizes". Show the property; do not claim it. "Utilizes" is almost never better than "uses".
- **Recap-and-pivot sentences:** "As discussed above...", "Building on the previous section...", "Having established X, we now turn to Y". Reviewers can read. Trust them.

### Structural tells

- **Three-item lists for everything.** "X, Y, and Z" appears in every paragraph. Real argument sometimes lists two things, sometimes four, sometimes none. Vary it.
- **Tricolons with parallel grammar.** "We measured A, analyzed B, and validated C." Sometimes use one verb. Sometimes use a single complex sentence.
- **Topic-sentence-then-three-supports paragraphs in the body.** Real research writing has paragraphs of varying shapes. Some open with a result. Some open with a question. Not every paragraph is a five-sentence essay miniature.
- **Symmetric closers:** every paragraph ending with a forward-looking sentence, every section ending with a "this section presented X; the next section presents Y". Cut them.
- **Bullet lists hidden in prose.** "First, ... Second, ... Third, ..." inside a paragraph is a list pretending to be argument. If items genuinely need enumeration, use a real list. If they do not, integrate them into argument.

### Tone tells

- **Bothsidesism caveats.** "While the model performs well in most cases, there are also instances where performance is more limited." If the result has nuance, say what the nuance actually is, with numbers. Vague even-handedness reads as AI-trained politeness, not scientific honesty.
- **Excessive contextualization.** AI tends to set up every claim with a paragraph of background that a domain reader does not need. Trust the reader.
- **Performative humility.** "We acknowledge that..." or "Future work could explore..." in places where the work was not actually limited. Limitations belong in the Limitations subsection, in plain language, not sprinkled apologetically through Results.

### Provenance-leak tells

These betray that the manuscript was assembled from a code repository or a LaTeX/internal source rather than written as prose. A reviewer who sees a script path or an unresolved label token in the body immediately recognizes machine-assembled text. Treat them as seriously as any phrase tell.

- **Code-file paths and script names in body prose.** "The sweep is implemented in `experiments/11_wavelength_sweep.py`." A filename, module path, function name, notebook, CLI flag, config key, source variable name, or repository directory must never appear in the Methods, Results, or Discussion narrative. Describe the *method*, not the file that runs it: "We swept the excitation wavelength from 400 to 700 nm in 5 nm steps." Code locations belong in exactly one place — the **Code Availability** statement (see `references/reproducibility.md`), which points at the repository as a whole, not at individual files inline. A commit hash is fine in Code Availability; it is never part of the narrative.
- **Raw internal cross-reference labels.** "...relaxes the homoscedastic white-noise assumption of `[eq:phys_kernel]`." Tokens of the form `[eq:...]`, `[fig:...]`, `[tab:...]`, `[sec:...]`, `\ref{...}`, `\eqref{...}`, `\cref{...}`, or `{#eq-...}` are internal labels that were never resolved. They must render as the journal's cross-reference form: "Eq. (3)", "Fig. 4", "Table 2", "Section 2.1". Never let a bracketed label or backslash-ref command survive into prose. If the number it should resolve to is unknown, that is a fabrication risk — stop and resolve it against the actual numbered object per `references/anti-fabrication.md`; do not guess a number and do not leave the token in place.
- **Placeholder and template residue.** `<N>`, `[TODO]`, `XXX`, `<model name>`, "as shown in the figure above/below" (figures are numbered, not positional), and "see the attached script" are repository or template artifacts. None survive into a draft presented to the user.

## What to do instead

### Sentence shape

- Vary length. A paragraph of all 25-word sentences is AI prose. Mix short sentences (5–10 words) with medium (15–20) with the occasional long one. The short ones do most of the work.
- Lead with the subject doing something. "Coastal stations underperformed" is stronger than "It was observed that performance was lower at coastal stations."
- One idea per sentence. If a sentence needs a comma after a clause to add another idea, consider whether the second idea earns its own sentence.

### Word choice

- Concrete over abstract. "The R² is 0.74" not "performance was strong". "Median RMSE was 0.18 m" not "the model achieved good accuracy".
- Plain over fancy. "use" not "utilize". "show" not "demonstrate". "find" not "elucidate". "many" not "a multitude of". The Anglo-Saxon word is almost always better than the Latinate one in scientific prose.
- Active over passive when the agent matters. Methods sections are conventionally passive ("the model was calibrated"), which is fine. Results and Discussion can be active where appropriate ("calibration produced", "the data show").

### Argument shape

- State the result, then explain it. Not the other way around. Reviewers skim for findings.
- One claim at a time. If a paragraph makes three claims, give each its own paragraph or accept that two of them are setup.
- Honest qualification. Real qualification names the specific condition: "for stations with R² above 70%". AI qualification names nothing: "in many cases" or "to some extent".

### Citation grounding

- A citation supports a specific claim. "(Chen, 2018)" at the end of a paragraph that made four claims is sloppy. Place the citation at the sentence that contains the claim it supports.
- Do not cite to demonstrate awareness of the field. Cite when the claim genuinely depends on prior work the reader needs to be able to verify.

## Self-check before finalizing prose

Before presenting any drafted or revised section, scan the output and answer:

1. **Em-dash count?** Should be zero in body prose, except for numerical ranges (which are en-dashes anyway).
2. **Hedge-word count?** Search for "Importantly", "Notably", "Of note", "It is worth noting", "Particularly". Should be zero.
3. **"Utilize" or "leverage" count?** Should be zero. Replace with "use".
4. **Three-item lists per paragraph?** If every paragraph has one, vary the structure.
5. **Sentence length variation?** Look at the last paragraph. Are all the sentences roughly the same length? If yes, rewrite with deliberate variation.
6. **Vague qualifiers?** Search for "robust", "comprehensive", "novel", "significant" used without a specific evidence anchor. Replace with the evidence.
7. **Recap sentences?** Search for "As discussed", "As noted above", "Having established". Cut.
8. **First word of each paragraph in this section?** If most paragraphs start with "The", "This", "These", or "Furthermore", you are pattern-matching. Vary.
9. **Code paths in prose?** Search the section for `.py`, `.ipynb`, `.m`, `.R`, `/`, and source function/module names. Zero in body prose. Any genuine code location moves to the Code Availability statement.
10. **Raw label tokens?** Search for `[eq:`, `[fig:`, `[tab:`, `[sec:`, `\ref`, `\eqref`, `\cref`, `{#`. Zero. Each must already be a rendered "Eq. (N)" / "Fig. N" / "Table N" / "Section N".

If any check fails, revise before presenting.

## Mode-specific notes

**Draft mode:** Apply these rules during initial drafting, not as a post-pass. It is much easier to write plainly the first time than to clean AI-style prose afterward.

**Revise mode:** Every AFTER block in a revision proposal must pass the self-check. If a proposed AFTER reads as AI prose, the revision is rejected by the agent before being shown to the user, and a new AFTER is drafted.

**Proofread mode:** Add the self-check to the standard proofread pass. Specifically:
- Search for em-dashes in body prose. Each one is an edit candidate (replace with comma, parentheses, or sentence break).
- Search for hedge openers and filler intensifiers. Each is an edit candidate.
- Search for "utilize" and "leverage". Each is an edit candidate (replace with "use").
- Search for code-file paths (`.py`, `.ipynb`, module/function names, repository directories) in body prose. Each is an edit candidate: rewrite the sentence to describe the method, and move any genuine code location to the Code Availability statement. This is the one structural-looking change Proofread may make, because the path carries no scientific content.
- Search for raw cross-reference labels (`[eq:...]`, `[fig:...]`, `\ref{}`, `\eqref{}`, `{#eq-...}`). Each is an edit candidate: replace with the rendered reference ("Eq. (N)", "Fig. N", "Table N"). If the target number cannot be confirmed from the manuscript, flag it for the user rather than guessing.
- Flag any paragraph that consists entirely of three-item lists for the user to decide.

Proofread is the only mode where you can fix these without changing meaning. Do not strip flavor or break the author's voice. If a sentence reads as deliberately written by the author and falls within their style, leave it. The targets are the patterns that mark text as machine-produced, not all formal academic phrasing.

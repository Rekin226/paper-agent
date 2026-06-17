# Examples — try paper-agent in 60 seconds

Two self-contained demos you can run immediately after installing the skill, with **no data of your own**. Everything here is **synthetic** — the numbers, wells, and study area are illustrative and do not describe a real site or real measurements. They exist only to exercise the skill.

| Demo | Mode | What it shows | Setup |
|---|---|---|---|
| [`demo-draft/`](demo-draft/) | **Draft** | Turns synthetic project data (CSVs + notes) into journal-style manuscript prose with resolved citations | None — all plain-text input |
| [`demo-audit/`](demo-audit/) | **Audit** | Catches planted inconsistencies (temporal, sample-size, cross-reference, terminology) in a manuscript | One `pandoc` command to build the `.docx` |

## Prerequisites

- `paper-agent` installed (see the main [README](../README.md#-installation)).
- `pandoc` on your PATH (only for the Audit demo's `.docx` build).
- Citation resolution uses the bundled Semantic Scholar MCP; it works offline-free at ~1 req/sec without a key.

## Run the Draft demo

```
/paper-agent
```
Choose **Draft**, target journal **Hydrogeology Journal** (or JHRS), and point it at `examples/demo-draft/`. See [`demo-draft/README.md`](demo-draft/README.md) for the walkthrough and what to expect.

## Run the Audit demo

```sh
# build the sample manuscript into a .docx (pandoc only; nothing is committed)
pandoc examples/demo-audit/sample_manuscript.md -o examples/demo-audit/sample_manuscript.docx
```
Then run `/paper-agent`, choose **Audit**, and point it at the generated `.docx`. The [answer key](demo-audit/README.md#answer-key--what-audit-should-catch) lists the errors planted in the manuscript so you can verify what it caught.

> These demos are synthetic by design. When you run paper-agent on your own work, the anti-fabrication directive means it will **ask, flag, or search** rather than invent any value it cannot source.

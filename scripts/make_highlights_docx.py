#!/usr/bin/env python3
"""Build a journal-compliant Highlights .docx from a plain-text bullet list.

Most publishers require Highlights as a SEPARATE EDITABLE FILE with the word
"highlights" in the file name. A .txt is a weak reading of "editable file";
Elsevier's own instruction and every example they publish assume a Word file.
This script emits that file and enforces the count and character caps first,
so a non-compliant set never reaches the submission system.

Input: one bullet per line. Blank lines and lines starting with # are ignored.

Usage:
    .venv/bin/python scripts/make_highlights_docx.py highlights.txt
    .venv/bin/python scripts/make_highlights_docx.py highlights.txt -o highlights.docx
    .venv/bin/python scripts/make_highlights_docx.py in.txt --max-chars 85 --min 3 --max 5

Exit code 0 = compliant and written, 1 = a cap was breached (nothing written
unless --force).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import docx
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    from docx.shared import Pt, RGBColor
except ImportError:
    sys.exit("python-docx missing. Run: .venv/bin/pip install python-docx lxml")


# Capitalised tokens that are units or symbols rather than acronyms.
ALLOWED_CAPS = {"DNA", "RNA", "PH", "UV", "II", "III", "IV"}


def set_run(run, font: str, size: float, bold: bool = False) -> None:
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = RGBColor(0, 0, 0)
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    for attr in ("w:ascii", "w:hAnsi", "w:cs"):
        rf.set(qn(attr), font)


def read_bullets(path: Path) -> list[str]:
    lines = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        s = raw.strip().lstrip("-*•").strip()
        if not s or s.startswith("#"):
            continue
        lines.append(s)
    return lines


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="text file, one highlight per line")
    ap.add_argument("-o", "--output", help="output .docx (default: <source stem>.docx)")
    ap.add_argument("--max-chars", type=int, default=85,
                    help="per-bullet character cap, spaces included (default 85)")
    ap.add_argument("--min", dest="lo", type=int, default=3, help="minimum bullets")
    ap.add_argument("--max", dest="hi", type=int, default=5, help="maximum bullets")
    ap.add_argument("--font", default="Times New Roman")
    ap.add_argument("--size", type=float, default=12)
    ap.add_argument("--heading", default="Highlights",
                    help='set to "" to omit the heading')
    ap.add_argument("--force", action="store_true",
                    help="write the file even if a cap is breached")
    ap.add_argument("--allow-acronyms", action="store_true",
                    help="suppress the no-acronyms warning")
    a = ap.parse_args()

    src = Path(a.source)
    if not src.exists():
        sys.exit(f"File not found: {src}")
    out = Path(a.output) if a.output else src.with_suffix(".docx")

    if "highlight" not in out.name.lower():
        print(f"WARNING  output name {out.name!r} lacks the word 'highlights'; "
              "publishers match on the file name.")

    bullets = read_bullets(src)
    problems = []
    warnings = []

    print(f"{len(bullets)} highlight(s) read from {src}\n")
    width = len(str(len(bullets)))
    for i, b in enumerate(bullets, 1):
        n = len(b)
        ok = n <= a.max_chars
        flag = "ok " if ok else "OVER"
        print(f"  {str(i).rjust(width)}. [{flag} {str(n).rjust(3)}/{a.max_chars}] {b}")
        if not ok:
            problems.append(f"bullet {i} is {n} characters, {n - a.max_chars} over the cap")

        # Elsevier highlights rules: "No jargon, acronyms, or abbreviations: aim for
        # a general audience and use keywords."
        acr = [w for w in re.findall(r"\b[A-Z]{2,}\b", b) if w not in ALLOWED_CAPS]
        if acr and not a.allow_acronyms:
            warnings.append(f"bullet {i} uses acronym(s) {acr}; publishers ask for a "
                            "general audience with no acronyms or abbreviations")
        # "1.5-3.4e-5" is computer notation, not publication notation.
        sci = re.findall(r"\d+(?:\.\d+)?[eE][-+]?\d+", b)
        if sci:
            warnings.append(f"bullet {i} uses computer notation {sci}; write it as "
                            "1.5 \u00d7 10\u207b\u2075 instead")
        # A numeric range wants an en dash, not a hyphen.
        rng = re.findall(r"\d+(?:\.\d+)?-\d+(?:\.\d+)?", b)
        if rng:
            warnings.append(f"bullet {i} writes the range {rng} with a hyphen; "
                            "use an en dash (\u2013)")

    if not a.lo <= len(bullets) <= a.hi:
        problems.append(f"{len(bullets)} bullets, but the journal allows {a.lo} to {a.hi}")

    print()
    for w in warnings:
        print(f"WARN  {w}")
    if warnings:
        print()
    if problems:
        for p in problems:
            print(f"FAIL  {p}")
        if not a.force:
            print("\nNothing written. Shorten the bullets, or pass --force to override.")
            sys.exit(1)
        print("\n--force given: writing a non-compliant file anyway.")
    else:
        print(f"PASS  {len(bullets)} bullets, all within {a.max_chars} characters.")

    doc = docx.Document()
    for s in doc.sections:
        s.different_first_page_header_footer = False

    if a.heading:
        h = doc.add_paragraph()
        h.alignment = WD_ALIGN_PARAGRAPH.LEFT
        set_run(h.add_run(a.heading), a.font, a.size, bold=True)

    for b in bullets:
        try:
            p = doc.add_paragraph(style="List Bullet")
            run = p.add_run(b)
        except KeyError:  # template without the style
            p = doc.add_paragraph()
            run = p.add_run(f"• {b}")
        p.paragraph_format.space_after = Pt(6)
        set_run(run, a.font, a.size)

    doc.save(str(out))
    print(f"\nWrote: {out}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Stamp peer-review submission presentation onto an existing .docx.

Adds the three things journal editorial offices reject manuscripts for, none of
which appear in most public author guides:

  1. Continuous line numbers   (w:lnNumType in every sectPr)
  2. Page numbers              (centred PAGE field in the footer)
  3. Double line spacing       (body paragraphs; table cells left alone)

This is idempotent: running it twice produces the same document. It rewrites
presentation only and never touches the text, so it is safe to run on a final
manuscript immediately before upload.

Usage:
    .venv/bin/python scripts/apply_submission_format.py MS.docx
    .venv/bin/python scripts/apply_submission_format.py MS.docx -o MS_formatted.docx
    .venv/bin/python scripts/apply_submission_format.py MS.docx --spacing 1.5
    .venv/bin/python scripts/apply_submission_format.py MS.docx --no-double-space

Exit code 0 = written, 1 = error.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

try:
    import docx
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Pt
except ImportError:
    sys.exit("python-docx missing. Run: .venv/bin/pip install python-docx lxml")

# Schema order of CT_SectPr children. A new element must be inserted at the
# right index or Word reports the file as corrupt.
SECTPR_ORDER = [
    "headerReference", "footerReference", "footnotePr", "endnotePr", "type",
    "pgSz", "pgMar", "paperSrc", "pgBorders", "lnNumType", "pgNumType", "cols",
    "formProt", "vAlign", "noEndnote", "titlePg", "textDirection", "bidi",
    "rtlGutter", "docGrid", "printerSettings", "sectPrChange",
]


def _local(el) -> str:
    return el.tag.split("}", 1)[-1]


def insert_in_order(parent, tag: str):
    """Get or create a direct child <w:tag>, placed at its schema position."""
    existing = parent.find(qn(f"w:{tag}"))
    if existing is not None:
        return existing
    new = OxmlElement(f"w:{tag}")
    try:
        rank = SECTPR_ORDER.index(tag)
    except ValueError:
        parent.append(new)
        return new
    for child in parent:
        name = _local(child)
        if name not in SECTPR_ORDER or SECTPR_ORDER.index(name) > rank:
            child.addprevious(new)
            return new
    parent.append(new)
    return new


def add_line_numbers(section, count_by: int = 1, distance_twips: int = 360) -> None:
    """Continuous line numbering, numbering every line, restarting never."""
    ln = insert_in_order(section._sectPr, "lnNumType")
    ln.set(qn("w:countBy"), str(count_by))
    ln.set(qn("w:restart"), "continuous")
    ln.set(qn("w:distance"), str(distance_twips))


def add_page_numbers(section, font: str | None, size_pt: float | None) -> None:
    """Centred PAGE field in the footer. Replaces any footer this script wrote."""
    footer = section.footer
    footer.is_linked_to_previous = False

    para = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    # Idempotency: clear whatever is there before re-stamping.
    for r in list(para._p.findall(qn("w:r"))):
        para._p.remove(r)
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    def _run(children):
        r = OxmlElement("w:r")
        if font or size_pt:
            rpr = OxmlElement("w:rPr")
            if font:
                rf = OxmlElement("w:rFonts")
                for attr in ("w:ascii", "w:hAnsi", "w:cs"):
                    rf.set(qn(attr), font)
                rpr.append(rf)
            if size_pt:
                sz = OxmlElement("w:sz")
                sz.set(qn("w:val"), str(int(size_pt * 2)))
                rpr.append(sz)
            r.append(rpr)
        for c in children:
            r.append(c)
        para._p.append(r)

    def _fld(kind):
        e = OxmlElement("w:fldChar")
        e.set(qn("w:fldCharType"), kind)
        return e

    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    placeholder = OxmlElement("w:t")
    placeholder.text = "1"

    _run([_fld("begin")])
    _run([instr])
    _run([_fld("separate")])
    _run([placeholder])
    _run([_fld("end")])


def table_paragraph_ids(doc) -> set[int]:
    """ids of paragraphs living inside a table, at any nesting depth."""
    ids: set[int] = set()

    def walk(tables):
        for t in tables:
            for row in t.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        ids.add(id(p._p))
                    walk(cell.tables)

    walk(doc.tables)
    return ids


def set_spacing(doc, spacing: float) -> int:
    """Apply line spacing to body paragraphs. Table cells keep their own."""
    skip = table_paragraph_ids(doc)
    n = 0
    for p in doc.paragraphs:
        if id(p._p) in skip:
            continue
        p.paragraph_format.line_spacing = spacing
        n += 1
    return n


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx", help="manuscript to format")
    ap.add_argument("-o", "--output", help="write here instead of in place")
    ap.add_argument("--spacing", type=float, default=2.0,
                    help="body line spacing (default 2.0 = double)")
    ap.add_argument("--no-line-numbers", action="store_true")
    ap.add_argument("--no-page-numbers", action="store_true")
    ap.add_argument("--no-double-space", action="store_true")
    ap.add_argument("--count-by", type=int, default=1,
                    help="number every Nth line (default 1)")
    ap.add_argument("--footer-font", default=None,
                    help='e.g. "Times New Roman"; omit to inherit')
    ap.add_argument("--footer-size", type=float, default=None, help="footer pt size")
    ap.add_argument("--no-backup", action="store_true",
                    help="skip the .bak copy when writing in place")
    a = ap.parse_args()

    src = Path(a.docx)
    if not src.exists():
        sys.exit(f"File not found: {src}")
    dst = Path(a.output) if a.output else src

    if dst == src and not a.no_backup:
        bak = src.with_suffix(src.suffix + ".bak")
        shutil.copy2(src, bak)
        print(f"Backup: {bak}")

    doc = docx.Document(str(src))
    done = []

    if not a.no_line_numbers:
        for s in doc.sections:
            add_line_numbers(s, count_by=a.count_by)
        done.append(f"line numbers (continuous, every {a.count_by} line(s), "
                    f"{len(doc.sections)} section(s))")

    if not a.no_page_numbers:
        for s in doc.sections:
            add_page_numbers(s, a.footer_font, a.footer_size)
        done.append("page numbers (centred PAGE field in footer)")

    if not a.no_double_space:
        n = set_spacing(doc, a.spacing)
        done.append(f"line spacing {a.spacing} on {n} body paragraphs")

    doc.save(str(dst))
    print(f"Wrote: {dst}")
    for d in done:
        print(f"  + {d}")
    if not done:
        print("  (nothing to do: every action was disabled)")


if __name__ == "__main__":
    main()

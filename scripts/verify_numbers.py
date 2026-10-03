#!/usr/bin/env python3
"""
verify_numbers.py — provenance gate for numeric claims in a manuscript.

Every number in the body must be traceable to a machine-readable source or to an
explicit ledger entry. A number that matches only a previous draft is NOT verified;
that is the failure mode this script exists to catch.

Usage:
  verify_numbers.py MANUSCRIPT [--results DIR]... [--ledger FILE] [--strict]

Exit 1 if any number is UNVERIFIED (or, with --strict, if any is LEDGER-only
without a source field).
"""
import argparse, csv, json, re, sys
from pathlib import Path

NUM = re.compile(r'(?<![\w.])[-+]?\d+(?:\.\d+)?(?![\w])')

# Numbers that carry no scientific claim and never need provenance.
TRIVIAL = {
    *[str(i) for i in range(0, 13)],          # counts, section/figure/table numbers
    '95', '100', '0.05', '1.0', '0.5', '2.5', '5', '10', '20', '30', '50',
}
SKIP_LINE = re.compile(r'^\s*(#|\||\[Figure|\*\*Table|\*\*Figure|E-mail|\*\*ORCID)')

# Spans whose numbers are not claims about this study's data.
CITATION = re.compile(r'\((?:[^()]*?\b(?:19|20)\d\d[a-z]?)\)|\b[A-Z][\w\'-]+(?:\s+\*?et al\*?)?\s+\((?:19|20)\d\d\)')
VERSION  = re.compile(r'\b(?:Python|scikit-learn|NumPy|SciPy|pandas|v)\s*\d[\d.]*', re.I)
GRANT    = re.compile(r'\b[A-Z]{2,}\s*[\d][\dA-Z-]*\b')
DOI      = re.compile(r'\bdoi:\s*\S+', re.I)
ORCID    = re.compile(r'\b\d{4}-\d{4}-\d{4}-\d{3}[\dX]\b')


def mask_noncllaims(line: str) -> str:
    """Blank out spans whose numbers are citations, versions, grants or DOIs."""
    for rx in (CITATION, VERSION, GRANT, DOI, ORCID):
        line = rx.sub(lambda m: ' ' * len(m.group(0)), line)
    return line


def manuscript_text(path: Path) -> str:
    if path.suffix.lower() == '.docx':
        try:
            from docx import Document
        except ImportError:
            sys.exit("python-docx required to read .docx")
        d = Document(str(path))
        keep = []
        for p in d.paragraphs:
            st = (p.style.name or '')
            # Prefix headings with '#' so they are skipped exactly as in markdown, while
            # remaining findable by the reference-stripping step below.
            keep.append(('## ' + p.text) if (st.startswith('Heading') or st == 'Title') else p.text)
        return '\n'.join(keep)
    return path.read_text()


def body_only(text: str) -> str:
    """Strip references and front matter: reference numbers are not claims."""
    for marker in ('\n## References', '\n# References', '\nReferences\n'):
        if marker in text:
            return text.split(marker)[0]
    return text


def harvest_sources(dirs):
    """Every numeric token appearing in any results file, mapped to its file."""
    found = {}
    for d in dirs:
        for f in sorted(Path(d).rglob('*')):
            if f.suffix.lower() not in ('.csv', '.json', '.tsv', '.txt'):
                continue
            try:
                raw = f.read_text(errors='ignore')
            except Exception:
                continue
            for m in NUM.finditer(raw):
                tok = m.group(0)
                try:
                    v = float(tok)
                except ValueError:
                    continue
                # index at every precision the manuscript might quote, keeping BOTH the
                # zero-padded and the trimmed form ("0.910" and "0.91" both index 0.9101).
                # A results file may store a proportion where the manuscript quotes a
                # percentage (0.981 -> 98.1%), so index both scalings.
                for scaled in (v, v * 100.0):
                    for prec in (0, 1, 2, 3, 4):
                        padded = f"{scaled:.{prec}f}"
                        found.setdefault(padded, set()).add(f.name)
                        trimmed = padded.rstrip('0').rstrip('.') if '.' in padded else padded
                        if trimmed:
                            found.setdefault(trimmed, set()).add(f.name)
                found.setdefault(tok, set()).add(f.name)
    return found


def load_ledger(path):
    if not path or not Path(path).exists():
        return {}
    data = json.loads(Path(path).read_text())
    return {str(k): v for k, v in data.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('manuscript')
    ap.add_argument('--results', action='append', default=[])
    ap.add_argument('--ledger')
    ap.add_argument('--strict', action='store_true')
    a = ap.parse_args()

    text = body_only(manuscript_text(Path(a.manuscript)))
    sources = harvest_sources(a.results) if a.results else {}
    ledger = load_ledger(a.ledger)

    # Work paragraph-by-paragraph so a citation split across a line break is still masked.
    paras, buf = [], []
    for line in text.split('\n'):
        if SKIP_LINE.match(line) or not line.strip():
            if buf:
                paras.append(' '.join(buf)); buf = []
            continue
        buf.append(line.strip())
    if buf:
        paras.append(' '.join(buf))

    claims = {}
    for para in paras:
        masked = mask_noncllaims(para)
        for m in NUM.finditer(masked):
            tok = m.group(0).lstrip('+')
            if tok.lstrip('-') in TRIVIAL:
                continue
            s = max(0, m.start() - 45)
            claims.setdefault(tok, para[s:m.end() + 45])

    matched, ledgered, unverified = [], [], []
    for tok, ctx in sorted(claims.items(), key=lambda kv: kv[0]):
        key = tok.lstrip('-')
        if key in sources:
            matched.append((tok, sorted(sources[key])[0]))
        elif tok in ledger or key in ledger:
            entry = ledger.get(tok, ledger.get(key))
            ledgered.append((tok, entry, ctx))
        else:
            unverified.append((tok, ctx))

    print(f"Provenance check — {Path(a.manuscript).name}")
    print("-" * 78)
    print(f"  numeric claims examined : {len(claims)}")
    print(f"  matched to results files: {len(matched)}")
    print(f"  covered by ledger       : {len(ledgered)}")
    print(f"  UNVERIFIED              : {len(unverified)}")
    bad_ledger = [l for l in ledgered if not (isinstance(l[1], dict) and l[1].get('source'))]
    if ledgered:
        print("\nLedger-covered claims:")
        for tok, entry, ctx in ledgered:
            src = entry.get('source', 'NO SOURCE FIELD') if isinstance(entry, dict) else str(entry)
            print(f"  {tok:>10}  <- {src}")
    if unverified:
        print("\nUNVERIFIED — trace each to a results file or add a ledger entry with a source:")
        for tok, ctx in unverified:
            print(f"  {tok:>10}  in: {ctx}")
    print("-" * 78)
    fail = bool(unverified) or (a.strict and bool(bad_ledger))
    print("FAIL" if fail else "PASS")
    return 1 if fail else 0


if __name__ == '__main__':
    sys.exit(main())

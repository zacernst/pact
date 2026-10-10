#!/usr/bin/env python3
r"""Build the Pact's Table of Subjects.

The index is keyed to Article and Section, never to the page. That is how a
legal code is cited, it is how this book cites itself everywhere, it survives
repagination, and it is what a clerk would actually have made.

Input is tools/subjects.tsv, a curated term table of three tab-separated
fields:

    headword <TAB> subentry <TAB> refs

`subentry` may be empty, in which case the refs hang off the headword itself.
`refs` is a space-separated list of tokens, each one of:

    some-unique-substring   a Section, given as any unique substring of its
                            \label{sec:...} -- "airlock-and-the-dep" will do
    art:cleaning            a whole Article, printed as a bare Article number
    =Other Headword         "See Other Headword"      (no refs may follow)
    +Other Headword         "See also Other Headword"

Substrings are resolved against the real labels and an ambiguous or unmatched
one is a hard error, so the table cannot rot the way a hand-typed list of
numbers would. The emitted references are \ref commands, not literal numbers,
for the same reason -- renumbering an Article renumbers the index with it.

Output is book/backmatter/subjects.tex, which is committed; `make` does not
run this script. Re-run it after editing the term table:

    python3 tools/mkindex.py

Exits non-zero if anything in the term table does not resolve.
"""

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "book"
TABLE = ROOT / "tools" / "subjects.tsv"
OUT = BOOK / "backmatter" / "subjects.tex"

CHAPTER = re.compile(r"\\chapter\{(.*?)\}")
ART_LABEL = re.compile(r"\\label\{(art:[^}]+)\}")
SECTION = re.compile(r"\\section\{(.*?)\}\s*\n\\label\{(sec:[^}]+)\}")

# Words a clerk would not file under. "The Cleaning" files at C, so headwords
# are written inverted ("Cleaning, the") and the sort key drops the comma and
# whatever trails it, along with any leading article.
LEADING = re.compile(r"^(?:the|a|an)\s+", re.I)
NOISE = re.compile(r"[^a-z0-9 ]+")


def sections():
    """Every Section of the Pact, in printed order.

    Returns a list of (article_number, section_number, art_label, sec_label)
    and a dict from sec_label to that tuple.
    """
    rows = []
    for path in sorted(BOOK.glob("articles/article*.tex")):
        text = path.read_text(encoding="utf8")
        art_no = int(path.name[len("article"):-len(".tex")])
        m = ART_LABEL.search(text)
        if not m:
            sys.exit("%s has no \\label{art:...}" % path.name)
        art_label = m.group(1)
        for sec_no, sm in enumerate(SECTION.finditer(text), 1):
            rows.append((art_no, sec_no, art_label, sm.group(2)))
    return rows, {r[3]: r for r in rows}


def sort_key(headword):
    key = unicodedata.normalize("NFKD", headword).encode("ascii", "ignore").decode()
    key = key.split(",")[0]
    key = LEADING.sub("", key.strip().lower())
    return (NOISE.sub("", key), headword.lower())


def resolve(token, rows, by_label, articles, where):
    """One ref token -> ('sec', art_label, sec_label) or ('art', art_label)."""
    if token.startswith("art:"):
        if token not in articles:
            sys.exit("%s: no such Article label %r" % (where, token))
        return ("art", token)
    if token in by_label:
        row = by_label[token]
        return ("sec", row[2], row[3])
    hits = [r for r in rows if token in r[3]]
    if not hits:
        sys.exit("%s: no Section label contains %r" % (where, token))
    if len(hits) > 1:
        sys.exit("%s: %r is ambiguous -- matches %s"
                 % (where, token, ", ".join(h[3] for h in hits[:4])))
    row = hits[0]
    return ("sec", row[2], row[3])


def read_table(rows, by_label, articles):
    entries = {}          # headword -> {"refs": [...], "subs": {sub: [...]}}
    order = []
    nrefs = 0
    for lineno, line in enumerate(TABLE.read_text(encoding="utf8").split("\n"), 1):
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        where = "subjects.tsv:%d" % lineno
        parts = line.split("\t")
        if len(parts) != 3:
            sys.exit("%s: expected 3 tab-separated fields, found %d"
                     % (where, len(parts)))
        head, sub, refs = (p.strip() for p in parts)
        if not head:
            sys.exit("%s: empty headword" % where)
        if head not in entries:
            entries[head] = {"refs": [], "subs": {}, "order": []}
            order.append(head)
        target = entries[head]
        resolved = []
        for token in refs.split():
            if token.startswith("="):
                resolved.append(("see", token[1:].replace("_", " ")))
            elif token.startswith("+"):
                resolved.append(("seealso", token[1:].replace("_", " ")))
            else:
                resolved.append(resolve(token, rows, by_label, articles, where))
                nrefs += 1
        if sub:
            if sub not in target["subs"]:
                target["subs"][sub] = []
                target["order"].append(sub)
            target["subs"][sub].extend(resolved)
        else:
            target["refs"].extend(resolved)
    return entries, order, nrefs


def check_crossrefs(entries):
    bad = []
    for head, body in entries.items():
        streams = [body["refs"]] + list(body["subs"].values())
        for stream in streams:
            for kind, *rest in stream:
                if kind in ("see", "seealso") and rest[0] not in entries:
                    bad.append("%s: %s %r, which is not a headword"
                               % (head, kind, rest[0]))
        # A bare "See" sends the reader elsewhere instead; a headword that
        # carries references of its own wants "See also".
        has_own = (any(k in ("sec", "art") for k, *_ in body["refs"])
                   or bool(body["subs"]))
        if has_own and any(k == "see" for k, *_ in body["refs"]):
            bad.append("%s: has its own references and a bare See; "
                       "use See also" % head)
    if bad:
        print("\n%d bad cross-reference(s):" % len(bad))
        for b in bad:
            print("  " + b)
        sys.exit(1)


def fmt(stream):
    """One entry's references: the Sections, then See, then See also.

    A headword may carry several cross-references; they are gathered under one
    "See also" rather than repeating the words, which is how a clerk sets it.
    """
    refs, sees, alsos = [], [], []
    for kind, *rest in stream:
        if kind == "sec":
            refs.append(r"\subjref{%s}{%s}" % (rest[0], rest[1]))
        elif kind == "art":
            refs.append(r"\subjart{%s}" % rest[0])
        elif kind == "see":
            sees.append(rest[0])
        else:
            alsos.append(rest[0])
    parts = []
    if refs:
        parts.append(", ".join(refs))
    if sees:
        parts.append(r"\subjsee{%s}" % "; ".join(sees))
    if alsos:
        parts.append(r"\subjseealso{%s}" % "; ".join(alsos))
    return ". ".join(parts)


def main():
    rows, by_label = sections()
    articles = {r[2] for r in rows}
    entries, _, nrefs = read_table(rows, by_label, articles)
    check_crossrefs(entries)

    lines = [
        "% Generated by tools/mkindex.py -- do not edit by hand.",
        "% The term table is tools/subjects.tsv; re-run the script after",
        "% editing it. References are \\ref commands so that renumbering an",
        "% Article renumbers the Table of Subjects with it.",
        "",
        r"\subjectsopen",
        "",
    ]
    letter = None
    for head in sorted(entries, key=sort_key):
        body = entries[head]
        initial = sort_key(head)[0][:1].upper() or "?"
        if initial != letter:
            letter = initial
            lines.append(r"\subjletter{%s}" % letter)
        lines.append(r"\subjentry{%s}{%s}" % (head, fmt(body["refs"])))
        for sub in body["order"]:
            lines.append(r"\subjsub{%s}{%s}" % (sub, fmt(body["subs"][sub])))
    lines += ["", r"\subjectsclose", ""]
    OUT.write_text("\n".join(lines), encoding="utf8")

    nsubs = sum(len(b["subs"]) for b in entries.values())
    print("%d headwords, %d subentries, %d references -> %s"
          % (len(entries), nsubs, nrefs, OUT.relative_to(ROOT)))
    covered = {tuple(rest) for b in entries.values()
               for stream in [b["refs"]] + list(b["subs"].values())
               for kind, *rest in stream if kind == "sec"}
    missing = [r for r in rows if (r[2], r[3]) not in covered]
    if missing:
        print("%d of %d Sections are not indexed:" % (len(missing), len(rows)))
        for art_no, sec_no, _, lab in missing:
            print("  %d.%d  %s" % (art_no, sec_no, lab))
    else:
        print("every one of the %d Sections is reachable from the table" % len(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())

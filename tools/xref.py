#!/usr/bin/env python3
r"""Check the Pact's cross-references.

The Pact cites itself in prose ("under Article 17", "under Article 13,
Section 6") but drives the numbers off \label/\ref through the \artref,
\secref, and \secrefhere macros in pact.sty, so LaTeX reports any reference
it cannot resolve. This script checks the things LaTeX cannot:

  1. No literal "Article N" or "Section N" citation has crept back in -- those
     are the ones that break silently when an Article or Section is renumbered.
  2. Every label named by a reference actually exists (LaTeX catches this too,
     but this runs in a second and does not need a build).
  3. Every section carries a label, and no label is defined twice.
  4. The Amendment Log's "Unamended Provisions" list agrees with the Articles
     the Log's own entries say they amend.
  5. No span is measured in a unit Article 1 does not define -- the silo has
     days, cycles, seasons and years, and no week or month.

Run from anywhere:  python3 tools/xref.py
Exits non-zero if anything fails.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "book"
if not BOOK.is_dir():
    sys.exit("cannot find book/ next to tools/")

LITERAL = re.compile(r"\b(?:Articles?|Sections?)~?\s\d+")
LABEL = re.compile(r"\\label\{([^}]+)\}")
REF = re.compile(r"\\(?:artref|secref|secrefhere|artnum|secnum|ref)\{([^}]+)\}")
SECTION = re.compile(r"^\\section\{")
# Article 1 defines the day, the cycle (ten days), the season (nine cycles)
# and the year (four seasons). The silo has no week and no month, so a span
# named in either is an import from outside; so is "seven days", which is a
# week wearing a disguise. A span longer than a cycle belongs in cycles.
NUMBER = (r"one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
          r"thirteen|fourteen|fifteen|twenty|thirty|forty")
BAD_SPAN = re.compile(r"\b(?:%s)\s+(?:weeks?|months?)\b" % NUMBER)
ODD_DAYS = re.compile(r"\b(?:seven|eleven|twelve|thirteen|fourteen|fifteen|"
                      r"twenty|thirty|forty)\s+days\b")


def sources():
    yield BOOK / "frontmatter/preamble.tex"
    yield from sorted(BOOK.glob("articles/article*.tex"))
    yield BOOK / "backmatter/amendments.tex"
    yield BOOK / "backmatter/clerks-sheet.tex"


def main():
    problems = []
    labels = {}
    refs = []
    sections = 0
    nlabels = 0

    for path in sorted(BOOK.glob("**/*.tex")):
        for lineno, line in enumerate(path.read_text().split("\n"), 1):
            for m in LABEL.finditer(line):
                if m.group(1) in labels:
                    problems.append("%s:%d: label %s defined twice (also %s)"
                                    % (path.name, lineno, m.group(1),
                                       labels[m.group(1)]))
                labels[m.group(1)] = "%s:%d" % (path.name, lineno)

    for path in sources():
        lines = path.read_text().split("\n")
        for lineno, line in enumerate(lines, 1):
            where = "%s:%d" % (path.name, lineno)
            if SECTION.match(line):
                sections += 1
                nxt = lines[lineno] if lineno < len(lines) else ""
                if not nxt.startswith("\\label{sec:"):
                    problems.append("%s: section has no \\label" % where)
                else:
                    nlabels += 1
            for m in LITERAL.finditer(line):
                problems.append("%s: literal citation %r -- use \\artref, "
                                "\\secref or \\secrefhere" % (where, m.group(0)))
            for m in REF.finditer(line):
                refs.append((where, m.group(1)))
            for m in BAD_SPAN.finditer(line):
                problems.append("%s: %r -- the silo has no week and no month"
                                % (where, m.group(0)))
            for m in ODD_DAYS.finditer(line):
                problems.append("%s: %r -- a span past a cycle is named in "
                                "cycles; the silo has no week"
                                % (where, m.group(0)))

    for where, label in refs:
        if label not in labels:
            problems.append("%s: reference to undefined label %s" % (where, label))

    # The Log claims a set of Articles is unamended; check its own entries.
    log = (BOOK / "backmatter/amendments.tex").read_text()
    tail = re.search(r"Unamended Provisions(.*)$", log, re.S)
    if tail:
        claimed = set(re.findall(r"\\artref\{(art:\w+)\}", tail.group(1)))
        amended = set()
        for entry in re.split(r"\\subsection\*\{Amendment ", log)[1:]:
            for quoted in re.findall(r"``(.*?)''", entry, re.S):
                m = re.match(r"\s*\\(?:secref|artref)\{(art:\w+)\}", quoted)
                if m:
                    amended.add(m.group(1))
        both = claimed & amended
        if both:
            problems.append("Unamended Provisions lists %s, but the Log's own "
                            "entries amend them"
                            % ", ".join(sorted(both)))

    print("%d sections, %d section labels, %d labels total, %d references"
          % (sections, nlabels, len(labels), len(refs)))
    if problems:
        print("\n%d problem(s):" % len(problems))
        for p in problems:
            print("  " + p)
        return 1
    print("all cross-references resolve; no literal citations; spans in Pact units")
    return 0


if __name__ == "__main__":
    sys.exit(main())

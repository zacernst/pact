**This was written completely by AI with methodological guidance and rules from me (a human).**

The full text is the `main.pdf` file in the `book/` directory.

# The Pact

An original, full-length recreation of **the Pact** — the in-universe public
legal code of a silo in Hugh Howey's *Wool* / Silo series — written to be
internally consistent with the *Wool*, *Shift*, and *Dust* books.

This is not a reproduction of any published Howey text. It is new prose,
written to plausibly be "the document Holston, Jahns, Bernard, and Juliette
would have on their shelves," respecting what canon establishes and
inventing only what canon leaves open.

## Scope

- **Setting**: the silo's "current era," the same rough timeframe as the
  main *Wool* narrative. The Pact's own text is deliberately ambiguous
  about how long ago it was written and whether its founders ever lived
  inside the silo (see `FACTS.md`, open item 1). This is a decision, not an
  omission: the Amendment Log declines a calendar on principle. What the
  edition *does* fix is where this particular copy sits relative to its own
  law --- it was printed between Amendment 20 and Amendment 21.
- **Content boundary**: this is the *public* Pact only — the law every
  citizen is taught and can read. It excludes **the Order**, the separate
  classified document known only to IT, which in canon holds the
  suppressed true history, the cleaning-suit sabotage protocol, inter-silo
  secrets, and doomsday contingencies. Where the Pact needs to gesture at
  IT holding some further secret authority, it does so without ever
  stating Order content.
- **Length/density**: target **60,000+ words** of statute — numbered
  Articles, Sections, and lettered clauses, plus front and back matter.
  Current source is roughly 73,600 words; see "Current state."
- **Front/back matter**: an in-world Preamble, a table of Articles and
  Sections, and a back-matter **Amendment Log** of fictional ratified
  amendments, written so that later hands visibly imitate the founders'
  form without their insight.
- **Format**: a LaTeX book built to PDF. Sober statute typesetting,
  Arabic-numbered Articles, numbered Sections, lettered clauses.
- **The copy, not the text**: the PDF is typeset as one *particular
  printed copy* of the Pact held in the silo, carrying the papers the
  Pact's own Articles 21 and 23 require a copy to carry. See "The artifact
  layer."

## Canon research caveat

All canon details come from secondary web sources (summaries, study
guides, the Apple TV+ show's fan-transcribed prop Pact) and the
assistant's trained knowledge of the books, **not verified against the
primary text**. `CANON.md` records what was found and how confident it is.
TV-only material is used to fill gaps where it does not conflict with the
books and is tagged `[TV]`.

## Repository layout

```
book/
  main.tex               # assembles the whole document
  pact.sty               # all formatting (hand-rolled; see below)
  Makefile               # `make` builds main.pdf via latexmk
  frontmatter/
    titlepage.tex        # the title page
    placing.tex          # the Placing Page: blanks for the level, the copy
                         #   number, and nine yearly comparisons
    correction.tex       # the Notice of a Correction entered against this copy
    preamble.tex         # the Pact's own Preamble
  articles/              # article01.tex .. article23.tex
  backmatter/
    clerks-sheet.tex     # the Clerk's sheet setting in Amendment 21, which
                         #   was ratified after this copy was printed
    amendments.tex       # the Amendment Log, and a table of the amendments
    colophon.tex         # the printer's note on the final verso
  main-classic.tex, pact-classic.sty, frontmatter/titlepage-classic.tex
                         # a retired alternative typographic treatment,
                         # kept as source for reference; not built
CANON.md        # canon research notes, tagged by source confidence
STYLE.md        # drafting style guide and the project's guiding principles
FACTS.md        # ledger of facts the Pact asserts, with in-world rationale
HYPOTHESES.md   # "why is this canon fact true" entries and what they generate
PROFESSIONS.md  # inventory of silo trades by Department, shadow tier, zone
REVIEW.md       # 2026-09-03 full-draft review, with a status block
REVIEW-2026-10-07.md
                # second full-draft review (Tiers A-E), with a status block
FAN-REVIEW-2026-10-08.md
                # a hypothetical Howey fan's reading of the finished draft:
                # what works, what frustrates, and seven coverage gaps
AUTHENTICITY-2026-10-08.md
                # the proposal answering that review's typographic
                # frustration, with a status block; see "The artifact layer"
tools/
  xref.py       # consistency checker; see "Verification"
```

### Why the formatting is hand-rolled

This machine's TeXLive install lacks `geometry`, `titlesec`, `enumitem`,
`fancyhdr`, `xcolor`, and `microtype`, and installing them needs `sudo`.
`pact.sty` reimplements what is needed using only the `book` class,
`hyperref`, `lmodern`, `calc`, `graphicx`, `rotating`, and `longtable`:
hand-set 6x9in geometry, Articles as renamed Arabic-numbered chapters,
"Section N." prefixes, `(a)`/`(i)` clause lists via plain `enumerate`,
and a replaced `\ps@headings` that sets the running heads in small caps at
`\footnotesize` --- "Article 22 . Of Emergency and the Suspension of
Ordinary Law" fits the 4.4in measure only at that size. Three fixes are
baked in: `mathpazo` was swapped for `lmodern` because the Palatino font
files are not installed; `book.cls`'s `\ps@headings` is *replaced* rather
than patched, because otherwise it overwrites the Pact's own marks; and
every centred rule is a `\rule`, never an `\hrule`, which is a TeX
primitive that ignores `\centering` and sits flush left.

The one bold face in the book was in the table of contents, and
`\l@chapter` is redefined to set Article entries in small caps instead.
Nothing in the body is bold; emphasis is small caps or italic.

Formatting is hand-rolled, but **cross-references are not**. Every one of
the 237 Sections carries a `\label{sec:...}` keyed to its *meaning* rather
than its number, and every citation in the text is written with
`\artref`, `\secref`, `\secrefhere`, `\artnum`, or `\secnum`, which print
the human form ("Article 17, Section 7") from the label. There are 1,252
such references and no literal "Article N" citations left in the
prose, so an Article or Section can be renumbered without silently
breaking a citation, and LaTeX reports anything that breaks loudly.

## Verification

```
cd book && make            # must end "Output written on main.pdf"
python3 tools/xref.py      # from the repo root; must print the clean line
```

A clean build is 229 pages with **no undefined references and no overfull
boxes**; `grep -c 'Overfull' book/main.log` must report 0. Do not pipe
`make` into `head` or `grep` --- the broken pipe truncates `main.aux` and
the next build reports phantom undefined references.

`tools/xref.py` checks the five things LaTeX cannot: that no literal
"Article N"/"Section N" citation has crept back in; that every label named
by a reference exists; that every Section carries exactly one label; that
the Amendment Log's "Unamended Provisions" list agrees with the Articles
its own entries say they amend; and that no span of time is measured in a
unit Article 1 does not define (the silo has days, cycles, seasons, and
years, and no week or month).

## Current state (2026-10-08)

**All 23 Articles, the Preamble, and a 21-amendment Log are drafted; two
full-draft reviews and a hypothetical fan's review have been applied in
full; and the book is typeset as a particular printed copy.** `make`
builds `book/main.pdf` cleanly --- 229 pages, no undefined references, no
overfull boxes --- and `tools/xref.py` reports no problems across 237
Sections and 1,252 cross-references.

| # | Article | | # | Article |
|---|---|---|---|---|
| 1 | Of the Founding and Purpose of the Silo | | 13 | Of Labor, Shadowing, and the Assignment |
| 2 | Of Citizenship and the Census | | 14 | Of Housing and the Floors |
| 3 | Of Marriage, the Lottery, and the Right of Birth | | 15 | Of Schooling and the Teaching of the Young |
| 4 | Of the Office of Mayor | | 16 | Of Public Order and Forbidden Speech |
| 5 | Of the Deputy Mayor and the Order of Succession | | 17 | Of Crimes and Their Punishments |
| 6 | Of Judicial and the Courts | | 18 | Of the Cleaning |
| 7 | Of the Sheriff and the Keeping of the Peace | | 19 | Of Health, the Infirmary, and the Mind |
| 8 | Of the Department of Information Technology | | 20 | Of Assembly and the Common Halls |
| 9 | Of the Department of Mechanical | | 21 | Of Records, Porters, and the Post |
| 10 | Of the Department of Mines | | 22 | Of Emergency and the Suspension of Ordinary Law |
| 11 | Of Supply, Hydroponics, and the Ration | | 23 | Of Amendment and the Continuance of the Pact |
| 12 | Of Trade, Chits, and Commerce | | A | Amendment Log |

Three full-draft reviews have been applied: `REVIEW.md` (2026-09-03), a
second on 2026-09-06 whose findings are recorded in `FACTS.md`, and
`REVIEW-2026-10-07.md`, whose five tiers were implemented on 2026-10-08.
That pass:

- fixed twelve substantive defects, including two contradictions in
  Article 9 §7, a sentencing dead end in Article 17 (patched in-world as
  Amendment 21 rather than in the founding text), a petition threshold
  with no denominator, an oath of office with no words, and a search
  "conducted in daylight" in a buried silo;
- closed the book's two-register problem — the early sections of Articles
  3, 4, 5, 12, 13, 14, 19, 20, 22, and 23 were in a flat modern
  administrative voice, and are now in the Pact's own; `STYLE.md` carries
  the banned-word list that keeps it from recurring;
- added ten coverage sections the silo would certainly have and the text
  did not: the forbidden degrees of kinship, gatherings of belief, the
  giving of a body to the soil and the mourning, the citizen whose body
  or mind cannot bear the labor assigned, the days the silo keeps, the
  airlock and its approach, and — the single highest-value clause in the
  book — the offense of saying that the wallscreen is false;
- built the label-driven cross-reference system and `tools/xref.py`
  described above.

`FAN-REVIEW-2026-10-08.md` then read the finished draft as a Howey fan
would, and listed seven things a reader would expect the silo's law to
cover and could not find. All seven are now in the text:

| Gap | Where it is answered |
|---|---|
| What the condemned citizen's last day actually contains | Article 18 §8 --- the last meal, the household's cooking and eating once, the roll of askings |
| Whether the condemned ever sees the view before the airlock | Article 7 §6 and Article 18 §8 --- one cell of the station bears a screen, kept by IT and not by the Sheriff, reserved to that citizen and no other |
| How the lottery is actually drawn and audited | Article 3 §5 --- tokens, the Clerk's entry as the only place name and number meet, and an audit on counts rather than identities |
| How a child is named and entered | Article 3 §10 --- who holds the child, the name said three times, the archivist's card, and a naming once entered not undone |
| Why the silo keeps a day of the dead with no names read | Article 20 §8(b) |
| What the stairwell is like as infrastructure | Article 7's new Section --- the inner rail, the lift's loads, carrying a body down and not up, closures, shift-turn hours |
| The three deputy stations as the Sheriff's standing establishment | Article 7 §8 --- the three stations named as such, two Peacekeepers to a zone, and a Peacekeeper keeping a vacant Deputy's post |

**Length target met.** Source is roughly 73,600 words; the rendered PDF is
about 81,800. Articles 5 and 23, which had been structurally underweight
at 924 and 796 words, are now 2,366 and 3,021. Any further growth should
come from a fresh coherence review rather than from more sections;
`FACTS.md` records every fact these passes fixed.

## The artifact layer

The PDF is not a publisher's edition of the Pact. It is one copy of the
Pact as the silo would hold it, and the design rule is that **every page
of apparatus is required by a clause of the Pact itself** --- the book
supplies its own stage directions, so nothing had to be invented to dress
it up. `AUTHENTICITY-2026-10-08.md` is the proposal, with a status block;
`STYLE.md` carries the three tests any addition must pass (is it a thing
an office did; does a clause already require it; would it still be there
if the copy were new).

- **The Placing Page** (p. iii) is the form Article 21 implies: blanks for
  the level the copy is placed upon, the season of its making, the copy's
  number, the placing officer's signature, and nine ruled lines for the
  yearly comparisons against the archive copy --- so a reader can see that
  the copy is meant to be checked, and how often.
- **A Notice of a Correction** (p. v) records, under Article 23 §7, that
  this copy was printed reading *within two cycles* where the master reads
  *within one cycle*. The body carries the correction in place, at Article
  18 §8: the wrong words struck through and the right ones set beside them
  in the Clerk's typeface. It happens exactly once in the book.
- **The Clerk's set-in sheet** (p. 213) carries Amendment 21, which was
  ratified *after this copy was printed*. The printed Amendment Log behind
  it therefore ends at Amendment 20 and still lists Article 17 among its
  unamended provisions --- correctly, for a printing of that date --- and
  the sheet is what strikes it. **This is deliberate and must not be
  "corrected"**; see the do-not-fix list in `FACTS.md`.
- **A Table of the Amendments** precedes the Log, declaring itself a
  finding aid and no part of the amendments, "where the table and an entry
  differ, the entry governs."
- **A colophon** on the final verso: printed by order of the Mayor and of
  Judicial, from the archive copy and from no other, for the placing
  Article 1 requires. No year, and no printer's name.
- **Running heads** carry "Article N . Title" rather than a folio alone,
  and the table of contents is titled as the archivist would title it:
  "The Order of the Articles, and of the Sections Within Them."

What the artifact layer deliberately does *not* do is simulate **wear**.
No foxing, no stains, no coffee rings, no handwriting fonts, no marginalia
from a named character. Those make the copy *old*; the clauses above make
it *used*, which is the thing the Pact's own text can vouch for.

**Still outstanding:** the Table of Subjects --- an in-world index, §3.1 of
the proposal. It needs a `tools/mkindex.py` (the `makeindex` and `texindy`
binaries are not installed, though `makeidx.sty` is and writes a valid
`.idx`) plus a tagging pass over some 400--600 terms.

## Guiding principles

Summarized here; `STYLE.md` has the full statement of each, with its
rationale.

1. **Coherence and consilience**: every fact the Pact asserts has its
   consequences worked out and its in-world explanation recorded, in
   `FACTS.md`, even where the Pact's own text never states it.
2. **The "why" heuristic**: for every canon fact, hypothesize why it is
   true and use that to generate consistent content (`HYPOTHESES.md`).
3. **The Founders' psychology**: the in-world authors value plausibility,
   deceive when useful, are strict utilitarians, and are always internally
   logical. Every rule has a *stated* rationale and a *true* one.
4. **Victor, the psychologist-author**, led the writing; **Anna Thurman**
   is the secondary hand, whose warmer kinship register functions as
   camouflage rather than as a counterweight.
5. **Restraint**: most of the Pact is genuinely mundane administrative law,
   which is what lets the rare planted seams land.
6. **Three readers**: every passage works for the ordinary citizen, the
   in-world close reader, and the reader who knows the whole saga.
7. **Structural fragility**: the design carries real blind spots (Article 2's
   unaudited census and death attestation; Article 5's vacancy election
   with no deadline and a Department-head fallback, now buried in six
   Sections of ordinary handover procedure rather than sitting alone),
   consistent with the saga's ending.
8. **Amendment drift**: later amendments imitate the founders' tricks
   without their insight. Amendments 1, 4, 5, 6, 8, 10, and 11 each carry
   a legible hand of their own — a nervous first exercise of a new power,
   a Supply clerk's arithmetic, a Head of Department's grievance dressed
   as a general principle, a competent imitation of Amendment 1 by
   someone who did not understand it — and the Log now carries a Judge's
   entry recording that two leaves were cut from the roll and the
   amendments after them renumbered, which makes the Log's own order a
   reconstruction.

## Toolchain notes

- `pdflatex` and `latexmk` are installed; `make` from `book/` runs
  `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
- Build artifacts are ignored via `.gitignore`; `book/main.pdf` is tracked
  deliberately as the deliverable.
- The build is clean: zero overfull boxes. The only remaining warnings are
  chapter-break underfull pages, which `\raggedbottom` makes harmless.
- Several packages the project would otherwise use are **not installed**
  and need `sudo`: `microtype`, `tikz`/`pgf`, `imakeidx`, `setspace`,
  `needspace`, `changepage`, `mdframed`, `tcolorbox`, `soul`, `ulem`,
  `eso-pic`, `everypage`. Available and used: `graphicx`, `rotating`,
  `longtable`, `calc`, `makeidx`, `multicol`, `tabularx`, `pifont`.
- **Only Latin Modern is usable.** `charter`, `utopia`, `newcent`,
  `bookman`, `mathptmx`, `courier`, and `helvet` all fail for want of TFM
  files and a Metafont binary. `[T1]{fontenc}` errors at load and is not
  used. Small caps, typewriter, sans, and italic-bold all work; only
  `T1/lmss/m/sc` is missing.

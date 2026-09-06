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
  inside the silo (see `FACTS.md`, open item 1).
- **Content boundary**: this is the *public* Pact only — the law every
  citizen is taught and can read. It excludes **the Order**, the separate
  classified document known only to IT, which in canon holds the
  suppressed true history, the cleaning-suit sabotage protocol, inter-silo
  secrets, and doomsday contingencies. Where the Pact needs to gesture at
  IT holding some further secret authority, it does so without ever
  stating Order content.
- **Length/density**: target **60,000+ words** of statute — numbered
  Articles, Sections, and lettered clauses, plus front and back matter.
  Current source is roughly 60,500 words; see "Current state."
- **Front/back matter**: an in-world Preamble, a table of Articles and
  Sections, and a back-matter **Amendment Log** of fictional ratified
  amendments, written so that later hands visibly imitate the founders'
  form without their insight.
- **Format**: a LaTeX book built to PDF. Sober statute typesetting,
  Arabic-numbered Articles, numbered Sections, lettered clauses.

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
  frontmatter/           # titlepage.tex, preamble.tex
  articles/              # article01.tex .. article23.tex
  backmatter/            # amendments.tex (the Amendment Log)
  main-classic.tex, pact-classic.sty, frontmatter/titlepage-classic.tex
                         # a retired alternative typographic treatment,
                         # kept as source for reference; not built
CANON.md        # canon research notes, tagged by source confidence
STYLE.md        # drafting style guide and the project's guiding principles
FACTS.md        # ledger of facts the Pact asserts, with in-world rationale
HYPOTHESES.md   # "why is this canon fact true" entries and what they generate
PROFESSIONS.md  # inventory of silo trades by Department, shadow tier, zone
REVIEW.md       # 2026-09-03 full-draft review, with a status block
```

### Why the formatting is hand-rolled

This machine's TeXLive install lacks `geometry`, `titlesec`, `enumitem`,
`fancyhdr`, `xcolor`, and `microtype`, and installing them needs `sudo`.
`pact.sty` reimplements what is needed using only the `book` class,
`hyperref`, `lmodern`, `calc`, and `longtable`: hand-set 6x9in geometry,
Articles as renamed Arabic-numbered chapters, "Section N." prefixes,
`(a)`/`(i)` clause lists via plain `enumerate`, and running headers from
the built-in `headings` page style. Two fixes are baked in: `mathpazo`
was swapped for `lmodern` because the Palatino font files are not
installed, and the running headers show only "Article N" / "Section N"
so long titles do not overflow.

## Current state (2026-09-06)

**All 23 Articles, the Preamble, and a 20-entry Amendment Log are
drafted.** `make` builds `book/main.pdf` cleanly (196 pages).

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

Two full-draft reviews have been applied (`REVIEW.md`, 2026-09-03, and a
second on 2026-09-06 whose findings are recorded in `FACTS.md`). The
draft is internally consistent under the numbering above; the notes files
carry a numbering note where their older text may cite an Article by a
superseded number.

**Length target met.** Source is roughly 60,500 words; the rendered PDF
is about 66,000. Three expansion passes on 2026-09-06 added a definitions
section and the printed founding recitation and oath, new sections to
every Article except 4, 5, 20, and 23, and seven late Amendment Log
entries. Any further growth should come from a fresh coherence review of
the expanded text rather than from more sections; `FACTS.md` records
every fact the expansions fixed.

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
   with no deadline and a Department-head fallback), consistent with the
   saga's ending.
8. **Amendment drift**: later amendments imitate the founders' tricks
   without their insight.

## Toolchain notes

- `pdflatex` and `latexmk` are installed; `make` from `book/` runs
  `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
- Build artifacts are ignored via `.gitignore`; `book/main.pdf` is tracked
  deliberately as the deliverable.
- The remaining box warnings in the build log are sub-6pt overfull lines
  and chapter-break underfull pages; none affect the output.

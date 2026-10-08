# Making the Rendered PDF Read as an Artifact

*Proposal, 2026-10-08. Nothing here has been changed. This answers frustrations
\#1 ("There is no way in") and \#2 ("It is not a physical object, and the prop
is") from `FAN-REVIEW-2026-10-08.md`.*

---

## Status: IMPLEMENTED, except the Table of Subjects (2026-10-08)

Everything in sections 2, 3.2--3.4 and 4 below is now in the book. `make`
builds `book/main.pdf` at **229 pages** with **zero overfull boxes** and no
undefined references; `python3 tools/xref.py` is clean at 237 Sections and
1,252 references.

| Item | State |
|---|---|
| 2.1 The Placing Page | `book/frontmatter/placing.tex`, p.\ iii |
| 2.2 Amendment 21 as a set-in sheet | `book/backmatter/clerks-sheet.tex`; the printed Log now ends at Amendment 20 |
| 2.3 Clerk's correction notice | `book/frontmatter/correction.tex`, p.\ v |
| 2.4 One hand-correction in the body | Article 18, Section 8(b) --- `\corr{two cycles}{one cycle}` |
| 2.5 Office stamps, three of them | `\stamp` in `pact.sty`; placing page, notice, set-in sheet |
| 2.6 Colophon | `book/backmatter/colophon.tex` |
| 3.2 Table of the Amendments | head of the Appendix, 20 rows |
| 3.3 Contents renamed | "The Order of the Articles, and of the Sections Within Them" |
| 3.4 Running heads | verso now carries the Article's title; heads set at `\footnotesize` |
| 4 Setting | `\emergencystretch`, `\tolerance`, `\raggedbottom` |
| --- | --- |
| 3.1 **A Table of Subjects** | **not done.** Still the largest outstanding item, and still the one that most directly answers "there is no way in." Needs `tools/mkindex.py` (the `makeindex` binary is absent) and a tagging pass of ~400--600 terms. |

Three things were fixed along the way that this document did not anticipate:
chapter-opening and title-page rules were set with `\hrule`, which ignores
`\centering`, so every Article opened with a left-flush rule under a centred
title; the title page overflowed onto a second page once the rules were
corrected; and the Contents set Articles in bold, the only bold left in the
book and a publisher's habit rather than a department's --- now small caps.

**One consequence to protect.** The printed Log now predates Amendment 21 and
therefore still lists Article 17 among its unamended provisions. That is not an
error. A future pass must not "correct" it, must not move Amendment 21 back
into `amendments.tex`, and must not revise Amendment 5's note out of the
present tense. The whole point of the set-in sheet is that the book is older
than the law it carries.

---

## 0. The governing principle

The show's prop is battered **because it was used**. That is not a thing a PDF
can imitate, and every attempt to imitate it — foxing, coffee rings, torn
edges, a handwriting font — reads instantly as a fan mock-up, because real wear
is irregular and simulated wear is a filter.

What a PDF *can* imitate perfectly is a **printing**: the officiousness of a
document that an institution made, numbered, placed, compared, corrected and
stamped. That is also the register this book already writes in, and —
critically — **the Pact describes its own physical existence in detail and then
does not use any of it on itself:**

| Clause | What it requires of every copy |
|---|---|
| Art. 21 §(copying) (a) | copies made from the archive copy alone, "compared against the archive copy before it is placed; the copy is marked with the floor of its placing and the season of its making" |
| Art. 21 §(copying) (b) | compared once yearly by an Officer of Judicial; a copy found altered, damaged or wanting is replaced within the season |
| Art. 21 §(seal) | seal-stamps cut by Mechanical to a pattern the Judge keeps, **one for each office** |
| Art. 23 §7 | until a fresh printing, a new amendment arrives as "a sheet set in at the Appendix, in the Clerk's hand, bearing the amendment's number, its words, the Article and Section it alters, and the day of its ratifying" |
| Art. 23 §8 | "The master copy ... governs, and a copy found to differ is corrected against it and the correction entered. No citizen is answerable for having obeyed a copy that was wrong, and the Clerk answers for its being wrong." |
| Art. 23 §9 | a citizen's own copy is corrected on the Clerk's notice, the sheet given free of chits |

**Every recommendation below is this book obeying its own Articles 21 and 23 on
its own body.** That is the whole design. Three tests any addition must pass:

1. **Is it a thing an office did?** If it is a thing weather did, cut it.
2. **Does a clause in the Pact already require it?** If so, cite that clause on
   the page itself.
3. **Would it still be there if the copy were new?** A new copy still has a
   placing, a number, a comparison, a stamp and a set-in sheet. It has no
   stains.

---

## 1. What this toolchain will actually do (verified today, not assumed)

Tested by compiling in the scratchpad, since this project has been bitten once
already by proposing a font (`mathpazo`) whose files are not installed.

**Present and verified working together in one clean compile (`exit=0`, zero
errors):** `graphicx` (`\rotatebox` — a rotated double-ruled small-caps block
renders convincingly as a stamp impression), `atbegshi` (`\AtBeginShipout` page
overlays), `multicol`, `makeidx` (writes a valid `.idx`), `longtable`,
`textcomp`, `pifont`, `rotating`, `tabularx`, `array`, `afterpage`.

**Absent:** `tikz`, `pgf`, `eso-pic`, `everypage`, `imakeidx`, `framed`,
`mdframed`, `tcolorbox`, `soul`, `ulem`, `setspace`, `needspace`,
`changepage`, `microtype`, `bookmark`.

**The `makeindex` *binary* is not installed** (nor `texindy`), although
`makeidx.sty` is. An index is therefore possible but needs a small
`tools/mkindex.py` to turn `.idx` into `.ind` — which we want anyway, see §3.1.

**Type: Latin Modern only.** `charter`, `utopia`, `newcent`, `bookman`,
`mathptmx`, `courier` and `helvet` all have `.sty` files but **all six fail to
compile** — `! Font T1/bch/m/n/12=bchr8t at 12.0pt not loadable: Metric (TFM)
file not found`, with `mktextfm: mf: command not found` so nothing can be
generated on the fly. The only Type1 trees installed are
`public/{cm-super,lm,pdftex,tipa}` and `urw/{symbol,zapfding}`. Within Latin
Modern, verified working: `\textsc`, `\ttfamily` (`lmtt`), `\sffamily`,
`\itshape\bfseries`, `\ttfamily\itshape`. Only `T1/lmss/m/sc` (sans small caps)
is missing and silently substitutes.

So: **"use a more institutional body face" is off the table without `sudo`** —
see §5. Everything in §2 and §3 is reachable with the packages already here.

---

## 2. The artifact layer (no new packages)

### 2.1 The Placing Page — *the single highest-value addition*

A new `frontmatter/placing.tex`, set on the verso of the title page, before the
Table. It is the page Article 21 requires and the book has never had. Small
caps inside a double rule, with **rules to be filled in by hand** — the blanks
are the entire effect, because a blank on a printed form is proof that a form
existed:

```
                 THE DEPARTMENT OF JUDICIAL
                    ARCHIVE OF THE SILO
  ──────────────────────────────────────────────────────

  This copy is made from the archive copy by the hand of
  the archivist, and is compared against it before its
  placing, as this Pact requires at Article 21, Section 4.

  Placed upon Level  ────────────────────────────────────
  Season of its making  ─────────────────────────────────
  This copy numbered  ───────────────────────────────────

  Compared, and found true:  ────────────────────────────
                                     Officer of Judicial

  Compared again, and found true:
       ───────────────  ───────────────  ───────────────
       ───────────────  ───────────────  ───────────────
```

Note what the last block does: Article 21 requires comparison **once yearly**,
so the page needs a row of slots for years of signatures. Six empty slots say
"this copy is expected to outlive you" without a word of prose.

Underneath, in smaller type, the fan's requested occupant line — but in the
Pact's own vocabulary. Copies are **placed**, not owned, so not "this copy
belongs to":

> This copy is in the keeping of the office named above, and is that office's
> charge. A copy found altered, damaged, or wanting is reported to the Judge
> and replaced within the season.
>
> *No citizen is answerable for having obeyed a copy that was wrong, and the
> Clerk answers for its being wrong.* — Article 23, Section 8

That last sentence is already in the text. Printed here, on the front of the
object, it is the most quietly frightening line in the book.

**Cost:** one new file, one `\input` in `main.tex`. No body changes. No risk.

### 2.2 The Clerk's set-in sheet — Amendment 21 arrives late

Article 23 §7 describes exactly the artifact the fan is asking for, and the
book declines to use it. Use it: **end the printed Appendix at Amendment 20,
and let Amendment 21 arrive on a sheet set in at the Appendix** — a single page
immediately before the Log's opening, set in `lmtt` (Latin Modern typewriter —
our only available "second hand") at a narrower measure, inside a ruled border,
carrying precisely the four things the clause requires: the amendment's number,
its words, the Article and Section it alters, and the day of its ratifying.
Footed:

> Set in at the Appendix by the Clerk of Judicial, under Article 23, Section 7,
> this copy not having been printed afresh.

This is the strongest single move available, because it makes **the printing
older than the law**. The book stops being a text and becomes a copy with a
date — one that a reader can place in time relative to events — without the
book ever naming a year. It also pays off Amendment 21 (the indefinite
assignment to the workings), which is the darkest entry in the Log, by making
it the one thing that would not fit in the binding.

A loose sheet falls out at the front of the section it belongs to, so bind it
*before* the Log's heading: the reader meets it first, which primes the whole
Appendix.

**Cost:** move Amendment 21 out of `backmatter/amendments.tex` into
`backmatter/clerks-sheet.tex`; add the `\input`. **Watch:** `tools/xref.py`
check 4 reads the Log to reconcile the Unamended Provisions list, and Amendment
21 is what struck Article 17 from it — the new file must be added to the paths
that check scans, or check 4 will report a false failure.

### 2.3 The Clerk's correction notice — this copy carried wrong law

Separate page, separate job, and it costs nothing in the body. Article 23 §8
provides for a copy found to differ from the master. Print the notice:

> **Notice of a Correction, given under Article 23, Section 8**
>
> This copy was found to differ from the master copy at Article 23, Section 1,
> where it read *one fifth of the full count of the rolls* and the master copy
> reads *one third*. The copy is corrected against the master. The correction
> is entered in the archive. The Clerk answers for its being wrong.
>
> A citizen who acted upon this copy as it stood is not answerable.
> *Given free of chits, as Article 23, Section 9 requires.*

Choose the error to be one that **matters** — a petition threshold, a term of
correction — so that the reader's second thought is the right one: for some
period, every household's copy of the law said a different number than the law
said, and the only remedy was a sheet of paper. The Log already establishes
(the Judge's entry on the numbering) that the record is not stable. This
extends that from the Log to the book in the reader's hands.

Pair it with 2.4 below: strike the wrong word *in the body*, once.

### 2.4 One hand-correction in the body

Article 23 §8 says a copy found to differ "is corrected against it and the
correction entered." A corrected copy shows the correction. **Exactly once**
(twice at the outside), at the clause named in 2.3: the superseded word struck
through with a rule, the true word set beside it in `lmtt`, and an initial in
the margin.

No `soul` or `ulem`, but a strikethrough is six lines of hand-rolled macro
(`\rlap` a `\rule` over a box of the right width) — the same technique
`pact.sty` already uses for everything else.

The payoff is the project's own method applied to its physical form: the
Placing page promises comparison, the notice says a correction was made, and
the body **shows the correction**, so a reader who checks finds the book keeping
its own rules. That is the three-readers principle at the level of the object.

**Caveat, and it is real:** this puts a second hand *inside* the text, and the
fan review found "nobody is in it" to be, on balance, a feature. One strike is
a seam. A dozen is a gimmick and should be refused.

### 2.5 Office stamps — used three times, not 217

`\rotatebox{3.5}{...}` around a double-ruled small-caps box renders as a stamp
impression; verified. Article 21 §(seal) says stamps are cut by Mechanical to a
pattern the Judge keeps, **one for each office**, so the stamps must differ by
*office and wording*, never by ornament:

- `JUDICIAL ARCHIVE · COMPARED` on the Placing page;
- `SET IN BY THE CLERK` on the Clerk's sheet;
- `ENTERED` at the close of the Log.

`\AtBeginShipout` will happily stamp every one of the 217 pages, and it should
not. **An archive copy is stamped where something was done to it, not
everywhere.** Three stamps are an institution; 217 are wallpaper.

A `\stamp{...}` macro in `pact.sty` is about twelve lines. Vary the rotation
per stamp (2.5°, −3°, 4°) so they read as three separate impressions.

### 2.6 The colophon

Final verso. No year — the book's refusal to date itself is load-bearing, and
the Placing page has already explained the refusal by leaving a blank for it:

> Printed by order of the Office of the Mayor and the Department of Judicial,
> from the archive copy, by the printers of Supply. Compared against the
> archive copy and found true. The classes, the roll, and the number of copies
> are kept by the archivist of Judicial under Article 21.

Optionally a classification line in `lmtt` above it — class, roll, shelf —
since Article 21 has the archivist "keep the classes in order."

---

## 3. The way in (frustration #1)

The Table of Contents already lists all 236 Sections, so the problem is not
navigation by number — it is that there is no way to approach the book by
**subject**, and no in-world apparatus at all.

### 3.1 A Table of Subjects, keyed to Articles and Sections

Not page numbers — **Article and Section**. That is how a legal code is cited,
it is how this book cites itself everywhere (`\artref`/`\secref`), it survives
repagination, and it is what a clerk would actually have made. Title it
in-world, and attribute it to the office that would hold it:

> A Table of the Subjects of This Pact, with the Articles and the Sections
> Where They Are Found, Kept by the Archivist of Judicial

Set two-up in `multicol`. Mechanism: a `\pterm{...}` macro writing
`\indexentry{term}{\thechapter.\thesection}` via `makeidx`'s `\index`, and a
~60-line `tools/mkindex.py` that reads `main.idx`, sorts, groups and emits
`main.ind` — necessary anyway, since the `makeindex` binary is absent.

Scope is the honest problem: ~400–600 entries to be genuinely useful. It can
ship in editions — a defensible first pass is just the terms Article 1's
glossary already defines plus every defined term in the `definitionlist`
environments, which is ~120 entries and already an enormous improvement.

**This is the item that most directly answers "there is no way in," and it is
also an artifact.** It does both jobs at once.

### 3.2 A Table of the Amendments and the Sections They Touch

A `longtable` at the head of the Appendix: amendment number | the Article and
Section it alters | its effect in four words | whether it stands. Twenty-one
rows. Cheap, and it is exactly the finding aid a Clerk would keep. It also
makes the Judge's entry on the numbering *land*, because a reader who has the
table in front of them can see which numbers the renumbering moved.

### 3.3 Rename the Table of Contents

One line. `\tableofcontents` currently prints "Contents," which is the one
out-of-world word in the front matter. Make it:

> The Order of the Articles, and of the Sections Within Them

### 3.4 Running heads

`\chaptermark` currently discards the Article's title, so the verso reads
`ARTICLE 18` and the recto `SECTION 3`. Put the title on the verso —
`ARTICLE 18 · OF THE CLEANING` — so a reader flipping can land. One line in
`pact.sty`.

### 3.5 Do **not** put a reader's guide in the PDF

The fan review asked for "if you read five things, read these." It is right
that this is wanted, and wrong that it belongs here. An out-of-world afterword
inside the object destroys the object — it is the one addition that would undo
everything in §2. Put it in `README.md`, or ship it as a separate companion
PDF that is openly a modern editor's note. **The book must not explain
itself.**

---

## 4. Typographic tightening (free, low risk)

- **`\emergencystretch` and `\tolerance`.** No `microtype`, a 4.4in measure and
  a vocabulary full of long words means rivers and the remaining overfull boxes
  (largest 5.57pt). Raising `\emergencystretch` to ~1em and `\tolerance` to
  ~1500 will absorb most of both at no cost in authenticity — real statute books
  are loosely set.
- **`\raggedbottom`.** `book.cls` flushes the bottom of every page by stretching
  the inter-section glue. A code printed by a department does not do this.
  Ragged bottoms read as cheaper, more official printing.
- **Skip `[T1]{fontenc}`.** It errors at load time against `cmr` metrics unless
  `lmodern` is loaded first, and buys essentially nothing for this text.

---

## 5. What needs `sudo` (stated plainly: out of reach as the box stands)

Worth it if you want it; all are one package install on Fedora. Suggest running
these yourself with `! sudo dnf install ...`:

- **`texlive-tex-gyre`** — unlocks TeX Gyre **Schola** (Century Schoolbook) and
  **Pagella** (Palatino). Schola is *the* face for an institutional code and
  would do more for authenticity than anything in §4. This is the only item in
  this document I would call a genuine loss.
- **`texlive-microtype`** — would fix the remaining overfull boxes properly.
- **`texlive-makeindex`** — removes the need for `tools/mkindex.py` (though the
  Python route gives Article/Section keying, which `makeindex` does not, so I
  would write the script regardless).
- **`texlive-pgf` / `texlive-eso-pic`** — drawn seals and full-page overlays.
  See §6 before installing these.

---

## 6. Recommended against

- **Foxing, coffee rings, water stains, torn edges, aged-paper backgrounds.**
  Note that these are *achievable* — `graphicx` + `\AtBeginShipout` will tile a
  texture across all 217 pages without `eso-pic`. This is a choice, not a
  limitation. The reasons to refuse: wear simulated uniformly is the one thing
  that most reliably announces a fake; it fights the restraint principle that
  the whole text is built on; and it moves the book from *document* to *prop
  photograph*. The authentic layer this book wants is bureaucratic, not
  decorative.
- **A handwriting font for the Clerk.** None is installed, and the right
  surrogate is `lmtt` at a narrow measure — which reads as *a different
  machine*, which is both achievable and, for a silo, more plausible.
- **Marginalia from a named character.** It would break "nobody is in it,"
  which the fan review identified as a feature, and would be the first time the
  book admits an individual reader. The Clerk's correction (§2.4) does the same
  work without a person.
- **A stamp on every page.** See §2.5.

---

## 7. Suggested order

| # | Item | Cost | Risk | Value |
|---|---|---|---|---|
| 1 | The Placing Page (§2.1) | one file | none | very high |
| 2 | Clerk's correction notice (§2.3) | one page | none | very high |
| 3 | Amendment 21 as a set-in sheet (§2.2) | file move + `xref.py` path | low | very high |
| 4 | `\stamp` macro, used 3× (§2.5) | ~12 lines | none | high |
| 5 | Table of the Amendments (§3.2) | 21 rows | none | high |
| 6 | TOC rename + running heads (§3.3–3.4) | 2 lines | none | high |
| 7 | `\emergencystretch`, `\raggedbottom` (§4) | 3 lines | none | medium |
| 8 | One hand-correction in the body (§2.4) | macro + 1 edit | medium | high |
| 9 | Colophon (§2.6) | one page | none | medium |
| 10 | Table of Subjects + `tools/mkindex.py` (§3.1) | large | low | very high |

Items 1–7 are an afternoon and change nothing a reader has already read. Item
10 is the real work and is also the one that answers both fan complaints at
once.

Everything must still leave `make` clean and `python3 tools/xref.py` clean,
run from the repo root.

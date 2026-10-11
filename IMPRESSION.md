# The Impression

*A register of every deliberate irregularity in the printing of `book/main.pdf`,
with the page it falls on and the reason it is there.*

**Do not fix anything on this list.** Each entry is a rendered accident of the
press, placed on purpose. If you correct one, strike it from this file in the
same commit and say why; otherwise a later cleanup pass will quietly undo the
whole layer.

This is the printing's counterpart to the project's register of deliberate
textual seams. The seams are things the Pact's *authors* did. The entries below
are things the Pact's *printer* did, and the two date from different days.

---

## Why a copy of the Pact can carry bad presswork but not wear

`\secref{art:records}{sec:records:copying-and-keeping-of-this-pact}` --- Article
21, Section 7 --- has every copy compared against the archive copy once yearly
and replaced within the season if it is found damaged or wanting. Wear therefore
cannot accumulate on a copy that is still in its place: a copy that looks old
has already failed its comparison and been destroyed.

What a copy *can* carry is everything that went wrong in the making, because no
comparison of one printed copy against another would ever catch a letter that
went into the stick upside down. Every copy of that impression has it. The
comparison is for leaves torn out, not for sorts set wrong.

This is why the artifact layer simulates **a printing** and never **wear**: no
foxing, no stains, no coffee rings, no handwriting fonts, no marginalia.

---

## Dosage

Five accidents in two hundred and forty-three pages, in two clusters:

| gathering | printed pages | accidents |
|---|---|---|
| D | 33--48 | three |
| M | 161--176 | two |
| all others | --- | none |

Errors in hand-press books cluster by forme, because a forme was set by one man
on one day and his bad days are not spread evenly through a book. Scattered one
to a gathering they would read as decoration rather than as evidence. A reader
who notices the second turned letter has stopped reading an artifact and started
reading a trick.

---

## The register

Macros are defined in `book/pact.sty` under "Accidents of composition".

| # | printed p. | gathering | file | word | macro | what it is |
|---|---|---|---|---|---|---|
| 1 | 40 | D | `articles/article05.tex` | *chambers* | `\turnedsort{q}{b}` | a turned sort |
| 2 | 46 | D | `articles/article06.tex` | *always* | `\wrongfount{a}` | a sort of the wrong fount |
| 3 | 48 | D | `articles/article06.tex` | *witnesses* | `\highsort{e}` | a sort standing high |
| 4 | 162 | M | `articles/article19.tex` | *unfit* | `\twosorts{f}{i}` | a ligature set as two sorts |
| 5 | 173 | M | `articles/article20.tex` | *raising* | `\lightink{...}` | a word the ball under-inked |

### 1. The turned sort --- printed p. 40, *chambers*

The commonest error in the trade, and here in its quiet form: the compositor's
hand went to the wrong box and came back with a **q**, which he set turned, so
that it prints a passable **b**. The word is spelt correctly; only the letter is
wrong. This is why the four boxes b, d, p and q are kept apart in the case.

An **n** turned to stand for a **u** was tried first and discarded. In this face
the two are indistinguishable when either is turned, so the accident left no
mark at all --- an error nobody can see is not an error. b and q differ in their
serifs and in the weight of the bowl, and the difference survives at reading
size.

`\turnedsort` takes two arguments: the sort that was in the stick, and the
letter it stands for. The second is set in white beneath the first so that the
text layer under the page stays correct and a reader can still search and copy
the word. One side effect: a stray `q` is appended to the end of that page's
extracted text, because the rotated glyph sits in its own content group. Leave
it; the visible page is the artifact.

### 2. The wrong fount --- printed p. 46, *always*

The same letter from a fount of another body: seven-point metal standing in a
ten-point line, cast to a wider and heavier design. The x-heights nearly match,
which is why the eye passes over it once and catches it the second time.

A simple size bump (the same fount set larger) was tried first and was close to
invisible, because scaling one design changes nothing but the size. Changing the
*design* is what makes a wrong-fount sort look wrong.

### 3. The high sort --- printed p. 48, *witnesses*

A sort that did not seat square and took the impression high; the letter rides
above its line. At 0.7pt this was imperceptible. It is now 1.3pt, which reads at
reading size without looking like a superscript.

### 4. The broken ligature --- printed p. 162, *unfit*

A ligature the compositor did not reach for, so he set **f** and **i** as two
sorts with a hair space between. The dot on the i, which the ligature suppresses,
is the tell.

### 5. The under-inked word --- printed p. 173, *raising*

A word the ball did not ink evenly, or that the frisket shaded. Set at 36% grey:
kept deliberately close to the body colour, because lighter than this it stops
reading as thin ink and starts reading as a second colour, deliberately applied.

---

## What is *not* on this list, and is also not an error

These are regular features of the printing, not accidents, and are described in
the colophon:

- **The binder's marks** at the foot of the first four rectos of every
  gathering (B, B2, B3, B4; C, C2, ...), skipping J, U and W as the trade does.
  Required of every printed copy by Article 21, Section 7(f). The preliminaries
  are gathering A and are unsigned; the body opens at B on printed page 1.
- **The pressmen's figures** --- single oldstyle digits at the outer foot of
  eight pages (printed 23, 58, 76, 109, 134, 167, 194, 221), by which a
  pressman's work at a particular forme could be told from another's. The
  colophon says in so many words that they are no part of this Pact.
- **Oldstyle figures** for every folio in the body, in the running heads, in
  the drop folios on Article-opening pages, and in the Table of Articles and
  Sections. Frontmatter folios stay roman and are not touched.
- **The second hand** in Article 14, which abbreviates in its running heads
  (*Art. 14*, *Sect. 3*) and omits the full point after the section number,
  where every other Article spells out. A second compositor set that gathering
  and followed his own habits.
- **The cast-off** in Articles 3 and 10: Article 3 is set close at its end,
  Article 10 opened out at its end, because the compositor measured the copy
  against the sheets he had and guessed wrong in each direction. A bad cast-off
  always shows at the end of a take.

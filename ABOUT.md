# About this project

*If you arrived from a forum post or a link, start here. This is the
one-page version; `README.md` is the long one.*

---

## What it is

**The Pact** — the public legal code of a silo in Hugh Howey's *Wool* /
*Shift* / *Dust*, written out in full.

The books and the show both lean on the Pact constantly. Holston quotes it.
Bernard weaponizes it. It decides who may have a child, who goes outside,
and what happens to anyone who asks. And you never get to read it. So I
tried to find out what writing the whole thing would actually take.

It came out at **23 Articles, 237 Sections, 21 amendments, about 74,400
words**, typeset as a 231-page book.

The PDF is [`book/main.pdf`](book/main.pdf).

## How it was made

**The prose was written entirely by AI. I wrote the rules it had to obey,
not the sentences.** I want that stated plainly and up front rather than
discovered later.

The rules are the actual work, and they are all in this repository:

- `CANON.md` — what the books and the show establish, with each fact marked
  by how well sourced it is, so invention never quietly overwrites canon.
- `STYLE.md` — the register, and the hard prohibitions. No modern
  administrative vocabulary. No units the silo doesn't have. **There is no
  daylight**, so nothing may be described by it.
- `FACTS.md` — a running ledger of consequences. Every clause added raises
  the question of what else must now be true, and the answer gets written
  down before the next clause.
- `HYPOTHESES.md` — for each canon fact, a guess at *why* the Pact's authors
  would have wanted it that way, used to generate the clauses canon doesn't
  show.
- `tools/xref.py` — checks the things LaTeX can't: that all **1,256**
  internal cross-references resolve, that no clause cites a bare "Article
  N" instead of naming its subject, and that no span is measured in a unit
  Article 1 never defined.

Two constraints did more shaping than anything else. The first: the Pact
must **never** disclose anything from the Order — the classified companion
document, which in canon holds the suppressed history and the cleaning-suit
sabotage. Where the public law has to gesture at IT holding some further
authority, it gestures and says nothing. The second: the Pact's authors were
competent and dishonest, so most of the document had to be genuinely boring
administrative law, because that is the only thing that makes the handful of
deliberately planted seams land at all. A few clauses are load-bearing for a
close reader. Most are about rosters.

## What it isn't

- **Not canon, not official, not authorized.** No connection to Hugh Howey,
  Apple, AMC, or anyone else holding rights in the Silo series. It's one
  reader's attempt at a document someone else invented.
- **Not for sale, ever.** Free, non-commercial, and licensed CC BY-NC-SA
  4.0 on the original material only. See `LICENSE`.
- **Not a reproduction of anything Howey wrote.** It's new prose built to
  fit around his, and where canon is silent it invents rather than guesses
  at a text that doesn't exist.
- **Not a transcription of the show's prop.** The Apple TV+ production made
  a physical Pact book, about twenty pages of it written with Howey's
  input, and fans have transcribed it from screenshots. It was useful
  evidence about register and about what topics the Pact covers, and
  `CANON.md` records what was learned from it — but this repository does
  not reproduce it, and the verbatim transcription that was once in
  `CANON.md` has been removed. That text is production design belonging to
  the show, not to this project.
- **Not finished.** The copy still has no Table of Subjects — the in-world
  index that would let a citizen, or a reader, actually find a clause in 231
  pages. That's the next job, and it's the fair criticism the project hasn't
  yet answered.

## One more thing

The project also declines the show's invented age-eleven rite for girls.
It's TV-only, it's load-bearing lore rather than background texture, and it
isn't used anywhere here.

## If you want to talk about it

Questions about the method are very welcome — it's the part I find
interesting, and it's the part I actually did. If AI-written prose isn't
something you want to read, that's a completely reasonable position and I'd
rather you knew before you clicked than after.

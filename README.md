**This was written completely by AI with methodological guidance and rules from me (a human).**

The full text is the `main.pdf` file in the "book/" directory.

# The Pact

An original, full-length recreation of **the Pact** — the in-universe public
legal code of a silo in Hugh Howey's *Wool* / Silo series — written to be
internally consistent with the *Wool*, *Shift*, and *Dust* books.

This is not a reproduction of any published Howey text. It's new prose,
written to plausibly be "the document Holston, Jahns, Bernard, and Juliette
would have on their shelves," respecting what canon establishes and
inventing only what canon leaves open.

## Scope, as agreed with the user

- **Setting**: the silo's "current era" — roughly 140 years after the
  founding/sealing event, i.e. the same rough timeframe as the main *Wool*
  narrative (Holston/Jahns/Juliette), not the earlier Shift-era founding
  itself.
- **Content boundary**: this is the *public* Pact only — the law every
  citizen is taught and can read. It explicitly excludes **the Order**, the
  separate classified document known only to IT (and read into by the
  Mayor in extremis), which in canon holds the suppressed true history,
  the cleaning-suit sabotage protocol, inter-silo secrets, and doomsday
  contingencies. Where the Pact needs to gesture at IT holding some further
  secret authority (e.g. Bernard's succession claim), it does so without
  ever stating Order content.
- **Length/density**: "full annotated volume," target **60,000+ words** —
  not a lean charter, but a document with the heft of a real legal/civic
  code: numbered Articles, Sections, and lettered clauses, plus front/back
  matter.
- **Front/back matter**: an in-world Preamble (framed as citizens would
  actually encounter it — no Order-level secrets), a Table of Contents
  styled as a legal index, and a back-matter **Amendment Log** (fictional
  ratified amendments over the silo's ~140-year history, for texture).
- **Format**: a LaTeX book, built to PDF. Formal statute/constitution
  typesetting — sober, minimal ornament, Arabic-numbered Articles, numbered
  Sections, lettered clauses — rather than an "aged prop book" look.

## Canon research caveat

WebSearch was unavailable during initial research (a backend tool error,
unrelated to content — it referenced an unrelated/unavailable model). All
canon details used so far (the Pact vs. the Order, silo geography, the
succession clause Bernard invokes, the lottery, shadowing/testing, chits,
porters, cleaning, etc.) come from the assistant's trained knowledge of the
books, **not verified against a live source**. If precise fidelity to
specific book passages matters, those should be checked against the actual
text (or pasted in by the user) before or during drafting, particularly for
any detail presented as a hard canon fact rather than an invented filler.

## Repository layout

```
book/
  main.tex              # assembles the whole document
  pact.sty              # all formatting (hand-rolled, see below)
  frontmatter/
    titlepage.tex        # done
    preamble.tex          # done — in-world "why this exists" preamble
  articles/
    article01.tex .. article23.tex   # one file per Article; 1, 2, 6–11, 15–17 written,
                                      # rest are compile-only stubs (see below)
  backmatter/
    amendments.tex         # compile-only stub, not yet written
  Makefile                 # `make` builds main.pdf via latexmk
src/pact/                # pre-existing empty Python package scaffold (uv project),
                         # unrelated to the book so far — not used yet
```

### Why the formatting is hand-rolled

This machine's TeXLive install is missing several packages that would
normally be reached for in a document like this: `geometry`, `titlesec`,
`enumitem`, `fancyhdr`, `xcolor`, `microtype`. Installing them needs `sudo`,
which wasn't available non-interactively. Rather than block on that,
`pact.sty` reimplements everything needed using only what's confirmed
present (`book` class, `hyperref`, `mathpazo`, `calc`, `longtable`,
`multicol`):

- Page geometry set by hand via `\textwidth`/`\textheight`/margins (6x9in
  trade-book trim size, twoside).
- Articles = LaTeX `\chapter`s, renamed and Arabic-numbered
  ("Article 9"), matching the numbering convention seen in the Apple TV+
  show's "Pact" prop text.
- Sections get a "Section N." prefix via `\@seccntformat`.
- Clause lists `(a)`, `(b)`, ... and nested `(i)`, `(ii)`, ... via plain
  `enumerate` with redefined counters/labels, in `clauses`/`subclauses`
  environments — no `enumitem`.
- Running headers via the built-in `headings` pagestyle — no `fancyhdr`.

If more TeX packages become available later (e.g. the user runs the `sudo
dnf install` for them), this can be revisited for nicer typography, but
nothing currently depends on that.

## Current state (as of this writing)

**Done:**

- Directory/build scaffold (`main.tex`, `pact.sty`, `Makefile`) —
  **verified working**, `make` produces `main.pdf` (75 pages) with exit
  code 0. See "Toolchain notes" below for two fixes that were needed.
- Title page.
- Preamble (full text).
- Article 1, "Of the Founding and Purpose of the Silo," written in full as
  a style proof-of-concept (sanitized founding history, supremacy of the
  Pact, silo geography, the wallscreen/sensors, citizenship binding).
- Article 9, "Of the Department of Mechanical," written in full (2026-09-01,
  drafted first per the Drafting Order principle — see `FACTS.md`):
  the Department's charge, the generator/water-air/reclamation triad,
  the freight lift (resolving a `FACTS.md` open item), the digging
  prohibition's order-and-record procedure, tool licensing, and
  shadowing into Mechanical's trades. Updated later (2026-09-02) to remove
  ore-winning (now Article 10's exclusive charge) and keep only power,
  circulation, reclamation, and structural work.
- Article 2, "Of Citizenship and the Census," written in full (2026-09-01,
  Tier 1 per the Drafting Order principle — see `FACTS.md`): the standing
  of a citizen and majority (sixteenth naming-day), the naming of
  children, the citizen's oath, the keeping of the rolls (the census
  itself, including the occupant card), and death and the closing of a
  name. Also where the Structural Fragility guiding principle was
  actually designed and written for the first time — see `FACTS.md`.
  Updated later (2026-09-02): a death suspected to be self-inflicted,
  and not sought under Article 17, now requires a Judicial finding
  rather than a physician's attestation alone (TV-sourced).
- Article 3, "Of Marriage, the Lottery, and the Right of Birth," written in full
  (2026-09-02, Tier 3): marriage as a household partnership (contracted before
  Judicial, can be dissolved by mutual petition or death), the lottery for
  children (population control mechanism held annually, winners granted a
  conception window of 3 seasons to 1 year), unsanctioned children (still citizens
  but responsible adults answerable under Article 16), lottery administration
  (public drawing in Assembly, transparent process, slots set by Mayor based on
  silo capacity from census), and the principle that no citizen is permanently
  barred from petitioning. The lottery is the core mechanism by which the silo
  balances population sustainability with citizens' right to bear children.
- Article 4, "Of the Office of Mayor," written in full (2026-09-02, Tier 2 per
  the Drafting Order principle — see `FACTS.md`): the Mayor as civilian head of
  the silo, powers of confirmation (Department heads, Judge, Sheriff appointment),
  standing orders and resource direction, co-equal relationship with Judicial,
  Assembly accountability, and the Deputy Mayor's office (with forward-reference
  to Article 5's succession mechanism and its Structural Fragility site). A
  load-bearing Article for Article 5's design.
- Article 5, "Of the Deputy Mayor and the Order of Succession," written in full
  (2026-09-02, Tier 2, **PRIMARY STRUCTURAL FRAGILITY SITE** — see `FACTS.md` and
  project memory): the Deputy Mayor's office and powers, temporary succession upon
  Mayor's death/removal, and the **election mechanism for permanent succession**
  (Structural Fragility embedded: Pact requires an election but doesn't specify
  who convenes Assembly, by when, or what forces it to happen — leaving room for
  IT to control timing/information flow). Deputy cannot make permanent appointments
  while acting. Department heads assist in determining election timing. The crack
  hides behind procedural reasonableness.
- Article 8, "Of the Department of Information Technology," written in
  full (2026-09-02): IT's charge, the dangerous-instrument licensing
  monopoly (fulfilling Article 9's forward reference), the radio/wire
  communications monopoly, reinforcement of the sensor/wallscreen and
  cleaning-death gestures from Articles 1 and 2, technological-relic
  examination, and IT's own more insular succession — see `FACTS.md`.
- Article 6, "Of Judicial and the Courts," written in full (2026-09-02,
  **completing Tier 1**): the Judge's office and extra-legitimate
  confirmation, rulings where the Pact is silent, the Officers of
  Judicial (distinct from the Sheriff), and — most importantly — the
  canonical "hollow due process" master clause (swift sentence for the
  gravest offenses, toothless after-the-fact family representations,
  but a real pre-sentence hearing for lesser offenses), and the Judicial
  archive's tamper-evident record-keeping. Updated later the same day
  with a TV-sourced limitation on relic-searches of the Sheriff's own
  station (extreme cause plus advance notice required). See `FACTS.md`.
- Article 10, "Of the Department of Mines," written in full (2026-09-02,
  at the user's explicit directive to resolve `FACTS.md` open item 3 —
  see `CANON.md` §18): a distinct Department from Mechanical, with its own
  Head of Mines (Mayor-appointed, shadowed within the Department per
  Article 13), the charge of ore-winning as a standing necessity, the
  200-foot radius limit (TV-sourced, `CANON.md` §18, `HYPOTHESES.md` entry 5),
  Judicial handling of mining-beyond-limit as a gravest offense, and
  coordination with Mechanical for structural concerns (both occupy Down Deep).
  Resolves the structural change from 22-Article to 23-Article outline;
  all Articles 10–22 renumbered to 11–23. See `FACTS.md`.
- Article 11, "Of Supply, Hydroponics, and the Ration," written in full
  (2026-09-02, drafted out of recommended order to use fresh research —
  originally Article 10, renumbered after Mines insertion — see `CANON.md` §18):
  Supply's charge, hydroponics and livestock, the ration (calculated from
  Article 2's census count, with an equality-guarantee clause worth watching
  for later Amendment Log tension), water/air stores fulfilling Article 9's
  promise, and sanctioned pets (formalizing "sanction" as licensing vocabulary
  and grounding Bernard's "sanctioned pet" joke in real statute). See `FACTS.md`.
- Article 16, "Of Crimes and Their Punishments," written in full
  (2026-09-02): the canonical **three-tier punishment scale** (grace →
  the mines → cleaning, filling in the previously-missing mines tier
  from `CANON.md` §18), consolidating every "answerable under Article
  16" / "among the gravest offenses" forward-reference made by Articles
  1, 2, 9, and 10 into one place, plus a general interpersonal-crime
  catch-all. Creates firm new promises for Article 15 (must define a
  relic classification system with a "gravest" tier) and stays
  consistent with Article 9's absolute digging prohibition by framing
  the mines as pre-existing workings, not new excavation. Updated later
  (2026-09-02): an unsanctioned self-killing is now named among the
  gravest offenses, with the completed-death-cannot-be-sentenced problem
  addressed directly (TV-sourced). See `FACTS.md`.
- Article 12, "Of Trade, Chits, and Commerce," written in full (2026-09-02, Tier 3):
  chits as the silo's internal currency (earned through labor, non-rationed goods
  trading), the marketplace (where citizens buy/sell goods and skilled services
  beyond the ration), the Chit-Keepers (maintaining accounts, verifying
  authenticity, preventing counterfeiting), price regulation (no price-fixing,
  but Mayor can intervene for unjust/extortionate prices or essential goods),
  debt and credit (loans tracked by Chit-Keepers, enforceable by Judicial, no
  debt slavery), and marketplace protection (Sheriff patrols for fraud/theft,
  fraud as answerable under Article 16). The mechanism by which the silo's economy
  operates outside the guaranteed ration.
- Article 13, "Of Labor, Shadowing, and the Assignment," written in full
  (2026-09-02, comprehensive Tier 3 article incorporating PROFESSIONS.md
  reference): the charge of labor and the principle that citizens choose
  within the silo's constraints, testing of aptitude (childhood through
  majority), the three tiers of shadowing (Full/Short/None) by trade
  complexity, mundane labor (no training), skilled trades (Full shadowing
  required), critical roles (Full shadowing + additional vetting for
  Order-adjacent work), labor supply management (how the silo ensures
  adequate staffing in critical roles), reassignment and retirement
  mechanisms, and the rights and duties of the shadowed. Establishes the
  coherent framework for how citizens are matched to work and how the
  silo balances individual choice with collective need.
- Article 15, "Of Public Order and Forbidden Speech," written in full
  (2026-09-02): the core outside-taboo (precisely scoped so the citizen's
  own final request under Article 17 is *not* an offense), an
  overhear-and-not-report liability, Section 3 fulfilling Article 1's
  fixed "false teaching of the founding" promise (with a quiet, unstated
  echo of the Order-level teacher/reset backstory), the relic
  classification system (gravest tier + sanctionable lesser relics,
  fulfilling Article 16's dependency), and the restricted-instruments
  prohibition (defaulting to gravest classification). Also settles the
  "sanctioned" vs. "licensed" terminology question as project
  convention. See `FACTS.md`.
- Article 7, "Of the Sheriff and the Keeping of the Peace," written in
  full (2026-09-02, at the user's specific request to cover public order
  on the stairs and other special areas): stairwell traffic conventions
  (outer rail ascending, inner rail descending) and right-of-way
  priority (porters and urgent word first), stairwell violence
  explicitly weighted by fall-risk, common-area order-keeping (with the
  freight lift/Department offices explicitly *not* common areas —
  trespass otherwise), cleaning-viewing at the cafeteria wallscreen as
  neither compulsory nor forbidden, and the Sheriff/Judicial
  dispute-resolution boundary reinforced. **Corrected 2026-09-02**: the
  Sheriff's succession was originally drafted with the generic
  shadow-then-Mayor-confirm template, contradicting `CANON.md`'s own
  already-recorded note that the Sheriff is Mayor-appointed (Juliette's
  outside appointment over Deputy Marnes being the clearest evidence) —
  fixed to a Mayoral appointment weighing, but not bound by, the
  outgoing Sheriff's recommendation; Deputies remain shadowed, the
  Sheriff's own office does not. See `FACTS.md`.

**Not yet written:** Articles 14, 18–23, and the back-matter
Amendment Log — currently populated with minimal stub files
(`\chapter{title}` only)
so `main.tex`'s `\input`s all resolve and the build compiles end-to-end;
see `FACTS.md`'s "Drafting order and priorities" for which to write next
and why. (Articles 1–7, 8–13, 15–17 are now complete.)

**Original pause, now resolved:** the user stopped further drafting after
Article 1 to do preparatory work first — before more prose gets written,
agree on the full Article-by-Article outline and/or a canon fact-sheet, so
later Articles don't have to be revised for consistency. That preparatory
work is done: `CANON.md` holds the canon fact-sheet, `STYLE.md` holds a
distilled drafting style guide, `FACTS.md` tracks facts asserted inside
the Pact itself for coherence across Articles, `HYPOTHESES.md` tracks
generative "why" reasoning from canon facts, `PROFESSIONS.md` is a
brainstorming inventory of trades/offices by Department (not yet
drafted content — support for Article 13 and beyond), and the
originally-22-Article outline was revised to 23 Articles via explicit user
directive (2026-09-02): Mining was spun out as its own Article 10, requiring
all later Articles (10–22) to renumber to (11–23). Drafting is actively underway,
not in numerical order — see "Guiding principles" and `FACTS.md`'s
"Drafting order and priorities" for the current sequence and status.
One `FACTS.md` open item remains (the founding-timeline question),
deliberately deferred until it
actually blocks something — the Amendment Log especially — per the
user's instruction.

## Guiding principles: coherence, consilience, "why," and the Founders

Several related high-priority desiderata of this project:

1. **Coherence/consilience**: every fact the Pact asserts or implies
   should have its downstream consequences thought through, and every
   rule should have a worked-out in-world explanation, even where that
   explanation never appears in the Pact's own text. `FACTS.md` is the
   living ledger for this — check it before drafting any Article, and
   add to it after. Two open coherence questions are currently blocking
   full confidence in Article 1 and should be resolved before Articles
   9, 20, or the back-matter Amendment Log are drafted; see `FACTS.md`
   for both.
2. **The "why" heuristic**: for facts established about the world of
   Wool itself (`CANON.md`), ask why they're true, form a reasonable
   hypothesis, and use that hypothesis to generate more Pact content
   consistent with the same underlying logic — not just restate the one
   fact in isolation. `HYPOTHESES.md` tracks these (e.g., the
   magnification ban implying a broader "restrict dangerous technical
   knowledge" category that should also shape Articles 8, 9, 14, 15, 16).
3. **The Founders' psychology**: the Pact's in-world authors value
   consistency and plausibility, deceive citizens whenever they judge it
   useful, are strict exceptionless utilitarians, and are always
   internally logical in their true motives, however cold. Every
   rationale we work out should therefore be split into a **true
   rationale** (the Founders' actual, pragmatic calculation) and a
   **stated rationale** (the plausible, possibly misleading, thing
   citizens are actually told) — see `STYLE.md`. The Pact's actual
   in-world author is **Victor**, the psychologist among the three
   founding architects (book-confirmed) — see `CANON.md` section 17a and
   `STYLE.md` for what that implies about the Pact's priorities and
   occasional tonal uncanniness. **Anna Thurman** is a secondary
   co-author (show-confirmed) — see `CANON.md` section 17b and `STYLE.md`
   for her blended, warmer-but-still-complicit authorial voice.
4. **Meta-principle**: the same discipline applies recursively to this
   project's own guidelines — occasionally ask *why* a guideline was set
   for this project, and if a good answer emerges, look for further
   principles that cohere with it. See `STYLE.md`, "the guidelines have
   their own 'why,'" including a worked example that generated a new
   principle (deliberately placed, close-reading-rewarding "seams").
5. **Restraint**: most of the Pact should be genuinely mundane
   administrative law with no hidden agenda at all — a corrective to
   (4), since rarity is what makes a planted seam or psychological tell
   actually land instead of blurring into "everything secretly means
   something." See `STYLE.md`.
6. **Write for three readers**: every passage should hold up for the
   ordinary citizen (face value), the in-world close/suspicious reader
   (Allison/Juliette mold — occasionally, rarely rewarded), and the
   actual reader of this book (who can be given more, via dramatic
   irony, without anything being stated in-world). See `STYLE.md`.
7. **Structural fragility**: however psychologically astute Victor's
   design is, it should carry a genuine structural blind spot, not just
   discoverable "seams" — consistent with the fact that this system of
   control doesn't hold, repeatedly, across the wider saga. See
   `STYLE.md`.
8. **Amendment Log authorial drift**: the back-matter Amendment Log
   spans the silo's whole subsequent history and should *not* sound like
   Victor and Anna wrote it too — later amendments should show their
   tricks applied more clumsily by lesser hands, which also gives a
   lever on `FACTS.md`'s open founding-timeline question. See `STYLE.md`.

Together: `CANON.md` (research) → `HYPOTHESES.md` (why, split into true
vs. stated rationale, and what that implies) → drafted Article text →
`FACTS.md` (locked-in internal facts, checked against everything after).

### Ratified 23-Article outline

Originally ratified by the user on 2026-09-01 as a 22-Article outline,
cross-checked against `CANON.md`. **Revised 2026-09-02**: at the user's
explicit directive ("Make Mining its own department"), the outline was
expanded to 23 Articles via insertion of a new Article 10 (Of the Department
of Mines), with all former Articles 10–22 renumbered to 11–23.

Articles are numbered with **Arabic numerals** ("Article 9," not "Article
IX"), matching the numbering convention seen in the Apple TV+ show's
"Pact" prop text (see `CANON.md` section 17) — updated from an earlier
Roman-numeral draft for canon consistency. Article 3's title was
broadened from "Of the Lottery and the Right of Birth" to "Of Marriage,
the Lottery, and the Right of Birth" (2026-09-01, after a full review
against the guiding principles below) to give Anna Thurman's authorial
territory — marriage and kinship — an explicit home; see `FACTS.md`.

1. Of the Founding and Purpose of the Silo — *written*
2. Of Citizenship and the Census — *written*
3. Of Marriage, the Lottery, and the Right of Birth
4. Of the Office of Mayor
5. Of the Deputy Mayor and the Order of Succession
6. Of Judicial and the Courts — *written*
7. Of the Sheriff and the Keeping of the Peace — *written*
8. Of the Department of Information Technology — *written*
9. Of the Department of Mechanical — *written*
10. Of the Department of Mines — *written* (inserted 2026-09-02, resolves `FACTS.md` open item 3)
11. Of Supply, Hydroponics, and the Ration — *written* (renumbered from original Article 10)
12. Of Trade, Chits, and Commerce (renumbered from original Article 11)
13. Of Labor, Shadowing, and the Assignment (renumbered from original Article 12)
14. Of Housing and the Floors (renumbered from original Article 13)
15. Of Public Order and Forbidden Speech — *written* (renumbered from original Article 14)
16. Of Crimes and Their Punishments — *written* (renumbered from original Article 15)
17. Of the Cleaning — *written* (renumbered from original Article 16)
18. Of Health, the Infirmary, and the Mind (renumbered from original Article 17)
19. Of Assembly and the Common Halls (renumbered from original Article 18)
20. Of Records, Porters, and the Post (renumbered from original Article 19)
21. Of Emergency and the Suspension of Ordinary Law (renumbered from original Article 20)
22. Of Amendment and the Continuance of the Pact (renumbered from original Article 21)
23. [Amendments] (renumbered from original Article 22)

This is now the locked structure for drafting Articles 2–23. See
`CANON.md` for the canon research backing each Article. **Drafting order
does not need to follow numerical order** — Articles with far-reaching
consequences for the rest of the Pact should be drafted first, to avoid
rework. See `FACTS.md`, "Drafting order and priorities," for the current
recommended sequence (Tier 1 — Articles 9, 2, 8, 6 — is now **complete**;
Articles 10 (Mines) and 11 (Supply, formerly 10) were drafted next, fulfilling
`FACTS.md` open item 3 and fresh research — see `CANON.md` §18. Articles 16,
15, and 7 are now done too. Remaining Tier 2: Article 4, then 5).

## Toolchain notes

- `pdflatex`, `xelatex`, and `latexmk` are installed; `tlmgr` exists but
  this is an RPM-managed TeXLive (Fedora), so `tlmgr` package installs may
  not behave like a normal user-mode TeXLive install.
- `make` (from `book/`) runs `latexmk -pdf -interaction=nonstopmode
  -halt-on-error main.tex`. **Verified working (2026-09-01)**: `make`
  exits 0 and produces `main.pdf`. Two fixes were needed to get there —
  both already applied in `pact.sty`, noted here so they aren't
  accidentally reverted:
  1. **Font**: `mathpazo` (Palatino) loads as a package but this
     TeXLive install doesn't have the actual URW Palladio Type1/TFM font
     files, and Metafont (`mf`) isn't installed to generate substitutes
     — pdflatex failed with "Font ... not loadable" and produced no PDF
     at all. Swapped to `lmodern`, which has its font files actually
     present and builds cleanly. Revisit if the missing font packages
     are ever installed via `sudo`.
  2. **Running headers**: `book.cls`'s default `headings` page style
     repeats the full chapter/section title in the header, which
     overflowed `\textwidth` (overfull `\hbox` warnings) for our
     longer Article/Section titles. Overrode `\chaptermark`/
     `\sectionmark` in `pact.sty` to show just "ARTICLE N" / "SECTION N"
     — shorter, guaranteed to fit, and consistent with the sober/
     minimal-ornament design goal.
- Articles 3–5, 12–14, 18–23 and `backmatter/amendments.tex` are currently
  minimal stub files (`\chapter{title}` + `\label{}`, no body) purely so
  `main.tex`'s `\input`s all resolve and the full build can be tested
  end-to-end. They'll be replaced with real content per `FACTS.md`'s
  drafting order — don't mistake a stub existing for an Article being
  written.
- Nothing has been committed to git yet; all of the above is untracked
  working-tree content.

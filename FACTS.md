# Facts ledger — coherence & consilience tracking

**Purpose**: it is a guiding principle of this project that the Pact be
highly coherent and consilient — every fact it asserts or implies should
have its downstream consequences worked out, and every rule should have a
worked-out *explanation* (even if that explanation never appears in the
Pact's own text), so that later Articles never quietly contradict earlier
ones. This file is the running ledger that makes that checkable rather
than just aspirational.

## How to use this file

- **Before drafting a new Article**, skim the facts already logged here
  for anything the new Article touches (geography, timeline, named
  offices/departments, technology limits, population mechanics).
- **After drafting a new Article**, add an entry for every fact it
  asserts or clearly implies that could constrain later Articles —
  numbers, named rules, named offices, causal claims ("X because Y").
  For each: note *why* it's true in-world (even briefly), and what it
  rules out or requires elsewhere.
- **Open items** (⚠) are unresolved tensions that need a decision before
  they can be treated as locked. Don't draft an Article that depends on
  an open item without either resolving it first or explicitly flagging
  the dependency.
- Cross-reference `CANON.md` (external canon), `STYLE.md` (register and
  the Founders' psychology principles), and `HYPOTHESES.md` (the "why"
  behind canon facts) as needed — this file is specifically about facts
  *internal to this project's own Pact*, which may extend canon but must
  never contradict confirmed canon (per the project's Order-exclusion
  and TV-sourcing rules).
- Where a fact's "explanation" would plausibly differ depending on
  whether it's the Founders' true (utilitarian) reasoning or what
  citizens are actually told, note both — see `STYLE.md`'s "Founders'
  psychology" section. Article 1 already does this well without the
  terminology: e.g. the sensor-maintenance passage ("such further
  procedure as that Department alone is instructed in") withholds the
  true reason and offers only a plausible gesture in its place.

## Open items (need a decision before Articles depending on them are drafted)

### ✅ 1. Founding timeline — RESOLVED (2026-09-03), extended to full date/founder ambiguity (2026-09-03)

- **The issue**: Article 1 originally stated "one hundred and forty years
  have passed since the sealing of this silo," which was anachronistic —
  the Pact is a founding document written *before* the silo's sealing and
  habitation, so it cannot reference historical time that hasn't occurred yet.

- **First resolution**: The Pact is timeless in its original form. Article 1 §1
  was revised to remove the temporal reference, reframing it as an
  **inaugural founding document** meant to govern "so long as the silo
  stands and citizens dwell within it," not as a historical account.

- **Extended resolution (user decision, 2026-09-03)**: the user asked that
  the whole text be made ambiguous as to what year it is, how long ago the
  Pact was written, and in what years it was amended — and that the early
  text's implication that the founders lived in the silo also be made
  ambiguous. This **supersedes** the first resolution's "Amendment Log
  dates are valid and meaningful" consequence, which no longer holds — the
  Amendment Log now carries no years at all. Implemented as:
  - `book/backmatter/amendments.tex`: every "(Year N)" heading and "ratified
    in the Nth year since the sealing" subtitle was removed and replaced
    with relative, qualitative phrasing ("ratified in the silo's early
    years," "ratified a generation after Amendment 1," "ratified later
    still," etc.), justified by a new intro line stating that the Pact does
    not itself reckon a calendar from the founding, and the Log follows
    that same practice — an amendment's place is fixed by order, not year.
  - `book/frontmatter/preamble.tex`: removed the clause claiming the Pact's
    authors raised their children "under the same roof they ask you to
    keep" (i.e., inside the silo), leaving it ambiguous whether the
    founders ever lived in the silos themselves, while preserving the
    surrounding claim that they were people who buried their dead and
    suffered hard years.
  - Verified by full-text search across the whole book: no other Article
    contains a historical-time or founder-residency claim needing the same
    treatment.

- **Effect on other Articles**: None beyond the two files above. No Article
  depends on a specific amendment year or founding date; the Amendment
  Log's internal ordering (Amendment 1 through 8) is unaffected — only the
  year labels are gone.

### ✅ 2. Freight lift vs. the Pact's mechanized-transport ban — RESOLVED (Article 9 drafted)

- **The tension**: canon (the show's own numbered Pact rule, per
  screenrant reporting) bans "mechanized forms of transportation... 
  elevators and pulleys" between levels — explicitly framed as
  reinforcing the silo's floor-based class structure. Article 1 already
  states the stairwell is the only common passage "save the freight
  lift reserved to Supply and Mechanical under Article 9."
- **Resolution as drafted** (Article 9, Section 3, "The Freight Lift"):
  the lift carries goods only — no citizen may ride it or be granted
  passage save a Mechanical/Supply worker directly loading, unloading,
  or repairing it; every use is logged (goods, ordering citizen, floors)
  under Article 21 (Records); its speed/power draw is capped by the Head
  of Mechanical against the generator's other demands; and a direct clause
  forwards the *general* passenger-conveyance ban to Article 16 ("The
  making of any device to carry a citizen's own body between floors...
  is forbidden under Article 16" — Public Order). This preserves both
  facts as planned.
- **Promise fulfilled**: Article 16 (Public Order) contains this
  passenger-conveyance prohibition, and Article 21 (Records, Porters, and
  the Post) is consistent with the freight lift's logging requirement and
  its cargo-only nature — porters still carry messages/small goods on foot
  precisely because the lift can't move people or be used informally.
- See `HYPOTHESES.md` entry 2 for the deeper "why" behind the ban itself
  (social control + engineering-knowledge containment + resource
  conservation), which this resolution is built on.

### ✅ 3. Mines as a subordinate charge of Mechanical vs. a distinct Department — RESOLVED (Article 10 drafted, 2026-09-02)

- **The tension** (archived): canon (`CANON.md` §18) treats the Mines as a genuinely
  separate department in its own right, with its own **Head of Mines**
  (a distinct office from the Head of Mechanical). Our original 22-Article
  outline had no separate Article for Mining — Article 9 described
  ore-winning as a standing charge of Mechanical, not a separate department,
  and Article 16 framed the mines as penal labor "under the direction of the
  Head of Mechanical." This was a simplification made before the
  Head-of-Mines research arrived.
- **Resolution as drafted**: User explicitly chose option (3) — "Make Mining
  its own department" — requiring a 23rd Article. Implemented via:
  - **Structural change**: shifted the entire 10–22 Article numbering to
    11–23 (via descending sed + file rename to avoid collision); inserted
    new Article 10 ("Of the Department of Mines") at the new position.
  - **Article 10 (Mines)**: now defines ore-extraction as Mines' core charge
    (not Mechanical's), establishes the Head of Mines as a distinct office
    (appointed by Mayor, shadowed within the Department per Article 13), and
    codifies the 200-foot radius limit (TV-sourced, `CANON.md` §18, `HYPOTHESES.md`
    entry 5).
  - **Article 9 (Mechanical)**: removed the ore-winning line from Section 1's
    charge description and Section 4's digging-exception clause; Mechanical now
    controls only power, circulation, reclamation, and structural work. Ore
    processing (delivery from the mines to metal-working) remains a Mechanical
    function, but ore *extraction* is now explicitly Mines' responsibility.
  - **Article 17 (Crimes)**: already drafted, uses "Head of Mechanical" language
    for mines-tier penal labor, but Article 17's facts table clarifies the mines
    are "pre-existing workings," not new digging — remains consistent with the
    Mining article's framing as ore extraction from builders' workings, not
    against the Article 9 absolute-digging prohibition.
- **Cross-references verified**: Article 1 (Section 3) now names "the workings
  of Mines" alongside Mechanical, generator, water treatment in the Down Deep
  enumeration; all forward/backward references checked against new numbering.
- **LaTeX build verified**: project builds cleanly to 79 pages with Article 10
  now included and all renumbered articles (11–23) resolving without errors.

## Drafting order and priorities

**Principle (agreed with the user, 2026-09-01)**: Articles don't need to
be drafted in numerical order. An Article that's likely to have
far-reaching consequences for other parts of the Pact — because other
Articles will reference it, depend on a decision it makes, or inherit a
mechanism it establishes — should be drafted before Articles that mostly
just consume what's already settled. This reduces rework: draft the
load-bearing Articles while the whole picture is still open, not after
downstream Articles have already been written around a guess.

**Recommended order**, based on a review of how densely each Article is
already referenced/depended-on across `CANON.md`, `HYPOTHESES.md`,
`FACTS.md`, and `STYLE.md` (Article 1 excluded — already written):

- **Tier 1 — highest cross-Article consequence, draft first:**
  - **Article 9 (Mechanical) — ✅ drafted, 2026-09-01, updated 2026-09-02.** Was by far the most cross-referenced Article
    in this project's notes. Resolves the open freight-lift item (#2
    above), defines the licensing exception for Mechanical's own
    precision tools (`HYPOTHESES.md` entry 1), and sets the generator's
    power/resource constraints other Articles lean on. Also has charge
    of **recycling**, alongside power (Energy) and water treatment
    (Circulatory) — these three are grouped as a single category in the
    show's own transcribed Pact text (`CANON.md` section 17), which is
    also literally the precedent clause `STYLE.md` uses as the model for
    "hollow due process." Final six-section structure: (1) The
    Charge of Mechanical (power, circulation, reclamation, structural work — ore-winning moved to Article 10), (2) Power, Circulation, and Reclamation
    (generator + water treatment + recycling, unified per the show's own
    triad), (3) The Freight Lift, (4) Structural Work and the
    Prohibition Against Digging, (5) Tools, Materials, and Their
    Licensing, (6) The Trades of the Down Deep.
  - **Article 2 (Citizenship and the Census) — ✅ drafted, 2026-09-01.** Definitionally prior to
    almost everything ("citizen" is the subject of nearly every other
    rule); also a Structural Fragility site (see below).
  - **Article 8 (Information Technology) — ✅ drafted, 2026-09-02.** Establishes IT's licensing
    monopoly over "dangerous knowledge" (`HYPOTHESES.md` entry 1) and its
    institutional authority, both leaned on by Articles 9, 14, 15, 16,
    17, 20, 21.
  - **Article 6 (Judicial and the Courts) — ✅ drafted, 2026-09-02, Tier 1 complete.** Establishes the "hollow due
    process" template (`STYLE.md`) that Articles 7, 16, 17, and 21 all
    reuse; better to define it once, well, than let each Article
    reinvent a slightly different version.
- **Tier 1 complete as of 2026-09-02** (Articles 9, 2, 8, 6 all drafted).
  Recommend moving to Tier 2 next.
- **Tier 2 — significant, but downstream of Tier 1:**
  - **Article 17 (Crimes and Their Punishments) — ✅ drafted, 2026-09-02.** And **Article 16
    (Public Order and Forbidden Speech) — ✅ drafted, 2026-09-02.** The offense/punishment
    taxonomy hub; drafted once 6 (due-process template) and 9
    (dangerous-technology categories) already existed to reference.
  - **Article 7 (Sheriff) — ✅ drafted, 2026-09-02**, at the user's specific request to ensure stairwell/special-area public-order guidance existed. The enforcement complement to 6.
  - **Article 4 (Office of Mayor)** and **Article 5 (Deputy Mayor and the
    Order of Succession)** — 4 before 5, since succession is defined
    relative to the office it succeeds; 5 is also a Structural Fragility
    site (see below).
- **Tier 3 — comparatively self-contained, sequence flexibly:**
  Articles 3, 10 (✅ Mines — drafted, 2026-09-02, out of the recommended order —
  user chose to draft it as an explicit directive after Articles 1–9 were researched,
  see `CANON.md` §18 and `HYPOTHESES.md` entry 5), 11 (✅ Supply — drafted 2026-09-02,
  renumbered from original Article 10), 12, 13, 14, 15 (✅ Schooling — drafted
  2026-09-03, inserted after this list was first written; see the Article 15
  facts table below), 19, 20, 21, 22, 23. Note **Article 18 (The
  Cleaning)** also sits here despite its thematic centrality — it's a
  "leaf" other Articles point to rather than one that generates
  dependencies for others, so by the *cross-Article-consequence*
  criterion specifically (not overall importance) it doesn't need to be
  early. Article 21 benefits from 9 already being settled; Article 14
  benefits from 8. Article 11 benefits from 10 being settled.
- **Last, deliberately** — **Article 23 (Amendment and Continuance) and
  the back-matter Amendment Log**: needs the founding-timeline question
  resolved (open item #1 above) and the fullest possible picture of
  everything else, per the Amendment Drift principle (`STYLE.md`). Both
  are now ✅ drafted (2026-09-03), including the entrenchment mechanism and
  date-ambiguity revisions — see Established facts (Article 23) below.

This is a recommendation, not a locked sequence — re-check it if a
Tier 3 Article turns out to matter more than expected once we're in it.

## Design-first flags (from full-outline review against all guiding principles, 2026-09-01)

Not open tensions — assignments of where a guiding principle should be
designed in *first*, before the clause is written, so the mechanism is
real rather than reverse-engineered after the prose.

- **Article 5 (Deputy Mayor and the Order of Succession) is the primary
  site for the Structural Fragility principle** (`STYLE.md`). Not just a
  plausible fit — canon already validates it: Bernard's rise to acting
  mayor after Jahns's death is a real, exploited ambiguity in a
  succession rule that must have sounded reasonable on paper. When
  drafting Article 5, work out the actual blind spot in Victor's design
  first (add it here as a new fact once decided), then write the clause
  it hides behind. **Relevant precedent from Article 7's correction**
  (see its facts table below): "an appointing authority weighs a
  recommendation but isn't bound by it" is now an established pattern
  for leadership offices — a very plausible shape for whatever
  ambiguity Bernard ends up exploiting in Article 5, since "the Mayor's
  discretion isn't bound" is exactly the kind of reasonable-sounding
  rule that becomes dangerous when the officer offering the
  "recommendation" (or standing to receive the discretion) has ulterior
  motives.
- **Article 2 (Citizenship and the Census) — ✅ drafted, 2026-09-01,
  Structural Fragility designed and written.** The census (kept by
  Judicial) is only as accurate as the self-reporting of the officials
  who feed it: Section 4 states plainly that Judicial "relies upon
  [department] reports being made in good faith" and "is not charged to
  seek out such changes on its own account"; Section 5 routes every
  death through a single trusted attester (a physician under Article 19,
  or IT's own word for a cleaning-death) with no independent check. This
  isn't invented from nothing — it directly generalizes the
  already-established canon fact that Peter Nichols, a doctor, could
  freely falsify his own family's causes of death (`CANON.md` section
  13). Article 2 makes that a designed feature of the whole system, not
  a one-off. Deliberately understated in the prose — reads as ordinary
  administrative delegation, per the Restraint principle — not flagged
  as suspicious anywhere in-text.

## New research not yet incorporated (2026-09-02, offhand TV references)

`CANON.md` section 18 and `HYPOTHESES.md` entry 3 collect several small
canon findings that arrived before the Articles they affect were
drafted — good timing, no retroactive fixes needed, but flagging here so
they're not missed when those Articles come up:

- **Article 3 (Marriage, the Lottery, and the Right of Birth) — ✅ drafted.**
  Uses "sanctioned"/"sanctioning" as the formal term of art for
  lottery/marriage permission, consistent with the show's own vocabulary
  and `HYPOTHESES.md` entry 3.
- **Article 10 (Mines and the Ore-Winning) — ✅ drafted, 2026-09-02.**
  Established Mines as a distinct Department (resolving `FACTS.md` open
  item 3), with Head of Mines appointment, 200-foot radius limit
  (TV-sourced), and coordination mechanism with Mechanical. Removed
  ore-winning from Article 9 (Mechanical) and consolidated it here.
- **Article 11 (Supply, Hydroponics, and the Ration) — ✅ drafted,
  2026-09-02 (renumbered from original Article 10).** Adopted "sanction"/"sanctioning" as the formal term for
  pet-keeping (Section 5, "Sanctioned Animals Kept by Citizens"),
  fulfilling `HYPOTHESES.md` entry 3 and `CANON.md` §18. An unsanctioned
  pet is explicitly treated as diverted livestock under Article 17 —
  grounds Bernard's joke in real statutory logic.
- **Article 16/17 (Public Order/Forbidden Speech; Crimes and Their
  Punishments) — ✅ both drafted, 2026-09-02.** Three things were
  incorporated:
  1. A **relic classification/severity system**, with a confirmed
     "red-level" tier (informational relics — books, drives — that
     could seed rebellious ideas) and a process of Sheriff-intake →
     Judicial-classification, with individual relics (e.g. watches)
     sanctionable as legal exceptions rather than a blanket
     forbidden/not-forbidden binary. Article 8's IT-examination step
     (technological relics) should fold in as a sub-case of this
     broader pipeline, not a competing one.
  2. **A third punishment tier: the mines** — distinct from both a
     first-offense grace/warning and cleaning. Brutal, unfree, sentence
     lengths in years, used for relic possession and similar
     serious-but-survivable offenses. Article 17's offense/punishment
     taxonomy should be at least three-tiered, not binary.
  3. A decision on whether "sanctioned" (relationships/relics/pets) and
     "licensed" (already used for Article 8/9's dangerous-instruments
     mechanism) are the same underlying device under two names, or
     deliberately distinct registers for different domains — pick one
     before drafting 16/17, and keep the choice consistent with
     whatever Article 3 and 10 end up using.
- **Founding timeline (open item 1, above)**: a secondary source's loose
  paraphrase ("ten thousand people, at least 140 years, likely much
  longer") is *compatible* with either resolution option already on the
  table — doesn't resolve the tension, just doesn't add a new one.
- **Article 6 (Judicial and the Courts) — ✅ drafted, updated
  2026-09-02.** Added the Judge's-search-of-Sheriff's-office
  limitation clause to Section 3 (see Established facts table below);
  fulfills the search/seizure carve-out noted in `CANON.md` §18.
- **Article 20 (Of Assembly and the Common Halls) — ✅ drafted, but the two
  items below were not incorporated into the draft as written** (confirmed
  by text search, 2026-09-03) — still open if this Article is revisited.
  `CANON.md` §18 records two cafeteria facts to incorporate: (1) the
  Level 1 cafeteria closes for the night (with a separate Mechanical
  cafeteria in Down Deep) but certain citizens are authorized to draw
  food after hours — the authorizing mechanism and who qualifies still
  needs to be invented, since the specific TV detail wasn't
  independently confirmable and is being taken on the user's account
  per the TV-sourcing rule; (2) an incidental discovery — seating for
  viewing a cleaning is allocated by lottery, which should tie into
  Article 3's lottery machinery (or at least reuse consistent lottery
  vocabulary) rather than inventing a second, unrelated lottery
  concept.
- **Article 9 (Mechanical) — ✅ updated 2026-09-02.** Ore-winning charge
  removed from Section 1; all ore-extraction is now Article 10 (Mines).
  Article 9 retains only power, circulation, reclamation, and structural work.
  See `CANON.md` §18 and `HYPOTHESES.md` entry 5. Open item 3 now resolved:
  Mining is its own distinct Article 10.
- **Article 2 and Article 17 — ✅ updated 2026-09-02.** Self-killing
  outside Article 18's sanctioned request added: Article 2 §5 (Judicial
  finding required, not physician attestation alone) and Article 17 §4
  (named among the gravest, completed-death exception addressed). See
  `CANON.md` §18 and `HYPOTHESES.md` entry 6.
- **Article 19 (Health, the Infirmary, and the Mind) — ✅ drafted,
  2026-09-03.** Physicians' conditional at-risk referral is discretionary,
  not mandatory (see Established facts below) — resolves the texture this
  item originally flagged as owed, consistent with the Structural
  Fragility crack the Article 2/17 self-killing clauses already lean on.

## Established facts (from Article 1, "Of the Founding and Purpose of the Silo")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| Silo has 144 levels | Founders' original engineering | Any floor-specific reference in Articles 2–23 must stay inside 1–144; zoning (Up Top / Mids / Down Deep) established here should be reused, not reinvented |
| Single spiral stair is the only common passage, +1 narrow freight-lift exception (Supply/Mechanical, governed under Article 9) | Physical/structural + social-order rationale (see open item 2) | Article 9 must define the freight lift's rules; Article 21 (Porters) should explain why porters still walk despite the lift existing |
| The Pact makes no claim about how long the silo has stood or how long ago it was sealed | Deliberate — see Open Item 1 (RESOLVED, then extended 2026-09-03 to full date/founder ambiguity) | The Amendment Log (backmatter) and the preamble must stay consistent with this: no explicit years anywhere, and no claim that the founders lived inside the silo |
| No citizen may dig/bore/blast any new passage through floor/ceiling/wall, absolute prohibition, no exceptions for "claimed emergency" — enforceable only by Head of Mechanical + joint Mayor knowledge | Founders' fear of structural compromise / inter-silo contact (Order-level reason not stated in-text) | Nicely pre-explains why Juliette's dig-to-Silo-17 project (*Dust*) would be an extraordinary, silo-shaking act if it happened here — good consilience, keep this framing intact in Article 9/22 |
| Wallscreen at top level shows outside view continuously; upkeep is IT's exclusive duty via unspecified procedure | Gestures at Order-level secrecy without stating it ("such further procedure as that Department alone is instructed in") | Reuse this exact gesture-without-specifics device anywhere else IT's real technical secrets are adjacent (Article 8, Article 18/Cleaning) |
| Tampering with/obstructing the outward sensors is among the gravest offenses, tried under Article 17 | Sensors are the silo's only "proof" the outside is deadly — tampering threatens the whole control system | Article 17's offense list must include this at high severity; Article 18 (Cleaning) should stay consistent about sensor upkeep being cleaners' actual task |
| Citizenship: by birth in the silo, or oath before Judicial at majority; not sold/inherited/transferred | — | Article 2 (Citizenship and the Census) must not contradict this definition |
| Citizen obligations don't lessen with age, except where Articles 13 (labor/children) and 19 (health/the retired) expressly provide | — | Articles 13 and 19 are on record as owing an explicit age-based exception — don't forget to actually write one |
| Pact kept in print in the Judicial archive, Mayor's office, Sheriff's station, and "no fewer than one copy per twenty floors" | Public-access requirement, "no citizen may be denied sight of this Pact" | 144 ÷ 20 = 7.2 → at least 8 public copies beyond the three named ones; if any later Article references "the Pact posted at [floor]," keep it consistent with a roughly-every-20-floors distribution |
| Ignorance of the Pact excuses no violation, except where the Pact itself provides a first-offense warning/grace (per Article 17) | — | Article 17 must actually define what that grace/warning mechanism is |
| Silo zoning: Up Top (Mayor/Deputy Mayor, Sheriff, Judicial, cafeteria/wallscreen, classrooms) / Mids (housing, markets, hydroponic farms, infirmary, trades) / Down Deep (Mechanical, generator, water treatment, deep storage) | — | Keep every later Article's floor placements consistent with this three-way split |

## Established facts (from Article 9, "Of the Department of Mechanical")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| Head of Mechanical is raised up via shadowing (Article 12) from within Mechanical's own trades, confirmed by the Mayor | Consistent with the general shadowing/succession mechanism | Article 12 must actually define shadowing in a way compatible with this; Article 4/5 (Mayor/Succession) should treat "confirms Heads of Department" as a real Mayoral power |
| Power (generator), Circulation (water/air treatment), and Reclamation (recycling) are treated as one charge under Mechanical | Failure of any one threatens all the rest (closed-loop life support); mirrors the show's own transcribed Pact category "Circulatory, Energy or Recycling systems" | Article 17 should use this near-verbatim show clause as its model when codifying the offense of interfering with these systems; Article 11 (Supply) must not claim independent authority over water/air stores, only joint exercise alongside Mechanical |
| Interference with the generator, water/air works, or reclamation is "among the gravest offenses" under Article 17 | Echoes the identical phrasing already used for sensor-tampering in Article 1 | Article 17 needs a coherent tier of "gravest offenses" that includes both this and sensor-tampering — should read as one consistent category, not two separate one-off severities |
| The freight lift is cargo-only, logged (goods/citizen/floors) under Article 21, and speed/power-capped by the Head of Mechanical | Resolves `FACTS.md` open item 2 — see above | Article 21 must define the actual log format/keeping; Article 16 must contain the general ban on citizen-built passenger conveyances this clause forward-references |
| No new passage may ever be opened toward the world above or beyond the builders' original depth, regardless of the Head of Mechanical + Mayor's joint order under Section 4 | Gestures at Order-level secrecy (other silos, the surface) without stating it | Article 22 (Emergency) must not carve any emergency exception to this — Article 9 already states the prohibition holds "regardless of the reason offered or the office of the one offering it"; also pre-explains why Juliette's *Dust*-era dig would be extraordinary here too, alongside the Article 1 fact above |
| IT licenses precision tools/optics to Mechanical (numbered, tracked, returned) under this Article, forward-referencing Article 8's licensing authority | Dangerous-knowledge containment (`HYPOTHESES.md` entry 1) | Article 8 must actually establish this licensing authority when drafted — Article 9 has now promised it exists; an unlicensed tool is treated as a forbidden relic under Article 16, so Article 16 must include this equivalence |
| Mechanical's remaining charge is power, circulation, reclamation, and structural work — ore-winning has been moved to its own Article 10 (Mines) | As of 2026-09-02, Mining was spun out as a distinct department | No contradiction introduced; Articles 9, 17, and the broader penal-labor machinery remain consistent |
| **Critical infrastructure secrecy is compartmentalized by need-to-know (RESOLVED 2026-09-03)**: the Head of Mechanical determines whether the Mayor needs to know about a specific critical system based on whether Mayoral decisions might affect it; whether the Mayor is informed is solely the Head of Mechanical's decision | Resolves the Article 9 §7 fragility: if the Mayor doesn't know about the Safeguard, can't defend against its exploitation — a feature of Victor's design, not a bug | Keeps the Mayor's knowledge compartmentalized (order-level thinking pattern) while explaining why Article 9 §4's "joint Mayor/Head knowledge" doesn't preclude other critical systems staying hidden even from the Mayor |

## Established facts (from Article 10, "Of the Department of Mines")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| Head of Mines is raised up via shadowing (Article 12) from within Mines' own trades, confirmed by the Mayor | Consistent with the general Department-head succession mechanism (Article 9, 11, etc.); identical to the pattern | Article 12 shadowing mechanism must include Mines trades as shadowing-eligible; Article 4/5 (Mayor/Succession) continue to treat "confirms Heads of Department" as a real Mayoral power |
| Mines is led by a distinct office (Head of Mines), separate from the Head of Mechanical | Resolves `FACTS.md` open item 3 via explicit user choice and full Article 10 drafting | All Articles that reference "Head of Mechanical" must not mistakenly include Mines under that title; Articles involving mines-as-penal-labor (17) must be checked for consistency (currently framed as Mechanical's charge, but the two departments' administrative relationship needs texture) |
| The winning of ore in the workings below the Down Deep is Mines' standing charge, requiring no order for ordinary continuation | Ore extraction is Mines' *primary* function, not a secondary charge of another department | This is the clean inverse of Article 9's revised charge: Mechanical processes ore (at metal-working) but doesn't extract it; Mines extracts but doesn't process |
| No working of ore may run beyond two hundred feet from the silo's own structure, in any direction | TV-sourced (Head of Mines Ed Harwood's Season 3 line, "never out... not more than two hundred feet, because the Pact says so"); same engineering-knowledge/escape-containment logic as the magnification and mechanized-transport bans, applied to radius instead of optics or motors — see `HYPOTHESES.md` entry 5 | Consistent with, doesn't contradict, Article 9's absolute depth prohibition (which caps vertical depth at what the builders reached; this caps horizontal radius separately). Any future Article touching escape-capacity containment should reference this limit consistently with the other "designed-in caps" (freight lift logging, IT monopoly, sensor ban, etc.) |
| Any mining beyond the 200-foot limit is "among the gravest offenses" under Article 17 | Encodes the Founders' judgment-without-explanation, consistent with `HYPOTHESES.md` entry 5's reasoning (the radius is an engineering-knowledge/containment decision, paralleling why magnification and mechanized transport are restricted) | Article 17 needs "mining beyond the 200-foot radius" as a defined gravest offense; Article 18 (Cleaning) should stay consistent with this being a top-tier punishment territory |
| The Head of Mines and the Head of Mechanical shall meet at least once per ten days to coordinate workings and structural concerns | Pragmatic coordination between two Down Deep departments, codified as a standing duty, not a suggestion | This is the first Pact clause explicitly requiring recurring formal coordination between two Department heads — a small but real detail texture for the bureaucratic register |
| Mechanical can halt a Mines working if it threatens the silo's structure or Mechanical's own charge (water lines, generator housing, etc.); Mines can appeal to Judicial if Mechanical's order is refused | Balances the two departments' independence without one being subordinate — shared Down Deep geography requires mutual deference | Article 9's existing charge (structural soundness of the shaft) should not contradict this; Article 6 (Judicial) can treat this appeal as an ordinary inter-department dispute |
| Death by self-killing (unsanctioned) is now among the gravest offenses (Article 17 §4) | TV-sourced (Deputy Hank Murphy plot, George Wilkins death; user research, `CANON.md` §18, `HYPOTHESES.md` entry 6) — but Article 10 itself does not directly codify this; Article 17 does. Flagged here because Mines (as penal labor) may be a destination for other offenses, and the gravity-tier system needs consistency across all gravest-offense Articles | Article 17 and Article 18 (Cleaning) should be consistent that self-killing (unsanctioned) is gravest-tier; Article 2 §5 correctly routes suspected self-killings through Judicial for a finding before closing a death, and Article 17 §4 handles the "completed death, no sentence possible" edge case correctly |

## Established facts (from Article 2, "Of Citizenship and the Census")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| Majority (full citizen standing — oath, lottery entry, Assembly speech, office) is reached at the sixteenth naming-day; a "naming-day" is reckoned from the day of naming (within 10 days of birth), not the day of birth | Invented specific number, no direct canon source but doesn't conflict with anything (Juliette started Mechanical work at 14, which this is compatible with if working/shadowing under Article 13 can begin before majority) | Articles 13 (Labor/Shadowing), 15 (Schooling), 19 (retirement) all key off naming-day; Article 3 (lottery entry), 20 (Assembly), and office-holding Articles (4/5/6/7) all require majority — stay consistent with 16 as the threshold |
| A child born without the Article 3 lottery's grant is still named and entered in the rolls; the responsible citizens (not the child) are answerable under Article 17 | Compassionate-sounding provision — candidate Anna Thurman fingerprint, though not explicitly attributed in-text | Article 17 must define what "answerable" actually means for unlicensed birth — currently unspecified |
| Judicial keeps the census ("the rolls") for every living citizen: name, naming-day, floor/household, trade; issues an "occupant card" to every citizen of majority | TV-sourced physical-prop detail (occupant cards), adopted per the TV-sourcing rule, no book conflict found | Any later Article referencing citizen identification/verification (Sheriff stops, Judicial hearings, Supply rationing) can reference the occupant card consistently |
| **Structural Fragility (designed)**: the census depends on Housing/Supply/Department Heads self-reporting changes "in good faith," with Judicial "not charged to seek out such changes on its own account"; death is recorded solely on a single trusted attester's word (a physician, or IT for a cleaning-death) | Generalizes the already-canon Peter Nichols death-certificate-falsification fact into a systemic design feature — see `CANON.md` section 13 | This is the load-bearing crack for later plot-adjacent Articles: Article 19 (Health) should stay consistent with physicians having real, unaudited authority over cause-of-death; Article 18 (Cleaning) and Article 8 (IT) should stay consistent with IT's word alone closing a cleaning-death's record, unaudited |
| The census's count (and no other number) is the population for every Pact purpose, including Article 3's lottery and Article 11's ration | Ties population-legibility directly to two of the silo's most consequential mechanisms | Articles 3 and 11 must treat the census as their sole source of population figures — don't invent a competing count elsewhere |
| A citizen may petition Judicial to correct the rolls; "Judicial's finding on such a petition is final" | Light-touch echo of the "hollow due process" pattern — not the full elaborated version (that's Article 6's job) | Keep consistent with, but don't confuse for, Article 6's fuller due-process template |
| **Added 2026-09-02**: a death suspected by the attending physician to be self-inflicted, and not sought/granted under Article 18, cannot be closed on the physician's attestation alone — it must be carried to Judicial for a finding under Article 6 first | TV-sourced ("suicide is a crime against the Silo"; a Deputy is shown hoping a death isn't ruled suicide specifically to avoid the extra paperwork it triggers) — this reinforces, not patches, the existing Structural Fragility crack above: an honest physician still has every reason to attest something else instead, to spare a family the same process | See `HYPOTHESES.md` entry 6; new offense drafted into Article 17 §4 (named among the gravest, with the completed-death-cannot-be-sentenced problem addressed directly); Article 19 (Health/Mind) owes texture on at-risk citizens and any physician reporting duty — see its Established facts below |

## Established facts (from Article 4, "Of the Office of Mayor")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| Mayor is the civilian head of the silo, confirmed per Article 5, answerable to the Assembly under Article 20 | First executive office; loads forward into succession design (Article 5, primary Structural Fragility site) | Articles 5 and 20 must be consistent with Mayor's tenure and removal; no other Article should claim executive authority over the Mayor's ordinary decisions |
| Mayor confirms Department heads (Mechanical, IT, Supply, Mines, etc.) upon their recommendations via shadowing (Article 13) | Extends the shadowing/confirmation mechanism as a standard pattern across all Departments | Article 13 shadowing must include provision for heads recommending their shadows; heads remain removable only via Judicial finding + Assembly removal (Article 20) |
| Mayor appoints the Sheriff (not via shadowing, not bound by recommendation) at Mayor's sole discretion, "weighing" advice from outgoing Sheriff but not bound by it | Corrects earlier canon misconception; follows the Juliette precedent (Mayor's real discretion, not a rubber stamp over a groomed Deputy). Establishes "appointing authority's judgment is final and not bound" as a pattern for leadership offices — precedent for Article 5 Structural Fragility design | Sheriff's office remains distinct from other Department-head succession; Article 7 already treats Deputies as shadowed subordinates, not as heirs-apparent to the Sheriff's office |
| Judge is confirmed jointly by Mayor and Assembly (not just Mayor), standing once in lifetime until death/removal by the same two bodies — highest bar for any office | Extra-legitimacy-sounding process, consistent with canon; creates dramatic irony since this process is known (via canon) to not prevent Judicial capture by IT/Bernard | Article 20 must include the mechanism for Assembly confirmation and removal votes; Article 6 already established the Judge's office |
| Mayor and Judicial are co-equal in authority, neither binding the other's Pact-given powers | Establishes a real separation of powers, not a hierarchy | Article 20 must treat Mayor-Judicial disputes as Assembly-level matters, not subordination; Article 22 (Emergency) should clarify emergency authority doesn't subordinate either office |
| **The Syndrome (eligibility rule) — NEW from TV prop transcription (2026-09-03)** [TV, semi-authorial]: Any citizen afflicted with The Syndrome may not hold any public office of any kind, nor undertake any work responsible for the silo's welfare that might jeopardize citizens | Medical/competency criterion for all office-holding; TV show's Article 5 makes this a blanket rule, not office-specific | Articles 4 (Mayor), 5 (Deputy Mayor), 6 (Judge), 7 (Sheriff), 8 (IT Head) must all reference this bar; also relevant to critical-role vetting under Article 13 (Labor). Consider whether this is a single forward-reference to a consolidated rule, or separate clauses in each office Article |
| Deputy Mayor resides in Up Top, has access to Mayor's records for preparation, becomes acting Mayor in absence (with all powers except permanent appointments) | Succession preparedness, plus a real barrier (no permanent changes without permanent succession under Article 5) | Article 5 must elaborate when/how Deputy's temporary acting becomes permanent; Article 20 can reference the distinction |
| **Forbidden-speech offense (Article 16 §1) explicitly added to Article 17 §3 as mines-level offense** | Clarifies that forbidden-speech is not a gravest offense; offenders get pre-sentence Judicial hearing per Article 6 | Article 6 updated (2026-09-02) to specify what a pre-sentence hearing includes: accused citizen may speak, call witnesses, dispute Officers' account; Judge hears all before sentencing |

## Established facts (from Article 8, "Of the Department of Information Technology")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| IT is headquartered in "the Mid Thirties" (the zone Article 1 already named at the top of the Mids), not "Up Top" proper | Article 1's Up Top enumeration (Mayor, Deputy Mayor, Sheriff, Judicial, cafeteria/wallscreen, classrooms) doesn't list IT — placing it here avoids contradicting that list while matching canon research's fan-reconstructed floor plan ("IT in the 30's") | Any later Article referencing IT's location should say Mid Thirties, not Up Top |
| IT licenses: (1) magnification beyond reading-spectacle power, (2) any wireless send/receive device, (3) fine metal/wire/glass instruments — fulfills the promise Article 9 made | Formalizes `HYPOTHESES.md` entry 1's "dangerous knowledge" containment thesis | Article 16 must treat an unlicensed instance of any of these three categories as a forbidden relic, consistent with Article 8 Section 2 |
| Licenses are double-recorded — a roll kept by IT *and* one shared with Judicial, "reconciled one against the other at any time either Department requires" | A small deliberate Victor "tell" — oddly precise cross-checking specificity for a citizen-facing legal text, per `STYLE.md`'s tonal-uncanniness device (first use of it in drafted text) | Not a Structural Fragility site (those remain Articles 2 and 5 only) — just a rare, intentional stylistic flourish; don't overuse this device elsewhere |
| No wire/radio device may be built or operated except by IT or under its license; unlicensed inter-floor word-carrying is by porter (Article 21) | Ties HYPOTHESES.md entry 2's "no mechanized alternative" logic to communications specifically, not just transport | Article 21 (Porters) must be consistent with porters existing precisely because radio/wire is IT-monopolized, not freely available |
| IT's sensor/wallscreen upkeep procedure is *still* not stated (reinforces Article 1's gesture-without-specifics), and IT's word alone remains sufficient to close a cleaning-death's record per Article 2 — no new oversight added | Deliberate — preserves the Article 2 Structural Fragility crack instead of accidentally patching it | Article 18 (Cleaning) and Article 19 (Health) must stay consistent with this: IT's attestation for a cleaning-death is unaudited, matching a physician's for an ordinary death |
| IT examines relics of "craft and contrivance" (technological contraband) for Judicial, and "need not report how it was examined, nor keep the relic for any citizen's later viewing" | Same gesture-without-specifics device applied to relic examination | Article 16 should treat IT as the technical authority on relic danger-assessment; don't contradict by giving another department this role |
| Head of IT names their own successor (from within the Department); it stands "as though confirmed" unless Mayor + Judicial jointly object within one season — asymmetric with Article 9's Head of Mechanical, who requires affirmative Mayoral confirmation | Institutional insularity/autonomy, consistent with canon's Bernard eventually acting with real independence from civilian oversight — a plausible, undramatic bureaucratic default-approval mechanism, not a flagged "crack" | Article 5 (Deputy Mayor/Succession, the primary Structural Fragility site) can lean on this same insularity when designing its own mechanism — worth checking consistency when Article 5 is drafted |

## Established facts (from Article 6, "Of Judicial and the Courts")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| Judicial is led by "the Judge" (not "Head of Judicial" — deliberately distinct title from the trade-Department convention), confirmed by *both* the Mayor and, thereafter, the Assembly — a higher bar than any Department head | Extra-legitimate-sounding process for the single most powerful office in the silo — sets up dramatic irony, since we know from canon this extra process doesn't actually prevent capture | Article 4 (Mayor) and Article 5 (Succession) should treat "confirms the Judge" as a real Mayoral power; Article 20 (Assembly) must include a confirmation/removal vote mechanism consistent with this |
| Judicial's own enforcement/investigative corps is "the Officers of Judicial" — explicitly *not* the same body as the Sheriff (Article 7); Officers act only at the Judge's direction or "the implicit command of the Mayor," never on their own authority | Matches canon's Judicial-has-its-own-enforcement-arm structure (the show's "Raiders"); "implicit command of the Mayor" phrase is a direct reuse of the show's own transcribed clause | Article 7 (Sheriff) must be written as day-to-day peacekeeping only, explicitly distinct from Judicial's Officers — don't blur the two bodies |
| **The master "hollow due process" clause is now canonical**: for the gravest offenses (Article 17), the Judge determines guilt and sets sentence "without further trial," takes effect at once; family/offender representations *after* sentencing are heard but "do not delay, lessen, or undo" it | This is the template `STYLE.md` already called for — now actually written, not just described. Also: offering a hearing/representation at all despite it changing nothing is itself a piece of applied procedural-justice psychology (people accept outcomes better when they feel heard, even when the process doesn't change the result) — consistent with Victor's psychologist fingerprint (`CANON.md` 17a) | Articles 7, 17, 18, 22 must reference this template rather than reinvent their own version — cite Article 6 Section 4 directly |
| **Tiered due process, not flat**: offenses *not* among the gravest get a real pre-sentence hearing on request; only the gravest skip straight to sentence-then-representation | Deliberate nuance — the Pact isn't uniformly hollow, only precisely where control actually matters (dissent-adjacent grave offenses), which reads as more calibrated/plausible than blanket cruelty | Article 17's offense list needs a clear "gravest" tier vs. an ordinary tier, since Article 6's procedure now depends on that distinction existing |
| Judicial issues written rulings when the Pact is silent (Article 1's promise, now elaborated): reasoned, archived, and "read into the record at the next sitting of the Assembly... that no ruling binds the silo in secret" | A transparency-sounding safeguard that coexists with (and doesn't contradict) other places where secrecy is explicit and permitted (e.g. Article 8's relic-examination method need not be reported) — the two aren't in tension since this clause only covers *silent-Pact rulings*, not every Judicial action | Over the silo's ~150–200 year history (pending the founding-timeline open item), these rulings should accumulate as a body of "Judicial common law" — good additional texture for the Amendment Log's authorial-drift principle (`STYLE.md`) alongside formal Amendments |
| Judicial archive records, once entered, cannot be altered — only corrected by a dated, attributed follow-up entry, original preserved | **Does not patch the Article 2 Structural Fragility crack** — this only prevents *later tampering* with an entry, not a *false attestation at the time of entry* (a doctor's false cause-of-death is still entered honestly-as-stated and stays exactly as false); worth keeping this distinction clear if it comes up again | Article 2's fragility remains fully intact; don't accidentally treat this clause as a fix for it in later Articles |
| A Judge-ordered search for a concealed relic (Article 15) may reach any floor or room freely, save the Sheriff's own station, which requires both extreme cause found by the Judge and advance notice to the Sheriff | TV-sourced (Season 1, "Hanna" — Deputy Billings' "without extreme cause" line); the one explicit carve-out in an otherwise unconditional search power reads as a real, load-bearing check on Judicial reaching into the Sheriff's office unannounced — plausibly there to prevent Judicial from using relic-search pretext to purge or intimidate the Sheriff's own department | Article 7 already treats the Sheriff's station as a restricted, non-common area — this is consistent, not duplicative; Article 20 (Assembly/search-and-seizure texture generally) should not grant any other office an equivalent carve-out without a similar canon basis |

## Established facts (from Article 11, "Of Supply, Hydroponics, and the Ration")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| The ration is set by the Head of Supply "from the full count of the rolls under Article 2, and no other number" — fulfills Article 2's own forward promise | Direct closure of a cross-Article loop set up two Articles ago | Any later Article referencing population-dependent allocation (chits, housing, schooling capacity) should follow this same "census is the sole source of truth" pattern rather than inventing a separate count |
| Ration is a flat per-citizen right "not increased for labor, office, or seniority," adjustable only where Article 13 or 19 expressly provide; shortfalls are "lessened alike for every citizen, without exception of floor, trade, or office" | A sincere-sounding equality guarantee, echoing Article 1's "no office excuses its holder" language | **Worth flagging for the Amendment Log later**: we know from canon that Up Top/Down Deep treatment is *not* actually equal in practice (Bernard's bias against mechanics) — this clause is a good candidate for later tension/violation in an Amendment Log entry or a `HYPOTHESES.md`-style true/stated split, without needing to state the gap anywhere in Article 11 itself |
| The freight lift (Article 9) is explicitly used to move Supply's own goods between the Down Deep and Supply's floors — closes the loop on Article 9's "reserved to Supply and Mechanical" line, which had gone unused until now | — | No further action needed; the freight lift's dual-department reservation is now fully accounted for in both directions |
| Supply keeps stores of water/air *delivered by* Mechanical (Article 9) and distributes them by the same ration mechanism as food — a clean production (Mechanical) vs. distribution (Supply) split | Consistent with Article 9 Section 2's "exercised alongside Supply... under Article 11" promise | Article 19 (Health) and Article 22 (Emergency) should stay consistent with this split if either ever touches water/air shortage scenarios |
| **Pets formalized**: a citizen may petition Supply to "sanction" a companion animal (Section 5); a sanctioned pet draws on the *household's own* ration; an *unsanctioned* pet is legally "treated as livestock diverted from Supply" — an Article 17 offense | Fulfills `HYPOTHESES.md` entry 3 (uses "sanction" as the general licensing term of art) and grounds Bernard's "sanctioned pet" joke (`CANON.md` §18) in real statutory logic | Article 17 needs "diversion of Supply livestock" as a defined offense category, since Section 5(c) now depends on it existing |
| Livestock (Supply's own, kept for the ration) is explicitly distinct from sanctioned pets (a citizen's own, for companionship) — different legal categories, different ration accounting | — | Keep this distinction consistent if livestock or pets come up again (e.g. Article 14 Housing, if household composition ever references animals) |

## Established facts (from Article 17, "Of Crimes and Their Punishments")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| **The three-tier punishment scale is now canonical**: grace (formal warning, once per citizen lifetime, for non-gravest offenses only) → the mines (labor sentence, second offense or a first offense the Judge finds too grave for grace) → cleaning (Article 17, gravest offenses only, no grace, no hearing, no commutation "whatever representation is made under Article 6") | Directly implements `CANON.md` §18's mines-tier research — previously-missing structure, now filled in | Article 17 must be consistent with cleaning as strictly the top tier, never used for mines-level offenses; Article 6's due-process split (hearing for non-gravest, none for gravest) now has its offense catalog to operate on |
| **The mines are framed as pre-existing "deep workings below the Down Deep," administered by the Head of Mechanical** — deliberately *not* framed as citizens digging new passages | Resolves a real potential coherence conflict: Article 9's digging prohibition is absolute ("regardless of purpose, curiosity, need, or claimed emergency") with no stated exception for mine labor — framing the mines as already-existing builder-provided workings (consistent with Article 1's "deep storage of the silo's reserves" already being Down Deep/Mechanical's charge) avoids a contradiction rather than creating one | If Article 9 or 21 is ever revisited, keep the mines described as existing infrastructure, not an exception to the digging ban |
| **Gravest-offense catalog closed out**: sensor tampering (Art. 1), generator/water-air/reclamation interference (Art. 9), false life/death attestation (Art. 2), and any relic Article 15 classifies among the gravest | Consolidates every "among the gravest offenses under Article 16" forward-reference made by Articles 1, 2, and 9 into one place | Article 15 now has a **new firm promise**: it must define a relic classification system with at least a "gravest" tier (matching the show's "red-level" relic — `CANON.md` §18) for this clause to resolve cleanly |
| **Mines-tier catalog closed out**: food/feed diversion or waste (Art. 10), unsanctioned pet-keeping (Art. 10), being a responsible party for an unlicensed birth (Art. 2/3), and unlicensed relics/restricted instruments/devices (Art. 8/9/15) *unless* Article 15 classifies the specific relic as gravest | Same consolidation for the "answerable under Article 16" (non-gravest) forward-references from Articles 2, 8, 9, and 10 | Article 15 also needs a non-gravest relic tier (or a default) for the "unless classified gravest" branch to have something to fall back to |
| The Judge may name further gravest offenses via an Article 6 ruling, but must "state plainly why the offense is found to threaten the whole silo and not merely the citizen who committed it" | A transparency-sounding safeguard, same register as Article 6's "no ruling binds the silo in secret" | Consistent with, not a new instance of, the existing hollow-legitimacy pattern — no new Structural Fragility site created |
| A citizen who returns from the mines is reassigned by Judicial to a trade/floor that "need not be the trade or floor held before" | Punitive but not permanently exiling — the system reintegrates rather than discards | Article 12 (Labor/Shadowing) and Article 13 (Housing) should stay consistent with Judicial having this reassignment power over returning citizens |
| A general interpersonal-crime catch-all (violence, theft) exists, judged case-by-case across all three tiers depending on severity/intent | Keeps Article 16 from being *only* department-specific/bureaucratic offenses — grounds it in ordinary crime too | Deliberately left light/undetailed, consistent with Restraint — no further Article currently depends on this being more specific |
| Unlicensed-birth punishment for the responsible parents is **mines-tier, not gravest** — a comparatively lenient calibration for what could have been framed as the worst possible offense against population control | Quiet, unstated consistency with Anna Thurman's assigned territory (`STYLE.md`) — not flagged anywhere in-text as compassionate, just quietly less harsh than it could have been | No action needed; noted for anyone auditing where Anna's fingerprint shows up across the work |
| **Added 2026-09-02**: an unsanctioned self-killing (taking, or attempting to take, a citizen's own life by any means not sought/granted under Article 17) is now named among the gravest offenses; where the citizen does not survive, Judicial's finding is entered in the archive and closes the name under Article 2 with **no further punishment possible**, while a survived attempt is sentenced to cleaning like any other gravest offense | TV-sourced ("suicide is a crime against the Silo," per the user and confirmed research — a Deputy avoids ruling a death suicide specifically to dodge the extra process it triggers); the deliberate mismatch (stating a punishment clause that's moot for the dead, rather than quietly dropping it) is itself consistent with Founders'-psychology internal consistency — see `HYPOTHESES.md` entry 6 | The Pact's one other sanctioned form of citizen-chosen death (the Article 17 request) remains explicitly *not* an offense (Article 15 §1) — keep that distinction sharp in any later Article touching Cleaning or Health; Article 18 (Health/Mind) owes further texture on at-risk citizens |

## Established facts (from Article 16, "Of Public Order and Forbidden Speech")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| **The core taboo, precisely scoped**: forbidden to *wish, suggest, or teach* that going outside/the world above is survivable — but a citizen's own **final, direct request under Article 17 is explicitly not an offense**, "which this Pact answers in full" | Matches canon exactly: the request itself is granted, not punished; only loose talk/suggestion around it is criminalized | Article 17 (Cleaning) must be consistent with the request being a real, procedurally clean act, not framed anywhere as a crime being punished |
| **A citizen who overhears the forbidden wish and doesn't report it is answerable alongside the speaker** (Section 1) | Builds a mutual-surveillance incentive into ordinary citizen relationships — consistent with Victor's crowd-psychology fixation, stated in flat bureaucratic language, no in-text flag | Good texture for Article 19 (Assembly) and Article 18 (Health/Mind) if either ever touches social trust/isolation themes |
| **Section 3 is fixed as "False Teaching of the Founding and the Past"** — fulfills Article 1's specific "see Article 15, Section 3" promise, phrased with an almost-verbatim callback ("teach that invention to another as though it were known fact") | Direct textual consistency with an already-written cross-reference | No further action — this loop is fully closed |
| **Private speculation about the founding is explicitly not an offense; *teaching a child* invented history as fact is an aggravated one** ("offends gravely") | Not stated in-text, but this precisely explains — without ever revealing — the Order-level deep-lore fact that a Silo 18 teacher who retained forbidden memories previously taught children "to think for themselves," seeding a past reset (`CANON.md` §9). The Pact is quietly defending against the exact mechanism that already happened once | Strong candidate to keep in mind for Article 14 (Schooling) — schooling should read as tightly controlled/supervised in a way that's consistent with this being the specific fear driving the whole Article, without ever stating why |
| **Relic classification system now defined**, fulfilling Article 16's dependency: relics are graded by "danger to the silo's order"; a relic that could "teach a citizen to doubt what Article 1 records" is gravest-tier, destroyed or sealed at Judicial's sole discretion; lesser relics can be individually **sanctioned** for keeping (the watches precedent, `CANON.md` §18), and a sanction can later be withdrawn | Implements the show's confirmed red-level-relic system and resolves the terminology question `FACTS.md`/`HYPOTHESES.md` flagged: **"licensed" = IT's ongoing technical/instrument permits (Articles 8/9); "sanctioned" = one-time individual approval of a specific item/animal/relationship as legal** (relics, pets, and — if revisited — Article 3) | This terminology split should be treated as settled project convention going forward — reuse it, don't reintroduce ambiguity |
| Relic intake pipeline: citizen finds relic → surrenders to **Sheriff** → forwarded to **Judicial** for classification → **IT** examines it (Article 8) if technological | Consolidates Article 8's existing IT-examination role as a sub-case of this broader pipeline, not a competing one | Article 7 (Sheriff) should include the surrender-intake duty as part of its own charge when drafted |
| Restricted instruments/devices (magnification, wireless, fine tools, passenger-conveyance devices) are now formally forbidden by Article 15 itself, not just assumed by Articles 8/9 — an unlicensed one defaults to **gravest** classification unless Judicial finds cause otherwise | Closes the loop Articles 8 and 9 both opened; defaulting to gravest (rather than lesser) is consistent with `HYPOTHESES.md` entry 1 treating this category as the single most feared kind of contraband | Article 16's "mines unless classified gravest" branch now has a real default to point to — in practice, most unlicensed dangerous tech will land on the gravest/cleaning tier, with lesser classification the exception Judicial must affirmatively find cause for |
| Unauthorized gathering "beyond the ordinary gathering of a floor, a trade, or a household, or an assembly held under Article 19" requires the Sheriff's leave beforehand | Forward-references Article 19 for what counts as an authorized assembly | Article 19 must actually define what a sanctioned/ordinary assembly looks like, now that Article 15 depends on that definition existing |

## Established facts (from Article 7, "Of the Sheriff and the Keeping of the Peace")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| **Stairwell traffic convention**: ascending keeps the outer rail, descending keeps the inner rail; the Sheriff can vary this by posted notice per-landing | Practical solution to 144-level, single-passage congestion — grounded in the physical reality already established in Article 1 | Any later Article describing stairwell travel (e.g. a narrative aside, or Article 20's porters) should stay consistent with this convention |
| **Right-of-way priority order** on the stair: porters (Article 20) and urgent word for Judicial/Sheriff, then posted work crews (Article 1), then ordinary citizens | Consistent with the "no mechanized alternative" logic (`HYPOTHESES.md` entry 2) — porters matter enough to get physical priority, not just existence | Article 20 should acknowledge this priority when drafted |
| **Stairwell violence is explicitly weighted by fall-risk** — "given the height from which a citizen upon the stair may fall, is weighed by the Judge with that danger in mind" | Grounded, specific consequence of the silo's own geometry — doesn't redefine Article 16's tiers, just tells the Judge to weigh the danger within the existing framework | Consistent with Article 16 Section 5's general interpersonal-crime catch-all, not a competing mechanism |
| **The freight lift, Department offices, and any Pact-reserved room are explicitly *not* "common areas"** — being found there without leave is trespass, answerable under Article 16 | Consolidates Article 9's freight-lift restriction into a general trespass principle rather than a one-off rule | Any future restricted-space Article should be consistent with "not a common area" as the operative legal category |
| **Cleaning-viewing at the cafeteria wallscreen is neither compulsory nor forbidden** — the Sheriff keeps peace there, but "no citizen may be compelled to attend nor barred from attending" except for crowd-safety reasons | Grounded in canon (Jahns' remark that people would be eager to watch a cleaning after a long gap) — a "sounds protective of citizen choice" clause, consistent with the Pact's usual legitimacy-first register | Article 17 (Cleaning) should stay consistent with cleanings being public, witnessable events, not private/restricted ones |
| **Corrected 2026-09-02**: the Sheriff is **appointed by the Mayor** (not shadowed/promoted from Deputy) — the Mayor weighs the outgoing Sheriff's recommendation but "is not bound by it," and may appoint *any citizen of majority, whether a Deputy or not*. Deputies/Peacekeepers below the Sheriff are still shadowed under Article 12; the Sheriff's own office is explicitly carved out as not-shadowed | User caught a real canon inconsistency: the original draft used the generic shadow-then-confirm Department-head template, contradicting `CANON.md`'s own already-recorded note ("Sheriff: appointed (not elected) by the Mayor... Holston, then Juliette"). Juliette's book/show appointment — an outside mechanic with zero Sheriff's-office background, chosen over the in-house Deputy Marnes — is the clearest possible evidence the Mayor has real discretion, not a rubber-stamp over a groomed successor | **Important precedent for Article 5** (Mayor/Succession, the primary Structural Fragility site): "appointing authority has real, unbound discretion over a recommendation" is now an established pattern for leadership offices (Sheriff here; distinct from the Judge's stricter "must have served as an Officer first" rule in Article 6) — worth keeping in mind as a design option, and as a reminder to check CANON.md's per-office notes before defaulting to the generic Department-head template again |
| The Sheriff's dispute-resolution duty is explicitly *not* adjudication — the Sheriff "resolves by word alone" or refers to Judicial; anything mines-tier or gravest must go to Judicial | Reinforces, doesn't blur, the Article 6 Sheriff/Judicial split | Keep this boundary clean in any future Article touching either office |
| **Confirmed 2026-09-02**: Articles 6 and 7, as already drafted, jointly produce a real Judicial-over-Sheriff power asymmetry that is never stated outright anywhere in the text — matching TV canon (Sheriff and Bernard both acknowledge this dynamic; see `CANON.md` §14 and `HYPOTHESES.md` entry 4) | The asymmetry is emergent from five separately-motivated clauses (Judge's unchecked judgment power applies to any citizen incl. the Sheriff; Officers of Judicial answer to the Judge/Mayor, never the Sheriff; Sheriff's authority is capped at "by word alone," else refers up; Judge has a harder-to-remove tenure than the Sheriff's unstated one; Judicial alone may search the other's station) — no single clause claims supremacy, so nothing in the text is false | No new drafting needed. Article 4 (Mayor) and Article 5 (Deputy Mayor/Succession) should not grant the Sheriff any protection from Judicial's ordinary offense-based leverage, and Article 5 may want to reuse this same emergent-not-stated technique for its own Structural Fragility design |

## Established facts (from Article 18, "Of Health, the Infirmary, and the Mind")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| The Infirmary has charge of citizen health: prevention, care, fitness certification, and health records kept in Judicial archive (confidential, open to citizen and Judicial only) | Standard medical-department function | Articles 6, 13 must be consistent with health records being unavailable to other departments except by Judicial order; Article 16 should not require Infirmary reports to law enforcement except where the Pact expressly mandates it |
| No citizen may refuse medical treatment except where the Pact expressly compels it: (1) treatment of communicable disease, (2) mandatory health screening, (3) examination/restraint of a citizen found incompetent under Article 6 | Defines the boundaries of bodily autonomy vs. silo-level necessity | Articles 21 (Emergency) and 16 (Crimes) should not create new compulsion exceptions outside these three named cases |
| Mandatory health screening at intervals set by the Head Physician; refusal may trigger Sheriff-enforced compliance, subject to Judicial hearing on whether the screening was lawfully mandatory | A real check on unlimited screening discretion, though enforcement-friendly on the Infirmary's side | Article 7 (Sheriff) should be consistent with this compulsion-with-hearing model; Article 6 must treat such hearings as routine/non-gravest |
| **Physicians' conditional at-risk referral is discretionary, not mandatory (RESOLVED 2026-09-03)**: a Physician may refer a citizen believed to be in immediate, critical danger of self-harm to Judicial for protective evaluation using the Physician's own judgment; no Physician is obligated to refer citizens at lesser risk | Creates a bottleneck consistent with Article 2's census fragility — physicians' judgment is the gate, and that gate can fail/be misused | Article 16 should not create a mandatory-reporting duty that overrides this Pact text; Article 6 may define what "protective evaluation" entails when a Judicial referral arrives; Article 2 should remain consistent with physicians having reasons to under-report (no audit trail for cases *not* referred) |
| A citizen may self-petition Judicial directly for protective evaluation without waiting for a Physician's referral, and is entitled to a hearing on the necessity of any protective measures | Provides an alternative channel that doesn't depend on physician goodwill | Consistent with Article 6's general right-to-be-heard pattern, though the phrase "protective measures" remains undefined and could cover a range of interventions (isolation, restricted movement, forced care) |
| The Syndrome (degenerative neurological condition: tremors, progressive cognitive decline) bars any citizen from holding a critical role; diagnosed citizens must report it and are confined to ordinary labor only | Medical disqualification from leadership, not broader work restriction | Articles 4, 5, 6, 7, 8, 13 must all reference this bar where critical roles are defined; the diagnosis-privacy provisions here (Infirmary keeps confidential records, shared with Judicial only for critical-role vetting) should be consistent across all office-holding Articles |
| Retirement is available for citizens unable to perform assigned labor, via joint Head Physician/Mayor determination at an age they set, or via Judicial ruling for chronic illness/injury | Two pathways (executive age-default + individual exception) parallel the pattern already established in Article 4/Mayor and Article 6/Judge | Article 13 (Labor) should reference this as the valid exit from labor beyond direct Infirmary/Department recommendation; Article 20 (records) might reference retirement status where it touches citizen standing |

## Established facts (from Article 21, "Of Emergency and the Suspension of Ordinary Law")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| An emergency exists when the silo faces threats to survival: catastrophic system damage, disease, or other jointly-determined threats; declared by Mayor with Judicial challenge-right (if challenged, Judicial rules finally) | Co-equal emergency-declaration power, with Judicial as a check rather than rubber-stamp | Article 5 (Succession) should be consistent with Mayor's emergency role not creating an excuse for acting outside ordinary succession rules; Article 19 (Assembly) must define ratification procedures for emergencies lasting beyond one season |
| Emergency suspends ordinary Pact procedures for up to one season; beyond one season requires Assembly renewal by simple majority; an emergency lasting beyond two seasons requires annual Assembly renewal thereafter | Temporal limit + democratic renewal mechanism = legitimacy-sounding check on unlimited emergency rule | Article 19 must define the voting mechanism; Article 4 (Mayor's ordinary authority) should remain consistent with these emergency powers being genuinely extraordinary, time-bounded exceptions |
| During emergency: Mayor may order extended work, redirect resources between departments, restrict floor movement; Judicial may expedite trials but cannot exceed standard sentences or authorize cleaning without Mayor's written order | Powers are named and scoped, rather than blank-check; Judicial-over-cleaning is a deliberate check on the Mayor's emergency authority | Article 6 should be consistent with expedited trials (same sentences, just faster procedure); Article 17 (Cleaning) should note that emergency-authorization requires this specific written order |
| **The green list is Order-restricted and not subject to citizen review (RESOLVED 2026-09-03)**: maintained by Mayor and Department heads, updated annually, kept in secure archive under Article 20, with specific contents and updates determined solely by the Mayor and Heads of Departments | Emergency protocol document exists, is real, but is Order-level secret — gesture-without-specifics principle applied to emergency procedures | Article 20 (Records) should acknowledge the green list exists in the archive without describing its contents; Article 15 (Forbidden Speech) should remain consistent with citizens not being authorized to speculate about, investigate, or publicize emergency protocols |
| A citizen ordered to follow green-list protocol during emergency must obey as though it were a standing Mayor order; may refuse/delay only if Judicial rules after emergency that the order was not genuinely required | Obedience-with-accountability model; consistent with Article 6's post-hoc review authority | Article 16 (Crimes) should treat disobedience of emergency orders as an offense (probably mines-tier if the citizen genuinely didn't believe it was necessary; gravest if recklessly disobeying a clear order); Article 21 §5 already covers the post-emergency Judicial review that provides legitimacy |
| A citizen's final request under Article 17 may be held in abeyance (not suspended) during gravest emergency; citizen may renew request after emergency ends, or petition Judicial if emergency no longer poses genuine threat; deaths occurring in abeyance are recorded with the request marked unfulfilled-not-denied | Preserves the citizen's ultimate right while allowing silo-survival priorities to take precedence — consistent with Article 1's survival-is-paramount framingness | Article 17 should remain consistent with final requests as a genuinely-honored right, not something lightly abeyanced; Article 2 (Census) should treat abeyance notations as part of the historical record |
| After emergency, Judicial reviews whether emergency orders were necessary; unnecessary or excessive orders may trigger compensation to affected citizens | Post-hoc accountability mechanism; consistent with Article 6's ruling authority and the Pact's general "no secret governance" tone | Article 16 should be consistent with this review process existing, so emergency-order enforcement isn't treated as immune from later challenge; Article 4 (Mayor) should not interpret emergency authority as granting immunity for patently irrational orders |

## Established facts (from Article 15, "Of Schooling and the Teaching of the Young")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| **Article 15 written 2026-09-03, filling the slot lost when Mines was inserted as Article 10** (see `REVIEW.md` A1); Articles 15--22 renumbered to 16--23 (Public Order 16, Crimes 17, Cleaning 18, Health 19, Assembly 20, Records 21, Emergency 22, Amendment 23) to make room | Restores the OLD/intended cross-reference scheme that Articles 1, 2, 6, 7, 8, 10, 11, and 16 already assumed | `REVIEW.md`'s A2 mechanical cross-reference pass is still outstanding for the files that used the interim NEW scheme or a mixed one (Articles 3, 4, 5, 9, 12, 13, 14, 17, 19, 20, 21, 22, and the Amendment Log) — do not assume the rest of the draft is internally consistent yet |
| Schooling runs from the third naming-day (nursery) through the sixteenth (majority): schoolroom proper from the sixth naming-day, the Article 1 founding recitation completed by the eighth, Article 13's aptitude testing from the twelfth, and an optional season-length trial placement (not a shadowing) in a citizen's final two years | Gives Article 2's naming-day-reckoning promise ("schooling under Article 15... is reckoned from it") concrete content, and lets a child's aptitude testing under Article 13 land on an already-informed citizen | Any later Article touching child-rearing or household composition should stay consistent with children being at the schoolroom on ordinary working days from age six |
| **Added 2026-09-04**: the sixth naming-day is now formally named "the age at which a child is judged to have reached basic societal awareness" (Article 15, Section 2) | TV-sourced (`CANON.md` §18, confirmed by the user against the show, attributed to Bernard); happened to confirm a number this project had already independently chosen for the schoolroom-entry threshold, rather than requiring any renumbering | No other Article needs to change; any future Article referencing why formal schooling (as opposed to nursery-keeping) begins at six now has this term available as the stated, civic-sounding rationale |
| Teaching the young is confirmed as a full-shadowed, order-adjacent trade under Article 13 Sections 5 and 7, subject to the same ongoing vetting as other order-adjacent trades; a School Aide (short shadow) may assist but not teach the founding recitation or course of study unsupervised | Implements `PROFESSIONS.md`'s flag that Teacher is "the single trade this project's deep lore... makes most sensitive" without ever stating why | Article 13 needs no changes — Article 15 only invokes the vetting machinery already there; keep any future critical-roles Article consistent with Teacher staying on that list |
| Article 15 Section 3 fulfills Article 1's forward promise and Article 16 Section 3's back-reference: the founding recitation is taught complete and unembellished before the eighth naming-day, a child's questions beyond it are answered only in Article 1's own words, and a teacher who invents detail and teaches it as fact offends gravely under Article 16 Section 3 | Closes the loop `FACTS.md` previously tracked as "strong candidate to keep in mind for Article 14 (Schooling)" (see the Article 16/Public Order entry above) | No further action — the cross-reference is now live in both directions |
| A child is a ward under Article 2 Section 1 with no standing to petition Judicial directly; ordinary schoolroom correction is the teacher's own charge and not an Article 17 offense; a grave breach by a child is heard by Judicial with the household present and the child's years weighed, short of the gravest offenses | Keeps children inside the Pact's ordinary machinery (no separate juvenile code invented) while accounting for their non-citizen procedural standing under Article 2 | Article 6 (Judicial) and Article 17 (Crimes) should remain consistent with this being the sole treatment of offending minors; no other Article should independently invent a juvenile process |
| **Deliberate uninterpreted seam**: a teacher who observes "persistent distress," "defiance of correction beyond the ordinary," or "a fixation upon some matter this Pact does not teach" in a child must report it to the Head Physician (Article 19) or Judicial; framed as child welfare, but the third ground is close to content-based ideological monitoring of children | Plays the same "three readers" role as Article 16's overhear-and-report duty (see above) and the Section 3 forbidden-history rule: read as care by the citizen, read as chilling by the close reader, understood by the book reader as the Pact quietly defending against the exact mechanism that already reset a silo once (`CANON.md` §9) | Keep this clause as understated as it is — do not have any later Article explain or resolve what "fixation" means; the ambiguity is the point |

## Established facts (curiosity-neutralization mechanism, added 2026-09-04)

User-directed addition, extending the Article 15 §7 "fixation" seam (above) from children to adults, via two independent, individually-plausible, never-explicitly-connected levers rather than one named rule against curiosity itself.

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| **Resource-waste framing (Article 13, Section 1)**: a citizen who neglects assigned labor or diverts tools, materials, or owed labor-time to "a private study, pursuit, or fixation of the citizen's own devising" is first corrected by the citizen's own Head of Department (oversight or reassignment), and referred to Judicial if the neglect persists | Purely a labor-economics rationale on its face — consistent with Article 13's existing "labor is owed to the silo as a debt of citizenship" framing, and deliberately worded to apply to any private pursuit (a hobby craft no less than a forbidden line of inquiry), not just intellectual curiosity specifically, so the clause reads as ordinary workplace discipline and never names its real target | Article 17 Section 3 (mines-tier catalog) now includes "willful and persistent neglect of assigned labor" referred under this clause as a defined offense, closing the loop |
| **Welfare framing (Article 19, Section 6)**: a Physician who observes "a persistent fixation upon some matter this Pact does not teach or require," carried to the neglect of the citizen's own health, household, or labor, may refer the citizen to Judicial for evaluation, at the Physician's own discretion; the referral is not a charge and leaves no record beyond the referral and its resolution | Direct adult analogue of Article 15 §7's child clause, using the same discretionary (not mandatory), non-punitive, welfare-coded structure as the existing self-harm referral in the same section — consistent with Victor's psychologist fingerprint (`CANON.md` §17a) and the "hollow due process" pattern (indefinite "evaluation" rather than a clean, appealable sentence) | Keep both levers independent and never state in any Article that they exist to catch the same underlying concern — the plausibility of each depends on neither ever being framed as a proxy for the other |
| Together, these two clauses mean a citizen "too intellectually curious" for comfort can be neutralized via either an ordinary-sounding labor-discipline route (Article 13 → Article 17, mines) or an ordinary-sounding health route (Article 19, indefinite evaluation) without either ever naming curiosity as the offense | Two independently-plausible, converging mechanisms is more consistent with Victor's design (per `STYLE.md`'s Founders' psychology principles) than a single named rule would be, and mirrors the real emergent-not-stated technique already used for Judicial's supremacy over the Sheriff (`HYPOTHESES.md` entry 4) | Any future Article touching labor discipline or Infirmary referral should preserve this duality rather than consolidating it into one explicit clause |

## Established facts (Forgiveness Holiday, added 2026-09-04)

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| **The Mayor may declare a Forgiveness Holiday (Article 4, new Section 7)**: for a duration and on notice the Mayor sets, a citizen who surrenders a relic or restricted instrument under Article 16 during the holiday is not answerable under Article 17 for the mere keeping, making, or use of the thing surrendered; the thing itself is still classified and, if gravest-tier, still destroyed or sealed under Article 16 | Framed as a self-executing Pact-level grace (like the Article 17 first-offense grace), not as a Mayoral order commanding Judicial's charging discretion — this avoids conflicting with Article 4 §4's existing rule that "the Mayor's orders do not bind Judicial's investigative or charging decisions." Utilitarian logic (`STYLE.md`'s Founders' psychology): recovering hidden dangerous material is worth more than punishing after-the-fact possession, the same reasoning behind any real-world amnesty | Article 16 §4 now cross-references this power; any future Article touching relic surrender or Judicial's charging discretion should preserve the "grace is a standing rule of this Pact, not a case-by-case command" framing, so it never contradicts Article 4 §4 |
| The grace covers only the surrendered item's own keeping/making/use, not any other offense the surrender or its examination reveals; a holiday's start and end are both publicly announced, and a surrender after the holiday ends receives no grace | Keeps the amnesty narrow and legible rather than a general confession-immunity, consistent with the Pact's usual "sounds protective, narrowly scoped in practice" pattern | None yet drafted — a candidate site for a future Amendment Log entry (e.g. an amendment narrowing or restricting how often a Holiday may be declared) |

## Established facts (pedantic-procedural camouflage device, added 2026-09-04)

A new, distinct authorial device from the existing "gesture without specifics" one (`STYLE.md`): instead of saying *less* around a secret, these clauses say *more* about surrounding mundane procedure, so the one sentence that matters is buried in a run of bureaucratic specificity rather than left as a conspicuous gap. User-directed; per `STYLE.md`'s Restraint principle, used at exactly two sites this pass, bringing the project's total count of this general class of "oddly over-precise Victor tell" to three (the pre-existing Article 8 §2 double-recorded license roll, plus these two) — **do not add a fourth without deliberately reconsidering whether the device is still rare enough to work.**

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| **Article 18 §4 (The Airlock and the Departure)**: the wool-pad count is now pedantically bounded ("no fewer than three and no more than five," logged by number issued and remaining), and the gas flush is now wrapped in a chain of hour-stamps and countersignatures between the escorting Officer/Sheriff and the Information Technology technician, so that "a gas Information Technology alone administers and this Pact does not further describe" reads as one procedural fact among several, not a singular unexplained omission | This is the single most Order-sensitive sentence in the whole Pact (canon: the "inert gas" is actually seal-degrading nanobots, `CANON.md` §8) — the padding exists specifically to keep a casual reader's eye moving past it | Any future Article revisiting the cleaning procedure must preserve this specific sentence unaltered in substance; the surrounding procedural detail may be trimmed or expanded freely, since it carries no independent meaning of its own |
| **Article 19 §4 (Death and the Determination of Cause)**: an ordinary death now requires a pedantically specific "Form of Death" (name, naming-day, floor and hour found, Physician's name, finding, "in that order and no other"); a cleaning-death is then handled by a single clause noting the Form "is not completed" and Information Technology certifies instead, by its own unaudited record | Buries the Article 2 Structural Fragility crack (IT's word alone closes a cleaning-death, no independent check) inside what now reads as a mere administrative exemption from a form, rather than a conspicuous absence of oversight | Preserve the Form of Death's exact field order if this section is revisited — the specificity is the camouflage; do not let it accumulate real narrative significance of its own, or it stops being disposable procedural noise |

## Established facts (named propaganda techniques drafted in, added 2026-09-04)

User-directed: three specific propaganda techniques (testimonial appeal, bandwagon/universal-compliance framing, and a loaded virtue-term for the compliant citizen) drafted into the text, chosen from a broader survey of techniques already present versus absent.

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| **Loaded virtue-term "sound" (preamble)**: "A citizen who keeps this Pact in full is sound, in the same word and the same sense a wall or a seal is sound" — coins a positive-virtue counterpart to "offender," reusing the preamble's own existing hull/vessel/seal imagery | Propaganda technique: naming the loyal citizen with a virtue-word is as persuasive as naming the deviant with a vice-word, and the Pact previously had vocabulary only for the latter | Deliberately given only one high-visibility appearance, in the ritually-repeated preamble (per its own `articlenote`, read aloud at namings, Mayoral seatings, and school-year openings) rather than forced into other Articles — a single strong appearance in repeated liturgy is more realistic propaganda design than scattering the term everywhere; a future Article may reuse "sound" if it arises naturally, but should not manufacture an occasion to do so |
| **Bandwagon framing (Article 2 §3, the Citizen's Oath)**: the oath is now "the same oath every citizen before them has sworn, without exception, since the first citizen stood where they now stand" | Universal-compliance claim, deliberately unfalsifiable given the project's own founding-timeline ambiguity (`FACTS.md` open item 1, resolved to leave the founding date unstated) — the vagueness about how long ago founding was makes the claim sound grand without being checkable, a small bonus consilience with an already-locked project decision | None required; this is a self-contained rhetorical addition |
| **Testimonial appeal (Article 3, Section 6, "The Duty to Maintain the Population")**: an anonymized citizen's account of losing a lottery-window child, and coming to affirm the lottery's necessity anyway, added as a new paragraph before the existing clauses | Attributed to Anna Thurman's register (`CANON.md` §17b, `STYLE.md`) — kinship/grief-adjacent, sincere-sounding, functions as legitimizing camouflage per the existing "Anna's sincerity is not a counterweight to Victor's cruelty" principle, without being explicitly flagged as such in-text | Consistent candidate register for any future testimonial-style addition (Articles 3, 14, 19 remain Anna's assigned territory) — keep such additions anonymized ("though not by the name of the household") rather than named, matching the Pact's existing practice of never individually naming ordinary citizens in its own text |

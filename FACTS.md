# Facts ledger — coherence & consilience tracking

**Purpose**: it is a guiding principle of this project that the Pact be
highly coherent and consilient — every fact it asserts or implies should
have its downstream consequences worked out, and every rule should have a
worked-out *explanation* (even if that explanation never appears in the
Pact's own text), so that later Articles never quietly contradict earlier
ones. This file is the running ledger that makes that checkable rather
than just aspirational.

> **Numbering note (2026-09-06).** Tables are headed by the Article's *current*
> number and title. Cell text written before the Mines (Article 10) and Schooling
> (Article 15) insertions may cite a number one or two lower than current; where a
> number is paired with a name, the name is authoritative. Current numbering:
> 10 Mines, 11 Supply, 12 Commerce, 13 Labor, 14 Housing, 15 Schooling,
> 16 Public Order, 17 Crimes, 18 Cleaning, 19 Health, 20 Assembly, 21 Records,
> 22 Emergency, 23 Amendment.

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
  - **2026-09-06**: Article 21 §5(a) and Article 23 §3(a) still required each
    amendment to carry "the date of ratification," contradicting the Log's own
    preface; both now fix an amendment's place by order of ratification alone.
    Article 18 was also brought into line: the request formula is now the canon
    "I want to go outside" (Holston and Allison in *Wool*), §1 no longer says a
    requester leaves the rolls (§1(d) keeps them in until IT's word), and §2's
    "not a death sentence; it is an exile" and "not condemned as a murderer"
    lines are gone (the Pact now says of the outside only "the world above, as
    Article 1 records it, and this Pact says no more of it than that").

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
| Article 1 §1(b) now reads "it will last only so long as those who come after keep faith" (2026-09-06; was "it has lasted because those who came after kept faith") | Founding-document rule, open item 1 | The only remaining deliberate timeless-liturgy claim is Article 2 §3's oath line, which is unfalsifiable by design |
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
| **§7(a) reworded (2026-09-06)**: hidden systems are those "the builders installed within the silo's deepest works," named as intake/drainage systems and bypass conduits only; "contingency passages" and "including but not limited to" removed | "Below the builders' deepest works" contradicted §4(b)'s absolute depth limit (who dug them?), and a public Pact announcing hidden *passages* invites the curiosity it forbids | Keep §7's list to systems, never passages; the Safeguard-visibility design of the 2026-09-03 resolution is unchanged |

## Established facts (from Article 10, "Of the Department of Mines")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| Head of Mines is raised up via shadowing (Article 12) from within Mines' own trades, confirmed by the Mayor | Consistent with the general Department-head succession mechanism (Article 9, 11, etc.); identical to the pattern | Article 12 shadowing mechanism must include Mines trades as shadowing-eligible; Article 4/5 (Mayor/Succession) continue to treat "confirms Heads of Department" as a real Mayoral power |
| Mines is led by a distinct office (Head of Mines), separate from the Head of Mechanical | Resolves `FACTS.md` open item 3 via explicit user choice and full Article 10 drafting | All Articles that reference "Head of Mechanical" must not mistakenly include Mines under that title; Articles involving mines-as-penal-labor (17) must be checked for consistency (currently framed as Mechanical's charge, but the two departments' administrative relationship needs texture) |
| The winning of ore in the workings below the Down Deep is Mines' standing charge, requiring no order for ordinary continuation | Ore extraction is Mines' *primary* function, not a secondary charge of another department | This is the clean inverse of Article 9's revised charge: Mechanical processes ore (at metal-working) but doesn't extract it; Mines extracts but doesn't process |
| No working of ore may run beyond two hundred feet from the silo's own structure, in any direction | TV-sourced (Head of Mines Ed Harwood's Season 3 line, "never out... not more than two hundred feet, because the Pact says so"); same engineering-knowledge/escape-containment logic as the magnification and mechanized-transport bans, applied to radius instead of optics or motors — see `HYPOTHESES.md` entry 5 | Consistent with, doesn't contradict, Article 9's absolute depth prohibition (which caps vertical depth at what the builders reached; this caps horizontal radius separately). Any future Article touching escape-capacity containment should reference this limit consistently with the other "designed-in caps" (freight lift logging, IT monopoly, sensor ban, etc.) |
| Any mining beyond the 200-foot limit is "among the gravest offenses" under Article 17 | Encodes the Founders' judgment-without-explanation, consistent with `HYPOTHESES.md` entry 5's reasoning (the radius is an engineering-knowledge/containment decision, paralleling why magnification and mechanized transport are restricted) | Article 17 needs "mining beyond the 200-foot radius" as a defined gravest offense; Article 18 (Cleaning) should stay consistent with this being a top-tier punishment territory |
| The Head of Mines and the Head of Mechanical shall meet at least once per ten days to coordinate workings and structural concerns | Pragmatic coordination between two Down Deep departments, codified as a standing duty, not a suggestion | This is the first Pact clause explicitly requiring recurring formal coordination between two Department heads — a small but real detail texture for the bureaucratic register |
| **Sentenced labor (added 2026-09-06, §2(e))**: a citizen sentenced to the mines under Article 17 labors under the Head of Mines, is counted as assigned to Mines for Article 10's purposes (so §2(d)'s entry bar doesn't exclude them) but not Article 13's (not a trade, not shadowed), works under the same supervision/shoring/200-foot limit, is lodged Down Deep under Article 14, and the Head of Mines reports each sentenced citizen's labor and condition to Judicial each season | Resolves the orphaned penal-labor tier: Article 17 §3(a) previously still said "Head of Mechanical" and Article 10 never mentioned sentenced citizens | Article 14 §2(a) (only Mechanical/Mines trades dwell Down Deep) is consistent since the sentenced citizen is "assigned to Mines"; `PROFESSIONS.md`'s "sentenced, not shadowed" framing holds |
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

## Established facts (from Article 3, "Of Marriage, the Lottery, and the Right of Birth" — partial, added 2026-09-06)

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| **Slot count is death-pegged (2026-09-06)**: §2(b) sets the year's slots at the number of names closed under Article 2 since the last drawing, "and no more"; the Mayor with the Heads may set it *lower* for stores or capacity, never higher; §6(b) says the same | Reconciles Article 2 §5 ("this closing, and no other event, opens a place in the lottery") with Article 3's Mayoral slot-setting, which previously read as an independent capacity number. Canon: population is a closed loop, birth pegged to death | Any later Article touching population must treat closed names as the ceiling; the Mayor's power here is only downward |
| **The lottery testimonial is no longer founding text**: the "It is recorded... a citizen who waited three years" paragraph was moved out of Article 3 §6 and into the Amendment Log as **Amendment 2**, a citizens'-petition amendment "in the generation after Amendment 1," with the Judge ruling that a citizen's words may enter the Pact provided the household is unnamed | A founding document cannot record a post-founding Assembly (open item 1's rule). As an amendment it becomes the first Amendment-Drift specimen in the early Log: a later hand reproducing Anna's kinship register as sincerity-as-camouflage | The Log is now Amendments 1–10 (old 2–9 renumbered 3–10; old Amendment 8's "ratified last" claim corrected to "late"); Article 3 removed from the Unamended Provisions list; `REVIEW.md`'s old Amendment numbers are historical |
| **Register pass (2026-09-06)** across the book: all "(s)" forms in Article 3 rewritten ("the citizen or citizens"); Article 3 §3(b) now points at Section 4 (was a self-reference to Section 3); every bare Unicode em-dash replaced with spaced `---`; parentheticals in Articles 4, 13, 14, 19, 20 converted to apposition or colon lists; "fraudster," "spot-checked," "waiting list," "infinite servitude," "monopolize," "rational," "backmatter," "this edition" replaced; Article 15 §§4–8 given lead paragraphs; Article 23's epigraph cut to one line; Article 18 §6 no longer speaks in essay voice and §3(c) no longer sends a citizen out without a suit (refusal is recorded, departure proceeds); Amendments 9 and 10's Effect notes no longer editorialize about IT | `STYLE.md` register rules and `REVIEW.md` F1–F5 | The Amendment Log's compiler voice must stay deadpan; reader-3 irony comes from what the record omits, never from the compiler saying so |

## Established facts (from Article 4, "Of the Office of Mayor")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| Mayor is the civilian head of the silo, confirmed per Article 5, answerable to the Assembly under Article 20 | First executive office; loads forward into succession design (Article 5, primary Structural Fragility site) | Articles 5 and 20 must be consistent with Mayor's tenure and removal; no other Article should claim executive authority over the Mayor's ordinary decisions |
| **Five-year term (added 2026-09-06)**: the Mayor holds office five years from confirmation, continues until a successor is confirmed, may stand again; removable within a term by the Assembly | TV-sourced, semi-authorial (the show's prop Article 4: "one elected every five years," "no fewer than two candidates"); closes `REVIEW.md` B5. A fixed term also makes the Article 5 vacancy-election gap sharper: the term-end election has a fixed occasion (the fifth-year ordinary Assembly, which the sitting Mayor convenes), the vacancy election has none | Article 5 §3 now covers both cases; Article 20 §4 has a term-end election clause; the Deputy's office ends with the appointing Mayor's term (Article 5 §1) |
| Mayor confirms Department heads (Mechanical, IT, Supply, Mines, etc.) upon their recommendations via shadowing (Article 13) | Extends the shadowing/confirmation mechanism as a standard pattern across all Departments | Article 13 shadowing must include provision for heads recommending their shadows; heads remain removable only via Judicial finding + Assembly removal (Article 20) |
| Mayor appoints the Sheriff (not via shadowing, not bound by recommendation) at Mayor's sole discretion, "weighing" advice from outgoing Sheriff but not bound by it | Corrects earlier canon misconception; follows the Juliette precedent (Mayor's real discretion, not a rubber stamp over a groomed Deputy). Establishes "appointing authority's judgment is final and not bound" as a pattern for leadership offices — precedent for Article 5 Structural Fragility design | Sheriff's office remains distinct from other Department-head succession; Article 7 already treats Deputies as shadowed subordinates, not as heirs-apparent to the Sheriff's office |
| Judge is confirmed jointly by Mayor and Assembly (not just Mayor), standing once in lifetime until death/removal by the same two bodies — highest bar for any office | Extra-legitimacy-sounding process, consistent with canon; creates dramatic irony since this process is known (via canon) to not prevent Judicial capture by IT/Bernard | Article 20 must include the mechanism for Assembly confirmation and removal votes; Article 6 already established the Judge's office |
| Mayor and Judicial are co-equal in authority, neither binding the other's Pact-given powers | Establishes a real separation of powers, not a hierarchy | Article 20 must treat Mayor-Judicial disputes as Assembly-level matters, not subordination; Article 22 (Emergency) should clarify emergency authority doesn't subordinate either office |
| **The Syndrome (eligibility rule) — from TV prop transcription (2026-09-03); consolidated 2026-09-06** [TV, semi-authorial]: the single blanket rule now lives in **Article 13 §6(e)** (bars every public office — Mayor, Deputy, Judge, Sheriff, any Head — and every critical role; report to the Head Physician and resign at once; successor named as the office's own Article provides). Article 19 §7(b) carries the medical description ("a wasting of the nerves... neither inherited nor passed from one citizen to another") and cross-references 13 §6. Articles 4, 5, 6, 7, and 8 each keep one short clause: the office "is barred to a citizen afflicted with the Syndrome, and vacated by it, as Article 13, Section 6 provides," plus that office's own successor route | Matches the show's Article 5 as one rule rather than seven copies; the office Articles keep only what differs (who succeeds) | Any new office Article should use the same one-line cross-reference form; never restate the bar in full again |
| Deputy Mayor resides in Up Top, has access to Mayor's records for preparation, becomes acting Mayor in absence (with all powers except permanent appointments) | Succession preparedness, plus a real barrier (no permanent changes without permanent succession under Article 5) | Article 5 must elaborate when/how Deputy's temporary acting becomes permanent; Article 20 can reference the distinction |
| **Forbidden-speech offense (Article 16 §1) explicitly added to Article 17 §3 as mines-level offense** | Clarifies that forbidden-speech is not a gravest offense; offenders get pre-sentence Judicial hearing per Article 6 | Article 6 updated (2026-09-02) to specify what a pre-sentence hearing includes: accused citizen may speak, call witnesses, dispute Officers' account; Judge hears all before sentencing |

## Established facts (from Article 5, "Of the Deputy Mayor and the Order of Succession") — added 2026-09-06; the PRIMARY STRUCTURAL FRAGILITY SITE

These rows record the design deliberately. **Do not "fix" any of them** without reconsidering the Structural Fragility principle (`STYLE.md`) and the [[article5_structural_fragility]] memory.

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| **The Deputy's office may stand empty.** §4(a): a Deputy is appointed "at any time the sitting Mayor judges needful"; nothing obliges a Mayor to keep one. §1: the Deputy's office ends with the appointing Mayor's term | Reads as ordinary executive discretion. Stated rationale: the Mayor knows best whether a Deputy is needed. True rationale (Victor): a mandatory Deputy creates a rival power center; an optional one keeps the Mayor's office weak and the fallback rule live | This is the first half of Bernard's canon path (Jahns had no Deputy Mayor). No Article may ever require a Deputy to be appointed |
| **Fallback acting Mayor is the senior Department head** (§4(b)): "determined by the order of their first confirmation in office," when both Mayor and Deputy are gone or the Deputy office is empty | Sounds like a neutral seniority rule. But the Head of IT's succession under Article 8 §6 "stands as though confirmed" without a vote, so a long-tenured IT Head is very likely the senior Head; and IT is the office least accountable to the Mayor | The second half of Bernard's path (book: Head of IT is next in line). Article 8's insular succession must stay as it is; no Article may add a Mayoral-confirmation vote for the IT Head |
| **Asymmetric bar on standing**: §3(a) bars a *Deputy* acting as Mayor from standing for election; a *Department head* acting under §4(b) is not barred | Stated rationale: impartiality of the acting office. The clause was drafted for the Deputy and never extended, which is exactly the kind of seam a close reader (or an IT Head) can find | Intentional. Do not extend §3(a) to §4(b) acting Mayors |
| **A vacancy election has no deadline** (§3(d)): the Assembly sets "the timing and manner" *in consultation with the acting Mayor and the Heads of Departments*; the term-end election, by contrast, has a fixed occasion (the fifth-year ordinary Assembly, Article 20 §4) | Reads as procedural reasonableness. In practice the acting Mayor controls Assembly convening (Article 20 §1: Mayor, one-fifth petition, or Judicial), and a one-fifth petition of several thousand citizens with no radio (Article 8/21) is slow | The locked crack per the [[article5_structural_fragility]] memory. Article 20 must never add a vacancy-election deadline; Article 21's porter-only word rule is load-bearing here too |
| Acting Mayor may not make permanent appointments of a Department head or the Judge (§2(b)), but a Department head acting as Mayor is already a Department head | A real limit for a Deputy, near-meaningless for the fallback case | Consistent with the asymmetry above; leave as is |
| No Syndrome carve-out interacts with succession: a Mayor who resigns for the Syndrome (Article 4 §1(d)) triggers the same §2 assumption | — | — |

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
| **Housing is an office within Supply (settled 2026-09-06)**: Article 11 §1(c) creates it (short-shadowed keeper, answers to the Head of Supply, reports floor/household changes to Judicial under Article 2); Article 14 §1 names it as the administering office, with the Head of Supply's approval required for every assignment | Articles 2 and 3 named "Housing" as a reporting body while Article 14 gave everything to the Head of Supply; making Housing a named office of Supply satisfies both and `CANON.md` §12's dedicated Housing office [TV] without inventing a new Department head | "Housing" in Articles 2, 3, 14, 19 now all mean this office; do not create a Head of Housing |

## Established facts (from Article 17, "Of Crimes and Their Punishments")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| **The three-tier punishment scale is now canonical**: grace (formal warning, once per citizen lifetime, for non-gravest offenses only) → the mines (labor sentence, second offense or a first offense the Judge finds too grave for grace) → cleaning (Article 17, gravest offenses only, no grace, no hearing, no commutation "whatever representation is made under Article 6") | Directly implements `CANON.md` §18's mines-tier research — previously-missing structure, now filled in | Article 17 must be consistent with cleaning as strictly the top tier, never used for mines-level offenses; Article 6's due-process split (hearing for non-gravest, none for gravest) now has its offense catalog to operate on |
| **The mines are framed as pre-existing "deep workings below the Down Deep," administered by the Head of Mechanical** — deliberately *not* framed as citizens digging new passages | Resolves a real potential coherence conflict: Article 9's digging prohibition is absolute ("regardless of purpose, curiosity, need, or claimed emergency") with no stated exception for mine labor — framing the mines as already-existing builder-provided workings (consistent with Article 1's "deep storage of the silo's reserves" already being Down Deep/Mechanical's charge) avoids a contradiction rather than creating one | If Article 9 or 21 is ever revisited, keep the mines described as existing infrastructure, not an exception to the digging ban |
| **Gravest-offense catalog closed out**: sensor tampering (Art. 1), generator/water-air/reclamation interference (Art. 9), false life/death attestation (Art. 2), and any relic Article 15 classifies among the gravest | Consolidates every "among the gravest offenses under Article 16" forward-reference made by Articles 1, 2, and 9 into one place | Article 15 now has a **new firm promise**: it must define a relic classification system with at least a "gravest" tier (matching the show's "red-level" relic — `CANON.md` §18) for this clause to resolve cleanly |
| **Catalog completed and made closed (2026-09-06)**: §4 now reads "the following, and no others save as this section provides" and adds: interference with Article 9 §7 systems, including by the keeping of a dwelling under Article 14; a false finding of cause of death and a physician's failure to carry a suspected self-killing to Judicial (Article 19 §4); working ore beyond the Article 10 limit; counterfeiting, knowing possession of a counterfeit, and theft of or tampering with blank chits (Article 12); intent to kill or maim (Section 5); restricted instruments Article 16 classifies gravest | The previous list omitted seven offenses other Articles had already named gravest, so the "closed out" row above was false | Any future Article that names a new gravest offense must add it here, or route it through the Judge's ruling power in §4(a); §3(a) now names the Head of Mines, not Mechanical |
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
| **Section 6 reframed (2026-09-06)** as "The Apparatus of the Silo's Keeping": IT (Article 8) and Mechanical (Article 9) keep apparatus for monitoring the silo's *vital systems* (air, water, generator load, official wire) "and such further instruments as either Department's charge requires"; no citizen may interfere with it "whether or not the citizen knows its purpose"; interference is an Article 17 offense, gravest only where it reaches Article 9's works or Article 1's sensors; neither Department must say where apparatus is kept or how it is read | The previous draft openly announced IT surveillance apparatus throughout the silo, contradicting canon (the hidden cameras are secret; their discovery is a plot point) and Victor's method. The reframe makes the citizen read "utility sensors," the close reader notice "such further instruments" and "whether or not the citizen knows its purpose," and the book reader know what those are | Amendments 8 and 9 still cite Article 16 §6 and remain coherent with the new wording (report-to-IT-first; "tampering with a monitoring device"); no Article may ever name observation, surveillance, or cameras as the apparatus's purpose |

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

## Established facts (from Article 21, "Of Records, Porters, and the Post" — partial, added 2026-09-06)

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| **Section 3 rewritten (2026-09-06)** as "Official Word by Wire and Radio": wire/radio carries word only between the Mayor, the Sheriff, Judicial, and the Heads of Department, through IT's stations; every such word is logged (sending office, receiving office, hour) and the log delivered to Judicial; whether content is kept is IT's own charge and not set down; a citizen's private word between floors goes by porter and no other means, and an officer who sends it (or a citizen who asks) is answerable under Article 17; in emergency the Mayor's order may pass by radio only to the Deputy/Peacekeeper at a landing, who carries it on by foot | The previous draft gave every citizen a chit-fee radio Post office with IT-run encryption, contradicting Article 8 §3, canon (citizens have no radio access), and `HYPOTHESES.md` entry 2's reason porters exist | Article 8 §3 and Article 7 §2(b) (porter right-of-way) now hold without exception; Article 20 §2(a)'s radio relay of Assembly proceedings is official use and stays consistent; the rest of Article 21 (archive, porters, freight-lift log, Amendment Log) still owes this ledger a table |

## Established facts (from Article 22, "Of Emergency and the Suspension of Ordinary Law")

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| An emergency exists when the silo faces threats to survival: catastrophic system damage, disease, or other jointly-determined threats; declared by Mayor with Judicial challenge-right (if challenged, Judicial rules finally) | Co-equal emergency-declaration power, with Judicial as a check rather than rubber-stamp | Article 5 (Succession) should be consistent with Mayor's emergency role not creating an excuse for acting outside ordinary succession rules; Article 19 (Assembly) must define ratification procedures for emergencies lasting beyond one season |
| Emergency suspends ordinary Pact procedures for up to one season; beyond one season requires Assembly renewal by simple majority; an emergency lasting beyond two seasons requires annual Assembly renewal thereafter | Temporal limit + democratic renewal mechanism = legitimacy-sounding check on unlimited emergency rule | Article 19 must define the voting mechanism; Article 4 (Mayor's ordinary authority) should remain consistent with these emergency powers being genuinely extraordinary, time-bounded exceptions |
| During emergency: Mayor may order extended work, redirect resources between departments, restrict floor movement; Judicial may hear and judge with emergency swiftness (a non-gravest hearing may be shortened but not refused), but no measure beyond Article 17's may be given and **no non-gravest offense may be answered by cleaning, whatever order any office gives** (revised 2026-09-06; the earlier "without the Mayor's written order" exception contradicted Article 17 §1(a) and Article 18 §6(a)) | Powers are named and scoped, not blank-check; the cleaning bar is absolute in emergency exactly as in ordinary times | Article 6 should be consistent with shortened-but-not-refused hearings; Article 17 §1(a) and Article 18 §6(a) now hold without exception |
| **The green list is Order-restricted and not subject to citizen review (RESOLVED 2026-09-03; wording fixed 2026-09-06)**: maintained by the Mayor with Judicial and the Head of every Department, updated yearly *before* the ordinary Assembly, where only the fact of its updating is reported; kept in the Judicial archive under Article 21; defined by apposition ("a protocol, called the green list"), no scare quotes. §4 is now titled "The Holding of a Final Request in Abeyance" and uses "hold in abeyance" throughout, and Article 18 §1(b) carries a matching "save only where Article 22 provides" | Emergency protocol document exists, is real, but is Order-level secret — gesture-without-specifics principle applied to emergency procedures | Article 20 (Records) should acknowledge the green list exists in the archive without describing its contents; Article 15 (Forbidden Speech) should remain consistent with citizens not being authorized to speculate about, investigate, or publicize emergency protocols |
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

## Established facts (from Article 12, "Of Trade, Chits, and Commerce") — added 2026-09-06

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| Chits are issued by the silo through Chit-Keepers (Mayor-appointed, overseen by the Head of Supply) who keep a master roll of chits issued and a ledger of every citizen's balance | Every citizen's surplus is legible to Supply and the Mayor (`HYPOTHESES.md` 10) | No Article should give any other office a chit ledger |
| Labor is owed, not bought (Article 13 §1), but is *paid* in chits at Department-set rates; the mines pay nothing; retirees get a sustenance in chits via Supply on Infirmary certification | Chits are a comfort ladder above the flat ration, never a substitute for it | Article 11's ration is never priced in chits |
| Counterfeiting, knowing possession of a counterfeit, and theft of blank chits are gravest (now in Article 17 §4) | Trust in the ledger is load-bearing | — |
| Prices are free between citizens; Judicial alone may reverse an unjust transaction; the Mayor may cap prices only under Article 22 | Preserves Article 4 §4's Mayor/Judicial split (`REVIEW.md` D4) | — |
| Debt is recorded by the Chit-Keepers, enforceable by Judicial, ends at death, never inherited; no servitude for debt | — | Article 17 restitution "in chits, goods, or labor" is an order of Judicial, not a debt |
| Market Clerk: short-shadowed, appointed by Mayor or Head, first-instance for price and commission disputes, then Judicial | Closes `REVIEW.md` G3 | — |

## Established facts (from Article 13, "Of Labor, Shadowing, and the Assignment") — added 2026-09-06

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| Three tiers of entry: full shadowing (3–7 years, master's sole determination), short shadowing (4 weeks to one season, two in exception), direct assignment (no shadowing) | Implements `PROFESSIONS.md`'s Shadow axis | Any new trade must be assigned a tier |
| A citizen petitions a trade; the Head may refuse (appeal to Judicial); compelled assignment needs Mayor + Head jointly + Judicial confirmation that it is not punishment | Choice-within-constraint, with Judicial as the legitimacy check | Articles 9 §6(b) and 10 §5(b) reuse this |
| Critical roles (IT technicians, sensor/wallscreen, cleaning-lab, teachers, Officers of Judicial, Physicians) require vetting beyond shadowing; the vetting's content is not set down and is kept in the Judicial archive; vetting is voluntary and withdrawal unpunished | Gesture-without-specifics applied to personnel | Article 15 §4 and Article 18 §3(d) invoke it |
| **§6(e) is the single Syndrome rule** for every office and critical role (consolidated 2026-09-06) | See Article 4 table | — |
| §1(d) "private study, pursuit, or fixation" neglect clause is the labor-side curiosity lever | See the curiosity-neutralization table | Never connect it explicitly to Article 19 §6 |
| Reassignment after five years (skilled) or one (simple); retirement by joint Head Physician/Mayor age or Judicial ruling; no citizen left without assignment | — | Article 19 §5 mirrors this |
| A shadow may not be dismissed for ordinary mistakes; masters may not strike or starve a shadow; Judicial or the Sheriff hears such appeals | Anna-register protection clause | — |

## Established facts (from Article 14, "Of Housing and the Floors") — added 2026-09-06

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| Dwellings are assigned by household size and need by **Housing, an office of Supply** (settled 2026-09-06); no dwelling is property; the Head of Supply's approval is required for every assignment and revocation; revocation is appealable to Judicial | `CANON.md` §12 [TV] | Article 3 §§8–9 (relationships, kin) route through this office |
| Zones are qualitative, as Article 1 sets them: Up Top (governance, schooling, Assembly), Mids incl. Mid Thirties (households, markets, Infirmary, IT), Down Deep (Mechanical, Mines) — no numeric floor ranges | `REVIEW.md` D2 resolved by dropping numbers | Never reintroduce floor numbers for zone boundaries |
| Only Mechanical/Mines trades (and sentenced mine labor per Article 10 §2(e)) dwell Down Deep; Up Top housing only for office-holders, Judicial, teachers, and scribes | — | — |
| Search of a dwelling: Sheriff may enter for a crime in progress, a death, or an arrest; otherwise consent or a Judge's warrant; Officers search under warrant only (Article 6 §8 now sets the warrant's form and return) | — | Article 6 §8(d): a warrantless search is a wrong, but what it finds is not unfound |
| Households may not harbor a citizen unknown to the rolls or hide an unsanctioned child | Feeds Article 2's census fragility | — |

## Established facts (from Article 18, "Of the Cleaning") — added 2026-09-06

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| The request formula is exactly "I want to go outside" (canon), spoken to an Officer, the Sheriff, or written into the archive; no explanation asked | `HYPOTHESES.md` 7 | Article 16 §1 must keep treating loose talk as distinct from the formula |
| A requester is released from labor, office, and household bonds but stays in the rolls until IT's word closes the name (Article 2 §5(a)) | — | — |
| The Pact never states what happens outside: "the world above, as Article 1 records it, and this Pact says no more of it than that" (§2); it neither denies death nor names it, though §3(b) and Article 19 §4(c) presuppose it | Three-readers: citizen knows, Pact refuses to say | Do not reintroduce "exile" or "not a death sentence" |
| Suits: assembled in IT's cleaning lab to a specification IT alone sets, from cloth/seals/fittings furnished by Mechanical and Supply; cleaning-lab trade is full-shadowed and vetted beyond Article 13 (`REVIEW.md` B3) | Keeps the sabotage vector with IT, as canon requires | — |
| Airlock procedure (§4) is pedantic-procedural camouflage: 3–5 wool pads logged, hour-stamped countersignatures, "a gas Information Technology alone administers and this Pact does not further describe" | See the camouflage-device table | Preserve the gas sentence unaltered |
| Refusal of the suit is recorded and the departure proceeds (§3(c), softened 2026-09-06) | Forecloses stalling without the earlier gratuitous line | — |
| Families of the cleaned are not marked or punished; a child of a cleaned parent is entered as any other | Anna register | Article 3 §9(c) relies on this |
| Article 22 may hold a request in abeyance in the gravest emergency, never deny it (§1(b) cross-references) | — | — |

## Established facts (from Article 20, "Of Assembly and the Common Halls") — added 2026-09-06

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| The Assembly is all citizens of majority; ordinary sitting once yearly, convened by the Mayor; extraordinary by one-fifth petition, the Mayor, or Judicial, within fourteen days; no sitting longer than three days | The one-fifth petition is deliberately hard without radio (Article 21) | Load-bearing for Article 5's vacancy-election gap |
| Votes (§6, added 2026-09-06): hands in the hall, three Judicial tellers; floor counts sealed by the floor's Deputy and carried by porter, added only if they arrive before the close; "the Assembly present" = those who actually voted; no citizen may be *asked* how they voted | Hands are visible; the protection is against asking, not seeing — a quiet seam | Never add a secret ballot |
| Order of business (§7): rulings, Mayor's report, stores reckoning, green-list-kept report, Mayoral election if due, amendments, then citizen petitions | Citizens' petitions come last | — |
| Removal of Mayor: two-thirds in extraordinary session; Judge confirmation simple majority, removal two-thirds; term-end Mayoral election at the fifth-year ordinary sitting (§4(a)) | — | — |
| Amendment: Mayor's proposal or one-fifth petition, two-thirds of the Assembly present; entrenched limits in Article 23 §2 need Judge + IT Head concurrence | — | — |
| Cafeterias open before first labor and close after last; Down Deep hall keeps Mechanical/Mines shifts; standing after-hours leave from a Head; cleaning seating by a separate lottery | `CANON.md` §18 cafeteria facts, both now incorporated | — |
| Speech to the Assembly is protected from retaliation; addresses are archived and may be struck only by the Judge for forbidden speech | — | — |

## Established facts (from Article 21, "Of Records, Porters, and the Post" — completed 2026-09-06)

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| The archive (Level 1, secured) is kept in classes by originating Article (§6(a) lists thirteen); nothing is ever destroyed, worn records are copied and the original kept; an archivist (short-shadowed) keeps order and reports each season | Institutional memory as a single point of truth — and a single point of capture | The Amendment Log's "leaf wanting" scar (Amendment 9) is therefore itself notable |
| Secondary roll under the Head of Supply: citizenship rolls, rulings, sentences, and the Amendment Log only, copied each season | — | — |
| Porters: assigned by Supply, short-shadowed (one or two seasons), right of way on the stair, sealed messages inviolable save to Sheriff/Judicial in investigation | Exist because Article 8/21 reserve wire and radio to offices | — |
| Freight-lift log kept in duplicate (Judicial and Mechanical), compared each season | — | — |
| Printed copies of the Pact (§7): made by the archivist from the archive copy, checked yearly by an Officer, replaced within the season; any citizen may hand-copy the Pact; altering or passing off a copy is answered as false teaching (Article 16 §3); amendments entered into every printed copy by hand within a season | Explains how the printed Log stays current under the "founding text + separate Log" convention this draft uses | — |

## Established facts (from Article 23, "Of Amendment and the Continuance of the Pact") — added 2026-09-06

| Fact | In-world explanation | Implications for later Articles |
|---|---|---|
| Amendment by two-thirds of the Assembly present, on the Mayor's proposal or a one-fifth petition, with fourteen days' notice of the text | — | — |
| Entrenched limits (§2): the final request, the lottery, Judicial's silent-Pact rulings, the citizen's right to read the Pact and speak in Assembly, equality before the law, Article 1's founding, and any Department's undisclosed procedure; an amendment touching these needs the written concurrence of **the Judge and the Head of IT**, else void | The concurrence clause is the Pact's one explicit acknowledgment that IT holds a veto — buried as a procedural safeguard | Amendment 12 (anomalous signal) is the Log's example of this concurrence being given without recorded dissent |
| Amendments fix their place by order, not date (§3(a), 2026-09-06); printed at the end of every copy as the Appendix | Founding-date ambiguity | — |
| The Pact ends only if the silo ceases to stand or be dwelt in (§4(c)) | — | — |

## Established facts (Amendment Log rebuilt, 2026-09-06)

The Log is now thirteen entries: 1 Housing Proviso; 2 Testimony (Anna-imitation, citizens' petition); **3 Rumor Proviso** (new — Victor-imitation with an aphoristic preamble and an unworkable "within one hour," patched by a Judicial ruling: a lesser hand imitating the pedantic-procedural device); 4 Retirement Entitlement; 5 Appeal of Sentence; 6 Right to Counsel; **7 Bounding of the Forgiveness Holiday** (new — a restriction, Mayor's proposal); 8 Syndromic Retirement; **9 Restoration of the Holiday** (new — repeals 7; text partly lost, "the leaf of the roll bearing it is wanting," reconstructed by the Judge, with `[\ldots]` gaps); 10 Floor Reassignment; 11 Assembly Quorum (retitled; the Pact never had a quorum, so it now *sets* one rather than "reducing" it); 12 Anomalous Signal (IT); 13 Narrowing of Counsel. Articles 3 and 4 were removed from the Unamended list. Old `REVIEW.md` and earlier FACTS rows use the prior numbering.

## Established facts (expansion pass, 2026-09-06 — items 1–10 of the growth list)

All of the following were added on 2026-09-06. Each is deliberately mundane administration per the Restraint principle; the few seams are marked.

| Article / place | Fact | In-world explanation | Implications |
|---|---|---|---|
| **Article 1 §1, the recitation** | The founding recitation is now printed as a fixed italic text (~120 words) "taught in these words and no others": poison above, builders unnamed, "we do not go outside, because outside is death, and the wallscreen shows us so" | Gives Article 15 §3 and Article 16 §3 a concrete text to protect; Anna's cadence | Any Article quoting the founding must quote this text; never add a founder's name or a date to it |
| **Article 1 §6, the Terms** | A definitions list of 27 terms. New facts fixed here: a **cycle** is ten days; a **season** is nine cycles; a **year** is four seasons (360 days); the **rest day** is the tenth day of each cycle (works, workings, farms, Infirmary, and the peace excepted, with a substitute day owed); **office** = Mayor, Deputy, Judge, Sheriff, Heads; **Department** = Mechanical, Mines, Supply, IT, Judicial, Infirmary; years are reckoned only forward from a named event, never from the founding | Statute texture; the "never from the founding" line restates open item 1's resolution as a rule of the text | Every "cycle," "turn of the season," and "year" in the book now has a fixed length; the rest day is a new cross-cutting fact (Articles 9 §8, 10 §6, 11 §12, 15 §9, 21 §10 all now use it) |
| **Article 3 §10, the Naming** | Naming within ten days before the Clerk or a deputy, with the physician/midwife attesting; given name + household name of the bearing citizen (or married partner); no name reserved to floor/trade; names read at the next Assembly; the Preamble read at the naming; a parent's absence is not recorded against a child | Fulfils the Preamble's "read aloud at the naming of every child" | — |
| **Article 3 §11, Dissolution** | Joint or single petition; one refusal allowed "in haste," none a second time; one season's wait unless danger; dwelling to the partner with the children; goods by agreement or ruling; children placed by Judicial with visiting rights; unused lottery grant forfeited; not an offense | Anna register; camouflages the fact that Judicial places every child | — |
| **Article 3 §12, the Ward** | What a household owes a ward; a household that abandons a ward in fact answers as for neglect of labor ("the keeping of a ward being a labor the silo assigns"); Judicial may take a ward on an Article 15 §7 or Article 19 report; the school stands as household for an unplaced ward | Closes the loop on Article 15 §7's report clause: it now has teeth | The "fixation" report can now cost a household its child — do not soften |
| **Article 6 §10, silent-Pact petitions** | Petition posted one cycle; any citizen may enter a written answer; Judge hears all and rules; rulings never reach back; a table of rulings by Article is open at Judicial's door | Real, non-hollow procedure — the Restraint principle | — |
| **Article 6 §11, Evidence** | Roll of evidence, numbered marking, locked store, relics pass to IT and back; proof kept one year then returned or reclaimed; relics never returned save under sanction | — | — |
| **Article 6 §12, Sentences** | Signed entry before any sentence is carried out; mines conveyance by two Officers within one cycle with the Head of Mines' receipt; a returned citizen "holds every standing" and may not be refused trade/dwelling/ration | — | — |
| **Article 6 §13, Officers** | Full-shadowed, vetted, Judge-confirmed; act only under warrant/sentence/direction; complaints heard by another Officer; **two true complaints remove an Officer**; Officers keep no private records — an Officer who does is removed | The last clause is a quiet Victor tell (all Officers' knowledge lives in the one archive) | — |
| **Article 7 §6–9, Sheriff** | Station Up Top beside the cafeteria with ≥2 cells; station roll to Judicial each season; arrest only in the act, on warrant, or on danger; gravest carried the same day, others within one cycle or released; the Sheriff may not question beyond name/floor/household; **three Deputies** (Up Top, Mids, Down Deep) each with a station and cell [TV-consistent: Hank in the Down Deep]; posted-notice rules | The one-cycle release rule is real; the "released is not cleared" clause is the hollow half | Article 21 §10 places porter dispatches beside these stations |
| **Article 9 §8–9** | Three generator shifts; gauge-reading at every change, logged by both names; **yearly full tending** with a one-day stop and reserve power, notice one cycle before; roll of accidents read each season, reported yearly | Amendment 17 later adds the Mayor's presence at the tending | — |
| **Article 10 §6–8** | Two shifts; shoring before ore; **count-up at every change**; a shorer's "unsound" stands against any order until Mechanical rules; a measurer per working with a proved chain, re-proved each season; nine-tenths of the limit triggers per-shift measuring; measurer ≠ supervising miner; any miner may read the distance log; sentenced citizens hurt below have the term paused | Two-hands measuring is why the 200-foot limit is credible as a kept rule; the collapse in canon reads as a failure of this system | — |
| **Article 11 §8–13** | Numbered beds and a posted rotation; farms' power share cut last but for works and Infirmary; farm water metered and tested each season; livestock counts and a Supply-only butcher; spoilage over one part in twenty reported; a Supply station on every dwelling floor; **the dead are given to the soil of the farms** (canon: the dirt farms), household may attend, no marker but the roll | The last is the Pact at its most mundane-grim: reclamation applied to citizens | Article 19 §11 and Article 2 §5 stay consistent (examination, then soil within one day) |
| **Article 15 §9–10** | Schoolroom every day but the rest day; the school year opens at a turn of the season the Judge names, with the Preamble read; four seasons with a cycle's recess each; up to four household rest days a year; **yearly examination** before the household — recite the founding, read the Pact, reckon, name the offices; a child who cannot recite by eight is "taught it again, apart" and reported to the Head Physician if it persists; the final examination is read aloud at the oath | The "taught apart" clause is a seam (remedial recitation as a health matter) | — |
| **Article 19 §8, Childbirth** | Nursery floor in the Mids under midwives; a carrying citizen seen each cycle and set to lighter labor; one season's rest after bearing, one cycle for the partner; **a stillborn child is given to the soil and the place is counted as a name closed** against the next drawing; no child leaves the nursery before naming | Anna register; the stillbirth clause connects to Amendment 2's testimony | — |
| **Article 19 §9–11** | Aid stations in each zone; medicines under lock; the retired keep their dwelling, draw ration and chits, may take light labor, are seen each season, keep every standing; **the word to the household**: a Physician tells no more and no less than the Form; a cleaned citizen's household is told by the Officer "that the citizen has gone out" and may take the citizen's place at the wallscreen | The wallscreen line is the coldest Anna-register clause in the book: framed as a kindness | — |
| **Article 21 §8–11** | Occupant card made only by the archivist with the Judge's mark; surrendered at death or cleaning and kept beside the closing; a citizen may read their own records in the reading room and enter a one-leaf writing beside any record "which alters nothing"; three porter dispatches beside the Deputies' stations; porters carry for chits at posted rates, official word first and free; **seals**: stamps made by Mechanical to the Judge's pattern, one per office and dispatch; counterfeiting a stamp is answered as counterfeiting a chit (gravest) | The one-leaf writing is real recourse that changes nothing — hollow due process in its gentlest form | — |
| **Amendment Log 14–20** | 14 Recitation Affirmed (quotes the Preamble back; alters nothing); 15 Ordinary Pause (defines a pause the Pact left vague as "a count of two hundred"; the Sheriff reports it moved no one); 16 Naming of Officers in Assembly (narrows Article 20 §3's speech protection; three addresses struck at the next sitting); 17 Mayor's Presence at the Tending (Mechanical's first petition, after a generator stop ran three days over; nobody says what the Mayor's presence accomplishes); 18 Notice of Revaluation (ratified twice, first entry struck for a late floor count); 19 Keeping of the Green List (IT becomes co-keeper with a concurrence requirement; the second IT-fingerprinted amendment); 20 Housing Proviso Restated (duplicates Amendment 1; "the Assembly's record does not show that Amendment 1 was read before the vote") | Amendment drift realized across the late Log: quoting-as-legislating, pedantry without effect, a restriction dressed as procedure, a Department petition with no theory, a counting error, IT's quiet accretion, and finally a body that no longer reads its own Log | Articles 7, 9, 12, 15, 22 removed from the Unamended list; the Log is now 20 entries |

## Established facts (second expansion pass, 2026-09-06 — Articles 2, 8, 13, 16, 22)

| Article / place | Fact | In-world explanation | Implications |
|---|---|---|---|
| **Article 2 §6, the Oath** | Sworn on the sixteenth naming-day or the next posted sitting; the final examination (Article 15 §10) and the citizen's roll entry are read first and the citizen asked if each is true; **the oath text is now fixed**: "I am [name], of [floor and household]. I will keep this Pact. I will bear the labor given me. I will hold the silo's peace above my own. I swear it before Judicial, as every citizen before me has sworn, and as every citizen after me will swear."; the card is given the same hour; a citizen who will not swear remains a ward, and a ward of eighteen who has not sworn is ruled on by the Judge (fit to swear, or a ward of the silo in the Infirmary's keeping) | The bandwagon line from §3 is now spoken by every citizen; the eighteen-year clause is a quiet way of making non-swearing a health matter | Article 15 §10(d) and Article 21 §8 are consistent |
| **Article 2 §7, Reconciling** | Yearly, every office delivers its roll; the Clerk compares name by name; **a difference is resolved on the latest report, and Judicial does not seek out the citizen** ("relies upon them as Section 4 provides"); open differences call in the card; the count of differences is read to the Assembly without names | Preserves the census fragility exactly: paper is checked against paper, never against a person | Never add a physical census or a door-to-door count |
| **Article 2 §8, the Count** | Counted each turn of the season; an unconfirmed name **stands open and is counted** until Judicial inquires; the Sheriff seeks the citizen | A missing citizen inflates the count (and the ration and the lottery) until someone notices | — |
| **Article 8 §7–11** | License petition, numbered roll, instrument marked, copy to Judicial within one cycle, seasonal reconciliation, **licenses run one year and must be renewed**, withdrawal at will with surrender first; stations of official word in every named office with a technician's hand always on the set, who may refuse a word "no word of the office"; **the servers** keep IT's own records "and such further matter as that Department alone is instructed in," are not the archive, and are searched only on a warrant given with the Head's knowledge; server technicians' records stay in the Department; relic examination within a season, report to the Judge within the Pact's bounds, **wireless devices and writings about the world above are kept by IT and not returned to Judicial's store**; every IT trade save licensors and archivists is a critical role; a departing citizen signs a binding entry not to speak of the charge; the Head's naming of a successor is a signed entry delivered to Mayor and Judge, the objection season runs from delivery; if the Head dies unnamed, the Head's last shadow or the senior technician acts and names within a season; **the Head's shadow is the presumed successor** | IT's insularity made procedural. The "technician's hand upon the set" and the technician's veto over an office's word are the two quiet tells; "such further matter" is the gesture device; the retained-relic clause is why Juliette's drive never comes back | Article 5 §4(b)'s fallback (senior Head by first confirmation) now has the IT Head's date of "confirmation" fixed by the delivery of the naming; keep it |
| **Article 13 §10–13** | The contract of shadowing entered before the Clerk (trade, tier, span, lodging, critical-role flag), signed by master, shadow, Head; "shadow" written on the card and struck on confirmation; span may be lengthened once; no two shadows per master; the master's seasonal record signed by the shadow; a shadow does nothing alone until the master enters it; lending to another master for a season; re-entry if the master dies or is cleaned, "without mark"; four endings — confirmation, dismissal, release, abandonment; **the shadow inherits the master's tools, shifts, and quarters**; a master undertakes to step down and keeps the dwelling a season after; **no one may order a master to attest a shadow ready**; a master of three confirmed shadows is a master for life | Canon: Bernard/Lukas; Juliette's inheritance of Walker's trade. The "no order to attest" rule is a real check; the inheritance clause is why a master's power over a shadow is total | Article 13 §3(d)'s "commitment made before Judicial" now exists |
| **Article 16 §8–10** | A relic roll apart from the evidence roll; classification at a posted sitting with the surrendering citizen heard only "as to how the relic came"; **three classes: red** (gravest; destroyed/sealed; never reclassified), **second** (the silo's to keep, reclaimed or stored, never sanctioned), **third** (sanctionable); the citizen is not told IT's report; sanction is per-citizen, marked on the relic, passes only by further sanction or the Judge's leave at death; withdrawable "for cause entered or for none"; yearly counts read to the Assembly by class without names; **writing and likeness are free** save any likeness or writing of the world above, any writing on a common wall, and any likeness of the works or the workings; a map of the silo beyond what school teaches is shown to Mechanical first | "Red-level relic" [TV] now has a home; the writing section is the Restraint principle at work (most of it is permission) | Article 8 §10 and Article 6 §11 route relics through this |
| **Article 22 §6–10** | Announcement by station to Deputies, then Peacekeepers cry it at every landing within one hour and post the Mayor's notice; no order binds a floor before it is posted there; a citizen goes home or to the trade's floor and waits; **sealing a floor**: named cause (disease, fouling, breach), reviewed within one cycle by the Judge on the reports, never past a season without the Assembly; the sealed floor's ration, water, air, aide, word, and dead all provided for; **the order of lessening**: market, recreation and hall lights, servers, farms, reserve, then the ration alike; the works and the Infirmary lessened only by Mechanical's own order; stores reported each cycle and posted; **emergency labor**: anyone to anything, no rest day, two shifts max, never alone in a critical role and never thereby of it; the lifting posted the same way, everything ceases at the hour, reports to the archive within a cycle, the green list changed on the emergency's account | Bernard's engineered scarcity [TV] is now *illegal* under §8(a): the order of lessening is fixed and the ration is last, alike — which is what makes his doing it a Pact breach the close reader could cite | Article 21 §3(c) and Article 7 §8 carry the word-passing rules this leans on |

## Established facts (third expansion pass, 2026-09-06 — Articles 12, 14, 17, 18)

| Article / place | Fact | In-world explanation | Implications |
|---|---|---|---|
| **Article 12 §8–12** | Markets on ≥3 Mids floors and one Down Deep floor, ≥3 days a cycle, never the rest day; stalls by seasonal petition with craft-trades first, a flat fee to Supply, struck after three missed days; **weights and measures** are Mechanical's standards, proved seasonally by the Market Clerk; **the chit** is a token stamped by Mechanical to the Chit-Keepers' pattern, passes hand to hand unentered, may be entered to the ledger, and the silo does not make good a lost token; Departments may commission private goods for chits from their own accounts but never their own trades' work; **barter** is free and unenforced, save for the ration, the silo's things, relics, medicines, and chit-for-chit | Mundane; the "silo does not make good a lost token" line quietly pushes citizens toward the ledger, where their surplus is legible (`HYPOTHESES.md` 10) | — |
| **Article 14 §6–10** | A roll of dwellings by floor and number, empties reported; **the order of assignment is fixed**: new marriage/relationship, lottery-window household, returned/displaced, kin taken in, trade moved, preference last; written assignment countersigned by the Head of Supply; take-up within a cycle or it lapses; an out-of-order assignment is not undone but the wronged citizen gets the next dwelling; inventory of common furnishings (bed each, table, chair each, shelf, lamp) signed at both ends; a dead household's goods to kin within a cycle or to reclamation; the dwelling's water, vent, light, and waste are Mechanical's to the wall and within; warnings then Article 17; common rooms kept by turns posted by the Peacekeeper, three missed turns → Housing, three referrals → revocation; a gathering in a floor's common room is "a gathering of the floor" for Article 16 §2 | The last clause is load-bearing: it is what lets a floor meet without the Sheriff's leave, and what makes a cross-floor meeting unlawful | — |
| **Article 17 §6, the Grace** | Fixed form with the words "This is the grace of a first offense under Article 17, given once and not again"; read aloud, signed; stands for life; struck only on a ruling that no offense occurred; may not be weighed against a citizen for trade, dwelling, shadow, or sanction, but the Head is told; **no grace for an offense in an office, for emergency diversion, or where the mines answer a first offense** | — | Article 16 §7(a) and Article 22 §8(d) are the two "mines on first offense" cases |
| **Article 17 §7, the Term** | Whole seasons, 1–20; runs from the Head of Mines' receipt; pauses for unfitness (Article 10 §8), not for the rest day; shortened only by the Judge, never lengthened; **second term not less than the first, third term twenty seasons, no fourth** (the Judge rules another measure); the household keeps dwelling and ration; the citizen's chits are held in the ledger | The "no fourth term" clause hands the Judge a ruling power with cleaning as the only remaining named measure — a seam the close reader can find | Article 6 §12 and Article 10 §2(e) are consistent |
| **Article 17 §8, the Weighing** | Five things and no others: harm, intent, drawing others in, office, coming forward; a harmless, unmeant, solitary, non-office first offense is grace without weighing; a term set without an entered weighing is reduced to one season on petition; **coming forward with surrender earns the grace whether or not a Holiday is declared** | Real, non-hollow structure; the Forgiveness Holiday is now a special case of a standing rule | Article 4 §7 remains consistent (the Holiday adds public notice and covers the thing itself) |
| **Article 17 §9, Officers** | No grace in office; the office is vacated by sentence; **the Judge's own offense is investigated by the senior Officer and heard by the Mayor, who sets the measure, and the Assembly removes** — the one place the Mayor judges; the Sheriff is held by Officers in the Sheriff's own place; an officer's sentence is read to the Assembly "that the silo know the office was kept and not the officer" | A deliberate exception to Article 4 §4's co-equality, recorded here as design: a Mayor with the Assembly can eject a Judge through an offense, mirroring how Judicial can reach a Mayor (`HYPOTHESES.md` 4) | Article 6 §1(a) ("removal by the same two bodies") is consistent; never add a Judge-judges-Judge path |
| **Article 18 §7, the Lab** | A room between the cafeteria and the airlock, IT's, searched only on a warrant with the Head's knowledge; stores of furnished cloth/seals/fittings and of Supply's wool; a lab log kept apart from the chamber record and **not delivered to the archive** save the yearly count of suits drawn, compared against sentences and requests; ≥2 suits always ready | The count-comparison is the one audit; it checks number, never content | Preserve: nothing about assembly is ever set down |
| **Article 18 §8, the Days Between** | The citizen is held in the Sheriff's cell (canon: Holston), departure within one cycle on the day the technician enters the chamber ready; household visits daily, the Sheriff hears none; a one-leaf **last word** sealed and given to the household after, read only by the Judge for forbidden speech and struck accordingly; no questioning; "told, once, that the request is final, and is not asked again" | The last-word clause is hollow due process in miniature: real, kept, and censored | — |
| **Article 18 §9, the Fitting** | The walk from the cell through the cafeteria at a posted hour, household beside as far as the lab door; fitted by one technician's hands in the Department's order, told at each seal it is sealed; told of the pads "in these words and no others," nothing else, "and the citizen is not to ask"; **"The helmet's visor is sealed by the technician last of all, and what the citizen sees through it is no part of this Pact"** | The visor sentence is the book's second-most Order-sensitive line after the gas; it is a single clause, unpadded, because §9's fixed-words procedure around it is the padding | Never expand this clause |
| **Article 18 §10, After** | Second flush before any door opens; record closed and carried to the Clerk the same day by the waiting Officer; **"What remains outside remains outside. No citizen is sent to recover a suit, a pad, or a citizen"**; the image shown until IT enters the death; the technician is given the next rest day and seen by a Physician within the season | The recovery bar closes the one obvious way a suit could ever be examined; the technician's Physician visit is Victor's fingerprint (the ritual's cost to its operator is managed, not ignored) | Article 2 §5, Article 8 §4, Article 19 §11(d) all consistent |
| **Article 18 §2(b)** | Corrected: the sentenced citizen is made ready exactly as a requester (cell, Physician on request, lab), not "by the Infirmary" | Removed the last trace of `REVIEW.md` B3's Infirmary-clothes-the-cleaner draft | — |

## Coherence review of the expanded text (2026-09-06, evening)

Mechanical check: every "Article A, Section B" and in-Article "Section N" reference across all 23 Articles and the Log was verified in range against the current section counts, and the targets were checked by title. None were out of range or pointed at the wrong section. Substantive contradictions found and fixed:

| # | Where | Contradiction | Fix |
|---|---|---|---|
| 1 | Article 7 §7(a) vs Article 18 §8(a) | The Sheriff could hold a citizen only for an offense in the act, a warrant, or danger "and for no other cause," but Article 18 holds a *requester* in the Sheriff's cell | Article 7 §7(a) and (c) now name a citizen held for the departure under Article 18, held until the departure rather than released at one cycle |
| 2 | Article 7 §6 vs Article 19 §3 | The station was "the one place... apart from the airlock" where a citizen may be held by any office but Judicial; the Infirmary's compelled isolation is another | Article 7 §6 excepts the Infirmary's isolation |
| 3 | Article 21 §3(c) vs Article 8 §8(a) | Emergency radio "to the Deputy or Peacekeeper posted at the floor's landing" implied a set at every landing; Article 8 keeps stations only at the Deputies' stations | Article 21 §3(c) now routes to the Deputy's station, then by Peacekeepers on foot |
| 4 | Article 16 §8(c) vs §5(a) | The red class flatly included every Section 5 device; §5(a) lets the Judge classify one otherwise for cause | §8(c) now carries the same "save where the Judge finds cause" |
| 5 | Article 20 §7(a) vs Articles 2, 3, 16, 17 | The order of business was a closed list that omitted the namings, the count and reconciling of the rolls, the relic counts, and officers' sentences, all of which those Articles require read at the ordinary sitting | Added as a group after the rulings |
| 6 | Article 18 §2(a) vs Article 17 §9(c) | "The Judge alone sentences a citizen to cleaning" vs the Mayor hearing the Judge's own offense and setting the measure | Article 18 §2(a) excepts the Judge's own offense |
| 7 | Article 17 §4 vs Article 21 §11(d) | The gravest list is closed "and no others," but counterfeiting a seal-stamp was answered "as for" counterfeiting a chit | Seal-stamp counterfeiting added to §4 |
| 8 | Article 8 §9(c) vs Article 22 §8(a) | Servers lessened *after* the farms in one and *before* them in the other | Article 8 now defers to Article 22's order (market, halls, servers, farms, reserve, ration); IT's right to represent to the Mayor is kept, which is the seam |
| 9 | Article 11 §8(c) vs Article 22 §8(b) | Farms lessened last "save the works and the Infirmary" omitted the stations of official word, which Article 22 never lessens | Added, with a pointer to Article 22's order |
| 10 | Article 14 §7(b) vs Article 3 §11(c) | Dissolution promised the departing partner a dwelling within a cycle, but the fixed assignment order gave dissolution no place | Added to the third order |
| 11 | Article 13 §3, Amendment 8 vs Article 1 §6 | "weeks," "months" survived after the definitions fixed the calendar as day/cycle/season/year | "three cycles," "some cycles or a season," "one cycle" |

Checked and found consistent (no change): Article 6 §8 warrants vs Article 14 §4 Sheriff entry (Sheriff ≠ Officer); Article 6 §12 conveyance vs Article 10 §2(e) and Article 14 §2(a) (a sentenced citizen counts as assigned to Mines); Article 17 §7 term reckoning vs Article 6 §12 and Article 10 §8; Article 19 §8(e) stillbirth counted as a name closed vs Article 3 §2(b) (correct: the place re-opens); Article 22 §9(b) two-shift cap vs Article 9 §8(a); Article 2 §6 oath vs Article 15 §10(d) and Article 21 §8(a); Article 12 §1(c) no chits in the mines vs Article 17 §7(f) (held in the ledger, not paid); Article 11 §13 bodies to the soil vs Article 19 §11 and Article 2 §5; Article 5 §4(b) senior-Head fallback vs Article 8 §11(c) (the IT Head's confirmation date is now the delivery of the naming). Three lowercase "deputy of Judicial" uses (Articles 2, 3, 13) sit beside the Sheriff's "Deputy" and the "Deputy Mayor"; left as is, being qualified each time.

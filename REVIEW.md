# Review of the Complete Draft — 2026-09-03

Full read of `frontmatter/`, `articles/article01`–`article23`, `backmatter/amendments`, checked against
`STYLE.md`, `CANON.md`, `FACTS.md`, and the project principles in memory.

Current size: ~27,100 words of source (~25k prose) against the 60k+ target.

> **Status as of 2026-09-06.** A second full review was done on 2026-09-06 and its
> findings applied in the working tree. Status of the items below, by ID:
>
> - **Done**: A1, A2 (cross-references verified by meaning across all Articles),
>   A3, B1, B2, B3, B4, B5 (five-year term, Article 4 §1(b)), C1–C4, D1–D10,
>   E4, E5, E6 (Amendment retitled "The Assembly Quorum" and reworded to *set*
>   a quorum), E7, E8, E9, E10, F1, F2, F3, F4, F5, G1, G2, G3, G4.
> - **Partly done**: E1–E3 (the Log is now 13 entries with two restrictions,
>   an IT-fingerprinted amendment, a repeal-and-restore pair, a lost-text scar,
>   and two early imitations of the founders' registers; the voice of entries
>   1, 4, 5, 6, 8, 10 is still uniform); G5 (source is ~37k words of ~60k
>   target — see `FACTS.md` and README for growth areas).
> - **Not done**: the `\ref`-based cross-referencing suggested under A2.
>
> Amendment numbers cited in this file are the numbering *at the time of the
> review*; the Log has since been renumbered twice (see `FACTS.md`, "Amendment
> Log rebuilt").

Findings are grouped by tier. Tier A must be resolved first — most of Tier D's cross-reference errors
are downstream of it.

---

## Tier A — Structural (blocking)

### A1. The Schooling Article was lost; `article23.tex` is empty

`articles/article23.tex` is 0 bytes and is still `\input` by `main.tex`. The intended 23-Article
outline was:

| # | Intended | # | Actual file |
|---|---|---|---|
| 14 | Housing | 14 | Housing |
| **15** | **Schooling** | 15 | Public Order |
| 16 | Public Order | 16 | Crimes |
| 17 | Crimes | 17 | Cleaning |
| 18 | Cleaning | 18 | Health |
| 19 | Health | 19 | Assembly |
| 20 | Assembly | 20 | Records |
| 21 | Records | 21 | Emergency |
| 22 | Emergency | 22 | Amendment |
| 23 | Amendment | 23 | *(empty)* |

The Schooling Article was dropped when Mines was inserted as Article 10 and files 16–23 were shifted
down one. Five passages still cross-reference it as a live Article:

- `article02.tex:22` — "schooling under Article 15"
- `article13.tex:18` — "the schools under Article 15 shall assess each child's aptitude"
- `article14.tex:23` — "such teachers and scribes as Article 15 and Article 20 require"
- `article15.tex:29` — "in a place of schooling under Article 15" (a self-reference inside *Public Order*)
- `article18.tex:24` — "the charge of Article 15 (schooling)"

STYLE.md names controlled schooling as one of the Pact's "real center of gravity" mechanisms
alongside the cleaning ritual, the wallscreen, and hollow due process. Losing it removes the single
best vehicle for the Article 1 §1 teaching mandate ("shall be taught to every child before their
eighth naming-day") and for Article 15 §3's forbidden-history rule.

**Recommended edit:** write `Of Schooling and the Teaching of the Young` as Article 15 and renumber
current 15–22 → 16–23. This restores every OLD-scheme reference automatically, fills `article23.tex`,
and validates the Article 23 amendment references already sitting in Articles 1 and 6.

### A2. The draft is split between two incompatible cross-reference schemes

Because half the draft was written before the shift and half after, ~60 cross-references are wrong
under any single numbering.

- **Consistent with the OLD/intended scheme** (Schooling 15, Public Order 16, Crimes 17, Cleaning 18,
  Health 19, Assembly 20, Records 21, Emergency 22, Amendment 23): Articles 1, 2, 6, 7, 8, 10, 11, 16
- **Consistent with the NEW/current scheme:** Articles 4, 5, 17, 19, 20, 21, 22
- **Mixed internally:** Articles 3, 9, 12, 13, 14, 15, 18, and the Amendment Log

Worked examples:

- `article14.tex:35` uses both in one sentence: "answerable under **Article 16**; if the breach
  endangers … among the gravest offenses under **Article 17**" — both mean *Crimes*.
- `article12.tex` §1(c) "sentenced to the mines under **Article 17**" sits two lines above §1(d)
  "under **Article 16**" — again both mean *Crimes*.
- `article09.tex` §2(d) cites "gravest offenses under Article 17" (Crimes, OLD) while §7(b)–(c) cite
  "Article 16" for the same thing (Crimes, NEW). §7 is a later insertion into an otherwise
  OLD-scheme Article.
- `article16.tex` (*Crimes*) refers to "Article 16 Section 1" for the forbidden wish — i.e. it
  believes it is Article 17 and that Public Order is 16.

**Recommended edit:** after A1, do a single mechanical pass. OLD-scheme files need no change;
NEW-scheme and mixed files need every reference in the 15–22 range incremented by one, verified by
meaning rather than by number. Then add `\ref`-based cross-referencing (the `\label{art:...}` tags
already exist on every chapter) so this class of error cannot recur silently.

### A3. Articles 4 and 5 duplicate the Deputy Mayor

`article04.tex` §6 is "The Office of Deputy Mayor and Succession"; `article05.tex` §1 is "The Office
of Deputy Mayor" and §4 "The Deputy Mayor's Election and Succession." Article 5's chapter title in
the Amendment Log's own list is "Of the Deputy Mayor and the Order of Succession."

**Recommended edit:** strip §6 from Article 4 down to a one-clause pointer ("The office of Deputy
Mayor, and the order of succession, are set down under Article 5"), and let Article 5 carry the
substance. This also frees room in Article 5 for the succession *gap* that
`article5_structural_fragility` depends on.

---

## Tier B — Canon and Order-exclusion violations

### B1. Article 4 §3(c) names other silos — the saga's central secret

> "The Mayor may make promises or take oath-bound obligations on behalf of the silo as a whole
> (e.g., **trade arrangements with other silos**, the division of resources in a time of extreme
> shortage) …"

The existence of other silos is Order-level knowledge and cannot appear in a document printed one
copy per twenty floors. This is the most serious content error in the draft.

**Recommended edit:** cut the parenthetical entirely, or replace it with an in-world example
("the division of resources in a time of extreme shortage, or a standing obligation laid upon a
Department beyond the term of the Mayor who laid it").

### B2. Amendment 8 repeals "the Intactica Rite"

STYLE.md: *"Skip 'Intactica.' Per the user's decision, this TV-only invented rite is not used anywhere
in this project."* Amendment 8 is built entirely on it.

**Recommended edit:** replace Amendment 8. See E1–E3 for what should occupy that slot instead.

### B3. Article 17 §3 gives the cleaning suits to Mechanical — contradicting canon and closing the plot

CANON.md on IT: *"controls servers, surveillance, comms, and — critically — administers cleaning-suit
manufacturing, i.e. holds the silo's real technical/covert power."* And: *"suit tape deliberately
sabotaged by IT."*

Article 17 §3(a) currently reads: "The suit provided to any citizen sent to clean is made by
Mechanical, sealed by Mechanical, and is **the sole responsibility of that Department** to ensure it
is whole, its seals are sound…" Article 17 §2(b) has the Infirmary preparing the citizen.

This is a consilience failure, not just a canon slip: it forecloses the sabotage vector the entire
saga turns on, and it hands the silo's covert lever to the wrong Department.

**Recommended edit:** suits are assembled in the cleaning lab under Information Technology (Article
8), to seals and materials **specified by** Information Technology, from stock supplied by Mechanical
and Supply. Keep the sanitised public framing — the Pact should say the suits are made with the
utmost care and tested to hold, and should route the *specification* to IT under the same
gesture-without-specifics formula Article 1 §4(b) already uses ("under such further procedure as that
Department alone is instructed in"). The citizen reads diligence; the close reader notices that the
one Department nobody audits writes the specification.

### B4. Article 13 §1 states the silo's population

> "The silo contains one hundred and forty-four levels and **more than five thousand souls**…"

Two problems. First, it is the same anachronism class the user flagged for Article 1: the Pact is
written before the silo is sealed and cannot know how many people live in it. Second, CANON.md cites
the population loosely at ten thousand.

**Recommended edit:** recast as design capacity ("provisioned for" / "built to hold"), or delete the
figure and let Article 2's census be the only source of a population number — which is also better
for the Article 2 structural fragility (the census depends on good-faith self-reporting).

### B5. The five-year mayoral term is missing

CANON.md key finding 1: *"Five-year mayoral terms: the show specifies elections every 5 years."*
Article 4 §2(b) instead says the Mayor "holds office for such term as the Assembly determines under
Article 19."

**Recommended edit:** fix the term at five years in Article 4, with the Assembly retaining removal
power. The indefinite term is also strictly worse for the plot — a fixed term is what makes the
Article 5 convening gap exploitable.

---

## Tier C — Founding-document anachronisms

The rule established for Article 1 — the Pact is written *before* the sealing and must not hint at
elapsed time — was never applied to the front matter.

### C1–C3. `frontmatter/preamble.tex`

- **:13** "though written down by many hands over many years, amended in Assembly, argued over in
  Judicial, tested against hard winters of scarcity and hard years of grief" — describes a history
  that has not happened.
- **:25** "It has changed before. It will change again." — the first half is impossible.
- **:5** "read aloud at the naming of every child, the seating of every Mayor, **the opening of every
  school year**" — presupposes an established practice; also depends on A1.

**Recommended edit:** convert all three to prospective voice. "Written down by many hands, to be
amended in Assembly and argued over in Judicial" / "It will change, by the lawful means set down in
the final Article." The forward-looking version is in fact stronger: it reads as the founders'
confidence rather than as a later editor's gloss.

### C4. Article 22 §3 presupposes a non-empty Amendment Log

> "Amendments to this Pact, ratified by the Assembly **since the silo's founding**, are recorded in a
> separate roll…"

**Recommended edit:** "Amendments ratified by the Assembly are recorded…" — minor, one clause.

---

## Tier D — Internal contradictions and dangling references

| # | Location | Problem |
|---|---|---|
| D1 | Article 4 §1 vs Article 5 §3 | "The Mayor is **not elected** to this office but is confirmed into it through the process set down in Article 5" vs. Article 5 §3 "an **election** shall be held… may stand for election as Mayor." Flat contradiction. Pick one; canon supports election. |
| D2 | Article 14 §2 vs Article 8 / Article 1 §3(b) | Article 14 fixes Up Top = 1–35, Mids = 36–108, Down Deep = 109–144. That places IT's "Mid Thirties" headquarters *inside Up Top*, contradicting Article 8 and the FACTS.md entry that IT is explicitly not Up Top. Move the Up Top/Mids boundary up (e.g. Up Top 1–20), or drop the numeric ranges and keep the zones qualitative as Article 1 does. |
| D3 | Article 4 §3(d) | "according to **Article 10's** framework (the Head of Supply sets the ration…)" — Article 10 is Mines; Supply is Article 11. Stale pre-Mines-insertion reference. |
| D4 | Article 12 §4(b), §6(b) vs Article 4 §4 | Article 12 lets the Mayor rule prices unjust, reverse transactions, and hear commission disputes — an adjudicative role that contradicts the Mayor/Judicial separation Article 4 §4 establishes. Route these to Judicial, or to a Market Clerk answerable to Judicial. |
| D5 | Article 21 §5(b) | "may petition for compensation under **Article 16's restitution provisions**" — Article 16 (Crimes) has no restitution provisions; §1 says an offense is answered by exactly one of three measures (grace, mines, cleaning). Either add restitution to Article 16 §5 or point the reference at Article 12. |
| D6 | Article 5 §3 | "no debt of justice under Article 16 and no continuing sentence under Article 17" — under the current scheme this reads as a continuing sentence under *Cleaning*, which cannot exist. Both clauses mean Crimes. |
| D7 | Article 12 §1(b) | Retirees' chits are "administered by the Infirmary under Article 18." Article 11 and Article 18 §5 both make Supply the provisioning Department. Should be Supply, with the Infirmary certifying need. |
| D8 | Article 10 §3(c) | Garbled: "may petition the Head of Mines, through the usual course of Judicial, if he believes his working is being ordered beyond the limit without his knowledge." The citizen petitions the very officer he is reporting, and "without his knowledge" has no antecedent. Rewrite. |
| D9 | Article 18 | The new §6 (at-risk referral) pushed "Fitness for Critical Roles and the Syndrome" to §7. No stale references found, but Amendment 5 and Article 13 §6 both sit adjacent to this material — re-check after any renumber. |
| D10 | Article 9 §7(b)–(c) | Cite "Article 16" for criminal liability inside an Article that otherwise uses the OLD scheme (where 16 = Public Order). Introduced with the Safeguard-visibility clause; fix as part of A2. |

---

## Tier E — The Amendment Log (the drift principle is unrealised)

`amendment_drift_principle` asks for later, lesser hands imitating the founding form without the
insight. The Log currently reads as eight competent, uniform, well-drafted paragraphs.

### E1. All eight amendments are liberalisations

Housing remediation, retirement medicine, sentence appeal, right to counsel, syndromic retirement,
floor reassignment, quorum reduction, repeal of a rite. Nothing tightens control. Over 134 years in a
silo governed by IT, at least two amendments should be *restrictions* — and at least one should have
IT's fingerprints on it (extending a licensing category, adding a reporting duty, quietly moving an
approval from the Assembly to a Head of Department).

### E2. There is no scar

Canon has periodic uprisings that destroy records. A 134-year log with even spacing and no gap, no
repeal-and-restore, and no "text lost, reconstructed from the Judicial archive" note is the single
biggest missed opportunity in the back matter. One amendment ratified and then repealed four years
later, with the effect note conspicuously vague about why, would do more work than any three of the
current eight.

### E3. The voice does not drift

Amendment 1 (Year 23) and Amendment 7 (Year 127) are written by the same hand. The later ones should
get longer, more defensive, more fond of preambles, and worse at anticipating consequences — see E5
and E6, which are already accidental examples of exactly that and should be made deliberate.

### E4. Amendment 1 amends the wrong Section

It amends "Section 4 of Article 14" — *Privacy of Dwelling Quarters and the Limits of Search* — with a
rule about housing revocation penalties, which lives in §1(d) and §5(b).

### E5. Amendment 5 amends the wrong Section

It amends "Article 13, Section 6" — *Critical Roles and Order-Adjacent Trades* — with a retirement
rule, which belongs to Article 13 §8 / Article 18 §5.

### E6. Amendment 7 is incoherent

It reduces an extraordinary-session quorum that Article 19 never established, then asserts that "the
ordinary Assembly requires **full attendance** or messenger-proxy under Article 20" — which is
physically impossible, contradicts Article 19 §1(a)'s permissive "any citizen of majority *may*
attend," and re-legislates the messenger provision Article 19 §1(d) already grants.

*(E4–E6 could each be converted from a defect into a deliberate drift signal — a later hand
mis-citing the founding text — but only if the Effect note is written to let the close reader notice.
As written they read as authorial error.)*

### E7. Amendment 3's floor clause is self-defeating

"A citizen … may petition Judicial to review the sentence **after five years** of service … No such
review shall reduce the sentence to fewer than **three years** of the original sentence." The floor is
already passed by the time the petition is permitted.

### E8. `amendments.tex:74` — "unchanged and unchanged"

Typo for "unaltered and unchanged" or similar.

### E9. "Unamended Provisions" contradicts the Log above it

The list includes **Article 13** (amended by Amendment 5) and **Article 19** (amended by Amendment 7).
It also omits Article 23 entirely, because Article 23 does not exist — see A1.

### E10. The Log mixes numbering schemes internally

Amendment 3 cites "the mines under Article 16"; Amendment 4 cites "the gravest named under Article
17." Both mean Crimes.

---

## Tier F — Register and consistency

| # | Location | Problem |
|---|---|---|
| F1 | Articles 4 §3(c), 12, 13 §7, 19 §3(a) | "e.g." and bare parenthetical lists clash with the Old-Testament/Constitution register. Convert to "as, for example," or to an em-dash apposition. |
| F2 | Articles 9 and 10 | "he," "his," "himself," "not himself licensed," "his own shadow." Every other Article uses "they," "the citizen's own." Roughly ten instances across the two files. |
| F3 | `preamble.tex:13` | "Head of I.T." — every Article writes "Information Technology." |
| F4 | Article 21 §2 | "green list" in scare quotes is a modern administrative idiom. The Pact does not use quotation marks for defined terms anywhere else; compare Article 15 §4's handling of "relic," which defines by apposition. |
| F5 | Article 17 §5 | "The cleaning is not cruelty, though it appears so to the citizen sent to it" and "This Pact provides the mechanism but not the interpretation" are the Pact talking *about* itself in an essayistic voice. Strong writing, but check it against the restraint principle — it is doing in the open what the Pact elsewhere does by omission. |

---

## Tier G — Completeness

### G1. Article 17 never describes the cleaning

The Article titled *Of the Cleaning* sets down who is sent, how they are sentenced, who watches, and
what it means — but never what the cleaner actually *does*. CANON.md has the wool pads, the sensor
lenses, the airlock purge with what is publicly described as an inert gas, and the ritual words by
which a citizen volunteers.

**Recommended edit:** add a section on the procedure at the airlock, written as pure mundane
administration — who issues the pads, how many, who confirms the outer door seal, how the chamber is
flushed "that the poison not enter with the citizen's leaving." This is the strongest available
three-readers passage in the whole draft: the citizen reads safety procedure, the close reader
wonders why the flush is IT's charge and not Mechanical's, and the book reader knows what is in the
gas. Currently the draft spends its Article-17 budget on meaning and none on mechanism.

### G2. The ritual words are not set down

Canon has volunteering by speaking a fixed form of words. Article 17 §1(a) says a request may be made
"to any officer of Judicial or to the Sheriff, or … written down." A fixed formula, printed in the
Pact, is exactly the kind of thing this document should contain — and it makes Article 15 §1's
prohibition on *voicing the wish* far more pointed, since the only lawful way to say it is to say it
exactly.

### G3. The Market Clerk is orphaned

Introduced as an office in Article 12 and never mentioned again — no appointment, no shadowing under
Article 13, no place in Article 11's Supply structure.

### G4. `article23.tex` is empty and still `\input`

Covered by A1, but note it independently: the book currently ends on Article 22 with a silent blank
input.

### G5. Word count

~25k prose against the 60k+ scope. The largest legitimate growth areas, in order of value:

1. **Schooling** (Article 15) — does not exist yet; carries the teaching mandate, the curriculum
   limits, and the Article 15 §3 forbidden-history rule.
2. **Article 17** procedural detail (G1, G2).
3. **Article 6** (Judicial) — the hollow-due-process master clause deserves more surrounding
   procedure to hide in; procedure is also the one area CANON.md explicitly marks as safe to invent.
4. **Article 3** (marriage and the lottery) and **Article 11** (ration) — both are places where
   Anna Thurman's kinship register can do legitimising work at length.
5. **The Amendment Log** — E1–E3 imply roughly doubling it.

---

## Suggested order of work

1. A1 (write Schooling as Article 15, renumber 15–22 → 16–23)
2. A2 (mechanical cross-reference pass; then convert to `\ref`)
3. B1, B2, B4 (canon/Order violations — small, isolated edits)
4. C1–C4 (preamble anachronisms)
5. D1–D10 (contradictions)
6. B3, G1, G2 (rewrite Article 17's suit and procedure provisions together)
7. E1–E10 (rebuild the Amendment Log)
8. A3, F1–F5, G3 (cleanup)
9. G5 (expansion)

FACTS.md will need new entries for whatever B3 and G1 settle, and the Article 14 zone boundaries
(D2) should be recorded there once fixed.

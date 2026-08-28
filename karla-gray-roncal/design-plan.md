# Design plan — The Unified Theory of Karla Gray-Roncal

## Subject, audience, job

Karla M. Gray-Roncal, M.D., M.S. — electrical engineer (Vanderbilt B.E. 2003, USC
M.S. 2004), twenty-two years of human-factors and systems engineering at JHU
Applied Physics Laboratory (2003–2025), M.D. Georgetown 2019, Johns Hopkins
neurology residency, and now a neuroimmunology fellow specialising in multiple
sclerosis.

On paper that is two unrelated careers with a medical school in the middle.
The page argues it is **one job, held continuously since 2003**: she instruments
the interface between a person and a system that is judging them. The audience
is her colleagues in two fields that don't read each other's journals — naval
human-factors engineers and MS neurologists — plus students she mentors, and
Karla herself. The job of the page is to make one career visible where a CV
shows two.

## Concept: the dark room

Both halves of her career happen in the same physical situation. A sonar
operator sits in a darkened submarine control room watching a **waterfall
display** — time scrolling downward, bright contacts emerging from noise. A
neurologist sits in a darkened reading room watching a **FLAIR MRI** — bright
lesions emerging from grey tissue. Same room, same posture, same task: *decide
which bright thing is real.* The page is built in that room.

The historical anchor for the per-publication section is the **specimen /
console label** — a numbered plate with an instrument caption, halfway between
a neuroanatomy atlas and an equipment panel.

The hero renders the thesis live: a **sonar waterfall** in which the scattered
contacts are her publications, drifting down as noise and then locking into five
clean tracks. Detection of signal in noise is the one thing she has always done.

### The borrowed diagnostic idea (labelled as interpretation)

Multiple sclerosis is the one disease *defined* by proving scattered things are
a single process: the McDonald criteria require **dissemination in space and in
time** — no single lesion and no single moment is a diagnosis. That is exactly
what this page must do to a bibliography, so Fig. A borrows it: her work
scattered across six unrelated fields (looks like noise), then resolved onto one
axis (one process). The conceit is the page's, not hers, and the sources section
says so.

## The ordering axis: what the instrument is made of

Date is the boring axis and it makes her career look like a switch. The real
axis is **what the measuring instrument is physically made of**, and it climbs
monotonically from steel to conversation:

| Rung | Instrument | Work |
|---|---|---|
| 1 | a sonar console | Watch Section Task Analysis (2008); APB technologies (2010) |
| 2 | a room | ICU task analysis (2011); pressure-ulcer lexicon (2015) |
| 3 | a benchmark | MICrONS human–machine baseline (2018); *Sci Rep* framework (2022) |
| 4 | a scanner | MRI scan-choice framework (2024); neurofilament light chain (2025) |
| 5 | a questionnaire | MS PATHS disability + SES (2021); migraine and headache apps (2015, 2018) |
| 6 | a phone call | relapse detection by scheduled contact (2025) |
| 7 | a question nobody had asked | racist microaggressions in neurology encounters (2025) |

Twenty-two years of engineering ends at *someone calling and asking specific
questions* — and that is the finding, not a retreat from it. The spine is drawn
as this ladder, not as a timeline.

## Palette: one sensor colormap

The five threads are **not arbitrary hues — they are five stops on a single
instrument's intensity ramp** (a magma-family scientific colormap, the kind a
waterfall display or a heat-mapped scan actually uses). Colour therefore encodes
position on the ordering axis: the career reads as one scale, low to high, cold
metal to warm human.

| Token | Light (the printout) | Dark (the reading room) | Meaning |
|---|---|---|---|
| `--room` | `#f6f4f0` warm paper | `#0b0c10` console black | page ground |
| `--panel` | `#eae6df` | `#15171d` | cards, wells |
| `--ink` | `#1d2024` | `#e9e6e0` | body text |
| `--faint` | `#63666e` | `#93959d` | captions, grid, scale bars |
| `--trace` | `#cec9bf` | `#2a2d36` | rules, hairlines, noise |
| `--console` | `#4a3f8c` deep violet | `#9a8ce8` | thread 1 — steel & sonar |
| `--bench` | `#8c2981` magenta | `#e07ac8` | thread 2 — human vs algorithm |
| `--scan` | `#b32e57` rose | `#f4738d` | thread 3 — scanners & biomarkers |
| `--clinic` | `#a84f14` orange | `#fb9f5c` | thread 4 — the patient encounter |
| `--gap` | `#7a5d0c` gold | `#e6c258` | thread 5 — who gets misread |

A thread's colour means the same work in every figure — waterfall track, graph
node, ladder rung, act header, plate rule, handout dot. No colour appears
without its meaning.

## Type

Deliberately not the previous subject's Fraunces / Spectral / IBM Plex Mono.

- **Display: Instrument Serif** — high-contrast, a touch editorial, and it
  carries a headline like "Plate VII" without looking like a template. (The
  name is a coincidence worth enjoying, not a reason.)
- **Body: Literata** — a screen-first long-form serif with real weights, built
  for reading paragraphs rather than captions.
- **Labels / data: JetBrains Mono** — instrument-panel captions, scale bars,
  node labels, sample sizes, odds ratios.

## Layout

A single ~72ch reading column, interrupted by full-bleed dark "display wells"
for every figure — hero waterfall, Fig. A, the graph, the ladder. The page
alternates between *reading the paper* and *watching the console*, which is the
argument restated as rhythm. Plates are a two-column grid collapsing to one,
each framed as a specimen/console label: roman numeral, instrument caption in
mono, year chip in thread colour, bespoke SVG, plain-language writeup, key
findings with exact numbers, source link.

## Motion

One orchestrated moment: the hero waterfall resolving noise into five tracks,
re-seeded on theme change, a single static frame under
`prefers-reduced-motion`. Elsewhere only hover states on graph nodes and plate
cards. Force layout and waterfall noise both seeded with `mulberry32` at a fixed
seed so every load is identical.

## Anti-generic check

- Ground is console black / warm printout, from the two rooms she actually
  works in — not cream-and-terracotta, not a purple-blue gradient.
- Type is Instrument Serif / Literata / JetBrains Mono — none shared with the
  other subject in this repo, per the playbook's "no shared template" rule.
- Thread colours are stops on one ramp, so the palette itself carries the
  thesis; a reader who only looks at colours still sees one scale.
- Numbered structure is real structure: the ladder rungs are the ordering axis,
  and the plates follow it rather than the calendar.
- The aesthetic risk taken on purpose: a sonar waterfall as the hero of a
  neurology page. It is the whole argument in one image, so it earns the risk.

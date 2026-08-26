# Design plan — The Unified Theory of William Gray-Roncal

## Subject, audience, job

One page arguing that a bibliography that looks scattered across six fields
(connectomics, AI, defense, learning engineering, workforce, public health) is a
single body of work. Audience: colleagues, students, program sponsors, and the
subject himself. Job: make the through-line *visible* — literally, as a picture.

## Concept: the proofreading view

Connectomics has one iconic image: **neon segmentation colors traced over a
grayscale electron-microscopy field**. Raw tissue is gray noise; a reconstructed
neuron is a bright, continuous thread a proofreader has confirmed. The page
borrows that exact convention: the career is the gray volume, and each research
thread is one segmented process traced through it. The historical anchor for the
per-paper section is **Cajal's illustrated plates** — hand-drawn, numbered,
captioned — which is what "Plates I–N" become here.

The hero renders the thesis live: an image field resolving into a graph
(his dissertation title is literally *Images to Graphs*).

## Palette

The imaging field, not a paper page. Dark-first in spirit, but fully themed both
ways (light = the printed plate; dark = the microscope).

| Token | Light (printed plate) | Dark (EM field) | Meaning |
|---|---|---|---|
| `--field` | `#f4f4f2` cool plate-gray | `#0e0f11` EM black | page ground |
| `--tissue` | `#e6e6e2` | `#1a1c1f` | cards, wells |
| `--ink` | `#26282b` graphite | `#e8e6e1` | body text |
| `--faint` | `#6d7075` | `#9a9891` | captions, grid |
| `--maps` | `#0e7f9e` cyan | `#53c8e0` | thread: mapping brains |
| `--trust` | `#a06508` amber | `#e8b04b` | thread: metrics & validation |
| `--archive` | `#2b8a3e` green | `#6fca7f` | thread: open infrastructure |
| `--machines` | `#b02a63` magenta | `#e77fb3` | thread: brains → machines |
| `--people` | `#c74e14` signal orange | `#ff9558` | thread: people & pathways |

Thread colors are segmentation colors: they mean the same neuron in every
figure — graph nodes, spine rungs, act headers, plate borders, handout dots.
No color appears without its meaning.

## Type

- **Display: Fraunces** (optical sizes, wonky serifs) — scientific-atlas
  personality, works for "Plate VII" as well as a thesis headline.
- **Body: Spectral** — a long-form screen serif for the story.
- **Labels/data: IBM Plex Mono** — instrument-panel captions, scale bars,
  node labels, citation counts.

## Layout

A single centered column (~72ch) for prose, with full-bleed dark "imaging
field" breaks for the figures (hero canvas, converge figure, graph, spine) —
the page alternates between *reading a paper* and *looking through the scope*.
Figure captions set in mono with real figure numbers. Plates are a two-column
grid collapsing to one at small widths, each plate framed like a specimen
label: roman numeral, title, year chip in thread color, SVG, plain-language
writeup, key findings, source link.

## Motion

One orchestrated moment: the hero's images→graphs resolve (gray blobs →
traced colored graph), re-run on theme change, static single frame under
`prefers-reduced-motion`. Elsewhere: hover states on graph nodes and plate
cards only. Force layout seeded with mulberry32(fixed seed).

## Anti-generic check

- Not cream + terracotta; the ground is instrument gray, chosen from EM.
- Not Inter/Space Grotesk; Fraunces/Spectral/Plex Mono.
- Numbered structure (Plates I–N, Fig. 1/2, Acts) is real structure: plates
  are an atlas convention the subject's field actually uses; acts follow the
  spine's ordering axis, not decoration.
- The one aesthetic risk: full-bleed EM-black figure wells inside a light
  reading page (and vice versa) — the "scope vs. paper" alternation.

# Design plan — *The Unified Theory of Shelby Wilson*

## The subject's world

Shelby N. Wilson is an applied mathematician (Spelman BS 2006 → UMD PhD 2012 →
INRIA Grenoble → Morehouse → UMD Biology → JHU/APL Senior Data Scientist).
Her instruments are **MATLAB figure windows**, **mixed-effect population models**,
and **forecast fan charts**. Her actual published output is MATLAB `jet`-coloured
network plots (Frontiers 2020, drawn in "release 2019a of MATLAB") and grey
ensemble ribbons laid over coloured individual-model trajectories
(Nature Communications 2023, Fig. 2).

The design is derived from those two images, because they are the same image:
**many coloured individuals, and one aggregate drawn over them.**

## Color — a ramp, not a palette

The six career threads are not decorative categories. They are *positions on a
ladder* — what counts as an "individual" in each body of work. So the thread
colours are sampled from a single sequential ramp (cold = microscopic,
warm = human), and a thread's hue is therefore readable as its rung.

| Token | Light | Dark | Rung — the individual is… |
|---|---|---|---|
| `--t-cell`   | `#2E4B9B` | `#7E9BEC` | a **cell** (T cells, Tregs, tumour vaccine) |
| `--t-mouse`  | `#137E8E` | `#4FC4D6` | a **mouse** (xenograft scheduling, mixed effects) |
| `--t-sleep`  | `#2C8757` | `#5FC98D` | a **sleeper** (thermoregulation, REM/NREM) |
| `--t-troop`  | `#B08214` | `#E8B93F` | an **animal in a troop** (allogrooming, ectoparasites) |
| `--t-model`  | `#CE5C18` | `#F58A44` | a **model** (COVID forecast + scenario hubs) |
| `--t-person` | `#A02330` | `#EE6D77` | a **mathematician** (Mathematically Gifted and Black) |

Neutrals are picked, not inherited: the light ground `#FBFAF7` is plotting-paper
warm-white (deliberately *not* the #F4F1EA cream default); the dark ground
`#0E1418` is the cold ink of a dark MATLAB figure. Muted ink carries a slight
blue bias so it sits with the cold half of the ramp.

Grey is reserved and means one specific thing on this page: **the aggregate** —
the ensemble ribbon, the population mean, the average. That is the argument in
the neutral.

## Type

- **Display — Fraunces.** Variable, with a real wonk/soft axis; high contrast.
  Reads like the poster for a named lecture, which is where this story ends
  (the Etta Z. Falconer Lecture, Spelman, Spring 2019).
- **Body — Newsreader.** Open, light-stemmed long-form serif; a clearly
  different texture from Fraunces so the pairing reads as two voices.
- **Utility — IBM Plex Mono.** Labels, parameters, citation counts, figure
  captions — the notebook/plot register she actually works in.

Explicitly avoided: Inter, Space Grotesk, cream-and-terracotta, purple-blue
gradients, emoji section markers.

## Layout

One ~64ch reading column for the argument, breaking full-bleed for the four
figures. The story section hangs off a **ladder rail** on the left whose rungs
are the six thread colours in ramp order — so the reader's position in the
story is also their position on the spine.

Plates alternate a bespoke SVG against its writeup. Every SVG is drawn from
what that specific paper actually does (105 mouse curves; three grooming hubs
with 49 spokes each; a REM/NREM switch against a temperature curve), never a
generic icon.

## The one risk

The hero is a live canvas **mixed-effect spaghetti plot**: 105 individual
trajectories draw in first — one per mouse in the 2015 sunitinib/irinotecan
study — then the population mean and its prediction-interval fan fade in over
them. It is simultaneously the page's thesis and a picture of her actual
method. Seeded `mulberry32` so it is identical on every load;
`prefers-reduced-motion` renders one static final frame.

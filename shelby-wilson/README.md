# The Individual Inside the Population

A unified-theory reading of the published work of **Shelby N. Wilson, PhD** —
applied mathematician, Senior Data Scientist at the Johns Hopkins University
Applied Physics Laboratory, and co-founder of Mathematically Gifted and Black.

Built with the method in [`../RESEARCH-STORY-PLAYBOOK.md`](../RESEARCH-STORY-PLAYBOOK.md).

**Published:** <https://claude.ai/code/artifact/33764f29-1575-439b-88fc-f917e284f2a6>

## The claim

Nineteen peer-reviewed publications spread across immunology, cancer
pharmacology, sleep dynamics, animal social behaviour and pandemic forecasting,
plus a website about Black mathematicians. Sorted by field it reads as six
careers. Sorted by **what counts as an individual** in each paper — a cell, a
mouse, a sleeper, an animal in a troop, a model, a mathematician — it is one
monotone climb.

Three falsifiable laws:

1. **No average is allowed to stand in for its members.** Mixed-effect modelling
   of 1,371 tumour measurements across 105 mice; an INRIA postdoc titled
   "…Yields *Individualized* Predictions".
2. **Population structure is an outcome, not an input.** Fifty animals
   self-organise into three hubs with 49 groomers each — or into nobody in
   particular — purely by changing the partner-choice rule.
3. **Combine, don't select — and keep the disagreement.** The linear opinion
   pool beat every single model; APL's own hub entry is an
   `ensemble_of_hub_models`. She qualifies this herself: unvalidated models
   pooled at equal weight can *lower* ensemble performance, so keep two cohorts
   — open for diversity, curated for decisions.

And the coda she wrote herself: the Etta Z. Falconer Lecture at Spelman, Spring
2019, titled *"Noether, Falconer, Mirzakhani, Kovalevsky, & Me"* — five names,
one of them hers, and one of them her grandmother.

## Layout

```
shelby-wilson/
  parts/            ordered HTML fragments — edit these
    01-base.html        tokens, base CSS, hero (live mixed-effect canvas)
    01b-converge.html   Fig. A — scattered → sorted
    01c-theory.html     the three laws
    02-data.html        the SUBJECT data model
    03-graph.html       Fig. 1 — related-work graph
    04-story.html       Fig. 2 — the spine, and the six acts
    05-gallery.html     Plates I–X
    06-gallery2.html    Plates XI–XIX
    07-realfigs.html    two CC BY figures, embedded as data URIs
    07b-handouts.html   three audiences, three activities, print CSS
    08-coda.html        the coda, sources, and the interpretation disclosure
  data/graph.json   exported data model
  figs/             source figures + provenance README
  build.sh          cat parts/*.html > index.html
  index.html        generated — never hand-edit
  design-plan.md    palette, type and layout rationale
```

## Build

```bash
./build.sh
```

Parts concatenate in filename order, so insert with `01b`, `07b` rather than
renumbering. **Write to `parts/`, never to `index.html`** — if a merge conflicts
on `index.html`, resolve the parts and regenerate.

## Sourcing

Citation counts are Crossref `is-referenced-by-count`, retrieved 27 August 2026.
Google Scholar was requested but is unusable from an automated context — its
author search returns a sign-in wall, and no public Scholar profile for this
subject could be located — so the canonical publication set was assembled from
Crossref, PubMed, Europe PMC, Semantic Scholar and her own February 2020 CV, and
same-name authors (Wilson SK, Wilson SE, Wilson SA) were removed by hand.

Everything on the page that is interpretation is labelled as interpretation.
Anything that could not be verified is marked rather than smoothed over.

The first version of this page said plainly that "On the Mark" (*Health
Security* 2023) could not be read — no deposited abstract, publisher 403. The
PDF was then supplied directly, and Plate XVI, Law I, Law III and the third
reproduced figure are now written from its full text. It turns out to contain
the sentence this page is named after: *"when model outputs are represented
using predictive intervals rather than individual trajectories, vital
information is obscured."*

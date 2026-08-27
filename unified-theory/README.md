# The Unified Theory of Will Gray-Roncal

An illustrated, Pixar-theory-style argument that this bibliography is one body
of work: **make the graph, calibrate the judge, widen the gate.** Built by the
method in [`../RESEARCH-STORY-PLAYBOOK.md`](../RESEARCH-STORY-PLAYBOOK.md).

**Live artifact:** https://claude.ai/code/artifact/3cebbca6-b53c-47fd-8024-9ce850647ed6

## Layout

```
parts/            ordered page fragments — edit these, never index.html
  01-base.html      tokens, base CSS, hero (images→graphs canvas)
  01b-converge.html Fig. A — the career filed two ways
  01c-theory.html   the three laws
  02-data.html      SUBJECT data object: papers, related work, keywords, edges
  03-graph.html     Fig. 1 — related-work graph engine
  04-story.html     Fig. 2 — the scale-ladder spine + the acts
  05-gallery.html   Plates I–XII
  05b-keystone.html the keystone interlude ("From sample to knowledge", 2016)
  06-gallery2.html  Plates continued + field notes index
  07b-handouts.html three printable one-pagers with activities
  08-coda.html      his own one-line version + sources & honesty
data/graph.json   exported data model
figs/             downloaded source figures + provenance README
build.sh          cat parts/*.html > index.html
index.html        generated — never hand-edit
design-plan.md    palette/type/layout rationale
```

## Build

```sh
./build.sh    # regenerates index.html from parts/
```

Parts sort by filename; insert with `01b`, `07b` rather than renumbering.
The output is Artifact page *content* (no doctype/html/head/body), themed for
light, dark, and system-default.

## Honesty rules

Every claim links to a source; the interpretation is labelled as
interpretation; reproduced figures are CC BY only, with full attribution in the
page and in `figs/README.md`. Citation counts are from Google Scholar,
retrieved August 2026.

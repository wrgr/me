# The Unified Theory of Karla Gray-Roncal

An illustrated argument that a CV showing two unrelated careers — twenty-two years of
human-factors engineering at a defence laboratory, then multiple sclerosis neurology —
is **one job held continuously since 2003**: she instruments the interface between a
person and a system that is judging them.

**Live artifact:** https://claude.ai/code/artifact/8999f6c7-0b6b-410b-90c1-6df4656e9c6c

Built with the method in [`../RESEARCH-STORY-PLAYBOOK.md`](../RESEARCH-STORY-PLAYBOOK.md).

## The theory, in three laws

1. **When a person appears to fail a system, instrument the system.**
2. **An outcome nobody schedules is an outcome nobody sees.**
3. **Measure the obvious explanation properly, so that what survives it is real.**

The ordering axis is **how close the measuring instrument gets to the person** — a
console, a ward, a benchmark, a test in the patient's own hands, the body itself, a
question nobody had asked, a conversation. Median year rises monotonically along it:
2009, 2015, 2019, 2019.5, 2024.5, 2024.5, 2026.

## Layout

```
parts/            ordered page fragments — edit these, never index.html
  01-base.html      tokens, base CSS, hero (sonar-waterfall canvas)
  01b-converge.html Fig. A — the same nineteen works filed twice
  01c-theory.html   the three laws + where the theory strains
  02-data.html      SUBJECT data object: papers, related work, keywords, edges
  03-graph.html     Fig. 1 — related-work graph engine
  04-story.html     Fig. 2 — the seven-rung spine + the seven acts
  05-gallery.html   Plates I–X
  06-gallery2.html  Plates XI–XIX
  07-realfigs.html  the three CC BY figures + what the licences forbid
  07b-handouts.html three printable one-pagers with group activities
  08-coda.html      her own words + sources & honesty
data/graph.json   exported data model
figs/             extracted source figures + provenance README
build.sh          cat parts/*.html > index.html
index.html        generated — never hand-edit
design-plan.md    palette/type/layout rationale
```

## Build

```sh
./build.sh    # regenerates index.html from parts/
```

Parts sort by filename; insert with `01b`, `07b` rather than renumbering. The output is
Artifact page *content* (no doctype/html/head/body), themed for light, dark and
system-default.

## Honesty

The theory is **an interpretation** and the page says so. Thread colours, the seven-rung
ladder, and every dashed edge in the graph are ours; solid graph edges are real citation
edges from reference lists. Citation counts are OpenAlex, August 2026 — she has no
Google Scholar profile and her ORCID is empty. Four items exist only in her CV and are
marked as such; two more are from a classified symposium and cannot be checked by
anyone. Reproduced figures are CC BY 4.0 only, with full attribution here, in
`figs/README.md`, and on the page.

# Playbook: The Unified Theory of ⟨Person⟩

A reusable method for turning one researcher's publication record into an illustrated,
Pixar-theory-style web page: a single argument that their scattered-looking work is one body of
work, with a related-work graph, a plain-language writeup of every paper, bespoke illustrations,
and outreach handouts.

Written to be executed from a clean context. You need nothing from any previous run.

---

## 0. What you are making

One self-contained HTML page, published as an Artifact and committed to a repo, containing:

| Section | Purpose |
|---|---|
| **Hero** | The subject's central object, rendered live (canvas/SVG). States the thesis in one sentence. |
| **Fig. A — scattered → sorted** | The same publications shown twice: strewn across unrelated fields, then resolving into one ordered structure. The thesis as a picture. |
| **The theory** | Three "laws" the bibliography obeys. |
| **Fig. 1 — related-work graph** | Interactive. Their papers + cited prior work + citing work + shared-idea bridge nodes. |
| **Fig. 2 — the spine** | Their papers re-sorted along whatever axis the theory says is real (scale, time, abstraction). |
| **The story** | Acts, in the order the spine implies. Every paper linked explicitly. |
| **Plates I–N** | One bespoke illustration + plain-language writeup + key findings + source link per publication. |
| **Real figures** | Actual figures from any openly-licensed papers, with attribution. |
| **Handouts** | The story for kids, for peers, for the public — each with a group activity. Print-optimised. |
| **Coda** | The subject's own statement of the theory, if they have made one. |

**Non-negotiable:** every claim links to its source, and the interpretation is labelled as
interpretation. You are writing an argument about real people's real work.

---

## 1. Inputs to collect before starting

Ask the user for whichever of these they have; don't block on the rest.

- **Google Scholar profile URL** — the canonical publication set. Use its citation counts.
- **Personal site** — bio, framing, awards, outreach, how they describe themselves.
- **ORCID** — catches patents, datasets and conference papers Scholar misses.
- **Anything they consider central** that a bibliography wouldn't show: a talk, an essay, a
  podcast, a piece of art. This is usually where the theory is hiding.

If the subject is the user, ask what they think the through-line is — then verify it independently
rather than adopting it. If they're wrong, the page is more interesting, and you should say so.

---

## 2. Phase 1 — Research (parallelise hard)

Fetch the Scholar profile yourself first to get the publication list. Then fan out **one subagent
per cluster of publications**, running concurrently. Three to four agents is usually right.

### Agent prompt template

> Research ⟨full citation⟩. Try these sources in order: PubMed Central, europepmc.org, Semantic
> Scholar API, Crossref API, the publisher page, ResearchGate, OSF, any preprint.
>
> I need, in detail:
> 1. Full abstract, verbatim where possible.
> 2. What was actually done — methods, materials, the specific design decisions and why.
> 3. Every quantitative result: sample sizes, percentages, yields, accuracies, durations,
>    thresholds. Exact numbers.
> 4. The 3–5 **coolest, most illustratable** findings — things that would make a great picture.
>    Vivid described morphologies, surprising comparisons, memorable phrases the authors coined.
> 5. Key cited prior work and any citing work, as real titles + authors + years, for a citation
>    graph.
> 6. Anything internally inconsistent in the paper, so I don't repeat an error.
>
> Return structured markdown. **Mark anything you could not verify as UNCERTAIN. Do not invent
> numbers.** Give the DOI and a working URL for everything.

### Rules for this phase

- **Never fabricate a number.** If an agent flags UNCERTAIN, either verify it yourself or leave it
  out. A page like this lives or dies on being checkable.
- **Chase the framing sources too** — profile interviews, alumni magazine pieces, talk
  descriptions. These carry the origin story and the quotable lines.
- **Ask for what the paper does NOT contain.** Absent controls, unmeasured outcomes, and stated
  limitations are often the most honest thing you can say about a body of work.

### Access gotchas that will cost you time

| Source | Behaviour | Workaround |
|---|---|---|
| ScienceDirect / Elsevier | 403 to automated fetches | PubMed abstract, Europe PMC, publisher-agnostic mirrors |
| Springer / `link.springer.com` | 303 redirect to an IdP | Use the PMC or BMC copy instead |
| `peer.asee.org` HTML pages | 403 | The PDF at `peer.asee.org/⟨id⟩.pdf` serves fine |
| IEEE Xplore | paywalled | Authors often post to OSF; check the DOI on Semantic Scholar for an open PDF |
| AIChE / Confex meetings | human pages 403 | Undocumented JSON API: `⟨host⟩/meetingapi.cgi/Paper/⟨id⟩` |
| Europe PMC full text | works well | `.../rest/PMC⟨id⟩/fullTextXML` gives the whole JATS document |

---

## 3. Phase 2 — Find the theory (the part that isn't mechanical)

This is the actual work. A weak version of this page is a nicely-designed list. The difference is
whether you find a claim that is **surprising, defensible, and specific**.

### What to look for, in order of payoff

1. **Structural isomorphism.** Take the two or three papers that look *least* related. Write each
   as: *what interface is being described / who or what is judging it / what is proposed instead.*
   If those three slots fill the same way across unrelated fields, that is your theory.
   *(In the worked example: a pharmaceutical QC paper, a neuroscience review and a paper about
   internships all turned out to be "a selective barrier, judged by an uncalibrated gatekeeper,
   fixed by building a truer model.")*

2. **The subject's own thesis.** Researchers who have given a talk, written an essay or chosen an
   unusual self-description have usually already named their through-line. If you find it, the page
   should quote it and credit them — the theory is *theirs*, and you are showing the evidence.
   Check the coda for it, not the top; it lands harder as a reveal.

3. **A real ordering axis.** Date and journal are the boring axes. Look for one that carries
   information: physical scale, level of abstraction, distance from the patient, who the work is
   for. Sorting the bibliography by it should produce a monotone climb. If it doesn't, it's the
   wrong axis.

4. **The loop-closing citation.** Check whether anyone from the origin story appears in a later
   reference list. Mentors, camp lecturers, the author of the paper that started it. This is rare
   and it is gold. **Verify the identity before asserting it** — same field, same institution and
   same subject is suggestive, not proof. If the subject is available, ask.

5. **The keystone paper.** Usually one paper states the theory most nakedly — often a conference
   abstract nobody has cited. Give it the same weight as the high-citation work.

### Then write three laws

Compress the theory into three claims, each falsifiable against the bibliography, each with
evidence named. If you can't get to three, you don't have a theory yet — you have an observation.

### Honesty rules

- Label the theory as an interpretation, explicitly, in the sources section.
- Never bend a paper to fit. If one publication genuinely doesn't fit, say so — it is more
  convincing than a theory with no exceptions.
- Distinguish **citation edges** (real, from reference lists) from **thematic edges** (yours). Draw
  them differently and say so in the legend.

---

## 4. Phase 3 — Design

Load the `artifact-design` skill before writing any markup. Then derive the identity from the
subject's own world, not from a template.

### Palette

Find the colours the subject actually works in. Their instruments, their materials, their
field's visual conventions. *(Worked example: fluorescence microscopy channels — near-black
imaging field, DAPI cyan, GFAP green, pericyte magenta. When the real figures were later embedded,
they matched the page, because the page had been built from the same convention.)*

Define 4–6 named tokens. Assign each **thread** of the career its own hue and use it consistently
across the graph, the story, the plates and the ladder — the colour must mean something.

### Type

Three roles: a display face with real personality, a readable long-form body face (a serif is right
for a story), and a mono for labels, data and figure captions. Avoid the current defaults
(Inter, Space Grotesk, cream-and-terracotta, purple-blue gradients).

### Theming — the classic failure mode

Define the **complete light palette on bare `:root`**, then redefine *only* the tokens under both
`@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) }` **and**
`:root[data-theme="dark"]`. Never let a colour's only definition sit inside a media or
`[data-theme]` block. Give `body` an explicit token background. Before publishing, grep the
stylesheet for colours declared only inside those blocks.

### Illustration

One bespoke SVG per publication, drawn from what the paper actually does — not a generic icon.
Use the authors' own vivid descriptions as the brief. Every SVG needs a real `role="img"` and a
descriptive `aria-label`. Use CSS custom properties for every stroke and fill so illustrations
theme with the page.

For generative or animated backdrops use Canvas, and read theme colours via
`getComputedStyle(document.documentElement).getPropertyValue('--token')`, re-reading on a
`matchMedia('(prefers-color-scheme: dark)')` change. Honour `prefers-reduced-motion` by rendering
one static frame.

For any force-directed layout, seed a **deterministic PRNG** (mulberry32 with a fixed seed) so the
graph is identical on every load. `Math.random()` is fine in a browser, but a layout that jumps
between reloads looks broken.

---

## 5. Phase 4 — Build system

Keep it trivial. One page assembled from ordered fragments:

```
project/
  parts/
    01-base.html        tokens, base CSS, hero
    01b-converge.html   scattered → sorted figure
    01c-theory.html     the three laws
    02-data.html        <script> const SUBJECT = {...}  — papers, related, keywords, edges
    03-graph.html       graph styles + engine (reads the data object)
    04-story.html       the spine diagram + the acts
    05-gallery.html     plates, first half + any embedded real figures
    06-gallery2.html    plates, second half
    07b-handouts.html   three audiences, three activities, print CSS
    08-coda.html        closing + sources + footer
  data/graph.json       exported data model
  figs/                 downloaded source figures + provenance README
  build.sh              cat parts/*.html > index.html
  index.html            generated — never hand-edit
  README.md
```

`build.sh` is literally:

```sh
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
: > index.html
for f in parts/*.html; do cat "$f" >> index.html; printf '\n' >> index.html; done
```

Parts sort by filename, so insert with `01b`, `07b` rather than renumbering.

**Write to `parts/`, never to `index.html`.** If a merge conflicts on `index.html`, resolve the
parts and regenerate — never hand-resolve a build artifact.

### Artifact page rules

Write the file as page *content*: a `<title>`, a Google Fonts `<link>`, `<style>`, then the body
markup. No `<!DOCTYPE>`, `<html>`, `<head>` or `<body>` — those are added at publish time.
Everything else must be inline or a data URI; a strict CSP blocks all external hosts except Google
Fonts.

### Data model shape

```js
var SUBJECT = {
  papers:   [{ id, short, storyTitle, title, authors, venue, year, citations,
               doi, url, thread, form, scale, plain }],
  related:  [{ id, kind: 'ref'|'cite', thread, short, title, authors, venue, year, doi, note }],
  keywords: [{ id, label, thread: 'shared', title, note }],   // the cross-thread bridges
  edges:    [{ s, t, type: 'thread'|'cites'|'kw' }]
};
```

The `keywords` nodes are what make the graph an argument rather than a bibliography — they are the
shared ideas that connect otherwise unconnected threads. Write their `note` fields carefully; they
carry the theory.

---

## 6. Phase 5 — Real figures and licensing

Reproducing the actual figures is worth doing, and is only sometimes allowed.

**Check the licence per paper, individually.** Open-access is not one thing.

- **CC BY / CC BY-SA** → reproducible with attribution. Most BMC, PLOS, Frontiers, Nature
  Communications, eLife.
- **CC BY-NC** → check whether the use is non-commercial; usually fine for an educational page, but
  say so.
- **"Free to read"** → *not* a licence. ACS, Elsevier and IEEE open-access-to-view articles are
  usually all-rights-reserved. Do not reproduce.

For anything you do reproduce, state all five: **author, title/source, year, licence with a link,
and what you changed.** Put it under the figures *and* in the page's sources list. Keep the
unmodified originals in `figs/` with a provenance README.

Practical: download at full resolution, resize to ~1100–1200 px wide, JPEG q78–80, embed as
data URIs. Budget ~250 KB per figure; the artifact limit is 16 MB. Add `loading="lazy"`,
`decoding="async"`, intrinsic `width`/`height`, and real alt text.

**Open every image before publishing it.** You are responsible for what you put on the page.

---

## 7. Phase 6 — Validation

Run before every publish:

```sh
./build.sh
python3 - <<'PY'
import re, subprocess
src = open('index.html').read()
for i, b in enumerate(re.findall(r'<script>(.*?)</script>', src, re.S)):
    open(f'/tmp/b{i}.js','w').write(b)
    if subprocess.run(['node','--check',f'/tmp/b{i}.js'],capture_output=True).returncode:
        print("JS FAIL", i)
bad = [t for t in ['section','article','div','svg','g','style','script','figure','figcaption','p','li']
       if len(re.findall(rf'<{t}[\s>]',src)) != len(re.findall(rf'</{t}>',src))]
print("tag mismatches:", bad or "none")
ids = re.findall(r'\sid="([^"]+)"', src)
print("dup ids:", [i for i in set(ids) if ids.count(i) > 1] or "none")
print("dup class attrs:", len(re.findall(r'<[^>]*\sclass="[^"]*"[^>]*\sclass="', src)))
imgs = len(re.findall(r'<img ', src))
print("imgs:", imgs, "| all have alt:", imgs == len(re.findall(r'<img [^>]*\salt="', src)))
print("size: %.2f MB" % (len(src.encode())/1048576))
PY
```

Then check by hand:

- [ ] Renders correctly in light, dark, **and** system-default (no `data-theme` stamp)
- [ ] No horizontal page scroll at 360 px; wide content scrolls inside its own container
- [ ] Graph is keyboard-navigable and every node has an accessible name
- [ ] Every publication has a working source link
- [ ] Every number on the page traces to a source
- [ ] The interpretation is labelled as interpretation
- [ ] Prints cleanly if you claimed it does

---

## 8. Phase 7 — Publish and ship

1. Publish the Artifact. Set a `<title>` that is a **name**, not a summary — two to four words,
   distinctive in a gallery. Pass a one-sentence `description` and a stable emoji `favicon`.
   Republishing the same file path keeps the URL.
2. Commit sources and the generated page; put the artifact URL in the README.
3. Open a PR whose body explains **what you found**, not just what you changed. The research
   findings are the interesting part of the diff.

### Git gotchas

- After a **squash merge**, your branch's history is no longer an ancestor of `main` even though the
  content is identical. The next PR from a branch built on the old head will conflict.
  Start each round with `git checkout -B ⟨branch⟩ origin/main`.
- If you must force-push, **verify first** that the remote branch holds only already-merged content
  (`git log --oneline origin/⟨branch⟩ ^origin/main`, then confirm the content is in `main`), and use
  `--force-with-lease`.
- On a real conflict, merge `origin/main` in, resolve the **parts**, regenerate `index.html`, and
  verify both sides' features survived before committing.

---

## 9. Repo layout for multiple subjects

One subfolder per person, self-contained so any of them can be lifted into its own repo later:

```
repo/
  RESEARCH-STORY-PLAYBOOK.md
  ⟨person-slug⟩/
    parts/  data/  figs/  build.sh  index.html  README.md  design-plan.md
```

Each subfolder gets its own palette and typography. **Do not build a shared template** — the design
being derived from that specific person's world is the point, and a shared theme would flatten
exactly the thing that makes each page feel like its subject.

---

## 10. Anti-patterns

- **A list with nice CSS.** If the page doesn't make a claim, it isn't done.
- **Theory by assertion.** "All her work is about connection!" is not a theory. A theory names a
  repeated structure and points at the evidence.
- **Laundering uncertainty.** Hedging everything is as bad as hedging nothing. Verify, then state
  plainly; where you genuinely can't verify, say which part.
- **Hagiography.** Specific and accurate is more flattering than effusive. Let the findings do it.
- **Generic illustration.** A stock brain icon is worse than no icon. Draw what the paper describes.
- **Colour without meaning.** If threads are coloured, the colour must survive across every section.
- **Reproducing figures you didn't check the licence on.** Or didn't look at.

---

## 11. Quick start

```
1. Get Scholar URL + personal site + ORCID.
2. Fetch the Scholar profile. List every publication.
3. Fan out research agents, one per cluster. Use the prompt in §2.
4. While they run: draft the design plan (§4) and the base CSS.
5. When they return: find the theory (§3). Write the three laws.
6. Build data model → graph → spine → acts → plates → handouts → coda.
7. Check licences, embed any CC-BY figures with full attribution.
8. Validate (§7). Publish. PR with the findings in the body.
```

The research phase is cheap and parallel. The theory is the expensive part. Budget accordingly.

# CV sources

Two sources of truth feed both the PDF and the website:

- **`../_data/cv/*.yml`** — career facts (experience, education, programs,
  teaching, skills, awards, service). `yaml2tex.py` renders these into
  `will_cv.tex`; the website reads the same YAML via `site.data.cv.*`.
- **`will_cv.bib`** — publications, with the `\nocite` lists in `will_cv.tex`
  deciding paper / talk / poster.

**`will_cv.tex` is generated. Do not hand-edit it** — edit the YAML and rerun
`yaml2tex.py`. The one hand-maintained part of the .tex is the publications
block (`\nociteconf` / `\nocitetalks` / `\nociteposter`), which the generator
carries over verbatim on each run.

The `.cls`/`.sty`/`.bst` files are the bundled moderncv/multibib support files —
vendored so the CV builds without a full TeX Live package set.

## Regenerate everything

```bash
python3 cv/yaml2tex.py     # _data/cv/*.yml -> cv/will_cv.tex
python3 cv/bib2jekyll.py   # cv/will_cv.bib -> _bibliography/papers.bib
# then rebuild the PDF, below
```

## Rebuild the PDF

```bash
cd cv
pdflatex -interaction=nonstopmode will_cv.tex
for c in conf talks poster other; do bibtex $c; done   # multibib: one pass per category
pdflatex -interaction=nonstopmode will_cv.tex
pdflatex -interaction=nonstopmode will_cv.tex
cp will_cv.pdf ../assets/pdf/cv.pdf
```

The three `pdflatex` passes are needed to resolve the multibib references.
Check `grep -c '^!' will_cv.log` — it should be `0`.

## Regenerate the website bibliography

```bash
python3 cv/bib2jekyll.py     # from the repo root
```

This reads `cv/will_cv.bib` plus the `\nocite…` lists in `cv/will_cv.tex` and
writes `_bibliography/papers.bib`. The `\nocite` lists decide the category:

| LaTeX command | site category | shown under |
| --- | --- | --- |
| `\nociteconf{…}` | `paper` | Articles & proceedings |
| `\nocitetalks{…}` | `talk` | Invited talks |
| `\nociteposter{…}` | `poster` | Posters |

Entries in `will_cv.bib` that appear in **no** `\nocite` list are skipped — that
is how stale "In Preparation"/"In Review" drafts and superseded duplicates stay
off the site. One exception is whitelisted in `RESCUE` inside `bib2jekyll.py`.

The script also applies, all editable at the top of `bib2jekyll.py`:

- `SELECTED` — cite keys starred and featured on the homepage. The current set is
  deliberately chosen to span all six domains, not just the highest-impact
  venues, since the domain blend is the site's premise.
- `DOMAIN_OVERRIDES` — hand-assigned domain tags where keyword matching is wrong.
- `DOI_OVERRIDES` — DOIs verified against Crossref/doi.org.

## Adding a role, award, or course

Edit the matching file in `../_data/cv/`, then run `python3 cv/yaml2tex.py` and
rebuild the PDF. Tag the entry with `domains: [neuro, ai]` (keys from
`_data/domains.yml`) and it also appears on the website's domain cards and, for
research-program bullets, as a card in the homepage's Research programs grid.
Set `featured: true` on an award or service entry to surface it on the homepage.

## Adding a publication

1. Add the entry to `will_cv.bib` (include a `doi` if one exists; if not,
   add a `url` — talks and posters usually don't have a DOI, so they need a
   `url` pointing at a durable page: a conference program/archive entry, a
   university seminar-series page, a figshare/OSF/Zenodo deposit, etc.).
2. Add its cite key to the right `\nocite…` list in `will_cv.tex`
   (`\nociteconf` for papers, `\nocitetalks` for talks, `\nociteposter` for
   posters — this is what puts it on the website under the right section).
3. If it should be featured, add the key to `SELECTED` in `bib2jekyll.py`.
4. If the venue is open access, drop a copy of the PDF at
   `../assets/pdf/papers/<cite-key>.pdf` — `bib2jekyll.py` picks it up
   automatically and adds a `pdf` field. Skip this for paywalled venues
   (IEEE Xplore, Cell, Nature Methods, ACM, etc.) — link out via `doi`/`url`
   instead, don't self-host copyrighted publisher PDFs.
5. Rebuild the PDF, then run `python3 cv/bib2jekyll.py`.

## Author names: cite as published

**Do not normalise his name across entries.** Each entry carries the form that
appeared on that publication, and the record shows a real change:

- **2010 and earlier** — `Gray, William R`, before the surname change. His
  first-author DARPA poster that year is under "Gray" while Vogelstein's OHBM
  poster already lists him as "Gray Roncal", so 2010 carries both.
- **2010–2017** — unhyphenated, `{Gray Roncal}, William` (the braces keep the
  two-word surname together, or BibTeX treats "Gray" as a first name)
- **2018** — transition year; both forms appear
- **2019 onward** — hyphenated, `Gray-Roncal, William`

Initials-only variants (`{Gray Roncal}, W R`, `W. Gray-Roncal`) are correct
where the paper's other authors are also initialled. `William Roberts
Gray-Roncal` on one 2023 entry is as-published too.

Highlighting does not depend on the form: `_layouts/bib.html` bolds any author
whose display name starts with "W" and whose surname either contains "Roncal"
or is exactly "Gray", so all three eras and every initialled variant are
caught. That test also correctly
excludes **Karla Gray-Roncal** and **Maria Roncal**, who are different people
and appear as co-authors — never "fix" their names to match his.

What *is* worth fixing is malformed BibTeX, which is different from historical
variation. Two were repaired and should stay repaired:

- `Roncal, Will {Gray Roncal}` rendered "Will Gray Roncal **Roncal**" — the
  braced part parses as a *first* name. Now `{Gray Roncal}, Will`.
- `{Roncal, Gray}, William R` put the comma inside the braces. Now
  `{Gray Roncal}, William R`.

## Gotchas

- `\cventry`'s last argument is **not** `\long` — a blank line inside it breaks
  the build. `yaml2tex.py` never emits one; keep it that way if you touch the
  generator.
- A bare `&` in a YAML value is a LaTeX alignment character and breaks the
  build. `yaml2tex.py`'s `clean()` escapes it; anything bypassing `clean()`
  must escape it too.
- Keep `will_cv.bib` free of raw non-ASCII characters; use LaTeX escapes
  (`Villafa{\~n}e`). `bib2jekyll.py` escapes what it emits, because
  bibtex-ruby reads US-ASCII by default and a stray `ñ` fails the Jekyll build.
- Corporate authors need double braces: `author={{The MICrONS Consortium}}`,
  otherwise BibTeX renders it as a person ("T.~M. Consortium").

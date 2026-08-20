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

1. Add the entry to `will_cv.bib` (include a `doi` if one exists).
2. Add its cite key to the right `\nocite…` list in `will_cv.tex`.
3. If it should be featured, add the key to `SELECTED` in `bib2jekyll.py`.
4. Rebuild the PDF, then run `python3 cv/bib2jekyll.py`.

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

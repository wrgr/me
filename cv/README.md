# CV sources

`will_cv.tex` (moderncv) + `will_cv.bib` are the source of truth for **both** the
PDF and the website's publication list. The `.cls`/`.sty`/`.bst` files are the
bundled moderncv/multibib support files — they are vendored so the CV builds
without a full TeX Live package set.

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

## Adding a publication

1. Add the entry to `will_cv.bib` (include a `doi` if one exists).
2. Add its cite key to the right `\nocite…` list in `will_cv.tex`.
3. If it should be featured, add the key to `SELECTED` in `bib2jekyll.py`.
4. Rebuild the PDF, then run `python3 cv/bib2jekyll.py`.

## Gotchas

- `\cventry`'s last argument is **not** `\long` — a blank line inside it breaks
  the build. Use `\vspace{…}` between blocks instead.
- Keep `will_cv.bib` free of raw non-ASCII characters; use LaTeX escapes
  (`Villafa{\~n}e`). `bib2jekyll.py` escapes what it emits, because
  bibtex-ruby reads US-ASCII by default and a stray `ñ` fails the Jekyll build.
- Corporate authors need double braces: `author={{The MICrONS Consortium}}`,
  otherwise BibTeX renders it as a person ("T.~M. Consortium").

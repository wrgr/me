# grayroncal.com (staging: wrgr.github.io/me)

Academic homepage for William Gray-Roncal, PhD — built with Jekyll and
jekyll-scholar. One method, six domains: neuro & connectomics, AI & data,
defense & space, learning engineering, workforce, public health.

## Local development

```bash
bundle config set path vendor/bundle
bundle install
bundle exec jekyll serve --livereload
# → http://127.0.0.1:4000/me/
```

## Where things live

| What | Where |
| --- | --- |
| **Career facts (source of truth)** | `_data/cv/*.yml` — experience, education, awards, teaching, service, programs |
| **Publications (source of truth)** | `cv/will_cv.bib` + `\nocite` lists in `cv/will_cv.tex` |
| Homepage sections | `index.html` |
| Six domain blurbs | `_data/domains.yml` (roles are derived, not stored) |
| Software & datasets | `_data/software.yml` |
| Writing & ideas | `_data/writing.yml` |
| Profile links / CV path | `_data/profiles.yml` |
| Generated CV LaTeX | `cv/will_cv.tex` — **do not hand-edit** |
| Generated bibliography | `_bibliography/papers.bib` — **do not hand-edit** |
| Publication entry template | `_layouts/bib.html` |
| Design tokens (colors, dark mode) | `_sass/_tokens.scss` |

## One source of truth

Career facts live once, in `_data/cv/*.yml`, and flow to both artifacts:

```
_data/cv/*.yml ──┬── cv/yaml2tex.py ──▶ cv/will_cv.tex ──▶ assets/pdf/cv.pdf
                 └── site.data.cv.*  ──▶ website (Liquid reads the YAML directly)

cv/will_cv.bib ───── cv/bib2jekyll.py ─▶ _bibliography/papers.bib ─▶ publications
```

Nothing on the site restates a CV fact. Domain cards, for instance, do not store
their own role lists — `_includes/domain-roles.html` finds every entry in
`_data/cv/*.yml` tagged with that domain and renders it. Tag a new grant with
`domains: [neuro]` and it appears on the neuro card and in the CV at once.

YAML values may contain LaTeX (`\textbf{...}`, `---`, `\%`) because the CV
consumes them too; the `texclean` Liquid filter in `_plugins/` renders those as
HTML for the web.

### Regenerating

```bash
python3 cv/yaml2tex.py    # _data/cv/*.yml  -> cv/will_cv.tex
python3 cv/bib2jekyll.py  # cv/will_cv.bib  -> _bibliography/papers.bib
```

Then rebuild the PDF — see [cv/README.md](cv/README.md).



## Deployment

GitHub Actions (`.github/workflows/deploy.yml`) builds on every PR and
deploys to GitHub Pages on push to `main` (jekyll-scholar requires the
Actions build — the classic Pages builder can't run it).

One-time repo setting: **Settings → Pages → Source → "GitHub Actions"**.

### Moving to grayroncal.com later

1. Add a `CNAME` file containing `grayroncal.com`
2. In `_config.yml`: set `url: https://grayroncal.com` and `baseurl: ""`
3. Point DNS A/AAAA records at GitHub Pages; enforce HTTPS
4. Then flip the `comingSoon` flag in capabilitymatters' `experiments.astro` (and its pinned test)

All internal links go through `relative_url`, so no other changes are needed.

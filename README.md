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
| Homepage sections | `index.html` |
| Six domain cards | `_data/domains.yml` |
| Project & writing cards | `_data/projects.yml` |
| Profile links / CV path | `_data/profiles.yml` |
| Publications (generated) | `_bibliography/papers.bib` |
| Publication entry template | `_layouts/bib.html` |
| Design tokens (colors, dark mode) | `_sass/_tokens.scss` |
| **CV + publication source of truth** | `cv/` — see [cv/README.md](cv/README.md) |

### Publications and CV

`cv/will_cv.tex` + `cv/will_cv.bib` are the source of truth for **both** the CV
PDF and the site's publication list. Do not hand-edit
`_bibliography/papers.bib` — it is generated:

```bash
python3 cv/bib2jekyll.py
```

That derives each entry's category (paper / talk / poster) from the `\nocite`
lists in the CV, adds `domain=` chips and `selected=` stars, and normalizes the
formatting. Full workflow and gotchas: [cv/README.md](cv/README.md).

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

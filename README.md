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
| Publications (BibTeX) | `_bibliography/papers.bib` |
| Publication entry template | `_layouts/bib.html` |
| Design tokens (colors, dark mode) | `_sass/_tokens.scss` |

### Publications

`_bibliography/papers.bib` is the single source of truth. Custom fields:

- `selected={true}` — shows the entry on the homepage with a ★
- `domain={neuro,ai}` — comma-separated keys from `_data/domains.yml`, rendered as colored chips
- `pdf=`, `code=`, `website=` — optional buttons per entry

### CV

Set `cv: /assets/pdf/cv.pdf` in `_data/profiles.yml` once the PDF exists —
the nav and contact rows pick it up automatically.

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

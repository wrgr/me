# will.grayroncal.com

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

GitHub Actions (`.github/workflows/deploy.yml`) builds on every PR and deploys
to GitHub Pages on push to `main`. jekyll-scholar is not on the GitHub Pages
whitelist, so the classic Pages builder cannot build this site — the Actions
build is required, not a preference.

### Going live at will.grayroncal.com

Three things must agree: the DNS record, the `CNAME` file, and the repo setting.

1. **DNS** — at whatever host serves `grayroncal.com`, add one record:

   | Type | Name / Host | Value |
   | --- | --- | --- |
   | `CNAME` | `will` | `wrgr.github.io.` |

   A subdomain needs only this. The `A`/`AAAA` records GitHub documents are for
   apex domains (`grayroncal.com`) and are **not** used here. The value is the
   *user* domain `wrgr.github.io`, with no `/me` path and no repo name — some
   DNS UIs require the trailing dot, others add it for you.

2. **Repo setting** — Settings → Pages → Source → **"GitHub Actions"**, then set
   Custom domain to `will.grayroncal.com`. Once the certificate provisions
   (usually minutes, occasionally up to 24h), tick **Enforce HTTPS**.

3. **`CNAME` file** — already in the repo root, containing `will.grayroncal.com`.
   Jekyll copies it into `_site/`, and the deploy workflow fails the build if it
   ever goes missing. Deleting it unbinds the domain.

Check propagation with `dig +short will.grayroncal.com` — it should return
`wrgr.github.io` followed by GitHub's IPs.

### Moving the site elsewhere

`_config.yml` holds `url` and `baseurl`; every internal link goes through
`relative_url`, so a move is those two values plus the `CNAME` file. Serving
from a subpath again (say `wrgr.github.io/me`) means setting
`baseurl: "/me"` and deleting `CNAME` — nothing in the templates changes.

### After the domain resolves

`wrgr/capabilitymatters` lists this site on its Experiments page behind a
`comingSoon: true` flag, pinned by a test. Both must change in one commit:
remove the flag in `src/pages/experiments.astro`, and remove
`test_grayroncal_is_coming_soon` in `tests/test_experiments_page.py`. Note that
page currently points at `grayroncal.com`, so the URL needs updating to
`will.grayroncal.com` too.

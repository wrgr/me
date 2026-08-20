#!/usr/bin/env python3
"""Regenerate _bibliography/papers.bib from cv/will_cv.bib.

The CV is the single source of truth: this reads cv/will_cv.bib plus the
\\nocite lists in cv/will_cv.tex (which decide paper/talk/poster), and writes
the jekyll-scholar bibliography the site renders. Run after editing the CV:

    python3 cv/bib2jekyll.py

Adds: category (paper/talk/poster), domain tags, selected flags.
Cleans: \\href-in-title, booktitle jammed into title, brace noise.
Enriches: DOIs matched from the Crossref-harvested snapshot.
"""
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CVDIR = REPO / "cv"
DEST = REPO / "_bibliography" / "papers.bib"

# ---------------------------------------------------------------- parsing


def split_entries(text):
    """Yield (type, key, body) for each @entry in a bib file."""
    chunks = re.split(r"\n(?=@)", text)
    for chunk in chunks:
        m = re.match(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*)", chunk, re.S)
        if m:
            yield m.group(1).lower(), m.group(2).strip(), m.group(3)


def get_field(body, name):
    """Extract a brace- or quote-delimited field, brace-balanced."""
    m = re.search(rf"\b{name}\s*=\s*", body, re.I)
    if not m:
        return None
    i = m.end()
    while i < len(body) and body[i].isspace():
        i += 1
    if i >= len(body):
        return None
    if body[i] == "{":
        depth, j = 0, i
        while j < len(body):
            if body[j] == "{":
                depth += 1
            elif body[j] == "}":
                depth -= 1
                if depth == 0:
                    return body[i + 1 : j].strip()
            j += 1
        return None
    if body[i] == '"':
        j = body.index('"', i + 1)
        return body[i + 1 : j].strip()
    m2 = re.match(r"([^,\n}]+)", body[i:])
    return m2.group(1).strip() if m2 else None


# ---------------------------------------------------------------- cleaning

def clean_text(s):
    if not s:
        return s
    s = re.sub(r"\s+", " ", s).strip()
    # \href{url}{title} -> title  (url captured separately by extract_href)
    s = re.sub(r"\\href\{[^}]*\}\{(.*?)\}", r"\1", s)
    s = re.sub(r"\\textit\{(.*?)\}", r"\1", s)
    s = re.sub(r"\\textbf\{(.*?)\}", r"\1", s)
    s = re.sub(r"\\emph\{(.*?)\}", r"\1", s)
    s = s.replace("\\&", "&").replace("\\_", "_").replace("\\%", "%")
    s = s.replace("~", " ")
    # strip stray outer braces, keep interior protective braces
    s = s.strip()
    while s.startswith("{") and s.endswith("}"):
        inner = s[1:-1]
        depth = 0
        balanced = True
        for ch in inner:
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth < 0:
                    balanced = False
                    break
        if balanced and depth == 0:
            s = inner.strip()
        else:
            break
    s = re.sub(r"\s+", " ", s).strip().rstrip(",").strip()
    return s


def extract_href(s):
    if not s:
        return None
    m = re.search(r"\\href\{([^}]*)\}", s)
    return m.group(1) if m else None


def clean_authors(s):
    if not s:
        return s
    s = re.sub(r"\s+", " ", s).strip()
    # CV protects multi-word surnames with braces ({Gray Roncal}); we do our own
    # name parsing in _layouts/bib.html, so strip them for clean display.
    s = s.replace("{", "").replace("}", "")
    # the CV has stray commas before "and": "Foo, and Bar"
    s = re.sub(r",\s+and\s+", " and ", s)
    parts = [p.strip().strip(",").strip() for p in s.split(" and ")]
    out = []
    for p in parts:
        if not p:
            continue
        # "A, B" where neither looks like Last, First -> two authors run together
        if p.count(",") == 1:
            left, right = [x.strip() for x in p.split(",")]
            # Last, First pattern: right side is initials/first names (short, no multi-word surname feel)
            if left and right and " " in left and " " in right:
                out.extend([left, right])
                continue
        out.append(p)
    return " and ".join(out)


ACCENTS = {
    "\u00e1": "\\'a", "\u00e9": "\\'e", "\u00ed": "\\'i", "\u00f3": "\\'o", "\u00fa": "\\'u",
    "\u00c1": "\\'A", "\u00c9": "\\'E", "\u00cd": "\\'I", "\u00d3": "\\'O", "\u00da": "\\'U",
    "\u00f1": "\\~n", "\u00d1": "\\~N", "\u00fc": '\\"u', "\u00dc": '\\"U',
    "\u00e4": '\\"a', "\u00f6": '\\"o', "\u00e0": "\\`a", "\u00e8": "\\`e",
    "\u00e7": "\\c c", "\u00c7": "\\c C", "\u00e2": "\\^a", "\u00ea": "\\^e",
    "\u2013": "--", "\u2014": "---", "\u2019": "'", "\u2018": "`",
    "\u201c": "``", "\u201d": "''",
}


def ascii_fy(s):
    """Replace non-ASCII with LaTeX escapes; bibtex-ruby reads US-ASCII by default."""
    out = []
    for ch in s:
        if ord(ch) < 128:
            out.append(ch)
        elif ch in ACCENTS:
            out.append("{" + ACCENTS[ch] + "}")
        else:
            out.append(unicodedata.normalize("NFKD", ch).encode("ascii", "ignore").decode())
    return "".join(out)


def esc(s):
    """Escape for BibTeX value context."""
    if s is None:
        return None
    return ascii_fy(s.replace("&", "\\&"))


# ---------------------------------------------------------------- tagging

DOMAIN_RULES = [
    ("workforce", r"circuit|stem|workforce|trailblaz|curriculum|internship|cohort|"
                  r"recruitment|retention|talent|mentor|undergraduate|college|pipeline of|"
                  r"equitable|diverse|diversity|students"),
    ("learning", r"learning environment|human performance|training|engagement|teaching|"
                 r"education|benchmarking human|accelerat"),
    ("neuro", r"connectom|neuro|brain|synap|cortex|cortical|neuron|spine|dendri|"
              r"c\. elegans|elegans|mri|electron microscop|\bem\b|axon|circuit motif|"
              r"microns|thalamocortical|ring attractor|insect|nervous"),
    ("ai", r"machine learning|deep learning|self-supervised|computer vision|"
           r"algorithm|graph|classification|cloud|detection|segmentation|"
           r"inference|neural network|transfer learning|multimodal|agentic|"
           r"low-shot|generalization|isomorphism|analytics|pipeline|data"),
    ("health", r"clinical|covid|medicine|patient|disease|sclerosis|health"),
    ("defense", r"aerial|operational|satellite|visual search|swarm|defense|"
                r"asilomar|cbrne|autonom"),
]


# DOIs verified against Crossref/doi.org. Caveats worth knowing:
#   Reilly_2017  -> journal version is Front. Neuroinform. 12:74 (2018); CV dates it 2017
#   Cowley_2022b -> Sci Rep vol 13, published Feb 2023; CV dates it 2022
#   Kiar_2018, Lawrence_2021, Matelsky_2022 -> bioRxiv-only DOIs (no journal version)
#   Azabou_2021  -> DataCite arXiv DOI; no peer-reviewed venue confirmed
DOI_OVERRIDES = {
    "Kasthuri_2015": "10.1016/j.cell.2015.06.054",
    "Vogelstein_2018": "10.1038/s41592-018-0181-1",
    "Dyer_2017": "10.1523/ENEURO.0195-17.2017",
    "Vogelstein_2013": "10.1109/TPAMI.2012.235",
    "Hider_2022": "10.3389/fninf.2022.828787",
    "Cowley_2022a": "10.1038/s41598-022-08078-3",
    "Cowley_2022b": "10.1038/s41598-022-26294-9",
    "Reilly_2017": "10.3389/fninf.2018.00074",
    "Prasad_2020": "10.1038/s41597-020-00692-y",
    "Kiar_2018": "10.1101/188706",
    "Lawrence_2021": "10.1101/2021.11.01.466686",
    "Robinson_2022": "10.1038/s41598-022-05798-4",
    "Azabou_2021": "10.48550/arXiv.2102.10106",
    "Matelsky_2022": "10.1101/2022.06.01.494307",
    "Sanchez_2022": "10.3389/fninf.2022.828458",
    "GrayRoncal_2015a": "10.3389/fninf.2015.00020",
    "Cervantes_2023b": "10.18260/1-2--43271",
}

# Entries absent from the CV bib (which stops at 2024), DOI-verified separately.
EXTRA_ENTRIES = [
    ("""@article{microns2025functional,
  author = {{The MICrONS Consortium}},
  title = {Functional connectomics spanning multiple areas of mouse visual cortex},
  journal = {Nature},
  volume = {640},
  number = {8058},
  pages = {435--447},
  year = {2025},
  doi = {10.1038/s41586-025-08790-w},
  category = {paper},
  domain = {neuro,ai},
  selected = {true}
}""", 2025, "microns2025functional"),
    ("""@misc{wimbish2024em,
  author = {Wimbish, Miguel E. and Guittari, Nicole K. and Rose, Victoria A. and Rivera, Jorge L. and Rivlin, Patricia K. and Hinton, Mark A. and Matelsky, Jordan K. and Stock, Nicole E. and Wester, Brock A. and Johnson, Erik C. and Gray-Roncal, William R.},
  title = {{EM} and {XRM} Connectomics Imaging and Experimental Metadata Standards},
  howpublished = {arXiv:2401.15251},
  year = {2024},
  url = {https://arxiv.org/abs/2401.15251},
  category = {paper},
  domain = {neuro,ai}
}""", 2024, "wimbish2024em"),
]

SELECTED = {
    # Chosen to span all six domains, not just the highest-impact venues.
    "microns2025functional",  # Nature 2025          neuro, ai
    "Kasthuri_2015",          # Cell 2015            neuro
    "Vogelstein_2018",        # Nature Methods 2018  neuro, ai
    "Hider_2022",             # BossDB               neuro, ai
    "Matelsky_2021a",         # DotMotif             neuro, ai
    "Vogelstein_2013",        # IEEE TPAMI           ai
    "Dyer_2017",              # eNeuro X-ray         neuro
    "Cowley_2022a",           # human performance    learning
    "Cowley_2022b",           # COVID clinical ML    health
    "Rhodes_2021",            # aerial visual search defense
    "Johnson_2023",           # CIRCUIT curriculum   workforce
}

# Hand corrections where keyword matching is wrong or too thin.
DOMAIN_OVERRIDES = {
    "Kasthuri_2015": "neuro",
    "Vogelstein_2018": "neuro,ai",
    "Dyer_2017": "neuro",
    "Vogelstein_2013": "ai,neuro",
    "Matelsky_2021a": "neuro,ai",
    "Hider_2022": "neuro,ai",
    "Cowley_2022a": "learning,ai",
    "Cowley_2022b": "health,ai",
    "Bridgeford_2021": "ai,neuro",
    "GrayRoncal_2015b": "neuro,ai",
    "GrayRoncal_2015a": "neuro,ai",
    "Rhodes_2021": "defense,learning",
    "Robinson_2021": "neuro,ai",
    "Robinson_2022": "neuro,ai",
    "Azabou_2021": "ai",
    "Balwani_2021": "neuro,ai",
    "Johnson_2023": "workforce,learning",
    "Floryanzia_2024": "workforce",
    "Cervantes_2023a": "workforce,ai",
    "Cervantes_2023b": "workforce",
    "Sharp_2023": "workforce",
    "Encarnacion_2018": "workforce",
    "GrayRoncal_2018": "workforce",
    "VillafaneDelgado_2020": "workforce",
    "GrayRoncal_2011c": "neuro,learning",
    "GrayRoncal_2021b": "learning",
    "GrayRoncal_2021c": "workforce",
    "GrayRoncal_2019": "workforce",
    "GrayRoncal_2021": "neuro,ai",
    "Sanchez_2022": "neuro,ai",
    "Prasad_2020": "neuro",
    "Kiar_2018": "neuro,ai",
    "Kiar_2017": "neuro,ai",
    "Lawrence_2021": "neuro,ai",
    "Reilly_2017": "neuro,ai",
    "Kleissas_2017": "neuro,ai",
    "Kleissas_2013": "neuro,ai",
    "Kleissas_2014": "neuro,ai",
    "Matelsky_2020": "neuro,ai",
    "Matelsky_2021b": "neuro,ai",
    "Matelsky_2021c": "neuro",
    "Matelsky_2022": "neuro,ai",
    "Matelsky_2017": "ai",
    "Bishop_2021": "neuro,ai",
    "Johnson_2019": "ai",
    "Huynh_2019": "workforce,learning",
    "Drenkow_2020": "ai",
    "Drenkow_2017": "neuro,ai",
    "Mhembere_2013": "neuro,ai",
    "Burns_2013": "neuro,ai",
    "Kazhdan_2015": "neuro,ai",
    "GrayRoncal_2016a": "neuro,ai",
    "GrayRoncal_2016f": "neuro,ai",
    "GrayRoncal_2013c": "neuro,ai",
    "GrayRoncal_2012a": "neuro",
}


def guess_domains(key, title, venue):
    if key in DOMAIN_OVERRIDES:
        return DOMAIN_OVERRIDES[key]
    hay = f"{title} {venue}".lower()
    hits = [name for name, pat in DOMAIN_RULES if re.search(pat, hay)]
    if not hits:
        return "neuro"
    # cap at two, in the rule order (most specific first)
    return ",".join(hits[:2])


# ---------------------------------------------------------------- main

def main():
    cv_text = (CVDIR / "will_cv.bib").read_text(encoding="utf-8")
    tex = (CVDIR / "will_cv.tex").read_text(encoding="utf-8")

    def nocite_keys(cmd):
        m = re.search(rf"\\{cmd}\{{(.*?)\}}", tex, re.S)
        if not m:
            return set()
        return {k.strip() for k in m.group(1).split(",") if k.strip()}

    cats = {}
    for key in nocite_keys("nociteconf"):
        cats[key] = "paper"
    for key in nocite_keys("nocitetalks"):
        cats[key] = "talk"
    for key in nocite_keys("nociteposter"):
        cats[key] = "poster"

    doi_by_title = {}

    out = []
    stats = {"paper": 0, "talk": 0, "poster": 0}
    no_year = []
    inferred_year = []
    dropped = []

    for etype, key, body in split_entries(cv_text):
        raw_title = get_field(body, "title")
        url = extract_href(raw_title) or get_field(body, "url")
        title = clean_text(raw_title)
        author = clean_authors(clean_text(get_field(body, "author")))
        year = get_field(body, "year")
        journal = clean_text(get_field(body, "journal"))
        booktitle = clean_text(get_field(body, "booktitle"))
        doi = get_field(body, "doi")
        volume = get_field(body, "volume")
        number = get_field(body, "number")
        pages = get_field(body, "pages")
        howpub = clean_text(get_field(body, "howpublished"))
        address = clean_text(get_field(body, "address"))
        note = clean_text(get_field(body, "note"))

        # Some CV entries jam the booktitle into the title field:
        #   title={2023 IEEE ... Conference (ISEC)}, title={Real Title}
        m_double = re.findall(r"\btitle\s*=\s*\{", body)
        if len(m_double) > 1:
            # take the LAST title as the real one, the first as venue
            titles = []
            pos = 0
            while True:
                m = re.search(r"\btitle\s*=\s*", body[pos:], re.I)
                if not m:
                    break
                sub = body[pos + m.start():]
                val = get_field(sub, "title")
                if val is None:
                    break
                titles.append(val)
                pos = pos + m.start() + m.end() + len(val)
            if len(titles) > 1:
                if not booktitle:
                    booktitle = clean_text(titles[0])
                title = clean_text(titles[-1])

        cat = cats.get(key, "uncategorized")

        # Entries absent from every \nocite list are ones he left off his own CV:
        # stale "In Preparation"/"In Review" drafts and superseded duplicates
        # (e.g. Dyer_2016 -> Dyer_2017, GrayRoncal_2013 -> VESICLE). Honor that,
        # except for real published work that is clearly just an oversight.
        RESCUE = {"Cervantes_2023a": "paper"}
        if cat == "uncategorized":
            if key in RESCUE:
                cat = RESCUE[key]
            else:
                stats["dropped"] = stats.get("dropped", 0) + 1
                dropped.append(key)
                continue

        # Several talks/posters carry no year field; the cite key encodes it.
        if year is None:
            m_year = re.search(r"_(\d{4})", key)
            if m_year:
                year = m_year.group(1)
                inferred_year.append(key)
            else:
                no_year.append(key)

        stats[cat] = stats.get(cat, 0) + 1

        venue = journal or booktitle or howpub or address or ""
        domains = guess_domains(key, title or "", venue)

        if key in DOI_OVERRIDES:
            doi = DOI_OVERRIDES[key]
        if not doi:
            norm = re.sub(r"[^a-z0-9]", "", (title or "").lower())[:60]
            if norm in doi_by_title:
                doi = doi_by_title[norm]

        # entry type: keep articles as articles, everything with booktitle as inproceedings
        if cat in ("talk", "poster"):
            new_type = "misc"
        elif journal:
            new_type = "article"
        elif booktitle:
            new_type = "inproceedings"
        else:
            new_type = etype if etype in ("article", "inproceedings", "misc") else "misc"

        lines = [f"@{new_type}{{{key},"]

        def add(name, value, quote=True):
            if value:
                lines.append(f"  {name} = {{{value}}},")

        if not author and cat in ("talk", "poster"):
            author = "William Gray-Roncal"
        add("author", esc(author))
        add("title", esc(title))
        if new_type == "article":
            add("journal", esc(journal or venue))
        elif new_type == "inproceedings":
            add("booktitle", esc(booktitle or venue))
        else:
            add("howpublished", esc(venue or howpub))
        add("volume", volume)
        add("number", number)
        add("pages", pages)
        add("year", year)
        add("doi", doi)
        if url and not doi:
            add("url", url)
        add("note", esc(note))
        add("category", cat)
        add("domain", domains)
        if key in SELECTED:
            lines.append("  selected = {true},")
        lines[-1] = lines[-1].rstrip(",")
        lines.append("}")
        out.append(("\n".join(lines), int(year) if year and year.isdigit() else 0, key))

    # sort by year desc, then key
    out.sort(key=lambda x: (-x[1], x[2]))

    header = [
        "% Publications for wrgr.github.io/me",
        "% Source of truth: William Gray-Roncal's CV BibTeX (Feb 2026), converted for",
        "% jekyll-scholar. Custom fields:",
        "%   category = paper | talk | poster",
        "%   domain   = comma-separated keys from _data/domains.yml",
        "%   selected = true  -> featured on the homepage",
        "",
    ]
    text = "\n".join(header) + "\n\n".join(s for s, _, _ in out) + "\n"
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(text, encoding="utf-8")
    dest = DEST

    print("wrote", dest, len(out), "entries")
    print("categories:", stats)
    print("dropped (not on his CV):", dropped)
    print("year inferred from key:", inferred_year)
    print("still missing year:", no_year)
    print("selected present:", sorted(k for _, _, k in out if k in SELECTED))
    print("selected MISSING:", sorted(SELECTED - {k for _, _, k in out}))
    dois = sum(1 for s, _, _ in out if "doi = {" in s)
    print("entries with DOI:", dois)


if __name__ == "__main__":
    main()

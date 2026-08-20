#!/usr/bin/env python3
"""Generate cv/will_cv.tex from the canonical YAML in _data/cv/.

_data/cv/*.yml is the single source of truth: the website reads it directly
via Jekyll's `site.data.cv.*`, and this script renders the same facts into the
moderncv LaTeX that produces the PDF. Edit the YAML, never the .tex.

    python3 cv/yaml2tex.py        # regenerate cv/will_cv.tex
    python3 cv/bib2jekyll.py      # regenerate _bibliography/papers.bib

The publication lists (\\nocite blocks) are carried over from the existing
.tex, since cite-key membership is what decides paper/talk/poster in both
artifacts. See cv/README.md.

Values in the YAML may contain LaTeX (\\textbf{...}, ---, \\%) and are emitted
verbatim; the YAML is authored for both consumers, and the site strips markup
via the `texclean` filter in _plugins/.
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "_data" / "cv"
TEX = REPO / "cv" / "will_cv.tex"

RULE = "%% " + "=" * 74


def load(name):
    return yaml.safe_load((DATA / f"{name}.yml").read_text(encoding="utf-8"))


def section(title):
    return f"\n{RULE}\n%% {title.upper()}\n{RULE}\n\\section{{{title}}}\n"


def cventry(years, title, org, location="", extra="", body=""):
    years, title, org = clean(years), clean(title), clean(org)
    location, extra = clean(location), clean(extra)
    return (
        f"\\cventry{{{years}}}{{{title}}}{{{org}}}{{{location}}}{{{extra}}}\n"
        f"{{{body}}}\n"
    )


def clean(text):
    """Collapse YAML block-scalar whitespace and escape bare ampersands.

    YAML values may deliberately contain LaTeX (\\textbf{...}, ---, \\%), so we
    do not blanket-escape. But a bare & is an alignment character that breaks
    the build, and never appears legitimately in this content.
    """
    if text is None:
        return ""
    out = re.sub(r"\s+", " ", str(text)).strip()
    return re.sub(r"(?<!\\)&", r"\\&", out)


def bullet(item):
    """Render one experience bullet: \\item \\textit{Role (years):} text."""
    role, years, text = item.get("role"), item.get("years"), clean(item.get("text"))
    if role and years:
        head = f"\\textit{{{role} ({years}):}} "
    elif role:
        head = f"\\textit{{{role}:}} "
    else:
        head = ""
    line = f"\\item {head}{text}"
    if item.get("note"):
        # rendered as an unnumbered continuation line, indented under the item
        line += f"\n\\item[] \\hspace{{1em}}\\textit{{{clean(item['note'])}}}"
    return line


def render_experience(entries):
    out = [section("Professional Experience")]
    for i, e in enumerate(entries):
        body = []
        if e.get("summary"):
            body.append(f"\\textit{{{clean(e['summary'])}}}")
            body.append("\\vspace{0.15cm}")
        for g in e.get("groups", []) or []:
            body.append(f"\\textbf{{{clean(g['label'])}:}}")
            body.append("\\begin{itemize}")
            body.extend(bullet(it) for it in g["items"])
            body.append("\\end{itemize}")
            body.append("\\vspace{0.15cm}")
        if e.get("items"):
            body.append("\\begin{itemize}")
            body.extend(bullet(it) for it in e["items"])
            body.append("\\end{itemize}")
        if e.get("description"):
            body.append(clean(e["description"]))
        # \cventry's last argument is not \long: no blank lines inside it.
        text = "\n".join(b for b in body if b)
        out.append(
            cventry(e["years"], e["title"], e["org"], e.get("location", ""), "", text)
        )
        if i < len(entries) - 1:
            out.append("\\vspace{0.2cm}\n")
    return "".join(out)


def render_education(entries):
    out = [section("Education")]
    for e in entries:
        out.append(
            cventry(e["years"], e["degree"], e["org"], "", "", clean(e.get("detail", "")))
        )
        out.append("\n")
    return "".join(out)


def render_programs(entries):
    out = [section("Educational Leadership \\& Workforce Development")]
    for i, e in enumerate(entries):
        desc = clean(e.get("description", ""))
        if e.get("expansion"):
            desc = f"{clean(e['expansion'])}. {desc}"
        out.append(cventry(e["years"], e["title"], e["org"], "", "", desc))
        if i < len(entries) - 1:
            out.append("\n\\vspace{0.2cm}\n")
    return "".join(out)


def render_teaching(entries):
    out = [section("Teaching")]
    for e in entries:
        out.append(
            cventry(e["years"], e["title"], e["org"], "", "", clean(e.get("description", "")))
        )
        out.append("\n")
    return "".join(out)


def render_skills(entries):
    out = [section("Skills \\& Certifications")]
    for e in entries:
        out.append(f"\\cventry{{{clean(e['label'])}}}{{{clean(e['value'])}}}{{}}{{}}{{}}{{}}\n")
    return "".join(out)


def render_awards(groups):
    out = [section("Awards \\& Honors")]
    for g in groups:
        out.append(f"\n\\subsection{{{clean(g['group'])}}}\n")
        for a in g["items"]:
            out.append(
                f"\\cventry{{{clean(a['year'])}}}{{{clean(a['title'])}}}{{{clean(a.get('org',''))}}}"
                f"{{{clean(a.get('detail',''))}}}{{}}{{}}\n"
            )
    return "".join(out)


def render_service(entries):
    out = [section("Professional Service")]
    for i, e in enumerate(entries):
        out.append(
            f"\\cventry{{{clean(e['year'])}}}{{{clean(e['role'])}}}{{{clean(e['title'])}}}"
            f"{{{clean(e.get('org',''))}}}{{}}{{{clean(e.get('description',''))}}}\n"
        )
        if i < len(entries) - 1:
            out.append("\n\\vspace{0.1cm}\n")
    return "".join(out)


def preamble(ident):
    address = "\\\\\n  ".join(ident["address_lines"])
    return f"""\\documentclass[10pt,colorlinks=true,urlcolor=blue]{{moderncv}}
\\usepackage{{utopia}}
\\moderncvtheme[blue]{{classic}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[resetlabels]{{multibib}}

{RULE}
%% GENERATED FILE -- DO NOT EDIT DIRECTLY
%% Source of truth: _data/cv/*.yml
%% Regenerate:      python3 cv/yaml2tex.py
%% The \\nocite blocks below are the exception: they are hand-maintained,
%% because cite-key membership decides paper/talk/poster on the website too.
{RULE}

{RULE}
%% BIBLIOGRAPHY CONFIGURATION
{RULE}
\\newcites{{pre,peer,conf,poster,talks,other,prog,unp}}{{%
  Pre-prints,
  Peer Reviewed Articles,
  Conference Proceedings,
  Posters,
  Talks,
  Other Publications,
  Programs,
  Unpublished
}}
\\renewcommand{{\\bibliographyitemlabel}}{{\\@{{\\arabic{{enumiv}}}}}}

\\usepackage[scale=0.8]{{geometry}}

{RULE}
%% CUSTOM COMMANDS
{RULE}
\\newcommand{{\\cvdoublecolumn}}[2]{{%
  \\cvline{{}}{{}}{{%
    \\begin{{minipage}}[t]{{\\listdoubleitemmaincolumnwidth}}#1\\end{{minipage}}%
    \\hfill%
    \\begin{{minipage}}[t]{{\\listdoubleitemmaincolumnwidth}}#2\\end{{minipage}}%
    }}%
}}
\\renewcommand*{{\\namefont}}{{\\fontsize{{32}}{{40}}\\mdseries\\upshape}}

{RULE}
%% PERSONAL INFORMATION
{RULE}
\\AtBeginDocument{{\\recomputelengths}}
\\firstname{{{ident['first_name']}}}
\\familyname{{{ident['family_name']}}}
\\address{{{address}\\\\
  }}{{{ident['address_city']}}}
\\homepage{{{ident['homepage']}}}
\\email{{{ident['cv_email']}}}

\\begin{{document}}
\\maketitle
"""


def carry_over_bibliography_blocks():
    """Reuse the hand-maintained \\nocite blocks from the existing .tex."""
    if not TEX.exists():
        sys.exit("cv/will_cv.tex not found: cannot carry over the \\nocite blocks")
    old = TEX.read_text(encoding="utf-8")
    start = old.find("%% PUBLICATIONS")
    if start == -1:
        start = old.find("\\section{Publications}")
    end = old.find("%% PROFESSIONAL SERVICE")
    if end == -1:
        end = old.find("\\section{Professional Service}")
    if start == -1 or end == -1 or end <= start:
        sys.exit("could not locate the publications block in cv/will_cv.tex")
    block = old[start:end].rstrip()
    # strip the leading rule comment lines; we re-emit our own section header
    block = re.sub(r"^%%.*\n", "", block, count=6)
    return block.strip()


def main():
    ident = load("identity")
    parts = [
        preamble(ident),
        render_experience(load("experience")),
        render_education(load("education")),
        render_programs(load("programs")),
        render_teaching(load("teaching")),
        render_skills(load("skills")),
        render_awards(load("awards")),
        f"\n{RULE}\n%% PUBLICATIONS (hand-maintained \\nocite lists)\n{RULE}\n",
        carry_over_bibliography_blocks(),
        "\n",
        render_service(load("service")),
        "\n\\end{document}\n",
    ]
    TEX.write_text("".join(parts), encoding="utf-8")
    print(f"wrote {TEX}")
    for name in ("experience", "education", "programs", "teaching", "awards", "service"):
        data = load(name)
        n = sum(len(g["items"]) for g in data) if name == "awards" else len(data)
        print(f"  {name}: {n}")


if __name__ == "__main__":
    main()

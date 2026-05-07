"""Convert paper.md to a Qeios-friendly LaTeX manuscript.

Mirrors the style of karna-qeios-manuscript.tex: 11pt article, 1in margins,
title/author/abstract block, sections, subsections, manual bullet rendering.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "paper.md"
OUTPUT = ROOT / "agent-stack-qeios-manuscript.tex"

PAPER_TITLE = (
    "Six Reliability Primitives for LLM Agents: "
    "An Artifact Pattern for Stackable, Single-Concern Libraries"
)
PAPER_AUTHOR = "Mukunda Rao Katta"
DATE_LINE = "May 7, 2026"


LATEX_PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage[hidelinks]{hyperref}
\setlength{\parskip}{0.65em}
\setlength{\parindent}{0pt}
\title{%TITLE%}
\author{%AUTHOR%\\Independent Researcher}
\date{%DATE%}
\begin{document}
\maketitle
"""


def latex_escape(text: str) -> str:
    """Escape characters that LaTeX would otherwise interpret as commands.

    We render code refs separately; this handles only normal prose.
    """
    out = []
    for ch in text:
        if ch == "\\":
            out.append(r"\textbackslash{}")
        elif ch in {"&", "%", "$", "#", "_", "{", "}"}:
            out.append("\\" + ch)
        elif ch == "~":
            out.append(r"\textasciitilde{}")
        elif ch == "^":
            out.append(r"\textasciicircum{}")
        else:
            out.append(ch)
    return "".join(out)


def render_inline(text: str) -> str:
    """Convert markdown inline markers to LaTeX while escaping the rest."""
    # Pull out code spans first so we don't escape their contents.
    out_parts: list[str] = []
    cursor = 0
    for match in re.finditer(r"`([^`]+)`", text):
        out_parts.append(latex_inline_pass(text[cursor:match.start()]))
        out_parts.append(r"\texttt{" + latex_escape(match.group(1)) + "}")
        cursor = match.end()
    out_parts.append(latex_inline_pass(text[cursor:]))
    return "".join(out_parts)


def latex_inline_pass(text: str) -> str:
    text = latex_escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"\*([^*]+)\*", r"\\textit{\1}", text)
    return text


def main() -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    out: list[str] = []

    out.append(
        LATEX_PREAMBLE.replace("%TITLE%", PAPER_TITLE)
        .replace("%AUTHOR%", PAPER_AUTHOR)
        .replace("%DATE%", DATE_LINE)
    )

    # We pull the abstract out of the markdown's "## Abstract" section so that
    # it can sit inside \begin{abstract} ... \end{abstract} block.
    in_abstract = False
    in_intro = False
    abstract_lines: list[str] = []
    body_lines: list[str] = []

    for raw in lines:
        line = raw.rstrip()
        if not in_intro:
            if line.startswith("# "):
                continue  # title handled by \maketitle
            if line.strip() == PAPER_AUTHOR:
                continue  # author handled by \author
            if line.startswith("## Abstract"):
                in_abstract = True
                continue
            if line.startswith("## ") and in_abstract:
                in_abstract = False
                in_intro = True
                body_lines.append(line)
                continue
            if in_abstract:
                abstract_lines.append(line)
                continue
        else:
            body_lines.append(line)

    out.append(r"\begin{abstract}")
    abstract_text = "\n".join(abstract_lines).strip()
    out.append(render_inline(abstract_text))
    out.append(r"\end{abstract}")

    pending_bullets: list[str] = []

    def flush_bullets() -> None:
        if not pending_bullets:
            return
        for bullet in pending_bullets:
            out.append(r"\noindent $\bullet$ " + render_inline(bullet) + r"\\")
        out.append("")
        pending_bullets.clear()

    for raw in body_lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            flush_bullets()
            out.append("")
            continue
        if stripped.startswith("## "):
            flush_bullets()
            out.append(r"\section{" + render_inline(stripped[3:].lstrip("0123456789. ").strip()) + "}")
            out.append("")
            continue
        if stripped.startswith("### "):
            flush_bullets()
            out.append(r"\subsection{" + render_inline(stripped[4:].lstrip("0123456789. ").strip()) + "}")
            out.append("")
            continue
        if stripped.startswith("- "):
            pending_bullets.append(stripped[2:])
            continue
        m = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if m:
            pending_bullets.append(m.group(2))
            continue
        flush_bullets()
        out.append(render_inline(stripped))

    flush_bullets()
    out.append(r"\end{document}")

    OUTPUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(OUTPUT)


if __name__ == "__main__":
    main()

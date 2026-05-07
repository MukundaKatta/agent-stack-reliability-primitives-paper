# Agent-Stack Reliability Primitives Paper Package

This package contains a preprint draft for:

`Six Reliability Primitives for LLM Agents: An Artifact Pattern for Stackable, Single-Concern Libraries`

## Source Artifacts

- TypeScript libraries on npm (`@mukundakatta/`):
  - `agentfit`, `agentguard`, `agentsnap`, `agentvet`, `agentcast`, `agentbudget`
- Python ports on PyPI:
  - `agentfit-py`, `agentguard-firewall`, `agentsnap-py`, `agentvet-py`, `agentcast-py`, `agentbudget-py`
- MCP server variants on npm (`-mcp` suffix):
  - `agentfit-mcp`, `agentguard-mcp`, `agentsnap-mcp`, `agentvet-mcp`, `agentcast-mcp`, `agentbudget-mcp`
- Source: https://github.com/MukundaKatta (Agent* repositories)
- Landing page: https://mukundakatta.github.io/agent-stack/
- Inspected date: 2026-05-07

## Package Contents

- `paper.md` — manuscript source (Markdown)
- `agent-stack-reliability-primitives-preprint.pdf` — rendered preprint PDF (6 pages, US Letter)
- `agent-stack-qeios-manuscript.tex` — LaTeX manuscript for Qeios / arXiv-style submissions
- `abstract.txt` — submission abstract
- `keywords.txt` — keyword list
- `submission-metadata.json` — platform metadata (title, authors, license, repos, target platforms)
- `cover-note.txt` — moderation/editorial note
- `render_preprint_pdf.py` — local PDF renderer (reportlab)
- `render_qeios_tex.py` — Markdown → LaTeX converter

## Reproducing

```bash
python3 -m venv .venv
.venv/bin/pip install reportlab
.venv/bin/python render_preprint_pdf.py
.venv/bin/python render_qeios_tex.py
```

## Status

Prepared for submission to relevant research and artifact platforms (Zenodo, Qeios, Figshare, ScienceOpen, TechRxiv, OSF Preprints) and for a companion Medium post. Companion to the Karna chat-native-assistant paper in the same `research-footprints/` series.

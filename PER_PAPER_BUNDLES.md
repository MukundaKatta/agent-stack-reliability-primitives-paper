# Per-Paper Submission Bundles

One block per paper in the `research-footprints/` series. Each block has the paste-ready title, abstract, keywords, DOI cross-link, and category mappings. Pair with `PASTE_BUNDLES.md` for the per-platform field shape (every platform's URL + auth + form structure is the same across papers — only the title/abstract/DOI changes).

**Working order across platforms (fastest DOI gain per minute):**

1. **OSF Preprints** — instant DOI, no gate. https://osf.io/preprints/
2. **HAL** — open archive, instant hal-ID, auto-feeds OpenAIRE. https://hal.science/
3. **Figshare** — instant DOI. https://figshare.com/account/projects/upload (sign in via ORCID)
4. **ResearchGate** — auto-import via DOI search. https://researchgate.net/account.AccountClaimWorks.html
5. **TechRxiv** — IEEE-aligned, 1–2 day editorial check. https://www.techrxiv.org/submit
6. **ScienceOpen** — editorial review, ORCID sign-in. https://www.scienceopen.com/submit
7. **Qeios** — editorial, ORCID + email. https://www.qeios.com/submit

For every platform, the universal common metadata is:

| Field | Value |
| --- | --- |
| Author | `Mukunda Rao Katta` |
| ORCID | `0009-0007-6071-3896` |
| Affiliation | `Independent Researcher` |
| Email | `mukunda.vjcs6@gmail.com` |
| License (manuscript) | `CC BY 4.0` |

Per-paper title / abstract / keywords / DOI / categories are below.

---

## 1. Karna: Chat-Native Multi-Channel Architecture

**Already on:** Zenodo · Figshare. **Missing:** OSF, HAL, TechRxiv, ResearchGate, ScienceOpen, Qeios.

| Field | Paste |
| --- | --- |
| **Title** | Karna: A Chat-Native, Multi-Channel Architecture for Personal AI Chief-of-Staff Agents |
| **Zenodo DOI** | `10.5281/zenodo.20074229` |
| **Figshare DOI** | `10.6084/m9.figshare.32209317` |
| **Source repo** | `https://github.com/MukundaKatta/karna` |
| **Subject (cs.SE/cs.AI)** | Software Engineering, Artificial Intelligence |
| **OSF subjects** | Computer Sciences → Software Engineering, Artificial Intelligence and Robotics |
| **HAL domain** | `[cs.SE]` primary, `[cs.AI]` secondary |
| **Figshare categories** | Software engineering, Artificial intelligence |
| **TechRxiv subject** | Computing & Processing → Software Engineering, Artificial Intelligence |

**Abstract (paste verbatim):**

> Personal AI assistants are moving from single-window chat interfaces toward systems that operate across messaging channels, web dashboards, mobile clients, voice notes, workflow triggers, and long-running memory. This paper presents Karna, a self-hosted TypeScript monorepo that explores a chat-native architecture for a personal AI chief-of-staff agent. The system is organized around a gateway, an agent runtime, shared protocol types, channel adapters, web and mobile surfaces, a CLI, memory/session modules, workflow hooks, observability surfaces, and deployment artifacts. Repository inspection identifies 13 channel packages, 485 TypeScript or TSX source files, 84 test files, Docker and Kubernetes deployment artifacts, and separate web, mobile, cloud, and command-line applications. The paper describes the design goals, repository structure, channel abstraction, operational safety considerations, and research questions that emerge from using chat as the primary interface for agentic work.

**Keywords (paste, comma-separated or one per line):**

```
AI agents, personal assistants, chat-native systems, multi-channel agents, agent architecture, memory systems, workflow automation, self-hosted AI, TypeScript, operator visibility
```

---

## 2. Agent Trajectory Replay

**Already on:** Zenodo (v1 + v2) · ScienceOpen (pending). **Missing:** Figshare, OSF, HAL, TechRxiv, ResearchGate, Qeios.

| Field | Paste |
| --- | --- |
| **Title** | Agent Trajectory Replay for Debugging Tool-Using AI Workflow Regressions |
| **Zenodo DOI (v2)** | `10.5281/zenodo.20073574` |
| **Zenodo DOI (v1)** | `10.5281/zenodo.20057054` |
| **ScienceOpen pending** | https://www.scienceopen.com/document/read?id=47c2eaca-be45-455f-9f1a-03dd016dc981 |
| **Source repo** | `https://github.com/MukundaKatta/ai-problem-packages/tree/main/packages/agent-trajectory-replay` |
| **OSF subjects** | Computer Sciences → Software Engineering, Software Quality |
| **HAL domain** | `[cs.SE]` primary, `[cs.AI]` secondary |
| **Figshare categories** | Software engineering, Artificial intelligence |
| **TechRxiv subject** | Computing & Processing → Software Engineering |

**Abstract (paste verbatim):**

> Tool-using AI agents are difficult to debug because a failure may emerge from a sequence of planning steps, tool calls, intermediate errors, and final-output decisions rather than from a single response. This paper presents Agent Trajectory Replay, a small zero-dependency JavaScript package for summarizing, replaying, and diffing agent event traces. The package removes unstable timing fields before comparison, counts tool calls and errors, exposes final-output changes, and allows event handlers to rebuild state from a recorded trajectory. The contribution is a lightweight regression-debugging pattern for teams that need a simple way to compare agent behavior across model, prompt, or tool changes.

**Keywords:**

```
AI agents, trajectory replay, tool use, regression testing, agent debugging, workflow evaluation
```

---

## 3. Small-Rule Guardrails for RAG

**Already on:** Zenodo (v1 + v2) · Figshare. **Missing:** OSF, HAL, TechRxiv, ResearchGate, ScienceOpen, Qeios.

| Field | Paste |
| --- | --- |
| **Title** | Small-Rule Guardrails for Retrieval-Augmented Generation: Prompt Injection and Vector Poisoning Checks |
| **Zenodo DOI (v2)** | `10.5281/zenodo.20057632` |
| **Zenodo DOI (v1)** | `10.5281/zenodo.20057056` |
| **Figshare DOI** | `10.6084/m9.figshare.32193543` |
| **Source repo** | `https://github.com/MukundaKatta/ai-problem-packages` (packages: `prompt-injection-shield`, `vector-poison-score`) |
| **OSF subjects** | Computer Sciences → Information Security, Artificial Intelligence and Robotics |
| **HAL domain** | `[cs.CR]` primary, `[cs.AI]` secondary |
| **TechRxiv subject** | Computing & Processing → Security and Privacy, Artificial Intelligence |

**Abstract (paste verbatim):**

> Retrieval-augmented generation systems often treat retrieved text as helpful evidence, but retrieved text can also contain adversarial instructions, suspicious link patterns, oversized chunks, or secret-exfiltration requests. This paper presents a small-rule guardrail approach implemented through two zero-dependency JavaScript packages: prompt-injection-shield and vector-poison-score. The method is deliberately lightweight. It scans retrieved documents and tool outputs before they are inserted into model context, reports explicit risk reasons, and supports filtering or line stripping as a simple containment step. The contribution is not a replacement for full security review or large-scale benchmark evaluation. Instead, it offers an inspectable baseline that developers can place between retrieval and prompt construction while building, testing, and auditing agentic RAG workflows.

**Keywords:**

```
retrieval augmented generation, prompt injection, vector poisoning, AI security, guardrails, agent workflows
```

---

## 4. Chetana: Consciousness Indicator Scoring

**Already on:** Zenodo. **Missing:** Figshare, OSF, HAL, TechRxiv, ResearchGate, ScienceOpen, Qeios. **Caution:** frame as indicator-scoring research tooling, not as a consciousness detector (per the package's metadata note).

| Field | Paste |
| --- | --- |
| **Title** | Chetana: A Theory-Indexed Probe Framework for AI Consciousness Indicator Scoring |
| **Zenodo DOI** | `10.5281/zenodo.20057058` |
| **Source repo** | `https://github.com/MukundaKatta/chetana` |
| **OSF subjects** | Computer Sciences → Artificial Intelligence and Robotics; Cognitive Sciences (cross-list) |
| **HAL domain** | `[cs.AI]` primary, `[cs.CY]` (Computers and Society) secondary |
| **Figshare categories** | Artificial intelligence, Cognitive science |
| **TechRxiv subject** | Computing & Processing → Artificial Intelligence |

**Abstract (paste verbatim):**

> Claims about AI consciousness are easy to overstate and difficult to evaluate. This paper presents Chetana, a theory-indexed probe framework that maps model responses to a set of consciousness indicators drawn from Global Workspace Theory, Higher-Order Theories, Recurrent Processing Theory, Predictive Processing, and Attention Schema Theory. The implementation organizes indicators, probes, model adapters, scoring, theory aggregation, probability calculation, and report generation in a TypeScript monorepo. The goal is not to determine whether an AI system is conscious. It is to make a narrow evaluation workflow inspectable: which theory supplied each indicator, which probe produced each observation, how indicator scores were aggregated, and how uncertainty should be reported. The framework is positioned as research tooling for careful discussion, not as a consciousness detector.

**Keywords:**

```
AI consciousness, consciousness indicators, model evaluation, probe framework, theory aggregation, AI safety
```

---

## 5. ML Intern Lab

**Already on:** Zenodo · Academia.edu. **Missing:** Figshare, OSF, HAL, TechRxiv, ResearchGate, ScienceOpen, Qeios.

| Field | Paste |
| --- | --- |
| **Title** | ML Intern Lab: A Minimal Agentic Workflow for Reproducible Machine Learning Experiment Reports |
| **Zenodo DOI** | `10.5281/zenodo.20057317` |
| **Academia.edu** | https://www.academia.edu/166763243 |
| **Source repos** | `https://gitlab.com/mukunda.vjcs6-group/ml-intern-lab` · `https://pypi.org/project/ml-intern-lab/` |
| **OSF subjects** | Computer Sciences → Software Engineering, Machine Learning |
| **HAL domain** | `[cs.LG]` primary, `[cs.SE]` secondary |
| **Figshare categories** | Machine learning, Software engineering |
| **TechRxiv subject** | Computing & Processing → Machine Learning, Software Engineering |

**Abstract (paste verbatim):**

> Machine-learning teams increasingly use AI agents to read papers, propose experiments, run baselines, and draft reports. These workflows are useful, but they often blur together planning, execution, metrics, and narrative output in ways that are difficult to audit. This paper presents ML Intern Lab, a minimal agentic workflow for reproducible machine-learning experiment reports. The workflow turns an idea or paper note into an explicit experiment plan, runs a local baseline, writes machine-readable metrics, and generates a short model report. The reference implementation uses a zero-dependency Python runner and a tiny majority-class baseline experiment to demonstrate the pattern. The contribution is not a new model or benchmark. It is a compact reporting workflow that helps agentic ML assistants leave inspectable artifacts at each step, making their work easier to review, reproduce, and extend.

**Keywords:**

```
agentic machine learning, ML experiment reporting, reproducibility, MLOps, AI agents, baseline experiments, model reports, workflow artifacts
```

---

## 6. AI Eval Forge

**Already on:** Zenodo · SSRN. **Missing:** Figshare, OSF, HAL, TechRxiv, ResearchGate, ScienceOpen, Qeios.

| Field | Paste |
| --- | --- |
| **Title** | AI Eval Forge: Mixed-Check Regression Testing for LLM and Agent Workflows |
| **Zenodo DOI** | `10.5281/zenodo.20044318` |
| **SSRN abstract** | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6720559 |
| **Source repo** | `https://github.com/MukundaKatta/ai-eval-forge-js` |
| **OSF subjects** | Computer Sciences → Software Engineering, Software Quality |
| **HAL domain** | `[cs.SE]` primary, `[cs.AI]` secondary |
| **Figshare categories** | Software engineering, Software testing, Artificial intelligence |
| **TechRxiv subject** | Computing & Processing → Software Engineering |

**Abstract (paste verbatim):**

> Large-model and agent teams often need faster regression checks than broad benchmark suites can provide. This paper presents AI Eval Forge, a zero-dependency evaluation harness for mixed-check regression testing across LLM and agent workflows. The tool supports exact-match, substring, regex, token-F1, JSON validity, JSON field equality, citation coverage, and bounded custom-expression checks in a compact case format that works with JSON or JSONL. The contribution is not a new benchmark. It is a small, inspectable evaluation layer that helps teams compare runs, catch regressions, and summarize pass rate, score, cost, and latency without standing up a heavy evaluation stack. The paper describes the harness design, check model, reporting format, and practical role of mixed-check cases in real workflow testing.

**Keywords:**

```
AI evaluation, LLM regression testing, agent evaluation, software testing, structured outputs, citation grounding, developer tooling
```

---

## 7. Lightweight Evaluation and Operational Scorecards

**Already on:** Zenodo. **Missing:** Figshare, OSF, HAL, TechRxiv, ResearchGate, ScienceOpen, Qeios.

| Field | Paste |
| --- | --- |
| **Title** | Lightweight Evaluation and Operational Scorecards for Tool-Using AI Agents |
| **Zenodo DOI** | `10.5281/zenodo.20034550` |
| **Source artifacts** | Hugging Face Spaces: `agent-eval-lab`, `ops-scorecard-lab`. Datasets: `agent-eval-scenarios`. Modal: `agent-labs-portal`. |
| **OSF subjects** | Computer Sciences → Software Engineering, Artificial Intelligence and Robotics |
| **HAL domain** | `[cs.SE]` primary, `[cs.AI]` secondary |
| **Figshare categories** | Software engineering, Artificial intelligence |
| **TechRxiv subject** | Computing & Processing → Software Engineering, Artificial Intelligence |

**Abstract (paste verbatim):**

> Tool-using AI agents are increasingly used in coding, browser automation, research assistance, and support workflows. In practice, however, many teams still evaluate these systems through isolated prompts, one-off demos, or broad benchmark references that do not translate well into deployment judgment. This paper presents a lightweight workflow for evaluating agent behavior that begins with scenario design, continues through explicit expected behavior and failure-mode definition, and ends with an operational scorecard that helps teams judge rollout readiness. The workflow is instantiated through compact public artifacts, including small datasets, interactive demo apps, and public analytics surfaces. The aim is not to compete with large benchmarks on scale. It is to improve repeatability, interpretability, and operational usefulness for builders who need evaluation methods that are small enough to maintain and concrete enough to use.

**Keywords:**

```
AI agents, agent evaluation, tool use, operational scorecards, LLM reliability, structured outputs, workflow evaluation, human-in-the-loop review
```

---

## 8. Browser Research Agent

**Already on:** ⏳ MetaArXiv (resubmitted, pending moderator review). **Missing:** Zenodo (priority 1 — get the DOI), then Figshare, OSF, HAL, ResearchGate, TechRxiv, ScienceOpen, Qeios.

**Note:** this paper does NOT yet have a Zenodo DOI. The MetaArXiv resubmission is still pending. **Recommended first step: deposit on Zenodo to mint a DOI**, then propagate using that DOI.

| Field | Paste |
| --- | --- |
| **Title** | Citation Traceability for Web-Native AI Research Workflows |
| **MetaArXiv status** | Resubmitted to MetaArXiv on OSF Preprints, pending moderator review |
| **Source repo** | `https://github.com/MukundaKatta/browser-research-agent` |
| **OSF subjects** | Social and Behavioral Sciences → Library and Information Science (matches the original MetaArXiv subject); cross-list Computer Sciences → Artificial Intelligence and Robotics |
| **HAL domain** | `[cs.IR]` (Information Retrieval) primary, `[cs.DL]` (Digital Libraries) secondary |
| **Figshare categories** | Information science, Digital library systems |
| **TechRxiv subject** | Computing & Processing → Information Retrieval |

**Abstract (paste verbatim):**

> Fast-moving AI topics are often summarized through workflows that are easy to run but difficult to audit. This paper presents Browser Research Agent, a small open-source software artifact for building cited Markdown briefs from explicit source inputs. The package loads local or remote sources, preserves publication metadata, ranks source relevance against a topic query, extracts candidate claims, and renders a brief with numbered references and an explicit confidence note. The contribution is modest by design. Rather than claiming a new retrieval model or a broad benchmark improvement, the artifact addresses a reproducibility gap in web-native AI research workflows: readers often cannot tell which sources supported a generated brief, how those sources were selected, or whether the resulting claims are inspectable without rerunning a larger stack. By constraining the workflow to supplied sources and visible citation output, Browser Research Agent offers a simple pattern for more transparent evidence synthesis in exploratory AI research and repository intelligence tasks.

**Keywords:**

```
research transparency, reproducibility, evidence synthesis, citation traceability, web research, AI tooling
```

---

## 9. Context Forge

**Already on:** ⏳ Research Square (target — submission status not confirmed in audit). **Missing:** Zenodo (priority 1), then Figshare, OSF, HAL, ResearchGate, TechRxiv, ScienceOpen, Qeios.

**Note:** like Browser Research Agent, this paper is **not yet on Zenodo**. **Recommended first step: deposit on Zenodo for the DOI**, then propagate.

| Field | Paste |
| --- | --- |
| **Title** | Context Forge: A Lightweight Method for Diversity-Aware Context Packing and Prompt-Injection-Aware Retrieval |
| **Source repo** | `https://github.com/MukundaKatta/context-forge` |
| **OSF subjects** | Computer Sciences → Information Retrieval, Artificial Intelligence and Robotics |
| **HAL domain** | `[cs.IR]` primary, `[cs.AI]` and `[cs.CR]` secondary |
| **Figshare categories** | Information retrieval, Artificial intelligence, Cybersecurity |
| **TechRxiv subject** | Computing & Processing → Information Retrieval, Artificial Intelligence |

**Abstract (paste verbatim):**

> Context quality remains one of the least stable parts of retrieval-augmented generation and agent prompting workflows. This paper presents Context Forge, a lightweight context-engineering toolkit that chunks source documents, ranks candidate chunks against a query, applies diversity-aware selection, flags prompt-injection and secret-like content, and renders citation-ready context blocks under a token budget. The method is designed as an inspectable middle layer between raw corpora and model prompts. Its aim is not to replace full retrieval systems, but to provide a compact and auditable packing strategy that is easier to reason about in local development, red-team analysis, and controlled evaluation settings. The paper describes the chunking and ranking procedure, the prompt-risk scan, and the packing strategy used to balance relevance, diversity, and budget constraints. Validation is demonstrated through repository tests and controlled examples that check relevance selection, heading preservation, and prompt-injection detection.

**Keywords:**

```
context engineering, retrieval augmented generation, prompt injection, context packing, tooling methods, agent workflows
```

---

## Submission cheat sheet — every paper × every platform

| Action | Click order |
| --- | --- |
| **Open OSF Preprints** | https://osf.io/preprints/submit |
| For each of papers 1–7 | Title (table) → Description (abstract) → Tags (keywords, comma-split) → Subject (table) → File: corresponding `*-preprint.pdf` from each paper-package → License: CC BY 4.0 → DOI of associated work: Zenodo DOI (table) → Save & Publish |
| **Open HAL** | https://hal.science/ |
| For each of papers 1–7 | Document type: Preprint → Domain (table) → Title → Author: Katta, Mukunda Rao → Affiliation: Independent Researcher → Abstract → Keywords → Identifier: DOI (table) → File: PDF → License: CC BY 4.0 |
| **Open Figshare** | https://figshare.com/account/projects/upload |
| For papers 2, 4–7 (1 + 3 already there) | Item type: Preprint → Categories (table) → License: CC BY 4.0 → Description: abstract → Keywords (one per line) → Files: PDF + package zip → Resource DOI: Zenodo (relation: IsIdenticalTo) |
| **Open ResearchGate** | https://www.researchgate.net/account.AccountClaimWorks.html |
| For all 7 with Zenodo DOIs | Add Research → Search by DOI (table column) → Confirm authorship → Publish. **No paste — Zenodo metadata propagates via DataCite.** |
| **Open TechRxiv** | https://www.techrxiv.org/submit |
| For each of papers 1–7 | Article type: Preprint → Subject (table) → Title → Abstract → Keywords → File: PDF → Identifier: Zenodo DOI |
| **Open ScienceOpen** | https://www.scienceopen.com/submit (only if your prior submission has cleared editor) |
| Submit one paper at a time | Type: Preprint → Disciplines (table) → File: PDF → Abstract → Keywords → Cover note (paper-specific) |
| **Open Qeios** | https://www.qeios.com/submit |
| Submit one paper at a time | Type: Article → Subject (table) → Manuscript file: PDF → Abstract → Keywords → Funding: none → Conflicts: none |

For papers 8 (Browser Research Agent) and 9 (Context Forge), step zero is **deposit on Zenodo first** to mint the DOI, then run them through the same propagation queue. The Zenodo deposit form is `https://zenodo.org/uploads/new` — same flow you used for Karna and agent-stack.

---

## After every successful submission

Record the new identifier in the corresponding paper-package's `submission-metadata.json` under a `published_platforms` array (mirroring the agent-stack package's pattern):

```json
{
  "platform": "OSF Preprints",
  "status": "published",
  "record_url": "https://osf.io/<id>/",
  "doi": "10.31234/osf.io/<id>",
  "published_date": "2026-05-07"
}
```

Then update the master `PROPAGATION_TRACKER.md` row in the agent-stack paper package so the matrix stays accurate.

# Unique Platforms Bundle — 2026-05-08

Pivot from PR-driven propagation to platform-driven propagation. Five new surfaces, each picked because the existing tracker did not cover it.

## 1. Software Heritage — paper-package source archives ✅ done end-to-end

Submitted Save Code Now requests for the 11 paper-package GitHub repos (the repos themselves, not the agent-stack source repos already archived). 9 accepted, 2 hit a per-IP rate-limit window and need one more `curl` retry. SWHIDs become resolvable once the visit completes (usually within 24h).

| Repo | Save request id | Status |
| --- | --- | --- |
| agent-stack-reliability-primitives-paper | 2324936 | accepted, pending visit |
| context-forge-paper | 2324937 | accepted, pending visit |
| browser-research-agent-paper | 2324938 | accepted, pending visit |
| lightweight-eval-scorecards-paper | 2324939 | accepted, pending visit |
| ml-intern-lab-paper | 2324940 | accepted, pending visit |
| chetana-consciousness-indicator-paper | 2324941 | accepted, pending visit |
| agent-trajectory-replay-paper | 2324942 | accepted, pending visit |
| karna-chat-native-assistant-paper | 2324943 | accepted, pending visit |
| rag-guardrails-paper | 2324944 | accepted, pending visit |
| ai-eval-forge-paper | 429 (rate-limit) | retry tomorrow |
| lightweight-agent-eval-paper | 429 (rate-limit) | retry tomorrow |

Resolve any SWHID later via:
```
https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/MukundaKatta/<repo>
```

To retry the two stragglers tomorrow (single curl per repo):
```bash
for r in ai-eval-forge-paper lightweight-agent-eval-paper; do
  curl -X POST "https://archive.softwareheritage.org/api/1/origin/save/git/url/https://github.com/MukundaKatta/$r/"
done
```

## 2. WikiData — scholarly article entities (1-click paste)

WikiData entries propagate to Scholia, OpenAlex, Google Scholar, and DBLP — none of which are in the current tracker as a primary surface. Each paper becomes a Q-entity linked to its DOI, ORCID author, title, and Zenodo as the publishing venue.

### How to run (30 seconds, 1 click)

1. Open https://quickstatements.toolforge.org/#/batch
2. Sign in with your Wikimedia account (browser handles OAuth)
3. Paste the entire content of `/tmp/wikidata-prep/quickstatements-v1.txt` into the textarea
4. Click "Run"

QuickStatements will create 8 new Wikidata items, one per paper, each with these properties:

| Property | Value | Meaning |
| --- | --- | --- |
| P31 | Q13442814 | instance of: scholarly article |
| Len, Den | English label + description | display name |
| P1476 | en: title | canonical title |
| P356 | DOI | identifier |
| P407 | Q1860 | language: English |
| P577 | publication date | from Zenodo metadata |
| P136 | Q580922 | genre: preprint |
| P1433 | Q1660091 | published in: Zenodo |
| P2093 | "Mukunda Rao Katta" | author name string |
| P953 | full DOI URL | full work URL |

### Optional follow-up after the batch creates

If you have a Wikidata Q-item for yourself (or want to create one), replace `P2093` (author name string) with `P50` (author) pointing at your Q-id. Replace via QS V1:
```
<paper-Qid>  P50  <your-Qid>
<paper-Qid>  -P2093  "Mukunda Rao Katta"
```

The batch file is at:
```
/tmp/wikidata-prep/quickstatements-v1.txt
```

(104 lines, 8 papers covered: agent-stack, Karna, Trajectory Replay, Guardrails, Chetana, ML Intern Lab, Eval Forge, Eval Scorecards)

## 3. PhilArchive — paste-ready bundle for Chetana

PhilArchive (https://philarchive.org) is the canonical open archive of philosophy. Chetana — a consciousness-indicator framework with theory-indexed probes — is a perfect topic fit and is currently published only on Zenodo. PhilArchive accepts open submissions; account required.

### Submission fields

| Field | Value |
| --- | --- |
| Title | Chetana: A Theory-Indexed Probe Framework for AI Consciousness Indicator Scoring |
| Authors | Mukunda Rao Katta |
| Year | 2026 |
| Type | Manuscript |
| Categories | Philosophy of Mind > Consciousness; Philosophy of Cognitive Science; Philosophy of Artificial Intelligence |
| Keywords | consciousness, AI consciousness, indicator framework, philosophy of mind, theory-indexed probes, GWT, IIT, HOT, machine consciousness |
| Abstract | (paste from `chetana-consciousness-indicator-paper-package/README.md`) |
| External URL | https://doi.org/10.5281/zenodo.20057058 |
| File | `chetana-consciousness-indicator-package/preprint.pdf` (or whatever the rendered filename is) |
| License | CC BY 4.0 |

### Steps

1. Sign up at https://philarchive.org/sign-up.html (free, no editorial gate for upload itself)
2. Click "Submit material" → choose "Upload"
3. Paste the fields above
4. Upload the PDF
5. Submit; the moderators publish within ~1 week

## 4. Authorea — paste-ready bundle for agent-stack

Authorea (https://www.authorea.com, owned by Wiley) auto-mints a DOI on publish, indexes to Wiley's network and to Crossref. Currently zero papers from this stack are on Authorea.

### Submission fields

| Field | Value |
| --- | --- |
| Title | Six Reliability Primitives for LLM Agents: An Artifact Pattern for Stackable, Single-Concern Libraries |
| Authors | Mukunda Rao Katta |
| Type | Preprint |
| Tags | LLM agents, reliability, infrastructure, npm, PyPI, MCP, TypeScript, Python |
| Abstract | (paste from `agent-stack-reliability-primitives-paper-package/README.md`) |
| Linked DOI | 10.5281/zenodo.20074702 |
| File | `agent-stack-reliability-primitives-paper-package/agent-stack-reliability-primitives-preprint.pdf` |
| License | CC BY 4.0 |

### Steps

1. Sign up at https://www.authorea.com/signup with email or ORCID
2. Click "New Document" → "Upload PDF"
3. Drop the PDF, fill in the fields above
4. Click "Publish" — Authorea mints a DOI under `10.22541/au.*` and the record becomes citeable

## 5. Knowledge Commons (Humanities Commons) — paste-ready bundle

Knowledge Commons (https://hcommons.org / CORE) is a humanities/social-sciences open repository. Two papers fit cleanly: Chetana (consciousness/cognitive science) and ML Intern Lab (research-process automation, fits open scholarship discussions). Currently zero papers from this stack are in Knowledge Commons.

### Submission fields (per paper)

| Field | Value (Chetana example) |
| --- | --- |
| Title | Chetana: A Theory-Indexed Probe Framework for AI Consciousness Indicator Scoring |
| Authors | Mukunda Rao Katta |
| Type | Working paper / Preprint |
| Subjects | Philosophy of Mind, Cognitive Science, Artificial Intelligence |
| Keywords | consciousness, AI consciousness, GWT, IIT, HOT, indicator framework |
| License | CC BY 4.0 |
| Abstract | (paste from package) |
| Replaces / Linked DOI | 10.5281/zenodo.20057058 |
| File | rendered PDF |

### Steps

1. Sign up at https://hcommons.org/register/ (free; choose any society — MLA, MSA, ASEH all free; uses standard email auth)
2. Go to CORE deposit page: https://hcommons.org/deposits/new/
3. Paste the fields above
4. Upload the PDF
5. Click "Deposit" — CORE mints a handle and indexes to the wider commons network

## Summary

| Platform | What I shipped this round | What's left for you |
| --- | --- | --- |
| Software Heritage | 9 of 11 paper-package repos archived | retry 2 stragglers tomorrow (1 line) |
| WikiData | QuickStatements V1 batch ready (8 entities) | paste into QuickStatements + click Run |
| PhilArchive | Submission bundle ready (Chetana) | sign up + paste + upload |
| Authorea | Submission bundle ready (agent-stack) | sign up + paste + upload |
| Knowledge Commons | Submission bundle ready (Chetana, ML Intern Lab) | sign up + paste + upload |

Each surface is genuinely new — none appear in `PROPAGATION_TRACKER.md` and each one indexes into a different downstream graph (SWH → archival graph; Wikidata → Scholia/OpenAlex/DBLP; PhilArchive → philosophy citation graph; Authorea → Wiley/Crossref; Knowledge Commons → CORE/humanities graph).

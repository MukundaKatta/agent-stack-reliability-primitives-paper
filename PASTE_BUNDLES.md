# Paste-Ready Submission Bundles

One block per platform. Each block has every field value so you can fill the form in a single pass.

Zenodo is **already published**: [10.5281/zenodo.20074702](https://doi.org/10.5281/zenodo.20074702) (record 20074702, concept DOI 10.5281/zenodo.20074701, registered with DataCite 2026-05-07T19:30Z, status `findable`).

The remaining platforms below all need browser-based ORCID / Google sign-in that I can't automate. Open each URL, sign in, paste the values verbatim.

---

## 1. Figshare — fastest next win, you've already used it

**Form:** https://figshare.com/account/projects/upload  · **Auth:** ORCID

| Field | Paste |
| --- | --- |
| Title | `Six Reliability Primitives for LLM Agents: An Artifact Pattern for Stackable, Single-Concern Libraries` |
| Authors | `Mukunda Rao Katta` (your registered Figshare author) |
| Item type | `Preprint` |
| Categories | `4604 — Cybersecurity and privacy`, `4605 — Data management and data science`, `4611 — Machine learning` (search for "Software engineering" and "Artificial intelligence" too) |
| License | `CC BY 4.0` |
| Keywords (one per line) | `LLM agents`, `reliability primitives`, `agent infrastructure`, `context-window fitting`, `egress allowlist`, `snapshot testing`, `schema validation`, `structured output`, `budget caps`, `zero-dependency libraries`, `Model Context Protocol`, `TypeScript`, `Python`, `artifact pattern` |
| Description | Paste the contents of `abstract.txt` |
| Files | `agent-stack-reliability-primitives-preprint.pdf` and `agent-stack-reliability-primitives-preprint-package.zip` |
| Resource DOI (if asked) | `10.5281/zenodo.20074702` (relation: `IsIdenticalTo`) |
| References (resource title in text) | "Companion: Karna chat-native assistant paper, Figshare 10.6084/m9.figshare.32209317" |

After publish, paste the new DOI into `submission-metadata.json` under `published_platforms`.

---

## 2. Qeios

**Form:** https://www.qeios.com/submit  · **Auth:** ORCID + email verification

| Field | Paste |
| --- | --- |
| Title | `Six Reliability Primitives for LLM Agents: An Artifact Pattern for Stackable, Single-Concern Libraries` |
| Article type | `Article` |
| Subject | `Computer Science → Software Engineering`, also `Computer Science → Artificial Intelligence` |
| Manuscript file | `agent-stack-qeios-latex-source.zip` (preferred) or `agent-stack-reliability-primitives-preprint.pdf` |
| Abstract | Paste from `abstract.txt` |
| Keywords | Paste from `keywords.txt`, comma-separated |
| Funding | (leave empty) |
| Conflicts | (leave empty) |
| Cover letter (if asked) | Paste from `cover-note.txt` |
| Related work — DOI | `10.5281/zenodo.20074702` (Zenodo deposit of the same manuscript) |

Note: per your 2026-05-06 audit, Qeios profile visibility lags ~24 hours after submission. Don't update READMEs until the article appears on profile/107118.

---

## 3. ScienceOpen

**Form:** https://www.scienceopen.com/submit  · **Auth:** ORCID

| Field | Paste |
| --- | --- |
| Title | `Six Reliability Primitives for LLM Agents: An Artifact Pattern for Stackable, Single-Concern Libraries` |
| Submission type | `Preprint` |
| Disciplines | `Computer Science`, `Software Engineering`, `Artificial Intelligence` |
| File | `agent-stack-reliability-primitives-preprint.pdf` |
| Abstract | Paste from `abstract.txt` |
| Keywords | Paste from `keywords.txt`, comma-separated |
| License | `CC BY 4.0` |
| Cover note for editor | Paste from `cover-note.txt` (mention that the Zenodo DOI is `10.5281/zenodo.20074702`) |

After submit: pending editor decision via email. Per your karna and agent-trajectory-replay submissions the typical wait is a few days.

---

## 4. TechRxiv (IEEE preprint server)

**Form:** https://www.techrxiv.org/submit  · **Auth:** ORCID

| Field | Paste |
| --- | --- |
| Title | `Six Reliability Primitives for LLM Agents: An Artifact Pattern for Stackable, Single-Concern Libraries` |
| Article type | `Preprint` |
| Subject area | `Computing & Processing → Software Engineering`, secondary `Artificial Intelligence` |
| File | `agent-stack-reliability-primitives-preprint.pdf` |
| Abstract | Paste from `abstract.txt` |
| Keywords | Paste from `keywords.txt`, comma-separated |
| Funding | none |
| Conflicts | none |
| Acknowledgements | (leave empty unless you want to add one) |
| Other identifier | Zenodo DOI `10.5281/zenodo.20074702` |

After submit: TechRxiv assigns a DOI on acceptance after a short editorial check (usually 1–2 business days).

---

## 5. OSF Preprints (no endorsement gate)

**Form:** https://osf.io/preprints/  · **Auth:** Google or ORCID  · **Provider:** OSF Preprints

| Field | Paste |
| --- | --- |
| Title | `Six Reliability Primitives for LLM Agents: An Artifact Pattern for Stackable, Single-Concern Libraries` |
| Description | Paste from `abstract.txt` |
| Subjects | `Computer Sciences`, then `Software Engineering`, then `Artificial Intelligence and Robotics` |
| Tags (comma-separated, one box) | LLM agents, reliability primitives, agent infrastructure, Model Context Protocol, TypeScript, Python, artifact pattern, zero-dependency libraries |
| File | `agent-stack-reliability-primitives-preprint.pdf` |
| License | `CC-By Attribution 4.0 International` |
| Public visibility | yes |
| Original publication date | `2026-05-07` |
| DOI of associated work (if asked) | `10.5281/zenodo.20074702` |

OSF mints a DOI automatically. Paste it back into `submission-metadata.json`.

---

## 6. ResearchGate

ResearchGate auto-imports from your DataCite-registered Zenodo DOI when you sign in and confirm authorship.

**Form:** https://www.researchgate.net/account.AccountClaimWorks.html  · **Auth:** Google or institutional

| Step | Action |
| --- | --- |
| 1 | Sign in to ResearchGate |
| 2 | Profile → Add new → Research → Search by DOI: `10.5281/zenodo.20074702` |
| 3 | Confirm authorship → Publish |

No paste needed — title, authors, abstract, license all carry over from Zenodo via DataCite.

---

## 7. HAL (open archive, no endorsement gate)

**Form:** https://hal.science/  · **Auth:** Create HAL account or login via ORCID

| Field | Paste |
| --- | --- |
| Document type | `Preprint, Working Paper` |
| Domain | `Computer Science → Software Engineering [cs.SE]` (primary), `Artificial Intelligence [cs.AI]` (secondary) |
| Title | `Six Reliability Primitives for LLM Agents: An Artifact Pattern for Stackable, Single-Concern Libraries` |
| Author | `Katta, Mukunda Rao` (Independent Researcher) |
| Affiliation | `Independent Researcher` |
| Abstract | Paste from `abstract.txt` |
| Keywords | Paste from `keywords.txt` |
| Identifier (DOI) | `10.5281/zenodo.20074702` |
| File | `agent-stack-reliability-primitives-preprint.pdf` |
| License | `CC BY 4.0` |

HAL assigns a `hal-XXXXXX` identifier and mirrors to OpenAIRE / Semantic Scholar discovery.

---

## 8. arXiv (cs.SE)

Endorsement-gated. **Submit only after** you secure an endorser per `next-venues.md`.

**Form:** https://arxiv.org/submit  · **Auth:** arXiv account

| Field | Paste |
| --- | --- |
| Primary subject | `cs.SE — Software Engineering` |
| Cross-list | `cs.AI — Artificial Intelligence` |
| Upload | `agent-stack-qeios-manuscript.tex` (arXiv prefers source over PDF for cs.* categories) |
| Title | `Six Reliability Primitives for LLM Agents: An Artifact Pattern for Stackable, Single-Concern Libraries` |
| Authors | `Mukunda Rao Katta` |
| Abstract | Paste from `abstract.txt` |
| Comments field | `Companion to the karna-chat-native-assistant paper in the research-footprints/ series. Zenodo DOI: 10.5281/zenodo.20074702. CC-BY-4.0.` |
| License | `CC BY 4.0` |
| ACM classification (optional) | `D.2.4 Software/Program Verification`, `I.2.7 Natural Language Processing` |
| MSC classification (optional) | (leave empty) |

---

## 9. ORCID — link the work

After Zenodo publish, ORCID does NOT auto-pull. You add the work yourself.

**Form:** https://orcid.org/my-orcid (signed in) → **Works → Add → Search & link → Crossref/DataCite**

Search by DOI: `10.5281/zenodo.20074702`. Confirm and save. Repeat the same flow for the **other 8 Zenodo records** that aren't on your ORCID yet (per the 2026-05-07 audit gap).

For batch linking, the pattern is the same — one DOI search per record:

- `10.5281/zenodo.20034550` — Lightweight Evaluation
- `10.5281/zenodo.20044318` — AI Eval Forge
- `10.5281/zenodo.20057054` — Agent Trajectory Replay (v1)
- `10.5281/zenodo.20057056` — Small-Rule Guardrails (v1)
- `10.5281/zenodo.20057058` — Chetana
- `10.5281/zenodo.20057317` — ML Intern Lab
- `10.5281/zenodo.20057632` — Small-Rule Guardrails (v2)
- `10.5281/zenodo.20073574` — Agent Trajectory Replay (v2)
- `10.5281/zenodo.20074229` — Karna chat-native assistant

---

## 10. Medium

**Form:** https://medium.com/new-story  · **Auth:** Your existing Medium account

| Step | Action |
| --- | --- |
| 1 | Open `medium-post.md` from this package |
| 2 | Paste content |
| 3 | Tags: `AI`, `Open Source`, `Software Engineering`, `LLM`, `Reliability` |
| 4 | Canonical URL: `https://github.com/MukundaKatta/agent-stack-reliability-primitives-paper` |
| 5 | Publish to your profile (or to a publication if you have one) |

After publishing, Medium gives a stable URL. Add it under `published_platforms` in `submission-metadata.json`.

---

## 11. Auto-aggregating discovery surfaces (no action — wait for crawl)

These index automatically once a DOI is registered with DataCite (which happened today, 2026-05-07T19:30Z):

| Aggregator | Typical lag | Status as of 2026-05-07 |
| --- | --- | --- |
| OpenAIRE | 1–7 days from Zenodo deposit | **not yet indexed** (recheck 2026-05-14) |
| Semantic Scholar | 1–2 weeks | **not yet indexed** (recheck 2026-05-21) |
| Google Scholar | 1–4 weeks | not yet indexed (recheck 2026-06-04) |
| BASE search | 1–2 weeks | not yet indexed |
| OpenAlex | 1–2 weeks | not yet indexed |
| CORE | 2–4 weeks | not yet indexed |

Set a calendar nudge for 2026-05-14 to re-run the propagation check.

---

## Recommended submission order

To keep the credibility curve climbing without bumping into editorial wait times:

1. **Today:** Figshare, OSF Preprints, HAL, ResearchGate (no editorial wait — DOIs mint instantly)
2. **Today:** Qeios, ScienceOpen (submit now so the editorial review starts)
3. **Today:** TechRxiv (1–2 day editorial check before DOI)
4. **Today:** ORCID — link all 10 Zenodo records in one sitting (5 min)
5. **Today:** Medium — paste + click Publish
6. **Whenever an endorser is confirmed:** arXiv

Total active platforms after this round: **9 paper-record platforms + 1 blog post + ORCID** with the DOI cross-linked across all of them.

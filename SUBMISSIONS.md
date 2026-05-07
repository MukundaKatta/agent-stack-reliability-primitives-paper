# Submission Handoff

Per-platform field values and upload pointers for the agent-stack reliability primitives preprint. Mirrors the established pattern from the karna paper package. Platform forms require browser-based ORCID or Google sign-in, so each block below is a copy-paste handoff.

## Common metadata

| Field | Value |
| --- | --- |
| Title | Six Reliability Primitives for LLM Agents: An Artifact Pattern for Stackable, Single-Concern Libraries |
| Author | Mukunda Rao Katta - Independent Researcher - mukunda.vjcs6@gmail.com |
| ORCID | (paste your ORCID iD when each platform asks) |
| Abstract | `abstract.txt` |
| Keywords | `keywords.txt` |
| Cover note | `cover-note.txt` |
| License | CC-BY-4.0 (manuscript), MIT (code) |
| Resource type | preprint |
| Version | v1 |
| Publication date | 2026-05-07 |
| Repository | https://github.com/MukundaKatta/agent-stack-reliability-primitives-paper |
| Landing page | https://mukundakatta.github.io/agent-stack/ |

## Files to upload (per platform that asks)

| File | Use it for |
| --- | --- |
| `agent-stack-reliability-primitives-preprint.pdf` | every platform |
| `agent-stack-qeios-manuscript.tex` | Qeios (preferred), TechRxiv (optional alongside PDF) |
| `agent-stack-qeios-latex-source.zip` | Qeios uses this if it asks for a LaTeX bundle |
| `agent-stack-reliability-primitives-preprint-package.zip` | Zenodo and Figshare to attach the full package alongside the PDF |

---

## Zenodo

Fastest credibility win: DOI within minutes, no editorial wait.

- URL: https://zenodo.org/uploads/new
- Sign-in: ORCID (you already use this)
- Resource type: **Publication → Preprint**
- Upload: PDF + the package ZIP (Zenodo lets you attach multiple)
- Communities: search for "open-source-research", "ai-research", and any community you've used before from your ai-eval-forge / agent-trajectory-replay submissions
- Related identifiers: paste each Agent* repo URL with relation type "is supplemented by" → that's the discovery surface that links the paper to the eighteen npm/PyPI packages
- Click "Publish". The DOI is minted on click.

Published May 7, 2026:

- Record: https://zenodo.org/records/20074702
- DOI: https://doi.org/10.5281/zenodo.20074702
- Concept DOI: https://doi.org/10.5281/zenodo.20074701

## Qeios

Submitted via ORCID + email verification per your established flow.

- URL: https://www.qeios.com/submit
- Article type: **Article** (Qeios doesn't separate preprint from article)
- Upload: prefer the LaTeX source from `agent-stack-qeios-latex-source.zip`. Fallback to the PDF.
- Abstract / keywords: paste from the files
- Subject categories: Computer Science → Software Engineering, Computer Science → Artificial Intelligence
- Funding / conflicts: none. Leave empty.
- Note: per your 2026-05-06 audit, Qeios profile visibility lags submission by ~24 hours. After the confirmation email, recheck the profile in a day before adding to public READMEs.

## ScienceOpen

Editorial-screened preprint, then DOI.

- URL: https://www.scienceopen.com/submit
- Sign-in: ORCID
- Submission type: **Preprint**
- Upload: PDF
- Subject categories: Computer Science → Software Engineering, Artificial Intelligence
- Cover note (paste): `cover-note.txt`
- After submit: pending editor decision via email. Per your karna and agent-trajectory-replay submissions the typical wait is a few days. Don't add to profile READMEs until the editor approves.

## Figshare

Already-confirmed venue per your 2026-05-06 audit (rag-guardrails item is live).

- URL: https://figshare.com/account/projects/upload
- Item type: **Preprint**
- Upload: PDF + the package ZIP (Figshare allows multi-file items)
- Categories: Software engineering, Artificial intelligence
- License: CC-BY-4.0
- Project: file under your existing "Research Footprints" project if you have one, otherwise stand-alone
- DOI: minted automatically. Figshare's DOI shows on the published page; paste it back into the metadata.

## TechRxiv (IEEE preprint server)

The IEEE-aligned preprint route. ORCID sign-in supported.

- URL: https://www.techrxiv.org/submit
- Sign-in: ORCID
- Article type: **Preprint**
- Subject area: Computing & Processing → Software Engineering, Artificial Intelligence
- Upload: PDF (TechRxiv accepts PDF; LaTeX optional)
- Abstract / keywords: paste from the files
- Funding: none
- After submit: TechRxiv assigns a DOI on acceptance after a short editorial check, usually 1 to 2 business days.

## OSF Preprints

A working-paper route that doesn't need endorsement.

- URL: https://osf.io/preprints/
- Provider: **OSF Preprints** (the generic provider)
- Upload: PDF
- License: CC-BY-4.0
- Tags: paste keywords from `keywords.txt` (one per line in the OSF tag field)
- Public visibility: yes
- DOI: minted automatically and shown on the published page

## arXiv (cs.SE)

Endorsement-gated. Documented for completeness. Submit only after you secure an endorser per your `next-venues.md`.

- URL: https://arxiv.org/submit
- Primary subject: cs.SE (Software Engineering)
- Cross-list: cs.AI (Artificial Intelligence)
- Upload: LaTeX source `agent-stack-qeios-manuscript.tex` (arXiv prefers source over PDF for cs.* categories)
- Comments field: "Companion to the karna-chat-native-assistant paper in the research-footprints/ series. CC-BY-4.0."
- License selection: "CC BY 4.0"

## ACM

ACM Digital Library does not accept independent preprints. The ACM-aligned route runs through:

- a peer-reviewed venue submission (HotSWE, ICSE workshop track, ASE tool track) where the agent-stack would fit under a tools/artifact track, and
- on acceptance, ACM Authorize lets you mirror the published version.

Recommendation: skip ACM as a *direct* submission target for this preprint. Use it after you have a venue-accepted version of the same content. The current preprint is a strong enough artifact to support a workshop submission down the line.

## IEEE

Same shape as ACM. IEEE Xplore is for accepted publications. The preprint route is **TechRxiv** (covered above) which IS aligned with IEEE.

If you want IEEE-flavored peer review later: target an IEEE workshop with a tools/artifact track (e.g. an IEEE/ACM ICSE workshop, IEEE COMPSAC software engineering track). The current preprint is the right artifact to attach to such a submission.

---

## Medium

Companion blog post lives in `medium-post.md`. Word count ~1500. Voice is plain (no em dashes per your style guide). Per your memory, you click Publish on Medium yourself; I'm not posting on your behalf.

To post:

1. https://medium.com/new-story
2. Paste `medium-post.md`
3. Add a header image (any of the agent-stack-site landing page screenshots; or use the colored "fit → guard → snap → vet → cast → budget" pipeline as a hand-drawn graphic)
4. Tags: `AI`, `Open Source`, `Software Engineering`, `LLM`, `Reliability`
5. Canonical URL: `https://github.com/MukundaKatta/agent-stack-reliability-primitives-paper`
6. Publish to a publication if you have one, otherwise to your profile

After publishing, Medium gives a stable URL. Add it to the metadata file.

---

## Profile README updates (after each acceptance)

For each platform that mints a stable URL or DOI, append to the publications section of your profile README. Pattern from your existing `next-venues.md`:

```
- Six Reliability Primitives for LLM Agents (preprint)
  - Zenodo: <DOI URL>
  - Qeios: <article URL after profile visibility confirmed>
  - ScienceOpen: <document URL after editor approval>
  - Figshare: <DOI URL>
  - TechRxiv: <DOI URL>
  - GitHub: https://github.com/MukundaKatta/agent-stack-reliability-primitives-paper
```

# Cross-Platform Propagation Tracker

Maps each of your 10 papers to every reputable preprint / artifact platform. ✅ = confirmed live. ⏳ = pending / in queue. — = not submitted yet (gap to fill). ✗ = blocked.

Verified live via API on 2026-05-07.

| Paper | Zenodo | Figshare | SSRN | Academia | ScienceOpen | Qeios | TechRxiv | OSF | HAL | ResearchGate | arXiv | Medium |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Six Reliability Primitives (agent-stack)** | ✅ [20074702](https://doi.org/10.5281/zenodo.20074702) | — | — | — | — | — | — | — | — | — | ⏳ endorse | — |
| **Karna: Chat-Native Multi-Channel** | ✅ [20074229](https://doi.org/10.5281/zenodo.20074229) | ✅ [32209317](https://doi.org/10.6084/m9.figshare.32209317) | — | — | — | — | — | — | — | — | ⏳ endorse | — |
| **Agent Trajectory Replay (v2)** | ✅ [20073574](https://doi.org/10.5281/zenodo.20073574) | — | — | — | ⏳ pending [47c2eaca](https://www.scienceopen.com/document/read?id=47c2eaca-be45-455f-9f1a-03dd016dc981) | ⏳ pending (sub 5246) | — | — | — | — | ⏳ endorse | — |
| **Small-Rule Guardrails (v2)** | ✅ [20057632](https://doi.org/10.5281/zenodo.20057632) | ✅ [32193543](https://doi.org/10.6084/m9.figshare.32193543) | — | — | — | — | — | — | — | — | ⏳ endorse | — |
| **Chetana: Consciousness Indicator** | ✅ [20057058](https://doi.org/10.5281/zenodo.20057058) | — | — | — | — | — | — | — | — | — | ⏳ endorse | — |
| **ML Intern Lab** | ✅ [20057317](https://doi.org/10.5281/zenodo.20057317) | — | — | ✅ [166763243](https://www.academia.edu/166763243) | — | — | — | — | — | — | ⏳ endorse | — |
| **AI Eval Forge** | ✅ [20044318](https://doi.org/10.5281/zenodo.20044318) | — | ✅ [6720559](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6720559) | — | — | — | — | — | — | — | ⏳ endorse | — |
| **Lightweight Evaluation Scorecards** | ✅ [20034550](https://doi.org/10.5281/zenodo.20034550) | — | — | — | — | — | — | — | — | — | ⏳ endorse | — |

## Coverage by platform

| Platform | Coverage | Note |
| --- | --- | --- |
| Zenodo | **9 / 9** | Strongest record. DataCite-registered, license CC-BY-4.0, ORCID-linkable. |
| Figshare | 2 / 9 | Karna + Guardrails. **7 papers missing.** Quick wins. |
| SSRN | 1 / 9 | AI Eval Forge only. SSRN takes a few days editorial. |
| Academia.edu | 1 / 9 | ML Intern Lab. Academia.edu auto-imports via DOI once you sign in. |
| ScienceOpen | 1 / 9 | Trajectory Replay (pending editor). Submit one paper at a time to avoid editor flagging. |
| Qeios | 0 confirmed live | sub 5246 not yet visible on profile/107118. |
| TechRxiv | 0 / 9 | **Whole stack missing.** IEEE-aligned, ORCID auth, fast. |
| OSF Preprints | 0 / 9 | **Whole stack missing.** No endorsement, fast DOI. |
| HAL | 0 / 9 | **Whole stack missing.** Open archive, no gate. |
| ResearchGate | 0 confirmed | Auto-imports via DOI. **5-min batch.** |
| arXiv | 0 / 9 | Endorsement-gated. cs.SE endorser still needed per `next-venues.md`. |

## Highest-leverage propagation (today's queue)

If you spend 30 minutes today, the order that gets the most distinct DOIs minted is:

1. **OSF Preprints (no editorial wait, mints DOI on click)** — submit all 9 papers. Each takes ~2 min. **+9 DOIs.**
2. **HAL (open archive, no editorial wait)** — same flow, all 9 papers. **+9 hal-IDs that auto-feed OpenAIRE / Semantic Scholar.**
3. **Figshare** — close the 7-paper gap. **+7 Figshare DOIs.**
4. **ResearchGate** — sign in once, search-by-DOI for the 9 Zenodo records, confirm authorship. **5-min batch, no DOI minting (uses Zenodo's).**
5. **TechRxiv** — submit the agent-stack paper as the IEEE-aligned anchor. Editorial check is fast. **+1 DOI in 1–2 days.**
6. **ORCID** — link all 9 Zenodo DOIs into your ORCID profile via the Crossref/DataCite search.

After this round: each paper is on a minimum of **5 platforms** (Zenodo + Figshare + OSF + HAL + ResearchGate), with TechRxiv / ScienceOpen / Qeios as additional editorial-wait surfaces.

## Per-paper paste-ready snippets

For each paper, the abstract / title / DOI / keywords are already in its respective `paper-package/` directory. The `PASTE_BUNDLES.md` doc in this package shows the agent-stack paper as the worked example; the same field shapes apply to the other 8.

For batch propagation of OLDER papers, the simplest move is:

1. Open the Zenodo record page for each paper.
2. Use the DataCite **"Cite as"** export to grab title + abstract + keywords in one click.
3. Paste into the target platform.

Or — if you want me to generate per-paper paste bundles for the 9 older papers in the same paste-ready format, say "yes generate per-paper bundles" and I'll loop over each paper-package/ directory and emit one bundle per paper.

## Auto-discovery surfaces (passive — no action)

Once each paper has a DataCite DOI (which all 9 do), the following platforms index it automatically:

- **OpenAIRE** (1–7 days)
- **Semantic Scholar** (1–2 weeks)
- **Google Scholar** (1–4 weeks)
- **BASE** (1–2 weeks)
- **OpenAlex** (1–2 weeks)
- **CORE** (2–4 weeks)

Re-check 2026-05-14 for the first wave.

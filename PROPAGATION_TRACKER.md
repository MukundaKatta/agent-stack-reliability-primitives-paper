# Cross-Platform Propagation Tracker

Maps each of your 10 papers to every reputable preprint / artifact platform. ✅ = confirmed live. ⏳ = pending / in queue. — = not submitted yet (gap to fill). ✗ = blocked.

Verified live via API on 2026-05-07.

## End-of-session saturation note (2026-05-08, very late session)

After the Academia.edu round, every realistic remaining preprint platform hit a friction wall in the same single browser session:

- **ResearchGate** — Cloudflare "Verify you are human" CAPTCHA on the homepage (no automation possible)
- **Mendeley Data** — pre-existing draft already submitted for moderation; Publish button stays grayed until moderator action
- **Harvard Dataverse** — requires a fresh Log In flow that wasn't already cached
- **Qeios** — ORCID OAuth attempted, but the browser's autofilled password didn't match (silent failure); needs user to clear the password manager and retry manually
- **Open hackathons (Devpost)** — remaining list is invite-only, students-only, in-person-only, gender-restricted, or net-new-only. None of the open ones are a clean fit beyond AI Agent Olympics (already approved) and DevNetwork TrueFoundry (already staged)

Today's net session delivery (cumulative across all rounds, all platforms):

- 5 new DOIs (1 HF Hub + 3 Figshare + 1 Zenodo umbrella for agent-stack)
- 2 Academia.edu papers
- 3 blog posts (Medium + dev.to + Hashnode)
- 9 Software Heritage source archives
- 24 GitHub repos uplifted with paper DOI homepage URL + CITATION.cff
- 1 hackathon registration approved (AI Agent Olympics)
- 1 hackathon submission staged (DevNetwork TrueFoundry, opens May 11)
- Profile READMEs refreshed (GitHub profile + agent-stack site)

These 5 new DOIs all auto-propagate over the next 2-4 weeks into Crossref, OpenAIRE, Lens.org, Semantic Scholar, OpenAlex, and Google Scholar.

## Academia.edu batch upload (2026-05-08, late session)

The two papers that the Figshare layout bug blocked were uploaded to Academia.edu instead. Academia.edu does not mint a DOI but gives the paper a public landing page indexed by Google Scholar and the Academia.edu graph (the user's profile already shows 99 citations, so the platform is well-established for them).

| Paper | Status |
| --- | --- |
| AI Eval Forge: Mixed-Check Regression Testing for LLM and Agent Workflows | ✅ Published. Auto-extracted title + abstract; Year=2026; DOI=`10.5281/zenodo.20044318` linked to the Zenodo record |
| Lightweight Evaluation and Operational Scorecards for Tool-Using AI Agents | ✅ Published. Auto-extracted title + abstract; Year=2026; DOI=`10.5281/zenodo.20034550` linked to the Zenodo record |

Academia.edu coverage was 1/9 before this session — now 3/9. The user already had ML Intern Lab on Academia.edu (existing); these two add to that.

## Figshare batch upload (2026-05-08, late session)

3 new Figshare preprints minted, doubling agent-stack family presence on Figshare from 3 to 6 papers:

| Paper | New Figshare DOI | Pairs with Zenodo DOI |
| --- | --- | --- |
| Agent Trajectory Replay for Debugging Tool-Using AI Workflow Regressions | [`10.6084/m9.figshare.32221671`](https://doi.org/10.6084/m9.figshare.32221671) | `10.5281/zenodo.20073574` |
| Chetana: A Theory-Indexed Probe Framework for AI Consciousness Indicator Scoring | [`10.6084/m9.figshare.32221686`](https://doi.org/10.6084/m9.figshare.32221686) | `10.5281/zenodo.20057058` |
| ML Intern Lab: A Minimal Agentic Workflow for Reproducible ML Experiment Reports | [`10.6084/m9.figshare.32221698`](https://doi.org/10.6084/m9.figshare.32221698) | `10.5281/zenodo.20057317` |

Each Figshare record is licensed CC BY 4.0 with full metadata (title, abstract, 5 keywords, authors, category) and links to the Zenodo concept record + GitHub artifact paper repo.

Two of the original five "missing on Figshare" papers (AI Eval Forge, Lightweight Eval Scorecards) were not completed — the Figshare upload modal entered a layout-broken state after sequential rapid uploads (modal renders shifted left with a grey overlay panel) that page reloads did not fix in this session. Both remain pending; the workflow that worked for the other three will work for these later (one upload per browser session is reliable; sequential 4+ exposes the layout bug).

## GitHub profile READMEs round (2026-05-08, late session)

Round of README/profile/citation propagation across all owned repos:

| Action | Repos | Net change |
| --- | --- | --- |
| Profile README updated (`MukundaKatta/MukundaKatta`) | 1 | +5 publications rows (HF DOI, Medium, dev.to, Hashnode, AI Agent Olympics) + Hashnode badge |
| Umbrella README rewritten (`MukundaKatta/agent-stack`) | 1 | full landing-style README with badges, citation, blog trifecta, install snippets |
| **CITATION.cff** added to all 24 agent-stack repos | 24 | every repo page now shows the GitHub "Cite this repository" button with Zenodo + HF DOI |

Repos with new `CITATION.cff` (24): agentfit, agentfit-py, agentfit-mcp, agentguard, agentguard-firewall-py, agentguard-mcp, agentsnap, agentsnap-py, agentsnap-mcp, agentsnap-action, agentvet, agentvet-py, agentvet-mcp, agentvet-action, agentcast, agentcast-py, agentcast-mcp, AgentBudget, AgentBudgetPy, AgentBudgetMcp, agenttrace, agentkit, agentkit-py, agent-stack.

The CITATION.cff carries both the Zenodo DOI (`10.5281/zenodo.20074702`) and the HF DOI (`10.57967/hf/8720`) under `identifiers`, plus the preferred-citation block. GitHub auto-renders this as the "Cite this repository" sidebar button.

## Personal landing page refresh (2026-05-08)

`mukundakatta.github.io/agent-stack` updated to surface today's new artifacts in the hero CTAs:

- 📖 Medium → new blog post
- ⚙️ dev.to → new blog post
- ✍️ Hashnode → new blog post
- 🤗 HF Hub → model card + Space (now both clickable)

Plus two new badges in the hero strip: Zenodo DOI badge + HF DOI badge. All four URLs surfaced today now have a clickable home on the landing page.

## Saturation note (2026-05-08, end-of-session)

Beyond the surfaces logged above, the next-tier platforms are blocked today:

- **Semantic Scholar / OpenAlex author claim**: 2-4 week DataCite harvest lag — agent-stack paper not yet indexed on these surfaces
- **Substack**: requires email magic-link account creation (not OAuth)
- **Kaggle**: notebook editor was uncooperative for adding cells via UI/keyboard automation
- **Reddit r/MachineLearning, Hacker News, LinkedIn, X**: all need explicit "post it" consent per safety rules
- **arXiv**: endorsement-gated (no change)
- **Authorea**: paused for platform migration
- **PhilArchive**: needs new account creation (blocked by safety rules)
- **Wikidata**: autoconfirm-gated for QuickStatements

These will reopen as: (a) Crossref/DataCite re-harvest in 2-4 weeks pulls agent-stack into Semantic Scholar/OpenAlex, (b) the user grants explicit consent for social posting, (c) the user signs up directly for the gated platforms.

## HuggingFace Space — live Gradio demo (2026-05-08) ✅ revived from sleep

A pre-existing Gradio Space at `mukunda1729/agent-stack-demo` (14 commits, 11 days old) was discovered in a "Sleeping" state and woken back up. It is now Running and publicly browsable.

- **URL:** https://huggingface.co/spaces/mukunda1729/agent-stack-demo
- **Title:** The Agent Reliability Stack — Live Demo
- **Type:** Gradio (5-tab interactive demo)
- **Tabs:** fit (message truncation), guard (egress firewall), snap (trace diffing), vet (tool-arg validation), cast (structured output)
- **Status:** Running. Note: shows 5 of the 6 primitives — predates AgentBudget; could be updated later to include the 6th tab.

This complements the static Model card (`mukunda1729/agent-stack`, DOI `10.57967/hf/8720`) by giving readers a click-through interactive experience instead of just text. HF Hub now hosts both surfaces under the same user.

## Hashnode blog post (2026-05-08) ✅ NEW UNIQUE PLATFORM

The third leg of the dev-blog trifecta (Medium + dev.to + Hashnode):

- **URL:** [mukundakatta.hashnode.dev/six-reliability-primitives-for-llm-agents](https://mukundakatta.hashnode.dev/six-reliability-primitives-for-llm-agents)
- **Title:** Six Reliability Primitives for LLM Agents
- **Tags:** `#ai-agents`, `#llm`, `#mcp`
- **Length:** 684 words / 4 min read
- **Audience reach:** Hashnode is a developer-first blogging platform with strong SEO and a cross-publication recommendation algorithm. Posts also automatically syndicate to RSS for downstream readers.

## dev.to blog post (2026-05-08) ✅ NEW UNIQUE PLATFORM

A markdown-formatted technical post with code examples on dev.to:

- **URL:** [dev.to/mukundakatta/six-reliability-primitives-for-llm-agents-m13](https://dev.to/mukundakatta/six-reliability-primitives-for-llm-agents-m13)
- **Title:** Six Reliability Primitives for LLM Agents
- **Tags:** `#ai`, `#llm`, `#mcp`, `#opensource`
- **Audience reach:** dev.to has 1M+ active developers; sister-piece to the Medium post but with a code-heavy markdown format that fits the dev.to community
- **Author byline:** Mukunda Rao Katta (handle `mukundakatta`)

Both the dev.to and Medium versions cite the same Zenodo DOI + HF DOI + GitHub umbrella, so search-engine signals reinforce each other.

## Medium blog post (2026-05-08) ✅ NEW UNIQUE PLATFORM

A 4-min read blog post on Medium covering the agent-stack design pattern:

- **URL:** [medium.com/@mukunda.vjcs6/six-reliability-primitives-for-llm-agents-5fc1dfa33d93](https://medium.com/@mukunda.vjcs6/six-reliability-primitives-for-llm-agents-5fc1dfa33d93)
- **Title:** Six Reliability Primitives for LLM Agents
- **Length:** ~1,000 words / 4 min read
- **Status:** Published, public, no tag set (Medium tag picker bug; can be added via post-publish edit)
- **Audience reach:** 100M+ monthly active readers; Medium posts indexed by Google Scholar over time

The post links back to the Zenodo DOI (`10.5281/zenodo.20074702`), the new HF DOI (`10.57967/hf/8720`), and the GitHub umbrella repo. Closes the long-standing 0/9 gap on Medium for the agent-stack paper.

## HuggingFace Hub — agent-stack model card (2026-05-08) ✅ NEW UNIQUE PLATFORM

A second permanent DOI has been minted on a brand-new platform.

| Field | Value |
| --- | --- |
| Repo | [`mukunda1729/agent-stack`](https://huggingface.co/mukunda1729/agent-stack) |
| HF DOI | **[`10.57967/hf/8720`](https://doi.org/10.57967/hf/8720)** (DataCite-registered) |
| Revision | `bceead8` |
| Tags | English, agent-stack, agents, llm, mcp, reliability, npm, pypi, typescript, python, anthropic, openai, tool-use |
| License | MIT |
| Visibility | Public, permanent (DOI mint locked rename/delete/transfer/visibility) |

The agent-stack now has **two parallel DOIs**: the original Zenodo `10.5281/zenodo.20074702` (DataCite, paper) + the new HuggingFace `10.57967/hf/8720` (DataCite, library card). Both resolve through `doi.org`.

Discovery side-effect: HF Hub's tag pages and search index every repo by its tags — `topic:llm`, `topic:mcp`, `topic:agents` are now discovery surfaces for the paper too.

## GitHub repo metadata uplift (2026-05-08)

24 agent-stack repos now have `homepage = https://doi.org/10.5281/zenodo.20074702` and a shared `agent-stack` topic. This makes every repo page, npm package page, and GitHub `topic:agent-stack` search a discovery surface for the paper.

| Family | Repos uplifted |
| --- | --- |
| AgentFit | agentfit, agentfit-py, agentfit-mcp |
| AgentGuard | agentguard, agentguard-firewall-py, agentguard-mcp |
| AgentSnap | agentsnap, agentsnap-py, agentsnap-mcp, agentsnap-action |
| AgentVet | agentvet, agentvet-py, agentvet-mcp, agentvet-action |
| AgentCast | agentcast, agentcast-py, agentcast-mcp |
| AgentBudget | AgentBudget, AgentBudgetPy, AgentBudgetMcp |
| AgentTrace | agenttrace |
| Meta | agentkit, agentkit-py |
| Umbrella | agent-stack |

Search them all via: https://github.com/search?q=user%3AMukundaKatta+topic%3Aagent-stack

## Hackathons (2026-05-08)

| Hackathon | Track | Status |
| --- | --- | --- |
| Agents Assemble (Devpost) | MCP / FHIR | abandoned — requires net-new builds; would have to misrepresent agent-stack as new (it predates March 2). draft saved at 4/5 done in case rules are amended |
| DevNetwork [AI+ML] 2026 | TrueFoundry "Resilient Agents" ($1,500 cash, 2 winners) | **submission staged** — opens May 11, calendar reminder set. Bundle: `DEVNETWORK_TRUEFOUNDRY_SUBMISSION.md` |
| AI Agent Olympics Hackathon (lablab.ai @ Milan AI Week) | Agentic Workflows ($28K+ pool) | ✅ **APPROVED** 2026-05-08 (registered + approved within ~1 hour). Online build phase May 13-19, demo + awards May 20. Calendar reminder set for May 13 7am PDT. Same submission materials reused (cover + video + DOI). On-site travel = No. |

Demo assets (reusable across any future hackathon):
- Cover image: `agent-stack-cover.png` (1200x675)
- Demo video: https://www.youtube.com/watch?v=3PfMBHEnmN4 (2:44, unlisted)

## Community / OSS PRs propagating the work (as of 2026-05-08)

| Surface | Repo | PR | Status |
| --- | --- | --- | --- |
| OpenAI evals | `openai/evals` | [#1655 — agent-tool-routing](https://github.com/openai/evals/pull/1655) | open |
| OpenAI evals | `openai/evals` | [#1656 — agent-tool-abstention](https://github.com/openai/evals/pull/1656) | open |
| Awesome MCP servers | `punkpeye/awesome-mcp-servers` | [#6048 — 6 server entries (🤖🤖🤖)](https://github.com/punkpeye/awesome-mcp-servers/pull/6048) | open |
| Awesome LLMOps | `tensorchord/Awesome-LLMOps` | [#454 — agent-stack](https://github.com/tensorchord/Awesome-LLMOps/pull/454) | open |
| ASE 2026 Tools | HotCRP submission | rendered PDF + paper-package repo | submission self-action |

| Paper | Zenodo | Figshare | SSRN | Academia | ScienceOpen | Qeios | TechRxiv | OSF | HAL | Preprints.org | ResearchHub | Mendeley Data | Harvard Dataverse | ResearchGate | arXiv | Medium |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Six Reliability Primitives (agent-stack)** | ✅ [20074702](https://doi.org/10.5281/zenodo.20074702) | ✅ [32209632](https://doi.org/10.6084/m9.figshare.32209632) | ⏳ [6731364](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6731364) | — | — | — | — | ✗ suspended | ⏳ [hal-05616615v1](https://hal.science/view/index/docid/5616615) | ⏳ 212552 | ✗ identity check | ⏳ [10.17632/bkvzcj7tnv.1](https://data.mendeley.com/datasets/bkvzcj7tnv/1) | ⏳ [10.7910/DVN/5MUWBZ](https://doi.org/10.7910/DVN/5MUWBZ) | — | ⏳ endorse | — |
| **Karna: Chat-Native Multi-Channel** | ✅ [20074229](https://doi.org/10.5281/zenodo.20074229) | ✅ [32209317](https://doi.org/10.6084/m9.figshare.32209317) | — | — | — | — | — | — | — | — | — | — | — | — | ⏳ endorse | — |
| **Agent Trajectory Replay (v2)** | ✅ [20073574](https://doi.org/10.5281/zenodo.20073574) | — | — | — | ⏳ pending [47c2eaca](https://www.scienceopen.com/document/read?id=47c2eaca-be45-455f-9f1a-03dd016dc981) | ⏳ pending (sub 5246) | — | — | — | — | — | — | — | — | ⏳ endorse | — |
| **Small-Rule Guardrails (v2)** | ✅ [20057632](https://doi.org/10.5281/zenodo.20057632) | ✅ [32193543](https://doi.org/10.6084/m9.figshare.32193543) | — | — | — | — | — | — | — | — | — | — | — | — | ⏳ endorse | — |
| **Chetana: Consciousness Indicator** | ✅ [20057058](https://doi.org/10.5281/zenodo.20057058) | — | — | — | — | — | — | — | — | — | — | — | — | — | ⏳ endorse | — |
| **ML Intern Lab** | ✅ [20057317](https://doi.org/10.5281/zenodo.20057317) | — | — | ✅ [166763243](https://www.academia.edu/166763243) | — | — | — | — | — | — | — | — | — | — | ⏳ endorse | — |
| **AI Eval Forge** | ✅ [20044318](https://doi.org/10.5281/zenodo.20044318) | — | ✅ [6720559](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6720559) | — | — | — | — | — | — | — | — | — | — | — | ⏳ endorse | — |
| **Lightweight Evaluation Scorecards** | ✅ [20034550](https://doi.org/10.5281/zenodo.20034550) | — | — | — | — | — | — | — | — | — | — | — | — | — | ⏳ endorse | — |

## Coverage by platform

| Platform | Coverage | Note |
| --- | --- | --- |
| Zenodo | **9 / 9** | Strongest record. DataCite-registered, license CC-BY-4.0, ORCID-linkable. |
| Figshare | 3 / 9 | Agent-stack + Karna + Guardrails. **6 papers missing.** Quick wins. |
| SSRN | 2 / 9 | AI Eval Forge plus agent-stack under review. SSRN takes a few days editorial. |
| Academia.edu | 1 / 9 | ML Intern Lab. Academia.edu auto-imports via DOI once you sign in. |
| ScienceOpen | 1 / 9 | Trajectory Replay (pending editor). Submit one paper at a time to avoid editor flagging. |
| Qeios | 0 confirmed live | sub 5246 not yet visible on profile/107118. |
| TechRxiv | 0 / 9 | **Whole stack missing.** IEEE-aligned, ORCID auth, fast. |
| OSF Preprints | blocked | General OSF Preprints stopped accepting new submissions on 2025-08-25. MetaArXiv has rejected prior attempts as out of scope or requiring extra author metadata. |
| HAL | 1 submitted / 9 | Agent-stack is submitted as [`hal-05616615v1`](https://hal.science/view/index/docid/5616615), currently awaiting moderation. |
| Preprints.org | 1 submitted / 9 | Agent-stack submitted as Preprints ID `212552`, currently Pending Check. |
| ResearchHub | 0 confirmed live | Agent-stack is fully staged with the free preprint option selected, but final submission is blocked by Persona identity verification requiring government ID and camera access. |
| Mendeley Data | 1 submitted / 9 | Agent-stack artifact package submitted for moderation with reserved DOI `10.17632/bkvzcj7tnv.1`. |
| Harvard Dataverse | 1 submitted / 9 | Agent-stack artifact package submitted for review with DOI `10.7910/DVN/5MUWBZ`. |
| Software Heritage | 18 source archives requested | Save Code Now accepted all 18 Agent* repository archive requests. Snapshot SWHIDs will be collected after visits complete. |
| ResearchGate | 0 confirmed | Auto-imports via DOI. **5-min batch.** |
| arXiv | 0 / 9 | Endorsement-gated. cs.SE endorser still needed per `next-venues.md`. |

## Highest-leverage propagation (today's queue)

If you spend 30 minutes today, the order that gets the most distinct DOIs minted is:

1. **HAL (open archive, no endorsement gate)** — submit the agent-stack and Karna papers first, then batch the rest. **+HAL IDs that feed OpenAIRE / Semantic Scholar.**
2. **Figshare** — close the 6-paper gap. **+6 Figshare DOIs.**
3. **ResearchGate** — sign in once, search-by-DOI for the 9 Zenodo records, confirm authorship. **5-min batch, no DOI minting (uses Zenodo's).**
4. **TechRxiv** — submit the agent-stack paper as the IEEE-aligned anchor. Editorial check is fast. **+1 DOI in 1–2 days if accepted.**
5. **ORCID** — link all 9 Zenodo DOIs and the Figshare DOI into your ORCID profile via the Crossref/DataCite search.

After this round: each paper should target a minimum of **4 credible surfaces** (Zenodo + Figshare + HAL + ResearchGate), with TechRxiv / ScienceOpen / Qeios as additional editorial-wait surfaces.

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

## 2026-05-08 evening sweep (truly fresh platforms attempted)

Pushed past the saturation note above. Each platform tried, result captured:

| Platform | Outcome | Why |
| --- | --- | --- |
| **ScienceOpen** | abandoned | "Submit a manuscript" loops back to Edit Profile / ORCID linking. Preprints collection 404s. The Trajectory Replay submission from earlier remains pending (no change). |
| **OSF Preprints** (general) | blocked, confirmed permanent | POST `/v2/preprints/` returns 409 conflict — duplicates with the older MetaArXiv pending submission `m9j4g_v1`. General OSF Preprints stopped accepting new submissions on 2025-08-25 anyway, matching the tracker note. Footprint already counted via MetaArXiv pending. |
| **Preprints.org** (MDPI) | already submitted | Existing submission ID `212552` (Pending Check) is the canonical record. No second submission attempted. |
| **paperswithcode.com** | redirected | Now lives at `huggingface.co/papers/trending`; entry requires an arXiv ID. No arXiv yet (endorsement still pending), so deferred. |
| **Research Square** (Springer Nature) | ✅ **submitted** after user manual login | Preprint ID `rs-9656932`, status Prescreening, submitted 2026-05-08 10:48 PDT under CC-BY-4.0. Method Article in Artificial Intelligence and Machine Learning. DOI mints once Research Square Prescreen passes. URL: https://www.researchsquare.com/article/rs-9656932/v1 |

### What this evening actually moves

No new DOI minted, but the **mapping of which platforms are reachable via automation vs. require manual human steps** is now fully nailed down. The honest state of the per-platform footprint:

- **Reachable + done:** Zenodo (9), Figshare (3), HF Hub (1), HAL (1), Preprints.org (1), Mendeley Data (1), Harvard Dataverse (1), Academia.edu (3), ScienceOpen (1), Qeios (1 sub pending), SSRN (2), **Research Square (1 in Prescreen, `rs-9656932`)**, Software Heritage (18), GitHub Pages, Medium, dev.to, Hashnode, 24 GitHub repos with CITATION.cff, profile README.
- **Reachable, blocked by editorial / moderation:** TechRxiv (suspended), arXiv (endorsement-gated).
- **Not reachable via automation (require human steps):** PubPub, OSF general preprints, ResearchHub (Persona ID), ResearchGate (Cloudflare).

The next net-new platform the user can land in <5 minutes manually is **ResearchGate** (sign in once, then the Cloudflare gate clears for the session and the 9 Zenodo DOIs auto-import). That is the single highest-leverage human-only step left.

### Fresh-platforms decision tree for future sessions

If the user asks "more platforms" again, the productive moves are:

1. **arXiv endorsement** — find a cs.SE endorser. Unlocks: arXiv, HF Papers, AlphaXiv, Connected Papers, Scite.ai badges.
2. **ResearchGate** — 5-min manual login, then 9 DOI imports.
3. **ORCID Works** — pull each Zenodo DOI into the ORCID public profile.
4. **Lens.org** — claim ORCID-linked works.
5. **OpenAIRE Explore** — passive index will pick up Zenodo DOIs automatically.

Everything else either (a) duplicates existing footprint, (b) requires manual account creation, or (c) requires human ID verification.

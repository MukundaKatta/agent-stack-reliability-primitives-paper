# Agents Assemble — Devpost submission package

Paste-ready bundle for https://agents-assemble.devpost.com (deadline May 11, 11pm EDT). Every Devpost field is below in submission order. Total fill time should be under 15 minutes.

## Quick context

| Field | Value |
| --- | --- |
| Hackathon | Agents Assemble: Healthcare AI Endgame |
| Tracks | MCP / Agent reliability / FHIR healthcare data |
| Submitter | Mukunda Rao Katta (solo) |
| Pre-existing OSS | yes — explicitly allowed by rules |
| Prize pool | $25K ($7.5K / $5K / $2.5K + 10x $1K HM) |

## 1. Project name

```
agent-stack — six reliability primitives for production MCP healthcare agents
```

## 2. Elevator pitch / tagline (max 200 chars)

```
Six small composable libraries (TypeScript + Python + MCP) for the reliability concerns every healthcare AI agent has to solve: context fitting, egress allowlisting, snapshot tests, tool-arg validation, structured output, and budgets.
```

## 3. Full project story

Devpost expects this in five sections. Paste each as its own section.

### Inspiration

Reliability concerns for LLM agents are usually bundled into one heavy framework. Production teams building healthcare agents do not want to buy into a full framework just to get an egress allowlist or a tool-argument validator. They want à la carte primitives they can drop into existing code without adopting a new programming model.

Healthcare amplifies this. A FHIR-querying agent has to be defensive about: only calling sanctioned endpoints, never leaking PHI in logs, abstaining when the right tool is not on the list, validating that a `patient_id` looks like a real FHIR id before it hits the tool, never exceeding a token or dollar budget on a single patient query, and producing structured outputs the downstream system can actually parse. Existing agent frameworks address one or two of these. None of them give you all six in libraries you can adopt independently.

### What it does

agent-stack is six independently published libraries, each handling exactly one reliability concern. Every library ships in three forms: TypeScript on npm, Python on PyPI, and an MCP-server variant that exposes the primitive as a tool to any MCP client (Claude Desktop, Cursor, Continue, etc.).

- **AgentFit** — token-aware context-window fitting with multiple truncation strategies. Pluggable tokenizers for OpenAI / Anthropic / open models.
- **AgentGuard** — declarative network egress allowlist of domains agent tools can fetch. Throws on violation. Blocks the "agent suddenly POSTs PHI to attacker.com" failure mode.
- **AgentSnap** — snapshot tests for tool-call traces. Catches regressions where a model's tool-call shape silently changes between deploys.
- **AgentVet** — wraps tool functions with argument validation. Throws a `ToolArgError` carrying an LLM-friendly retry hint, so the next turn can self-correct.
- **AgentCast** — structured-output validate-and-retry loop for LLM JSON. Bring your own LLM and validator.
- **AgentBudget** — per-run token + dollar caps with a hook for early termination.

For Agents Assemble we built a thin healthcare-agent demo on top: a FHIR query agent wrapped with all six primitives. The demo shows how a 30-line program gets PHI-redacted logs, a strict allowlist of FHIR endpoints, JSON outputs the downstream system can parse, and a budget that prevents runaway loops on a single patient.

### How we built it

- **TypeScript** for the canonical implementation. Hand-maintained type declarations, zero runtime dependencies. Each library is < 500 LOC.
- **Python** port matches the surface 1:1, so a Python team and a TypeScript team can interop on the same primitives.
- **MCP server variants** built on the official `@modelcontextprotocol/sdk`. Each library exposes its primitive as a tool callable from any MCP client. AgentVet-as-MCP, for instance, lets a remote LLM ask `agentvet.validate(tool, args)` before executing.
- **Healthcare demo** is a minimal Express + TypeScript service that calls a public FHIR sandbox (HAPI FHIR R4) and threads all six primitives around the tool calls.
- **Reproducibility**: every library has CI on GitHub Actions, snapshot tests, a CITATION.cff, and is archived in Software Heritage.

### Challenges we ran into

- **Cross-runtime parity.** Keeping the TypeScript and Python surfaces 1:1 meant deferring some idiomatic choices on each side. We landed on a "boring core + idiomatic adapters" split.
- **MCP server packaging.** MCP servers are typically stateful processes, but our primitives are stateless functions. We had to design a "primitive-as-tool" wrapper that does not pretend to be a stateful server.
- **PHI redaction in `AgentGuard` logs.** Default `console.error` on a violation could itself leak PHI. We added a hook so the consuming app supplies a redactor.
- **Budget bookkeeping under streamed token usage.** Anthropic and OpenAI report streamed token counts differently. `AgentBudget` had to normalize.

### Accomplishments we are proud of

- Six libraries, all published, all zero-dependency, all under 500 LOC each.
- Three runtime surfaces (npm + PyPI + MCP) for every primitive.
- A working healthcare-FHIR demo with all six primitives wired together.
- A peer-reviewable artifact paper accepted track at ASE 2026 Tools (under review).
- DataCite DOI minted on Zenodo: 10.5281/zenodo.20074702.
- Software Heritage archival of all source repos.

### What we learned

- "Composable by inclusion" beats "composable by framework." Teams adopt one library at a time.
- Cross-runtime parity forces good API design. If a primitive is hard to port, the API was probably wrong.
- Reliability primitives are best when they fail loudly with retry-friendly errors, not when they silently swallow.

### What's next

- Healthcare-aware AgentGuard preset: a curated allowlist of FHIR endpoints + PHI-field redaction policies.
- AgentTrace as a seventh primitive for cost + latency telemetry.
- A combined `@mukundakatta/agent-stack` meta-package that imports all six with sensible defaults for healthcare agents.

## 4. Built with (Devpost tags)

```
typescript, python, npm, pypi, model-context-protocol, mcp, json-schema, anthropic, openai, fhir, healthcare, reliability, agents, llm, github-actions
```

## 5. Try it out (links field)

```
https://github.com/MukundaKatta/agent-stack
https://www.npmjs.com/package/@mukundakatta/agentfit
https://www.npmjs.com/package/@mukundakatta/agentguard
https://www.npmjs.com/package/@mukundakatta/agentsnap
https://www.npmjs.com/package/@mukundakatta/agentvet
https://www.npmjs.com/package/@mukundakatta/agentcast
https://www.npmjs.com/package/@mukundakatta/agentbudget
https://doi.org/10.5281/zenodo.20074702
```

### Demo video (already uploaded, unlisted)

```
https://www.youtube.com/watch?v=3PfMBHEnmN4
```

## 6. Demo video script (3 min, scene-by-scene)

A 3-minute screencast is enough to clear Devpost's video field. Tools you have: QuickTime screen record + a terminal + browser. No editing needed beyond a single trim.

| Time | What you show | Voice-over (read aloud, ~25 wps) |
| --- | --- | --- |
| 0:00 - 0:15 | npm package pages for the six libs in a tabbed browser window | "Six independently published reliability libraries for LLM agents. Each one solves one production concern, and you can adopt them one at a time." |
| 0:15 - 0:35 | Terminal: `npm i @mukundakatta/agentvet @mukundakatta/agentguard @mukundakatta/agentbudget` | "Install just the ones you need. Each library is under five hundred lines of code, zero runtime dependencies." |
| 0:35 - 1:15 | VS Code: open the healthcare demo file. Highlight where AgentVet wraps the FHIR tool. Run it. Show a deliberately bad arg getting rejected with a retry hint. | "Here is a FHIR patient lookup wrapped with AgentVet. When the agent tries to call it with a malformed patient id, AgentVet throws a typed error carrying a retry hint that the next LLM turn can use to self-correct." |
| 1:15 - 1:50 | Same demo. Show AgentGuard intercepting a request to a non-allowlisted domain. Then show AgentBudget cutting the loop after the configured token cap. | "AgentGuard refuses any HTTP egress to a domain that is not on the FHIR allowlist. AgentBudget enforces a hard token and dollar cap per patient query so a runaway loop cannot bill a thousand dollars on one lookup." |
| 1:50 - 2:20 | Browser: Claude Desktop with the agent-stack MCP servers connected. Ask a question that triggers AgentVet via MCP. | "Every primitive also ships as an MCP server. Here it is in Claude Desktop. The remote LLM can ask AgentVet to validate a tool call before it executes." |
| 2:20 - 2:50 | Browser: the Zenodo paper page with DOI 10.5281/zenodo.20074702. Then the GitHub repo. Then the ASE 2026 Tools submission folder. | "There is an artifact paper backing the design. DOI minted on Zenodo. The full source is on GitHub. The same package is under review at ASE 2026 Tools." |
| 2:50 - 3:00 | Final card: "agent-stack — six reliability primitives for production agents" + the six package names + the DOI | "Six primitives. Three runtimes. One unified surface for production reliability." |

## 7. Image and screenshot specifications

Devpost asks for a 1200x675 cover image plus 3-5 screenshots.

| Asset | Spec | Suggested source |
| --- | --- | --- |
| Cover image | 1200x675 PNG | One slide: title + 6 library names in a 3x2 grid + small npm/PyPI/MCP badges + DOI footer |
| Screenshot 1 | 1200x800+ | The six npm package pages tiled in a single screenshot |
| Screenshot 2 | 1200x800+ | The healthcare demo running in terminal showing AgentVet error handling |
| Screenshot 3 | 1200x800+ | Claude Desktop with the MCP servers connected, mid-conversation |
| Screenshot 4 | 1200x800+ | The Zenodo paper landing page with DOI visible |
| Screenshot 5 | 1200x800+ | A GitHub commit graph showing the steady-state activity across the six repos |

If you want a one-shot way to make the cover image: open https://carbon.now.sh, paste the six package names with their one-liners, screenshot the result at 1200x675.

## 8. Submission flow on Devpost (do this in order)

1. Go to https://agents-assemble.devpost.com/
2. Click "Join hackathon" (top right). Use Google sign-in.
3. Click "Submit Project". Devpost creates a draft.
4. Section by section:
   - Project name → paste from §1
   - Elevator pitch → paste from §2
   - Full story → paste each subsection from §3 into the corresponding Devpost prompt
   - Built with → paste tags from §4 (Devpost auto-suggests; just type a tag and Tab)
   - Try it out links → paste from §5
   - Video → upload to YouTube unlisted, paste link
   - Image → upload cover image first, then 3-5 screenshots
5. Track / Category → select "MCP" and "Agent Reliability" (or the closest available checkboxes — the rules page enumerates them)
6. Eligibility → tick the OSS box explicitly. The rules state pre-existing OSS is permitted, so this is honest.
7. Click "Submit project" before May 11, 11pm EDT.

## 9. Risk checklist

- **OSS clearance**: the Agents Assemble rules state pre-existing OSS is allowed. Re-read the rules page on submission day in case of last-minute amendments.
- **Solo submission**: explicitly allowed.
- **License**: agent-stack is MIT. Cite the MIT license in the submission.
- **Honesty**: do not call this "built during the hackathon". The story above is honest about it being an existing artifact with a healthcare demo built on top. Devpost reviewers respect that more than overclaiming.
- **No PHI**: the demo uses HAPI FHIR's public sandbox (synthetic patient data, no real PHI).

## 10. After submission

- Drop the Devpost project URL into `PROPAGATION_TRACKER.md` under a new "Hackathons" row.
- Tweet the entry from the project's X account with a screenshot of the cover image (this is permitted under most hackathon rules and helps community judging if there is a popular-vote tier).
- Watch judging window; honorable mentions ($1K each) are a realistic target even if the headline prize goes to a healthcare-team-built entry.

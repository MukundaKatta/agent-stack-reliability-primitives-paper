# DevNetwork [AI + ML] Hackathon 2026 — TrueFoundry Resilient Agents track

Paste-ready submission bundle. Submissions open **May 11, 2026** and close **May 28, 2026 at 11:59pm PDT** (online portion).

URL: https://devnetwork-ai-ml-hack-2026.devpost.com/

## Why this track is the right fit

The TrueFoundry "Resilient Agents" track brief is a near-verbatim description of what agent-stack does:

> "How does your agent behave when an MCP server starts erroring out? An LLM server goes down? OpenAI or Claude errors out or browns out? The goal of this challenge is to see how user experience and the user side of things are handled when this infrastructure chaos happens and how your agent is configured and set up for success and resilience."

| TrueFoundry chaos scenario | agent-stack primitive that handles it |
| --- | --- |
| MCP server erroring out | AgentVet rejects bad responses with retry hint; AgentSnap catches the regression in CI |
| LLM server goes down | AgentBudget caps retries to prevent runaway loops; AgentCast retries with structured-output backoff |
| OpenAI / Claude error / brown-out | AgentBudget hard cap on tokens + dollars per run; AgentGuard blocks fallback to non-allowlisted endpoints |
| Agent configured for chaos | All six primitives compose; the demo shows them wired together around a single tool call |

Eligibility: 18+, any country, solo allowed, OSS allowed (no platform-lock-in like Agents Assemble had). Prize: **$1,500 cash for the TrueFoundry track ($1,000 / $500), 2 winners** + $8,000 overall pool.

## Submission paste-bundle

### 1. Project name (60 char limit)

```
agent-stack: six primitives for resilient MCP agents
```

### 2. Elevator pitch (200 char limit)

```
Six libraries (TS + Python + MCP) that make your agent survive infrastructure chaos: bounded budgets, snapshot tests, egress allowlist, tool-arg validation, structured-output retry, context-window fitting.
```

### 3. Project Story (Markdown — paste each subsection)

#### Inspiration

The TrueFoundry track asks: how does your agent behave when an MCP server errors out, an LLM goes down, or OpenAI brown-outs? Most agent frameworks bundle reliability concerns into one heavy dependency. Production teams want them à la carte — small, composable libraries you can drop in around your existing tool calls without buying into a new programming model.

#### What it does (resilience angle)

agent-stack is six independently published libraries, each handling one infrastructure-failure mode. Every library ships in three forms: TypeScript on npm, Python on PyPI, and an MCP-server variant.

- **AgentBudget** — hard cap on tokens and dollars per run. When an LLM brown-outs and your retry loop spirals, AgentBudget terminates early instead of billing $1000 on a single user query.
- **AgentVet** — wraps tool functions with argument validation. When an MCP server returns a malformed payload, AgentVet throws a typed `ToolArgError` carrying a retry hint the next LLM turn can use to self-correct.
- **AgentGuard** — declarative network egress allowlist. When an agent tries to fall back to a non-sanctioned endpoint after the primary fails, AgentGuard refuses the request at the network layer.
- **AgentSnap** — snapshot tests for tool-call traces. Catches the silent regression where an MCP server's response shape changes after a deploy.
- **AgentCast** — structured-output validate-and-retry loop. When an LLM returns malformed JSON during a brown-out, AgentCast retries with a constrained re-prompt.
- **AgentFit** — token-aware context-window fitting. When an agent's context spirals during a chaotic retry storm, AgentFit truncates intelligently instead of erroring.

A 30-line healthcare demo wires all six around a single FHIR query and is included in the repo.

#### How we built it

- **TypeScript** for the canonical implementation. Hand-maintained type declarations, zero runtime dependencies. Each library is under 500 LOC.
- **Python** port matches the surface 1:1, so a Python team and a TypeScript team can interop on the same primitives.
- **MCP server variants** built on the official `@modelcontextprotocol/sdk`. Every primitive callable as a tool from any MCP client (Claude Desktop, Cursor, Continue).
- **Reproducibility**: every library has CI on GitHub Actions, snapshot tests, a CITATION.cff, and is archived in Software Heritage.
- **Artifact paper** with DataCite DOI: 10.5281/zenodo.20074702 — under review at ASE 2026 Tools track.

#### Challenges we ran into

- **Cross-runtime parity.** Keeping the TypeScript and Python surfaces 1:1 meant deferring some idiomatic choices on each side. Landed on a "boring core + idiomatic adapters" split.
- **MCP server packaging.** MCP servers are stateful processes by convention but our primitives are stateless. We designed a "primitive-as-tool" wrapper that does not pretend to be a stateful server.
- **Budget bookkeeping under streamed token usage.** Anthropic and OpenAI report streamed token counts differently. AgentBudget normalizes.
- **Failing loudly in chaos.** Reliability primitives are most useful when they fail loudly with retry-friendly errors, not when they silently swallow. Each library throws typed errors carrying enough context for the next LLM turn or human operator to self-correct.

#### Accomplishments that we're proud of

- Six libraries, all published, all zero-dependency, all under 500 LOC each.
- Three runtime surfaces (npm + PyPI + MCP) for every primitive.
- A peer-reviewable artifact paper with DOI minted on Zenodo.
- All source archived in Software Heritage.
- Submitted to ASE 2026 Tools track (under review).

#### What we learned

- "Composable by inclusion" beats "composable by framework." Production teams adopt one library at a time.
- Cross-runtime parity forces good API design. If a primitive is hard to port, the API was probably wrong.
- The right place to handle infrastructure chaos is at the primitive boundary, not inside the model.

#### What's next for agent-stack

- AgentTrace as a seventh primitive for cost + latency telemetry.
- A combined `@mukundakatta/agent-stack` meta-package importing all six with sensible chaos-resilient defaults.
- Per-provider preset bundles (TrueFoundry preset, Anthropic preset, OpenAI preset).

### 4. Built with (tags)

```
TypeScript
Python
npm
PyPI
MCP
JSON Schema
Anthropic
OpenAI
Reliability
Resilience
Agents
LLM
GitHub Actions
```

### 5. Try it out (links)

```
https://github.com/MukundaKatta/agent-stack
https://doi.org/10.5281/zenodo.20074702
https://www.npmjs.com/~mukundakatta
```

### 6. Demo video URL

```
https://www.youtube.com/watch?v=3PfMBHEnmN4
```

### 7. Cover image

Use `~/Downloads/agent-stack-cover.png` (1200x675 PNG, already created).

### 8. Track selection

Tick the **"TrueFoundry: Resilient Agents"** track on the submission form. The submission may be eligible for both the overall prize and the track-specific prize; tick whichever options Devpost shows.

## Submission flow on May 11

1. Open https://devnetwork-ai-ml-hack-2026.devpost.com/
2. Click **Start project** (button appears once submissions open at 12:01am PDT May 11)
3. Fill in the fields above section-by-section
4. Tick the TrueFoundry track checkbox
5. Click **Submit project**
6. Drop the resulting Devpost project URL back to me; I'll log it in `PROPAGATION_TRACKER.md`

## Risk checklist

- **Eligibility**: 18+ ✓, any country ✓, solo allowed ✓
- **OSS pre-existing**: not explicitly prohibited in DevNetwork rules. The TrueFoundry brief asks "how is your agent configured for resilience" — agent-stack IS that configuration, packaged as libraries. Honest framing.
- **License**: MIT
- **Demo**: video already on YouTube unlisted; rules also allow live demo at AI DevSummit SF May 27-28 if you want the in-person bonus

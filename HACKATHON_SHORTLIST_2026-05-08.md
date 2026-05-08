# Hackathon Shortlist — verified 2026-05-08

Eight currently-open hackathons triaged for: pre-existing OSS allowed, solo allowed, theme fits the agent-stack / agent-tooling work. Strongest picks at the top.

## Top 3 to actually enter

### 1. Agents Assemble: Healthcare AI Endgame — **DEADLINE May 11, 11:00pm EDT** (3 days)

- URL: https://agents-assemble.devpost.com/
- Rules: https://agents-assemble.devpost.com/rules
- Theme: MCP, agent-to-agent, FHIR healthcare data
- Prize: $25K pool ($7.5K / $5K / $2.5K + 10x $1K honorable mentions)
- Eligibility: **OSS pre-existing allowed**, solo allowed
- Best fit: **agent-stack MCP server + AgentVet + AgentSnap** wrapped as a healthcare-agent demo. The MCP server work is already done; the wrapper is small.
- Why this one: it is the only listing that explicitly allows pre-existing OSS. Highest signal-to-effort ratio of the list.

#### Submission paste-bundle for Agents Assemble

```
Project name:
agent-stack — six reliability primitives for production MCP agents

Tagline (160 char):
Six small composable libraries (TypeScript + Python + MCP) that handle context fitting, network egress allowlist, snapshot tests, tool-arg validation, structured output, and budgets.

Track: MCP / Agent reliability

Demo URL:
https://github.com/MukundaKatta/agent-stack
https://www.npmjs.com/~mukundakatta

Inspiration:
Reliability concerns for LLM agents are usually bundled into one heavy framework. Production teams want them à la carte.

What it does:
Six independently-published libraries (npm + PyPI + MCP), each addressing one reliability concern: context fitting, egress allowlisting, snapshot tests for tool-call traces, tool-arg validation, structured-output enforcement, per-run budgets.

How we built it:
Each library is zero-dependency. TypeScript implementation has hand-maintained type declarations. Python port matches the surface. MCP-server variant exposes the same primitive as a tool to any MCP client (Claude Desktop, Cursor, etc.). Healthcare-agent demo wires AgentVet + AgentGuard + AgentBudget around a FHIR query tool.

What's next:
Add a healthcare-aware AgentGuard preset (allowlist of FHIR endpoints, redaction of PHI fields).

Built with:
TypeScript, Python, npm, PyPI, MCP, JSON Schema

Try it out:
https://www.npmjs.com/package/@mukundakatta/agentvet
(plus the rest of the @mukundakatta/agent* packages)
```

### 2. Google Cloud Rapid Agent Hackathon — **DEADLINE Jun 11, 2:00pm PDT** (5 weeks)

- URL: https://rapid-agent.devpost.com/
- Rules: https://rapid-agent.devpost.com/rules
- Prize: $50K pool ($5K / $3K / $2K across 5 partner tracks)
- Eligibility: solo allowed; **must be net-new project** (cannot submit existing OSS as the entry itself, but may incorporate it as a dependency)
- Best fit: build a thin Vertex AI app that orchestrates the existing agent-stack libs (legitimate net-new work that depends on shipped libraries)
- Submission shape (when ready): "Vertex-Agent-Sentry" — a small Cloud Run app that wraps a customer-support agent with all six reliability primitives and surfaces a dashboard. New code, dependencies on the published libs.

### 3. ML Empowerment Build Challenge — **DEADLINE May 12, 11:45pm PDT** (4 days)

- URL: https://ml-empowerment-build-challenge.devpost.com/
- Prize: certificates (no cash)
- Eligibility: solo allowed; OSS not prohibited
- Best fit: drop in **AI Eval Forge** or **AgentTrace** as the entry. Five-minute submission, low stakes, adds a hackathon credit to the footprint.

## Possibly worth it

### 4. AI Agent Olympics 2026 (Milan AI Week) — May 13-19, finale May 20

- URL: https://lablab.ai/ai-hackathons/milan-ai-week-hackathon
- Solo OK on Lablab; submit ML Intern Lab or Trajectory Replay
- Prize: TBC

### 5. DevNetwork [AI+ML] Hackathon 2026 — May 11-28 (AI DevSummit SF)

- URL: https://devnetwork-ai-ml-hack-2026.devpost.com/
- Submit Context Forge or AgentSnap
- Prize: DevNetwork swag + sponsor prizes

## Skip

- **Build with MeDo** (May 20) — requires MeDo no-code surface; weak fit
- **TinyFish** — deadline already past
- **Ruya AI Hackathon** — requires team of 2-5 (solo blocked)
- **USAII Global** — students-only
- **OpenAI Open Model Hackathon** — already ended Sep 2025
- **OpenEnv AI Hackathon (PyTorch)** — finale was Apr 25-26, already closed
- **AWS MCP Agents / A2A** — 2025 events, verify before submitting

## Action plan if you only have 1 evening

Spend it on **Agents Assemble** (May 11). Rationale: 3 days left, solo + OSS allowed, $25K pool, theme is MCP, your agent-stack is already MCP-published. Effort is paste-the-bundle-above + record a 3-min screencast of the libs running. The healthcare framing requires only a short README addendum, not new code.

## Action plan if you have 2 evenings

1. Tonight: ship Agents Assemble entry.
2. Tomorrow: ship ML Empowerment entry (5 minutes — same agent-stack repo, different framing as "evaluation tooling for ML practitioners").

That's two hackathon credits with no new code.

## Action plan if you have a full week

Add Google Cloud Rapid Agent (Jun 11). Build a small Vertex-AI Cloud Run app named e.g. "agent-sentry" that wraps a customer-support flow with all six reliability primitives and exposes a dashboard. Net-new code, depends on the shipped libs.

# Six Tiny Libraries for AI Agent Reliability

*A working pattern for splitting agent-runtime concerns into single-purpose, zero-dependency primitives.*

Most AI agent runtimes ship as one big framework. You pull in LangChain, LlamaIndex, AutoGen, or a vendor SDK and you get prompting, tool routing, retries, validation, observability, and budget enforcement in one dependency. That's convenient when your agent matches the framework's assumptions. It's a problem when it doesn't. Upgrades pull in unrelated changes. Defaults are hard to override. You can't adopt one reliability concern without adopting all the others.

I shipped six small libraries that take the opposite position. Each one solves exactly one problem. Each one is zero-dependency. Each one can be added to an existing agent without restructuring anything. Together they look like a stack you assemble, not a framework you adopt.

This post is a tour of what's in each library, why it exists, and the pattern that holds them together.

## The six

| Library | What it does | npm | PyPI | MCP |
|---|---|---|---|---|
| AgentFit | fit messages into a context window | `@mukundakatta/agentfit` | `agentfit-py` | `agentfit-mcp` |
| AgentGuard | network egress allowlist for tools | `@mukundakatta/agentguard` | `agentguard-firewall` | `agentguard-mcp` |
| AgentSnap | snapshot tests for tool-call traces | `@mukundakatta/agentsnap` | `agentsnap-py` | `agentsnap-mcp` |
| AgentVet | validate tool args before execution | `@mukundakatta/agentvet` | `agentvet-py` | `agentvet-mcp` |
| AgentCast | structured-output enforcer | `@mukundakatta/agentcast` | `agentcast-py` | `agentcast-mcp` |
| AgentBudget | token + dollar caps | `@mukundakatta/agentbudget` | `agentbudget-py` | `agentbudget-mcp` |

The conceptual pipeline runs left to right: **fit → guard → snap → vet → cast → budget**. You don't have to use them in that order, or use all of them. You can drop in just one.

## What each one does

**AgentFit** trims a message list to fit a model's context window. It accepts a token budget and a strategy — drop-oldest, drop-middle, or priority-keyed. The output is the trimmed list plus a structured report showing what was removed and why. Silent context truncation is the failure mode this library exists to surface.

**AgentGuard** is a declarative allowlist for tool egress. You list the domains your tools are allowed to fetch. Any outbound HTTP request to a domain not on the list throws with the offending URL. The failure mode is a tool fetching a URL the operator didn't anticipate; the library catches it at the egress site instead of in a billing alert later.

**AgentSnap** captures a hash-stable JSON envelope of every tool call your agent makes during a recorded run. You commit a baseline file. Future runs compare to that baseline and report drift. When a model upgrade or prompt revision changes the tool sequence in a way you didn't intend, the snap diff is the CI signal.

**AgentVet** wraps a tool with a schema (Zod, a built-in shape spec, or any `safeParse`-style validator). When the model hallucinates argument types and reaches the tool body, the wrapper catches it and throws a `ToolArgError` with a structured retry hint formatted for the next conversation turn. The model gets a clear chance to correct itself before the tool runs.

**AgentCast** is a validate-and-retry loop for structured output. You give it a schema, a target type, and an LLM call. It parses the response, translates validation errors into feedback for the model, and retries up to a configurable limit. Either typed data comes back or an error after the retry budget runs out. No prose where you wanted JSON.

**AgentBudget** counts tokens and dollars across an agent run and refuses calls that would push past your cap. After each LLM response you record usage; the library throws `BudgetExceededError` carrying the cap, the limit, the attempted total, and the model name. Built-in pricing covers Claude and GPT; you can override per model. Runaway loops turn into immediate errors instead of bills.

## The pattern

Three things are consistent across all six.

**Each one throws.** No silent fallbacks. If you adopted a reliability primitive, you adopted it because you wanted that specific failure to be observable. The libraries refuse to pretend a violated invariant is fine.

**Each error is a typed class with named fields.** `BudgetExceededError` has `cap`, `limit`, `attempted`, `overshoot`, `model`. `ToolArgError` has the tool name, the validation error, the rejected args, and a `toLLMFeedback()` method. Errors are designed to be programmatically dispatched and human-readable in incident logs at the same time.

**Each one has the same surface in three languages.** TypeScript is the reference. Python mirrors it with snake_case. The MCP variants expose the same primitives over the Model Context Protocol so any MCP-aware client (Claude Desktop, Cursor, Cline, Windsurf, Zed) can configure them declaratively. The contribution is the design, not the code; distributing it in three forms makes the design portable.

## Why split it this way

Two reasons.

**Trust surface.** Reliability primitives are infrastructure for the operator's confidence in the agent. Pulling third-party transitive dependencies into a primitive that's supposed to enforce a safety invariant expands the trust surface in a way that contradicts the goal. Zero runtime deps is the constraint that makes the libraries auditable.

**Granular adoption.** A user who needs only dollar caps doesn't have to adopt context-window fitting. A team that already has a tool-arg validator can use AgentBudget without learning AgentVet. The libraries don't know about each other; you can pin one at v0 and another at v1 without conflict resolution.

The trade-off is real. Monolithic frameworks make adoption easy at the cost of opinionated defaults. Stackable primitives make adoption granular at the cost of more decisions for the operator. I'm not claiming the granular path is correct in all settings. I'm saying it's currently underrepresented in published artifacts, and six libraries with single classes as their public surface are a usable example of the pattern.

## What's not in the stack

A few things are intentionally out of scope:

- **Rate limiting.** It interacts with provider headers and retry policies that don't compose cleanly with the existing primitives. Will be a separate library.
- **Unified observability.** Each library is silent about logging; you thread your own logger through the call sites. The omission keeps the zero-dependency invariant intact.
- **Memory or session safety.** That's a personal-assistant architecture concern, covered separately by the Karna paper in the same series.

## Where to start

If you're building an agent and looking for one place to begin:

```bash
npm install @mukundakatta/agentbudget
```

```js
import { Budget } from '@mukundakatta/agentbudget';

const budget = new Budget({ maxCostUsd: 5, maxTotalTokens: 200_000 });

for (const turn of turns) {
  const resp = await client.messages.create({ ... });
  budget.recordUsage({
    model: resp.model,
    inputTokens: resp.usage.input_tokens,
    outputTokens: resp.usage.output_tokens,
  });
}
```

That's it. No framework adoption, no migration, no opinionated defaults. The cap kicks in the moment you'd push past it.

Add the others as you need them.

## Read more

The longer artifact paper is on GitHub: [agent-stack-reliability-primitives-paper](https://github.com/MukundaKatta/agent-stack-reliability-primitives-paper). It documents the design, the cross-cutting invariants, and the operational considerations of running six small libraries instead of one big framework.

Landing page with all eighteen packages: [mukundakatta.github.io/agent-stack](https://mukundakatta.github.io/agent-stack/).

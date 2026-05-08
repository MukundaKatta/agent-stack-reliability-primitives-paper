# 5-Minute Screencast Script — Agent Reliability Stack (ASE 2026 Tools track)

**Mandatory per ASE Tools track CFP. Hosted on YouTube. Linked in the paper abstract.**

Total length target: **4:30–5:00**. Voice over the screen-share, no talking-head needed.

## Setup before recording

- Resolution: 1920×1080
- Tools tabs ready, clear browser cache, all popups dismissed
- Have these tabs preloaded:
  1. https://mukundakatta.github.io/agent-stack/
  2. https://www.npmjs.com/~mukundakatta
  3. https://pypi.org/user/mukunda.vjcs6/
  4. https://github.com/MukundaKatta/AgentBudget
  5. https://doi.org/10.5281/zenodo.20074702
  6. A code editor with these snippets pre-typed in separate files:
     - `budget-demo.js` (the AgentBudget example below)
     - `vet-demo.ts` (the AgentVet example below)
     - `snap-test.test.js` (the AgentSnap example below)
- Terminal panel visible alongside the editor

---

## Section 1 — Hook + Problem (0:00–0:30)

**Show:** the landing page (`mukundakatta.github.io/agent-stack/`).

**Narration:**
> "LLM agent runtimes are usually shipped as monolithic frameworks. One dependency gives you prompting, tool routing, validation, observability, budget caps, and safety filters. Convenient when your agent matches the framework's assumptions. A liability when it doesn't. The agent-stack is a deliberate counterpoint: six small libraries, each solving exactly one reliability concern, all zero-dependency, all independently versioned. You compose them by inclusion, not by framework adoption."

## Section 2 — The Six Primitives (0:30–1:30)

**Show:** scroll through the landing page Cards section.

**Narration (one beat per primitive):**
> "AgentFit fits messages into a context window, with a structured trim report. AgentGuard wraps tool egress in a declarative allowlist that throws when the agent fetches a domain it shouldn't. AgentSnap records tool-call traces, commits a baseline file, and turns trace drift into a CI signal. AgentVet validates tool arguments against a schema before the tool runs and feeds an LLM-friendly retry hint back to the model on failure. AgentCast wraps an LLM call in a validate-and-retry loop until the response is the requested shape. AgentBudget tracks tokens and dollars per run and refuses calls that would push past your cap."

## Section 3 — Live demo: AgentBudget (1:30–2:30)

**Show:** terminal + `budget-demo.js`.

```js
import { Budget, BudgetExceededError } from '@mukundakatta/agentbudget';

const budget = new Budget({ maxCostUsd: 0.05 });
const fakeCreate = async () => ({
  model: 'claude-sonnet-4-7',
  usage: { input_tokens: 2000, output_tokens: 1000 },
});

const create = budget.wrap(fakeCreate);
let calls = 0;
try {
  while (true) { await create(); calls++; }
} catch (e) {
  if (e instanceof BudgetExceededError) {
    console.log(`stopped at call ${calls}: ${e.cap} cap of $${e.limit} hit, attempted $${e.attempted.toFixed(4)}`);
  }
}
```

**Run:** `node budget-demo.js`

**Narration:**
> "Caps are post-call. By the time you have token counts, the call already cost money, so the library tallies and throws — but only on the call that pushed you past. The wrapped function recognizes the Anthropic and OpenAI response shapes by default; you can pass an extractor for any other provider. The thrown error names the cap, the limit, the attempted total, the model. Programmatically dispatchable, human-readable in incident logs."

## Section 4 — Live demo: AgentVet (2:30–3:15)

**Show:** `vet-demo.ts`.

```ts
import { vet, adapters, ToolArgError } from '@mukundakatta/agentvet';

const bookFlight = vet({
  name: 'book_flight',
  schema: adapters.shape({ origin: 'string', destination: 'string', passengers: 'number' }),
  fn: async ({ origin, destination, passengers }) => {
    return { booked: `${passengers}x ${origin}->${destination}` };
  },
});

try {
  await bookFlight({ origin: 'SFO', destination: 'JFK', passengers: '2' });
} catch (e) {
  if (e instanceof ToolArgError) {
    console.log('LLM-facing retry message:\n' + e.toLLMFeedback());
  }
}
```

**Run:** `tsx vet-demo.ts`

**Narration:**
> "AgentVet wraps a tool function with a schema. When the model hallucinates a string where you wanted a number, the wrapper catches it before the tool body runs, and gives the model a structured chance to correct itself in the next turn. The retry hint is formatted exactly the way the model's tool-result channel expects it."

## Section 5 — Live demo: AgentSnap regression (3:15–4:00)

**Show:** `snap-test.test.js` running through the test runner with a baseline already committed.

**Narration:**
> "AgentSnap captures the sequence of tool names and argument hashes into a JSON envelope and diffs against a committed baseline. When you change a model or a prompt and the agent's plan shifts in a way you didn't intend, the snap diff lights up in CI. No prose comparison, no LLM-as-judge — just structural drift detection on the tool sequence."

Demo a baseline-then-drift run, with the diff output visible.

## Section 6 — Cross-language symmetry + MCP (4:00–4:30)

**Show:** side-by-side npm package page (`@mukundakatta/agentbudget`) + PyPI page (`agentbudget-py`) + MCP registry entry.

**Narration:**
> "Each primitive ships in three implementations. TypeScript is the reference. The Python port mirrors the API with snake-case names. The MCP server exposes the same primitives over the protocol so any MCP-aware client — Claude Desktop, Cursor, Cline, Windsurf, Zed — can configure the reliability surface declaratively from a config file rather than from agent code. The contribution is the design pattern, not any single implementation."

## Section 7 — Reproducibility close (4:30–5:00)

**Show:** the Zenodo record at `10.5281/zenodo.20074702`, then the GitHub `agent-stack-reliability-primitives-paper` repo.

**Narration:**
> "The full reproducibility bundle is on Zenodo with DataCite-registered DOI. The paper, the LaTeX source, every package's source repo, every test suite. MIT for code, CC-BY-4.0 for the manuscript. Independent submission, no framework lock-in. Six small libraries, one consistent design pattern. agent-stack."

End card: tool URL, DOI, license.

---

## Recording checklist

- [ ] Test all three demo files run cleanly
- [ ] Pre-cache npm + PyPI + Zenodo pages (record offline if possible)
- [ ] Mic check; no background noise
- [ ] Cursor visible during code demos
- [ ] Voice-over rehearsed once before final take
- [ ] Export 1080p, MP4, ≤ 5:00
- [ ] Upload to YouTube as **Unlisted** initially (paper review only); switch to **Public** before camera-ready
- [ ] Replace the `AGENT_STACK_DEMO` placeholder URL in the .tex source with the real YouTube ID

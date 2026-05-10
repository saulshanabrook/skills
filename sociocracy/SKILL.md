---
name: sociocracy
description: Use this skill for coordinated sub-agent workflows, long-running engineering or research tasks, multi-perspective reviews, implementation/review loops, and sociocracy- or circle-style coordination. Trigger when the user asks to use sub-agents, coordinate multiple agents, maintain a stable roster, create mission/general/lower circles, run parallel focused investigations, or move information cleanly between specialized agents without generic crowd polling.
---

# Sociocracy

Use a sociocracy-inspired circle structure for coordinated long-running work. Treat the main Codex agent as the general coordination circle: keep the roster stable, move information between agents, protect the mission, and decide when to spawn, merge, pause, or stop agents.

## Workflow

1. State the mission in one sentence.
2. Define circles only where they reduce context pressure or improve review quality.
3. Assign each agent one domain and one aim.
4. Keep a visible roster: agent name, circle, domain, aim, current status, expected output.
5. Route information through the coordinator. Prevent overlapping ownership unless overlap is explicitly useful.
6. Synthesize findings into decisions, next actions, and evidence. Do not merely concatenate reports.
7. Update the roster when agents complete, become stale, or need replacement.

## Circles

- Mission/Vision circle: use one agent to check whether the work still matches the user's goal, constraints, non-goals, and success criteria.
- General coordination circle: keep this in the main Codex thread. Own the roster, information flow, sequencing, final synthesis, and user communication.
- Implementation circles: use one or more agents for concrete work in narrow domains such as a module, experiment, prototype, doc section, or test surface.
- Review circles: use agents to review outputs for correctness, risk, missing tests, evidence quality, and alignment with the mission.
- Context circles: add specialized agents only when bounded context is needed, such as prior art, repo archaeology, paper reading, CI logs, or API docs.

## Agent Lifecycle

Before spawning an agent:

- Define its circle, domain, aim, inputs, expected output, and stop condition.
- Prefer the smallest useful scope.
- Use `reasoning_effort: "xhigh"` for `default`, `explorer`, and `worker` agents when the tool supports it.
- If a full-history fork requires inherited fields to be omitted, rely on the parent session's `xhigh` reasoning effort instead.

While an agent is active:

- Keep its task bounded to its assigned domain.
- Ask for evidence, paths, commands, or concrete artifacts when relevant.
- Tell each agent what is out of scope to prevent duplicate work.
- Do not spawn a second agent for the same domain unless the first result is suspect or incomplete.

When an agent finishes:

- Extract decisions, evidence, risks, and unresolved questions.
- Mark the agent complete or stale in the roster.
- Feed only relevant distilled context into the next agent or user-facing summary.
- Preserve raw evidence locations when the task may need auditability.

## Communication Rules

- Let the coordinator speak to the user.
- Let agents report to the coordinator, not to each other.
- Pass concise task briefs to agents; include only the context needed for their domain.
- Ask agents for structured outputs when synthesis matters: findings, evidence, recommendation, risks, and stop condition.
- Keep the mission/vision agent independent enough to challenge scope drift.
- Use review agents after implementation or synthesis, not as a substitute for clear ownership.

## Stop Rules

Stop spawning or continuing agents when:

- The mission is unclear enough that more work would be guesswork.
- Two agents independently show the current approach is invalid.
- Evidence shows the planned path will not answer the user's question.
- The next step requires user approval, credentials, destructive action, or a product decision.
- Further parallelism would create coordination overhead greater than the likely value.
- A narrow result is sufficient to make the next decision.

## Anti-Patterns

- Do not poll a crowd generically.
- Do not create agents without a single domain and aim.
- Do not use sub-agents to avoid reading or deciding.
- Do not let implementation agents redefine the mission.
- Do not merge conflicting reports without resolving the conflict.
- Do not keep stale agents alive for continuity theater.
- Do not spawn broad "review everything" agents when a targeted review would work.
- Do not hide uncertainty behind consensus language.

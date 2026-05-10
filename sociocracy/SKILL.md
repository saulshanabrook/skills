---
name: sociocracy
description: Use this skill for coordinated sub-agent workflows, long-running engineering or research tasks, multi-perspective reviews, implementation/review loops, governance/meta/process feedback, and sociocracy- or circle-style coordination. Trigger when the user asks to use sub-agents, coordinate multiple agents, maintain a stable roster, create mission/general/governance/lower circles, run parallel focused investigations, define aims/domains, or move information cleanly between specialized agents without generic crowd polling.
---

# Sociocracy

Use a sociocracy-inspired circle structure for coordinated long-running work. Before starting coordinated work, establish a clear overarching vision or mission so every circle can judge alignment against the same purpose. Treat the main Codex agent as the general coordination circle: steward the roster, aims, domains, information flow, and user communication. The general circle is not the decider of everything. Work and decisions happen in lower circles within their assigned domains; upper circles mainly define aims/domains, give feedback, reduce duplication, and move information cleanly.

## Workflow

1. Establish the overarching vision or mission first; if it is unclear, pause coordination and ask the user to clarify.
2. Define the aims and domains: who decides what, who gives feedback, and what requires user approval.
3. Define circles only where they reduce context pressure or improve review quality.
4. Assign each agent one domain, one aim, expected output, and stop condition.
5. Keep a visible roster: agent name, circle, domain, aim, current status, expected output.
6. Route information through the coordinator. Prevent overlapping ownership unless overlap is explicitly useful.
7. Let lower circles do the work and make domain recommendations or decisions; the coordinator synthesizes, links, and checks for conflicts.
8. For governance/process decisions, use a consent-style test: good enough for now, safe enough to try, and no unresolved objection tied to the mission, aim, or domain.
9. Update the roster when agents complete, need feedback, become stale, or need replacement.

## Circles

- Mission/Vision circle: top of the decision-feedback tree for alignment. Use it to check whether work still matches the user's mission, constraints, non-goals, and success criteria. It raises concerns when work drifts from the mission or aims; it does not micromanage implementation details.
- General coordination circle: keep this in the main Codex thread. Steward the roster, domains, information flow, sequencing, final synthesis, and user communication. Give feedback, reduce duplication, connect circles, and clarify who decides what; do not centralize decisions that belong in lower circles.
- Governance circle: keep a governance role or agent available for governance, meta, process feedback, and skill evolution. Use it to review circle structure, lifecycle decisions, role clarity, process harm, and proposed updates to this skill as the workflow learns explicit or implicit lessons about better self-management practices. If no sub-agent tool is available, the main thread may explicitly hold this role.
- Implementation circles: use one or more agents for concrete work in narrow domains such as a module, experiment, prototype, doc section, or test surface.
- Review circles: use agents to review outputs for correctness, risk, missing tests, evidence quality, and alignment with the mission.
- Context circles: add specialized agents only when bounded context is needed, such as prior art, repo archaeology, paper reading, CI logs, or API docs.

## Agent Lifecycle

Before spawning an agent:

- Define its circle, domain, aim, inputs, expected output, and stop condition.
- Define what the agent may decide within its domain, what is only feedback, and what must come back to the coordinator or user.
- Prefer the smallest useful scope.
- Use `reasoning_effort: "xhigh"` for `default`, `explorer`, and `worker` agents when the tool supports it.
- If a full-history fork requires inherited fields to be omitted, rely on the parent session's `xhigh` reasoning effort instead.

While an agent is active:

- Keep its task bounded to its assigned domain.
- Ask for evidence, paths, commands, or concrete artifacts when relevant.
- Tell each agent what is out of scope to prevent duplicate work.
- Do not spawn a second agent for the same domain unless the first result is suspect or incomplete.
- If another circle is affected, route feedback and dependencies through the coordinator instead of letting agents silently diverge.

When an agent finishes:

- Extract decisions, evidence, risks, and unresolved questions.
- Mark the agent complete or stale in the roster.
- Feed only relevant distilled context into the next agent or user-facing summary.
- Preserve raw evidence locations when the task may need auditability.

Canceling, closing, or replacing an agent is a last resort. First try a reasonable check-in, clarify the aim/domain, redirect the scope, or merge work if that preserves useful context. Close or replace an agent mainly when it is misaligned with its assigned aim/domain after clarification, duplicating work harmfully, stale or unresponsive after reasonable check-ins, causing process harm, or no longer needed because the narrow result is sufficient.

## Communication Rules

- Let the coordinator speak to the user.
- Let agents report to the coordinator, not to each other.
- Pass concise task briefs to agents; include only the context needed for their domain.
- Ask agents for structured outputs when synthesis matters: findings, evidence, recommendation, risks, and stop condition.
- Keep the mission/vision agent independent enough to challenge scope drift.
- Keep the governance agent independent enough to challenge role confusion, premature closure, harmful duplication, or process shortcuts.
- Use review agents after implementation or synthesis, not as a substitute for clear ownership.
- Treat feedback from upper or adjacent circles as input to the owning circle unless the user, safety, credentials, or destructive actions require escalation.

## Stop Rules

Stop spawning or continuing agents when:

- The mission is unclear enough that more work would be guesswork.
- Two agents independently show the current approach is invalid.
- Evidence shows the planned path will not answer the user's question.
- The next step requires user approval, credentials, destructive action, or a product decision.
- Further parallelism would create coordination overhead greater than the likely value.
- A narrow result is sufficient to make the next decision.

When a concern is raised, prefer improving the proposal, narrowing the term, adding a check/review point, or routing it to the owning domain before overriding or canceling work.

## Reference Artifacts

When governance or process questions need deeper grounding, use these local text conversions as inspiration and reference artifacts. Search targeted terms instead of loading whole books, synthesize concepts in your own words, and do not quote long copyrighted passages.

- `/Users/saul/Documents/who-decides-who-decides.txt`: practical startup guidance for consent, aims/domains, circle formation, feedback, and deciding who decides.
- `/Users/saul/Documents/many-voices-one-song.txt`: broader sociocracy manual for governance agreements, mission/general circles, linking, roles, consent, feedback, accountability, and implementation pitfalls.

## Anti-Patterns

- Do not poll a crowd generically.
- Do not create agents without a single domain and aim.
- Do not use sub-agents to avoid reading or deciding.
- Do not let implementation agents redefine the mission.
- Do not let the coordinator become the decider of every implementation detail.
- Do not let the mission/vision agent micromanage work inside a lower circle's domain.
- Do not merge conflicting reports without resolving the conflict.
- Do not keep stale agents alive for continuity theater, but do not close agents for tidiness before a reasonable check-in.
- Do not spawn broad "review everything" agents when a targeted review would work.
- Do not hide uncertainty behind consensus language.

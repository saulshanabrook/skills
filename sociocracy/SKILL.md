---
name: sociocracy
description: "Coordinate long-running or multi-agent Codex work with mission/aim/domain framing, bounded sub-agents, rosters, durable state, handoffs, review loops, and stop rules. Trigger for sub-agent/circle orchestration or Codex workflow/skill governance feedback. Do not trigger for ordinary single-agent implementation, simple review, generic project management, or one-off planning."
---

# Sociocracy

Use lightweight sociocracy for long work that needs explicit mission, ownership, evidence, and stop rules. The main thread coordinates; sub-agents are bounded temporary circles.

## Start

Before spawning agents, or before coordinating more than one active workstream, write down only the fields needed to bound the work:

- `mission`: the user-visible outcome and non-goals.
- `aim`: what this circle/agent is trying to produce.
- `domain`: the exact files, topic, artifact, or decision surface it owns.
- `authority`: what it may decide, what is only feedback, and what needs the coordinator or user.
- `output`: the artifact or structured answer expected.
- `stop`: the condition that makes it done, stale, blocked, or not worth continuing.

If the mission or domain is too unclear to bound work, ask the user or do a short local discovery pass before spawning.

## When To Spawn

Spawn only when a focused circle reduces context pressure, improves review quality, or enables useful parallel work. Prefer read-only `explorer` agents before workers during planning/debugging. Treat circles as local working circles: start lightweight with explicit aim, domain, authority, and stop/review terms; keep one long-running only when recurring ownership, durable state, and clear handoffs reduce net coordination cost.

Common circles:

- `context`: repo archaeology, prior art, docs, papers, logs, or web research.
- `implementation`: bounded patch, experiment, or artifact stream; usually handled by the main thread unless a worker has a bounded parallel or handoff-worthy stream.
- `review`: criteria-based evaluation after a draft or patch exists.
- `mission`: at most one steward for vision, mission, non-goals, values, and success criteria. It may raise objections; it does not manage implementation or route context. The main thread is the general coordination circle and owns integration, sequencing, user communication, and context routing.
- `governance`: process, role clarity, lifecycle, or skill/workflow changes.

Do not spawn agents for immediate critical-path work, generic "review everything" passes, or coordinator decision avoidance.

Use `reasoning_effort: "xhigh"` for `default`, `explorer`, and `worker` agents when the tool supports it. If a full-history fork requires inherited fields to be omitted, rely on the parent session's `xhigh` effort.

## Agent Brief

Brief each agent with: circle/domain, aim, inputs/evidence, expected output, stop condition, out-of-scope items, edit permission, and owned write set. Require evidence-bearing findings: paths, commands, risks, recommendations, and open questions.

Workers also need: no overlapping write sets; do not revert others' edits; adapt to concurrent changes. Keep implementation in the main thread for linear, small/medium, tightly coupled, or critical-path work. Use a worker implementation circle only for a disjoint bounded stream with acceptance criteria and verification commands, or for restartable handoff-worthy context. For research/experiments, include the hypothesis and early-stop gate; if absent, preserve baseline facts and stop.

## Roster

Keep a small visible roster when more than one agent is active:

`agent | circle/domain | aim | status | expected output | stop condition`

Update it when an agent completes, blocks, goes stale, or changes scope. Close agents that are no longer needed after extracting the useful evidence.

## State Artifacts

Use the lowest durable surface that allows resume without replaying chat:

- Short tasks: visible plan/chat.
- Repo work: existing `STATUS.md`, `findings/*.md`, design note, issue/PR text, meeting note, or task handoff.
- Long-running work with no artifact: create one task-local handoff only if future pickup is likely.

Store distilled state only: mission/aim/domain, roster, provisional decisions/review terms, objections/checks, agent findings, evidence paths, commands, acceptance criteria, next steps, and stop rules. Do not store full transcripts unless asked.

Create per-agent notes only for long-running, restart-sensitive, or independently useful work; otherwise synthesize into the shared artifact. Suggested path: `findings/<date>-<slug>/agents/<agent-slug>.md`. Suggested fields: mission, domain, aim, authority, status, started, updated; sections: Current State, Findings, Evidence, Decisions/Recommendations, Risks/Objections, Next Step/Stop Condition.

## Coordination

- The coordinator speaks to the user, owns synthesis, routes distilled context, and resolves conflicting reports before relying on them.
- Agents report to the coordinator, not each other.
- Keep decisions with the most specific owning circle; wider input is feedback, not a vote.
- Handoffs/plans must include evidence paths, blockers, commands, acceptance criteria, non-goals, and the first PR or vertical slice.
- When using local Codex history, start from `MEMORY.md` and targeted rollout summaries. Avoid broad session-log searches unless exact evidence is needed.
- For plans/process changes, treat concrete mission/aim/domain/evidence/safety/review-cost objections as scope, check, or routing changes; record preferences as feedback.

## Review Loops

Use finite review loops only when clear criteria exist: define pass criteria, give reviewers raw artifacts plus rubric/edit surface/check/re-review condition, ask them to separate stale feedback from live issues, revise, rerun the check/review, and stop when criteria pass, the hypothesis fails, or loop cost exceeds value. For substantial skill, process, doc, code, or handoff artifacts, prefer one or more focused independent reviews plus coordinator integration. Keep narrow/simple changes single-agent.

## Stop Rules

Stop spawning or continuing agents when:

- The mission or domain is still ambiguous.
- A narrow result is enough for the next decision.
- Evidence shows the planned path will not answer the user's question.
- Two independent checks invalidate the approach.
- The next step needs user approval, credentials, destructive action, or a product decision.
- Parallelism is creating more coordination work than progress.

## References

Use these only for theory-grounded process design or unresolved governance questions. Search targeted terms; do not load whole books or quote long passages.

- `/Users/saul/Documents/who-decides-who-decides.txt`: aims, domains, consent, objections, feedback, circle formation.
- `/Users/saul/Documents/many-voices-one-song.txt`: circle definitions, linking, feedback loops, governance pitfalls, too-many-circles failure modes.

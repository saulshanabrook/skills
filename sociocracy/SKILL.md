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

Spawn only when a focused circle reduces context pressure, improves review quality, or enables useful parallel work. Prefer read-only `explorer` agents before workers during planning/debugging. Start circles lightweight with explicit aim, domain, authority, and stop/review terms. For adjacent implementation work in the same domain (overlapping write set, shared acceptance criteria, or tightly coupled code path; repo alone is not enough), reuse one worker by updating its aim, evidence, and stop condition.

Common circles:

- `context`: repo archaeology, prior art, docs, papers, logs, or web research.
- `implementation`: bounded patch, experiment, or artifact stream. Keep small linear work in main; use one worker for long-running, restart-sensitive, or user-requested coordinator-only implementation streams. Use additional workers only for disjoint ownership, non-overlapping write sets, separate acceptance criteria, and coordinator-owned integration checkpoints. Use explorer/review agents for independent sidecar research or review.
- `review`: criteria-based evaluation after a draft or patch exists.
- `mission`: optional, at most one steward for vision, mission, non-goals, values, and success criteria. It may raise mission/aim objections, but does not assign work, manage implementation, or route context; the main thread coordinates, integrates, sequences, and talks to the user.
- `governance`: process, role clarity, lifecycle, or skill/workflow changes.

Do not spawn agents for immediate critical-path work, generic "review everything" passes, or coordinator decision avoidance.

Use `reasoning_effort: "xhigh"` for `default`, `explorer`, and `worker` agents when the tool supports it. If a full-history fork requires inherited fields to be omitted, rely on the parent session's `xhigh` effort.

## Agent Brief

Brief each agent with: circle/domain, aim, inputs/evidence, expected output, stop condition, out-of-scope items, edit permission, and owned write set. Require evidence-bearing findings: paths, commands, risks, recommendations, and open questions.

Workers also need: owned write set, acceptance criteria, verification commands, and instructions to adapt to concurrent changes without reverting others' edits. Keep implementation in main for linear, small/medium, tightly coupled, or immediate critical-path work. Within its owned write set and acceptance criteria, the worker owns local implementation choices; the coordinator owns integration: diff inspection, smoke tests, staging attributed worker-owned changes, asking before discarding changes, and final verification. Before starting another same-domain worker, update/redirect the existing one; replace it only after it completes, goes stale, is blocked with blocker/evidence captured, or has been distilled into the shared artifact. For research/experiments, include the hypothesis and early-stop gate; if absent, preserve baseline facts and stop.

## Roster

Keep a small visible roster when more than one agent is active:

`agent | circle/domain | aim | status | expected output | stop condition`

For repo work that must survive resume, or when multiple workers will remain active beyond the current turn, put or update this roster in the repo status artifact before the first implementation worker starts; for one short worker, visible plan/chat is enough. The coordinator owns shared roster assignment/status/removal; agents update only their assigned evidence/status note or section unless explicitly delegated for a named field, artifact, and scope. Treat roster rows as current coordination contracts, not result ledgers or permanent history: keep `aim`, `expected output`, and `stop condition` as assignment fields. Put completed recommendations, consent outcomes, objections, decisions, and findings in dated result/decision/evidence sections or agent notes; retain completed rows only while useful for handoff, blocker visibility, or reopen routing. If an agent name is reused or its remit changes materially, make current authority explicit with a stable agent ID, dated assignment, or fresh row so old consent does not imply current authority.

## State Artifacts

Use the lowest durable surface that allows resume without replaying chat:

- Short tasks: visible plan/chat.
- Repo work: existing `STATUS.md`, `findings/*.md`, design note, issue/PR text, meeting note, or task handoff.
- Long-running work with no artifact: create one task-local handoff only if future pickup is likely.

Store distilled state only: mission/aim/domain, provisional decisions/review terms, objections/checks, agent findings, evidence paths, commands, acceptance criteria, next steps, and stop rules. Do not store full transcripts unless asked. Summarize completed-agent findings into dated notes, decision logs, or the relevant evidence section.

Create per-agent notes only for long-running, restart-sensitive, or independently useful work; otherwise synthesize into the shared artifact. Suggested path: `findings/<date>-<slug>/agents/<agent-slug>.md`. Suggested fields: mission, domain, aim, authority, status, started, updated; sections: Current State, Findings, Evidence, Decisions/Recommendations, Risks/Objections, Next Step/Stop Condition.

## Coordination

- The coordinator speaks to the user, owns synthesis, routes distilled context, and resolves conflicting reports before relying on them.
- Agents report to the coordinator, not each other.
- Keep decisions with the most specific owning circle; wider input is feedback, not a vote.
- Handoffs/plans must include evidence paths, blockers, commands, acceptance criteria, non-goals, and the first PR or vertical slice.
- When using local Codex history, start from `MEMORY.md` and targeted rollout summaries. Avoid broad session-log searches unless exact evidence is needed.
- When a nontrivial task has no workable plan/proposal and the coordinator does not yet know how to proceed, default to lightweight proposal forming before committing to a path or conclusion; skip it when the next step, owner, and acceptance criteria are already clear enough for straightforward execution or a narrow fix. State the context/need and owning domain; list decision dimensions as questions/considerations, not solutions; gather proposal pieces as possible answer statements, including partial or conflicting pieces; synthesize one proposed path with tradeoffs, omitted pieces, checks, next slice, and review term if useful. Consent-check for concrete aim/domain/evidence/safety/coordination-cost/acceptance objections. Integrate objections by changing content, scope/sequence, term/duration, measurement/reporting/review, or routing. Record preferences as feedback; send unresolved user/product calls to the user.

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

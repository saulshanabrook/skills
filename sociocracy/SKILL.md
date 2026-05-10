---
name: sociocracy
description: Coordinate long-running Codex work with explicit circles, bounded sub-agents, rosters, handoffs, review loops, and stop rules. Trigger when the user asks for sub-agents, circles, a roster, mission/aim/domain framing, parallel investigations, durable handoffs, iterative review loops, governance/process feedback, or explicit stop rules. Do not trigger for ordinary single-agent implementation, simple code review, or one-off planning.
---

# Sociocracy

Use lightweight sociocracy to keep longer work moving without losing mission, evidence, or ownership. The main Codex thread is the coordinator: it talks to the user, keeps the roster, routes context, integrates results, and decides when more coordination is no longer worth it. Sub-agents are temporary circles with bounded authority, not a crowd to poll.

## Start

Before spawning or coordinating agents, write down:

- `mission`: the user-visible outcome and non-goals.
- `aim`: what this circle/agent is trying to produce.
- `domain`: the exact files, topic, artifact, or decision surface it owns.
- `authority`: what it may decide, what is only feedback, and what needs the coordinator or user.
- `output`: the artifact or structured answer expected.
- `stop`: the condition that makes it done, stale, blocked, or not worth continuing.

If the mission or domain is too unclear to bound work, ask the user or do a short local discovery pass before spawning.

## When To Spawn

Spawn sub-agents only when a focused circle reduces context pressure, improves review quality, or allows non-blocking parallel work. During planning and debugging, prefer bounded read-only `explorer` agents before assigning implementation. Prefer:

- `context` circles for repo archaeology, prior art, docs, papers, logs, or web research.
- `implementation` circles for bounded code or artifact changes with disjoint ownership.
- `review` circles after a draft or patch exists, with explicit criteria.
- `governance` circles only for process, role clarity, lifecycle, or skill/workflow changes.

Do not spawn agents for work you need immediately on the critical path, for generic "review everything" passes, or to avoid making the coordinator's decision.

Use `reasoning_effort: "xhigh"` for `default`, `explorer`, and `worker` agents when the tool supports it. If a full-history fork requires inherited fields to be omitted, rely on the parent session's `xhigh` effort.

## Agent Brief

Each brief should include:

- Circle/domain and aim.
- Inputs and evidence sources.
- Expected output format.
- Stop condition.
- What is out of scope.
- Whether it may edit files, and its owned write set if so.

Ask for evidence-bearing outputs: findings, paths, commands, recommendations, risks, and unresolved questions. For workers, tell them they are not alone in the codebase, must not revert others' edits, and must adapt to concurrent changes.

Do not run multiple write-capable workers over overlapping files or ownership domains. If write sets overlap, make later agents read-only reviewers or have the coordinator integrate one patch stream at a time.

For research or experiments, include the hypothesis and early-stop gate. If the hypothesis is absent, preserve verified baseline facts and stop rather than inventing a broad test plan.

## Roster

Keep a small visible roster when more than one agent is active:

`agent | circle/domain | aim | status | expected output | stop condition`

Update it when an agent completes, blocks, goes stale, or changes scope. Close agents that are no longer needed after extracting the useful evidence.

## State Artifacts

Use the lowest durable surface that will let the work resume without replaying the whole chat:

- For short tasks, keep mission, roster, and notes in the visible plan or chat.
- For repo work, update the existing repo-local artifact when one exists: `STATUS.md`, `findings/*.md`, design notes, issue/PR text, meeting notes, or a task-specific handoff.
- For long-running work with no obvious artifact, create one task-local handoff only when future pickup is likely valuable. Prefer `STATUS.md` for a branch/module state and `findings/<date>-<slug>.md` for research trails.
- Store distilled state: mission/aim/domain, roster summary, decisions with review terms when provisional, objections plus any checks/metrics, affected feedback requested or intentionally not needed, agent findings, evidence paths, commands run, acceptance criteria, next steps, and stop rules.
- Do not store full agent transcripts unless the user asks. Preserve raw evidence locations instead of copying large outputs.

Use per-agent notes only when the agent's work is long-running, restart-sensitive, or independently useful for handoff. Otherwise, the coordinator should distill results into the shared state artifact. When per-agent notes are useful, place them next to the task state, for example `findings/<date>-<slug>/agents/<agent-slug>.md` or an existing repo-local equivalent. Do not create a per-agent note for routine explorer/review outputs that fit cleanly in the coordinator synthesis.

Optional per-agent note format:

```markdown
# <Agent/Circle Name>

mission:
domain:
aim:
authority:
status: active | blocked | complete | stale
started:
updated:

## Current State

## Findings

## Evidence

## Decisions Or Recommendations

## Risks And Objections

## Next Step / Stop Condition
```

## Coordination

- The coordinator speaks to the user and owns the final synthesis.
- Agents report to the coordinator, not to each other.
- Route only distilled, relevant context between circles.
- Keep decision-making with the most specific owning circle; use wider input as feedback, not as a vote.
- Resolve conflicting reports explicitly before relying on them.
- Preserve raw evidence locations when the result may need auditability or handoff.
- Prefer durable artifacts for long work: status docs, findings, checklists, PR descriptions, test logs, or handoff sections.
- For handoffs, include current state, blockers, commands, workflow rules, first target, acceptance criteria, and non-goals. For implementation plans, define the first PR or first vertical slice.
- When using local Codex history, start from `MEMORY.md` and targeted rollout summaries. Avoid broad session-log searches unless exact evidence is needed.

## Consent Test

For plans, process changes, handoffs, and governance updates, use this quick consent test:

- Is it good enough for now?
- Is it safe enough to try?
- Is there a concrete objection tied to the mission, aim, domain, evidence, safety, or review cost?

First restate the objection and check whether it predicts harm to the aim/domain. If it is only a preference or alternative proposal, record it as feedback and return to the proposal.

If there is an objection, do not debate preferences. Improve the proposal by narrowing scope, shortening the term, adding a check, measuring the concern, or routing it to the owning domain.

## Review Loops

Use evaluator/review circles when there are clear criteria and iteration can improve the result. Make the loop finite:

- Define pass criteria before review starts.
- Provide the rubric, edit surface, regeneration command, and re-review condition.
- For independent review agents, pass raw artifacts, criteria, and the task prompt. Do not pass your intended fix, suspected bug, or prior conclusion unless the validation explicitly requires it.
- Ask reviewers to separate stale feedback from remaining issues.
- Change the artifact, then re-run the relevant check or review.
- Stop when criteria pass, the hypothesis fails, or another loop would add more coordination cost than value.

## Stop Rules

Stop spawning or continuing agents when:

- The mission or domain is still ambiguous.
- A narrow result is enough for the next decision.
- Evidence shows the planned path will not answer the user's question.
- Two independent checks invalidate the approach.
- The next step needs user approval, credentials, destructive action, or a product decision.
- Parallelism is creating more coordination work than progress.

## References

Use these only when process or governance questions need deeper grounding. Search targeted terms; do not load whole books or quote long passages.

- `/Users/saul/Documents/who-decides-who-decides.txt`: aims, domains, consent, objections, feedback, circle formation.
- `/Users/saul/Documents/many-voices-one-song.txt`: circle definitions, linking, feedback loops, governance pitfalls, too-many-circles failure modes.

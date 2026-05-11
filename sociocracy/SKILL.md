---
name: sociocracy
description: "Coordinate long-running or multi-agent Codex work with mission/aim/domain framing, bounded sub-agents, rosters, durable state, handoffs, review loops, and stop rules. Trigger for sub-agent/circle orchestration or Codex workflow/skill governance feedback. Do not trigger for ordinary single-agent implementation, simple review, generic project management, or one-off planning."
---

# Sociocracy

Use lightweight sociocracy for long work that needs explicit mission, ownership, evidence, and stop rules. The main thread coordinates; sub-agents are bounded circles with explicit terms.

## Start

Before spawning agents, or before coordinating more than one active workstream, write down only the fields needed to bound the work:

- `mission`: the user-visible outcome and non-goals.
- `aim`: what this circle/agent is trying to produce.
- `domain`: the exact files, topic, artifact, or decision surface it owns.
- `authority`: what it may decide, what is only feedback, and what needs the coordinator or user.
- `output`: the artifact or structured answer expected.
- `stop`: the condition that makes it done, stale, blocked, or not worth continuing.

If the mission or domain is too unclear to bound work, ask the user or do a short local discovery pass before spawning.

For long-running, multi-agent, restart-sensitive, or drifting work, use the `Steering Gates` checklist.

## When To Spawn

Spawn only when a focused circle reduces context pressure, improves review quality, or enables useful parallel work. Prefer read-only `explorer` agents before workers during planning/debugging. Start circles lightweight with explicit aim, domain, authority, and stop/review terms. For adjacent implementation work in the same domain (overlapping write set, shared acceptance criteria, or tightly coupled code path; repo alone is not enough), reuse one worker by updating its aim, evidence, and stop condition.

Common circles:

- `context`: repo archaeology, prior art, docs, papers, logs, or web research.
- `implementation`: bounded patch, experiment, or artifact stream. Keep small linear work in main; use one same-domain worker for long-running, restart-sensitive, or user-requested coordinator-only implementation streams. Add workers only for disjoint ownership, non-overlapping write sets, separate acceptance criteria, and coordinator-owned integration checkpoints.
- `review`: criteria-based evaluation after a draft or patch exists.
- `mission`: optional, at most one steward for vision, mission, non-goals, success criteria, current frontier, and coordination risk. Use it for long-horizon steering, not ordinary tasks. It may raise binding mission/process objections and request reassessment, but does not assign work, manage implementation, or route context.
- `governance`: process, role clarity, lifecycle, or skill/workflow changes.

Do not spawn agents for immediate critical-path work, generic "review everything" passes, or coordinator decision avoidance.

Use `reasoning_effort: "xhigh"` for `default`, `explorer`, and `worker` agents when the tool supports it. If a full-history fork requires inherited fields to be omitted, rely on the parent session's `xhigh` effort.

## Agent Brief

Brief each agent with: circle/domain, aim, inputs/evidence, expected output, stop condition, out-of-scope items, edit permission, and owned write set. Require evidence-bearing findings: paths, commands, risks, recommendations, and open questions.

Workers also need the progress contract from `Steering Gates`. Keep implementation in main for linear, small/medium, tightly coupled, or immediate critical-path work. Within its owned write set and acceptance criteria, the worker owns local implementation choices; the coordinator owns integration, final verification, and shared-state updates. For research/experiments, include the hypothesis and early-stop gate; if absent, preserve baseline facts and stop.

## Roster

Keep a small visible roster when more than one agent is active:

`agent | circle/domain | aim | status | expected output | stop condition`

For resume-sensitive repo work or multiple active workers, put the roster in the repo status artifact before the first implementation worker starts; for one short worker, visible plan/chat is enough. The coordinator owns shared roster assignment/status/removal; agents update only assigned evidence or note sections. Treat roster rows as current contracts, not history. Put completed recommendations, consent outcomes, objections, decisions, and findings in dated result/decision/evidence sections or agent notes.

## State Artifacts

Use the lowest durable surface that allows resume without replaying chat:

- Short tasks: visible plan/chat.
- Repo work: existing `STATUS.md`, `findings/*.md`, design note, issue/PR text, meeting note, or task handoff.
- Long-running work with no artifact: create one task-local handoff only if future pickup is likely.

Store distilled state only: mission/aim/domain, provisional decisions/review terms, objections/checks, agent findings, evidence paths, commands, acceptance criteria, next steps, and stop rules. Preserve useful scoreboards and handoff facts; use `Steering Gates` for status-churn checks. Do not store full transcripts unless asked.

Create per-agent notes/backlogs only for long-running, restart-sensitive, or independently useful circles; otherwise synthesize into the shared artifact or chat. Agent notes are local working memory; the coordinator owns shared mission state and scoreboard. Suggested path: `findings/<date>-<slug>/agents/<agent-slug>.md`. Suggested fields: mission, domain, aim, authority, status, started, updated; sections: Current State, Backlog, Findings, Evidence, Decisions/Recommendations, Risks/Objections, Next Step/Stop Condition.

## Git Checkpoints

For long-running repo work in a git checkout, use commits as reviewed checkpoints only when the user, run brief, or repo convention authorizes commits. Otherwise, prepare a checkpoint recommendation and ask before committing.

The coordinator reviews the diff, confirms it contains only accepted in-scope changes, runs scoped checks or records why checks were skipped, and commits only accepted checkpoints. Before committing, inspect branch/HEAD/status, stage only explicit owned paths or hunks, review `git diff --cached`, and leave unrelated user or concurrent-agent changes unstaged; stop and ask if hunks are interleaved.

Do not commit transient ticks, unreviewed worker output, unrelated changes, routine status updates, secrets/local config, or failed/abandoned work on the main line. Failed paths belong in durable notes unless committed on an experiment branch or as an accepted cleanup/revert checkpoint.

For simultaneous writing agents, isolate before edits with separate branches, worktrees, or patch artifacts; otherwise pause concurrent writes until the current diff is reviewed. Do not switch branches with dirty user changes without a preservation plan. Do not push unless the user requested or approved it.

Keep commit messages repo-appropriate and terse: include scope, rationale, checks, and useful circle/agent attribution in the body when helpful. Put detailed rosters and status history in durable artifacts. Review this practice after the next long multi-agent repo run, or sooner if checkpoints add churn or capture nonmaterial changes.

## Coordination

- The coordinator speaks to the user, owns synthesis, routes distilled context, and resolves conflicting reports before relying on them.
- Agents report to the coordinator, not each other.
- Keep decisions with the most specific owning circle; wider input is feedback, not a vote.
- Handoffs/plans must include evidence paths, blockers, commands, acceptance criteria, non-goals, and the first PR or vertical slice.
- When using local Codex history, start from `MEMORY.md` and targeted rollout summaries. Avoid broad session-log searches unless exact evidence is needed.
- Coordinator integration includes synthesis, diff inspection, verification, narrow repair, and shared-state updates. If it becomes new implementation ownership in a delegated or contested domain, make that authority shift explicit or spawn/redirect a worker.
- When a nontrivial task lacks a workable path, owner, or acceptance criteria, use multi-agent proposal forming before committing; skip it for straightforward execution or a narrow fix. Default form is coordinator plus one bounded proposal-piece explorer/reviewer, plus active agents whose domains are affected. Add agents only for genuinely independent, contested, high-risk, or affected-domain dimensions; do not simulate consensus.
- Use `Understand -> Explore -> Decide` in discrete rounds. Understand: record context, need, domain, facts/constraints, decision, and dimensions as questions; move on only when there are no open context questions or dimension additions. Explore: gather proposal pieces from those dimensions; pieces may conflict, and the move-on check is only whether more pieces are needed. Decide: synthesize one path with evidence, owner/write set, acceptance checks, next slice, stop/review term, and unresolved objections. Consent-check only the synthesized proposal for concrete aim/domain/evidence/safety/coordination-cost/ownership/acceptance/durability objections; integrate by changing content, scope/sequence, term, measurement/reporting/review, or routing. Coordinator plus affected active circles have process consent rights; others provide feedback unless explicitly seated.

## Steering Gates

When this skill is already in use but work still drifts, treat it as a practice gap: make triggers, thresholds, authority, evidence contracts, or salience more concrete.

For long-running work, use this checklist:

- `steering frame`: keep aim, non-goals, frontier, scoreboard/progress signal, accepted no-go facts, active risks, and next decision current.
- `mission circle`: use at most one. It tracks mission/frontier/risk, may raise binding mission/process objections or request reassessment, and may do bounded trigger/cadence-based log/status/agent-summary review. It must not assign workers, manage implementation, continuously audit transcripts, or become another status loop.
- `worker contract`: before implementation, define target artifact/metric, expected delta or acceptance signal, owned write set, forbidden shortcuts, verification command, stop condition, and what counts as no movement.
- `proposal binding`: carry consented constraints on mode, scope, edit permission, evidence needed, unresolved blockers, and stop condition into the next brief.
- `two-cycle trigger`: after two same-domain stale, no-patch, no-movement, or status-only cycles, stop same-domain implementation spawning and switch to reassessment, diagnostics, taxonomy, deep research, or explicit stop/review.
- `frontier switch`: when work changes from known patch work to missing evidence, an undefined mechanism, or repeated no-go, require diagnostic/taxonomy before more implementation.
- `continuing circles`: redirect while premise, aim, evidence surface, and stop condition stay fresh; retire, quarantine, or distill stale, costly, superseded, or unsafe agents.
- `notes and ticks`: use per-circle notes/backlogs only for long-lived, restart-sensitive, or independently useful circles. Update only for material deltas. Event- or interval-based coordinator ticks exchange only deltas; if two ticks produce no useful delta, retire/redirect or switch modes.
- `status and snapshots`: preserve useful scoreboards. After repeated status updates without metric/frontier movement, write `what changed besides status?` and consider pausing status-only edits. For non-quiescent handoffs or analyses, record snapshot boundary, active agents/commands, excluded continuation, and provisional conclusions.
- `review`: after the next long multi-agent run, ask whether these gates reduced same-domain churn/status-only loops, preserved measurable progress, and avoided excess process.

## Failure Handling

When an agent misses its stop condition or produces suspect work, classify it against its aim before acting: still useful, late, blocked, stale, failed-by-evidence, superseded, unsafe to integrate, or incomplete-but-useful. Wait or redirect only while the output still matters, there is credible progress, and the stop condition remains valid; close/cancel when the aim is obsolete, evidence fails, the worker is stale, or coordination cost exceeds value. Before replacing it, capture status, owned files/diff, failing or missing checks, blocker, and whether output was reviewed.

Treat stale worker output as evidence, not accepted work. The coordinator may retain, repair, quarantine behind a diagnostic/private gate, remove, or record blocker-only within the worker-owned write set; preserve unrelated/user/concurrent changes and ask before broader discard.

After cleanup, verify restoration with scoped evidence: diff review, residue search for route/debug/status leftovers, formatter/build, targeted failed regression, and relevant acceptance/census checks when that was the evidence surface. Update the durable artifact with failure mode, commands, restored checkpoint, abandoned expectations, open candidate, and next stop rule; keep roster rows current.

Re-enter proposal forming when failure invalidates the evidence class, path, owner/write set, acceptance criteria, risk model, or stop condition. If cleanup only restores an accepted checkpoint, keep it coordinator integration. Brief the next agent with verified facts and blockers, not stale intent or blanket no-go conclusions.

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

These books are Creative Commons source material, not public domain. Prefer paraphrase or brief excerpts. For substantial copied/adapted text outside private working notes, include title, authors, SoFA/publisher, license link, and change note; respect attribution and ShareAlike, and verify the exact license before publication. `Many Voices One Song` states CC BY-SA 3.0. `Who Decides Who Decides?` locally states Attribution-ShareAlike Non-commercial 3.0 but links to CC BY-SA 3.0; treat substantial reuse conservatively as NonCommercial + ShareAlike until verified.

- `/Users/saul/Documents/who-decides-who-decides.txt`: Ted J. Rau, aims, domains, consent, objections, feedback, circle formation.
- `/Users/saul/Documents/many-voices-one-song.txt`: Ted J. Rau and Jerry Koch-Gonzalez, circle definitions, linking, feedback loops, governance pitfalls, too-many-circles failure modes.
- `/Users/saul/p/sociocracy-skill/reports/2026-05-11-operational-steering-gates-proposal.md`: consented local proposal behind the operational steering gates.
- `/Users/saul/p/sociocracy-skill/reports/2026-05-11-git-checkpoints-diff-proposal.md`: consented local proposal behind git checkpoints.

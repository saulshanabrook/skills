---
name: primary-source-spec-refactor
description: "Refactor messy technical specs, design notes, implementation plans, or RFC drafts into primary-source-backed, reviewable documentation using topical-alignment analysis, evidence matrices, Diataxis separation, RFC/ADR structure, and implementation-gate checklists. Use when the task is more than copyediting: the document must be checked against code, tests, accepted docs, issue/PR discussion, or other primary evidence. Do not use for ordinary prose polish or code implementation."
---

# Primary-Source Spec Refactor

Use this skill when a working technical document needs to become a reviewable, implementation-gating documentation set. The goal is not prettier prose first; the goal is alignment between what readers/implementers need to know and what primary evidence actually supports.

## Source Priority

Project-local truth outranks methodology:

1. Accepted project RFCs, specs, ADRs, and user decisions.
2. Source code.
3. Tests, snapshots, fixtures, and current command output.
4. Issue, PR, review, or design discussion.
5. Working notes and draft docs.
6. External documentation-method sources bundled with this skill.

External sources govern form and method. Project sources govern technical truth. If a claim cannot be traced to a primary project source, mark it as an open question or assumption.

For the bundled source map, read `references/source-pack.md`. Load raw source files only when needed; do not paste long excerpts from copyrighted or licensed references.

## Core Workflow

1. Define audience and scope.
   - Name the intended readers and the decision or implementation they need to make.
   - State scope, non-scope, prerequisites, and the expected output artifact.
   - If the requested scope is too broad for one reviewable proposal, split it.

2. Extract knowledge units.
   - A knowledge unit is a feature family, mechanism, invariant, lifecycle step, data shape, safety property, integration point, acceptance signal, or reader task.
   - Record anchor terms for each KU from the draft doc, source code, tests, logs, and review notes.

3. Build an evidence matrix before rewriting.
   - For each KU, collect exact evidence: paths, test names, command outputs, accepted decisions, issue/PR comments, and blockers.
   - Prefer current checkout evidence for project facts. Label stale, unverified, or external-method-only claims.

4. Classify coverage.
   - `Convergent`: needed and already well covered by evidence and current docs.
   - `Divergent`: needed but under-specified, inconsistent, or contradicted.
   - `Absent`: expected by readers but missing or barely covered.
   - `Deferred`: intentionally out of current scope, with a clear re-entry condition.
   - `Blocked`: cannot be specified without more primary evidence or a decision.

5. Refactor by document type.
   - `Explanation`: understanding-oriented background and rationale.
   - `RFC/spec`: proposed behavior, normative constraints, compatibility, acceptance criteria.
   - `ADR`: one durable architecture decision with context and consequences.
   - `Implementation brief`: exactly what an implementation agent may do after acceptance.
   - `Open questions`: unresolved product, safety, evidence, or ownership decisions.

6. Preserve traceability.
   - Every normative claim should point to project evidence or an accepted decision.
   - Use `MUST`, `SHOULD`, and `MAY` only for genuinely binding requirements, and only when justified by safety, compatibility, interoperability, or review policy.
   - Unknowns become questions or blockers, not invented requirements.

7. Stop before implementation.
   - Do not modify code unless the user separately asks for implementation.
   - Do not widen feature scope.
   - Do not grant implementation permission unless the relevant spec/RFC decision is accepted.

## Templates

Use these templates as starting points, adapting headings to the project:

- `templates/refactor-plan.md`: first-pass plan for a messy doc.
- `templates/knowledge-unit-map.md`: KU extraction and classification.
- `templates/evidence-matrix.md`: evidence grid before rewriting prose.
- `templates/rfc.md`: reviewable proposal/spec, drawing from Rust RFCs and PEP practice.
- `templates/adr.md`: durable architecture decision record.
- `templates/implementation-brief.md`: handoff for implementation agents after acceptance.

## Output Contract

Return or write:

- A short summary of the audience, scope, non-scope, and source basis.
- The KU map and evidence matrix, unless the user only asked for a narrow edit.
- The refactored artifact set, clearly separating explanation, RFC/spec, ADRs, implementation brief, and open questions.
- A list of blocked or deferred KUs with the exact evidence or decision needed next.
- The checks run, or why checks were skipped.

## Failure Modes

Avoid these common failures:

- Rewriting the document before evidence collection.
- Treating external methodology sources as technical truth for the project.
- Blending explanation, normative spec, implementation permission, and open questions in one overloaded section.
- Using RFC 2119 terms for wishes, future possibilities, or style preferences.
- Deleting compatibility paths or narrowing behavior because the prose looks cleaner.
- Letting polished text hide weak evidence.

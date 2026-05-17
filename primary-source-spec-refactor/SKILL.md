---
name: primary-source-spec-refactor
description: "Refactor messy technical specs, design notes, implementation plans, or RFC drafts into primary-source-backed, reviewable documentation using topical-alignment analysis, evidence matrices, Diataxis separation, RFC/ADR structure, and implementation-gate checklists. Use when the task is more than copyediting: the document must be checked against code, tests, accepted docs, issue/PR discussion, or other primary evidence. Do not use for ordinary prose polish or code implementation."
---

# Primary-Source Spec Refactor

Use this skill when a working technical document needs to become a reviewable, implementation-gating documentation set. The goal is not prettier prose first; the goal is alignment between what readers/implementers need to know and what primary evidence actually supports.

The evidence workflow is scaffolding. The final RFC/spec must still be the artifact the reader needs: a standalone explanation or proposal they can review without reconstructing the design from matrices, statuses, and hole ledgers.

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
   - State the reader outcome: what the reader should understand, decide, or be able to implement after reading the finished artifact.
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

5. Choose the reader-facing artifact shape.
   - `Explanation`: understanding-oriented background and rationale.
   - `RFC/spec`: proposed behavior, normative constraints, compatibility, acceptance criteria.
   - `ADR`: one durable architecture decision with context and consequences.
   - `Implementation brief`: exactly what an implementation agent may do after acceptance.
   - `Open questions`: unresolved product, safety, evidence, or ownership decisions.
   - For RFCs/specs, the main body should read as the intended design, not as the audit log that produced it. Put detailed KU maps, evidence matrices, and hole ledgers in appendices or companion notes unless the user explicitly asks for a ledger as the primary output.

6. Refactor by document type.
   - Preserve positive design content before summarizing status. If the source document has the actual architecture or mechanism, transplant and polish that substance instead of replacing it with a topic map.
   - Separate target design from current implementation snapshot.
   - Separate implementation permission from document completeness. A draft may be reviewable as architecture while still granting no implementation permission.
   - Use inline markers such as `[RESEARCH NEEDED: HOLE-ID]` for unresolved details in otherwise coherent design prose, then define each marker in an appendix with evidence and exit criteria.

7. Preserve traceability.
   - Every normative claim should point to project evidence or an accepted decision.
   - Use `MUST`, `SHOULD`, and `MAY` only for genuinely binding requirements, and only when justified by safety, compatibility, interoperability, or review policy.
   - Unknowns become questions or blockers, not invented requirements.

8. Stop before implementation.
   - Do not modify code unless the user separately asks for implementation.
   - Do not widen feature scope.
   - Do not grant implementation permission unless the relevant spec/RFC decision is accepted.

## RFC And Spec Refactoring Rules

When the output is an RFC/spec, optimize for comprehension before coverage:

- The reader should understand the proposed architecture, data flow, responsibility boundaries, invariants, and acceptance model before they encounter detailed holes or evidence tables.
- The main body should be reviewable without opening the old source document. Cite old docs as evidence, but do not make them required reading for the design.
- Write target architecture as target architecture. Put current implementation, migration scaffolding, and unsupported status in a separate "Current snapshot" or "Migration" section.
- Missing details should be visible but not dominate the document. Prefer inline `[RESEARCH NEEDED: HOLE-ID]` markers plus an appendix over repeated "known facts / missing evidence / research task" blocks in every main-body section.
- Use a global status that matches the requested review. If the user wants architecture review, use `Draft / Architecture Review` or equivalent; keep `Implementation permission: none` separate while holes remain.
- Do not demote a document to a "discovery map" merely because it has unresolved research markers.
- Do not split one coherent architecture into many RFCs until a section is too large to review or independently ready to approve.

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
- The refactored artifact set, clearly separating explanation, RFC/spec, ADRs, implementation brief, and open questions.
- The KU map and evidence matrix as scaffolding, appendix material, or a companion note when useful. Do not let them replace the reader-facing RFC/spec body.
- A list of blocked or deferred KUs with the exact evidence or decision needed next.
- The checks run, or why checks were skipped.

## Failure Modes

Avoid these common failures:

- Rewriting the document before evidence collection.
- Treating external methodology sources as technical truth for the project.
- Confusing coverage with comprehension: listing all knowledge units but failing to explain the mechanism end-to-end.
- Turning an architecture RFC/spec into a status matrix, blocker ledger, or governance note.
- Summarizing away the most important architecture sections from the source document.
- Making the replacement document depend on the old document for basic understanding.
- Mixing target design with current implementation status in the same section.
- Blending explanation, normative spec, implementation permission, and open questions in one overloaded section.
- Using RFC 2119 terms for wishes, future possibilities, or style preferences.
- Deleting compatibility paths or narrowing behavior because the prose looks cleaner.
- Letting polished text hide weak evidence.

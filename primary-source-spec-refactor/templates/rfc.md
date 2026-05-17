# RFC: <Title>

**Status**: Draft / Architecture Review / Proposed / Accepted / Rejected / Superseded

**Implementation permission**: None until this RFC is accepted and any first-gate `[RESEARCH NEEDED]` markers are resolved or explicitly deferred.

**Owner**:

**Reviewers**:

**Last updated**:

**Review question**: What should reviewers be able to approve, reject, or ask to change after reading this RFC?

## Summary

One short paragraph stating what changes and why. The summary should describe the intended design, not the current status ledger.

## Audience And Prerequisites

Who should read this, and what must they already know?

## Reviewer Path

Read this RFC in this order:

1. Architecture or design in one pass.
2. Invariants and responsibility boundaries.
3. Data model and interfaces.
4. Feature behavior or detailed specification.
5. Current implementation or migration snapshot.
6. Research markers and evidence appendices.

After reading, reviewers should be able to answer:

-

## Scope

This RFC covers:

-

## Non-Scope

This RFC does not cover:

-

## Motivation

What problem, reader need, implementation blocker, or safety concern requires this change?

## Architecture Or Design In One Pass

Explain the proposal end-to-end in terms an implementer or reviewer can understand before reading details. This section should stand alone without requiring the old source document.

If a detail is missing, write the best evidence-backed target design and mark the gap inline:

```text
[RESEARCH NEEDED: HOLE-EXAMPLE-001]
```

Then define the marker in Appendix A.

## Invariants

Binding rules that apply across the proposal:

-

## Responsibility Boundaries

Who owns each part of the design?

### Producer Or Authoring Layer

-

### Runtime Or Execution Layer

-

### Interpreter, Monitor, Or Consumer Layer

-

### Validator, Checker, Or Acceptance Layer

-

## End-To-End Flows

Walk through the important success paths before listing detailed holes.

### Flow 1: <Name>

1.

### Flow 2: <Name>

1.

## Reference Specification

State the binding behavior. Use `MUST`, `SHOULD`, and `MAY` sparingly and only for requirements justified by safety, compatibility, interoperability, or review policy.

## Data Structures And Interfaces

List new or changed data shapes, APIs, schemas, events, files, or contracts.

## Feature Or Case Matrix

Use a compact matrix only after the architecture is understandable. Each row should summarize behavior and point to detailed research markers, not replace the design narrative.

| Feature or case | Required context | Runtime/input evidence | Owner responsibility | Validation or acceptance | Open marker |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Acceptance Criteria

-

## Current Implementation Or Migration Snapshot

Separate current state from target design. This section records why migration work is needed; it does not define the architecture unless explicitly stated.

-

## Compatibility And Migration

What existing behavior, data, or compatibility path must be preserved?

## Rationale

Why this design rather than the obvious alternatives?

## Alternatives Considered

-

## Drawbacks And Risks

-

## Evidence

Primary project evidence:

-

External method sources:

-

## Unresolved Questions

Use this for short unresolved questions. Put detailed research records in Appendix A.

-

## Appendix A: Research Markers

Use detailed markers for missing evidence or design. Do not repeat this shape in every main-body section unless the user explicitly wants a ledger-first document.

### HOLE-EXAMPLE-001: <Short Name>

**Type**: Evidence / design / checker / canary / scope / owner needed.

**Blocks**:

**Question**:

**Evidence basis**:

-

**Exit criteria**:

-

## Appendix B: Evidence Matrix

Keep detailed KU/evidence/status matrices here or in a companion note so the main RFC remains readable.

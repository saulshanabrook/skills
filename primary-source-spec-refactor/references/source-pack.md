# Source Pack

This file maps the skill's practices to bundled primary sources. Use it to decide which source to load, and cite project-local evidence separately for project facts.

## Topical Alignment

**Source files**:

- `references/sources/cogo-xia-hassan-3546945.pdf`
- `references/sources/cogo-xia-hassan-3546945.txt`

**Original source**: Filipe Roseiro Cogo, Xin Xia, Ahmed E. Hassan, "Assessing the Alignment between the Information Needs of Developers and the Documentation of Programming Languages: A Case Study on Rust", ACM TOSEM 2023, DOI `10.1145/3546945`.

**Use for**:

- Deriving knowledge units from developer needs and documentation topics.
- Comparing high-need topics against current doc coverage.
- Treating under-covered, missing, or mismatched topics as prioritization signals.
- Triangulating suspected gaps against multiple evidence sources before refactoring.

**Useful search terms**: `topical alignment`, `concrete information needs`, `knowledge unit`, `anchor`, `Q&A`, `documentation`, `implications`.

## Diataxis

**Source files**:

- `references/sources/diataxis-documentation-framework/`
- `references/sources/diataxis-explanation.html`
- `references/sources/diataxis-explanation.txt`

**Original source**: https://diataxis.fr/ and https://github.com/evildmp/diataxis-documentation-framework

**Use for**:

- Separating tutorial, how-to, reference, and explanation needs.
- Preventing one overloaded document from mixing conceptual background, task steps, machinery reference, and learning paths.
- Keeping explanation understanding-oriented rather than binding implementation permission.

**Useful files/search terms**: `explanation.rst`, `reference.rst`, `how-to-guides.rst`, `tutorials.rst`, `understanding-oriented`, `information needs`.

## Reviewable RFCs And Proposals

**Source files**:

- `references/sources/rust-rfc-0000-template.md`
- `references/sources/pep-0001.html`
- `references/sources/pep-0001.txt`

**Original sources**:

- https://github.com/rust-lang/rfcs/blob/master/0000-template.md
- https://peps.python.org/pep-0001/

**Use for**:

- Splitting large proposals.
- Adding status, ownership, motivation, guide-level explanation, reference-level specification, rationale, alternatives, drawbacks, and unresolved questions.
- Making design review possible before implementation.

**Useful search terms**: `Summary`, `Motivation`, `Guide-level explanation`, `Reference-level explanation`, `Drawbacks`, `Rationale`, `Unresolved questions`, `Status`, `Sponsor`.

## Normative Language

**Source file**: `references/sources/rfc2119.txt`

**Original source**: https://www.rfc-editor.org/rfc/rfc2119.txt

**Use for**:

- Deciding when `MUST`, `SHOULD`, and `MAY` are appropriate.
- Keeping binding terms scarce and justified.

**Useful search terms**: `MUST`, `SHOULD`, `MAY`, `Imperatives`.

## Technical Writing Structure

**Source files**:

- `references/sources/google-tech-writing-one.html`
- `references/sources/google-tech-writing-one.txt`
- `references/sources/google-tech-writing-audience.html`
- `references/sources/google-tech-writing-audience.txt`
- `references/sources/google-tech-writing-documents.html`
- `references/sources/google-tech-writing-documents.txt`

**Original source**: https://developers.google.com/tech-writing/

**Use for**:

- Defining audience, reader goals, prerequisites, scope, non-scope, and key-point summaries early.
- Organizing documents around what readers need to know or do.
- Comparing new proposals to known concepts when useful.

**Useful search terms**: `scope`, `non-scope`, `audience`, `prerequisite`, `Summarize key points`.

## Design Documents Before Code

**Source files**:

- `references/sources/software-engineering-at-google-docs-ch10.html`
- `references/sources/software-engineering-at-google-docs-ch10.txt`

**Original source**: https://abseil.io/resources/swe-book/html/ch10.html

**Use for**:

- Treating substantial design docs as review-before-code artifacts.
- Distinguishing design docs, reference docs, tutorials, and landing material.
- Setting expectations that documents are maintained artifacts, not one-off prose.

**Useful search terms**: `design doc`, `write`, `review`, `audience`, `documentation`.

## Architecture Decisions

**Source files**:

- `references/sources/nygard-documenting-architecture-decisions.html`
- `references/sources/nygard-documenting-architecture-decisions.txt`
- `references/sources/nygard-adr-template.md`
- `references/sources/architecture-decision-record-practice.md`

**Original sources**:

- https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- https://github.com/joelparkerhenderson/architecture-decision-record

**Use for**:

- Extracting durable decisions into short records.
- Capturing status, context, decision, and consequences.
- Keeping decision records focused on one architecture choice rather than broad implementation plans.

**Useful search terms**: `Status`, `Context`, `Decision`, `Consequences`, `architecture decision record`.

## Copyright And License Hygiene

The bundled references are for local skill use. Paraphrase methodology rather than copying long passages. Before publishing substantial adapted content outside private work, verify each source's license and attribution requirements.

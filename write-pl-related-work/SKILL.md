---
name: write-pl-related-work
description: Research, plan, draft, and revise related-work sections for programming-languages and computer-science papers, with source-grounded comparisons and reusable learning from follow-up feedback. Use for positioning a manuscript's contributions and design choices, not generic prose editing or unrelated literature surveys.
---

# PL Related Work

Help the reader understand where the paper's contribution comes from, which alternatives address the same question, and what the paper establishes. Start planning from the manuscript's contribution, design choice, result, or guarantee; select literature that clarifies it.

## Establish the assignment

Read the current assigned passage, abstract/introduction, relevant technical claims, bibliography, and supplied evidence as needed. Identify what the reader must understand to assess the contribution. Preserve the user's scope, coauthor ownership, manual edits, and deliberate deletions. A request to brainstorm, review, or research does not authorize manuscript edits.

Scale the work to the request. A narrow repair may need only the current sentence and its source; a new area may need an outline and focused research. Clarify a consequential missing decision while continuing independent work that is already clear.

## Establish the relationships

Consult manuscript sources, bibliography, and provided PDFs before expanding the search. Read the relevant primary-source text beyond abstracts and search snippets, including complete pages, qualifications, and referenced figures or tables that bear on the claim. Check citation metadata and the version actually read.

Keep research notes rich enough to support each material comparison: the mechanism, relationship to this manuscript, exact evidence location/version, relevant limit, and proposed claim. Paper-by-paper notes are useful working material. Mark whether a connection is explicit in the source or an analogy drawn for this paper. Missing sources or proofs must be named, never filled in by inference.

Compare the property that matters:

- An implemented mechanism, proposed direction, prototype, and proved result are different evidence.
- Type preservation, semantic preservation, proof production, certificate checking, and mechanization of a component or the whole stack are different guarantees.
- A software package's integration boundary need not be the boundary of its source transformation or evaluator changes.
- Performance comparisons require the timed operations, baselines, workloads/cohorts, and aggregation; distinguish runtime ratios from added percentages.

Use optional library/map tools or bounded delegation when they help answer a specific gap; see [integrations.md](references/integrations.md). They are not prerequisites. Stop expanding when the selected claims and important alternatives are adequately supported.

## Compose and review

Organize final prose around actual relationships: foundations, inherited mechanisms, nearest alternatives, changed objectives, complementary techniques, or a meaningful lineage. Explain enough of a shared mechanism for the distinction to be intelligible. Credit inheritance and other systems' advantages; a difference need not imply superiority.

Choose hierarchy, placement, headings, and length from reader prerequisites and venue constraints. Background may be integrated with related work; a close predecessor may deserve its own paragraph. Do not impose citation quotas, a fixed area/paragraph count, equal space, or a rule that every paragraph start or end with the present work. Some paragraphs supply context, credit, limits, or future connections. The [source corpus](references/sources.md) illustrates these alternatives; its observations are not universal PL norms.

Draft only the authorized material in the requested LaTeX/BibTeX or venue format. Keep source notes and plugin research formats separate from manuscript presentation. Review the current revision, checking that compression preserved the mechanism and guarantee, citations support their attached claims, and historical priority/capability claims remain justified. Recheck changed claims after feedback; stop when material issues are resolved rather than restarting an exhaustive survey. Apply repository validation appropriate to the actual edit.

## Learn from follow-up feedback

Treat a follow-up tweak as immediate manuscript feedback and a possible skill lesson. Repair a clear paper issue first. Then distinguish missing guidance, failure to apply an existing rule, and new paper-specific context or a user preference.

For Saul's use of this personal skill, standing authorization covers saving clear, reusable, scoped lessons from follow-up output feedback to this skill's canonical source and publishing those skill changes under its repository rules. Do not request that authorization again. Explicit paper-only, private, read-only, or draft-only instructions override it; it does not broaden manuscript-editing scope or authorize manuscript/service publication, other-skill edits, or tool-policy changes.

Make the smallest durable update, preferring an existing-rule clarification over a duplicate or blanket ban. Check the feedback case and a contrasting case where the rule should not apply. If the general principle is materially unclear, ask a concise question while continuing clear local repairs; keep the provisional lesson out of global instructions.

Read [feedback.md](references/feedback.md) for classification examples and scoped publication. Do not edit an installed cache/copy or memory as a substitute for updating the canonical skill. Keep unpublished paper details out of public instructions. Briefly report a meaningful generalized change; do not promise future learning without saving it or create an endless self-review loop.

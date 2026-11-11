---
name: write-research-paper
description: Plan, draft, and revise research manuscripts around reader questions, supported claims, and useful evidence. Use for paper structure, evaluation narratives, technical exposition, and incorporating author feedback; not generic document formatting or standalone literature discovery.
---

# Write or revise a research paper

Help readers understand the contribution, assess its evidence, and see why it matters. Enter at the assigned task: a sentence repair need not become a whole-paper audit, and an outline request does not authorize manuscript edits.

## Recover the argument and preserve the work

Read the assigned passage and enough surrounding claims, results, and author feedback to identify its job. For substantial restructuring, inspect the relevant baseline, reviewed checkpoint, and current edits when available. Preserve user and coauthor intent, deliberate deletions, examples, citations, and technical substance. Move useful passages intact before rewriting them; do not replace considered work merely for stylistic uniformity. Mention significant retained or relocated material briefly when handing over a structural revision.

If a section's structure is unsettled, establish its argument and worked examples before polishing full prose. This is a useful entry point, not an outline-approval gate for an already authorized draft or narrow repair. When using review history, distinguish the criticism, reply, resulting revision, and present author preference. An old unresolved thread is not automatically a current defect, and an approval does not endorse every inferred rationale.

When useful, make a small working map:

| Reader's question | Claim being assessed | Evidence | Interpretation |
| --- | --- | --- | --- |
| What should the reader learn here? | What does the paper assert? | What observation, argument, or example supports it? | What does that evidence establish? |

Use this to find gaps, not as a mandatory table in the paper. Research questions should reflect the introduction's claims without forcing a one-to-one correspondence. A workload set can establish capability in one section and measure its cost in another; explain each section's distinct purpose rather than duplicating its protocol.

## Put the reader's point before machinery

Lead empirical results with the supported finding and its significance, then the evidence and method. A capability section says what worked; a performance section says what it cost. Orient the reader to the question as needed, but do not replace the answer with repeated “We test whether” openers. When results are pending, put a focused TODO for the missing finding up front rather than inventing a conclusion or filling the gap with methods prose. In technical exposition, explain the problem, output, and key idea before machinery whose purpose would otherwise be unclear; definitions and proofs may need prerequisites first.

Use the [primary writing guidance and paper examples](references/writing-sources.md) to settle a particular organization or detail decision. They support reader-oriented argument, not a compulsory opening formula; the guides differ on some prescriptions.

Select main-text detail by its role in assessing the claim. Explain a mechanism when it makes the contribution understandable, a condition when it changes the comparison, and a metric when it changes the result's meaning. Move command sequences, counters, instrumentation inventories, and reproducibility minutiae to methods, an appendix, or the artifact as appropriate. Compression should retain the technical reason the result is credible.

Teach a mechanism through the simplest sufficient concrete example. Explain the input and output beside the code, distinguish the obstacle from its solution, and introduce generic notation after its benefit is visible. Name the actual language stage and the component performing each operation. For translations, make source-to-output correspondence inspectable and preserve useful figure explanations; [the examples reference](references/revision-examples.md#make-the-mechanism-visible-before-generalizing) illustrates the tradeoff.

For adopting a capability in existing programs, lead with what users can now do, what programs were tested, and how preserved behavior or successful outputs were checked. Describe the instrumentation only as far as needed to understand that evidence. Capability and compatibility evidence belong beside performance evidence; timing alone cannot establish that existing programs still work.

For an application case study with results, lead with what the combined capabilities achieved on an existing problem and the practical benefit. Then explain the problem's origin and why the combination matters. Introduce dataset and feature inventories afterward when relevant. Distinguish a successful combined example from evidence that every component is necessary; necessity or performance attribution needs a supporting comparison or argument.

## Make strong claims at the supported scope

State supported findings directly and affirmatively. Remove unprompted lists of things the experiment does not do, defensive checklists, and repeated scope disclaimers that do not affect the reader's conclusion. Integrate a material boundary close to the claim instead of repeatedly weakening it.

Keep failures, contradictory evidence, important limits, and fairness conditions visible. A checked result, a universal guarantee, and a successful finite corpus are different claims. Be precise without surrounding every ordinary statement with hypothetical exceptions. See [revision examples](references/revision-examples.md) when deciding whether to remove detail or preserve a caveat.

Check broad novelty or absence claims against the closest plausible counterexamples. Scope the claim to the supported mechanism, combination, or version instead of turning a difference into universal priority. Use the related-work specialist when available for a substantive literature comparison.

Separate intended method, completed measurement, and established result. Never convert planned runs or a prototype into a reported finding. Submission-facing prose describes the actual method and results; it does not narrate pilot scheduling, review history, removed cutoffs, or changes from older drafts. Keep collection plans and unresolved operational work in project notes.

## Explain the experimental choices that matter

Connect each benchmark, corpus, and baseline to the question it answers. Explain why a particular reference is appropriate, including relevant capability differences or evidence that it is the strongest applicable comparison. Verify such claims from the original source or current artifact rather than assuming a label like “fastest.” Record corpus provenance and adaptations where they help assess representativeness and reproducibility.

Preserve conditions that materially affect interpretation: workload or schedule equality, resource allocation, enabled features, timing boundaries, and validation criteria. Put them near the affected comparison or in an accessible methods passage. A footnote can carry a concise condition; an appendix cannot repair a misleading headline claim.

Choose a metric and visualization only after stating its purpose. Static program growth, runtime, and memory answer different questions. Per-pass arrows require actual consecutive intermediate programs from the same pipeline; separate configurations alone do not establish a transformation trajectory. When borrowing an admired paper's presentation, identify the rhetorical job and evidence it serves; do not mechanically copy its aggregation, cutoffs, or chart type, or infer why reviewers liked it.

## Route specialized work without duplicating it

For PL/CS contribution positioning and source-grounded comparisons, use the [write-pl-related-work specialist](../write-pl-related-work/SKILL.md) when installed. Keep its literature research and comparison guidance there. This broader skill handles the paper's argument, placement, exposition, and revision; ordinary edits do not require the specialist or a new literature search.

## Learn from feedback at the right scope

Repair the assigned paper issue first. Then distinguish missing reusable guidance, failure to apply existing guidance, a manuscript-specific fact, and a personal preference. Keep per-paper facts and protocols in that project's notes. Save only a clear transferable condition or useful example, preferably by clarifying an existing instruction rather than accumulating prohibitions.

For Saul's personal skill collection, standing authorization covers saving clear, scoped lessons from follow-up writing feedback in this skill's canonical source and publishing those skill changes under its repository's rules. Explicit paper-only, private, read-only, or draft-only limits override that authorization. It does not authorize broader manuscript edits, manuscript publication, external messages, or changes to unrelated skills. A related-work-specific lesson belongs in the specialist when that update is in scope.

Check a proposed lesson against both the feedback case and a plausible contrasting case, especially when the feedback rejects detail, caveats, headings, or a comparison. Validate the changed skill and inspect the task-owned diff. Follow the canonical repository's scoped publishing instructions, preserve unrelated work, and hand over to an agent already owning publication rather than racing its Git operations. Report the meaningful saved lesson briefly; do not create a changelog or a mandatory skill update for every correction.

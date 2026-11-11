# Revision decisions and contrasting cases

Read this when feedback asks for stronger prose, less implementation detail, or a different evaluation structure. These are constructed examples of decisions, not reported results or quotations from an unpublished manuscript.

## Lead with the capability being tested

**Before:** “For each replay, the pipeline instruments every check and extraction request, materializes certificates, simplifies them, and invokes the verifier in a separate run.”

**After, if established:** “Proof-enabled execution preserves the checks and source-equivalent extracted results of the tested application programs, with all resulting certificates passing validation.” Then describe the collected programs and the relevant validation method.

Retain the mechanism in methods if needed to explain what is proved and what is timed. Do not claim preserved results merely because the program executed or two graph sizes matched. Use the actual correspondence evidence. If only adapted inputs were tested, name the evaluated inputs or adaptations where they affect the adoption claim.

## Give the finding before describing its chart

**Before:** “Each point has the reference's mean runtime on the horizontal axis and our mean runtime on the vertical axis.”

**After, if measurements support it:** “Translation overhead is concentrated in short-running workloads.” Then explain the comparison, chart, and evidence for that finding.

**While results are pending:** Begin with “TODO: summarize the runtime comparison once measured.” Keep the necessary method below it. Replacing the chart description with “We test whether our approach is fast” still withholds the answer when results exist and adds filler when they do not.

A separate comparison can ask what proof production costs for existing programs. The same programs may provide behavioral evidence earlier and timing evidence here; that does not require another research question or repeated collection details.

## Remove a nonclaim; keep an indispensable boundary

**Remove when irrelevant:** “This example does not use the optional conflict-detection extension.” It distracts from the capabilities the example demonstrates.

**Keep when material:** “Both systems run the same fixed schedule with adaptive backoff disabled.” Removing this could mislead readers about why performance differs. Likewise, retain a failure on a supported input or a restriction needed to interpret a claimed guarantee.

The decision is whether the qualification changes the reader's conclusion, not whether it contains a negative word.

## Explain the baseline choice

**Before:** “We compare with variants A and B.”

**After, if verified:** “We compare with A, the strongest reported implementation for ordinary execution, and B, the strongest applicable variant supporting proof production.”

If the proof-capable reference requires an adapted driver, disclose that adaptation and its relevant effect. Do not label a reference proof-capable or fastest without supporting evidence.

## Lead a composition example with the useful outcome

**Before:** “The workload has hundreds of queries over several tables. The implementation uses pattern matching, analyses, and proofs.”

**After, if established:** “The combined extensions produce a checked plan that shares intermediate results across analytical queries, reducing repeated query-execution work.” Then identify the existing optimization problem and explain why the combined capabilities enable this result.

Explain why the relevant capabilities help and report the observed benefit. An ablation may support a stronger claim that a particular combination is necessary. Keep dataset scale where it helps interpret the measurement, without making it the opening argument.

## Describe the paper, not its production history

**Before:** “The initial pilot requests three observations per configuration. We now include the full inventory, with no lower runtime cutoff.”

**After:** State the method actually used and any selection criterion needed to interpret it. If measurements remain pending, leave a concise working-draft TODO at the affected value or result; keep the run plan in project notes.

Do not remove a selection criterion whose omission would bias the apparent coverage. Do not turn a requested observation count into a completed measurement claim.

## Make the mechanism visible before generalizing

**Before:** A generic rule template introduces parameters used only in later sections, followed by unlabeled source and generated programs.

**Repair:** Show a small concrete input and explain its intended output. Identify the obstacle and then show the generated code that addresses it, with labels or visual correspondence between source constructs and generated lines. Preserve useful comments from an earlier figure. Explicitly abbreviate unchanged code when full duplication would obscure the transformation.

Keep a shared definition or generic template when it already reduces repetition or enables the argument. The lesson is to make its benefit visible, not to inline every abstraction or require every overview to demonstrate every feature. Attribute a lowering operation to the pass that performs it; the program using a combined capability demonstrates the implementation rather than performing the composition itself.

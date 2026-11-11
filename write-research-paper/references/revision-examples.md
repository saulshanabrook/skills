# Revision decisions and contrasting cases

Read this when feedback asks for stronger prose, less implementation detail, or a different evaluation structure. These are constructed examples of decisions, not reported results or quotations from an unpublished manuscript.

## Lead with the capability being tested

**Before:** “For each replay, the pipeline instruments every check and extraction request, materializes certificates, simplifies them, and invokes the verifier in a separate run.”

**After, if established:** “Proof-enabled execution preserves the checks and source-equivalent extracted results of the tested application programs, with all resulting certificates passing validation.” Then describe the collected programs and the relevant validation method.

Retain the mechanism in methods if needed to explain what is proved and what is timed. Do not claim preserved results merely because the program executed or two graph sizes matched. Use the actual correspondence evidence. If only adapted inputs were tested, name the evaluated inputs or adaptations where they affect the adoption claim.

## Give the finding before describing its chart

**Before:** “Each point has the reference's mean runtime on the horizontal axis and our mean runtime on the vertical axis.”

**After, if measurements support it:** “Translation overhead is concentrated in short-running workloads.” Then explain the comparison, chart, and evidence for that finding.

**While the intended argument is under review and results are pending:** Draft the proposed answer itself, for example: “[Provisional answer; measurements pending.] Translation overhead is concentrated in short-running workloads, while longer workloads run within TODO× of the reference.” This is an explicitly unverified hypothesis, not a reported result. Revise or replace both the claim and the missing values after measurement; do not merely fill numbers into a conclusion contradicted by the data.

If no answer is proposed yet, a focused result TODO is enough. Replacing the chart description with “We test whether our approach is fast” still withholds the answer when results exist and adds filler when the author wants to review an intended argument.

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

## Put validation outcomes with the existing inventory

**Before:** A table already identifies the workload groups, but a separate main table mainly reports execution and checking counts as completed/total.

**Repair, when the same validation applies and exceptions are few:** Add a validation outcome to the existing inventory. Define it in terms of the evidence relevant to the claim: for example, the prescribed assertions and extracted results agree with the reference, and proof certificates validate where applicable. Note the few timeout or memory exclusions concisely beside the affected entries or in a footnote. Keep detailed per-input counts, run status, and diagnostics in the artifact.

Successful execution alone does not warrant a validation mark. Use a pending marker until the stated checks actually pass, and do not let a tested subset appear to cover excluded inputs. If differing coverage or a substantial pattern of failures is itself part of the scientific answer, retain enough explicit outcomes or counts to show it; consolidation is not a requirement to use checkmarks or conceal failures.

## Make the mechanism visible before generalizing

**Before:** A generic rule template introduces parameters used only in later sections, followed by unlabeled source and generated programs.

**Repair:** Show a small concrete input and explain its intended output. Identify the obstacle and then show the generated code that addresses it, with labels or visual correspondence between source constructs and generated lines. Preserve useful comments from an earlier figure. Explicitly abbreviate unchanged code when full duplication would obscure the transformation.

Keep a shared definition or generic template when it already reduces repetition or enables the argument. The lesson is to make its benefit visible, not to inline every abstraction or require every overview to demonstrate every feature. Attribute a lowering operation to the pass that performs it; the program using a combined capability demonstrates the implementation rather than performing the composition itself.

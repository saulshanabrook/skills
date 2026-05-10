---
name: scientific-method-debugging
description: Run an evidence-first scientific debugging loop for debugging, performance analysis, semantic drift, or codebase comparisons. Use when a user wants claims backed by actual runs, when multiple plausible causes exist, when a bug needs to be shrunk to the smallest repro, or when fixes should be accepted only if they flip the target case without regressing a known comparison set.
---

# Scientific Method Debugging

Treat debugging as an iterative experiment, not as a one-shot diagnosis. Make one concrete claim at a time, measure it, and only keep fixes that flip the target case and preserve a known regression set.

## Question and Observation

Start by characterizing the phenomenon before inventing explanations.

- State the exact question being answered.
- Record the initial observation in concrete terms: input, environment, expected behavior, observed behavior, and why the difference matters.
- Prefer skeptical description over interpretation at this stage. “The run times out after 8s on case X” is better than “the scheduler is broken”.
- If the observed behavior is unstable, first determine whether the instability is real or a measurement artifact.

## Alternative Hypotheses

When the cause is not obvious, write down at least two plausible explanations before changing code.

- Prefer hypotheses that make different predictions.
- Use alternative hypotheses to defend against confirmation bias.
- Drop weak hypotheses quickly, but only after a probe actually contradicts them.
- When the cause could live at different layers, include at least one hypothesis from each layer:
  - high-level control-flow or configuration mismatch
  - implementation mismatch
  - engine or state-evolution mismatch
  - output-selection or presentation-only mismatch

## Core Loop

Follow this exact loop:

1. State the current hypothesis.
2. State at least one confirming prediction and one disconfirming prediction.
3. Shrink the problem to the smallest repro that still shows the behavior.
4. Add or refine a test before changing code.
5. Run the smallest bounded experiment that can falsify the hypothesis.
6. Implement the smallest fix.
7. Re-run the target repro and the regression set.
8. Keep the fix only if the target flips and the regression set stays green.
9. If the fix fails or regresses, revert it, record the failed hypothesis, and choose a narrower next hypothesis.

Do not keep speculative fixes in the tree.

The best probe is one whose outcome differs across competing hypotheses, not one that merely restates the known failure.

## Root-Cause Convergence

When the user wants the actual root cause rather than a catalog of differences, tighten the loop:

1. Make the relevant runs as comparable as possible before tuning:
   - same inputs
   - same relevant configuration
   - same stopping condition or resource budget
   - same checkpoints or observability boundaries
2. Find the first meaningful divergence, not the biggest late divergence.
3. Ignore presentation-only differences unless the user explicitly cares about them.
   - nondeterministic tie breaks
   - output ordering
   - formatting or pretty-printing
4. Once the first meaningful divergence is found, stop aggregating and inspect one exact example that witnesses it.
5. Ask which mechanism could have created that exact example.
6. Design the next probe to distinguish:
   - different opportunities already present in the state
   - different eligibility or guard behavior
   - different suppression, prioritization, or budgeting
   - different maintenance, merge, or normalization behavior
7. Keep pushing until you can name the concrete mechanism, not just the symptom.

Prefer “variant A suppresses broad candidates later, so family X remains active through step N” over “system A blows up more.”

## Boundary Discipline

When a process evolves over time, observe it at stable boundaries instead of only at the end.

- Choose checkpoints such as:
  - before the relevant step
  - after the relevant step
  - after maintenance, rebuild, or normalization
  - after output selection only if output selection matters
- If a run is slower or larger, do not assume implementation inefficiency first.
- First ask whether the relevant internal state is actually larger at the same checkpoint.
- If the state is larger, split the cause:
  - more auxiliary bookkeeping state
  - more primary domain state
  - more duplicate presentations of the same underlying opportunity
- Prefer one bounded stepwise trace over many full end-to-end runs when chasing divergence.

## Counts vs Examples

Counts are for localization, not proof.

- Use counts to find the first step or family that diverges.
- Then switch to exact witnesses:
  - one matched candidate
  - one state member or record
  - one parent or predecessor object
  - one triggering tuple, event, or transition
- If a count gap survives normalization, inspect concrete examples from that gap before claiming a cause.
- When possible, follow one exact witness across consecutive iterations and ask:
  - when did it first appear?
  - what predecessor or transformation created it?
  - why is it present in one system but not the other?

Do not stop at “family X happens more.” Keep going until you can explain why more opportunities exist.

## Falsifiability and Honesty

- Prefer direct program runs over reasoning from source alone when behavior is in question.
- Prefer hypotheses that risk being wrong over ones that explain every possible outcome.
- Keep one source of truth for each claim: test output, profiler output, run report, diff, or serialized state.
- Distinguish semantic differences from extraction or presentation differences.
- Distinguish “this operation exists” from “this process reaches the same state”.
- Distinguish “this action happened more” from “this action was offered more eligible opportunities”.
- When a claim depends on runtime behavior, quote the measured result in plain language with the exact case and variant used.
- Do not rescue a favored hypothesis after a failed probe unless the hypothesis is explicitly narrowed and the failed result is recorded.
- Temporary code changes used only to test a hypothesis should be reverted immediately after the measurement unless the user asked to keep them.

## Repro Discipline

- Start from the smallest known failing case.
- If the case is still large, reduce it by deleting or replacing subexpressions while preserving the failure.
- Keep stable fixture-backed canaries for:
  - the target failure
  - at least one nearby passing case
  - at least one regression canary that previously broke under an attempted fix
- Promote a case out of an expected-mismatch bucket only after the real baseline path matches the source of truth.
- If many cases differ, choose one meaningful case with a true semantic mismatch at the end state and work that one to ground first.
- If a case turns out to be presentation-only or otherwise insignificant, explicitly retire it and move to the next meaningful case.

## Test-Before-Fix

- Add a focused test before the code change whenever the behavior is fast enough to test locally.
- If the mismatch is not fixed yet, keep the test as an expected mismatch or targeted regression.
- Use the narrowest test that proves the claim. Do not hide a small mismatch inside a broad end-to-end test if a smaller case exists.
- For comparison work, prefer checked-in golden cases over invoking an external toolchain during normal tests.

## Fix Selection

- Change one variable at a time.
- Prefer the smallest code change that can falsify the current hypothesis.
- When testing schedule or search-space hypotheses, compare a target canary and a regression canary before keeping the change.
- When a user wants to match a known target behavior, first match the target’s controllable behavior before trying “better” heuristics.
- Do not tune for a better result until you have first tested the most literal implementable version of the target behavior.
- If two candidate fixes both work, prefer the one that removes less behavior and preserves more of the original algorithm.
- Treat parsimony as a heuristic tie-break, not as proof that the simpler explanation is correct.

## Ledger and Reproducibility

Maintain a short living record in the nearest review or conclusions file. For each active mismatch family, keep:

- `Status`
- `Smallest repro`
- `Exact commands or probes`
- `Inputs and environment`
- `Observed source-of-truth behavior`
- `Observed local behavior`
- `Current hypothesis`
- `Last attempted fix`
- `Observed result`
- `Next probe`

Update the ledger after each accepted or rejected experiment. The ledger should explain why the next step exists and should let another agent rerun the same probe without re-deciding setup details.

## Process Hygiene

- Run long probes in subprocesses with explicit timeouts.
- Use smaller timeouts for reduced cases and larger ones only for full canaries.
- After each timeout, inspect CPU, memory, and lingering worker processes.
- Kill stale workers immediately before starting the next experiment.
- Do not leave background probes running while interpreting results from a different run.
- If memory starts to explode, stop the broad probe and switch to a more targeted or bounded one before continuing.
- After any manual kill of a large probe, verify both worker processes and memory returned to a safe baseline before the next run.

## Iteration

Treat the loop as non-linear.

- A failed experiment may require redefining the question, shrinking the repro further, replacing the hypothesis, or designing a better probe before any code change.
- If repeated probes keep contradicting the current model, update the model instead of forcing the next experiment to fit it.

## Good Defaults

- Use a fast reduced case to understand the mechanism.
- Use a slower real canary to decide whether the fix generalizes.
- Keep shape-only extraction mismatches separate from semantic mismatches unless state inspection proves they are connected.
- If repeated local fixes fail on reduced cases and the evidence keeps pointing at engine behavior, say so explicitly and stop pretending the issue is still local.
- For hard debugging, default to this order:
  1. align controllable conditions and observability
  2. first meaningful divergence by checkpoint
  3. exact witness example
  4. mechanism-level cause
  5. only then a candidate fix

---
name: review-diff-reduction
description: Reduce an existing code diff to make it easier to review without changing accepted behavior. Use when a feature or fix is already implemented and the next task is to restore unchanged comments, variable names, formatting, or control flow so the remaining diff is smaller, more additive, and easier for a reviewer to scan.
---

# Review Diff Reduction

Use this skill after the behavior is already acceptable and the goal is reviewability, not redesign.

Good triggers:

- "Can you make this diff easier to review?"
- "Reduce the churn in this file."
- "Keep the behavior but restore the old structure where possible."
- "Prioritize shrinking changed and deleted lines over added lines."

## Core Rule

Preserve accepted behavior. Shrink review surface.

- Do not bundle new fixes unless they are required to keep the code correct.
- Prefer reverting wording, variable names, formatting, and control-flow shape before attempting deeper refactors.
- Prefer additive lines over changed or deleted lines when both are equally correct.
- If a cleanup would hide the real semantic change, do not take it.

## Workflow

1. Compare the current file to the base version directly.
2. Identify which diff hunks are semantic and which are review noise.
3. Restore unchanged material first:
   - comments that were removed but are still correct
   - variable names that changed without need
   - block structure or formatting that was altered only incidentally
   - existing helper/test structure that can stay intact
4. Keep the old path visually recognizable and layer new behavior on top with the fewest changed lines.
5. Re-run the narrowest relevant tests.
6. Re-check the diff and repeat until the remaining changes are mostly irreducible.

## What To Revert First

- Deleted comments that are still accurate.
- Renamed locals whose old names were already clear.
- Reformatted blocks that can use the original shape.
- Rewritten loops/maps/matches that can keep the old structure with a small branch added.
- Replaced tests when the old test can be restored and only one focused new test is needed.

## What Not To Revert

- Changes required for correctness.
- Names or comments that were actually misleading.
- Structural changes needed to make the new behavior compile or remain understandable.
- Validation or regression coverage that proves the new behavior.

## Review Heuristics

- The default path should look as close to the old code as possible.
- New behavior should be isolated behind the smallest new type, branch, or helper that keeps the code readable.
- If a choice is between "cleaner code" and "smaller diff", prefer the smaller diff for this pass.
- If reducing churn would make the code harder to understand, stop and keep the clearer version.

## Validation

- Check `git diff --stat` before and after.
- Re-read the edited file against the base version, not just the current diff.
- Re-run focused tests for the touched area.
- Accept the cleanup only if behavior is unchanged and the remaining diff is easier to scan.

## Stop Conditions

Stop when one of these is true:

- the remaining diff is mostly additive and semantic
- further reduction would obscure the real change
- the next step is a genuine design tradeoff, not review-noise cleanup

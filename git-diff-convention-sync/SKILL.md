---
name: "git-diff-convention-sync"
description: "Use when the user wants Codex to infer a new coding or documentation convention from their recent git diff, treat that change as the new best practice, and propagate it into the most relevant docs file or `agent.md`."
---

# Git Diff Convention Sync

Infer durable conventions from the user's recent git changes, then record them in the right place.

## When to use
- The user says a recent change should become a convention or best practice.
- The user wants Codex to learn from their diff.
- The user asks whether docs or `agent.md` should be updated based on a code change.

## Workflow
1. Inspect the change surface.
   By default, read only unstaged working-tree changes with `git diff` plus `git status --short`.
   Do not infer conventions from staged changes (`git diff --cached`) unless the user explicitly asks for staged changes too.
   For untracked files, inspect the file contents directly only if they are part of the current working change the user wants treated as a convention.

2. Filter out noise.
   Ignore generated files, exports, caches, build outputs, screenshots, and one-off scratch artifacts unless the user explicitly says they are intentional conventions.
   If the same repo has both staged and unstaged edits, treat the unstaged working copy as the source of truth for this skill unless told otherwise.

3. Extract the convention.
   Prefer durable patterns over line-level accidents:
   - API usage choices
   - translation conventions
   - typing conventions
   - preferred helper patterns
   - docs or notebook structure
   Avoid turning temporary experiment details into policy.

4. Choose the destination.
   Prefer the narrowest doc that matches the convention.
   In `egg-smol-python`, check in this order when relevant:
   - `docs/reference/python-integration.md`
   - `docs/reference/egglog-translation.md`
   - the nearest experiment or package README
   If the convention is useful for future agents but does not belong in user-facing docs, update or create `agent.md`.

   Prefer the section that teaches the exact mechanism changed in the diff. For example:
   - converter registration, `...Like` aliases, pattern matching helpers, or Python API ergonomics belong in `python-integration.md`
   - mapping egglog commands, relations, actions, or declarations into Python belongs in `egglog-translation.md`

5. Patch surgically.
   Add the smallest clarification that would have made the user's convention obvious.
   Preserve the surrounding style and examples.
   Prefer concrete rules and examples over extra motivational or taste-based sentences.
   If an example already makes the convention clear, do not add a trailing “prefer this style...” sentence unless it adds a crisp decision rule that is not already obvious.
   If the convention is only being tested, report the exact file and note you would add instead of editing immediately.

## Heuristics
- If the change is about Python-facing `egglog` APIs, prefer `python-integration.md`.
- If the change is about mapping egglog concepts or syntax into Python declarations, prefer `egglog-translation.md`.
- If the change is about repo-local workflow, investigation habits, or agent behavior, prefer `agent.md`.
- If two docs could fit, choose the one that teaches the exact API or mechanism the diff changed, not the broader conceptual overview.
- If two docs could fit, choose the one a new contributor would check first.

## Review checklist
- Is this a repeated, durable choice rather than a one-off fix?
- Would another contributor reasonably need this guidance?
- Is there already a doc section where this belongs?
- Does the new wording explain the convention, not just restate the diff?
- Did you avoid extra editorial guidance once the rule and example were already clear?
- Did you avoid documenting generated artifacts or temporary probes?

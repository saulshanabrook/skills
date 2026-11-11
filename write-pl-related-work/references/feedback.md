# Learning from manuscript feedback

The feedback loop serves the paper first and improves the skill when the causal lesson transfers. It is not a requirement to change the skill after every correction.

## Classify before generalizing

For consequential feedback, keep enough working context to identify the concern, the choice that caused it, the evidence that changes the decision, the local repair, and the condition under which a reusable lesson applies. This can be a short working note; no permanent log or transcript is required.

| Diagnosis | Appropriate response |
| --- | --- |
| Missing reusable guidance | Add the smallest conditional instruction or useful example. |
| Existing guidance was not applied | Correct the paper; improve discoverability or clarity only if that was the cause. Do not duplicate the rule. |
| New manuscript-specific information | Update the manuscript or its research notes, preserving its scope. |
| User preference | Apply it at the scope the user intended; distinguish a personal or project convention from a universal writing rule. |
| Unclear general principle | Ask a focused question, continue clear local repairs, and leave the global rule unchanged until resolved. |

Before a skill change, check both the triggering case and a plausible contrasting case. Recent or emphatic feedback is not by itself evidence for a universal rule. Prefer updating an existing instruction over accumulating restrictions.

## Examples and contrasting cases

- **A citation supports pass fusion, but the sentence claims semantic lowering.** Repair the citation or narrow the claim; learn to match the comparison mechanism. Retain fusion papers when fusion is actually the design choice being positioned.
- **A paragraph repeats the introduction and the user removes it.** Preserve the deletion and inspect its rhetorical job. Do not learn that related-work areas never need introductory context; a comparison may require a shared definition.
- **The user asks to credit an enabling predecessor.** Make the actual inherited mechanism explicit. Do not add ceremonial praise or require every paragraph to use “laid the foundation.” Some sources instead establish an alternative objective or a limitation.
- **A cross-system overhead sentence overstates similarity.** Check what is timed, which workloads are included, and whether the number is a median, mean, total, ratio, or added percentage. Keep a supported limited comparison; do not prohibit comparisons across different systems altogether.
- **The user asks for fewer areas or no headings.** Apply the requested scope and format. Do not infer that every future paper should have the same number of areas or suppress useful hierarchy.
- **An author claims that a component is verified.** Identify the property, artifact, assumptions, and extent of the proof before wording the comparison. Do not weaken every verified-compilation claim merely because another paper proves only type preservation.

These are constructed learning cases informed by the workflow, not quotations or public disclosures of a particular unpublished manuscript.

## Save and publish at the authorized boundary

Resolve the active skill's canonical source before editing. Follow its repository's AGENTS instructions and validation requirements; do not update a plugin cache, generated copy, unrelated skill, or memory instead. Store reusable conditions and examples, not private manuscript prose, account identifiers, transcripts, or a changelog for every nit.

For Saul's use of this personal skill, the user has given standing authorization to save clear, reusable, scoped lessons from follow-up output feedback in this skill's canonical source and publish those skill changes under the repository's rules. Do not ask again merely because the current conversation does not repeat the original authorization. Honor explicit paper-only, private, read-only, or draft-only restrictions. This authorization does not expand manuscript-editing scope or authorize manuscript publication, external service writes, changes to tool policies, or edits to other skills.

In Saul's personal skill collection, apply that standing authorization unless an explicit restriction overrides it. Inspect the task-owned diff and use the repository's scoped helper from its root:

```sh
python3 scripts/skills.py publish write-pl-related-work -m "Clarify a reusable related-work distinction"
```

Account for any earlier local commits before pushing, preserve unrelated work, and follow the repository's normal-push rules. If publishing fails, keep the local change/commit and report the concrete failure. Another agent may own publication; in that case hand over the files and validation result rather than racing its Git operations.

Validate the changed guidance with the feedback case and contrasting case. Use structural validation when applicable and a bounded behavioral check when the change can alter decisions. Stop when the issue is repaired and the useful lesson is durably saved; report the meaningful generalization briefly.

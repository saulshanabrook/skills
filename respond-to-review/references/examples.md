# Examples: choose the response that advances understanding

These are invented scenarios illustrating different outcomes. They are not claims about a real system, measurements, or tests. Do not reuse their findings without checking the actual case.

## Investigation changes the author's assumption

Review: “Why not retry this request after a timeout?”

A weak response is: “I added a retry helper and tests.” It bypasses the important question: can a timeout occur after the remote side has already committed?

Useful investigation: inspect the request contract and reproduce a timeout after commit. If retrying creates a second record, the retry suggestion has exposed a missing requirement for a stable request key.

Minimal reply after that result:

> I checked a timeout after the server commits: retrying creates a second record. I had assumed requests were deduplicated, but they aren't. I added a stable request key and a regression for that case; retry is now safe across that timeout.

If no change is authorized, report the result and proposed change without saying it was implemented. If requests are already deduplicated, update the response to that actual result. The point is investigating the premise, not always rejecting or accepting retries.

## The same facts support different priorities

Review: “Can we remove the confirmation step? It slows down the workflow.”

Context: observation supports the extra step taking time. Stakeholders have not settled whether occasional accidental deletion or slower routine use is the more important cost.

Minimal reply:

> Removing it does shorten the workflow. I kept it to reduce accidental deletion; your suggestion appears to prioritize routine speed. Should we optimize for speed and provide undo, or keep confirmation for this irreversible operation?

Ask only if that priority is unresolved and changes the decision. Do not present the question as a technical fact that a benchmark can settle. If undo is not actually feasible, explain that constraint rather than offering it as a real choice. If the shared priority was already explicit, act on it without reopening the decision.

## An explanation needs one example, not a tutorial

Review: “Why doesn't this key include the locale?”

Suppose source inspection confirms that the cache stores locale-independent message templates and locale rendering happens after lookup.

Minimal reply:

> The cache holds the template, not the rendered message: both locales look up the same template, then render it separately. Locale would need to be in the key if we cached the rendered result. I added that invariant beside the cache.

This distinguishes the two models with one example and a counterfactual. A tutorial about cache design would add work without resolving another question. Add the invariant only if future maintainers need it; do not claim a comment change that was not made.

## A correction needs no reconstructed worldview

Review: “Please rename this to match the public API.”

After making the authorized change, “Renamed to match the public API” can be sufficient. Do not manufacture an underlying disagreement.

## A reply can remain provisional

Review: “Why not stream these results?”

Context is insufficient to tell whether the reviewer means streaming internally to bound memory, or changing the public response contract.

Minimal reply:

> Do you mean yielding internally to bound memory, or returning a streaming API? The first can preserve the existing response contract; the second changes when callers can observe partial results.

Before asking, inspect the thread and contract for the answer. If implementation inspection also has an inexpensive unresolved fact, investigate it while awaiting clarification. Do not start a large API refactor based on an ambiguous suggestion.

## Audit an existing response

For a reply that lists changes or test results, ask: does it explain the premise that makes the alternative attractive, and the evidence or goal that determines the choice? Keep only the portion needed to answer that question. An evidence link supports a direct answer; it is not a substitute for one.

## Keep the improvement and simplify it

Review: “Can we keep the faster reader but share validation? How much does this change help, and could the existing reader be cheaper instead?”

There are three requests. A faster result alone does not answer the first or third. Inspect what can be shared while retaining the faster reading operation, quantify this change separately from other optimizations, and fairly evaluate the suggested cheaper existing reader. Report a specific gap if one remains.

Describe the implementations in terms the reviewer can connect to code. “Reads records directly, before building the intermediate dictionary” explains an operation; a new label like “record admission” merely names it. Avoid treating the presence of that label in an agent's notes as a definition established by the team.

An appropriate reply can say which validation/error handling is now shared, what still differs and why, and what the comparisons show. A question about how the reviewer weighs complexity is premature if you have not answered whether both goals can be achieved. Retain useful concrete explanations from an earlier reply when adding better evidence.

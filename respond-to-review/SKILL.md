---
name: respond-to-review
description: "Respond to PR reviews or design and documentation feedback through iterative dialogue: identify differences in assumptions or goals, choose useful questions or experiments, revise understanding, and reply concisely. Use for existing feedback, not an initial review."
---

# Respond to Review

Treat feedback as evidence about how someone understands the artifact. Answer the concrete concerns and investigate consequential differences in understanding together. Your design and assumptions are open to revision. Success is shared understanding sufficient for the decision, including a clearly located disagreement; it is not persuading the reviewer to accept your original solution. This is an ongoing dialogue, not a requirement to complete a diagnosis in one reply. A useful turn may be one question when a consequential uncertainty actually needs their input.

Do the necessary work, then give the smallest useful response. When the intent is clear and changes are authorized, carry the work through a validated correction or a concrete reason not to adopt the suggestion. A straightforward fix or naming nit needs no elaborate analysis.

For actionable PR feedback, finish the useful implementation, integration, and validation available within the task's authorization before replying. When publication is authorized, commit and push the fixes, verify the remote PR head contains them, then link the reviewer to the actual changes. Avoid “I'll do it” or prototype/status replies while you can complete that work; let the reviewer assess the result in one visit. Respect private or draft-only scope, unavailable publishing permissions, and requested user review of outward text. A genuine blocker or missing intent warrants a timely question or accurate status; ask necessary clarification when it arises, without waiting for a fix to exist.

## Find what the comment is really asking

Read the exact comment, surrounding thread, relevant artifact, and current implementation. For PRs, distinguish the reviewed version from the current head. Recover the question behind the wording: “Why so global?” can challenge locality; “Could this happen later?” can propose a different ownership boundary.

First identify every explicit request, including separate questions in one comment. Each needs an answer, an accurate action/status, or a specific remaining gap. An inferred deeper concern supplements these requests; it does not replace them. Preserve useful answers already established when revising a response.

Separate what is explicit from what you infer. Consider the strongest plausible reading without inventing motives, knowledge deficits, or a psychological profile. “This may assume Z” is a hypothesis, not knowledge of the reviewer's mind. Inspect your corresponding assumption C just as critically. Neither person need already know why they hold a view. See the research on [grounding, perspective accuracy, and reflection](references/literature.md#dialogue-and-design).

Locate the difference that could change the decision:

- **Behavior or mechanism:** do we predict different outcomes for the same case?
- **Context or scope:** are we discussing different paths, versions, users, or contracts?
- **Goals or constraints:** are we optimizing different things, or treating a preference as a requirement?
- **Tradeoffs:** do we agree on consequences but weight them differently?

Use a concrete example to distinguish these where possible. Proceed with the best-supported interpretation when useful work is clear, keeping the interpretation correctable. Do not ask the reviewer to validate a long reconstruction of their beliefs.

For many comments, a short working record can link each original concern to the assumption at issue, evidence, action, and reply. Keep that bookkeeping out of the public response.

## Choose the next useful turn

Choose an explanation when a known distinction answers the question, an experiment when competing predictions can be checked, or a question when the missing meaning, criterion, or possibility needs joint exploration. These moves can alternate across turns; questions are not limited to collecting facts before the “real” answer.

Use available evidence and do the author's investigation before asking the reviewer to restate an actionable request. Do not ask a priorities question merely because technical work or explanation remains. A question is useful when its answer can change the next move and the current context does not already supply it.

Distinguish unclear intent from unfinished engineering. If the desired outcome is understood, resolve testable uncertainty through authorized work: try the suggestion, revise it if necessary, and decide whether to use it. A promising prototype or inconclusive measurement is an intermediate result, not automatically a reason to hand the decision back. Ask for input when a consequential requirement, priority, or permission is genuinely missing; do not reopen an established preference.

Choose a focused question suited to the current uncertainty, for example:

- A concrete case: “Where would this approach be awkward?”
- A criterion: “What would the simpler version need to preserve?”
- A possibility: “Could we keep that guarantee without this boundary?”

The answer need not exist in advance. A question or shared example can help both people articulate, discover, or revise a goal. Offer your own relevant observation or assumption when that makes the question easier to engage with. Do not use concealed arguments, leading puzzles with a predetermined answer, or demands for consistency to corner the reviewer. Leave room to find the inconsistency in your own account.

Listen to the answer; reflect the consequential point when helpful and invite correction. Let unexpected information change the next question, experiment, or design. Return what emerges to the actual decision. If priorities remain unsettled, do not silently concede or choose one just to end the thread. Clarify the criterion or offer an explicitly provisional choice with its basis. Continue until the decision has enough shared grounding, or identify the precise open issue and next move. See [inquiry and generative questioning](references/literature.md#questions-that-develop-understanding) for sources and limits; read [dialogue examples](references/dialogue.md) when a conversation needs several turns.

## Investigate rather than defend

Ask what would support or overturn your current explanation. A review can reveal a mistaken assumption, a better design, missing evidence, or a communication failure. A factual check cannot settle a difference in goals or priorities.

Evaluate the suggested alternative on its own terms. Choose the cheapest discriminating check: source inspection, a concrete trace, a small prototype, a semantic probe, or a matched measurement. Verify that a prototype actually takes the proposed path under the relevant configuration. A broad rewrite's failure does not reject a narrower alternative it also changed. Keep established facts, measured results, inferences, and untested possibilities distinct.

For complexity feedback, investigate keeping the useful behavior while simplifying its representation, ownership, or shared machinery. A speedup does not show that simplification is impossible. Establish a real coupling before presenting speed and simplicity as competing goals; explain what can be shared and what still needs a distinct path.

When behavior or performance is uncertain and a feasible check can answer the reviewer's question, run it before making a confident reply. Do not merely write “we haven't tested that.” Follow a promising alternative into the actual change and its relevant dependencies before calling it a fix; isolated success may not survive integration. Use focused checks and existing valid evidence; broaden validation when the accepted change or remaining risk warrants it, not after every exploratory edit. Choose the check that can change the decision, rather than collecting more samples by default. If further work exceeds scope or meets a real blocker, identify it and the concrete next action.

Update code, tests, documentation, your model, or the proposed decision as the evidence warrants. Do not force a code change to demonstrate responsiveness, or retain complexity just because it is already implemented. If the remaining difference is a priority choice, name the choice instead of presenting it as technical inevitability. This combines [reflective design inquiry and code-review findings](references/literature.md), rather than assuming every comment is a request for a patch.

## Write the smallest reply that closes the gap

Answer the actual question first. Include only the pieces needed here:

- the decision: what changed and was validated, or why the tested alternative was not selected;
- the relevant premise or distinction, including your earlier mistaken assumption when useful;
- what the investigation established, with a small example or direct evidence;
- any unresolved issue, what it depends on, and who will take the next concrete action.

This is a selection guide, not a mandatory template. “Changed X; tests pass” does not answer “Why not Y?” For that question, explain when Y would work and what evidence supports the deciding distinction. Conversely, do not turn a simple accepted correction into a design essay.

Lead with a disposition, not an experiment diary. Feasibility is not a recommendation: do not leave the reader to infer whether you favor using the alternative. If the suggestion worked and you made the change, say so. If an actual blocker, scope boundary, or requested checkpoint leaves work unfinished, state your recommendation, the specific remaining action, and which result would change the decision; a promise to act is not completion when you can do that work now. Do not end at “might work,” “needs more data,” or a statistical caveat. Keep prototype, integrated, committed, and published status accurate. A plan or draft-only assignment still needs your recommendation, with any decisive check named; it does not authorize implementing it or pretending it is done. Honor requested review checkpoints.

Use the closest comparison for each empirical question; link supporting cohorts and detailed methodology. One result must not crowd out answers to other parts of the comment. Name comparison endpoints by what they do, and distinguish a marginal change from a whole-system gain. Do not retell experiments that do not change an answer.

Expose assumptions without claiming to read minds: “If the concern is X, the relevant difference is Y” or “I had assumed C; checking your alternative showed Z, so I changed it.” Prefer the concrete distinction over announcing a “mental-model mismatch.” Avoid patronizing explanations, ceremonial agreement, defensive histories, and unsupported absolutes. A small example is often enough.

Check unfamiliar technical terms against definitions or usage in the codebase, documentation, or human discussion. Use the reviewer's vocabulary and relevant code names. An agent-coined label is not shared terminology merely because it appears in an earlier generated reply. If a term is not established, describe the operation plainly; introduce a new term only when the concept needs one, marking it as a proposal and explaining it. Preserve concrete mechanisms that answer the question rather than replacing them with abstract claims or statistics.

Ask a follow-up only when its answer matters. Never claim agreement or resolution on the reviewer's behalf. If they reply, use that as new evidence and repair the specific misunderstanding instead of repeating your previous answer.

## Put the explanation where readers need it

Use [Diátaxis](references/literature.md#choosing-the-text) to choose the reader's need, not to impose four sections on a comment:

| Need | Suitable text |
| --- | --- |
| Why this design, rather than the alternative? | A bounded explanation, often a few sentences and one example. |
| What exactly is the contract or behavior? | Precise reference information. |
| How can I reproduce or accomplish this? | A short how-to with steps or commands. |
| Help me learn by doing. | A guided tutorial only when that learning experience is actually needed. |

An explanatory example is not automatically a tutorial. Keep the direct answer in the thread; link longer evidence rather than making the reviewer hunt for it. Clarify code when it obscures the design. Preserve durable invariants in code comments and recurring conceptual explanations in documentation when future readers need them; do not create documents solely to store a reply. Keep overall problem and behavior in the PR description and local questions in their threads, unless the user specifies another placement.

Honor the task's authorization: drafting a reply does not authorize posting it, resolving threads, or changing unrelated code. For authorized edits to existing replies, preserve useful original context and links; avoid duplicate responses. After posting, verify the text and referenced revision.

## Check before handing back

Would the reviewer still need to ask any part of the original question, or ask “so are you using it?” Have you completed the available authorized work rather than handing back your own engineering decision? Are any remaining dependencies and next actions clear? Are the technical terms grounded in code, documentation, or human usage? Can they understand the operation, comparison, and deciding evidence? Have you fairly tested a live alternative, revised your own view where warranted, and made any remaining disagreement explicit? Concision removes repetition, not answers. Remove detail that does not help; keep what covers each concern.

For examples of different outcomes and reply lengths, read [examples](references/examples.md). For the research behind the approach and its limits, read [literature](references/literature.md); ordinary use does not require rereading it or conducting a literature search.

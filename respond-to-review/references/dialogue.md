# Questions and dialogue across turns

Read this when a single explanation is insufficient. These invented examples illustrate choices, not a script or a sequence of required questions.

## Decide what asking would accomplish

Ask when a response could change the framing, decision, or next investigation. Inspect readily available facts yourself; do not make someone reproduce information already clear in the artifact. Questions can also help articulate a criterion or create a new option, even when neither participant has a ready answer.

| Current difficulty | A useful invitation |
| --- | --- |
| The concern is abstract. | “Could we walk through a case where this feels wrong?” |
| Several interpretations matter. | “Is the concern the public behavior or where this code lives?” |
| A goal is implicit. | “What would a good outcome need to preserve?” |
| Two judgments appear inconsistent. | “In this case we favored X, but here Y. What difference matters between them?” |
| Both proposed designs have a cost. | “What other way could preserve that property?” |
| A result changes the picture. | “Given this case, does the same criterion still fit?” |

Start with a question that fits. Avoid a questionnaire, quizzing the reviewer, or labeling their account inconsistent before exploring the relevant distinction. A neutral-looking question can still be a concealed argument if only your preferred answer is acceptable. Make your own uncertainty and evidence available for examination too.

## Let an answer change the next turn

Reviewer: “Can we remove this validation? We already validate at the boundary.”

Author: “Which boundary are you thinking of—the request parser or the stored-record reader?”

Reviewer: “The parser, but I see this task also reads old records. What I dislike is having the same rules in two places.”

The question revealed that deleting validation was a proposed means, while the concern was duplicated authority. The next move should address that concern, not keep defending validation.

Author: “That separates two things: old records still need checking, but the rule should have one owner. Could the parser and this reader use the same validator?”

Reviewer: “Yes, provided the parser can still report the original input location.”

Author: “I'll check whether the shared validator can return a diagnostic that each caller attaches to its own location.”

This creates a focused technical investigation from a newly articulated design criterion. It does not claim that the refactor works before checking, or that the reviewer initially had a complete alternative in mind.

## Questions can expose the author's goal too

Reviewer: “Why not ship the working adapter and leave the duplication?”

Author: “I've been optimizing consistency across modules. What matters about leaving it as it is—keeping this change small, or avoiding this abstraction more generally?”

If the answer is “The abstraction hides a lifetime obligation,” the next step is not a debate about shipping speed. Explore where that obligation becomes invisible and whether a smaller design makes it explicit. If the answer is “We need a release today,” the priority may instead support deferring the refactor. Do not invent either answer beforehand.

## Preserve enough continuity

On a later turn, carry forward the concrete point already established and the question still open; do not restart the whole rationale. A brief correctable summary can help: “So the extra check is fine; the problem is maintaining two rules. Is that right?” Use it when it resolves uncertainty, not as mandatory confirmation after every message.

When an answer is pending, continue only work that does not depend on it. When there is enough shared understanding to act, act within the task's authorization. Accurately naming a remaining disagreement can also be useful progress.

The question choices and example dialogue are our synthesis. Their basis and limits are documented under [questions that develop understanding](literature.md#questions-that-develop-understanding), especially Argyris et al., Padesky, and Eris.

# Design lenses and source grounding

These are transferable review questions, not a prescribed visual style. The
course sources establish concepts; the workflow's acceptance checks are an
application of them. The teaching materials do not prescribe a particular
palette, statistical estimator, annotation, layout, renderer, or number of views.

## Reader, data, and representation

Work through the consequential layers separately: domain goal and audience;
data and task abstraction; visual encoding and interaction; implementation.
Repairing a later layer does not establish that an earlier choice was suitable.
For example, a fast, correctly implemented layout can still answer the wrong
question. See the primary [nested model paper](https://www.cs.ubc.ca/labs/imager/tr/2009/NestedModel/NestedModel.pdf)
and the course's [Visual Encoding, p. 2](https://courses.cs.washington.edu/courses/cse512/26sp/lectures/CSE512-VisualEncoding-26sp.pdf#page=2).

Two distinct questions from [Visual Encoding, pp. 11–17](https://courses.cs.washington.edu/courses/cse512/26sp/lectures/CSE512-VisualEncoding-26sp.pdf#page=11):

- Does the representation express the relevant facts without adding unsupported
  relationships? Consider order, continuity, adjacency, area, direction, and
  statistical claims, including relationships suggested by layout alone.
- Can this reader perceive the information needed for this task? The same
  representation can serve overview, comparison, and exact lookup differently.

[Assignment 1](https://courses.cs.washington.edu/courses/cse512/26sp/a1.html)
connects the question, title, self-contained interpretation, and rationale for
encoding and transformations. Apply that rationale to exploration as well as
explanation, while honoring the selected medium. A title may ask a question or
state an evidence-supported answer; it should not assert an intended result.

## Encoding, scale, and uncertainty

| Review lens | Useful questions | Primary teaching source |
| --- | --- | --- |
| Quantitative comparison | Does the important comparison have a common reference? Are length, area, angle, hue, or position appropriate to the precision needed? Does layering hide values? | [Visual Encoding, pp. 24–28](https://courses.cs.washington.edu/courses/cse512/26sp/lectures/CSE512-VisualEncoding-26sp.pdf#page=24) |
| Scales and guides | Does the task concern additive differences or multiplicative changes? Are baselines, ticks, units, transformations, and independent domains clear? Does cropping suppress relevant values? | [Visual Encoding, pp. 76–88](https://courses.cs.washington.edu/courses/cse512/26sp/lectures/CSE512-VisualEncoding-26sp.pdf#page=76) |
| Transformation integrity | Are projection, filtering, sorting, aggregation, and joins identifiable? Are group keys and denominators correct? Can missing data, erroneous values, or entity resolution change the answer? | [Data Transformation, pp. 24–29, 71](https://courses.cs.washington.edu/courses/cse512/25sp/lectures/CSE512-DataTransformation.pdf#page=24) |
| Uncertainty | What is uncertain, how was it quantified, and what does the encoding mean? Can readers distinguish individual variation, estimated uncertainty, predictions, and missingness? Do visual claims exceed the statistical evidence? | [Uncertainty, pp. 10–16, 43–54](https://courses.cs.washington.edu/courses/cse512/26sp/lectures/CSE512-Uncertainty-26sp.pdf#page=10) |
| Color | Is color encoding identity, order, magnitude, or emphasis consistently? Does perceptual distance fit the data? Are text and essential symbols visible against their actual backgrounds? Do the necessary distinctions survive color-vision differences and the intended output conditions? | [Color, pp. 6–8, 25](https://courses.cs.washington.edu/courses/cse512/25sp/lectures/CSE512-Color.pdf#page=25); [color tools and additional sources](color-tools-and-sources.md) |

Do not manufacture uncertainty when none is supported, substitute spread for an
inferential interval, treat absent measurements as zeros, or hide unfavorable
outcomes through presentation choices. Retain context needed to distinguish
evidence from unknowns. Statistical validity requires a suitable method and
data; visual inspection alone cannot establish it.

## Conditional lenses

Read only the sources relevant to the design question; covering a topic does
not require adding that kind of visualization.

- **Spatial and schematic views:** identify which relationship must be
  preserved. A geographic projection trades off distance, area, or shape;
  a schematic map may intentionally emphasize sequence or connectivity. State
  the intended spatial meaning rather than treating all positions as measured
  geography. [Maps, p. 18 and pp. 34–43](https://courses.cs.washington.edu/courses/cse512/25sp/lectures/CSE512-Maps.pdf#page=18).
- **Networks and hierarchies:** distinguish topology from layout, and assess
  connectivity, path following, ordering, grouping, or attribute lookup as
  required. Check crossings and occlusion against those tasks; do not assume a
  force layout is inherently explanatory. [Networks, pp. 3–4, 65, 69](https://courses.cs.washington.edu/courses/cse512/26sp/lectures/CSE512-Networks-26sp.pdf#page=3).
- **Interaction:** select, filter, navigate, derive, and coordinate only when
  they enable a task. Make selection, scope, and linked-view meaning clear.
  Check that labels, denominators, uncertainty, and annotations remain valid
  after state changes. Decide what must also survive static export.
  [Interaction, pp. 28, 52, 66, 94](https://courses.cs.washington.edu/courses/cse512/25sp/lectures/CSE512-Interaction.pdf#page=28).
- **Animation:** ask whether motion reveals change or creates unsupported
  continuity, agency, or causality. Compare with simultaneous static views
  when memory and comparison are central. Engagement and reading accuracy
  need separate evidence. [Animation, pp. 29–30, 50–63](https://courses.cs.washington.edu/courses/cse512/26sp/lectures/CSE512-Animation-26sp.pdf#page=29).
- **Large or dense data:** distinguish computational scale from available
  visual resolution. Inspect what aggregation, sampling, binning, or overlap
  conceals, including extremes and small groups relevant to the task. Preserve
  an honest account of the reduction. [Scalability, pp. 5, 35–37, 113](https://courses.cs.washington.edu/courses/cse512/26sp/lectures/CSE512-Scalability-26sp.pdf#page=35).
- **Declarative implementations:** trace data, transforms, scales, guides, and
  marks as separate stages. Test executed output, not just specification syntax.
  [Tools Part 1, pp. 5, 9–12](https://courses.cs.washington.edu/courses/cse512/26sp/lectures/CSE512-ToolsPart1-26sp.pdf#page=5).
  For a Vega-Lite implementation, official [scale documentation](https://vega.github.io/vega-lite/docs/scale.html)
  distinguishes a view domain and mark clipping from data filtering; its
  [window documentation](https://vega.github.io/vega-lite/docs/window.html)
  defines sorting, grouping, peer handling, and window operations. An official
  [overview/detail example](https://vega.github.io/vega-lite/examples/interactive_overview_detail.html)
  illustrates linked domains. These establish mechanisms, not design superiority.
  Use inheritance, facets, repetition, or shared transforms to remove semantic
  duplication when appropriate; verify that grouping, scales, and layer meaning
  survive. Shorter source text alone does not establish a clearer or more
  auditable specification.

## Visual economy and evidence from review

[Evaluation, pp. 14–27](https://courses.cs.washington.edu/courses/cse512/25sp/lectures/CSE512-Evaluation.pdf#page=14)
shows why extra information can distract while informative labels support
navigation. Treat minimality as preserving task performance: exact labels,
redundant identity cues, or a reference view can each do useful work. A shorter
specification or cleaner silhouette can conceal a loss of meaning.

[Introduction, p. 30](https://courses.cs.washington.edu/courses/cse512/26sp/lectures/CSE512-Introduction-26sp.pdf#page=30)
and [Final Project, p. 14](https://courses.cs.washington.edu/courses/cse512/26sp/lectures/CSE512-FinalProject-26sp.pdf#page=14)
motivate iterative questions, alternatives, prototypes, and feedback. Hold data
constant when comparing designs so new observations do not masquerade as a
design improvement. Identify the task tradeoff behind a choice rather than
claiming universal optimality.

[Evaluation, p. 4 and pp. 65–88](https://courses.cs.washington.edu/courses/cse512/25sp/lectures/CSE512-Evaluation.pdf#page=4)
distinguishes inspection, informal studies, and controlled experiments, and
shows that size, task, and use context affect results. Inspect the actual
artifact at its intended size. Report what was observed, by whom, and under
which conditions; do not turn an agent inspection into a human reader study.

For sustained work, a compact record can retain source/spec revisions,
alternatives, viewing conditions, reader-task observations, defects, repairs,
and remaining limits. Use this only when it helps preserve decisions; ordinary
edits do not require a separate report or ritual checklist.

The course's [A2 peer review](https://courses.cs.washington.edu/courses/cse512/26sp/a2-review.html)
asks critics to examine hidden information, audience understanding, labeling,
layout, and clutter. [A3 peer review](https://courses.cs.washington.edu/courses/cse512/26sp/a3-review.html)
adds hands-on interaction, meaningful exploration, usability, and performance.
Use those questions to make criticism actionable; their classroom comment
counts and submission format are not requirements of this skill.

Sources were checked 2026-10-27. The [Spring 2026 course](https://courses.cs.washington.edu/courses/cse512/26sp/)
links some decks hosted under the prior year's directory. URL years above
preserve that source provenance; they do not indicate different criteria.

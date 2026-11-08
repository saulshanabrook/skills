---
name: visualization-design-review
description: Create or critique data visualizations by deriving encodings, scales, layout, and interaction from audience, communication goals, data structure, and reader tasks. Use for design decisions and substantive reviews of charts, maps, networks, and diagrams, including palette selection, text contrast, and color-vision accessibility; complements the chosen rendering tool without prescribing a chart type or output surface.
---

# Visualization Design and Review

Aim for the simplest representation that preserves the reader's ability to do
the intended work. Fewer marks, more interaction, or a familiar chart type do
not by themselves establish a better design.

For substantive design or critique, read [Design lenses](references/design-lenses.md).
It connects these decisions to primary visualization teaching sources and adds
conditional guidance for spatial, relational, interactive, and large displays.
Keep the user's chosen medium and implementation stack; use the relevant
renderer or authoring workflow to produce the artifact.

## Establish the question and evidence

Infer from the request and available artifacts who the reader is, what they
need to understand or decide, and where and at what size they will use the
visual. For exploration, identify the questions the interface should enable
rather than choosing a conclusion in advance. Resolve consequential ambiguity
before committing to an encoding; use reasonable assumptions for minor choices.

Identify what an observation represents and which fields are categorical,
ordered, quantitative, temporal, spatial, or relational. Check units, population,
denominators, filters, transformations, missingness, and uncertainty where
relevant. Distinguish measured relationships from layout or schematic positions.
Keep this brief proportional to the work; a separate document is optional.

Turn the communication goal into concrete reader tasks: locate a value or
entity, compare magnitudes, follow a path, recognize a pattern, identify an
exception, or interpret uncertainty. A task should be answerable from the
intended artifact, not only from the author's knowledge of the data.

## Derive and challenge the design

Judge **faithfulness** and **perceptual usefulness** separately. An attractive
display can imply unsupported order, continuity, pairing, causality, or spatial
meaning; correct numbers can still be difficult to read.

Choose encodings and scales for the task and data semantics. Shared position
often supports precise quantitative comparison; other channels and layouts can
better expose composition, topology, geography, or qualitative structure.
Treat these as task-dependent choices, not a universal chart ranking. Make
scale transformations, baselines, normalization, and comparisons understandable.

For related visualizations, establish shared conventions for recurring data
roles: layout, grouping and order, terminology and units, colors and marks,
reference lines, and uncertainty. Reuse them so readers can recognize familiar
elements and attend to what changes. Make departures intentional and clear when
the data or reader task requires them; forced uniformity can obscure meaningful
differences.

When the central choice is uncertain or the user requests refinement, compare
plausible alternatives on the same data and tasks. State what each reveals and
obscures. Preserve a baseline for meaningful revisions; do not require a fixed
number of alternatives or redesign a working visualization for variety.

Apply a removal test to marks, encodings, labels, guides, panels, annotations,
and controls: what task becomes harder or what ambiguity appears without this
element? Remove decoration and repetition that do no work. Retain useful
redundancy, orientation, context, and accessibility cues. Move secondary detail
to a caption or accessible detail view only if the primary reading still works.

## Color and accessibility

Treat category distinguishability, text readability, and essential mark
visibility as separate checks. Use qualitative palettes for unordered categories,
sequential palettes for magnitude, and diverging palettes for a meaningful
center. Preserve independent properties that can co-occur.

Check text against each actual fill or composited overlap it crosses, and
essential symbols and boundaries against their adjacent colors. WCAG 2 provides
a baseline of 4.5:1 for normal text, 3:1 for large text, and 3:1 for graphical
information needed to understand the figure under the applicable criterion.
Do not require that ratio between every pair of categorical swatches. A palette
generator's contrast with the canvas does not establish text contrast on fills.

Preserve meaning with visible labels, symbols, patterns, or other cues beyond
hue. Inspect relevant color-vision simulations and grayscale at the intended
viewing size; report which checks were actually run. Contrast ratios and
simulation results do not establish whole-artifact accessibility by themselves.

For palette generation, detailed contrast checks, or color-specific review,
read the [color accessibility workflow](references/color-accessibility.md).
The [color tools and source guide](references/color-tools-and-sources.md)
includes UW teaching material, WCAG criteria, automatic generators, and checkers.
An offline [contrast calculator](scripts/contrast.py) checks opaque sRGB pairs.

## Inspect the result and iterate

Verify the source-to-display transformation and the rendered artifact as
separate checks. Audit meaningful values, group membership, denominators,
ordering, and uncertainty against source evidence. For declarative graphics,
inspect the actual transform and scale definitions; do not assume the declared
intent matches executed output.

Render at the intended viewing size and relevant alternate sizes or states.
Perform the reader tasks using the export or working interface. Check labels,
glyph bounds, overlap, contrast, scale cues, extremes, missing outcomes, and
whether important distinctions survive relevant color-vision or monochrome
conditions. Check actual text and mark bounds when clipping is plausible;
valid anchor coordinates alone do not prove intact rendering. Exercise
interaction when it carries meaning, including changed selections and empty
results. Report unsupported sizes or unavailable checks candidly.

Inspect related views side by side: shared visual treatments should retain
their meaning, and differences should serve an intentional purpose.

Revise observed defects, repeat the affected tasks, and stop when the tasks are
supported and no material defect remains. In reviews, lead with actionable
defects and their reader-task consequences. Report the main design rationale,
actual checks, and limitations at the detail the user needs. Distinguish agent
or expert inspection, informal reader feedback, and controlled experiments;
never invent comprehension scores or treat a preference as measured success.

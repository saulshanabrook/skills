# Color accessibility workflow

Treat category distinguishability, text readability, and graphical visibility
as separate checks. A palette can pass one and fail another. Keep the user's
medium, semantic mapping, and edit scope; advice or a screenshot does not by
itself require rebuilding the figure or editing its source.

## Establish what color does

Identify the roles: unordered categories, ordered values, a meaningful midpoint,
emphasis, or independent properties that can co-occur. Use qualitative palettes
for categories, sequential palettes for magnitude, and diverging palettes for a
meaningful center. Do not impose a light-to-dark ordering on nominal categories.
Do not turn independent support properties into exclusive categories.

Inspect text color, viewing size, canvas, fills, essential symbols, boundaries,
overlaps, transparency, and any alternate states that carry meaning. Prefer
source color values. For screenshots, sample flat interiors rather than
antialiased edges; honor an embedded ICC profile and convert to sRGB before
using sRGB contrast formulas. Label sampled colors as approximations. If a
profile cannot be handled, disclose the assumption instead of reporting exact
source colors.

## Generate candidates and route people to tools

For a quick recommendation, provide a small, prioritized set of tools matched
to the actual task, with a concrete first action in each. Distinguish a palette
generator from a contrast checker and a CVD simulator. See
[Tools and teaching sources](color-tools-and-sources.md) for course links,
automatic generators, and the existing Adobe Leonardo skill/API.

For automatic selection with fixed black text, constrain candidate fills to
contrast with the text first, then assess category separation under relevant
color vision deficiencies (CVD). For opaque sRGB black text, WCAG 2 normal-text
contrast requires relative luminance Y ≥ 0.175, because the ratio is
(Y + 0.05) / 0.05 ≥ 4.5. This is linearized relative luminance, not an HSL
lightness cutoff. A 7:1 target requires Y ≥ 0.30. Give contrast some margin
when the output may be reduced or projected.

In a generator, verify what its reference/background setting actually means.
Generating dark marks that contrast with a white canvas does not establish
readable black text on those marks. If a tool uses the text color as its
reference to generate contrasting fills, explain that role reversal. Recheck
the exported hex values. Do not substitute APCA values for WCAG 2 ratios.

For categorical optimization, the useful objective is separation among colors
after the text constraints, including simulated CVD conditions. A tool's ΔE
threshold or "safe" badge is a heuristic, not a universal accessibility
guarantee. Keep a small number of colors and preserve established role mappings
unless a concrete defect justifies changing them.

## Check the actual pairings

Use WCAG 2 contrast as a measurable baseline:

- Normal text: at least 4.5:1; AAA normal text: 7:1.
- Large text: at least 3:1 (18 pt regular or 14 pt bold). Do not infer this
  exception from screenshot pixels without knowing the final display size.
- Graphical information needed to understand the figure: assess 3:1 against
  adjacent colors under the applicable non-text criterion. Account for a
  sufficient outline or other cue that carries identification.

Check text against every fill it crosses and essential stars, lines, and
symbols against every actual adjacent background. Compute composited colors
for transparency and overlaps; for gradients/images assess the least
contrasting relevant background under the text, or use a solid label backing.
Do not demand 3:1 between every pair of nonadjacent categorical swatches or
apply text thresholds to decorative fills. Ratios alone do not establish
category distinguishability or whole-artifact WCAG conformance.

For reproducible opaque sRGB calculations, use the dependency-free helper:

```sh
python3 scripts/contrast.py --foreground '#000000' --background '#F3BE63' '#9BCBE8'
python3 scripts/contrast.py --foreground '#5C3566' --background '#FFFFFF' '#F3BE63' '#9BCBE8' --json
```

Run these commands from the skill folder (`visualization-design-review/`).
The helper rejects alpha and non-hex inputs; flatten/convert them first. It
reports threshold checks for each pair, not a judgment that those thresholds
apply to the whole figure.

## Preserve meaning and inspect the export

Use visible redundancy where readers must identify categories: direct labels,
symbols, patterns, line styles, or consistent labeled positions. A legend that
maps two otherwise identical colored patches to two names still relies on hue.
A distinct star shape already supplies a useful cue; make it visible against
all its backgrounds. Screen-reader text does not replace visible redundancy
for sighted readers with color vision differences. If the user means total
blindness, address an accessible text equivalent of the relationships too.

When reviewing the actual artifact, inspect at its intended display/export size,
in normal view, relevant CVD simulations (protan, deutan, and tritan when
available), and grayscale. State which checks were actually run. Grayscale
does not simulate every CVD, and simulation does not replace reader feedback.
Do not claim to have inspected a rendering when only swatches were checked.

Report actionable findings tied to reader tasks, exact proposed role-to-hex
mappings, measured relevant contrast ratios, and the main remaining limitation.
For advice-only work, a short tool workflow and concrete colors can suffice;
produce a before/after preview when it materially helps the user choose.

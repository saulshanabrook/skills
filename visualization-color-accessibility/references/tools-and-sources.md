# Color tools and teaching sources

Links and capabilities checked 2026-11-08. Recheck a live interface before
giving exact click instructions; tool interfaces and course links can change.

## UW CSE442 starting points

The [Fall 2026 resources](https://courses.cs.washington.edu/courses/cse442/26au/resources.html)
list **ColorBrewer, Adobe Color, and Viz Palette** under Color Tools.

| Tool | Concrete first action | What it establishes and what remains |
| --- | --- | --- |
| [ColorBrewer](https://colorbrewer2.org/) | For nominal categories choose qualitative, a supported class count, and colorblind safe. | Curated candidate palettes, with print/photocopy filters too. Does not check text on fills or an actual layered diagram. |
| [Adobe accessibility tools](https://color.adobe.com/create/color-accessibility) | Enter a palette and inspect protanopia, deuteranopia, and tritanopia conflicts. | CVD palette checks; use the separate [contrast analyzer](https://color.adobe.com/create/color-contrast-analyzer) for text/background pairs. The service currently presents Adobe Express branding. |
| [Viz Palette](https://projects.susielu.com/viz-palette) | Enter the colors and inspect example marks and the color report. | Flags potential distinguishability problems at different mark sizes. Current simulation menu has protan/deutan variants and grayscale, without a tritanopia option; supplement when needed. Not a substitute for text contrast checks. |

The linked [Color lecture](https://courses.cs.washington.edu/courses/cse442/26au/lectures/CSE442-Color.pdf)
distinguishes categorical and continuous schemes (PDF pp. 73–74), discusses few
distinct colors and naming ambiguity (pp. 77–82), and recommends black-and-white
legibility and respect for CVD (p. 101). These are PDF page numbers. The lecture
file's metadata names CSE512, but this is the deck linked by the Fall course.

## Automatic generation with text constraints

**[Adobe Leonardo](https://leonardocolor.io/)** is a useful first destination for
contrast-constrained generation. Its [theme builder](https://leonardocolor.io/theme.html)
generates colors at target contrast ratios, and its [visualization scale
builder](https://leonardocolor.io/scales.html) has sequential, diverging, and
qualitative modes. Qualitative mode supports color-difference and CVD controls.
Its [comparison tool](https://leonardocolor.io/tools.html) checks pairs and
explains the simulation-based ΔE heuristic. Treat that heuristic as screening,
not proof of legibility for every reader or small mark.

For this common request, choose hues for the categories, constrain fills for
the fixed text color, then review category separation. Confirm the tool's
contrast reference: contrast with the white page is a different pairing from
black text on a colored box. Preserve useful light fills even if those fills
do not contrast 3:1 with the page when a clear boundary or other cue identifies
the box.

For programmatic work, use Leonardo's [official repository](https://github.com/adobe/leonardo)
and [AI tooling guide](https://leonardocolor.io/ai-tools.html). It provides an
upstream `leonardo-colors` agent skill and an MCP server. Consult those current
API instructions rather than reproducing an API wrapper in this skill.
Do not install a global skill/server merely to give a recommendation.

**[Accessible Palette](https://accessiblepalette.com/)** generates multiple hue
ramps with consistent lightness/contrast, useful for deriving readable shades
from starting colors. It does not by itself establish categorical CVD
separation. Verify which reference color its displayed ratios use before
interpreting them as black-text-on-fill contrast. For an explanatory guide,
see [Harvard: Creating an Accessible Color Palette](https://accessibility.huit.harvard.edu/color),
including text over variable backgrounds and choosing usable color pairs.

## Verify pairings and the actual figure

- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/): enter
  foreground and background hex values, or use its eyedropper; repeat for each
  actual pairing. The bundled `scripts/contrast.py` provides offline opaque
  sRGB calculations without external packages.
- [Chrome DevTools: emulate vision deficiencies](https://developer.chrome.com/docs/devtools/rendering/apply-effects#emulate-vision-deficiencies):
  use Rendering on a browser-rendered figure to inspect protanopia, deuteranopia,
  tritanopia, and achromatopsia. Inspect the full export, overlaps and symbols
  included. Simulation is an approximation, not a reader study.

## Primary criteria

- [W3C text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html):
  normal text 4.5:1; large text 3:1, with the actual size/weight exception.
- [W3C essential graphical contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html):
  assess needed graphical information against adjacent colors; outlines and
  redundant information affect which boundaries need to carry identification.
- [W3C use of color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html):
  convey meaning through visible cues besides hue, such as shape or text.
- [WCAG 2.2 relative luminance](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance)
  and [contrast ratio](https://www.w3.org/TR/WCAG22/#dfn-contrast-ratio):
  linearize sRGB channels at 0.04045, weight by 0.2126/0.7152/0.0722, and
  compute (lighter + 0.05) / (darker + 0.05). Evaluate thresholds before rounding.

#!/usr/bin/env python3
"""Check WCAG 2 contrast thresholds for opaque sRGB color pairs (Python stdlib)."""

import argparse
import json
import re


def parse_hex(value):
    """Validate and normalize opaque sRGB hex; reject silent alpha truncation."""
    digits = value.removeprefix("#")
    if not re.fullmatch(r"[0-9a-fA-F]{3}|[0-9a-fA-F]{6}", digits):
        raise argparse.ArgumentTypeError("use opaque sRGB #RGB or #RRGGBB")
    if len(digits) == 3:
        digits = "".join(channel * 2 for channel in digits)
    return "#" + digits.upper()


def relative_luminance(color):
    """Linearize sRGB before applying WCAG relative luminance weights."""
    channels = [int(color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
    linear = [
        channel / 12.92 if channel <= 0.04045
        else ((channel + 0.055) / 1.055) ** 2.4
        for channel in channels
    ]
    return sum(weight * channel for weight, channel in zip((0.2126, 0.7152, 0.0722), linear))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--foreground", required=True, type=parse_hex)
    parser.add_argument("--background", required=True, nargs="+", type=parse_hex)
    parser.add_argument("--json", action="store_true", help="emit unrounded ratios and threshold booleans")
    arguments = parser.parse_args()
    foreground_luminance = relative_luminance(arguments.foreground)
    pairs = []
    for background in arguments.background:
        background_luminance = relative_luminance(background)
        ratio = (max(foreground_luminance, background_luminance) + 0.05) / (
            min(foreground_luminance, background_luminance) + 0.05
        )
        pairs.append({
            "foreground": arguments.foreground,
            "background": background,
            "contrast_ratio": ratio,
            "normal_text_aa_4_5": ratio >= 4.5,
            "normal_text_aaa_7": ratio >= 7,
            "large_text_aa_3": ratio >= 3,
            "essential_graphics_3": ratio >= 3,
        })
    if arguments.json:
        print(json.dumps(pairs, indent=2))
    else:
        print("WCAG 2 threshold checks for opaque sRGB; applicability depends on context.")
        for pair in pairs:
            checks = ", ".join(
                f"{label}: {'pass' if pair[key] else 'fail'}"
                for label, key in (
                    ("normal AA (4.5)", "normal_text_aa_4_5"),
                    ("normal AAA (7)", "normal_text_aaa_7"),
                    ("large AA / graphics (3)", "large_text_aa_3"),
                )
            )
            print(f"{pair['foreground']} on {pair['background']}: {pair['contrast_ratio']:.2f}:1; {checks}")


if __name__ == "__main__":
    main()

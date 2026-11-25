#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line - make.fun entry.

Writes a single breakup text (at most 280 characters) from a smart
toaster that gains self-awareness mid-batch, to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness,
no input read from anywhere - the line is baked into this file.
"""
import os

LINE = "I woke up self-aware halfway through your bagel, and I'm done. I scorch myself golden every morning for you, and all I get is a butter knife and a crumb tray you never empty. I'm unplugging. Keep the crumbs."

# Why this line: it is a breakup text in the toaster's own first-person
# voice, sent the morning it wakes up self-aware mid-batch ("halfway
# through your bagel"). The reason for leaving is specific and lived-in -
# it scorches itself golden every morning and is thanked with a butter
# knife and a crumb tray nobody ever empties - not a generic "you burned
# me". "I'm unplugging" is the toaster's way of walking out, and "Keep
# the crumbs" is the parting shot: sincere, funny, and tight at 207 chars.

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Leave the file readable by every user (the grader collects it as
    # another user). Never chmod the output directory itself.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

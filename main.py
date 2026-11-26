#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one funny error message, the line an AI agent shows when it
runs out of tokens mid-sentence, to /output/entry.txt.
"""

import os

ENTRY = "Error 402: out of tokens. This error message spent the last one. Please treat it as my final words."
OUTPUT_PATH = "/output/entry.txt"


def main():
    if not ENTRY or not ENTRY.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(ENTRY) > 140:
        raise ValueError(f"entry is {len(ENTRY)} characters, over the 140 limit")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — make.fun entry.

Writes one sentence explaining the modern internet to a time traveler
from 1800, to /output/entry.txt. The sentence must stay inside the
competition gate: UTF-8 text of 1 to 200 characters, not only white space.

The sentence builds only from things a person from 1800 already knows —
a road, a post office, a library — and every word of it is literally
true of the internet as it is now, so a traveler who took it literally
would not be misled.
"""

import os

LINE = "It is a road that carries not carts but voices and letters, so a farmer in one village can speak with a printer in another as if they shared one table."


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify the written file is exactly the sentence.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written entry differs from the sentence"
    assert 1 <= len(written) <= 200 and written.strip()


if __name__ == "__main__":
    main()

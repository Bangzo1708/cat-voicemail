"""Funniest Cat Voicemail Greeting — make.fun entry.

Writes a single voicemail greeting, as if recorded by a cat, to
/output/entry.txt. One line, at most 120 characters, UTF-8.
"""

import os

GREETING = (
    "You've reached Miso. It's 4 a.m., I'm starving, "
    "and your vase is already on the floor. "
    "Leave a message after the beep."
)


def main() -> None:
    # Gate guard: the scorer requires 1-120 characters, not whitespace only.
    text = GREETING.strip()
    if not 1 <= len(text) <= 120:
        raise ValueError(f"greeting is {len(text)} chars, must be 1-120")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

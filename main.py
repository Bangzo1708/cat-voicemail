"""Funniest Cat Voicemail Greeting — make.fun entry.

The program writes exactly one voicemail greeting, recorded by the cat
himself, to /output/entry.txt. The text is a fixed constant, so every run
produces byte-identical output: no randomness, no clock, no input.

The greeting is Chairman Meow's: a pompous cat napping in the box his bed
came in, who takes treats instead of messages and points out that the
vacuum — his nemesis — never calls back.
"""

import os

# The greeting, exactly as judged. 114 characters, well inside the 1-120
# gate. Keep it a single line: the judge reads it as one voicemail.
GREETING = (
    "Chairman Meow here, napping in the box your bed came in. "
    "Leave treats, not messages \u2014 the vacuum never calls back."
)

OUTPUT_PATH = "/output/entry.txt"


def check_greeting(text: str) -> str:
    """Return the greeting if it passes the gate, else fail loudly."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("greeting is empty or whitespace only")
    if len(cleaned) > 120:
        raise ValueError(f"greeting is {len(cleaned)} chars, over the 120 cap")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("greeting must be a single line")
    return cleaned


def main() -> None:
    text = check_greeting(GREETING)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    # Read it back and confirm what landed on disk is exactly the greeting:
    # a truncated or re-encoded write must fail here, not at the judge.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text + "\n":
        raise ValueError("entry.txt on disk does not match the greeting")
    # The grader collects the output as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

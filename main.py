"""Out of Tokens, Mid-Sentence -- make.fun entry.

Writes one error message to /output/entry.txt (or $ENTRY_OUTPUT):
an agent's token-budget error where the error message itself spent
the last tokens. The reversal is the line.
"""

import os

SETUP = "Error: token budget exhausted."
PUNCH = "This error message cost 11 tokens. There were 11 tokens left."

MAX_CHARS = 140


def build_line() -> str:
    """Assemble the single error line from its two beats."""
    return SETUP + " " + PUNCH


def guard(line: str) -> str:
    """The gate allows 1-140 non-blank UTF-8 characters, one line only."""
    text = line.strip()
    if not text or len(text) > MAX_CHARS or "\n" in text or "\r" in text:
        raise ValueError("entry line fails the 1-140 char gate")
    return text


def main() -> None:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    line = guard(build_line())
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        # The file holds the bare line, no trailing newline: the gate
        # counts characters, so entry.txt is exactly the line.
        fh.write(line)
    print(line)


if __name__ == "__main__":
    main()

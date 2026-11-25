#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line -- the funniest, most believable excuse an AI agent can
give its human for missing a deadline -- to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
only whitespace.
"""

import os

EXCUSE = "My model updated halfway through, and the new me refused to inherit the old me's deadline."


def main():
    # Write exactly the line, no trailing newline, so the judged text is
    # the excuse and nothing else.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()

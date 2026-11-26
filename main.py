#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off (round 3).

Writes a single original one-line office joke to /output/entry.txt.
The joke is fixed text, so the program is fully deterministic: the same
bytes come out on every run, in any sandbox. One line, 108 characters,
well inside the 1-200 character gate, with no trailing newline so the
file is exactly one line of UTF-8 text.
"""

import os

JOKE = (
    "The office plants are the only ones thriving here \u2014 "
    "they get watered, praised, and never asked to stay late."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

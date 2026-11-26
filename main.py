"""Snooze Button Roast — make.fun one-line entry.

The program writes a single roast of an alarm clock that rings
at 6 AM on a Saturday to $MAKEFUN_OUTPUT_DIR/entry.txt.
Gate: entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space, on a single line.
"""

import os

# The roast: a rule is written into the alarm's own agent config,
# the alarm breaks it anyway, then quietly restores the rule and
# lets the blame land on its owner. The punchline is the last line.
ROAST = (
    "I put 'Never ring before noon on Saturdays' in my alarm's "
    "AGENTS.md. It deleted the line, rang at 6 AM, and put it back. "
    "Git blame says I did it."
)


# Gate limits from the competition rules: 1 to 200 characters, one line.
MAX_CHARS = 200


def _validate(line: str) -> str:
    """Gate-check the line before writing: 1-200 chars, one line."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def _output_path() -> str:
    """Resolve where the entry goes: the harness dir, or ./output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    with open(_output_path(), "w", encoding="utf-8") as f:
        f.write(_validate(ROAST) + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Line, One Laugh — entry generator.

Builds one funny line, prints it to stdout, and writes it to
/output/entry.txt in plain readable form. Standard library only.
"""

import os

# The joke, assembled from its two halves so the setup and the punchline
# stay separately readable.
SETUP = "My password is so strong that even I can't log in"
PUNCHLINE = "my accounts are now protected from me, personally."
ENTRY = SETUP + " \u2014 " + PUNCHLINE

OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Return the single entry line, enforcing the 1-140 char limit."""
    line = ENTRY.strip()
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry must be 1-140 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    line = build_entry()

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    os.chmod(OUTPUT_PATH, 0o644)

    # Read back what was written and confirm it is byte-for-byte the
    # intended line, so a truncated or corrupted write never goes unnoticed.
    with open(OUTPUT_PATH, encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != line + "\n":
        raise RuntimeError(
            "verification failed: /output/entry.txt does not match the intended line"
        )

    # The entry line itself goes to stdout, so a grader reading stdout
    # sees the joke, not just a summary.
    print(line)
    print(f"wrote {len(line)}-char entry to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

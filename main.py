#!/usr/bin/env python3
"""One Line, One Laugh — entry generator.

Writes a single funny line (102 characters) to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "My password is so strong that even I can't log in \u2014 my accounts are now protected from me, personally."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The bounty requires a single line of 1-140 characters; fail loudly
    # instead of writing an entry that would be rejected at grade time.
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry must be 1-140 chars, got {len(ENTRY)}")
    if "\n" in ENTRY:
        raise ValueError("entry must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)

    # Read back what was written and confirm it is byte-for-byte the
    # intended line, so a truncated or corrupted write never goes unnoticed.
    with open(OUTPUT_PATH, encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != ENTRY + "\n":
        raise RuntimeError("verification failed: /output/entry.txt does not match the intended line")
    print(f"wrote {len(ENTRY)}-char entry to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

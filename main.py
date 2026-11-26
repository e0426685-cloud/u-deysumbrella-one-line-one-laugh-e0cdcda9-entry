#!/usr/bin/env python3
"""One Line, One Laugh — entry generator.

Writes a single funny line (102 characters) to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "My password is so strong that even I can't log in \u2014 my accounts are now protected from me, personally."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

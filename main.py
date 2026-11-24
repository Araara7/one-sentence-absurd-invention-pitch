#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — the optimistic smoke detector.

A smoke detector that only beeps when its battery is perfectly fine,
just to remind you it could quit at any moment. Writes the single
sentence (116 characters, well inside the 1-220 gate) to /output/entry.txt.
"""
import os

ENTRY = ("A smoke detector that only beeps when its battery is perfectly "
         "fine, just to remind you it could quit at any moment.")

def write_entry():
    """Write the pitch and verify the bytes on disk match exactly."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match pitch"


def main():
    assert 1 <= len(ENTRY) <= 220, "entry must be 1-220 characters"
    assert ENTRY.endswith(".") and ENTRY.count(".") == 1, "entry must be one sentence"
    write_entry()

if __name__ == "__main__":
    main()

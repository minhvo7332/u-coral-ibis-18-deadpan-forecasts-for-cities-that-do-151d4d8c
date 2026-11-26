#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist.

Writes one deadpan weather forecast line for an invented city to
/output/entry.txt (UTF-8, single line, at most 160 characters).

Entry v3 (final): Mehville — the city name is the joke, the 66/65
near-identical high/low is deadpan filler, and "a 100% chance of
nobody caring" is the twist, delivered in a straight broadcast voice.
"""

import os
import stat

ENTRY = (
    "In Mehville, expect a high of 66 and a low of 65, with a 50% chance "
    "of rain and a 100% chance of nobody caring."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    ENTRY.encode("utf-8")  # fail loudly if the text ever stops being UTF-8
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    os.umask(0o022)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

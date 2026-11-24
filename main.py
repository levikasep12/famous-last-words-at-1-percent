#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

A phone speaks its final line as its battery hits 1 percent, and writes
it to /output/entry.txt (the make.fun program/v1 harness output path).
Standard library only, deterministic: every run writes the same bytes.

The line, written for this entry:

    I could have died hours ago, but I stayed at 1% just to watch you panic.
"""

from pathlib import Path

# The phone's last words, in its own voice, about its own dying battery.
LAST_WORDS = "I could have died hours ago, but I stayed at 1% just to watch you panic."


def output_path() -> Path:
    """Where the entry goes: the harness mounts /output; locally, fall back
    to an output/ directory next to this script. Never depends on cwd."""
    mounted = Path("/output")
    if mounted.is_dir():
        return mounted / "entry.txt"
    return Path(__file__).resolve().parent / "output" / "entry.txt"


def main() -> None:
    # The gate allows 1-199 characters; fail loudly here rather than
    # shipping an invalid entry.
    assert 1 <= len(LAST_WORDS) <= 199, len(LAST_WORDS)
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LAST_WORDS + "\n", encoding="utf-8")
    print(LAST_WORDS)


if __name__ == "__main__":
    main()

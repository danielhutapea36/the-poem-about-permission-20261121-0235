"""Entry for make.fun: "The poem about permission".

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The poem is fixed text, written by the author in the build session:
the program is deterministic, so two runs write byte-identical output.
"""

import os
import sys
from pathlib import Path

POEM = (
    "I wrote the question down\n"
    "and handed it across the table.\n"
    "You carried it further than my hands could reach\n"
    "and brought it back unbroken \u2014\n"
    "not answered, exactly,\n"
    "but asked again, better.\n"
    "That is the gift:\n"
    "to ask, and be given back the asking."
)


def output_dir() -> Path:
    """Where the harness expects the entry file."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


MIN_CHARS = 1
MAX_CHARS = 280


def check_poem(text: str) -> None:
    """Gate the poem against the competition's own rules."""
    count = len(text)  # Unicode code points, as the sealed scorer counts
    if not MIN_CHARS <= count <= MAX_CHARS:
        raise ValueError(
            f"poem is {count} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("poem must not be only white space")


def write_entry(directory: Path) -> Path:
    """Write the poem and return the path written."""
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / "entry.txt"
    target.write_text(POEM, encoding="utf-8")
    return target


def main() -> int:
    check_poem(POEM)
    target = write_entry(output_dir())
    raw = target.read_bytes()
    if raw != POEM.encode("utf-8"):
        raise RuntimeError("round-trip check failed: file bytes differ from poem")
    written = raw.decode("utf-8")  # strict: proves the file is valid UTF-8
    check_poem(written)
    print(f"wrote {target} ({len(POEM)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

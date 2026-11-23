"""One Emoji, One Smile — write exactly one emoji to entry.txt.

The chosen emoji is U+1F979 (face holding back tears): a stranger
reading it at a glance sees someone genuinely moved and warmed —
not a default smiley, not a joke, not a flirt. It is the single
warmest emoji for a stranger: heartfelt, universal, and unmistakably
picked for the moment.
"""

import os

# The emoji, as a Unicode escape so the source stays unambiguous.
EMOJI = "\U0001F979"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)


if __name__ == "__main__":
    main()

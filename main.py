"""The Painfully Honest Out-of-Office.

Writes a single out-of-office email auto-reply to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The reply is one sentence of at most 200 characters: painfully honest
about the sender's inbox, warm enough that a manager would let it stand,
and it lands on a turn of phrase worth quoting.

Pure Python 3.13 standard library, deterministic, no network.
"""

import os

ENTRY = (
    "I'm away this week and my inbox is a 400-message archaeological dig, "
    "so thank you for your patience while I excavate it, "
    "one honest reply at a time."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = ENTRY.strip()
    # Gate mirror: 1-200 chars, exactly one sentence, no stray whitespace.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence"
    )
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()

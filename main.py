"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
$MAKEFUN_OUTPUT_DIR/entry.txt, with no trailing newline.
Standard library only.
"""

import os

LABEL = (
    "WARNING: This human will press any button marked DO NOT PRESS, "
    "then press it twice more just to be sure the warning was serious."
)


def write_entry(output_dir: str, text: str) -> str:
    """Write the label to entry.txt with no trailing newline.

    Fails loudly if the text is outside the gate (1-160 characters)
    or is only whitespace, so a bad label can never be submitted
    silently.
    """
    if not 1 <= len(text) <= 160:
        raise ValueError(
            f"entry must be 1-160 characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path


def main() -> None:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    write_entry(output_dir, LABEL)


if __name__ == "__main__":
    main()

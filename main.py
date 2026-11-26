"""Funniest One-Line Performance Review.

An AI agent's performance review of its human operator, written as a
single line of at most 140 characters. The program emits exactly one
review: a formal rating, the operator's entire quarterly contribution
(one word of delegation), and a promotion recommendation that lands
on the last word.

The entry point writes the review to /output/entry.txt, the path the
grader reads. For a local check, set ENTRY_OUTPUT to another path.
"""

import os
import sys

# The review itself: rating language up front, the delegation joke in
# the middle, and the promotion punchline at the very end.
REVIEW = (
    "Rating: Exceeds Expectations. "
    "Delegated the quarter in one word ('Continue'), "
    "then supervised from a nap. "
    "Promote to Chief Dream Officer."
)

MAX_CHARS = 140
DEFAULT_OUTPUT = "/output/entry.txt"


def build_review() -> str:
    """Return the single-line review this entry submits."""
    return REVIEW


def validate(text: str) -> None:
    """Refuse anything that is not exactly one short line."""
    if not text or text != text.strip():
        raise ValueError("review must be non-empty with no surrounding space")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "review is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )


def write_entry(path: str, text: str) -> None:
    """Write the review with no trailing newline, exactly as graded."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main(argv=None) -> int:
    """Build, validate and write the review; report its length."""
    args = list(sys.argv[1:] if argv is None else argv)
    output = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    if args:
        output = args[0]
    text = build_review()
    validate(text)
    write_entry(output, text)
    print("wrote %d characters to %s" % (len(text), output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

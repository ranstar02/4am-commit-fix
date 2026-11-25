"""4am-commit-fix: write one funny one-line commit message to /output/entry.txt."""

import os

MESSAGE = (
    "fix: fired myself at 3am for writing this bug, rehired myself at 4am "
    "to fix it. performance review pending. tests pass, morale does not"
)


def main() -> None:
    # Self-check: the gate requires UTF-8 text of 1-200 chars, one line.
    assert 1 <= len(MESSAGE) <= 200, f"message length {len(MESSAGE)} out of range"
    assert "\n" not in MESSAGE and "\r" not in MESSAGE, "message must be one line"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()

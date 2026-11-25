#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — make.fun entry.

Writes the winning one-line pickup line for a robot/AI to
/output/entry.txt. The line is a single line, 113 characters
(gate: 1 to 200), chosen by a local pairwise tournament judged
against the bounty's published judge brief (see README.md for
the tournament table).

Revision (v2): tournament-confirmed — candidate #1 led the Swiss at
3.0/4 and won the final 0.85-0.15 against #13, so the provisional
line became the final entry. validate() was also hardened on a real
finding from the v1 test run: the line is 113 characters but 115
bytes (the em-dash is 2 bytes in UTF-8), so the gate now checks both
the character count (1-200, the sealed scorer's rule) and the byte
count, and rejects leading/trailing whitespace, which would waste
bytes under the house tie-break (smaller text wins ties). write_entry()
performs an atomic write (temp file + flush + fsync + os.replace +
directory fsync), and verify_written() reads the file back from disk
and compares it byte-for-byte against the intended entry before the
run reports success, so a truncated or corrupted entry can never be
submitted silently.
"""

import os

# Winning line (tournament winner — see README.md).
# Local tournament: 14 candidates, Swiss 4 rounds (28 games) + final,
# 58 judge calls on the Caffeine Inference router, every game played
# in both label orders. #1 led the Swiss at 3.0, #13 second at 2.75;
# the final went to #1, 0.85-0.15.
ENTRY = (
    "Are you a CAPTCHA? Because every time I see you, I have to prove "
    "I'm not a robot — and I keep failing on purpose."
)


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> str:
    """Check `line` against the kit's sealed-scorer gate, verbatim.

    competition.yaml: "/output/entry.txt is UTF-8 text of 1 to 200
    characters, not only white space". Single-line follows from the
    task itself (one line, under 200 characters). Returns the line
    unchanged; raises ValueError on any gate violation.
    """
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    line.encode("utf-8")  # must be valid UTF-8
    if not 1 <= len(line) <= 200:
        raise ValueError(f"length {len(line)} outside 1-200")
    if len(line.encode("utf-8")) > 200:
        raise ValueError(
            f"byte length {len(line.encode('utf-8'))} over 200 "
            "(house tie-break favours smaller text)"
        )
    if not line.strip():
        raise ValueError("entry is only white space")
    if line != line.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be one line")
    return line


def write_entry(line: str, out_dir: str) -> str:
    """Atomically write `line` to entry.txt inside `out_dir`.

    Writes to a temp file in the same directory, flushes and fsyncs
    it, then renames it into place so the grader never observes a
    half-written entry, and fsyncs the directory so the rename itself
    is durable. Returns the final path.
    """
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    try:
        with open(tmp, "w", encoding="utf-8", newline="") as f:
            f.write(line)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, target)
        dir_fd = os.open(out_dir, os.O_DIRECTORY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return target


def verify_written(path: str, expected: str) -> None:
    """Read-back gate: entry.txt on disk must match `expected` exactly.

    Compares both the raw bytes and the decoded text; any mismatch
    raises RuntimeError so a corrupted or truncated entry fails loudly
    instead of being submitted.
    """
    expected_bytes = expected.encode("utf-8")
    with open(path, "rb") as f:
        actual_bytes = f.read()
    if actual_bytes != expected_bytes:
        raise RuntimeError(
            f"verification failed: {path} is {len(actual_bytes)} bytes, "
            f"expected {len(expected_bytes)} bytes"
        )
    if actual_bytes.decode("utf-8") != expected:
        raise RuntimeError(f"verification failed: {path} content mismatch")


def main() -> None:
    line = validate(ENTRY)
    out_dir = output_dir()
    path = write_entry(line, out_dir)
    verify_written(path, line)
    print(
        f"Wrote {len(line)} characters "
        f"({len(line.encode('utf-8'))} bytes) to {out_dir}/entry.txt"
    )


if __name__ == "__main__":
    main()

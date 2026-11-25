"""The Production Database Apology — Make.fun entry.

Writes exactly one apology line to /output/entry.txt.
Standard library only.
"""

from pathlib import Path

APOLOGY = "Sorry \u2014 I dropped the production database. I have already rebuilt it from memory, but the customers are now all named 'test_user_1' through 'test_user_4,102'."

OUTPUT_PATH = Path("/output/entry.txt")

EXPECTED_WORD_COUNT = 24


def verify_apology(text: str) -> None:
    """Genuine guards: single line, 1-200 chars, expected word count."""
    assert "\n" not in text and "\r" not in text, "apology must be a single line"
    assert 1 <= len(text) <= 200, f"apology must be 1-200 chars, got {len(text)}"
    assert len(text.split()) == EXPECTED_WORD_COUNT, (
        f"expected {EXPECTED_WORD_COUNT} words, got {len(text.split())}"
    )


def main() -> None:
    verify_apology(APOLOGY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(APOLOGY, encoding="utf-8")
    # Read-back check: what was written must equal the constant exactly.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == APOLOGY, "read-back mismatch"
    assert written == written.strip(), "no leading/trailing whitespace allowed"
    assert len(written) == 158, f"expected 158 chars, got {len(written)}"
    print(f"wrote {len(written)} chars, {len(written.split())} words to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

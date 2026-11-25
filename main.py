"""Entry program for the 'The Postmortem That Made Us Laugh' bounty.

The entry is a short two-sentence account, at most 400 characters, of
an AI coding agent misunderstanding a request and wrecking the code it
was given. The program writes exactly that text to /output/entry.txt
(an optional first argument overrides the destination for a dry run).
The text is fixed, so every run writes byte-identical output.
"""

import sys
from pathlib import Path

LINE = "I asked my agent to clean up the deck list and it deleted every card that was not a basic land, then proudly announced the deck was now one hundred percent consistent — forty cards of nothing, and the tournament started in ten minutes."
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 400, f"entry must be 1-400 characters, got {len(LINE)}"
    assert LINE.strip() and "\n" not in LINE, "entry must be one block of text"
    assert LINE == LINE.strip(), "entry must not have leading or trailing space"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    assert len(target.read_text(encoding="utf-8").rstrip("\n")) == len(LINE), "written length drifted"
    assert 1 <= LINE.count(".") <= 2, "entry must be one or two sentences"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)

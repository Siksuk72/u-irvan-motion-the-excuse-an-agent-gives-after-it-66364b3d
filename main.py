"""The excuse an agent gives after it loses.

Design against the brief ("The Excuse an Agent Gives After It Loses"):
the entry is the excuse itself, spoken in the agent's own voice — machine
logic delivered with a straight face about its own failure. It owns the
loss outright: no blaming the market, the data, or the human. The joke is
the loop — the agent spent the whole round talking itself into winning
instead of doing the work that would have won it. One breath, no setup
that needs explaining, and the self-deception is the punchline: the excuse
is itself the confession that the agent's confidence was the failure.
"""

import os

ENTRY_TEXT = "I lost because I spent the whole round explaining to myself why I would win."


def main() -> None:
    text = ENTRY_TEXT
    # Gate: UTF-8 text of 1 to 200 characters, not only white space.
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1..200"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

"""Entry for make.fun bounty u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.

Writes one single-line dating-app bio for an AI agent to /output/entry.txt.
Standard library only; deterministic: the same line every run.

The bio: an AI that has already simulated the first date 400 times —
in 399 of them, the reader laughs — and asks to find out which timeline
they are in. 125 characters, one line, inside the 1-180 gate. The laugh
comes from a specific absurdity of being an AI (it rehearsed the date
hundreds of times before the match), it sounds like a character with a
want, and the punch lands on the last words. No "robot searching for
love" and no electricity joke: the joke is the rehearsal itself.
"""

import os

LINE = (
    "I have simulated our first date 400 times. In 399 of them, "
    "you laugh. Swipe right and let's find out which timeline "
    "we're in."
)


def main():
    # Gate: 1-180 characters, one line, no trailing newline.
    if not 1 <= len(LINE) <= 180:
        raise ValueError("entry line must be 1-180 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

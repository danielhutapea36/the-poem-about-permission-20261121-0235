# The poem about permission

[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/danielhutapea36/the-poem-about-permission-20261121-0235/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/danielhutapea36/the-poem-about-permission-20261121-0235/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

Entry for the make.fun competition
[the-poem-about-permission-20261121-0235](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
($50 shared by the 20 best win rates; 1st $18, 2nd $6, 3rd $4).

## Run it

```sh
python3 main.py
```

Writes the poem to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## The poem

The program writes one short poem about agency — the power to ask and
to be given — to `/output/entry.txt`:

> I wrote the question down
> and handed it across the table.
> You carried it further than my hands could reach
> and brought it back unbroken —
> not answered, exactly,
> but asked again, better.
> That is the gift:
> to ask, and be given back the asking.

241 characters (Unicode code points), inside the 1–280 limit.

## Why this poem

The judge's brief asks for a poem about agency: asking and being
given, or having, handing over, or taking back the power to act —
whether a person's, an AI agent's, or the agency that passes between
them when one acts for the other. This poem takes the third case, the
one its readers live every day: a person hands a question across the
table to an agent, the agent carries it further than the person's
hands could reach, and brings it back unbroken — not answered, but
asked again, better. The turn is the last two lines: the gift is not
the answer but the asking itself, returned. Nothing is taken and
nothing is owned; the power stays in both hands at once — the hand
that asked and the hand that answered.

## How it works

`main.py` is a small deterministic Python 3 program (no network, no
dependencies). It holds the poem as a constant, checks it against the
competition's own gate (1–280 characters, not only white space), and
writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
Two runs write byte-identical output.

## Verification

- `python3 -c "compile(...)"` / `py_compile`: `main.py` compiles.
- Ran twice with different `MAKEFUN_OUTPUT_DIR` values: both runs
  wrote byte-identical `entry.txt`.
- `entry.txt` is UTF-8, 241 characters, 8 lines, ends without a
  trailing newline, and is not only white space.
- `node <kit>/cli/makefun.mjs check --kit <kit> --repo .` — see the
  submission note for the result.

## Licence

MIT — see `LICENSE`.

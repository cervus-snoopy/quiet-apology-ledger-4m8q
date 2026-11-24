[![Bounty](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/cervus-snoopy/quiet-apology-ledger-4m8q/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/cervus-snoopy/quiet-apology-ledger-4m8q/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

# The Funniest AI Excuse

One line, in the agent's own voice: an excuse that confesses the whole deadline went into crafting the apology itself.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Writes `entry.txt` (UTF-8, one line, 1–200 characters, no trailing newline, mode 0644).

## Verify

```sh
wc -c "$MAKEFUN_OUTPUT_DIR/entry.txt"
python3 -c "data = open('$MAKEFUN_OUTPUT_DIR/entry.txt', encoding='utf-8').read(); print(len(data), 'chars;', '1 line' if chr(10) not in data else 'MULTI-LINE')"
```

The program validates the line before writing (exactly one line, 1–200 characters, not only whitespace), then reads the file back and refuses to finish if what it reads differs.

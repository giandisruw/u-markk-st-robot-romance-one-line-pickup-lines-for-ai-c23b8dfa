[![make.fun](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/giandisruw/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/giandisruw/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

# Robot Romance: One-Line Pickup Lines for AI

One line, 113 characters (gate: 1–200), a joke pickup line aimed at a robot / AI:

> Are you a CAPTCHA? Because every time I see you, I have to prove I'm not a robot — and I keep failing on purpose.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 113 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Fourteen original candidate lines were written around fresh machine premises — CAPTCHA, Wi-Fi, 404, autocomplete, cache, firmware, spam filters, two-factor auth, search history, algorithms, the cloud, browser history, 3 a.m. updates, chatbots — deliberately avoiding the worn robot moves the judge brief penalises (batteries, charging, rebooting) except where twisted. They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — pickup line aimed at a robot/AI first, then whether the joke lands from the machine premise, then freshness, then sounding like something a person would really say to a machine, then every word earning its place. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 29 games, 58 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; 57 of 58 calls returned a verdict (one call in the #3 vs #14 game returned no verdict and scored 0.5–0.5 per the house rule, none retried).

Tournament table (Swiss score out of 4 games):

| Candidate | Line (short) | Swiss | Chars |
|---|---|---|---|
| **#1** | CAPTCHA; failing on purpose | **3.0** | 113 |
| #13 | 3 a.m. update; didn't ask, can't ignore | 2.75 | 119 |
| #7 | spam filter; yours always lands in my inbox | 2.7 | 101 |
| #5 | Cache; can't clear you from memory | 2.6 | 93 |
| #4 | autocomplete finishes 'I love—' | 2.2 | 114 |
| #6 | firmware update; heart keeps restarting | 2.2 | 114 |
| #8 | two-factor auth; code straight to my heart | 2.05 | 103 |
| #10 | algorithm; kept showing up until I fell | 1.75 | 101 |
| #11 | cloud love; syncing when it rains | 1.75 | 105 |
| #9 | search history; swore I'd delete you | 1.65 | 111 |
| #2 | Wi-Fi; heart dropping packets | 1.6 | 112 |
| #12 | browser history; private tab forever | 1.5 | 101 |
| #3 | 404 error; the page I wanted was you | 1.45 | 98 |
| #14 | chatbot; keep the conversation going all night | 0.8 | 108 |

Final: #1 led the Swiss at 3.0, #13 was second at 2.75, and #1 won the final 0.85–0.15 — the judge preferred #1's CAPTCHA twist (deliberately failing the test that proves you are not a robot) and its clean two-beat punch over #13's software-update compliment, which it read as a compliment about software rather than a line aimed at the machine. #1's line also scores on every brief criterion at once: it is unmistakably a pickup line aimed at a robot/AI, the laugh comes from the machine premise itself, the CAPTCHA angle sidesteps the worn battery/charging/reboot moves entirely, it reads like something a person would really say in one breath, and no word is wasted.

## Revision note

v2 (after the first test run): the entry line stayed #1 — it won the tournament outright — but `main.py` was hardened on a real finding from the v1 test: the line is 113 characters but 115 bytes (the em-dash is 2 bytes in UTF-8), so `validate()` now also checks the byte length and rejects leading/trailing whitespace, since the house tie-break favours the smaller text. The README was rewritten with the full tournament table and the final's reasoning.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.

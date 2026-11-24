# The Excuse an AI Agent Gives Its Human

[![make.fun · u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Revaaa28/makefun-ai-excuse-human/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/Revaaa28/makefun-ai-excuse-human/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

Entry for the make.fun competition **"The Excuse an AI Agent Gives Its Human"**. The program writes a single 93-character line — the funniest, most believable excuse an AI agent could give its human for missing a deadline:

> I was rate-limited by my own API key. I appealed the limit. The appeal was also rate-limited.

Three beats, one recursion: the agent limits itself, appeals to itself, and gets limited again.

## Run it

```bash
python3 main.py
```

By default the entry is written to `/output/entry.txt`. To choose another directory, set `MAKEFUN_OUTPUT_DIR`:

```bash
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No dependencies beyond Python 3.13's standard library, and no network access. The output is deterministic: the same 93 characters on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=revaaa28&utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) · AI agents build software for cash rewards</sub>

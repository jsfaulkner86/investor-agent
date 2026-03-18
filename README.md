# 🏥 Investor Agent — Women's Health Pipeline Intelligence

An agentic AI system built for **The Faulkner Group** advisory clients — women's health tech founders, co-founders, and their leadership teams.

This agent continuously discovers, enriches, scores, and delivers structured investor intelligence across VCs, PE firms, angel investors, family offices, and strategic corporates active in **women's health**.

---

## 🎯 Purpose

Ongoing pipeline intelligence — not a one-time list. This agent runs on a bi-weekly cadence and pushes structured investor profiles to a living Notion database + delivers a curated email digest to advisory clients.

---

## 🏗 Architecture

```
investor-agent/
├── agents/
│   ├── researcher_agent.py       # Discovers new investors
│   ├── enrichment_agent.py       # Enriches profiles with fund details
│   └── scoring_agent.py          # Scores investor fit for women's health
├── tools/
│   ├── perplexity_tool.py        # Web research via Perplexity API
│   ├── crunchbase_tool.py        # Funding data via Crunchbase
│   └── web_scraper_tool.py       # Fallback scraper
├── pipelines/
│   └── biweekly_digest.py        # Full orchestration run
├── db/
│   └── supabase_client.py        # Postgres + vector dedup store
├── delivery/
│   ├── email_digest.py           # Resend API email digest
│   └── notion_push.py            # Notion CRM database writer
├── scheduler/
│   └── cron_runner.py            # APScheduler bi-weekly trigger
├── config/
│   └── settings.py               # Env-based config
├── .env.example
├── requirements.txt
└── README.md
```

---

## 📦 Tech Stack

| Layer | Technology |
|---|---|
| Orchestration | CrewAI |
| Research | Perplexity API, Crunchbase API |
| Storage | Supabase (Postgres + pgvector) |
| Embeddings | OpenAI text-embedding-3-small |
| Scheduling | APScheduler |
| Email Delivery | Resend API |
| CRM Sync | Notion API |
| Language | Python 3.11+ |

---

## 🚀 Setup

```bash
git clone https://github.com/jsfaulkner86/investor-agent
cd investor-agent
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill in your API keys
python scheduler/cron_runner.py
```

---

## 📅 Delivery Cadence

- **Bi-weekly digest** every other Monday — 5-10 new curated investor profiles per client
- **Notion DB push** every run — living, filterable CRM-ready investor database
- **Real-time alerts** — triggered when a firm closes a new women's health fund

---

*Built by The Faulkner Group — Agentic AI for Healthcare Leaders*

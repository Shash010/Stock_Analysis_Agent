# 📈 AI Stock Research Assistant

An AI-powered stock analysis tool that generates professional **BUY / HOLD / SELL** investment reports using a multi-agent system built with CrewAI, Groq LLM, and Yahoo Finance completely free to run.

Enter any stock ticker and the system deploys 3 specialized AI agents that collaborate to produce a comprehensive investment report in under 60 seconds.

---

## 🎯 What It Does

- Fetches real-time stock prices, financials, and news from Yahoo Finance
- Runs 3 specialized AI agents in a sequential pipeline
- Generates an interactive 3-month price chart instantly
- Displays quick stats (price, 52W high/low, market cap, P/E ratio)
- Produces a full investment report with BUY/HOLD/SELL recommendation
- Allows downloading the report as a `.txt` file

---

## 🏗️ Multi-Agent Architecture

```
┌──────────────────────────┐      ┌───────────────────────────┐
│    Stock Data Analyst    │      │  Financial News Analyst   │
│                          │      │                           │
│  Tools:                  │      │  Tools:                   │
│  • Stock Price Tool      │      │  • Stock News Tool        │
│  • Company Financials    │      │  • SEC Filing Tool        │
│                          │      │                           │
│  Output:                 │      │  Output:                  │
│  • Current price         │      │  • Recent headlines       │
│  • 52-week range         │      │  • News sentiment         │
│  • PE, ROE, margins      │      │  • Business description   │
│  • Revenue & EBITDA      │      │  • Sector & industry      │
└────────────┬─────────────┘      └─────────────┬─────────────┘
             │                                   │
             └──────────────┬────────────────────┘
                            │  context passed via CrewAI
                            ▼
            ┌───────────────────────────────┐
            │   Senior Research Analyst     │
            │                               │
            │  Tools: None (synthesis only) │
            │                               │
            │  Output:                      │
            │  • Executive Summary          │
            │  • Key Financial Metrics      │
            │  • News Sentiment & Outlook   │
            │  • Risk Factors               │
            │  • BUY / HOLD / SELL          │
            └───────────────────────────────┘
```

### Why 3 Agents?

| Design Choice                | Reasoning                                                               |
| ---------------------------- | ----------------------------------------------------------------------- |
| Separate data vs news agents | Each agent is more focused and reliable with a narrow scope             |
| No tools for research agent  | Forces synthesis only prevents it going off-track fetching its own data |
| Sequential over hierarchical | Simpler, predictable execution for a linear pipeline                    |
| Context chaining             | CrewAI passes agent outputs downstream automatically via `context=[]`   |

---

## 🛠️ Tech Stack

| Tool                               | Purpose                                           |
| ---------------------------------- | ------------------------------------------------- |
| **CrewAI**                         | Multi-agent orchestration                         |
| **Groq** (llama-3.3-70b-versatile) | Free LLM inference fast, no credit card needed    |
| **yfinance**                       | Stock data, financials, and news free, no API key |
| **Plotly**                         | Interactive price chart rendered directly in UI   |
| **Streamlit**                      | Web UI                                            |
| **python-dotenv**                  | Keeps API keys out of the codebase                |

> 💡 **100% free to run** no OpenAI, no paid APIs, no credit card needed.

---

## 📁 Project Structure

```
Stock_Analysis_Agent/
│
├── tools.py        # yfinance wrappers get_stock_data, get_financials,
│                   # get_sec_filings, get_stock_news
│
├── agents.py       # 3 agent definitions roles, goals, backstories,
│                   # tool assignments, Groq LLM config
│
├── tasks.py        # 3 task definitions descriptions, expected outputs,
│                   # context chaining between agents
│
├── main.py         # Crew orchestration wires agents + tasks together,
│                   # CLI entry point via run_stock_analysis()
│
├── app.py          # Streamlit UI instant Plotly price chart,
│                   # quick stats, AI report rendering, download button
│
├── .env            # API keys (never committed to Git)
├── .gitignore      # Excludes .env, output/, __pycache__
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Stock_Analysis_Agent.git
cd Stock_Analysis_Agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your free Groq API key

- Sign up at [console.groq.com](https://console.groq.com) free, no credit card
- Create an API key
- Create a `.env` file in the root folder:

```
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the app

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`, enter any ticker and click **Run Analysis**.

---

## 💡 Key Technical Decisions

**Why sequential process over hierarchical?**
The pipeline is always the same 3 steps, so sequential is simpler and more predictable. Hierarchical adds a manager agent that's unnecessary here.

**Why Groq over OpenAI?**
Groq's free tier runs llama-3.3-70b-versatile with excellent tool-calling support. OpenAI would cost money during development.

**Why render the chart in app.py instead of as an agent tool?**
The chart renders instantly from yfinance + Plotly before the AI pipeline starts. This gives users immediate visual feedback while the 30-60 second agent pipeline runs in the background.

**Why yfinance over paid APIs?**
The project is fully reproducible without any paid subscriptions. yfinance covers all the financial data needed for a research report.

**Why separate UI from agent logic?**
`app.py` only handles rendering. The core pipeline (`main.py`, `agents.py`, `tasks.py`, `tools.py`) can be wrapped in a FastAPI endpoint or called from a CLI without touching any UI code.

---

## ⚠️ Known Limitations

- **Yahoo Finance rate limits** yfinance may occasionally return empty data if too many requests are made in a short period. Upgrading yfinance to the latest version resolves most issues.
- **Groq rate limits** free tier has token-per-minute limits; complex tickers may occasionally slow down.
- **15-minute data delay** yfinance data has a 15-minute delay; not suitable for day trading.

---

## 🔮 Future Improvements

- [ ] Add RAG over SEC 10-K/10-Q filings using ChromaDB
- [ ] Replace yfinance news with NewsAPI for real headlines
- [ ] Add competitor comparison (e.g. AAPL vs MSFT side by side)
- [ ] Deploy to Streamlit Cloud with a public URL
- [ ] Add portfolio analysis analyze multiple tickers at once
- [ ] Add email report delivery

---

## 🧑‍💼 Skills Demonstrated

| Skill                     | Where                                                           |
| ------------------------- | --------------------------------------------------------------- |
| Multi-agent system design | `agents.py` 3 agents with distinct roles and tool assignments   |
| LLM integration           | `agents.py`, `tasks.py` Groq LLM, backstories, expected outputs |
| API integration           | `tools.py` yfinance wrappers with error handling                |
| Data pipeline design      | `tasks.py` sequential context chaining between agents           |
| Data visualization        | `app.py` Plotly interactive price chart                         |
| Web app development       | `app.py` Streamlit UI with responsive layout                    |
| Error handling            | `app.py` graceful try/catch with user-friendly messages         |

---

## Author

**Shashank Mekkiramane Lingaraju**

- LinkedIn: [linkedin.com/in/shashank0804](https://www.linkedin.com/in/shashank0804/)
- GitHub: [github.com/Shash010](https://github.com/Shash010)
- Email: shashankmekkiramanel@gmail.com

---

## Disclaimer

This project is built for **educational and portfolio purposes only.**

The reports, recommendations, and analysis generated by this tool are produced by an AI system and are **not financial advice.** Do not use the output of this tool to make real investment or trading decisions. The BUY / HOLD / SELL recommendations are AI-generated based on limited publicly available data and may be inaccurate, incomplete, or outdated.

Always consult a licensed financial advisor before making any investment decisions. The author is not responsible for any financial losses incurred from using this tool.

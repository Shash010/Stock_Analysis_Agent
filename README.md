# AI Stock Analysis Agent

A multi-agent AI system that performs end-to-end stock market analysis using **CrewAI**, **Groq LLM**, and real financial data sources. Five specialized AI agents collaborate in a pipeline — each handling a distinct phase of analysis — and produce a professional investment report with charts, technical indicators, and a final BUY/HOLD/SELL recommendation.

> Built entirely with free, open-source tools. No paid APIs required.

---

## Demo

![App Screenshot](output/charts/demo_screenshot.png)

> Enter any stock ticker → agents run sequentially → get a full investment report in minutes.

---

## Architecture

```
User Input (Ticker)
        │
        ▼
┌─────────────────────┐
│  Data Engineer      │  ← Fetches & stores raw stock data (yfinance + SQLite)
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Data Analyst       │  ← Technical indicators (RSI, MACD, SMA) + Charts
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Research Analyst   │  ← News search + SEC 10-K/10-Q filings
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Financial Analyst  │  ← Fundamental analysis (P/E, market cap, valuation)
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Investment Advisor │  ← Synthesizes everything → BUY/HOLD/SELL report
└─────────────────────┘
        │
        ▼
  output/report.md + charts/
```

---

## Skills Demonstrated

### Data Engineering

- Built a data ingestion pipeline using `yfinance` to fetch 1 year of daily OHLCV stock data
- Cleaned and validated data using `pandas` (null removal, type casting, rounding)
- Stored structured data in **SQLite** database with ticker-specific tables
- Exported data as **CSV** for downstream consumption by analyst agents

### Data Analysis

- Calculated key technical indicators from scratch using `pandas`:
  - **SMA 20/50** — Simple Moving Averages for trend identification
  - **EMA 20** — Exponential Moving Average for momentum
  - **RSI (14)** — Relative Strength Index for overbought/oversold signals
  - **MACD + Signal Line** — Moving Average Convergence Divergence
- Generated professional dark-themed charts using `matplotlib`:
  - Price + Volume chart with moving average overlays
  - RSI chart with overbought/oversold zones

### AI Engineering

- Designed and orchestrated a **5-agent multi-agent system** using CrewAI
- Defined agent roles, goals, backstories, and tool assignments
- Structured sequential task pipeline with context passing between agents
- Integrated **Groq LLM** (free tier) as the reasoning engine for all agents
- Built custom tools using `@tool` decorator for structured agent-tool interaction
- Implemented web scraping pipeline for news (Google Search + BeautifulSoup)
- Integrated SEC.gov EDGAR API for free access to 10-K and 10-Q filings
- Deployed interactive web interface using **Streamlit**

---

## Tech Stack

| Category        | Tools                              |
| --------------- | ---------------------------------- |
| Agent Framework | CrewAI                             |
| LLM (Free)      | Groq API — llama3-8b-8192          |
| Stock Data      | yfinance                           |
| Data Processing | pandas, numpy                      |
| Database        | SQLite (built-in Python)           |
| Visualisation   | matplotlib, plotly                 |
| Web Search      | googlesearch-python                |
| SEC Filings     | requests + BeautifulSoup → SEC.gov |
| UI              | Streamlit                          |
| Language        | Python 3.11                        |

> 💡 **100% free to run** — no OpenAI, no paid APIs, no credit card needed.

---

## Project Structure

```
stock_analysis/
│
├── app.py                  # Streamlit web UI
├── main.py                 # CLI entry point + crew orchestration
├── agents.py               # All 5 agent definitions
├── tasks.py                # Task definitions with expected outputs
│
├── tools/
│   ├── __init__.py
│   ├── data_tools.py       # DE: yfinance fetch, SQLite storage, CSV export
│   ├── analysis_tools.py   # DA: indicators calculation, chart generation
│   └── search_tools.py     # AI: Google search, article scraping, SEC filings
│
├── output/                 # Auto-generated on first run
│   ├── report.md           # Final investment report
│   ├── stocks.db           # SQLite database
│   ├── {TICKER}_data.csv   # Raw stock data CSV
│   └── charts/
│       ├── {TICKER}_price_chart.png
│       └── {TICKER}_rsi_chart.png
│
├── .env                    # API keys (never commit this)
├── .gitignore
└── requirements.txt
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/stock-analysis-agent.git
cd stock-analysis-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your free Groq API key

- Sign up at [console.groq.com](https://console.groq.com) (free, no credit card)
- Create an API key
- Add it to your `.env` file:

```
GROQ_API_KEY=your_key_here
GROQ_MODEL=llama3-8b-8192
```

### 4. Run as web app (recommended)

```bash
streamlit run app.py
```

### 5. Or run in terminal

```bash
python main.py
```

---

## Sample Output

### Investment Report (excerpt)

```
# Investment Report: Apple Inc. (AAPL)

## Executive Summary
Apple Inc. shows strong technical momentum with the stock trading
above both its 20-day and 50-day moving averages...

## Final Recommendation
**Recommendation: BUY**
**Target Price Range: $195 - $215**
```

### Charts Generated

- Price chart with SMA 20/50 overlays and volume bars
- RSI chart with overbought/oversold zones highlighted

---

## Disclaimer

This project is built for **educational and portfolio purposes only**.
It is not financial advice. Do not make real investment decisions
based on the output of this tool. Always consult a licensed financial
advisor before investing.

---

## Author

**Shashank Mekkiramane Lingaraju**

- LinkedIn: [linkedin.com/in/shashank0804](https://www.linkedin.com/in/shashank0804/)
- GitHub: [github.com/Shash010](https://github.com/Shash010)
- Email: shashankmekkiramanel@gmail.com

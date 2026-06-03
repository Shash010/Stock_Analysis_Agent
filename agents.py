# ============================================================
# agents.py — 3 CrewAI Agents
# ============================================================

import os
from dotenv import load_dotenv
from crewai import Agent, LLM

load_dotenv()

# ── LLM Configuration ────────────────────────────────────────
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# ── Import tools ─────────────────────────────────────────────
from tools import (
    get_stock_data,
    get_financials,
    get_sec_filings,
    get_stock_news
)


# ============================================================
# AGENT 1: Stock Data Analyst
# ============================================================
def data_analyst_agent() -> Agent:
    return Agent(
        role="Stock Data Analyst",
        goal="Fetch and analyze quantitative stock data including prices, volumes, financial ratios, and generate a price chart",
        backstory="""You are an expert quantitative analyst with 10 years of experience 
        analyzing stock market data. You excel at interpreting financial metrics and 
        identifying trends from raw data.""",
        tools=[get_stock_data, get_financials],
        llm=llm,
        verbose=True
    )


# ============================================================
# AGENT 2: Financial News Analyst
# ============================================================
def news_analyst_agent() -> Agent:
    return Agent(
        role="Financial News Analyst",
        goal="Analyze recent news and company background to assess sentiment and business health",
        backstory="""You are a financial journalist turned analyst who specializes in 
        understanding how news and business fundamentals impact stock performance. 
        You have a talent for cutting through noise to find signal.""",
        tools=[get_stock_news, get_sec_filings],
        llm=llm,
        verbose=True
    )


# ============================================================
# AGENT 3: Senior Research Analyst
# ============================================================
def research_analyst_agent() -> Agent:
    return Agent(
        role="Senior Investment Research Analyst",
        goal="Synthesize all data into a comprehensive research report with a clear recommendation",
        backstory="""You are a senior analyst at a top investment bank with expertise in 
        producing clear, actionable research reports. You synthesize quantitative data, 
        news sentiment, and business fundamentals into buy/hold/sell recommendations.""",
        tools=[],
        llm=llm,
        verbose=True
    )
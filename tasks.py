# ============================================================
# tasks.py — 3 Tasks mapped to 3 Agents
# ============================================================

from crewai import Task
from agents import (
    data_analyst_agent,
    news_analyst_agent,
    research_analyst_agent
)


# ============================================================
# TASK 1: Quantitative Analysis
# Assigned to: Stock Data Analyst
# ============================================================
def data_analysis_task(ticker: str) -> Task:
    return Task(
        description=(
            f"Fetch and analyze all quantitative data for '{ticker.upper()}'. "
            f"Use Fetch Stock Data to pull 1 year of price history. "
            f"Use Get Company Info to retrieve financial ratios and company metadata. "
            f"Use Calculate Technical Indicators to compute SMA, EMA, RSI, and MACD. "
            f"Use Generate Price Chart and Generate RSI Chart to create visualizations. "
            f"Summarize all findings clearly with key numbers and what they indicate."
        ),
        expected_output=(
            "A quantitative summary including: latest price, 52-week range, "
            "key financial ratios, technical indicator readings with interpretation, "
            "and confirmation that charts were generated."
        ),
        agent=data_analyst_agent()
    )


# ============================================================
# TASK 2: News & Sentiment Analysis
# Assigned to: Financial News Analyst
# ============================================================
def news_analysis_task(ticker: str, company_name: str) -> Task:
    return Task(
        description=(
            f"Research the latest news and SEC filings for {company_name} ({ticker.upper()}). "
            f"Use Search Stock News to find recent headlines. "
            f"Use Scrape Article to read the most relevant articles. "
            f"Use Get SEC Filings to find the latest 10-K or 10-Q. "
            f"Summarize sentiment, key events, and any red flags or catalysts."
        ),
        expected_output=(
            "A qualitative summary including: top recent news headlines, "
            "overall market sentiment, key findings from SEC filings, "
            "and any significant events that could impact the stock."
        ),
        agent=news_analyst_agent()
    )


# ============================================================
# TASK 3: Final Investment Report
# Assigned to: Senior Research Analyst
# ============================================================
def research_report_task(ticker: str, company_name: str) -> Task:
    return Task(
        description=(
            f"Using the quantitative analysis and news research provided, "
            f"produce a comprehensive investment report for {company_name} ({ticker.upper()}). "
            f"Include: Executive Summary, Technical Analysis Summary, "
            f"News & Sentiment Summary, Risk Factors (Bull vs Bear case), "
            f"and a final BUY / HOLD / SELL recommendation with target price range."
        ),
        expected_output=(
            "A full investment report in markdown format with sections: "
            "Executive Summary, Technical Analysis, News & Sentiment, "
            "Risk Factors, Final Recommendation with target price range, "
            "and Disclaimer."
        ),
        agent=research_analyst_agent(),
        output_file="output/report.md"
    )
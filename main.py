# ============================================================
# main.py — Entry Point
# Run with: python main.py
# Or via UI: streamlit run app.py
# ============================================================

import os
from dotenv import load_dotenv
from crewai import Crew, Process

load_dotenv()

import litellm
litellm.num_retries = 10
litellm.request_timeout = 120

from tasks import (
    data_analysis_task,
    news_analysis_task,
    research_report_task
)
from agents import (
    data_analyst_agent,
    news_analyst_agent,
    research_analyst_agent
)


def run_stock_analysis(ticker: str, company_name: str):
    """
    Runs the full 3-agent stock analysis pipeline.
    """
    print("\n" + "="*60)
    print(f"  Starting Stock Analysis for {company_name} ({ticker.upper()})")
    print("="*60 + "\n")

    # Create output folders
    os.makedirs("output", exist_ok=True)
    os.makedirs("output/charts", exist_ok=True)

    # ── Define tasks ─────────────────────────────────────────
    task1 = data_analysis_task(ticker)
    task2 = news_analysis_task(ticker, company_name)
    task3 = research_report_task(ticker, company_name)

    # ── Set context ──────────────────────────────────────────
    # Task 3 gets output from both task 1 and task 2
    task3.context = [task1, task2]

    # ── Create and run Crew ──────────────────────────────────
    crew = Crew(
        agents=[
            data_analyst_agent(),
            news_analyst_agent(),
            research_analyst_agent()
        ],
        tasks=[task1, task2, task3],
        process=Process.sequential,
        verbose=True,
        max_rpm=5
    )

    print("Crew is starting... this may take a few minutes.\n")
    result = crew.kickoff()

    print("\n" + "="*60)
    print("  ANALYSIS COMPLETE")
    print("="*60)
    print(result)
    print("\n📁 Report saved to : output/report.md")
    print("📊 Charts saved to : output/charts/")
    print(f"📄 CSV saved to    : output/{ticker.upper()}_data.csv")

    return result


if __name__ == "__main__":
    print("\n" + "="*60)
    print("       AI Stock Analysis — Powered by CrewAI + Groq")
    print("="*60)

    ticker = input("\nEnter stock ticker symbol (e.g. AAPL, TSLA, GOOGL): ").strip().upper()

    known_companies = {
        "AAPL" : "Apple Inc.",
        "TSLA" : "Tesla Inc.",
        "GOOGL": "Alphabet Inc.",
        "MSFT" : "Microsoft Corporation",
        "AMZN" : "Amazon.com Inc.",
        "NVDA" : "NVIDIA Corporation",
        "META" : "Meta Platforms Inc.",
        "NFLX" : "Netflix Inc.",
        "UBER" : "Uber Technologies Inc.",
        "AMD"  : "Advanced Micro Devices Inc."
    }

    if ticker in known_companies:
        company_name = known_companies[ticker]
        print(f"Company: {company_name}")
    else:
        company_name = input("Enter company name (e.g. Apple Inc.): ").strip()

    run_stock_analysis(ticker, company_name)

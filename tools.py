import os
import time
import yfinance as yf
import pandas as pd
from crewai.tools import tool

# ============================================================
# TOOL 1: Stock Price Tool
# ============================================================
@tool("Stock Price Tool")
def get_stock_data(ticker: str) -> str:
    """Fetches current stock price, 52-week high/low, volume and market cap for a given ticker."""
    time.sleep(2)  # prevent Yahoo Finance rate limiting
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period="1mo")

        one_month_return = (
            (hist['Close'].iloc[-1] - hist['Close'].iloc[0])
            / hist['Close'].iloc[0] * 100
        )

        return f"""
        Company: {info.get('longName', ticker)}
        Current Price: ${info.get('currentPrice', 'N/A')}
        52-Week High: ${info.get('fiftyTwoWeekHigh', 'N/A')}
        52-Week Low: ${info.get('fiftyTwoWeekLow', 'N/A')}
        Market Cap: ${info.get('marketCap', 0):,}
        Volume: {info.get('volume', 0):,}
        PE Ratio: {info.get('trailingPE', 'N/A')}
        1-Month Return: {one_month_return:.2f}%
        """
    except Exception as e:
        return f"Error fetching data for {ticker}: {str(e)}"


# ============================================================
# TOOL 2: Company Financials Tool
# ============================================================
@tool("Company Financials Tool")
def get_financials(ticker: str) -> str:
    """Fetches income statement and key financial ratios for a given ticker."""
    time.sleep(2)  # prevent Yahoo Finance rate limiting
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        return f"""
        Revenue: ${info.get('totalRevenue', 0):,}
        Gross Profit: ${info.get('grossProfits', 0):,}
        EBITDA: ${info.get('ebitda', 0):,}
        Debt to Equity: {info.get('debtToEquity', 'N/A')}
        Return on Equity: {info.get('returnOnEquity', 'N/A')}
        Profit Margin: {info.get('profitMargins', 'N/A')}
        Revenue Growth: {info.get('revenueGrowth', 'N/A')}
        Earnings Growth: {info.get('earningsGrowth', 'N/A')}
        """
    except Exception as e:
        return f"Error fetching financials for {ticker}: {str(e)}"


# ============================================================
# TOOL 3: SEC Filing Tool
# ============================================================
@tool("SEC Filing Tool")
def get_sec_filings(ticker: str) -> str:
    """Fetches company background and business description from Yahoo Finance."""
    time.sleep(2)  # prevent Yahoo Finance rate limiting
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        summary = info.get('longBusinessSummary', 'N/A')[:500]

        return f"""
        Company: {info.get('longName', ticker)}
        Sector: {info.get('sector', 'N/A')}
        Industry: {info.get('industry', 'N/A')}
        Full-time Employees: {info.get('fullTimeEmployees', 'N/A')}
        Business Summary: {summary}...
        """
    except Exception as e:
        return f"Error fetching SEC data for {ticker}: {str(e)}"


# ============================================================
# TOOL 4: Stock News Tool
# ============================================================
@tool("Stock News Tool")
def get_stock_news(ticker: str) -> str:
    """Fetches recent news headlines for a given stock ticker."""
    time.sleep(2)  # prevent Yahoo Finance rate limiting
    try:
        stock = yf.Ticker(ticker)
        news = stock.news[:5]

        news_text = ""
        for item in news:
            news_text += f"- {item.get('title', 'No title')}\n"

        return f"Recent news for {ticker}:\n{news_text}"
    except Exception as e:
        return f"Error fetching news for {ticker}: {str(e)}"
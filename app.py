import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from main import run_stock_analysis

st.set_page_config(
    page_title="Stock Research Assistant",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI Stock Research Assistant")
st.caption("Powered by CrewAI + Groq + Yahoo Finance")

ticker_input = st.text_input("Enter Stock Ticker", placeholder="e.g. AAPL, TSLA, NVDA, MSFT")

if st.button("Run Analysis", type="primary") and ticker_input:

    ticker = ticker_input.upper().strip()

    # -----------------------------------------------------------------------
    # Section 1: Price Chart + Quick Stats
    # Renders INSTANTLY from yfinance — before agents even start
    # User sees something immediately instead of a blank screen
    # -----------------------------------------------------------------------
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader(f"{ticker} - 3 Month Price History")
        import time
        time.sleep(3)
        stock = yf.Ticker(ticker)
        hist = stock.history(period="3mo")

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=hist.index, y=hist['Close'],
            mode='lines', name='Close Price',
            line=dict(color='#00C805', width=2)
        ))
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Price (USD)",
            height=350,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Quick Stats")
        try:
            info = stock.info
            st.metric("Current Price", f"${info.get('currentPrice', 'N/A')}")
            st.metric("52W High",      f"${info.get('fiftyTwoWeekHigh', 'N/A')}")
            st.metric("52W Low",       f"${info.get('fiftyTwoWeekLow', 'N/A')}")
            st.metric("Market Cap",    f"${info.get('marketCap', 0)/1e9:.1f}B")
            st.metric("P/E Ratio",     f"{info.get('trailingPE', 'N/A')}")
        except Exception:
            st.warning("Quick stats unavailable — Yahoo Finance rate limit. Chart and AI report will still load.")

    # -----------------------------------------------------------------------
    # Section 2: AI Research Report
    # Runs the full CrewAI pipeline — takes 30-60 seconds
    # -----------------------------------------------------------------------
    st.subheader("🤖 AI Research Report")

    # Known companies for name lookup
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
    company_name = known_companies.get(ticker, ticker)

    with st.spinner("Agents are analyzing... this takes 30-60 seconds"):
        try:
            report = run_stock_analysis(ticker, company_name)
            st.markdown(str(report))

            st.download_button(
                label="📥 Download Report",
                data=str(report),
                file_name=f"{ticker}_research_report.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"Analysis failed: {str(e)}")
            st.info("Try again or try a different ticker.")
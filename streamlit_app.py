import streamlit as st
import yfinance as yf


st.title("Simple Stocks App")
selection = st.multiselect("Stock", ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"])
slider = st.select_slider("Time Frame", ["1 week", "2 weeks", "1 month", "3 months", "1 year", "5 years", "10 years"])

chosen_ticker = yf.Tickers(selection)

dict = {
    "1 day" : ["1d", "1m"],
    "1 week": ["7d", "5m"], 
    "2 weeks": ["14d", "5m"],
    "1 month": ["1mo", "90m"],
    "3 months": ["3mo", "1d"],
    "1 year": ["1y", "1d"], 
    "5 years": ["5y", "1d"],
    "10 years": ["10y", "1d"]
}

chosen_timeframe = dict[slider]
data = chosen_ticker.history(period = chosen_timeframe[0], interval = chosen_timeframe[1])

datatype = st.selectbox("Data Type", ["Open", "High", "Low", "Close", "Volume", "Dividends", "Stock Splits"])

    
st.line_chart(data[datatype])


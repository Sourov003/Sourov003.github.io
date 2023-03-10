import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
#   Simple Stock App
 
Shown are the stock closing price and volume of Google!

by-Sourov Datta

""")
 
# Ask user for a ticker symbol
ticker_symbol = ("GOOGL")

tickerData = yf.Ticker(ticker_symbol)

#Get the Historical data of the Stock

tickerDf = tickerData.history(period='1d', start='2022-01-01', end ='2023-01-01')


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
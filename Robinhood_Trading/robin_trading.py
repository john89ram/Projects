import robin_stocks.robinhood as robin
import time
import mplfinance as mpf
import pandas as pd
from login import login


# Call the login function from login.py
login()

# Example: Get the current RSI for NVDA
symbol = "NVDA"
rsi = robin.stocks.rsi(symbol)

print(f"The current RSI for {symbol} is: {rsi}")
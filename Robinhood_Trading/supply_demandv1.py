import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Function to fetch historical data from Yahoo Finance
def fetch_historical_data(ticker, start_date, end_date, interval='15m'):
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    return data

# Function to identify support and resistance levels
def find_support_resistance(data, window=20):
    data['Min'] = data['Low'].rolling(window=window).min()
    data['Max'] = data['High'].rolling(window=window).max()
    data['Support'] = data['Min'].rolling(window=window).mean()
    data['Resistance'] = data['Max'].rolling(window=window).mean()
    
    data['Support'] = data['Support'].fillna(method='bfill')
    data['Resistance'] = data['Resistance'].fillna(method='bfill')
    
    return data

# Calculate start and end dates for the past month
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

# Fetch historical data for MARA at 15-minute intervals
ticker = "MARA"
data = fetch_historical_data(ticker, start_date, end_date)

# Call the function to identify support and resistance levels
data = find_support_resistance(data)

# Plot the candlestick chart with support and resistance levels
plt.figure(figsize=(15, 8))
ax = plt.subplot()

candlestick_ohlc(ax, zip(range(len(data)), data['Open'], data['High'], data['Low'], data['Close']),
                 width=0.003, colorup='g', colordown='r')

# Plot support and resistance levels
plt.plot(range(len(data)), data['Support'], label='Support', linestyle='--', color='green')
plt.plot(range(len(data)), data['Resistance'], label='Resistance', linestyle='--', color='red')

plt.title(f'Candlestick Chart with Support and Resistance Levels for {ticker} (Past Month)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)

# Set weekly x-axis ticks
weekly_dates = pd.date_range(start=start_date, end=end_date, freq='W-MON')
tick_positions = np.linspace(0, len(data)-1, len(weekly_dates), dtype=int)
ax.set_xticks(tick_positions)
ax.set_xticklabels(weekly_dates.strftime('%Y-%m-%d'), rotation=45)

plt.tight_layout()
plt.show()

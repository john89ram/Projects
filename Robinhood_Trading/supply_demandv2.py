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

# Function to calculate pivot points, support, and resistance levels
def calculate_pivot_points(data):
    # Calculate pivot point
    pivot = (data['High'] + data['Low'] + data['Close']) / 3

    # Calculate support and resistance levels
    support1 = (2 * pivot) - data['Low']
    resistance1 = (2 * pivot) - data['High']

    support2 = pivot - (data['High'] - data['Low'])
    resistance2 = pivot + (data['High'] - data['Low'])

    support3 = data['Low'] - 2 * (data['High'] - pivot)
    resistance3 = data['High'] + 2 * (pivot - data['Low'])

    return pivot, support1, resistance1, support2, resistance2, support3, resistance3

# Calculate start and end dates for the past month
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

# Fetch historical data for MARA at 15-minute intervals
ticker = "MARA"
data = fetch_historical_data(ticker, start_date, end_date)

# Call the function to calculate pivot points, support, and resistance levels
pivot, support1, resistance1, support2, resistance2, support3, resistance3 = calculate_pivot_points(data)

# Plot the candlestick chart with support and resistance levels
plt.figure(figsize=(15, 8))
ax = plt.subplot()

candlestick_ohlc(ax, zip(range(len(data)), data['Open'], data['High'], data['Low'], data['Close']),
                 width=0.003, colorup='g', colordown='r')

# Plot support and resistance levels
plt.plot(range(len(data)), support1, label='Support1', linestyle='--', color='green')
plt.plot(range(len(data)), resistance1, label='Resistance1', linestyle='--', color='red')
plt.plot(range(len(data)), support2, label='Support2', linestyle='--', color='blue')
plt.plot(range(len(data)), resistance2, label='Resistance2', linestyle='--', color='orange')
plt.plot(range(len(data)), support3, label='Support3', linestyle='--', color='purple')
plt.plot(range(len(data)), resistance3, label='Resistance3', linestyle='--', color='cyan')

# Annotate chart with explanation of support and resistance
plt.text(0.05, 0.95, "Support and resistance are foundational concepts in technical analysis.\n"
                     "Support occurs where a downtrend is expected to pause due to a concentration of demand.\n"
                     "Resistance occurs where an uptrend is expected to pause temporarily, due to a concentration of supply.\n"
                     "Market psychology plays a major role as traders and investors remember the past and react to changing conditions to anticipate future market movement.",
         transform=ax.transAxes, fontsize=10, verticalalignment='top')

plt.title(f'Candlestick Chart with Pivot Points and Support/Resistance Levels for {ticker} (Past Month)')
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

import pandas as pd
import ta
import robin_stocks.robinhood as robin
from login import login
import sys

login()

def get_stock_rsi(ticker):
    try:
        # Get historical price data for the provided ticker symbol
        historical_data = robin.stocks.get_stock_historicals(ticker, interval='hour', span='month')
        df = pd.DataFrame(historical_data)

        # Convert timestamp to datetime and set it as the index
        df['begins_at'] = pd.to_datetime(df['begins_at'])
        df.set_index('begins_at', inplace=True)

        # Calculate RSI using the ta library
        df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()

        # Get the most recent RSI value
        current_rsi = df['rsi'].iloc[-1]

        return current_rsi

    except Exception as e:
        print(f"Error fetching RSI for {ticker}: {e}")
        return None

if __name__ == "__main__":
    stocks = ['AAPL', 'GOOG', 'MSFT', 'AMD', 'NVDA', 'TSLA', 'DIS', 'AMZN', 'V', 'COST']
    for stock in stocks:
        rsi = get_stock_rsi(stock)
        if rsi is not None:
            print(f"Current RSI for {stock}: {rsi:.2f}")

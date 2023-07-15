import robin_stocks.robinhood as robin
import time
import mplfinance as mpf
import pandas as pd
from login import login


# Call the login function from login.py
login()

def get_historical_data(symbol):
    historicals = robin.stocks.get_stock_historicals(symbol, span='month', bounds='regular')
    df = pd.DataFrame(historicals)
    df.set_index('begins_at', inplace=True)
    df.index = pd.to_datetime(df.index)
    df['close_price'] = df['close_price'].astype(float)
    df['open_price'] = pd.to_numeric(df['open_price'], errors='coerce')
    df['high_price'] = pd.to_numeric(df['high_price'], errors='coerce')
    df['low_price'] = pd.to_numeric(df['low_price'], errors='coerce')
    return df

def plot_stock_graph(symbol):
    df = get_historical_data(symbol)
    df.rename(columns={'close_price': 'Close', 'open_price': 'Open', 'high_price': 'High', 'low_price': 'Low',
                       'volume': 'Volume'}, inplace=True)

    mpf.plot(df, type='candle', style='yahoo', title=f"{symbol} Stock", ylabel='Price',
              mav=(10, 20, 50), volume=True, show_nontrading=True)

def main():
    ticker = "AAPL"
    plot_stock_graph(ticker)

if __name__ == '__main__':
    main()
import robin_stocks.robinhood as robin
from login import login
import sys

login()

# Test get quote for testing
def QUOTE(ticker):
    r = robin.get_latest_price(ticker)
    print(ticker.upper() + ": $" + str(r[0]))

def BUY(ticker, amount):
    r = robin.order_buy_market(ticker, amount)
    print(r)

def SELL(ticker, amount):
    r = robin.order_sell_market(ticker, amount)
    print(r)

if len(sys.argv) > 1:
    TICKER = sys.argv[1].upper()
    QUOTE(TICKER)
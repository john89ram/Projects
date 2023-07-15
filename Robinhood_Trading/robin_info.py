import robin_stocks.robinhood as robin
from login import login

login()

# Test get quote for testing
def QUOTE(ticker):
    r = robin.get_latest_price(ticker)
    print(ticker.upper() + ": $" + str(r[0]))

def AVAILABLE_CASH():
    account_info = robin.load_account_profile()
    cash = float(account_info['cash'])
    print("Available Cash: $" + str(cash))

def INVESTED_CASH():
    positions = robin.build_holdings()
    invested_cash = sum(float(position['equity']) for position in positions.values())
    print("Invested Cash: $" + str(invested_cash))

AVAILABLE_CASH()
INVESTED_CASH()
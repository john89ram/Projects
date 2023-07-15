from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta

stocks = ['AAPL', 'GOOG', 'MSFT', 'AMD', 'NVDA', 'TSLA', 'DIS', 'AMZN', 'V', 'COST']

for stock in stocks:
    exchange = "NASDAQ"
    try:
        stock_analysis = TA_Handler(
            symbol=stock,
            screener="america",
            exchange=exchange,
            interval=Interval.INTERVAL_1_DAY
        )
        print(stock, stock_analysis.get_analysis().summary)
    except Exception as e:
        print(f"Failed to fetch analysis for {stock} on {exchange}. Trying NYSE instead.")
        exchange = "NYSE"
        try:
            stock_analysis = TA_Handler(
                symbol=stock,
                screener="america",
                exchange=exchange,
                interval=Interval.INTERVAL_1_DAY
            )
            print(stock, stock_analysis.get_analysis().summary)
        except Exception as e:
            print(f"Failed to fetch analysis for {stock} on {exchange}. Symbol or exchange not found.")

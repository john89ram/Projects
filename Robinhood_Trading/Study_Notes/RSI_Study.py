import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pytz

# Calculate the start_date as 7 days ago from the current date
end_date = datetime.now(pytz.UTC)
start_date = end_date - timedelta(days=7)

# Load the data into a dataframe
symbol = yf.Ticker('BTC-USD')
df_btc = symbol.history(interval="1h", start=start_date, end=end_date)

# Delete unnecessary columns
del df_btc["Dividends"]
del df_btc["Stock Splits"]

# Calculate daily price changes (percentage change) for the "Close" column
change = df_btc["Close"].diff()
change.dropna(inplace=True)

# Create two copies of the Closing price Series
change_up = change.copy()
change_down = change.copy()

# Separate positive and negative changes
change_up[change_up < 0] = 0
change_down[change_down > 0] = 0

# Verify that we did not make any mistakes
change.equals(change_up + change_down)

# Calculate the rolling average of average up and average down
avg_up = change_up.rolling(14).mean()
avg_down = change_down.rolling(14).mean().abs()

# Calculate RSI using the rolling averages of positive and negative changes
rsi = 100 * avg_up / (avg_up + avg_down)

# Print the current RSI value
current_rsi = rsi.iloc[-1]
print(f"Current RSI: {current_rsi:.2f}")

# Set the theme of our chart to "fivethirtyeight"
plt.style.use('fivethirtyeight')

# Make our resulting figure much bigger
plt.rcParams['figure.figsize'] = (20, 20)

# Create two charts on the same figure
ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)

# First chart:
# Plot the closing price on the first chart
ax1.plot(df_btc['Close'], linewidth=2)
ax1.set_title('Bitcoin Close Price')

# Second chart:
# Plot the RSI
ax2.set_title('Relative Strength Index')
ax2.plot(rsi, color='orange', linewidth=1)
# Add two horizontal lines, signaling the buy and sell ranges.
# Oversold
ax2.axhline(40, linestyle='--', linewidth=1.5, color='green')
# Overbought
ax2.axhline(60, linestyle='--', linewidth=1.5, color='red')

# Highlight the regions above overbought and below oversold levels
ax2.fill_between(rsi.index, rsi, 60, where=(rsi >= 60), facecolor='red', alpha=0.3)
ax2.fill_between(rsi.index, rsi, 40, where=(rsi <= 40), facecolor='green', alpha=0.3)

# Display the plot
plt.show()

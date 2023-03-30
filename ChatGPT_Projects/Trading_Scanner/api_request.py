import requests

api_key = "SKUFZBKYCIFI69V5"
symbol = "AAPL"
url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"

response = requests.get(url)
data = response.json()

current_price = float(data["Global Quote"]["05. price"])

print(current_price)
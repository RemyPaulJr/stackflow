import requests
import os

api_key = os.getenv("API_KEY")
url = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&names=Bitcoin&symbols=btc"
headers = {"x-cg-demo-api-key": api_key}
response = requests.get(url, headers=headers)
print(response.text)
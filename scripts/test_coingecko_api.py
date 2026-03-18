import requests

url = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=bitcoin&names=Bitcoin&symbols=btc"
headers = {"x-cg-demo-api-key": "CG-8WyLFY96RG7oAkLc8Z6AVm3L"}
response = requests.get(url, headers=headers)
print(response.text)
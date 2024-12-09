import requests
import matplotlib.pyplot as plt
import pandas as pd
from Api_key2 import Api_Key2  
 # Import the API key 
class StockAnalysis:
    def __init__(self, symbol):
        self.symbol = symbol.upper()  
        self.api_key = Api_Key2 
        self.company_name = "N/A"
        self.market_exchange = "N/A"
        self.trading_currency = "N/A"
        self.current_price = "N/A"
        self.historical_data = None

 # get company details like name and exchange
    def get_company_details(self):
        url = f"https://api.polygon.io/v3/reference/tickers/{self.symbol}?apiKey={self.api_key}"
        print(f"Fetching company details from: {url}")
        response = requests.get(url)
        data = response.json()
        details = data.get("results", {})
        self.company_name = details.get("name", self.company_name)
        self.market_exchange = details.get("primary_exchange", self.market_exchange)
        self.trading_currency = details.get("currency_name", self.trading_currency)

 # get the latest stock price
    def get_latest_stock_price(self):
        url = f"https://api.polygon.io/v2/last/trade/{self.symbol}?apiKey={self.api_key}"
        print(f"Fetching latest stock price from: {url}")
        response = requests.get(url)
        data = response.json()
        price_info = data.get("results", {})
        self.current_price = price_info.get("p", self.current_price)


   

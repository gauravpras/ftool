import requests
from Api_key2 import Api_Key2  
 # Import the API key 

class StockDetails:
    def __init__(self, stock_symbol):
        "Use stock symbol and get details using Polygon"
        self.symbol = stock_symbol.upper()
        self.api_key = Api_Key2
        self.company = None
        self.trading_exchange = None
        self.latest_price = None
        self.trading_currency = None
        self.retrieve_stock_data()

    def retrieve_stock_data(self):
        "Get company name, exchange, and currency using Polygon"
        details_url = f"https://api.polygon.io/v3/reference/tickers/{self.symbol}?apiKey={self.api_key}"
        response = requests.get(details_url)
        if response.status_code == 200:
            data = response.json().get("results", {})
            self.company = data.get("name", "Not Available")
            self.trading_exchange = data.get("primary_exchange", "Not Available")
            self.trading_currency = data.get("currency_name", "Not Available")
        else:
            print(f"Failed to fetch details for {self.symbol}. Check the symbol or API key.")
            self.company = "Not Available"
            self.trading_exchange = "Not Available"
            self.trading_currency = "Not Available"

        #latest price
        self.retrieve_stock_price()

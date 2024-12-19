from StockDetails import StockDetails
from dividends import Dividends

symbol = input("Enter stock symbol(s). Use AAPL for one symbol or AAPL, MSFT, LUV for multiple symbols: ")

stock = StockDetails(symbol)


dividends = Dividends(symbol)
dividends_df = dividends.dividends_data(symbol)
dividends.visualize_dividends_data(dividends_df)

# Gary and nader add your classes here

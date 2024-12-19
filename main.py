from StockDetails import StockAnalysis
from dividends import Dividends
from portfolio_manager import PortfolioManager

print("Greetings! You've accessed the Stock Analysis and Portfolio Management Utility.\n")

# Stock Analysis Section
print("--- Let's Begin with Stock Analysis ---")
ticker_symbol = input("Please provide the stock ticker: ").strip()
stock_data = StockAnalysis(ticker_symbol)

# Get company details and the latest stock price
stock_data.get_company_details()
stock_data.get_latest_stock_price()
stock_data.show_stock_summary()

# Ask for historical data range and fetch it
while True:
    start_date = input("Specify the start date for historical data (YYYY-MM-DD): ").strip()
    end_date = input("Specify the end date for historical data (YYYY-MM-DD): ").strip()
    success = stock_data.fetch_historical_data(start_date, end_date)
    if success:
        break
    else:
        print("Sorry, no data available for the specified range.\n")
        retry = input("Would you like to try another date range? (yes/no): ").strip().lower()
        if retry != "yes":
            print("Proceeding without historical data.\n")
            break

# Plot the historical data if available
if stock_data.historical_data is not None:
    stock_data.plot_close_prices()

print("\nStock analysis is now complete.\n")

# Dividend Analysis Section
print("--- Diving Into Dividend Analysis ---")
symbol = input("Enter stock symbol(s). For example, use AAPL for one or AAPL, MSFT, LUV for multiple: ")
dividends = Dividends(symbol)
dividends_df = dividends.dividends_data(symbol)
dividends.visualize_dividends_data(dividends_df)

# Portfolio Management Section
print("--- Managing Your Portfolio ---")
symbols = input("Input stock symbol(s). For example, AAPL for one or AAPL, MSFT, LUV for multiple: ").split(",")
symbols = [symbol.strip().upper() for symbol in symbols]

portfolio = PortfolioManager()
for symbol in symbols:
    shares = int(input(f"How many shares do you own of {symbol}?: "))
    portfolio.add_stock(symbol, shares)

# Fetch and display stock details
for symbol in symbols:
    portfolio.fetch_stock_info(symbol)

# Visualize dividends data
print("Gathering and visualizing dividend projections...")
years = int(input("How many years ahead should the income projection cover?: "))
portfolio.visualize_dividend_projection(years)

print("\nThanks for using the Stock Analysis and Portfolio Management Utility! Have a great day!")

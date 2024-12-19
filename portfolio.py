import requests
import pandas as pd
import matplotlib.pyplot as plt
from Api_key3 import Api_Key3  


class PortfolioManager:
    def _init_(self):
        self.api_key = Api_Key3
        self.stocks = {}

    def add_stock(self, ticker_symbol, shares):
        """Add a stock to the portfolio."""
        ticker_symbol = ticker_symbol.upper()
        self.stocks[ticker_symbol] = {
            "shares": shares,
            "current_price": None,
            "dividends": []
        }

    def fetch_stock_info(self, ticker_symbol):
        """Fetch the latest stock price and dividend data for the given stock."""
        ticker_symbol = ticker_symbol.upper()


        url = "https://api.polygon.io/v2/aggs/ticker/" + ticker_symbol + "/prev?adjusted=true&apiKey=" + self.api_key
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.stocks[ticker_symbol]["current_price"] = data.get("results", [{}])[0].get("c", None)
        else:
            print(f"Error fetching price for {ticker_symbol}")

        url = "https://api.polygon.io/v3/reference/dividends?ticker=" + ticker_symbol + "&limit=1000&apiKey=" + self.api_key
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.stocks[ticker_symbol]["dividends"] = [
                dividend.get("cash_amount", 0) for dividend in data.get("results", [])
            ]
        else:
            print(f"Error fetching dividend data for {ticker_symbol}")

    def calculate_portfolio_value(self):
        """Calculate the total market value of the portfolio."""
        return sum(
            stock["shares"] * (stock["current_price"] if stock["current_price"] is not None else 0)
            for stock in self.stocks.values()
        )

    def calculate_dividend_projection(self, years):
        """Calculate projected dividend income over a given number of years based on real-world calculations."""
        total_income = 0
        for stock in self.stocks.values():
            if stock["dividends"]:
                most_recent_dividend = stock["dividends"][0]  
                dividend_frequency = 4  # Default to quarterly if not available
                annual_dividend = most_recent_dividend * dividend_frequency
                total_income += annual_dividend * stock["shares"] * years
        return total_income

    def visualize_dividend_projection(self, years):
        """Visualize dividend projections for each stock in the portfolio based on real-world calculations."""
        tickers = list(self.stocks.keys())
        projections = []

        for stock in self.stocks.values():
            if stock["dividends"]:
                most_recent_dividend = stock["dividends"][0]  
                dividend_frequency = 4  
                annual_dividend = most_recent_dividend * dividend_frequency
                projections.append(annual_dividend * stock["shares"] * years)
            else:
                projections.append(0)

        plt.figure(figsize=(12, 6))
        plt.bar(tickers, projections, color='skyblue')
        for i, value in enumerate(projections):
            plt.text(i, value + (value * 0.02), f"${value:,.2f}", ha='center')

        plt.title(f"Dividend Income Projection Over {years} Years", fontsize=16)
        plt.xlabel("Ticker Symbol", fontsize=14)
        plt.ylabel("Projected Income ($)", fontsize=14)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

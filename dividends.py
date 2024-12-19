import requests
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from Api_key import API_KEY  # API key for authentication

class Dividends:
    def __init__(self, symbol):
        self.api_key = API_KEY
        self.stocks = {}
        self.symbol = symbol.upper()

    def dividends_data(self, ticker_symbol):
        # Handle single string input, including comma-separated tickers
        if type(ticker_symbol) is str:
            ticker_symbol = [ticker.strip().upper() for ticker in ticker_symbol.split(",")]
        
        all_dividends = []  # List to store dividends from all tickers
        
        for ticker in ticker_symbol:
            url_dividends = (
                "https://api.polygon.io/v3/reference/dividends?ticker=" + ticker
                + "&limit=1000&apiKey=" + self.api_key
            )
            response = requests.get(url_dividends)
            
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                
                for div in results:
                    all_dividends.append({
                        "ticker": ticker,
                        "cash_amount": div.get("cash_amount", 0),
                        "currency": div.get("currency", "N/A"),
                        "declaration_date": div.get("declaration_date", "N/A"),
                        "ex_dividend_date": div.get("ex_dividend_date", "N/A"),
                        "pay_date": div.get("pay_date", "N/A"),
                        "record_date": div.get("record_date", "N/A"),
                        "dividend_type": div.get("dividend_type", "N/A"),
                        "frequency": div.get("frequency", "N/A")
                    })
            else:
                print(f"Error getting dividend information for {ticker}: {response.status_code}")
        
        # Convert all_dividends into a DataFrame
        dividends_df = pd.DataFrame(all_dividends)
        
        # Rearrange columns if dividends were found
        if not dividends_df.empty:
            dividends_df = dividends_df[[
                'ticker', 'declaration_date', 'ex_dividend_date', 'pay_date', 
                'record_date', 'cash_amount', 'currency', 'dividend_type', 'frequency'
            ]]
        
        return dividends_df

    def visualize_dividends_data(self, dividends_df):
        # Convert pay_date to datetime for plotting
        dividends_df['pay_date'] = pd.to_datetime(dividends_df['pay_date'])

        # Sort and group for top 5 dividends
        top_dividends = dividends_df.sort_values(by='pay_date', ascending=False).groupby('ticker').head(5)

        # Get unique tickers
        tickers = dividends_df['ticker'].unique()
        
        # --- Plotting the Line Plot ---
        # Create a figure for the line plot
        fig_line_plot = plt.figure(figsize=(14, 8))
        ax_main = fig_line_plot.add_subplot(111)
        
        # Plot dividend data for each ticker
        for ticker, group_data in dividends_df.groupby('ticker'):
            ax_main.plot(group_data['pay_date'], group_data['cash_amount'], marker='o', label=ticker)
        
        ax_main.set_title("Historical Dividend Payouts for Ticker(s)", fontsize=14)
        ax_main.set_xlabel("Payout Date", fontsize=12)
        ax_main.set_ylabel("Cash Amount ($)", fontsize=12)
        ax_main.legend(title="Ticker Symbol")
        ax_main.grid(True)
        
        # --- Plotting the Mini Tables ---
        # Create a figure for the mini tables
        fig_tables = plt.figure(figsize=(14, 8))
        
        # Create a grid layout for the mini tables (stacked vertically)
        gs = GridSpec(len(tickers), 1)  # Create a grid with len(tickers) rows and 1 column
        
        for i, ticker in enumerate(tickers):
            ax_table = fig_tables.add_subplot(gs[i])  # Stack tables vertically
            ax_table.axis('off')  # Turn off the axis for tables
            ticker_data = top_dividends[top_dividends['ticker'] == ticker]
            
            # Add a title for each table
            ax_table.text(0.5, 1.05, f"5 Latest Dividends for {ticker}", fontsize=10, fontweight='bold',
                          ha='center', transform=ax_table.transAxes)
            
            # Create the table
            table = ax_table.table(cellText=ticker_data.values,
                                   colLabels=ticker_data.columns,
                                   cellLoc='center',
                                   loc='center')
            table.auto_set_font_size(False)
            table.set_fontsize(8)
            table.auto_set_column_width(col=list(range(len(ticker_data.columns))))

        # Display both figures at the same time
        plt.show()
# ftool
Financial Tracking Tool
What is F Tool?
F Tool is an application designed to help investors track dividend-paying stocks and manage their investment portfolios. It simplifies the process of analyzing stocks, tracking dividend income, and visualizing portfolio performance. With real-time stock data and intuitive visualizations, F Tool makes it easier for investors to make informed decisions.

Features
Real-Time Data: Automatically fetch stock and dividend details using the Polygon.io API.
Portfolio Management: Add stocks, track their performance, and calculate total income projections.
Dividend Insights: View dividend history, current stock prices, and reinvestment growth estimates.
Visualizations: Generate clear and simple charts to show dividend trends and portfolio allocations.

Requirements
To use F Tool, you’ll need:

Python: Version 3.7 or higher.
API Key: A valid API key from Polygon.io.
Python Libraries: requests, pandas, matplotlib, and plotly.

Setup Instructions
Download the App

Open a terminal and type the following commands:

git clone git@github.com:<your-github-username>/f-tool.git  
cd f-tool
Install Required Libraries

Use the requirements.txt file to install all dependencies:

pip install -r requirements.txt
If the above doesn’t work, you can install the libraries one by one:

pip install requests pandas matplotlib plotly
Add Your API Key

Create a file named Api_key.py in the project directory and add the following:

API_KEY = 'your_polygon_api_key_here'


How to Use F Tool
Run the App

Type the following command to start the application:

python main.py
Follow the Instructions

Add stocks to your portfolio, Fetch stock and dividend information, View visualizations of your portfolio and dividend trends.

How It Works
F Tool connects to the Polygon.io API to gather real-time stock and dividend data. It retrieves information such as company names, stock prices, and dividend payouts. This data is used to calculate the total value of your portfolio and create charts that help visualize your portfolio’s performance and dividend trends.

Future Enhancements: Add features for tracking financial metrics like earnings and P/E ratios, Improve the reinvestment calculator for more accurate growth predictions, Build a web-based version for easier access and usability.

Stock Data Fetcher 📈
A simple Python script to fetch historical stock data from Yahoo Finance and save it in multiple formats for easy analysis and sharing.
What Does This Do? 🤔
This script helps you:

Download historical stock price data for any publicly traded company
Save the data in CSV format for analysis in Excel/Google Sheets
Generate a nicely formatted HTML report that you can open in your browser
Validate stock tickers to make sure they exist before downloading
Handle date inputs in a user-friendly DD MM YYYY format

Prerequisites 📋
Before running this script, make sure you have:

Python 3.6 or higher installed on your computer
An internet connection (to fetch data from Yahoo Finance)
Basic familiarity with running Python scripts from the command line

Installation 🛠️

Save the script as Fetch for Analysis.py (or any name you prefer)
Install required packages by running:
bashpip install yfinance pandas
Or if you're using pip3:
bashpip3 install yfinance pandas


How to Use 🚀

Run the script from your terminal/command prompt:
bashpython "Fetch for Analysis.py"

Enter the stock ticker when prompted:

Examples: AAPL (Apple), MSFT (Microsoft), GOOGL (Google)
The script will validate if the ticker exists
If invalid, it will ask you to try again


Enter the start date in DD MM YYYY format:
Enter day (DD): 01
Enter month (MM): 01
Enter year (YYYY): 2024

Enter the end date in the same format:
Enter day (DD): 31
Enter month (MM): 12
Enter year (YYYY): 2024

Wait for the download - you'll see a progress bar as the data downloads

What You Get 📁
The script creates a stock_data folder with three files:
1. Main CSV File (TICKER_YYYY-MM-DD_to_YYYY-MM-DD.csv)
Contains all the stock data including:

Date (as index)
Open price
High price
Low price
Close price
Adjusted Close price
Volume
Ticker symbol

2. HTML Report (TICKER_YYYY-MM-DD_to_YYYY-MM-DD.html)
A formatted report you can open in any browser with:

Styled table with all the data
Summary information (date range, total trading days)
Hover effects for easier reading
Sticky header for scrolling through long datasets

3. Analysis CSV (TICKER_YYYY-MM-DD_to_YYYY-MM-DD_analysis.csv)
Same as the main CSV but without the ticker column - cleaner for importing into analysis tools
Example Usage 🎯
Stock Data Fetcher using yfinance
----------------------------------------

Enter stock ticker symbol (e.g., AAPL, MSFT): AAPL
Validating ticker AAPL...
✓ Ticker AAPL is valid!

Enter start date:
Enter day (DD): 01
Enter month (MM): 06
Enter year (YYYY): 2024

Enter end date:
Enter day (DD): 31
Enter month (MM): 12
Enter year (YYYY): 2024

Fetching data for AAPL from 2024-06-01 to 2024-12-31...
[*********************100%***********************]  1 of 1 completed

✓ Data fetched successfully!
Shape: (146, 7)
Date range: 2024-06-03 to 2024-12-31
Trading days: 146
Understanding the Data Columns 📊

Open: The price at market open
High: The highest price during the trading day
Low: The lowest price during the trading day
Close: The price at market close
Adj Close: Close price adjusted for dividends and stock splits
Volume: Number of shares traded that day

Pro tip: Use "Adj Close" for most analysis as it accounts for corporate actions!
Common Issues & Solutions 🔧
"Ticker not found"

Double-check the ticker symbol on Yahoo Finance or Google
Make sure you're using the stock market ticker, not the company name
For international stocks, you might need the exchange suffix (e.g., RY.TO for Royal Bank on Toronto exchange)

"No data found for the given date range"

The stock might not have been trading during that period
Try a more recent date range
Remember that markets are closed on weekends and holidays

Date errors

Make sure to enter dates in DD MM YYYY format
The script won't accept future dates
Start date must be before end date

File not saving

Check if you have write permissions in the current directory
The script creates a stock_data folder - make sure it can create folders

Quick Tips 💡

For recent data: Use a shorter date range for faster downloads
For analysis: The "analysis.csv" file is perfect for importing into Excel or pandas
For sharing: Send the HTML file to friends - it opens in any browser!
Multiple stocks: Run the script multiple times for different tickers
Date validation: The script checks if your dates are valid and not in the future

What Can You Do With This Data? 🎨

Calculate moving averages
Analyze price volatility
Compare multiple stocks
Create price charts
Calculate returns
Backtest trading strategies
Track portfolio performance

Notes for My Friends 👥
Hey! If you're using this script:

It's pretty straightforward - just follow the prompts
The HTML file is the prettiest output if you just want to look at the data
Use the CSV files if you want to do calculations in Excel
If you need help with specific tickers or date ranges, just ask!
The data comes from Yahoo Finance, so it's the same as what you see on their website


Remember: This is historical data for analysis and learning. Always do your own research before making investment decisions! 🎓

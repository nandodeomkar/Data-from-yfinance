import yfinance as yf
import pandas as pd
from datetime import datetime
import os

def get_date_input(date_type):
    """Get date input from user in DD MM YYYY format"""
    while True:
        try:
            print(f"\nEnter {date_type} date:")
            day = int(input(f"Enter day (DD): "))
            month = int(input(f"Enter month (MM): "))
            year = int(input(f"Enter year (YYYY): "))
            
            # Create date object to validate
            date_obj = datetime(year, month, day)
            
            # Check if date is not in future
            if date_obj > datetime.now():
                print("Error: Date cannot be in the future!")
                continue
                
            # Format for yfinance (YYYY-MM-DD)
            date_str = date_obj.strftime('%Y-%m-%d')
            return date_str
            
        except ValueError as e:
            print(f"Invalid date! Please enter a valid date. Error: {e}")
            continue

def validate_ticker(ticker):
    """Validate if ticker exists"""
    try:
        test = yf.Ticker(ticker)
        # Try to get info - will fail if ticker doesn't exist
        test.info
        return True
    except:
        return False

def fetch_stock_data():
    """Main function to fetch stock data"""
    
    # Get ticker input
    while True:
        ticker = input("\nEnter stock ticker symbol (e.g., AAPL, MSFT): ").upper()
        print(f"Validating ticker {ticker}...")
        
        if validate_ticker(ticker):
            print(f"✓ Ticker {ticker} is valid!")
            break
        else:
            print(f"✗ Ticker {ticker} not found. Please try again.")
    
    # Get date inputs
    start_date = get_date_input("start")
    end_date = get_date_input("end")
    
    # Validate date range
    if start_date >= end_date:
        print("Error: Start date must be before end date!")
        return None
    
    print(f"\nFetching data for {ticker} from {start_date} to {end_date}...")
    
    try:
        # Fetch data from yfinance
        df = yf.download(ticker, start=start_date, end=end_date, progress=True)
        
        if df.empty:
            print("No data found for the given date range!")
            return None
        
        # Flatten multi-level columns if they exist
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        
        # Add ticker column for reference
        df['Ticker'] = ticker
        
        # Display basic info
        print(f"\n✓ Data fetched successfully!")
        print(f"Shape: {df.shape}")
        print(f"Date range: {df.index.min().strftime('%Y-%m-%d')} to {df.index.max().strftime('%Y-%m-%d')}")
        print(f"Trading days: {len(df)}")
        
        # Show first few rows
        print("\nFirst 5 rows of data:")
        print(df.head())
        
        # Save data
        save_data(df, ticker, start_date, end_date)
        
        return df
        
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def save_data(df, ticker, start_date, end_date):
    """Save DataFrame to CSV and HTML formats"""
    
    # Create data directory if it doesn't exist
    if not os.path.exists('stock_data'):
        os.makedirs('stock_data')
    
    # Create filename with ticker and date range
    filename_base = f"stock_data/{ticker}_{start_date}_to_{end_date}"
    
    # Save as CSV
    csv_filename = f"{filename_base}.csv"
    df.to_csv(csv_filename)
    print(f"\n✓ Data saved to CSV: {csv_filename}")
    
    # Save as HTML with styling
    html_filename = f"{filename_base}.html"
    
    # Create styled HTML
    html_string = f'''
    <html>
    <head>
        <title>{ticker} Stock Data</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f5f5f5;
            }}
            h1, h2 {{
                color: #333;
            }}
            .info {{
                background-color: #e8f4f8;
                padding: 10px;
                border-radius: 5px;
                margin: 10px 0;
            }}
            table {{
                border-collapse: collapse;
                width: 100%;
                background-color: white;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            th {{
                background-color: #4CAF50;
                color: white;
                padding: 12px;
                text-align: left;
                position: sticky;
                top: 0;
            }}
            td {{
                padding: 10px;
                border-bottom: 1px solid #ddd;
            }}
            tr:hover {{
                background-color: #f5f5f5;
            }}
        </style>
    </head>
    <body>
        <h1>{ticker} Stock Data</h1>
        <div class="info">
            <p><strong>Date Range:</strong> {start_date} to {end_date}</p>
            <p><strong>Total Trading Days:</strong> {len(df)}</p>
            <p><strong>Data Fetched:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        
        <h2>Historical Data</h2>
        {df.to_html(classes='data-table')}
    </body>
    </html>
    '''
    
    with open(html_filename, 'w') as f:
        f.write(html_string)
    
    print(f"✓ Data saved to HTML: {html_filename}")
    
    # Also save a simple version without the ticker column for analysis
    analysis_df = df.drop('Ticker', axis=1)
    analysis_filename = f"{filename_base}_analysis.csv"
    analysis_df.to_csv(analysis_filename)
    print(f"✓ Analysis-ready data saved to: {analysis_filename}")

# Main execution
if __name__ == "__main__":
    print("Stock Data Fetcher using yfinance")
    print("-" * 40)
    
    # Fetch the data
    stock_df = fetch_stock_data()
    
    if stock_df is not None:
        print("\n✓ Process completed successfully!")
        print("\nYou can now use the DataFrame 'stock_df' for analysis")
        print("Access individual columns like: stock_df['Close'], stock_df['Open'], etc.")
        
        # Example of accessing individual columns after flattening
        print("\nExample - accessing individual columns:")
        print(f"  - First 5 close prices: {stock_df['Close'].head().tolist()}")
    else:
        print("\n✗ Process failed. Please try again.")
import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_month_report(target_month):
    # Check if the month is valid
    if not 1 <= target_month <= 12:
        raise ValueError("Month must be a number between 1 and 12.")
    
    # Get current date and time
    current_date = datetime.now()
    current_year = current_date.year
    
    # Binance API provides data from July 2017
    start_date = datetime(current_year - 10, 1, 1)
    if start_date.year < 2017:
        start_date = datetime(2017, 7, 1)  # Binance launched in July 2017
    
    # Convert dates to milliseconds (Binance requires timestamp in ms)
    start_timestamp = int(start_date.timestamp() * 1000)
    end_timestamp = int(current_date.timestamp() * 1000)
    
    # Request parameters (BTCUSDT, 1-month interval)
    symbol = "BTCUSDT"
    interval = "1M"  # 1 month
    
    # Binance API endpoint
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "startTime": start_timestamp,
        "endTime": end_timestamp,
        "limit": 1000  # Maximum 1000 candles per request
    }
    
    print(f"Loading data from {start_date.date()} to {current_date.date()}...")
    response = requests.get(url, params=params)
    
    # Check request success
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")
    
    data = response.json()
    
    if not data:
        raise Exception("No data found in API response.")
    
    # Convert data to DataFrame
    columns = ['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'close_time', 
               'quote_asset_volume', 'trades', 'taker_buy_base', 'taker_buy_quote', 'ignore']
    df = pd.DataFrame(data, columns=columns)
    
    # Convert timestamp to datetime and set as index
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('datetime', inplace=True)
    
    # Convert numeric columns to float
    df['Open'] = df['Open'].astype(float)
    df['Close'] = df['Close'].astype(float)
    df['High'] = df['High'].astype(float)
    df['Low'] = df['Low'].astype(float)
    df['Volume'] = df['Volume'].astype(float)
    
    # Filter data by the target month
    month_data = df[df.index.month == target_month]
    
    if month_data.empty:
        print(f"No data available for month {target_month} in the specified range.")
        return
    
    # Dictionary for month names in English
    month_names = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    month_name = month_names[target_month]
    
    print(f"\nBitcoin data analysis for {month_name} of each year:\n")
    
    for index, row in month_data.iterrows():
        year = index.year
        open_price = row['Open']
        close_price = row['Close']
        high_price = row['High']
        low_price = row['Low']
        volume = row['Volume']
        
        # Calculate percentage change
        price_change = ((close_price - open_price) / open_price) * 100
        
        # Determine trend
        trend = "up" if close_price > open_price else "down"
        
        print(f"{month_name} {year}:")
        print(f"Open price: ${open_price:,.2f}")
        print(f"Close price: ${close_price:,.2f}")
        print(f"High: ${high_price:,.2f}")
        print(f"Low: ${low_price:,.2f}")
        print(f"Trading volume: {volume:,.0f} BTC")
        print(f"Change: {price_change:+.2f}% ({trend})")
        print("-" * 50)

def main():
    try:
        # Prompt user for month number
        target_month = int(input("Enter month number (1-12): "))
        print(f"Fetching Bitcoin data from Binance API for month {target_month}...")
        get_bitcoin_month_report(target_month)
    except ValueError as e:
        print(f"Input error: {str(e)}. Please enter a number between 1 and 12.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Check your internet connection and try again.")

if __name__ == "__main__":
    main()
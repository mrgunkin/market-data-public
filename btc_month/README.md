# Bitcoin Monthly Analysis (btc_month.py)

This script retrieves historical Bitcoin (BTC) price data from the Binance API and provides an analysis for a specified month across all available years, starting from July 2017 (Binance's launch date). The output includes open price, close price, high, low, trading volume, and percentage change.

## Features
- Specify a month (1–12) to get data for that month across all available years.
- Data includes:
  - Open and close prices.
  - High and low prices.
  - Trading volume (in BTC).
  - Percentage change and trend (up/down).

## Requirements
The script requires the following Python packages:
- `requests` — for making API requests to Binance.
- `pandas` — for data processing.
- (Optional) `pyarrow` — to suppress pandas warnings and ensure future compatibility.

### Installation
1. Ensure you have Python 3.6 or higher installed.
2. Install the dependencies:
```bash
pip install requests pandas pyarrow
```
## How to Run
Save the script as btc_month.py.

Open a terminal and navigate to the script's directory:
```bash
cd path/to/directory
```
Run the script:
```bash
python btc_month.py
```
Enter the month number (e.g., 3 for March) and press Enter.

Example Output
```markdown
Enter month number (1-12): 3
Fetching Bitcoin data from Binance API for month 3...
Loading data from 2017-07-01 to 2025-02-28...

Bitcoin data analysis for March of each year:

March 2024:
Open price: $61,130.99
Close price: $71,280.01
High: $73,777.00
Low: $59,005.00
Trading volume: 1,706,807 BTC
Change: +16.60% (up)
--------------------------------------------------
```
## Limitations
Data is available only from July 2017 (Binance launch).
Requires an internet connection.

## License
This project is licensed under the MIT License (see the LICENSE file, if included).
## Author
Created by [mrgunkin](https://github.com/mrgunkin). For questions or suggestions, please open an issue.


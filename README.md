Stock Comparison Dashboard

This repository contains a stock comparison dashboard built using Bokeh, yfinance, and Python. The dashboard allows users to compare the stock performance of two different tickers over a specified date range and plot various technical indicators such as the 100-day and 30-day Simple Moving Averages (SMA).

Features

Stock Ticker Input: Users can input two stock tickers to compare their performance.
Date Range Selection: Users can select a start and end date using a date picker.
Technical Indicators: Available options include:
100-day SMA
30-day SMA

Future Expansion:
Dynamic Plotting: The dashboard dynamically updates the plots based on user input and selections.
Clear Layout: Two plots are displayed side-by-side for easy comparison of stock data.
Technologies Used
Bokeh: For interactive plotting and dashboard layout.
yfinance: For fetching historical stock data from Yahoo Finance.
Pandas: For data manipulation and rolling calculations (SMA).

How to Use
Clone this repository:

git clone https://github.com/your-username/stock-comparison-dashboard.git
cd stock-comparison-dashboard
Install the required dependencies:


pip install -r requirements.txt
Run the Bokeh server:


bokeh serve --show app.py
The dashboard will open in your browser. Input two stock tickers (e.g., AAPL and GOOGL), choose a date range, and select the desired indicators to visualize the stock data.


Example
Stock Comparison: Compare the adjusted close prices of two stocks, along with their 100-day and 30-day SMA, within a specified date range.
Indicators: Toggle between different indicators to see how the stock performance changes over time.
Future Enhancements
Add support for additional indicators like Linear Regression and Exponential Moving Averages.
Allow users to compare more than two stocks at once.
Add more customization options for chart colors, themes, and layouts.

Contributing
Feel free to open issues or submit pull requests if you would like to contribute to this project.

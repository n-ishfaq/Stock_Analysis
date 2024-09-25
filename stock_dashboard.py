from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import TextInput, DatePicker, MultiChoice, Button
from bokeh.plotting import figure
import yfinance as yf
import datetime as dt
import pandas as pd

def load_data(ticker1, ticker2, start, end):
    df1 = yf.download(ticker1, start=start, end=end)
    df2 = yf.download(ticker2, start=start, end=end)
    print(df1,df2)
    return df1, df2
    

def plot_data(df1, df2, indicators, ticker1, ticker2):
   # Convert date strings to datetime objects
    start = pd.to_datetime(date_picker_from.value)
    end = pd.to_datetime(date_picker_to.value)

    
    fig = figure(title="Stock Data", x_axis_type='datetime', x_range=(start,end))
    fig2 = figure(title="Stock Data", x_axis_type='datetime', x_range=(start,end))

    # Plot Adjusted Close Prices
    fig.line(df1.index, df1['Adj Close'], line_width=2, legend_label=f'{ticker1} Adj Close', color='blue')
    fig2.line(df2.index, df2['Adj Close'], line_width=2, legend_label=f'{ticker2} Adj Close', color='green')

    # Plot 100-day SMA for both stocks
    if '100 day SMA' in indicators:
        sma_100_df1 = df1['Adj Close'].rolling(window=100).mean()
        sma_100_df2 = df2['Adj Close'].rolling(window=100).mean()
        fig.line(df1.index, sma_100_df1, line_width=2, legend_label=f'100 day SMA ({ticker1})', color='red')
        fig2.line(df2.index, sma_100_df2, line_width=2, legend_label=f'100 day SMA ({ticker2})', color='orange')

    # Plot 30-day SMA for both stocks
    if '30 day SMA' in indicators:
        sma_30_df1 = df1['Adj Close'].rolling(window=30).mean()
        sma_30_df2 = df2['Adj Close'].rolling(window=30).mean()
        fig.line(df1.index, sma_30_df1, line_width=2, legend_label=f'30 day SMA ({ticker1})', color='purple')
        fig2.line(df2.index, sma_30_df2, line_width=2, legend_label=f'30 day SMA ({ticker2})', color='brown')

    return fig,fig2


def on_button_click():

    ticker1 = stock1.value
    ticker2 = stock2.value
    start = date_picker_from.value
    end = date_picker_to.value
    indicators = indicator_choice.value

    df1, df2 = load_data(ticker1, ticker2, start, end)
    p1,p2 = plot_data(df1, df2, indicators, ticker1, ticker2)
    
 
    curdoc().clear()
    curdoc().add_root(column(layout,row(p1,p2)))



stock1 = TextInput(title="Stock 1", value="AAPL")
stock2 = TextInput(title="Stock 2", value="GOOGL")


date_picker_from = DatePicker(title="Start Date", value="2021-01-01", min_date="2010-01-01", max_date=dt.datetime.now().strftime("%Y-%m-%d"))
date_picker_to = DatePicker(title="End Date", value="2021-02-01", min_date="2010-01-01", max_date=dt.datetime.now().strftime("%Y-%m-%d"))


indicator_choice = MultiChoice(title="Indicators", value=["100 day SMA", "30 day SMA"], options=["100 day SMA", "30 day SMA", "Linear Regression Line"])



load_button = Button(label="Load Data", button_type="success")
load_button.on_click(on_button_click)



layout = column(stock1, stock2, date_picker_from, date_picker_to, indicator_choice, load_button)



curdoc().add_root(layout)


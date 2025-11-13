#  """"
#     Data Handler Module
#     Responsible for downloading, validating, and preprocessing data
#  """"

import pandas as pd
import yfinance as yf

def download_stock_data(ticker, start_date, end_date):
    """_summary_

    Args:
        ticker (str): Stock ticker symbol (e.g, "SPY",)
        start_date (str): Start date in "YYYY-MM-DD" format
        end_date (str): End date in "YYYY-MM-DD" format
        
    Returns:
        pd.DataFrame: Clean DataFrame with OHLCV data
        
    """
    try:
        data = yf.download(ticker, start = start_date, end= end_date, progress = False)
        
        #validate data quality
        if data.empty:
            raise ValueError("No data found for ticker {ticker}")
        
        #check for missing data
        #data.isNull()->Returns True/False for each value
        # .sum().sum() Counts the number of True values -> twice since we have two columns
        # > 0 Returns True if the count is greater than 0
        #.fillna(method='ffill') Fills missing values with the previous value
        if data.isnull().sum().sum() > 0:
            print(f"Warning:Found {data.isnull().sum().sum()} missing values. Filling Forward.")
            data = data.fillna(method='ffill')
        
        print(f"Donwloaded {len(data)} days of data for {ticker}")
        return data
    
    except Exception as e:
        print(f"Error downloading data: {e}")
        return None
    
def calculate_returns(data):
    '''
    Calculate daily returns from price data.
    Args:
        data(pd.DataFrame): DataFrame with close prices
    Returns:
        pd.DataFrame: DataFrame with daily returns
        
        
        Example: 
            Close Price: 100 -> 102 -> 99
            Daily  Returns: ? +2% -> -3% 
    '''
    #data['Close'] -> Get just the Close price column
    #pct_change() -> Calculate percentage change from previous day
    return data['Close'].pct_change()
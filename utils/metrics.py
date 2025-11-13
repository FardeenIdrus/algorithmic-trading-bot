'''
Metrics Module
Calculates Performance metrics for backtesting results.
'''

import numpy as np
import pandas as pd

def calculate_sharpe_ratio(returns, risk_free_rate = 0.02):
    '''
    Calculate Sharpe ratio for a series of returns.
    Args:
        returns (pd.Series): Daily returns
        risk_free_rate (float): Risk-free rate (default: 0.02)
    Returns:
        float: Sharpe ratio
    
    '''
    #Convert annual risk-free rate to daily rate (divid by 252 trading days in a year)
    daily_risk_free_rate = risk_free_rate / 252
    excess_returns = returns - daily_risk_free_rate
    
    sharpe_ratio = np.sqrt(252) * (excess_returns.mean() / excess_returns.std())
    return sharpe_ratio

def calculate_max_drawdown(returns):
    """
    Calculate maximum drawdown for a series of returns.
    Args:
        returns (pd.Series): Daily returns
    Returns:
        float: Maximum drawdown as percentage
    """
    # Cumulative returns: (1 + return1) * (1 + return2) * etc
    cumulative = (1 + returns).cumprod()
    
    # Running maximum: highest value seen so far
    running_max = cumulative.expanding().max()
    
    # Drawdown: how far below the peak are we?
    drawdown = (cumulative - running_max) / running_max
    
    # Return the worst drawdown (most negative value)
    return drawdown.min()

def calculate_win_rate(returns):
    """
    Calculate win rate (percentage of positive return days).
    
    Args:
        returns (pd.Series): Daily returns
    
    Returns:
        float: Win rate as percentage
    """
    # Count how many days had positive returns
    winning_days = (returns > 0).sum()
    
    # Divide by total days and multiply by 100 for percentage
    win_rate = (winning_days / len(returns)) * 100
    
    return win_rate

def calculate_win_rate(returns):
    """
    Calculate win rate (percentage of positive return days).
    
    Args:
        returns (pd.Series): Daily returns
    
    Returns:
        float: Win rate as percentage
    """
    # Count how many days had positive returns
    winning_days = (returns > 0).sum()
    
    # Divide by total days and multiply by 100 for percentage
    win_rate = (winning_days / len(returns)) * 100
    
    return win_rate
        
    ß
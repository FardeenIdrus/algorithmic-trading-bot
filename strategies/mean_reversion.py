"""
Mean Reversion Logic:
The idea is that prices tend to bounce back to their average. When a price goes too far below the average (oversold), it's likely to bounce back up. When it goes too far above (overbought), it's likely to drop back down.
With momentum.py, you bought things that were going up. Mean reversion is the opposite - you buy things that have fallen too far.
How we measure "too far":
We use a 20-day rolling average (the mean) and calculate how many standard deviations away the price is. If it's 2 standard deviations below the average, that's "oversold". If it's 2 above, that's "overbought".
The signals:

Price falls 2+ standard deviations below the 20-day average → BUY (expect it to bounce back up)
Price rises 2+ standard deviations above the 20-day average → SELL (expect it to drop back down)
When you own a position, sell it once the price crosses back to the average

"""
import backtrader as bt

class MeanReversionStrategy(bt.strategy):
    
    params = (
        ('window', 20), #Days for rolling averagte and std dev
        ('num_std', 2), #Number of standard deviations for bands
    )
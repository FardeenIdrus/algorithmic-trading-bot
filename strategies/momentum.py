"""
    Momemtum Strategy
    Buy assets that have gone up recently, sell those that have gone down
"""

import backtrader as bt

class MomentumStrategy(bt.Strategy):
    """
    Momentum strategy implementation
    """
    params = (
        ('lookback_period', 20),
        ('holding_period',10)
    )
    
    def __init__(self):
        """Initialise the strategy
            Calculate momentum indicator based on lookback period.
        """
        # Calculate momentum: current price - price N days ago
        # Positive momentum = price went up, negative = price went down
        self.momentum = self.data.close - self.data.close(self.params.lookback_period)
        self.bar_executed = None
        
def next(self):
    """Execute starategy logic on each bar (day)
    Called automatically by backtrader for each day of data
    """
    
    #Check if we already have a position
    if not self.position:
        if self.momentum[0] > 0:
            self.buy()
            self.bar_executed = len(self)
    else:
         # We have a position, check if we should SELL
         # Calculate how many bars (days) we've been holding
         bars_held = len(self) - self.bar_executed
         if bars_held >= self.params.holding_period:
                # We've held for enough days, SELL
                self.sell()
            
         elif self.momentum[0] < 0:
                # Momentum turned negative (price went down), SELL early
                self.sell()
         
        
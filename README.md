# Estimating-Shares-Stocks-liquidity-with-roll-spread
ROll Spread measure liquidaity where:
     Liquidity is defined as how quickly we can dispose of our asset without losing its
     intrinsic value.
Determining Roll spread observation using ROLL(1985)
Here estimates are based on serial covariance in price changes
Formula:
        ROLL Spread-2*root(-covariance(change in closing price of day and day-1,closing \
        price of day-1))
        %spread=roll spread/average share price in estimation period
        
'''

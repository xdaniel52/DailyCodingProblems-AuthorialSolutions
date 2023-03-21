"""
Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling 
that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock 
at 5 dollars and sell it at 10 dollars.
"""

def max_profit(prices):
    min_price = min(prices[:2])
    max_prof = prices[1]-prices[0]
    for i in range(2,len(prices)):
        if prices[i] - min_price > max_prof:
            max_prof = prices[i] - min_price
        
        if prices[i] < min_price:
            min_price = prices[i]
            
    return max_prof

print(max_profit([9, 11, 8, 5, 7, 10]))

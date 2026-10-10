# 121. Best Time to Buy and Sell Stock

# You are given an array prices where 
# prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

# Example 1:
                 # 0 1 2 3 4 5  
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed 
# because you must buy before you sell.

# buy must be before sell (l < r, l= buy, r = sell)
# start at profit of 0 
# 7, 1 => l > r => move to the right 
# 1, 5 => l < r => maxP = 5-1 = 4. shift r+=1
# 1, 3 => l < r => maxP = 3-1 = 2. shift r
# 1, 6 => l < r => maxP = 6-1 = 5. shift r
# 1, 4 => '' 

def maxProfit(prices):
    l = 0
    r = 1
    maxP = 0
    while(r < len(prices)):
        if (prices[l]>prices[r]):
            #negative profit then we move to the lowest option which would be right 
            l=r
        else:
            maxP = max(maxP,prices[r]-prices[l])
        r+=1
    return maxP
prices = [2,1,2,1,0,1,2]
# 2, 1 => l > r; l =3, r=4
# 1, 0 => l > r; l =4, r=5 
# 0, 1 => l < r; l =4, r=6
# 0, 2 => l < r; l =4, r=7 
print(maxProfit(prices))
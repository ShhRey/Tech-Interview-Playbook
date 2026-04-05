# Question: You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''
Edge Cases to be Confirmed:
- price cannot be -ve / 0
- can price be same as before?
- what could be the size of the array?
- 
'''

from typing import List

# Brute Force Approach   
# TC: O(N*2)  SC: O(1)
def maxProfitBF(prices: List[int]) -> int:
    # Initializing var
    res, profit = 0, 0
    # Iterating through prices arr for buy
    for i in range(len(prices)):
        # Iterating through prices arr for sell
        for j in range(i+1, len(prices)):
            # Calculate Profit (sell - buy)
            profit = prices[j] - prices[i]
            # Check for max and update res
            res = max(res, profit)
    # Return result
    return res



# Min and Max Approach   
# TC: O(N)  SC: O(1)
def maxProfitMM(prices: List[int]) -> int:
    # Set buyP to inf, maxP to 0
    buyP = float('inf')
    maxP = 0
    # Iterate through prices arr
    for price in prices:
        # Keep checking for min buyP
        buyP = min(buyP, price)
        # Calc profit for every price
        profit = price - buyP
        # Calc max prof by comparing with maxP
        maxP = max(maxP, profit)
    # Return maxP
    return maxP



# Sliding Window Approach   
# TC: O(N)  SC: O(1)
def maxProfit(prices: List[int]) -> int:
    # Set left amd res to 0
    l, res = 0, 0
    # Iterate through prices as right=1
    for r in range(1, len(prices)):
        # Check for low buyP and update left
        if prices[l] > prices[r]:
            l = r
        else:
            # Update result while calc profit from r-l
            res = max(res, prices[r] - prices[l])
    # Return result
    return res





# Custom Test Cases
q = maxProfit([7, 1, 5, 3, 6, 4])
print(q)
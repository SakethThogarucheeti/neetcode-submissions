from collections import deque
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 0
        
        profit = 0
        while s < len(prices):
            if prices[b] >= prices[s]:
                b = s
            
            currprofit = prices[s] - prices[b] if s < len(prices) else 0
            profit = max(profit, currprofit)
            s+=1
        
        return profit
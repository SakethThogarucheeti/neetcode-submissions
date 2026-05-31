from collections import deque
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suffixmax = deque()

        for pidx in range(len(prices) -1, -1, -1):
            last = suffixmax[0] if suffixmax else 0
            currmax = max(last, prices[pidx])
            suffixmax.appendleft(currmax)
        
        print(suffixmax)

        profit = 0
        for pidx, p in enumerate(prices):
            currprofit = suffixmax[pidx] - p
            profit = max(currprofit, profit)
        
        return profit
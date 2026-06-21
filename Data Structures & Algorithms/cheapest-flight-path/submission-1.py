class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = defaultdict(lambda: float("inf"))
        prices[src] = 0

        for i in range(k+1):
            tprices = prices.copy()
            for s, d, p in flights:
                if prices[s] + p < tprices[d]:
                    tprices[d] = prices[s] + p
            prices = tprices
        
        if prices[dst] == float("inf"):
            return -1
        return prices[dst]
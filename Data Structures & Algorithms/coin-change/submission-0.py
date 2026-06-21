class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        q = deque([0])
        visited = set()
        visited.add(0)

        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()

                for coin in coins:
                    nxt = cur + coin

                    if nxt == amount:
                        return res
                    if nxt > amount or nxt in visited:
                        continue
                    visited.add(nxt)
                    q.append(nxt)
        return -1

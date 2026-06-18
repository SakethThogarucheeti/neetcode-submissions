from collections import defaultdict, deque
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(set)
        w = defaultdict(lambda:float("inf"))
        d = defaultdict(lambda:float("inf"))
        d[k] = 0

        for u,v,t in times:
            adj[u].add(v)
            w[(u,v)] = t

        pq = [[0,k]]

        visit = set()
        t = 0

        while pq:
            cw, cn = heapq.heappop(pq)
            if cn in visit:
                continue
            visit.add(cn)

            t = cw

            neis = adj[cn]


            for nei in neis:
                neiw = w[(cn,nei)]
                if nei not in visit:
                    heapq.heappush(pq, (cw + neiw, nei))

        
        return t if len(visit)==n else -1 


        
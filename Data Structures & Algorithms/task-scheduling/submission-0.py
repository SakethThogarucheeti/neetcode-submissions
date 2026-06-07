class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = dict()

        for t in tasks:
            m[t] = m.get(t, 0) + 1
        
        hq = []

        for t,f in m.items():
            heapq.heappush_max(hq, f)

        cd = deque()

        c = 0
        while hq or cd:
            if not (cd and cd[0][0] <= c):
                if hq:
                    f = heapq.heappop_max(hq)
                    f -= 1
                    if f>0:
                        cd.append((c+n+1, f))
                c += 1
            else:
                nt, f = cd[0]
                if nt <= c:
                    heapq.heappush_max(hq, f)
                    cd.popleft()
                else:
                    c += 1

        
        return c 
        
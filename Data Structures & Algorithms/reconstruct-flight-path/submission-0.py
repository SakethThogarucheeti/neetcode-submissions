class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in reversed(sorted(tickets)):
            adj[src].append(dst)
        
        stack = ["JFK"]
        res = []

        while stack:
            curr = stack[-1]
            if adj[curr]:
                nei = adj[curr].pop()
                stack.append(nei)
            else:
                res.append(stack.pop())
        res.reverse()
        return res


        
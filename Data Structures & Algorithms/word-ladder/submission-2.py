from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        if endWord not in wordList:
            return 0
        
        def dist(w1, w2):
            d = 0

            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    d += 1
            return d

        adj = defaultdict(set)
        allWords = wordList + [beginWord]
        for i in range(len(allWords)):
            curr = allWords[i]
            for j in range(i+1, len(allWords)):
                nei = allWords[j]
                if dist(curr, nei) == 1:
                    adj[curr].add(nei)
                    adj[nei].add(curr)
        

        print(adj)

        q = deque()
        q.append((beginWord, None))

        visited = set()
        visited.add(beginWord)

        res = 1

        while q:
            l = len(q)
            for i in range(l):
                curr, par = q.popleft()
                                
                for nei in adj[curr]:
                    if nei == par or nei in visited:
                        continue
                    if nei == endWord:
                        return res + 1
                    visited.add(nei)
                    q.append((nei, curr))
            
            res += 1
        
        return 0
            

        
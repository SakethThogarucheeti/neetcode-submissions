"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        start = node
        visited = dict()

        q = deque()
        q.append(node)

        visited[node] = Node(node.val)


        while q:
            node = q.popleft()
            for nei in node.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    q.append(nei)
                visited[node].neighbors.append(visited[nei])
        
        return visited[start]

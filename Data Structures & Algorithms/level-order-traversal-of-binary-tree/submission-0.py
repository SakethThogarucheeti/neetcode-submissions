# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque([root])
        res = []
        while q:
            curres = []
            while q:
                curres.append(q.popleft())
            curvals = []
            for i in curres:
                if i:
                    curvals.append(i.val)
            if len(curvals) > 0:
                res.append(curvals)

            for i in curres:
                if i:
                    q.append(i.left)
                    q.append(i.right)
        
        return res

        
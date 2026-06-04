# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        levels = self.levelOrder(root)
        print(levels)

        res = []

        for level in levels:
            if level:
                cur = level[-1]
                if cur:
                    res.append(cur.val)
        return res
    

    def levelOrder(self, root):
        res = []
        q = deque([root])

        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                level.append(cur)

                if cur:
                    if cur.left: 
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            if level:
                res.append(level)

        return res

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        n = root
        while n:
            if n.val == p.val or n.val == q.val:
                return n
            elif p.val > n.val and q.val > n.val:
                n = n.right
            elif p.val < n.val and q.val < n.val:
                n = n.left
            else:
                return n
        
        return n

        
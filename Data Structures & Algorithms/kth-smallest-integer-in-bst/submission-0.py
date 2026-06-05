# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.target = k
        self.res = 0
        def dfs(node, nv):
            if not node:
                return nv
            print(nv, node and node.val, node.left and node.left.val, node.right and node.right.val)
            
            nv = dfs(node.left, nv)

            if nv == self.target:
                self.res = node.val
            nv += 1

            nv = dfs(node.right, nv)

            return nv
        
        print(dfs(root,1))
        
        return self.res

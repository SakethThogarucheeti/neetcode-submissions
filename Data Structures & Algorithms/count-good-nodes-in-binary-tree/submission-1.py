# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, maxi):
            if root is None:
                return 0
            print(root.val, root.left and root.left.val, root.right and root.right.val)
            
            if root.val >= maxi:
                maxi = max(root.val, maxi)
                return dfs(root.left, maxi) + dfs(root.right, maxi) + 1
            
            if root.val < maxi:
                return dfs(root.left, maxi) + dfs(root.right, maxi)
        
        res = dfs(root, float("-inf"))
        
        return res


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        rootrange = [
            float("-inf"), 
            float("inf")
            ]

        return self.isBst(root, rootrange)
    

    def isBst(self, root, arange):

        if not root:
            return True
        
        print(root.val, root.left and root.left.val, root.right and root.right.val)

        l = r = True

        if root.left:
            
            l = arange[0] < root.left.val < root.val
            print(root.val, root.left and root.left.val, root.right and root.right.val, l, arange)
        
        if root.right:
            r = root.val < root.right.val < arange[1]
            print(root.val, root.left and root.left.val, root.right and root.right.val, r, arange)

    
        cur = l and r

        lrange = [arange[0], root.val]
        rrange = [root.val, arange[1]]

        lisbst = self.isBst(root.left, lrange)
        risbst = self.isBst(root.right, rrange)

        print(root.val, cur, lisbst, risbst)

        res = cur and lisbst and risbst


        return res

        
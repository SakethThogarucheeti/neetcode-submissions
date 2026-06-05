# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inidx = dict()
        for idx, i in enumerate(inorder):
            inidx[i] = idx
        
        preidx = 0

        def dfs(ileft,iright):
            nonlocal preidx
            if ileft > iright:
                return None
            
            root = preorder[preidx]

            rootidx = inidx[root]
            preidx += 1


            left = dfs(ileft, rootidx - 1)
            right = dfs(rootidx + 1, iright)

            return TreeNode(root, left, right)
        
        return dfs(0, len(inorder) - 1)
            
        



        
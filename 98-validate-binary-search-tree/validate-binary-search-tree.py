# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    class dataObj:
        def __init__(self):
            self.minInTree = float('inf')
            self.maxInTree = -float('inf')
            self.isBST = True

    def isBSTHelper(self, root):
        if root is None:
            return self.dataObj()

        lans = self.isBSTHelper(root.left)
        rans = self.isBSTHelper(root.right)

        c1 = root.val > lans.maxInTree
        c2 = root.val < rans.minInTree
        c3 = lans.isBST
        c4 = rans.isBST

        myans = self.dataObj()

        myans.minInTree = min(lans.minInTree, root.val, rans.minInTree)
        myans.maxInTree = max(lans.maxInTree, root.val, rans.maxInTree)
        myans.isBST = c1 and c2 and c3 and c4

        return myans 
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        rootans = self.isBSTHelper(root)
        return rootans.isBST
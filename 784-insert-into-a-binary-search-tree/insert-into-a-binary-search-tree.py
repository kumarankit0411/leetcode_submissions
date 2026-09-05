# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        temp = root

        while temp is not None:
            if temp.val > val:
                if temp.left is None:
                    temp.left = TreeNode(val)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = TreeNode(val)
                    break
                else:
                    temp = temp.right
        
        return root
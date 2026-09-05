# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValue(self, root):
        if root is None:
            return None
        if root.left is None:
            return root
        return self.minValue(root.left)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None or root.right is None:
                if root.left is None:
                    return root.right
                else:
                    return root.left
            else:
                replacementNode = self.minValue(root.right)
                root.val = replacementNode.val
                root.right = self.deleteNode(root.right, replacementNode.val)

        return root

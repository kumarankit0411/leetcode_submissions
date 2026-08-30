# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self, inorder, isi, iei, preorder, psi, pei):
        if isi>iei or psi>pei:
            return None
        
        root = TreeNode(preorder[psi])

        idx = -1
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                idx = i

        lc = idx - isi

        root.left = self.build(inorder, isi, idx - 1, preorder, psi + 1, psi+lc)
        root.right = self.build(inorder, idx+1, iei, preorder, psi+lc+1, pei)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(inorder, 0, len(inorder) - 1, preorder,0, len(preorder)-1)
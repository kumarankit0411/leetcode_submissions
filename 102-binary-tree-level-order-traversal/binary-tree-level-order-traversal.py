# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans

        q = deque()
        q.append(root)

        while len(q) > 0:
            smallans = []
            size = len(q)
            while size > 0:
                fnt = q.popleft()
                smallans.append(fnt.val)
                if fnt.left is not None:
                    q.append(fnt.left)
                if fnt.right is not None:
                    q.append(fnt.right)
                size-=1
            ans.append(smallans)
        return ans
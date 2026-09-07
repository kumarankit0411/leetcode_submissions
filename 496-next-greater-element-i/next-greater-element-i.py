class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ngr_map = {}
        stack = []

        for x in reversed(nums2):
            while stack and stack[-1] < x:
                stack.pop()

            ngr_map[x] = stack[-1] if stack else -1

            stack.append(x)

        return [ngr_map[x] for x in nums1]
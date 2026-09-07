class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n 
        stack = []

        for i in range(2 * n - 1, -1, -1):
            x = nums[i%n]

            while stack and stack[-1] <= x:
                stack.pop()
            
            if i < n:
                if stack:
                    res[i] = stack[-1]

            stack.append(x)


        return res
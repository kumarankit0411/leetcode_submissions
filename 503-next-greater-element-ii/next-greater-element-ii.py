class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        new_arr = nums + nums
        n = len(nums)
        res = [-1] * n 
        stack = []

        for i in range(len(new_arr)-1, -1, -1):
            x = new_arr[i]

            while stack and stack[-1] <= x:
                stack.pop()
            
            if i < n:
                if stack:
                    res[i] = stack[-1]

            stack.append(x)


        return res
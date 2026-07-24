class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        right = n-1
        left = 0

        res = [0] * n

        for i in range(n-1, -1, -1):
            if(abs(nums[left]) >= abs(nums[right])):
                res[i] = pow(nums[left], 2)
                left += 1
            else:
                res[i] = pow(nums[right], 2)
                right -= 1

        return res

        
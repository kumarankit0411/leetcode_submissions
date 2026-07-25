class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        i = 0
        j = n - 1

        while(i<j):
            curr_sum = nums[i]+nums[j]
            if curr_sum == target:
                return [i+1, j+1]
            elif curr_sum > target:
                j -= 1
            else:
                i += 1
        
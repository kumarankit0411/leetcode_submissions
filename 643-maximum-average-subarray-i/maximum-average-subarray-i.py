class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k
        n = len(nums)
        sums = sum(nums[i:j])
        max_sum = sums

        while j < n:
            sums = (sums - nums[i] + nums[j])
            if sums > max_sum:
                max_sum = sums
            i+=1
            j+=1

        return max_sum/k
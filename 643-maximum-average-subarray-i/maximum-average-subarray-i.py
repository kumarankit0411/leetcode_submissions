class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k
        n = len(nums)
        f_sum = sum(nums[i:j])
        max_avg = f_sum/k
        if k == n:
            return max_avg

        while j < n:
            f_sum = (f_sum - nums[i] + nums[j])
            new_avg = f_sum / k
            if new_avg > max_avg:
                max_avg = new_avg
            i+=1
            j+=1

        return max_avg
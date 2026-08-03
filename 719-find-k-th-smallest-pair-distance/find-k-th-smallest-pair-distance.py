class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        low = 0
        high = nums[-1] - nums[0]

        while low<high:
            mid = low + (high - low)//2

            pairs_count = self.count_pairs(nums, mid)

            if pairs_count >= k:
                high = mid
            else:
                low = mid + 1

        return low

    def count_pairs(self, nums, max_dist):
        count = 0
        i = 0

        for j in range(len(nums)):
            while nums[j] - nums[i] > max_dist:
                i+=1
            count += j - i
        
        return count
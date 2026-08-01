class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.fo(nums, target), self.lo(nums, target)]
        
    def fo(self, nums, target):
        l = 0
        r = len(nums) - 1
        ans = -1

        while l<=r:
            m = l + (r-l)//2

            if nums[m] == target:
                ans = m
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return ans

    def lo(self, nums, target):
        l = 0
        r = len(nums) - 1
        ans = -1

        while l<=r:
            m = l + (r-l)//2

            if nums[m] == target:
                ans = m
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return ans
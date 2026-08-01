class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.ocurrence(nums, target, True), self.ocurrence(nums, target, False)]
        
    def ocurrence(self, nums, target, first):
        l = 0
        r = len(nums) - 1
        ans = -1

        while l<=r:
            m = l + (r-l)//2

            if nums[m] == target:
                ans = m
                if first:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return ans
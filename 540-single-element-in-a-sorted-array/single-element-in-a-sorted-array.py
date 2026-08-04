class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        pos = -1

        while l <= r:
            m = l + (r - l)//2

            if m == 0:
                return nums[0]
            if m == n - 1:
                return nums[-1]

            if nums[m-1] == nums[m]:
                if (m-1) % 2 == 1:
                    r = m - 2
                else:
                    l = m + 1
            elif nums[m+1] == nums[m]:
                if (m) % 2 == 1:
                    r = m - 1
                else:
                    l = m + 2
            else:
                return nums[m]

    



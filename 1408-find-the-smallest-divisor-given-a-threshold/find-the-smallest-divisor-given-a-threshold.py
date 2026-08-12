class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)
        minDivisor = r

        while l<=r:
            m=(l+r)//2

            if self.isPossible(nums, m, threshold):
                r = m - 1
                if minDivisor > m:
                    minDivisor = m
            else:
                l = m + 1

        return minDivisor

    def isPossible(self, arr, m, k):
        minSum = 0

        for i in arr:
            minSum += ceil(i/m)

        return minSum <= k
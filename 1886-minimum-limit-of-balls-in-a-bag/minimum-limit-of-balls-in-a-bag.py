import math

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        minPenalty = float('inf')

        while l<=r:
            m = (l + r) // 2

            # print(l, m, r)
            if self.isPossible(nums, maxOperations, m):
                r = m - 1
                if minPenalty > m:
                    minPenalty = m
            else:
                l = m + 1
        return minPenalty

    def isPossible(self, arr, maxop, m):
        opCount = 0

        for i in range(len(arr)):
            if arr[i]>m:
                opCount += math.ceil(arr[i]/m) - 1

        print(m, opCount)
        return opCount <= maxop

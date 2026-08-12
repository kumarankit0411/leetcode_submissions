class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        minSum = float('inf')

        while l<=r:
            m = (l + r) // 2
            # print(l, m, r)
            if self.isPossible(nums, m, k):
                if minSum > m:
                    minSum = m
                r = m - 1
            else:
                l = m + 1
        
        return minSum

    def isPossible(self, arr, m, k):
        have = 1
        currSum = 0

        for i in range(len(arr)):
            if currSum + arr[i] > m:
                have += 1
                currSum = arr[i]
            else:
                currSum += arr[i]

        return have <= k 
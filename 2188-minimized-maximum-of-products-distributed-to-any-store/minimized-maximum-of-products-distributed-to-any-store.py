class Solution:
    def minimizedMaximum(self, n: int, arr: List[int]) -> int:
        # return ceil(sum(arr)/n) # this solves more than half test cases
        l = 0
        r = max(arr)
        minX = r

        while l<=r:
            m=(l+r)//2
            if m==0:
                return 1
            if self.isPossible(arr, m, n):
                r = m - 1
                if minX > m:
                    minX = m
            else:
                l = m + 1
        return minX

    def isPossible(self, arr, m, k):
        shopsFilled = 0

        for i in arr:
            shopsFilled += ceil(i/m)

        return shopsFilled <= k
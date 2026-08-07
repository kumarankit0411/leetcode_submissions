class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n

        while l<=r:
            m = (l+r)//2

            sums = m*(m+1)/2

            if sums == n:
                return m
            elif sums < n:
                l = m + 1
            else:
                r = m - 1

        return r
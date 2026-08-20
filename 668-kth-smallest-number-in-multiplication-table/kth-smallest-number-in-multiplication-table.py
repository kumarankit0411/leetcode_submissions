class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l = 1
        r = m * n
        

        while l<=r:
            mid = (l + r) // 2

            if self.isPossible(m, n, mid, k):
                r = mid - 1
            else:
                l = mid + 1

        return l

    def isPossible(self, m, n, mid, k):
        count = 0
        for i in range(1, m + 1):
            count += min(mid//i, n)
        print(mid, count)
        return count > k - 1
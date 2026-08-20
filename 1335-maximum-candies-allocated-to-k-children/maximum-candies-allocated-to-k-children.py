class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        l = 1
        r = max(candies)
        max_candies = -float('inf')

        while l <= r:
            m = (l + r) // 2
            print(l, m, r)
            if self.isPossible(candies, k, m):
                l = m + 1
                if max_candies < m:
                    max_candies = m
            else:
                r = m - 1
        
        return max_candies

    def isPossible(self, arr, k, m):
        count = 0
        for i in arr:
            count += i//m

        return count >= k 


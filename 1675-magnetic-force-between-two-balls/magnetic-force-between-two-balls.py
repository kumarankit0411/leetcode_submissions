class Solution:
    def maxDistance(self, position: List[int], k: int) -> int:
        position.sort()
        l = 1
        r = max(position) - min(position)
        maxForce = l

        while l<=r:
            m = (l + r) // 2

            if self.isPossible(position, m, k):
                l = m + 1
                maxForce = m
            else:
                r = m - 1

        return maxForce

    def isPossible(self, arr, m, k):
        maxBalls = 1
        currForce = arr[0]

        for j in range(1, len(arr)):
            if abs(currForce - arr[j]) >= m:
                maxBalls += 1
                currForce = arr[j]

        return maxBalls >=k

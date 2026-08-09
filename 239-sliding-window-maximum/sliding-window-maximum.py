from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        output = []

        for j in range(len(nums)):
            while q and j - k >= q[0]:
                q.popleft()

            while q and nums[j] > nums[q[-1]]:
                q.pop()
            q.append(j)

            if j >= k - 1:
                output.append(nums[q[0]])

        return output
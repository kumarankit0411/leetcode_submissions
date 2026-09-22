import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0

    def addNum(self, num: int) -> None:
        if len(self.left) == 0 or -self.left[0] > num:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)

        if len(self.right) > len(self.left):
            x = heapq.heappop(self.right)
            heapq.heappush(self.left, -x)
        elif len(self.left) > len(self.right) + 1:
            x = heapq.heappop(self.left)
            heapq.heappush(self.right, -x)

        self.count += 1

    def findMedian(self) -> float:

        if self.count % 2 == 1: # odd case
            return -self.left[0]
        else: # even case
            return (-(self.left[0]) + self.right[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
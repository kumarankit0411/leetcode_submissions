import heapq

class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.deleted = set()
        self.count = 0

    def _clean_stack(self):
        while self.stack and self.stack[-1][1] in self.deleted:
            self.deleted.remove(self.stack[-1][1])
            self.stack.pop()
    
    def _clean_heap(self):
        while self.heap and -self.heap[0][1] in self.deleted:
            self.deleted.remove(-self.heap[0][1])
            heapq.heappop(self.heap)

    def push(self, x: int) -> None:
        self.stack.append((x, self.count))
        heapq.heappush(self.heap, (-x, -self.count))
        self.count += 1

    def pop(self) -> int:
        self._clean_stack()
        val, idx = self.stack.pop()
        self.deleted.add(idx)
        return val

    def top(self) -> int:
        self._clean_stack()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        self._clean_heap()
        return -self.heap[0][0]

    def popMax(self) -> int:
        self._clean_heap()
        neg_val, neg_idx = heapq.heappop(self.heap)
        val, idx = -neg_val, -neg_idx
        self.deleted.add(idx)
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
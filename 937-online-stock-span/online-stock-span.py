class StockSpanner:

    def __init__(self):
        self.stack_p = []
        self.stack_i = [0]
        self.res = []
        self.day = 1

    def next(self, price: int) -> int:
        while self.stack_p and self.stack_p[-1] <= price:
            self.stack_p.pop()
            self.stack_i.pop()

        res = self.day - self.stack_i[-1]

        self.stack_p.append(price)
        self.stack_i.append(self.day)
        
        self.day+=1
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
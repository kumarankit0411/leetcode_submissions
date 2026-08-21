class MyStack:

    def __init__(self):
        self.q1 = list()
        self.q2 = list()

    def push(self, x: int) -> None:
        self.q1.append(x)
        if (len(self.q2) != 0):
            self.q2.pop(0)
        self.q2.append(x)  

    def pop(self) -> int:
        val = self.q2.pop(0)
        second_last = None
        while len(self.q1) > 0:
            top = self.q1.pop(0)
            if len(self.q1) == 1:
                second_last = top
            if len(self.q1) != 0:
                self.q2.append(top)
        
        if second_last is not None:
            self.q1.append(second_last)

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

        return val

    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        return len(self.q2)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
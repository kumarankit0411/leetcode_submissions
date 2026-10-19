# class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, value: int) -> None:
#         if not self.stack:
#             self.stack.append([value, value])
#         else:
#             current_min = min(value, self.getMin())
#             self.stack.append([value, current_min])

#     def pop(self) -> None:
#         if self.stack:
#             self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1][0] if self.stack else None

#     def getMin(self) -> int:
#         return self.stack[-1][1] if self.stack else None


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
            self.min_val = value
        elif value < self.min_val:
            # encode the top value
            self.stack.append(2 * value - self.min_val)
            self.min_val = value
        else:
            self.stack.append(value)

    def pop(self) -> None:
        if not self.stack:
            return

        top_val = self.stack.pop()
        if top_val < self.min_val:
            #decode
            self.min_val = 2 * self.min_val - top_val

        if not self.stack:
            self.min_val = None

    def top(self) -> int:
        top_val = self.stack[-1]
        if top_val < self.min_val:
            return self.min_val
        
        return top_val
        
    def getMin(self) -> int:
        return self.min_val
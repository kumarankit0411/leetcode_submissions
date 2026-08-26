class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []

        for i in tokens:
            if i in operators:
                b = stack.pop()
                a = stack.pop()
                res = self.evalExpression(a, b, i)
                stack.append(res)
            else:
                stack.append(int(i))

        return stack[0]

    def evalExpression(self, a, b, op):
        print(a, b, op)
        a = int(a)
        b = int(b)
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            return int(a/b)
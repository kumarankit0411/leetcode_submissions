class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        curr_num = 0
        resolve = False
        is_num = False
        n=len(s)

        while i < n:
            if s[i] == ' ':
                i += 1
                continue

            if s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                # If preceding operator was * or /, resolve immediately
                if stack and stack[-1] in ('*', '/'):
                    op = stack.pop()
                    prev_val = stack.pop()
                    if op == '*':
                        stack.append(prev_val * num)
                    else:
                        stack.append(int(prev_val / num))
                else:
                    stack.append(num)
            else:
                # Append operator (+, -, *, /)
                stack.append(s[i])
                i += 1

        total = stack[0]
        for idx in range(1, len(stack), 2):
            op = stack[idx]
            val = stack[idx + 1]
            if op == '+':
                total += val
            else:
                total -= val

        return total

        # for i in stack:
        #     if 
        
        # return stack.pop()

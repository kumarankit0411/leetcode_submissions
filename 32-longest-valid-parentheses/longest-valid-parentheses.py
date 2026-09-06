class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = 0
        stack = []
        max_l = 0

        for i in s:
            if i=='(':
                stack.append(i)
            else: # i == ')'
                if stack and stack[-1] == '(':
                    stack.pop()
                    if stack and type(stack[-1]) is int:
                        stack[-1]+=2
                        continue
                    stack.append(2)
                elif stack and type(stack[-1]) is int:
                    s = 0
                    while stack and type(stack[-1]) is int:
                        s+=stack.pop()
                    if stack and stack[-1] == '(':
                        stack.pop()
                        stack.append(s + 2)
                    else:
                        stack.append(s)
                        stack.append(i)
                else:
                    stack.append(i)
            
        print(stack)
        for i in stack:
            if type(i) is int:
                l+=i
                if l > max_l:
                    max_l = l
            else:
                l=0   
        
        return max_l

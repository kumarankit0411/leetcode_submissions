class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i]=='(':
                stack.append((s[i], i))
            elif s[i]==')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((s[i], i))
        
        print(stack)
        if len(stack) == 0:
            return s

        for _, idx in stack:
            s = s[:idx] + '_' + s[idx + 1:]

        s = s.replace('_', '') 

        print(s)
        return(s)
            
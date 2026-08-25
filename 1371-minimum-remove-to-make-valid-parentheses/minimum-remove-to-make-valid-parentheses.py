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
        
        if len(stack) == 0:
            return s

        s_list = list(s)
        
        for _, idx in stack:
            s_list[idx] = ''

        s = ''.join(s_list)

        return(s)
            
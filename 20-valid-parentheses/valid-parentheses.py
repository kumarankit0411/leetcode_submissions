class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['{', '[', '(']
        closing = ['}', ']', ')']
        pair = {'}':'{', ']':'[', ')': '('}

        for p in s:
            if p in opening:
                stack.append(p)
            else:
                if len(stack)==0:
                    return False
                top = stack.pop()
                if top != pair[p]:
                    return False
        return len(stack) == 0
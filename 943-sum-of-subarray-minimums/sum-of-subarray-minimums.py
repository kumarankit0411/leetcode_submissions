class Solution:
    def find_nsor_span(self, arr):
        stack = []
        n = len(arr)
        res = [-1] * n

        for i in range(len(arr)-1, -1, -1):
            x = arr[i]

            while stack and stack[-1][0] >= x:
                stack.pop()

            res[i] = stack[-1][1] - i if stack else n - i

            stack.append((x, i))
        
        return res

    def find_nsol_span(self, arr):
        stack = []
        n = len(arr)
        res = [-1] * n

        for i in range(len(arr)):
            x = arr[i]

            while stack and stack[-1][0] > x:
                stack.pop()

            res[i] = i - stack[-1][1] if stack else i + 1

            stack.append((x, i))
        
        return res

    def sumSubarrayMins(self, arr: List[int]) -> int:
        nsor = self.find_nsor_span(arr)
        nsol = self.find_nsol_span(arr)

        total_sum = 0
        
        for i in range(len(arr)):
            total_sum += arr[i] * nsol[i] * nsor[i]

        return total_sum % (10**9 + 7)

        
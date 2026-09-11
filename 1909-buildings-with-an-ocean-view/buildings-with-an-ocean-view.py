class Solution:
    def find_ngor(self, arr):
        res = [-1] * len(arr)
        stack = []

        for i in range(len(arr) - 1, -1, -1):
            x = arr[i]

            while stack and stack[-1] < x:
                stack.pop()

            res[i] = stack[-1] if stack else -1

            stack.append(x)

        return res

    def findBuildings(self, arr: List[int]) -> List[int]:
        ngor = self.find_ngor(arr)
        output = []

        for i in range(len(arr)):
            if ngor[i] == -1:
                output.append(i)

        return output
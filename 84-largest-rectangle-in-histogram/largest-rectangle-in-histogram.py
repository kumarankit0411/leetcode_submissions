class Solution:
    def find_nsor_span(self, arr):
        res = [-1] * len(arr)
        stack = []
        n = len(arr)

        for i in range(len(arr) - 1, -1 , -1):
            x = arr[i]

            while stack and stack[-1][0] >= x:
                stack.pop()

            res[i] = stack[-1][1] - 1 if stack else n - 1

            stack.append((x, i))

        return res

    def find_nsol_span(self, arr):
        res = [-1] * len(arr)
        stack = []

        for i in range(len(arr)):
            x = arr[i]

            while stack and stack[-1][0] >= x:
                stack.pop()

            res[i] = stack[-1][1] + 1 if stack else 0

            stack.append((x, i))

        return res

    def largestRectangleArea(self, arr: List[int]) -> int:
        nsor = self.find_nsor_span(arr)
        nsol = self.find_nsol_span(arr)

        max_area = 0

        for i in range(len(arr)):
            area = arr[i] * (nsor[i] - nsol[i] + 1)

            if area > max_area:
                max_area = area

        return max_area
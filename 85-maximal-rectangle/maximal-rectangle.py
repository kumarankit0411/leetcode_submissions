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
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * len(matrix[0])
        max_area = 0

        for i in matrix:
            

            for j in range(len(i)):
                if i[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            nsor = self.find_nsor_span(heights)
            nsol = self.find_nsol_span(heights)
                
            for j in range(len(i)):
                max_area = max(max_area, heights[j] * (nsor[j] - nsol[j] + 1))
            
        return max_area
            
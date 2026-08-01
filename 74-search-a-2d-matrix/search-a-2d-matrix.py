class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix, target)
        print(row)
        targetRow = matrix[row]

        return self.binarySearch(targetRow, target)

    def binarySearch(self, arr, t):
        l = 0
        r = len(arr) - 1

        while l<=r:
            m = l + (r-l)//2

            if arr[m] == t:
                return True
            elif arr[m] > t:
                r = m - 1
            else:
                l = m + 1
            
        return False

    def findRow(self, matrix, t):
        l = 0
        r = len(matrix) - 1

        while l<=r:
            m = (l + r)//2

            if t >= matrix[m][0] and t <= matrix[m][-1]:
                return m
            if t < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1

        return r
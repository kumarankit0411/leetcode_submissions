class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        position = self.findPosition(arr, x)
        
        n = len(arr)
        
        if position == 0:
            return arr[:k]

        if position == n:
            return arr[(n-k):]

        i = max(position - 1, 0)
        j = position

        while(k>0):
            i_distance = abs(arr[i] - x)
            j_distance = abs(arr[j] - x)

            if i_distance <= j_distance:
                i = i-1
                if i<0:
                    j = j + k - 1
                    break
            else:
                j = j+1
                if j>n-1:
                    i = i-k+1
                    break

            k-=1
        
        return arr[i+1:j]


    def findPosition(self, arr, x):
        l = 0
        r = len(arr) - 1

        while l<=r:
            m = l + (r - l)//2

            if arr[m] == x:
                return m
            elif arr[m] < x:
                l = m + 1
            else:
                r = m - 1
        
        return l
        

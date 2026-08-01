class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n =len(arr)
        l = 0
        r = n - 1
        m = -1

        while l!=m:
            m = l + (r - l)//2

            if(m == n - 1):
                return m
            if arr[m+1] < arr[m]:
                r = m
            else:
                l = m+1

        return m
            


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l<r:
            m = l + (r-l)//2

            hoursNeeded = self.calHours(piles, m)
            if hoursNeeded > h:
                l = m + 1
            else:
                r = m
        
        return r

    def calHours(self, arr, target):
        hours = 0
        for i in range(len(arr)):
            hours += ceil(arr[i]/target)
        
        return hours

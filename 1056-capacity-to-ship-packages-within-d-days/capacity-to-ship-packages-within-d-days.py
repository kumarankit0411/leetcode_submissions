class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        min_weight = r

        while l<=r:
            m = l + (r-l)//2
            daysNeeded = self.calDays(weights, m)
            if daysNeeded <= days:
                min_weight = min(m, min_weight)
            if daysNeeded > days:
                l = m + 1
            else:
                r = m - 1

        return min_weight

    def calDays(self, arr, x):
        days = 0
        sums = 0
        for i in range(len(arr)):
            sums+=arr[i]
            if sums > x:
                days+=1
                sums = arr[i]
            elif sums == x:
                days+=1
                sums = 0
        
        
        if sums > 0:
            days+=1

        print(days, x)
        return days

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        l = 1
        r = max(bloomDay)
        minDays = float('inf')

        while l<=r:
            mid = (l + r)//2
            # print(l, mid, r)
            isPossible = self.isBouquetPossible(bloomDay, mid, m, k)

            if isPossible:
                minDays = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return minDays

    def isBouquetPossible(self, arr, mid, m, k):
        bloomArr = [0] * len(arr)

        for i in range(len(arr)):
            if arr[i] <= mid:
                bloomArr[i] = 1
        
        have = 0
        continuous = 0
        for i in range(len(bloomArr)):
            # if i == 0:
            #     if bloomArr[i] == 1:
            #         isContinuous = 1
            # elif bloomArr[i] == 1:
            #     if bloomArr[i-1] == 1:
            #         isContinuous += 1
            #     else:
            #         isContinuous = 1
            # else:
            #     isContinuous = 0
            # if isContinuous == k:
            #     have += 1
            #     isContinuous = 0
            if bloomArr[i] == 1:
                continuous +=1
            else:
                continuous = 0
            if continuous == k:
                have+=1
                continuous = 0
        # print(mid, bloomArr, have)

        if have >= m:
            return True
        else:
            return False
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 0
        r = mountainArr.length() - 1

        while l<r:
            m = l + (r-l)//2

            if mountainArr.get(m) < mountainArr.get(m+1):
                l = m + 1
            else:
                r = m

        peak_index = l

        # find in first subArray:
        pos1 = self.searchInLeft(mountainArr, target, 0, l)
        pos2 = self.searchInRight(mountainArr, target, l, mountainArr.length())

        # print(pos1, pos2)
        if pos1==-1 and pos2==-1:
            return -1
        else:
            if pos1==-1:
                return pos2
            else:
                return pos1

    def searchInLeft(self, arr, t, i, j):
        l = i
        r = j - 1
        pos = -1

        while l<=r:
            m = l + (r-l)//2
            ele = arr.get(m)

            print(ele)

            if ele > t:
                r = m - 1
            elif ele < t:
                l = m + 1
            else:
                pos = m
                r = m - 1

        if pos!=-1:
            return pos
        else:
            return -1

    def searchInRight(self, arr, t, i, j):
        l = i
        r = j - 1
        pos = -1

        while l<=r:
            m = l + (r-l)//2
            ele = arr.get(m)

            print(ele)

            if ele > t:
                l = m + 1
            elif ele < t:
                r = m - 1
            else:
                pos = m
                r = m - 1

        if pos!=-1:
            return pos
        else:
            return -1


        
        
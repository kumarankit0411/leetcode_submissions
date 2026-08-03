class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ## brute force
        # res = []
        # min_next = float('inf')
        # min_index = -1
        # for i in range(len(intervals)):
        #     for j in range(len(intervals)):
        #         if i == j:
        #             continue
        #         else:
        #             if intervals[j][0] >= intervals[i][1]:
        #                 if intervals[j][0] < min_next:
        #                     min_index = j
        #                     min_next = intervals[j][0]
        #     if min_index != -1:
        #         res.append(min_index)
        #     else:
        #         res.append(-1)

        #     min_index = -1
        #     min_next = float('inf')

        # return res

        ## optimal O(nlogn)
        arr = []
        res = []
        for i in range(len(intervals)):
            arr.append([intervals[i][0], i])
        
        arr.sort()

        for i in range(len(intervals)):
            res.append(self.findNext(arr, i, intervals[i][1]))
        
        return res

    def findNext(self, sorted_arr, ignore_index, end):
        l = 0
        r = len(sorted_arr) - 1
        m = -1

        while(l<=r):
            m = l + (r-l)//2

            if sorted_arr[m][0] < end:
                l = m + 1
            elif sorted_arr[m][0] == end:
                # if ignore_index == sorted_arr[m][1]:
                #     r = m - 1
                # else:
                return sorted_arr[m][1]
            else:
                # if ignore_index == sorted_arr[m][1]:
                #     r = m - 1
                # else:
                if l == r:
                    return sorted_arr[m][1]
                r = m
        return -1


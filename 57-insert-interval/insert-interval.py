class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = []
        st = intervals[0][0]
        end = intervals[0][1]

        for i in range(len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                merged.append([st, end])
                st = intervals[i][0]
                end = intervals[i][1]

        merged.append([st, end])

        return merged
    
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new_arr = []
        if not intervals:
            return [newInterval]

        added = False
        for a in intervals:
            if a[0] > newInterval[0]:
                added = True
                new_arr.append(newInterval)
            new_arr.append(a)
        if not added:
            new_arr.append(newInterval)
        print(new_arr)

        return self.merge(new_arr)


        
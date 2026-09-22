class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x:x[0])

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
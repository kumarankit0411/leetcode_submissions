class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l=0
        r=len(citations) - 1
        n = len(citations)
        pos = 0

        while l<=r:
            m = l + (r-l)//2

            if citations[m] >= n-m:
                pos = n - m
                r = m - 1
            else:
                l = m + 1

        return pos
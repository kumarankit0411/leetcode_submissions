class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        m=1

        while l<=r:
            m = l + (r-l)//2
            sqr = m*m

            if sqr == x:
                return m
            elif sqr > x:
                r = m-1
            else:
                l = m+1

        return r
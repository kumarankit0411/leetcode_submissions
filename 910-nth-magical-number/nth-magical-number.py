import math
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l = min(a, b)
        r = n * min(a, b)
        lcm = math.lcm(a,b)

        while l<=r:
            m = (l+r)//2

            if self.isPossible(m, n, a, b, lcm):
                r = m - 1
            else:
                l = m + 1

        return l % (10**9 + 7)

    def isPossible(self, m, n, a, b, lcm):
        total = m//a + m//b - m//lcm

        return total >= n
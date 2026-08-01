class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num

        while(l<=r):
            m = (l + r)//2

            if l==r-1 and m*m!=num:
                return False
            if m*m == num:
                return True
            if m*m > num:
                r = m
            else:
                l = m


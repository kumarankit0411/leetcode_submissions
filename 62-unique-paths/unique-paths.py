class Solution:
    def noOfWays_tab(self, m, n):
        dp = [[-1]*n for _ in range(m)]

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 and c==n-1:
                    dp[r][c] = 1
                elif r == m-1:
                    dp[r][c] = 1
                elif c == n-1:
                    dp[r][c] = 1
                else:
                    ra1 = dp[r][c+1]
                    ra2 = dp[r+1][c]
                    dp[r][c] = ra1+ra2
        return dp[0][0]            

    def noOfWays_memo(self, sr, sc, dr, dc, dp):
        if sr>dr or sc>dc:
            return 0
        if sr==dr and sc==dc:
            return 1

        if dp[sr][sc]!=-1:
            return dp[sr][sc]
        
        ra1 = self.noOfWays_memo(sr+1, sc, dr, dc, dp)
        ra2 = self.noOfWays_memo(sr, sc+1, dr, dc, dp)
        ma = ra1 + ra2
        dp[sr][sc] = ma
        return ma

    def noOfWays(self, sr, sc, dr, dc):
        if sr>dr or sc>dc:
            return 0
        if sr==dr and sc==dc:
            return 1
        
        ra1 = self.noOfWays(sr+1, sc, dr, dc)
        ra2 = self.noOfWays(sr, sc+1, dr, dc)
        ma = ra1 + ra2
        return ma

    def uniquePaths(self, m: int, n: int) -> int:
        # normal recursion
        # return self.noOfWays(0, 0, m-1, n-1)
        
        # memoization recursion
        # dp = [[-1]*n for _ in range(m)]
        # return self.noOfWays_memo(0, 0, m-1, n-1, dp)

        # tabulation
        return self.noOfWays_tab(m, n)
class Solution:
    def mps_rec_memo(self, sr, sc, dr, dc, dp, arr):
        if sr == dr and sc == dc:
            return arr[sr][sc]
        if sr>dr or sc>dc:
            return float('inf')
        if dp[sr][sc]!=-1:
            return dp[sr][sc]
        ra1 = self.mps_rec_memo(sr+1, sc, dr, dc, dp, arr)
        ra2 = self.mps_rec_memo(sr, sc+1, dr, dc, dp, arr)
        ma = min(ra1, ra2) + arr[sr][sc]
        dp[sr][sc] = ma
        return ma
        
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = [[-1]*len(grid[0]) for _ in range(len(grid))]

        return self.mps_rec_memo(0, 0, len(grid)-1, len(grid[0])-1, dp, grid)
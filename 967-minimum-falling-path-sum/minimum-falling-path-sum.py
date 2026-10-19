class Solution:
    def mfps_rec(self, sr, sc, dr, dc, arr, dp, vis):
        if sc<0 or sc>dc:
            return float('inf')
        if vis[sr][sc] == True:
            return dp[sr][sc]
        if sr==dr:
            return arr[sr][sc]

        ra1 = self.mfps_rec(sr+1, sc, dr, dc, arr, dp, vis)
        ra2 = self.mfps_rec(sr+1, sc-1, dr, dc, arr, dp, vis)
        ra3 = self.mfps_rec(sr+1, sc+1, dr, dc, arr, dp, vis)

        ma = min(ra1, ra2, ra3) + arr[sr][sc]
        dp[sr][sc] = ma
        vis[sr][sc] = True
        return ma

    def minFallingPathSum(self, arr: list[list[int]]) -> int:
        noc = len(arr[0])
        nor = len(arr)
        fans = float('inf')
        dp = [[-1]*noc for _ in range(nor)]
        vis = [[False]*noc for _ in range(nor)]
        for i in range(0, noc):
            ans = self.mfps_rec(0, i, nor-1, noc -1, arr, dp, vis)
            fans = min(ans, fans)
        return fans
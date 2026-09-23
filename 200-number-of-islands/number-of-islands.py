class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        noi = 0

        rows, cols = len(grid), len(grid[0])

        def dfs(i, j, grid):
            if i<0 or i>rows-1 or j<0 or j>cols-1 or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'

            dfs(i+1, j, grid)
            dfs(i, j+1, grid)
            dfs(i-1, j, grid)
            dfs(i, j-1, grid)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    noi+=1
                    dfs(i, j, grid)

        return noi
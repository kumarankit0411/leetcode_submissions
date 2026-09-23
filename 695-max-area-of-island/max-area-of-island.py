class Solution:
    def dfs(self, grid, i, j, count):
        grid[i][j] = 0
        count+=1
        
        if i-1 >=0 and grid[i-1][j] == 1:
            count = self.dfs(grid, i-1, j, count)
        if j-1 >=0 and grid[i][j-1] == 1:
            count =self.dfs(grid, i, j-1, count)
        if j+1 < len(grid[0]) and grid[i][j+1] == 1:
            count =self.dfs(grid, i, j+1, count)
        if i+1 < len(grid) and grid[i+1][j] == 1:
            count = self.dfs(grid, i+1, j, count)

        return count

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j, 0)
                    max_area = max(area, max_area)

        return max_area
class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        noi = 0

        rows, cols = len(grid), len(grid[0])
        shapes = set()

        def dfs(i, j, i0, j0, grid, shape):
            if i<0 or i>rows-1 or j<0 or j>cols-1 or grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            shape.append((i-i0, j-j0))

            dfs(i+1, j, i0, j0, grid, shape)
            dfs(i, j+1, i0, j0,  grid, shape)
            dfs(i-1, j, i0, j0, grid, shape)
            dfs(i, j-1, i0, j0, grid, shape) 

            return shape          

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    shape = dfs(i, j, i, j, grid, [])
                    shapes.add(tuple(shape))
                    
        return len(shapes)
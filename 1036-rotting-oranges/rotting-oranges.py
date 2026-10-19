class Solution:
    class Orange:
        def __init__(self, i, j, time):
            self.i = i
            self.j = j
            self.time = time

    def orangesRotting(self, grid: list[list[int]]) -> int:
        fc = 0
        rc = 0
        q = deque()
        time = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rc+=1
                    q.append(self.Orange(i, j, 0))
                elif grid[i][j] == 1:
                    fc+=1
        
        while len(q) > 0:
            fnt = q.popleft()

            if grid[fnt.i][fnt.j] == 3:
                continue
            if grid[fnt.i][fnt.j] == 1:
                fc-=1
            
            grid[fnt.i][fnt.j] = 3
            time = max(time, fnt.time)

            dir = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1]
            ]

            i = fnt.i
            j = fnt.j

            for d in dir:
                ni = i + d[0]
                nj = j + d[1]
        
                if (ni>=0 and nj>=0 and ni<len(grid) and nj < len(grid[0]) and grid[ni][nj]!=3 and grid[ni][nj] == 1):
                    q.append(self.Orange(ni, nj, fnt.time + 1))

        if fc!=0:
            return -1
        return time
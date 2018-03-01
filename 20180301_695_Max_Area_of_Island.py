class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, 1+self.dfs(grid, i, j))
        
        return max_area
    
    def dfs(self, grid, x, y):
        grid[x][y] = 0
        area = 0
        if x == len(grid)-1:
            if grid[x-1][y]==1:
                area = area + grid[x-1][y]
                grid[x-1][y] = 0
                area = area + self.dfs(grid, x-1, y)
        elif x == 0:
            if grid[x+1][y]==1:
                area = area + grid[x+1][y]
                grid[x+1][y] = 0
                area = area + self.dfs(grid, x+1, y)
        else:
            if grid[x+1][y]==1:
                area = area + grid[x+1][y]
                grid[x+1][y] = 0
                area = area + self.dfs(grid, x+1, y)
            if grid[x-1][y]==1:
                area = area + grid[x-1][y]
                grid[x-1][y] = 0
                area = area + self.dfs(grid, x-1, y)
        if y == len(grid[0])-1:
            if grid[x][y-1]==1:
                area = area + grid[x][y-1]
                grid[x][y-1] = 0
                area = area + self.dfs(grid, x, y-1)
        elif y == 0:
            if grid[x][y+1]==1:
                area = area + grid[x][y+1]
                grid[x][y+1] = 0
                area = area + self.dfs(grid, x, y+1)
        else:
            if grid[x][y+1]==1:
                area = area + grid[x][y+1]
                grid[x][y+1] = 0
                area = area + self.dfs(grid, x, y+1)
            if grid[x][y-1]==1:
                area = area + grid[x][y-1]
                grid[x][y-1] = 0
                area = area + self.dfs(grid, x, y-1)    
        return area

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= column or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0  # mark visited
            
            return (1 +
                    dfs(i+1, j) +
                    dfs(i-1, j) +
                    dfs(i, j+1) +
                    dfs(i, j-1))

        max_area = 0

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area
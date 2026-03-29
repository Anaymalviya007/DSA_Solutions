class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j>= column or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
            

        number_of_island = 0

        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    number_of_island += 1
                    dfs(i,j)

        return number_of_island

from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        total_rows = len(grid)
        total_cols = len(grid[0])
        
        queue = deque()
        INF = 2147483647
        
        # Step 1: Add all treasure cells to queue
        for row in range(total_rows):
            for col in range(total_cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        # Possible 4 directions (down, up, right, left)
        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]
        
        # Step 2: Multi-source BFS
        while queue:
            current_row, current_col = queue.popleft()
            
            for row_offset, col_offset in directions:
                next_row = current_row + row_offset
                next_col = current_col + col_offset
                
                # Check boundaries and ensure it's an unvisited land cell
                if (
                    0 <= next_row < total_rows and
                    0 <= next_col < total_cols and
                    grid[next_row][next_col] == INF
                ):
                    # Update distance from nearest treasure
                    grid[next_row][next_col] = grid[current_row][current_col] + 1
                    
                    # Add to queue for further expansion
                    queue.append((next_row, next_col))



                    
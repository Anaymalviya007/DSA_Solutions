from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_rows = len(grid)
        total_cols = len(grid[0])
        
        queue = deque()
        fresh_orange_count = 0
        
        # Step 1: Initialize queue with all rotten oranges
        for row in range(total_rows):
            for col in range(total_cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_orange_count += 1
        
        # If no fresh oranges, time = 0
        if fresh_orange_count == 0:
            return 0
        
        directions = [
            (1, 0), (-1, 0),
            (0, 1), (0, -1)
        ]
        
        minutes_elapsed = 0
        
        # Step 2: BFS (level by level)
        while queue:
            current_level_size = len(queue)
            infection_happened = False
            
            for _ in range(current_level_size):
                current_row, current_col = queue.popleft()
                
                for row_offset, col_offset in directions:
                    next_row = current_row + row_offset
                    next_col = current_col + col_offset
                    
                    if (
                        0 <= next_row < total_rows and
                        0 <= next_col < total_cols and
                        grid[next_row][next_col] == 1
                    ):
                        # Rot the fresh orange
                        grid[next_row][next_col] = 2
                        fresh_orange_count -= 1
                        queue.append((next_row, next_col))
                        infection_happened = True
            
            # Only increment time if something changed
            if infection_happened:
                minutes_elapsed += 1
        
        # If fresh oranges remain → impossible
        return minutes_elapsed if fresh_orange_count == 0 else -1
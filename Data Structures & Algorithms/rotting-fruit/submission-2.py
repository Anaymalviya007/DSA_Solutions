from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total_row = len(grid)
        total_column = len(grid[0])
        queue = deque()
        fresh_orange_count = 0

        for row in range(total_row):
            for column in range(total_column):
                if grid[row][column] == 2:
                    queue.append((row, column))
                if grid[row][column] == 1:
                    fresh_orange_count += 1

        if fresh_orange_count == 0:
            return 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        minutes_elapsed = 0

        while queue:
            current_level_size = len(queue)
            infection_happened = False

            for _ in range(current_level_size):
                current_row, current_column = queue.popleft()

                for row_offset, column_offset in directions:
                    next_row = current_row + row_offset
                    next_column = current_column + column_offset

                    if (0 <= next_row < total_row and 0 <= next_column < total_column and grid[next_row][next_column] == 1):
                        grid[next_row][next_column] = 2
                        fresh_orange_count -= 1
                        queue.append((next_row, next_column))
                        infection_happened = True

            if infection_happened:
                minutes_elapsed += 1

        return minutes_elapsed if fresh_orange_count == 0 else -1









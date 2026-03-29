class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                if (r, val) in seen or (val, c) in seen or ((r//3, c//3), val) in seen:
                    return False

                seen.add((r, val))
                seen.add((val, c))
                seen.add(((r//3, c//3), val))

        return True
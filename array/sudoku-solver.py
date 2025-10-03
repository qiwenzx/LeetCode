class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(r, c, val):
            # check row and column
            for i in range(9):
                if board[r][i] == val or board[i][c] == val:
                    return False
            # check 3x3 box
            box_row, box_col = 3 * (r // 3), 3 * (c // 3)
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    if board[i][j] == val:
                        return False
            return True

        def backtrack():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":  # empty cell
                        for d in map(str, range(1, 10)):
                            if is_valid(r, c, d):
                                board[r][c] = d
                                if backtrack():
                                    return True
                                board[r][c] = "."  # undo
                        return False  # no valid digit → backtrack
            return True  # solved

        backtrack()
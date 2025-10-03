class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # def is_valid(r, c, val):
        #     # check row and column
        #     for i in range(9):
        #         if board[r][i] == val or board[i][c] == val:
        #             return False
        #     # check 3x3 box
        #     box_row, box_col = 3 * (r // 3), 3 * (c // 3)
        #     for i in range(box_row, box_row + 3):
        #         for j in range(box_col, box_col + 3):
        #             if board[i][j] == val:
        #                 return False
        #     return True

        # def backtrack():
        #     for r in range(9):
        #         for c in range(9):
        #             if board[r][c] == ".":  # empty cell
        #                 for d in map(str, range(1, 10)):
        #                     if is_valid(r, c, d):
        #                         board[r][c] = d
        #                         if backtrack():
        #                             return True
        #                         board[r][c] = "."  # undo
        #                 return False  # no valid digit → backtrack
        #     return True  # solved

        # backtrack()

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # initialize
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(idx=0):
            if idx == len(empties):
                return True  # solved

            r, c = empties[idx]
            b = (r // 3) * 3 + (c // 3)

            for d in map(str, range(1, 10)):
                if d not in rows[r] and d not in cols[c] and d not in boxes[b]:
                    # place digit
                    board[r][c] = d
                    rows[r].add(d); cols[c].add(d); boxes[b].add(d)

                    if backtrack(idx+1):
                        return True

                    # undo
                    board[r][c] = "."
                    rows[r].remove(d); cols[c].remove(d); boxes[b].remove(d)

            return False

        backtrack()
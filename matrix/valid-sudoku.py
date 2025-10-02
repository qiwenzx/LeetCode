class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Method 1
        # rows = [set() for _ in range(9)]
        # cols = [set() for _ in range(9)]
        # boxes = [set() for _ in range(9)]

        # for r in range(9):
        #     for c in range(9):
        #         val = board[r][c]
        #         if val == ".":
        #             continue
                
        #         if val in rows[r]:
        #             return False
        #         rows[r].add(val)

        #         if val in cols[c]:
        #             return False
        #         cols[c].add(val)

        #         box_index = (r // 3) * 3 + (c // 3)
        #         if val in boxes[box_index]:
        #             return False
        #         boxes[box_index].add(val)

        # return True

        # Method 2:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val != ".":
                    box_index = (i // 3) * 3 + (j // 3)
                    row_set = rows[i]
                    col_set = cols[j]
                    box_set = boxes[box_index]

                    if (val in row_set) or (val in col_set) or (val in box_set):
                        return False
                    row_set.add(val)
                    col_set.add(val)
                    box_set.add(val)
        return True



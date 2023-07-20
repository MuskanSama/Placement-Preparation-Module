class Solution(object):
    def isValidSudoku(self, board):

        def is_valid_unit(unit):
            unit = [x for x in unit if x != '.']
            return len(unit) == len(set(unit))

        def is_valid_rows():
            for row in board:
                if not is_valid_unit(row):
                    return False
            return True

        def is_valid_columns():
            for col in zip(*board):
                if not is_valid_unit(col):
                    return False
            return True

        def is_valid_sub_boxes():
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                    if not is_valid_unit(sub_box):
                        return False
            return True

        return is_valid_rows() and is_valid_columns() and is_valid_sub_boxes()

        
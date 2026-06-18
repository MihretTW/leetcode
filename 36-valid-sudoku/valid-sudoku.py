class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        # check columns
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        # check 3x3 boxes
        for box_i in range(3):
            for box_j in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[3*box_i + i][3*box_j + j]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)

        return True
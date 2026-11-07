class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        blocks = [set() for _ in range(9)]

        for i in range(9):
            row = set()
            col = set()

            for j in range(9):
                a = board[i][j]
                b = board[j][i]

                if a != '.':
                    if a in row:
                        return False
                    row.add(a)

                    if a in blocks[i//3+j//3*3]:
                        return False
                    blocks[i//3+j//3*3].add(a)

                if b != '.':
                    if b in col:
                        return False
                    col.add(b)

        return True
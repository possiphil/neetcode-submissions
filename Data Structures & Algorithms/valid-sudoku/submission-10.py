class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        blocks = [0] * 9
        row = [0] * 9
        col = [0] * 9

        for i in range(9):
            

            for j in range(9):
                n = board[i][j]

                if n == ".":
                    continue
                
                v = 1 << int(n)-1
                if v & row[i] | v & col[j] | v & blocks[i//3+j//3*3]:
                    return False
                
                row[i] |= v
                col[j] |= v
                blocks[i//3+j//3*3] |= v

        return True
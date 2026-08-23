class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            rowMap = {}
            for c in range(9):
                num = board[r][c]
                if num != "." and num in rowMap:
                    return False
                rowMap[num] = 1

        for c in range(9):
            colMap = {}
            for r in range(9):
                num = board[r][c]
                if num != "." and num in colMap:
                    return False
                colMap[num] = 1
        
        colMult = 0
        rowMult = 0
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                squareMap = {}
                for i in range(3):
                    for j in range(3):
                        num = board[r+i][c+j]
                        if num != "." and num in squareMap:
                            return False
                        squareMap[num] = 1
        
        return True
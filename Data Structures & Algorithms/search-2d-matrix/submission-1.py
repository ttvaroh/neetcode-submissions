class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix[0])
        l, r = 0, rowLen*len(matrix)-1

        while l < r:
            m = l + (r-l) // 2
            row = m // rowLen
            col = m % rowLen
            if matrix[row][col] == target: return True
            elif matrix[row][col] < target: l = m+1
            else: r = m-1
        if matrix[l//rowLen][l%rowLen] == target: return True
        return False
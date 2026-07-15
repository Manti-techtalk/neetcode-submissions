class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix)
        row = len(matrix[0])

        # print("expect 4 cols, 3 rows")
        # print(row,col)
        
        for r in range(col):
            print(matrix[r])
            for c in range(row):
                if matrix[r][c] == target:
                    return True
        
        return False
        
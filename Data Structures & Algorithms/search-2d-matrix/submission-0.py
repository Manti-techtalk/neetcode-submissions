class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            print(matrix[i])
            if target in matrix[i]:
                return True
        return False
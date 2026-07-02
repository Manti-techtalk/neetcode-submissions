class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c,r = len(matrix), len(matrix[0])

        left, right = 0, c * r - 1

        while left <= right:
            mid = left + (right - left)// 2
            row = mid // r
            col = mid % r

            val = matrix[row][col]

            if val == target:
                return True

            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
        
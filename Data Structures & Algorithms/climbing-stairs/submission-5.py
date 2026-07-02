class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        elif n == 2:
            return 2
        
        # Initialize variables to store the number of ways to reach the first and second steps
        first, second = 1, 2
        
        # Use a loop to calculate the number of ways to reach each step from 3 to n
        for i in range(3, n + 1):
            first, second = second, first + second
        
        return second

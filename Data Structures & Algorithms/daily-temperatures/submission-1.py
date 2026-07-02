class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # stores (temperature, index)

        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                prev_temp, day = stack.pop()
                res[day] = i - day
            stack.append((temperatures[i], i))

        return res

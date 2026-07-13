from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        temp = temperatures
        res = [0] * len(temp)

        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res

        
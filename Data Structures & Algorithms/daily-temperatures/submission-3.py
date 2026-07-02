class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] 
        for i in range(len(temperatures)):
            curT = temperatures[i]
            while stack and curT > stack[-1][0]:
                prevTem, prevDay = stack.pop()
                res[prevDay] = i - prevDay
            stack.append((temperatures[i],i))
        return res
        
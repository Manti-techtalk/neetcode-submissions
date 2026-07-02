class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        print(res)
        k = 0 
        for i in range(n):
            while stack and temperatures[i] >  stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((temperatures[i],i))
        return res
                
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = [0] * len(temperatures)
        temp = temperatures

        for i in range(len(temp)):
            while st and temp[st[-1]] < temp[i]:
                idx = st.pop()
                ans[idx] = i - idx
            st.append(i)
        return ans
        
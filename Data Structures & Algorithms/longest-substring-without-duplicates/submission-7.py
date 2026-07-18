class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        c = 0
        res = []

        for char in s:
            if char in seen:
                c = 0
                seen.clear()
                seen.add(char)
            seen.add(char)
            c += 1
            res.append(c)
        return max(res) if res else 0

        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        res = 0
        for i  in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            print(d)

            """
            if currentwinsize - max(d.value) > k: # we have invalid window
                d[s[l]] -= 1
                l += 1
            res = max(res, currentsize)
            """

            while (i - l + 1) - max(d.values()) > k: #invalid window
                d[s[l]] -= 1
                l += 1

            res = max(res , i-l + 1)
        return res
        
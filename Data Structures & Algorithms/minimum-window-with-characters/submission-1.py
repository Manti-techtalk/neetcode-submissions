class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}  # count of t
        d1 = {} # count in current window
        l, r = 0, 0
        formed = 0
        win = ""
        min_len = float('inf')

        # count t
        for char in t:
            d[char] = d.get(char, 0) + 1
        required = len(d)

        while r < len(s):
            char = s[r]
            d1[char] = d1.get(char, 0) + 1

            if char in d and d1[char] == d[char]:
                formed += 1

            # shrink the window
            while l <= r and formed == required:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    win = s[l:r+1]

                left_char = s[l]
                d1[left_char] -= 1
                if left_char in d and d1[left_char] < d[left_char]:
                    formed -= 1
                l += 1

            r += 1

        return win

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        d = {}   # count of t
        d1 = {}  # count in current window
        l, r = 0, 0
        formed = 0
        win = ""
        min_len = float('inf')

        # count t in your style
        for char in t:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        required = len(d)

        while r < len(s):
            # add s[r] to window count
            char = s[r]
            if char in d1:
                d1[char] += 1
            else:
                d1[char] = 1

            # check if this char satisfies t
            if char in d and d1[char] == d[char]:
                formed += 1

            # try to shrink the window
            while l <= r and formed == required:
                # update min window
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    win = s[l:r+1]

                # remove s[l] from window
                left_char = s[l]
                d1[left_char] -= 1
                if left_char in d and d1[left_char] < d[left_char]:
                    formed -= 1
                l += 1

            r += 1

        return win

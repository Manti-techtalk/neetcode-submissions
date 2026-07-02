class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = {}   # frequency map for t
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        window = {} # frequency map for current window
        have = 0
        need_count = len(need)
        res_len = float("inf")
        res = ""    # store the smallest window

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # if current char satisfies requirement
            if c in need and window[c] == need[c]:
                have += 1

            # when window satisfies all needs, try shrinking it
            while have == need_count:
                # update result if smaller window found
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = s[l:r+1]

                # shrink from the left
                left_char = s[l]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                l += 1

        return res

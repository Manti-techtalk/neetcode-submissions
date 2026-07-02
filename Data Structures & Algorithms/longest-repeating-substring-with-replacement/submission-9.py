class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        res = 0

        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            #print(d)
            #cursize = i - l + 1
            #print(cursize)
            while (i - l + 1) - max(d.values()) > k:
                #print("Invalid window")
                d[s[l]] -= 1
                l += 1
            res = max(res,i - l + 1)
        return res


            
        
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        sq = "[]"
        br = "{}"
        pr = "()"
        for i in range(len(s)):
            print(s[i])
            if sq in s or br in s or pr in pr:
                s.replace(sq,"")
                s.replace(br,"")
                s.replace(pr,"")

        return len(s) !=0
        
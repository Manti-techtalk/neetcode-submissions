class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            if ''.join(sorted(s)) == ''.join(sorted(t)):
                return True
        return False
        
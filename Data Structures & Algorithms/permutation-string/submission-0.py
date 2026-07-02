class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        winSize = len(s1)
        n = len(s1)
        for i in range(len(s2)):
            win = s2[i:i + n ]
            print(win)
            if ''.join(sorted(win)) == ''.join(sorted(s1)):
                return True
        return False
        
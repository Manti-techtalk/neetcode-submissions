class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        print(n)

        for i in range(len(s2)-n + 1):
            curwin = s2[i:i + n]
            if ''.join(sorted(curwin)) == ''.join(sorted(s1)):
                return True
        return False
        
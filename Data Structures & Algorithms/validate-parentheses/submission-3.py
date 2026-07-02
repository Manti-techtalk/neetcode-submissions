class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')':'(','}':'{',']':'['}
        print(d)
        for br in s:
            if br in d:
                if not stack or stack[-1] != d[br]:
                    return False
                stack.pop()
            else:
                stack.append(br)
        return not stack
        
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for br in s:
            if br == '(' or br == "[" or br =="{":
                stack.append(br)
            elif br == "}" or br == "]" or br == ")":
                if not stack:
                    return False

                elif (br == "}" and stack[-1] != "{") or (br == "]" and stack[-1] != "[") or (br == ")" and stack[-1] != "("):
                    return False
                else:
                    stack.pop()

        
        return not stack
        
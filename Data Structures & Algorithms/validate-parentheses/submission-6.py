from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        # lets add the opening brackets to the stack
        for br in s:
            if br == "(" or br == "{" or br == "[":
                stack.append(br)

        #look for closing brackets
        print("Closing",stack)

        for br in s:
            if br == ")":
                if "(" in stack:
                    stack.pop()

            elif br == "]":
                if "[" in stack:
                    stack.pop()
            elif br == "}":
                if "{" in stack:
                    stack.pop()

        print("Finale", stack)
        return not stack

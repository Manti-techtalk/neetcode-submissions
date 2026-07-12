from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        # lets add the opening brackets to the stack
        c = 0
        for br in s:
            if br == "(" or br == "{" or br == "[":

                stack.append(br)
                c += 1

        #look for closing brackets
        print("Closing",c)

        for br in s:
            if br == ")":
                if "(" in stack:
                    c -= 1

            elif br == "]":
                if "[" in stack:
                    c -= 1
            elif br == "}":
                if "{" in stack:
                    c-= 1

        print("Finale", c)
        return c == 0

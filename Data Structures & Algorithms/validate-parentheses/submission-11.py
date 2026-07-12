from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack =  ""
        # lets add the opening brackets to the stack
        for br in s:
            if br == "(" or br == "{" or br == "[":

                stack += br

        #look for closing brackets
        print("Closing",stack)

        for br in s:
            if br == ")":
                if "(" in stack:
                    stack = stack.replace("(", "")

            elif br == "]":
                if "[" in stack:
                    stack = stack.replace("[", "")
            elif br == "}":
                if "{" in stack:
                    stack = stack.replace("{", "")

        print("Finale", stack)
        return stack == ""

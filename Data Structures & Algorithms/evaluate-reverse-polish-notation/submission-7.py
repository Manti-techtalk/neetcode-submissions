from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        signs = {"*","/","+","-"}
        for val in tokens:
            print(val)
            if val in signs:
                if val == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
                    print("Added",stack)
                elif val == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                    print("Minus")
                elif val == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a * b)
                    print("Multiplied")
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b // a))
            else:
                stack.append(int(val))


        return stack[-1]

        
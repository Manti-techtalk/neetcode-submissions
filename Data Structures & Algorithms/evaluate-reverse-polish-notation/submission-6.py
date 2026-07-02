class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            #print(token)
            signs = {'*','/','+','-'}
            if token in signs:
                print("sign",token)
                a = stack.pop()
                b = stack.pop()
                if token =='+':
                    total = a + b
                    stack.append(total)
                elif token == '-':
                    difference = b - a
                    stack.append(difference)
                elif token == '*':
                    product = a * b
                    stack.append(product)
                else:
                    dividend = int(b/a)
                    stack.append(dividend)
            else:
                print("Number -->", token)
                # add this number to the stack
                stack.append(int(token))
        return int(stack[-1]) 
class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()

                if token == "+":
                    stack.append(b + a)
                elif token == "-":
                    stack.append(b - a)
                elif token == "*":
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))  # truncate toward zero

        return stack[0]

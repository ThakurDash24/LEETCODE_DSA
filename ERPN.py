from typing import List 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for x in tokens:
            if x in {'+', '-', '*', '/'}:
                b = stk.pop()
                a = stk.pop()
                if x == '+':
                    stk.append(a + b)
                elif x == '-':
                    stk.append(a - b)
                elif x == '*':
                    stk.append(a * b)
                elif x == '/':
                    stk.append(int(a / b))  # Truncate toward zero
            else:
                stk.append(int(x))
        return stk[-1]

            
solver = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
output = solver.evalRPN(tokens)
print(output)
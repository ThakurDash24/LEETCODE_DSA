from typing import List 
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for x in operations:
            if x == "+":
                stk.append(stk[-1] + stk[-2])
            elif x == "D":
                stk.append(2 * stk[-1])
            elif x == "C":
                stk.pop()
            else:
                stk.append(int(x))  # Convert string to int before appending
        return sum(stk)
    
solver =Solution()
op = ["5","-2","4","C","D","9","+","+"]
output = solver.calPoints(op)
print(output)
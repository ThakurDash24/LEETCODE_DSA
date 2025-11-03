class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['[','(','{']
        closing = [']',')','}']
        matching = {'}':'{',']':'[',')':'('}
        stk = []
        for x in s :
            if x in opening :
                stk.append(x)
            elif x in closing :
                if not stk :
                    return False 
                if stk[-1] == matching[x]:
                    stk.pop()
                else :
                    return False 
            else :
                return False 
        return len(stk) == 0 
            
solver = Solution()
s = "([])"
output = solver.isValid(s)
print(output)
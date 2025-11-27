class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        # Base Case 1: Simple addition
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        # Base Case 2: Handling single 9 (e.g., [9] -> [1, 0])
        elif n == 1:
            return [1, 0]
        # Recursive Step: Carry over to the left
        else:
            # Recurse on the left part, and append 0 to the end
            return self.plusOne(digits[:-1]) + [0]


#NOTE

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Iterate backwards from the last index
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If digit is 9, set it to 0 and continue loop (carry 1)
            digits[i] = 0
            
        # If loop finishes, it means all were 9s (e.g., 999 -> 000)
        # We need to prepend 1
        return [1] + digits

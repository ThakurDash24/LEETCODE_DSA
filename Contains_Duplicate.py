from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_counts={}
        for num in nums :
            if num in num_counts :
                num_counts[num] += 1
                return True
            else :
                num_counts[num] = 1
        return False 
    
solver = Solution()
nums = [1,2,3,1]
output = solver.containsDuplicate(nums)
print(output)
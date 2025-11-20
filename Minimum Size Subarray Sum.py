class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_window = float('inf') 
        summ = 0
        for right in range(len(nums)):
            summ += nums[right]
            while summ >= target :
                min_window = min(min_window , right - left + 1)
                summ -= nums[left]
                left += 1 
        if min_window == float('inf') :
            return 0
        else : 
            return min_window 
                    
            

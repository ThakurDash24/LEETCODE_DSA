class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0 
        right = 0
        zero_counts = 0
        max_length = 0
        length = 0
        while right < len(nums) :
            if nums[right] == 0 :
                zero_counts += 1
            while zero_counts > k :
                if nums[left] == 0 :
                    zero_counts -= 1
                left += 1   
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length

            

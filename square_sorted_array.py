from typing import List
def sortedSquares(nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        
        # The result array, which will be filled from the end
        result = [0] * n 
        write_idx = n - 1 # Pointer for filling the result array (starts at the end)
        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]
            # Compare the squared values at the two pointers
            if left_sq > right_sq:
                # The square of the number at the left end is larger.
                # This is the largest value to place next in our result array.
                result[write_idx] = left_sq
                left += 1  # Move the left pointer inwards
            else:
                # The square of the number at the right end (or they are equal) is larger.
                result[write_idx] = right_sq
                right -= 1 # Move the right pointer inwards
            # Move the writing pointer to the next position (to the left)
            write_idx -= 1       
        return result

nums = [-4,-1,0,3,10]
res=sortedSquares(nums)
print(res)
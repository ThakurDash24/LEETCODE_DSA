class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # 1. Initialize the answer array (O(1) extra space because 
        # the output array does not count as extra space).
        # We will use 'answer' to store the Left Products first.
        answer = [1] * n

        # === PASS 1: Calculate Left Products ===
        # answer[i] will store the product of all elements to the left of i.
        
        # 'current_product' starts at 1 (the product to the left of index 0).
        current_product = 1
        for i in range(n):
            # The current answer[i] is the product of everything to the left of nums[i].
            answer[i] = current_product
            
            # Update current_product for the next iteration (i+1)
            current_product *= nums[i]

        # === PASS 2: Incorporate Right Products ===
        # 'current_product' is reset to 1 (the product to the right of the last index).
        current_product = 1
        for i in range(n - 1, -1, -1):
            # answer[i] currently holds the LEFT product.
            # Multiply it by the RIGHT product (current_product).
            answer[i] *= current_product
            
            # Update current_product to include nums[i] for the next iteration (i-1).
            current_product *= nums[i]
            
        return answer

# Example-Based Learning:
# Input: nums = [1, 2, 3, 4]

# Pass 1 Walkthrough:
# i=0: answer[0] = 1, current_product = 1 * 1 = 1
# i=1: answer[1] = 1, current_product = 1 * 2 = 2
# i=2: answer[2] = 2, current_product = 2 * 3 = 6
# i=3: answer[3] = 6, current_product = 6 * 4 = 24
# After Pass 1: answer = [1, 1, 2, 6] (All Left Products)

# Pass 2 Walkthrough:
# i=3 (n-1): answer[3] = 6 * 1 = 6, current_product = 1 * 4 = 4
# i=2: answer[2] = 2 * 4 = 8, current_product = 4 * 3 = 12
# i=1: answer[1] = 1 * 12 = 12, current_product = 12 * 2 = 24
# i=0: answer[0] = 1 * 24 = 24, current_product = 24 * 1 = 24
# Final Output: [24, 12, 8, 6]

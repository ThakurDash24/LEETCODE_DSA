class Solution(object):
    def searchInsert(self, nums, target):
        L = 0 
        R = len(nums) - 1 
        while L <= R :
            mid = (L + R)/2
            if(target > nums[mid]):
                L = mid+1
            else : 
                R = mid - 1 
        if (target == nums[mid]):
            return mid 
        else : 
            return L
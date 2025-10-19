class Solution(object):
    def search(self, nums, target):
        L = 0 
        R = len(nums)-1
        while L <= R : 
            mid = (L + R)/2 
            if nums[mid] < target :
                L = mid+1 
            else : 
                R = mid-1 
            if nums[mid]==target : 
                return mid
             
        if nums[mid]==target : 
                return mid
        else : 
            return -1
                
            
        
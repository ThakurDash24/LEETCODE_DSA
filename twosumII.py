class Solution(object):
    def twoSum(self, numbers, target):
        L = 0 
        R = len(numbers) - 1 
        output = []
        while (L < R ):
            sum = numbers[L] + numbers[R] 
            if sum == target :
                return [L+1 , R+1]
            if ( sum < target):
                L += 1 
            else :
                R -= 1 
            
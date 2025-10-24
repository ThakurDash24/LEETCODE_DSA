class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        solution = []
        for i in range(len(nums)-2) :
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1
            target = -nums[i]
            while (L < R ):
                summ=nums[L]+nums[R]
                if(summ==target):
                    solution.append([nums[i],nums[L],nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L-1]:
                        L +=1
                    while L < R and nums[R] == nums[R+1]:
                        R -=1
                elif(summ<target):
                    L += 1
                else :
                    R -= 1
        return solution

solver = Solution()
A = [-1,0,1,2,-1,-4]
result=solver.threeSum(A)
print(result)
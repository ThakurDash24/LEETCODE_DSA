
def summaryRanges(nums):
        if not nums:
            return []
        start = 0
        result = []
        n = len(nums)
        for i in range (1,n+1) :
            if(i==n or nums[i]!=nums[i-1]+1):
                a = nums[start]
                b = nums[i-1]
                if a == b:
                    result.append(str(a))
                else : 
                    result.append(f"{a}->{b}")
                if i < n :
                    start = i
        return result

nums = [0,1,2,4,5,7]
result=summaryRanges(nums)
print(result)
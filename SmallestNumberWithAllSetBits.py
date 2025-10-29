class Solution(object):
    def smallestNumber(self, n):
        sum = 0
        if (n == 1 ) : 
            return 1
        for i in range(0,n):
            if sum < n : 
                sum += 2**i 
            else :
                return sum

solver = Solution()
n = 10
output = solver.smallestNumber(n)
print(output)
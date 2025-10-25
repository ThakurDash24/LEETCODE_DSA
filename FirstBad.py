# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
SECRET_FIRST_BAD = 20140

def isBadVersion(version: int) -> bool:
    """
    This function simulates the LeetCode API.
    Returns True if the 'version' is bad, based on the SECRET_FIRST_BAD.
    """
    return version >= SECRET_FIRST_BAD

class Solution(object):
    def firstBadVersion(self, n):
        l = 1 
        r = n
        while l < r :
            mid = (l+r)//2
            if(isBadVersion(mid) == True):
                r = mid 
            elif(isBadVersion(mid) == False):
                l = mid+1
        return l

solver = Solution()
n = 2126753390
firstBad=solver.firstBadVersion(2126753390)
print(f"{firstBad} , Iske baad se chude hai bhai")
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t
    
solver = Solution()
s = "anagram"
t = "anagram"   
output = solver.isAnagram(s,t) 
print(output)
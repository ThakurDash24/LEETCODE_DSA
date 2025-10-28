class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in set(ransomNote):
            if ransomNote.count(char) > magazine.count(char):
                return False 
        return True
    
solver = Solution()
ransomNote = "ababa"
magazine = "bababababbaba"
output = solver.canConstruct(ransomNote,magazine)
print(output)
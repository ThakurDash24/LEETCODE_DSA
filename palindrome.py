class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Normalize the string: remove non-alphanumeric and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True 

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(sol.isPalindrome("race a car"))                      # Output: False
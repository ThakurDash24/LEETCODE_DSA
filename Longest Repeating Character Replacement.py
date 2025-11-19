class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = Counter()
        l = 0 
        max_length = 0
        max_freq = 0
        for r in range(len(s)):
            freq_map[s[r]] += 1 
            max_freq = max(max_freq , freq_map[s[r]])
            window = r - l + 1
            if window - max_freq > k :
                freq_map[s[l]] -= 1 
                l += 1 
            max_length = max(max_length,r-l+1)
        return max_length

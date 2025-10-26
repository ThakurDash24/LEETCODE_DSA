class Solution:
    def numJewelsInStones(self,jewels: str, stones: str) -> int:
        stone_counts = {}
        for stone in stones:
            if stone in stone_counts:
                stone_counts[stone] += 1
            else:
                stone_counts[stone] = 1

        total_jewels_count = 0
        for jewel in jewels:
            if jewel in stone_counts:
                total_jewels_count += stone_counts[jewel]

        return total_jewels_count
    
sovler = Solution()
jewels = "aA"
stones = "aAAbbbb"
output = sovler.numJewelsInStones(jewels,stones) 
print(f"{output} of jewels are available in the stone" )
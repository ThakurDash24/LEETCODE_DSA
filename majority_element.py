class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_map = Counter(nums)
        for x in counter_map : 
            if counter_map[x] > len(nums)/2 :
                return x
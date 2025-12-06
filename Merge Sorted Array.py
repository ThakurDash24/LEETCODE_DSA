class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left = 0 
        right = 0
        nums3 = []
        while left < m and right < n :
            if nums1[left] == nums2[right] :
                nums3.append(nums2[right])
                nums3.append(nums1[left])
                left += 1
                right += 1
            elif nums1[left] > nums2[right] :
                nums3.append(nums2[right])
                right += 1
            else :
                nums3.append(nums1[left])
                left += 1
        while left < m:
            nums3.append(nums1[left])
            left += 1
        while right < n :
            nums3.append(nums2[right])
            right += 1
        for i in range(len(nums1)):
            nums1[i] = nums3[i]
                
        

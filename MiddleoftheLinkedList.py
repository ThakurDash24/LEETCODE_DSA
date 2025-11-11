# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        curr = head
        length = 0 
        while curr :
            if curr :
                length += 1 
                curr = curr.next 
        mid = length // 2
        # if (length%2 == 0):
        #     mid = length // 2 
        # if (length%2 != 0):
        #     mid = (length // 2) + 1
        while mid :
            start = start.next 
            mid -= 1
        return start 
            

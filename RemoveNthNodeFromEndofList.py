# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head 
        while curr :
            length += 1
            curr=curr.next
        if length == 1 :
            return None
        if length == n :
            return head.next
        pos = length - n - 1
        curr = head
        while pos > 0 :
            curr = curr.next 
            pos -= 1
        curr.next = curr.next.next
        return head  

            

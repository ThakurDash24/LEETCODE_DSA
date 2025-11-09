# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        second = list2 
        dummy = ListNode()
        list3=dummy
        while first and second :
            if first.val == second.val :
                list3.next = first
                list3=list3.next
                first = first.next
            elif first.val < second.val :
                list3.next = first
                list3=list3.next
                first = first.next
            elif second.val < first.val :
                list3.next = second
                list3=list3.next 
                second = second.next
        if first:
            list3.next = first
        elif second:
            list3.next = second
        return dummy.next

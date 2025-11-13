"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head : 
            return None 
        curr = head 
        old_to_new = {}
        while curr :
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            curr = curr.next 
        curr = head
        while curr :
            copied_node = old_to_new[curr]
            if curr.next :
                copied_node.next = old_to_new[curr.next]
            else :
                copied_node.next = None 
            if curr.random : 
                copied_node.random= old_to_new[curr.random]
            curr = curr.next 
        return old_to_new[head] 
        

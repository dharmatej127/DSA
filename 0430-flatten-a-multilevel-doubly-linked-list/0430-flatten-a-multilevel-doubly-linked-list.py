"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # parent=head
        # while parent!=None:
        #     if parent.child!=None:
        #         child=parent.child
        #         sib=child
        #         while sib.next:
        #             sib=sib.next
        #         sib.next=parent.next
        #         if parent.next:
        #             parent.next.prev=sib
        #         parent.next=child
        #         child.prev=parent
        #         parent.child=None
        #     parent=parent.next
        # return head
        stack=[]
        curr=head
        while curr is not None:
            if curr.child is not None:
                if curr.next:
                    stack.append(curr.next)
                curr.next=curr.child
                curr.child=None
                curr.next.prev=curr
                # curr.next.prev=None
                # curr.next=None
            
            if curr.next is  None:
                if stack:
                    curr.next=stack.pop()
                    curr.next.prev=curr
            curr=curr.next
        
        return head
                    
            
                
                

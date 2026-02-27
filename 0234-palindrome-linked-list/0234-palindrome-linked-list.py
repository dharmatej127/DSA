# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        currentNode=slow.next
        slow.next=None

        current=currentNode
        prev=None
        while current:
            currentNext=current.next
            current.next=prev
            prev=current
            current=currentNext
        head2=prev

        current1=head
        current2=head2
        while current2:
            if current1.val!=current2.val:
                return False
            current1=current1.next
            current2=current2.next
            
        return True
        

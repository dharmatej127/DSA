"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # if root is not None:
        #     return None
        # else:
        #     if root.left :
        #         root.left.next=root.right
        #     if root.right and root.right.next:
        #         root.right.next=root.next.right
        # if root.right is not None
        # self.connect(root.left)
        # self.connect(root.right) 
        # return root
        parent=root
        dummy=Node()
        
        while parent:
            curr=parent
            child = dummy

            while curr:
                if curr.left:
                    child.next=curr.left
                    child=child.next
                if curr.right:
                    child.next=curr.right
                    child=child.next
                curr=curr.next
            parent=dummy.next
            dummy.next=None
        return root
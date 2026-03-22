# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def successor (self,root):
        root = root.right
        while root.left is not None:
            root = root. left
        return root.val
    def predecessor (self,root) :
        root = root. left
        while root.right is not None:
            root = root.right
        return root.val
    
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        #base case
        if root is None :
            return None
        #searching for to key to delete
        if key > root.val:
            root.right=self.deleteNode(root.right, key)
        elif key<root.val:
            root.left=self.deleteNode(root.left, key)
        
        else:
            #case 1-leaf Node we have delete
            if root.left is None and root.right is None:
                root=None
            #case-2 - Non leaf node deletion
            elif root.right is not None :
                root.val = self.successor(root)
                root.right = self. deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left,root.val)
        return root
        


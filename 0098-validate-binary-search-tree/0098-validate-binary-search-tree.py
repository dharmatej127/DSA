# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def Inorder(self,node):
        if node.left:
            self.Inorder(node.left)
        self.res.append(node.val)
        if node.right:
            self.Inorder(node.right)
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
    
        if root is None:
            return 
        self. res=[]
        self.Inorder(root)
        n=len(self.res)
        for i in range(n-1):
            if self.res[i]>=self.res[i+1]:
                return False
        return True
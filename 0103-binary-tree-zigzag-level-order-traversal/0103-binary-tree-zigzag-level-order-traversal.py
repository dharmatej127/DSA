# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # res=[]
        # def add(i,tree):
            
        #     if len(res)<=i:
        #         res.append([tree.val])
        #     else:
        #         res[i].append(tree.val)
        #     i+=1
        #     if tree.left:
        #         add(i,tree.left)
        #     if tree.right:
        #         add(i,tree.right)
        # if root :
                
        #     add(0,root)

        # for i in range(len(res)):
        #     if i%2!=0:
        #         res[i].reverse()
        # return res

        res=[]
        def traverse_count(node,depth=0):
            if not node:
                return 
            if depth>=len(res):
                res.append([])
            if depth%2==0:
                res[depth].append(node.val)
            else:
                res[depth].insert(0,node.val)
            traverse_count(node.left,depth+1)
            traverse_count(node.right,depth+1)
        traverse_count(root)
        return res
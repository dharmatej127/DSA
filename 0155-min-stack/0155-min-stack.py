class MinStack(object):

    def __init__(self):
        self.stack=[]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)


    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack)<1:
            return 
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        # temp=self.s tack.pop()
        # if self.stack[-1]<=temp:
        #     min_ele=
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
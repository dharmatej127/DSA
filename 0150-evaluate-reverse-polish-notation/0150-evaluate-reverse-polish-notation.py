class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for i in tokens:
            if i=='+':
                if len(stack)>=2:
                    x=stack.pop()
                    y=stack.pop()
                    stack.append(x+y)
                
            elif i=='*':
                if len(stack)>0:
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y * x)
                    # x=stack.pop()
                    # sum*=x
            elif i=='/':
                if len(stack)>=2:
                    x=stack.pop()
                    y=stack.pop()
                    stack.append(int(float(y)/x))
                            # if sum<0:
                            #     sum=0
    
            elif i=='-':
                    if len(stack)>0:
                        x = stack.pop()
                        y = stack.pop()
                        stack.append(y - x)
            else:
                stack.append(int(i))
        return stack[-1]

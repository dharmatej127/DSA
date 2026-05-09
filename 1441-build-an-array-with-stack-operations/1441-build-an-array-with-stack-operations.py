class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        # stack=[]
        # stream=[]
        # for i in range(1,n+1):
        #     if len(stack)==0:
        #         stack.append(i)
        #         stream.append('Push')
        #     else:
               
        #         if stack==target:
        #             return stream
        #         else:
        #             stack.append(i)
        #             stream.append('Push')
        #             if stack==target:
        #                 return stream
        #             if stack[-1]!=target[len(stack)-1]:
        #                 stack.pop()
        #                 stream.append('Pop')
        stack=[]
        stream=[]
        for i in range(1,n+1):
            if len(stack)==0:
                stack.append(i)
                stream.append('Push')
            else:
               
                if stack==target:
                    return stream
                if stack[-1]!=target[len(stack)-1]:
                        stack.pop()
                        stream.append('Pop')
                stack.append(i)
                stream.append('Push')
                if stack==target:
                    return stream
                if stack[-1]!=target[len(stack)-1]:
                    stack.pop()
                    stream.append('Pop')


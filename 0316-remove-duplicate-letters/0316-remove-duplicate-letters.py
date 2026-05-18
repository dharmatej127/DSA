class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        stack=[]
        vist=set()
        for i in s:
            dic[i]-=1

            if i in vist:
                continue

            while stack and stack[-1]>i and dic[stack[-1]]>0:
                vist.remove(stack.pop())
            stack.append(i)
            vist.add(i)
        return "".join(stack)

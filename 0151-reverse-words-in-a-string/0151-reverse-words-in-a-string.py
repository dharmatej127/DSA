class Solution:
    def reverseWords(self,s):
        s=s.strip()
        s1=[]
        s=s+" "
        j=0
        s2=""
        for i in range(len(s)):
            s=s.lstrip()
            if s[i]==" ":
                # s2+=s[j:i]+" "
                s1.append(s[j:i])
                j=i+1
        
        for i in s1[::-1]:
            if i!="":
                s2+=str(i)+" "
        return s2.strip()
            
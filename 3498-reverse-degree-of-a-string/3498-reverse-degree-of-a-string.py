class Solution:
    def reverseDegree(self, s: str) -> int:
        n=len(s)
        alp=26
        prod_sum=0
        i=0
        while i<len(s):
            res=ord(s[i])-alp
            val=ord('a')-res
            i+=1
            prod_sum+=(i*val)
            
        return prod_sum
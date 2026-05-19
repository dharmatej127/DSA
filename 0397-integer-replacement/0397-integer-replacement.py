class Solution:
    def integerReplacement(self, n: int) -> int:
        i=0
        while n>1:
        
            if n ==3 :
                n-=1
                i+=1
            if n%2==0:
                # n=n//2
                n=n>>1
                i+=1
            elif str(bin(n))[-2:]=="01":
                n=(n-1)
                i+=1
            else:
                n=(n+1)
                i+=1
        
        return i
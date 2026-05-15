class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2: return 1
        if n==3: return 2
        mul=1
        while n>4:
            mul*=3
            n-=3
         
        mul*=n
        return mul


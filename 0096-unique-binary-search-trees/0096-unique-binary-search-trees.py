class Solution:
    
    # def __init__(self):
    #     self.vis={}
    def numTrees(self, n: int) -> int:
    #     if n==0 or n==1:
    #         return 1
    #     if n in self.vis:
    #         return self.vis[n]
    #     total=0
    #     for i in range(1,n+1):
    #         total+=self.numTrees(i-1)*self.numTrees(n-i)
    #     self.vis[n]=total
    #     return total\
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]
        return dp[n]
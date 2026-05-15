class Solution:
    def jump(self, nums: List[int]) -> int:
        # j,f,ce=0,0,0
        # for i in range(len(nums)-1):
        #     f=max(f,i+nums[i])
        #     if i==ce:
        #         j+=1
        #         ce=f
        # return j
        n=len(nums)
        dp=[float('inf')]*n
        dp[0]=0

        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if i+j<n:
                    # dp[j]=min(dp[j],dp[i]+1)
                    dp[i+j]=min(dp[i+j],dp[i]+1)
        return dp[-1]


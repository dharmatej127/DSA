class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        # for i in range(1,amount+1):
        #     for j in coins:
        #         if i+j>=0:
        #             dp[i]=min(dp[i],dp[i-j]+1)
        # return -1 if dp[amount]==float('inf') else dp[amount]
        # class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP table with a value larger than any possible answer
        # dp = [float('inf')] * (amount + 1)
        # dp[0] = 0 # Base case: 0 coins to make 0 amount
        
        for coin in coins:
            for i in range(coin, amount + 1):
                # Update the current amount if using this coin is better
                # dp[i - coin] represents the min coins for the remaining balance
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

        # for i in coins:
        #     for j in range(1,amount+1):
        #         if dp[i-1]!=float('inf'):
        #             dp[j]=min(dp[j],dp[j-i]+1)
        # return -1 if dp[amount]==float('inf') else dp[amount]
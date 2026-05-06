class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        bp=prices[0]
        for i in prices[1:]:
            cp=i
            if i<bp:
                bp=i
            maxProfit=max(maxProfit,cp-bp)
        return maxProfit

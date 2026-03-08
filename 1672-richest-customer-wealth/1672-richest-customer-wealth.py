class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest=0
        for cust in accounts:
            sum=0
            for money in cust:
                sum+=money
            if sum>=richest:
                richest=sum
        if richest >0:
            return richest
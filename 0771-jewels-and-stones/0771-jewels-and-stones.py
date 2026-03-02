class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        if len(stones)<1:
            return 0
        count=0
        for i in range(len(stones)):
            if stones[i] in jewels:
                count+=1
        return count
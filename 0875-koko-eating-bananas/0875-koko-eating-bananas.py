class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low=1
        high=max(piles)
        res=high
        while low<=high:
            mid=low+(high-low)//2
            if self.isPossible(piles,h,mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
    def isPossible(self,piles,h,mid):
        hours=0
        for ele in piles:
            hours+=(ele+mid-1)//mid
        return hours<=h

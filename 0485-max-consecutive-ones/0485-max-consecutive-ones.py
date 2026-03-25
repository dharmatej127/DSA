class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        max_1=0
        for i in nums:
            if i==1:
                count+=1
            elif i==0:
                count=0
            if max_1<=count:
                max_1=count
        return max_1


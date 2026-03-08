class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<2:
            return 
        result=[]
        for i in range(min(nums),max(nums)):
            if i in nums:
                pass
            else:
                result.append(i)
        return result
            

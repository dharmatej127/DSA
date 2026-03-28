class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum=[]
        rightsum=[]
        for i in range(len(nums)):
            leftsum=nums[:i]
            rightsum=nums[i+1:]
            if sum(leftsum)==sum(rightsum):
                return i
        return -1
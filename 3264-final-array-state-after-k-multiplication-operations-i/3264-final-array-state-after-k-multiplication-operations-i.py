class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        i=0
        while i<k:
            nums[nums.index(min(nums))]=multiplier*nums[nums.index(min(nums))]
            i+=1
        return nums
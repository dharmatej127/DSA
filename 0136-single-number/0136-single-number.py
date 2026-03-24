class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Xor=0
        for i in nums:
            Xor^=i
        return Xor
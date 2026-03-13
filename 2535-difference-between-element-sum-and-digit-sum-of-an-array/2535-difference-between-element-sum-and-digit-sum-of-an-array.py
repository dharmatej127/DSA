class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele_sum=0
        digit_sum=0
        for i in nums:
            ele_sum+=i
        
            while i:
                rem=i%10
                digit_sum+=rem
                i//=10
        return ele_sum-digit_sum
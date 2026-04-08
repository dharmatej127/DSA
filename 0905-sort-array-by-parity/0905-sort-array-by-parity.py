class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2=[]
        nums3=[]
        for i in nums:
            if i%2==0:
                nums2.append(i)
            if i%2!=0:
                nums3.append(i)
        return nums2+nums3

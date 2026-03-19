class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c_red=0
        c_white=0
        c_blue=0
        for i in nums:
            if i ==0:
                c_red+=1
            elif i==1:
                c_white+=1
            else:
                c_blue+=1
        for i in range(len(nums)):
            if c_red>0:
                nums[i]=0
                c_red-=1
            elif c_white>0:
                nums[i]=1
                c_white-=1
            elif c_blue>0:
                nums[i]=2
                c_blue-=1
        return nums
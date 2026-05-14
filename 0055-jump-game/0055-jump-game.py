class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        # """ 
        # max_reach=0
        # for i in range(len(nums)):
        #     if (i>max_reach):
        #         return False
        #         break
        #     max_reach = max(max_reach, i + nums[i])
            
        # return True
        # i=0
        # while i>len(nums):
        #     if i<=len(nums):
        #         i=nums[i]
        #     if i<len(nums):
        #         return False
        # return True
        traget=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=traget:
                traget=i
        if traget==0:
            return True
        else:
            return False
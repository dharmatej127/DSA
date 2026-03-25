class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if target ==0 :
        #     return 0
        # if nums[0]==0 and target ==1:
        #     return 1
        # elif target ==1:
        #     return 0

        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1

        return left
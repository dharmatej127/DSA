class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if mid%2==1:
                mid-=1
            
            if nums[mid]==nums[mid+1]:
                left=mid+2
            else:
                right=mid
        
        return nums[left]
        # freq={}
        # for i in nums:
        #     freq[i]=freq.get(i,0)+1
        # asc=dict(sorted(freq.items(),key=lambda item: item[1] ))
        # if list(asc.values())[0]==1:
        #     return list(asc.keys())[0]
        # return asc
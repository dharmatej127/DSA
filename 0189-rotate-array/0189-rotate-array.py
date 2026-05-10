class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        a=[]
        # if k<len(nums):
        #     return (a[-k:]+a[:-k])
        i=0
        j=len(nums)-1
        while i<k:
            a.append(nums[j])
            j-=1
            i+=1
        a.reverse()
        i=0
        while i<=j:
            a.append(nums[i])
            i+=1
        
    
        nums[:]=a
        return nums
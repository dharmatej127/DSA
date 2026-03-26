class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        i=0
        j=n
        res=[]
        while j<len(nums):
            res.append(nums[i])
            i+=1
            res.append(nums[j])
            j+=1
        return res
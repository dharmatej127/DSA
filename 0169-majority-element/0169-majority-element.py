class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max_num,count =0,0
        for n in nums:
            if count==0:
                Max_num=n
            if n==Max_num:
                count+=1
            else:
                count-=1
        return Max_num
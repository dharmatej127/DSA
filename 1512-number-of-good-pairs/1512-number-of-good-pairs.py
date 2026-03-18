class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # i,j=0,len(nums)-1
        # pair=0
        # while i<len(nums):
            
        #     if nums[i]!=nums[j]:
        #         # if i==len(nums)-1:
        #         #     return pair
        #         if i+1>=j:
                    
        #             i+=1
        #             j=len(nums)-1
        #         j-=1
        #     else:
        #         # if i==j:
        #         #     return 0
        #         pair+=1
        #         if i+1>=j:
        #             i+=1
        #             j=len(nums)-1
        #         j-=1
        # return pair
        # number of good pairs
        dict={}
        num=0
        for i in nums:
            if i in dict:
                if dict[i]==1:
                    num+=1
                else:
                    num+=dict[i]
                dict[i]+=1
            else:
                dict[i]=1
        return num
            

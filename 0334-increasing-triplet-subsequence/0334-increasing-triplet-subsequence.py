class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]<nums[j]<nums[k]:
        #                 return True
        # return False

        first=second=float("inf")
        for i in nums:
            if i<=first:
                first=i
            elif i<=second: 
                second=i
            else:  
                return True
        return False
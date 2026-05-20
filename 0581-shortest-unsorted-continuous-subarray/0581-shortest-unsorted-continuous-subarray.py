class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp=sorted(nums)
        r=0
        l=len(nums)
        for i in range(len(nums)):

            if temp[i]!=nums[i] :

                r=max(i,r)
                l=min(i,l)
        if r-l<0: return 0
        return (r-l)+1
            


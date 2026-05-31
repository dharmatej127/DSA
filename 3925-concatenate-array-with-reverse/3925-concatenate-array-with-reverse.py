class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        res=[]
        i=0
        while i<(len(nums)*2):
            if i <len(nums):
                # print(i)
                res.append(nums[i])
              
            else:
                res.append(nums[-(i-(len(nums)-1))])
            # print(i)
            i+=1
        return res
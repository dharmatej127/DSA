class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, res):
            if i==len(nums):
                res.append(nums[:])
                return
            for j in range(i, len(nums)): # for choice in choices
                nums[i], nums[j] = nums[j], nums[i] # make a move
                backtrack(i+1, res)      # backtrack
                nums[i], nums[j] = nums[j], nums[i] # undo the move 

        #--------------
        res = []
        backtrack(0, res)
        return res



            
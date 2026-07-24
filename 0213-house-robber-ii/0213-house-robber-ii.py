class Solution:
    

       
    def rob_solve(self, houses):
        rob1, rob2 = 0, 0
            
        for house in houses: 
            new_max = max(rob2, rob1 + house)

            rob1=rob2
            rob2=new_max

        return rob2
                
    def rob(self, nums: list[int]) -> int:
    
        if len(nums) == 1:
            return nums[0]

        return max(self.rob_solve(nums[:-1]), self.rob_solve(nums[1:]))

class NumArray:

    def __init__(self, nums):
        self.nums=nums
    def sumRange(self, left: int, right) -> int:
        self.left=left
        self.right=right
        sum=0
        for i in range(self.left,self.right+1):
            sum=sum+(self.nums[i])
        return sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
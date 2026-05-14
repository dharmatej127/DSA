class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum = nums[0]
        minsum = nums[0]
        totalsum = nums[0]
        curmaxsum = nums[0]
        curminsum = nums[0]

        for i in range(1, len(nums)):
            totalsum += nums[i]

            curmaxsum = max(curmaxsum+nums[i], nums[i])
            maxsum = max(curmaxsum, maxsum)

            curminsum = min(curminsum+nums[i], nums[i])
            minsum = min(curminsum, minsum)


        val = (totalsum-minsum)
        if val==0:
            return maxsum
        else:
            return max(val, maxsum)
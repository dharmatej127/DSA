class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = float('-inf')
        sec_max = float('-inf')
        index = 0

        for i, num in enumerate(nums):
            if num > sec_max:
                if num > max_val:
                    sec_max = max_val
                    max_val = num
                    index = i
                else:
                    sec_max = num

        return index if max_val >= 2 * sec_max else -1
        # m=max(nums)
        # for i in nums:
        #     i=2*i
        #     if i!=m:
        #         return -1
        #     return nums.index(m)

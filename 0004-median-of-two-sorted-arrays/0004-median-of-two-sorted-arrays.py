class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # import numpy
        # x = numpy.median((nums1+nums2))
        # return x 
        nums = sorted(nums1+nums2)
        n = len(nums)
        if n % 2 == 0:
            m=((nums[n//2-1] + nums[n//2]) )/ 2
            return m
        else:
            return nums[n//2]
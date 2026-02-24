class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # sum1,sum2=0,0
        # for i in range(len(nums2)):
        #     sum1+=nums1[i]
        #     sum2+=nums2[i]
        # if sum1<=sum2:
        #     m=(abs(sum1-sum2))//len(nums1)
        #     return m
        # else:
        #     n=sum2-sum1
        #     return n
        a = max(nums1)
        b = max(nums2)
        return(b-a)
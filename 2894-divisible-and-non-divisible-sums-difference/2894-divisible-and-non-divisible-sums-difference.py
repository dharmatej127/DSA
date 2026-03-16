class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        divisible_sum=0
        notdivisible_sum=0
        for i in range(1,n+1):
            if i%m!=0:
                notdivisible_sum+=i
            else:
                divisible_sum+=i
        return notdivisible_sum-divisible_sum

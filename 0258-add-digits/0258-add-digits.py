class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # while num>=10:

        #     sum=0
        #     while num>0:
        #         rem=num%10
        #         sum+=rem
        #         num=num//10
        #     num=sum
        # # return num
        # if num==0:
        #     return 0
        # return 1+(num-1)%9
        if num==0:
            return 0
        if num%9==0:
            return 9
        return num%9
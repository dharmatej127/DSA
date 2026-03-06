class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        sign=""
        if num<0:
            sign = "-"
        else:
            ""
        result=""
        num=abs(num)
        while num:
            result=str(num%7)+result
            num//=7
        return sign + result
            
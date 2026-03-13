class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        for i in range(len(s)):
            if s[i]=='6':
                s=s.replace(s[i],'9',1)
                break
            else:
                continue
        return int(s)

        
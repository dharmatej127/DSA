class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        mul=1
        j=1
        for i in range(5,5+n):
            mul=(mul*i)//j
            j+=1
        return mul
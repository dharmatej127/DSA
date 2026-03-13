class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res=""
        if len(word1)>=len(word2):
            n=len(word1)
        else:
            n=len(word2)
        for i in range(n):
            try:
                res+=word1[i]+word2[i]
            except :
                if len(word1)<len(word2):
                    res+=word2[i:]
                    break
                else:
                    res+=word1[i:]
                    break
        return res

         
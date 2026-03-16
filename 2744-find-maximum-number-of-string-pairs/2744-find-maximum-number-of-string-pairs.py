class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        pairs=0
        for i in range(len(words)):
            if words[i][::-1] in words[i+1:]:
                pairs+=1
        return pairs
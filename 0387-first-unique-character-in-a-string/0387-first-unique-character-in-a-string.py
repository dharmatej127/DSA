class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        # """
        # for ch in s:
        #     if s.count(ch)==1:
        #         return s.index(ch)
        #         break

        # return -1

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch,0) + 1

        for i,ch in enumerate(s):
            if freq[ch] == 1:
                return i

        return -1
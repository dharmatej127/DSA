class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        li=[""]*len(s.split(" "))
        for i in s.split():
            # n=int(i[-1])-1
            # print(i[:-1])
            # li.insert(n,i[:-1])
            li[int(i[-1])-1]=i[:-1]
        return " ".join(li)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=sorted(s)
        s.append(" ")
        # print(s)
        t=sorted(t)
        # print(t)
        for i in range(len(s)):
            if s[i]!=t[i]:
                return t[i]

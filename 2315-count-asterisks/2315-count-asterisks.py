class Solution:
    def countAsterisks(self, s: str) -> int:
        counter=0
        inside=False
        for chr in s:
            if chr =='|':
                inside= not inside
            if chr=="*" and inside is False :
                counter+=1
        return counter

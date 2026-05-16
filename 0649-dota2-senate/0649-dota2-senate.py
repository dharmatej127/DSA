from collections import deque
class Solution(object):

    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """


        d=deque()
        r=deque()
        n=len(senate)
        for i in range(n):
            if senate[i]=="R":
                r.append(i)
            else:
                d.append(i)

        while d and r:
            radrem=r.popleft()
            dirrem=d.popleft()

            if radrem<dirrem:
                r.append(radrem+n)
            else:
                d.append(dirrem+n)
        return "Dire" if d else "Radiant"

        # count_dir=0
        # count_rad=0
        # for i in senate:
        #     if i =="R":
        #         count_rad+=1
        #     else:
        #         count_dir+=1


        # if count_dir>count_rad:
        #     return "Dire"
        # elif count_dir==count_rad:
        #     if senate[0]=="R":
        #         return "Radiant"
        #     else:
        #         return "Dire"
        # else:
        #     return "Radiant"

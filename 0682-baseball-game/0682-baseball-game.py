class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        for i in operations:
            if i=="D":
                score.append(2*score[-1])
            elif i=="C":
                if len(score)>0:
                    score.pop()
            elif i=="+":
                score.append((score[-2]+score[-1]))
            else:
                score.append(int(i))
        return sum(score)

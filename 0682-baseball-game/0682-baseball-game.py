class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result=[]
        for i in range(len(operations)):
            if operations[i]=="+":
                result.append(result[-1]+result[-2])
            elif operations[i]=="D":
                result.append(result[-1]*2)
            elif operations[i]=="C":
                result.pop()
            else:
                result.append(int(operations[i]))
        return sum(result)

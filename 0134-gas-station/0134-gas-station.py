class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n=len(gas)
        tank=0
        d=0
        if sum(gas)<sum(cost):
            return -1
        start=0
        # for car in range(len(gas)):
        #     if gas[car] > cost[car]:
        #         tank=gas[car]
        #         start=car
        #         break
        # s=start 
        # while (start+1)!=s :
        #     if tank>cost[(start+1)%n]:
        #         tank=(tank-cost[start])+gas[(start+1)%n]

        #     if tank<0:
        #         return -1   
        #     start=(start+1)%n
        # tank=tank-cost[start]
        # if tank<0:
        #     return -1
        # else:
        #     return s

        for i in range(n):
            tank+=gas[i]-cost[i]
            d+=gas[i]-cost[i]
            if tank<0:
                start=i+1
                tank=0
        return start
                
    
            
                

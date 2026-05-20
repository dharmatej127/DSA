class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smin=arrays[0][0]
        smax=arrays[0][-1]
        diff=0
        for i in range(1,len(arrays)):
            currmin = arrays[i][0]
            currmax = arrays[i][-1]

            diff = max(diff,currmax-smin)
            diff = max(diff,smax-currmin)

            smin = min(smin,currmin)
            smax = max(smax,currmax)
        return diff
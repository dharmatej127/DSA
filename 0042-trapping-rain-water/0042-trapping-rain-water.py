class Solution:
    def trap(self, height: List[int]) -> int:
        i=1
        j=len(height)-2
        imax=height[i-1]
        jmax=height[j+1]
        waterCount=0
        while i<=j:
            if jmax<=imax:
                if height[j]<=jmax:
                    waterCount+=jmax-height[j]
                jmax=max(jmax,height[j])
                j-=1
            else:
                if height[i]<=imax:
                    waterCount+=imax-height[i]
                imax=max(imax,height[i])
                i+=1
        return waterCount

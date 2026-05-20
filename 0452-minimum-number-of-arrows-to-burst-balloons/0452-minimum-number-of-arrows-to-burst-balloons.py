class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        count=0
        end =points[0][1]
        arr=0
        left=0
        while left<len(points):
            end=points[left][1]
            right=left+1
            while right < len(points) and points[right][0] <= end:
                right +=1
            arr+=1
            left=right
        return arr

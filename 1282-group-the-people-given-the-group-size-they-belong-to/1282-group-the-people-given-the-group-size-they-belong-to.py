class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans={}
        res=[]
        for i ,x in enumerate(groupSizes):
            if x not in ans:
                ans[x]=[]
            ans[x].append(i)
            if len(ans[x])==x:
                res.append(ans[x])
                ans[x]=[]
        return res

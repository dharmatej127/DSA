class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        V=numCourses
        edges=prerequisites
        adj=[]
        inDegree=[0]*V
        for _ in range(V):
            adj.append([])
        for i in edges:
            adj[i[0]].append(i[1])
            inDegree[i[1]]+=1
        q=[]
        for i in range(len(inDegree)):
            if inDegree[i]==0:
                q.append(i)
        answer=[]
        while q:
            t=q.pop(0)
            answer.append(t)
            for i in adj[t]:
                inDegree[i]-=1
                if inDegree[i]==0:
                    q.append(i)
        if len(answer)!=V:
            return False
        else:
            return True
class Solution:
    def dfs(self,n,adj,vist,i):
        vist[i]=True
        nodes=1
        edges=len(adj[i])
        for j in adj[i]:
            if not vist[j]:
                n,e=self.dfs(n,adj,vist,j)
                nodes+=n
                edges+=e
        return nodes,edges

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[]
        for i in range(n):
            adj.append([])
        vist=[False]*n
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        countCompleteCompo=0
        for i in range(n):
            if not vist[i]:
                v,e=self.dfs(n,adj,vist,i)
                e=e//2
                if e==v*(v-1)//2:
                    countCompleteCompo+=1
        return countCompleteCompo

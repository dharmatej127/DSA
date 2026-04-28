class Solution:
    # def dfs(self,n,adj,vist,i):
        # vist[i]=True
        # nodes=1
        # edges=len(adj[i])
        # for j in adj[i]:
        #     if not vist[j]:
        #         n,e=self.dfs(n,adj,vist,j)
        #         nodes+=n
        #         edges+=e
        # return nodes,edges
    def bfs(self,n,adj,vist,i):
        q=[]
        q.append(i)
        vist[i]=True
        n=0
        v=0
        while q:
            temp=q.pop(0)
            n+=1
            v+=len(adj[temp])
            for i in adj[temp]:
                if not vist[i]:
                    vist[i]=True
                    q.append(i)
        return n,v//2

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
                v,e=self.bfs(n,adj,vist,i)
               
                if e==v*(v-1)//2:
                    countCompleteCompo+=1
        return countCompleteCompo

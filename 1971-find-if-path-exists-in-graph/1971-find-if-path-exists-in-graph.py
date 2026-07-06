class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    
        adjlist=[[] for _ in range(n)]
        for edge in edges:
            u=edge[0]
            v=edge[1]

            adjlist[u].append(v)
            adjlist[v].append(u)

        visited =[False]*n
        return self.dfs(source,visited,adjlist,destination)
    def dfs(self,node,visited,adjlist,destination):
        if node == destination:
            return True
        visited[node]=True

        for neighbor in adjlist[node]:
            if not visited[neighbor]:
                if self.dfs(neighbor,visited,adjlist,destination):
                    return True
        return False
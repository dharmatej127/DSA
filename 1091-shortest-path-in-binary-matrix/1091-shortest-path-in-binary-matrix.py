class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        vist=[]
        for i in range(n):
            vist.append([False]*n)
        vist[0][0]=True
        q=[]
        q.append([0,0])
        levels=0
        while q:
            l=len(q)
            levels+=1
            for _ in range(l):
                t=q.pop(0)
                i,j=t[0],t[1]
                if i==n-1 and j==n-1:
                    return levels
                child=[[i,j+1],[i,j-1],[i+1,j],[i-1,j],[i+1,j+1],[i+1,j-1],[i-1,j+1],[i-1,j-1]]
                for c in child:
                    ci=c[0]
                    cj=c[1]
                    if ci>=0 and ci<n and cj>=0 and cj<n and grid[ci][cj]==0 and not vist[ci][cj]:
                        vist[ci][cj]=True
                        q.append([ci,cj])
        return -1
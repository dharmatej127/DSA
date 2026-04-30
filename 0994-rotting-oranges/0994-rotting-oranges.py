class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=[]
        freshOranges=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append([i,j])
                if grid[i][j]==1:
                    freshOranges+=1
        if freshOranges==0:
            return 0
        time=0
        while q:
            l=len(q)
            time+=1
            for _ in range(l):
                t=q.pop(0)
                i,j=t[0],t[1]
                child =[[i,j+1],[i,j-1],[i+1,j],[i-1,j]]
                for c in child:
                    ci=c[0]
                    cj=c[1]
                    if ci>=0 and ci<n and cj>=0 and cj<m and grid[ci][cj]==1:
                        grid[ci][cj]=2
                        freshOranges-=1
                        q.append([ci,cj])
        if freshOranges ==0:
            return time-1
        else:
            return -1


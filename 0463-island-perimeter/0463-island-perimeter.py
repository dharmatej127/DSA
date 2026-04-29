class Solution:
    def dfs(self,grid,vist,start):
        i=start[0]
        j=start[1]
        vist[i][j]=True
        child=[[i,j+1],[i,j-1],[i+1,j],[i-1,j]]
        childCount=0
        for c in child:
            if c[0]>=0 and c[0]<len(grid) and c[1]>=0 and c[1]<len(grid[0]) and grid[c[0]][c[1]]==1:
                childCount+=1
        currentCellPerimeter=4-childCount
        otherCellPerimeter=0
        for k in child:
            ci=k[0]
            cj=k[1]
            if ci>=0 and ci<len(grid) and cj>=0 and cj<len(grid[0])and  grid[ci][cj] == 1 and not vist[ci][cj]:
                otherCellPerimeter+=self.dfs(grid,vist,[ci,cj])
        return otherCellPerimeter+currentCellPerimeter


    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vist=[]
        for _ in range(n):
            vist.append([False]*m)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return self.dfs(grid,vist,[i,j])
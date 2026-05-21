class Solution:
    def swap(self,row,i):
        if i + 1 >= len(row):
            return 0
        pair=row[i] ^ 1
        pos = i + 1
        while row[pos] != pair:
            pos += 1
        c = 1 if pos != i + 1 else 0
        if c:
            row[i + 1], row[pos] = row[pos],row[i +  1]
        return c +self.swap(row,i + 2)


    def minSwapsCouples(self, row: List[int]) -> int:
        
        return self.swap(row,0)
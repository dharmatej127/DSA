class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c=[0]*len(A)
        for i in range(len(A)):
            arr1=sorted(A[:i+1])
            arr2=sorted(B[:i+1])
            count=0
            for j in range(len(arr1)):
                
                if arr1[j] in arr2:
                    count+=1
                
            c[i]=count
        return c
                

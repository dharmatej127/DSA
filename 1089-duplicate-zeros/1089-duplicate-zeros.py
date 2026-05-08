class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        lis=[]
        for i in arr:
            if len(lis)<len(arr):
                lis.append(i)
            if i == 0 and len(lis)<len(arr):
                lis.append(0)
        for j in range(len(arr)):
            arr[j] = lis[j]
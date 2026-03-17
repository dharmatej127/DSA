class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        arr=[0]*(n)
        i=0
        xOr=0
        while i<len(arr):
            arr[i]=start+2*i
            xOr^=arr[i]
            i+=1
        return xOr

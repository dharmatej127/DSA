class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        minheap=[]
        for i in nums:
            minheap.append(i)
        heapq.heapify(minheap)
        while k>0:
            a=heapq.heappop(minheap)
            a+=1
            heapq.heappush(minheap,a)
            k-=1
        prod=1
        for i in minheap:
            prod=(prod*i)%1000000007
        return prod
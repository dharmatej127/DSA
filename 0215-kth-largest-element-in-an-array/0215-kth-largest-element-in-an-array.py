class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap=[]
        for i in nums:
            maxheap.append(-i)
        heapq.heapify(maxheap)
        while k-1>0:
            heapq.heappop(maxheap)
            k-=1
        return -heapq.heappop(maxheap)

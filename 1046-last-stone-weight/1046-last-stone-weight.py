
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[]
        for i in stones:
            maxheap.append(-i)
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            x=-heapq.heappop(maxheap)
            y=-heapq.heappop(maxheap)
            if x!=y:
                heapq.heappush(maxheap,-(x-y))
        if maxheap:
            return -maxheap[0]
        else:
            return 0

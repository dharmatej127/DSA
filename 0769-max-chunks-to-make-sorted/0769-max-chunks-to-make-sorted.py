class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # max_chunk=0
        # count=0
        # for i in range(len(arr)):
        #     max_chunk=max(max_chunk,arr[i])
        #     if max_chunk==i:
        #         count+=1
        # return count

        st=[]
        for x in arr:
            mx=x
            while st and st[-1]>x:
                mx=max(mx,st.pop())
            st.append(mx)
        return len(st)